"""Plugin system for extensibility."""

from typing import Any, Callable, Dict, List, Optional, Protocol
from pathlib import Path
import importlib.util
import yaml


class PluginHook(Protocol):
    """Protocol for plugin hooks."""

    async def on_register(self) -> None:
        """Called when plugin is registered."""
        ...

    async def on_pre_action(self, service: str, action: str, params: Dict[str, Any]) -> None:
        """Called before a service action."""
        ...

    async def on_post_action(
        self, service: str, action: str, params: Dict[str, Any], result: Any
    ) -> None:
        """Called after a service action."""
        ...

    async def on_teardown(self) -> None:
        """Called when plugin is unloaded."""
        ...


class Plugin:
    """Base class for plugins."""

    name: str = "base_plugin"
    version: str = "0.1.0"

    async def on_register(self) -> None:
        """Called when plugin is registered."""
        pass

    async def on_pre_action(self, service: str, action: str, params: Dict[str, Any]) -> None:
        """Called before a service action."""
        pass

    async def on_post_action(
        self, service: str, action: str, params: Dict[str, Any], result: Any
    ) -> None:
        """Called after a service action."""
        pass

    async def on_teardown(self) -> None:
        """Called when plugin is unloaded."""
        pass


class PluginManager:
    """Manages plugin lifecycle and execution."""

    def __init__(self) -> None:
        self._plugins: Dict[str, Plugin] = {}
        self._enabled: Dict[str, bool] = {}

    async def load_plugin(self, plugin_path: str) -> None:
        """Load a plugin from a Python file or YAML config."""
        path = Path(plugin_path)
        if not path.exists():
            raise ValueError(f"Plugin not found: {plugin_path}")

        if path.suffix == ".py":
            await self._load_python_plugin(path)
        elif path.suffix in (".yaml", ".yml"):
            await self._load_yaml_plugin(path)
        else:
            raise ValueError(f"Unsupported plugin format: {path.suffix}")

    async def _load_python_plugin(self, path: Path) -> None:
        """Load a Python plugin."""
        spec = importlib.util.spec_from_file_location(path.stem, path)
        if spec is None or spec.loader is None:
            raise ValueError(f"Cannot load plugin: {path}")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Find Plugin subclass
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (
                isinstance(attr, type)
                and issubclass(attr, Plugin)
                and attr is not Plugin
            ):
                plugin = attr()
                await self.register_plugin(plugin)
                break

    async def _load_yaml_plugin(self, path: Path) -> None:
        """Load a YAML plugin config (simplified)."""
        with open(path) as f:
            config = yaml.safe_load(f)

        # Create a simple plugin from YAML config
        plugin = Plugin()
        plugin.name = config.get("name", path.stem)
        plugin.version = config.get("version", "0.1.0")
        await self.register_plugin(plugin)

    async def register_plugin(self, plugin: Plugin) -> None:
        """Register a plugin."""
        self._plugins[plugin.name] = plugin
        self._enabled[plugin.name] = True
        await plugin.on_register()

    async def unload_plugin(self, name: str) -> None:
        """Unload a plugin."""
        if name in self._plugins:
            await self._plugins[name].on_teardown()
            del self._plugins[name]
            del self._enabled[name]

    def enable_plugin(self, name: str) -> None:
        """Enable a plugin."""
        if name in self._plugins:
            self._enabled[name] = True

    def disable_plugin(self, name: str) -> None:
        """Disable a plugin."""
        if name in self._plugins:
            self._enabled[name] = False

    async def execute_pre_action(
        self, service: str, action: str, params: Dict[str, Any]
    ) -> None:
        """Execute pre-action hooks."""
        for name, plugin in self._plugins.items():
            if self._enabled.get(name, False):
                await plugin.on_pre_action(service, action, params)

    async def execute_post_action(
        self, service: str, action: str, params: Dict[str, Any], result: Any
    ) -> None:
        """Execute post-action hooks."""
        for name, plugin in self._plugins.items():
            if self._enabled.get(name, False):
                await plugin.on_post_action(service, action, params, result)

    def list_plugins(self) -> List[Dict[str, str]]:
        """List all registered plugins."""
        return [
            {
                "name": plugin.name,
                "version": plugin.version,
                "enabled": str(self._enabled.get(plugin.name, False)),
            }
            for plugin in self._plugins.values()
        ]

// ===========================
// Mobile Menu Toggle
// ===========================

const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        mobileMenuToggle.classList.toggle('active');
    });
}

// ===========================
// Navbar Scroll Effect
// ===========================

const navbar = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    
    lastScroll = currentScroll;
});

// ===========================
// Tab Switching
// ===========================

const tabButtons = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        const targetTab = button.getAttribute('data-tab');
        
        // Remove active class from all buttons and contents
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));
        
        // Add active class to clicked button and corresponding content
        button.classList.add('active');
        const targetContent = document.querySelector(`.tab-content[data-tab="${targetTab}"]`);
        if (targetContent) {
            targetContent.classList.add('active');
        }
    });
});

// ===========================
// Copy Code to Clipboard
// ===========================

const copyButtons = document.querySelectorAll('.copy-btn');

copyButtons.forEach(button => {
    button.addEventListener('click', async () => {
        const codeText = button.getAttribute('data-copy');
        
        try {
            await navigator.clipboard.writeText(codeText);
            
            // Visual feedback
            const originalHTML = button.innerHTML;
            button.innerHTML = `
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                    <path d="M3 8L6.5 11.5L13 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                Copied!
            `;
            button.classList.add('copied');
            
            setTimeout(() => {
                button.innerHTML = originalHTML;
                button.classList.remove('copied');
            }, 2000);
        } catch (err) {
            console.error('Failed to copy text: ', err);
            
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = codeText;
            textArea.style.position = 'fixed';
            textArea.style.opacity = '0';
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            
            try {
                document.execCommand('copy');
                button.innerHTML = `
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                        <path d="M3 8L6.5 11.5L13 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Copied!
                `;
                button.classList.add('copied');
                
                setTimeout(() => {
                    button.innerHTML = originalHTML;
                    button.classList.remove('copied');
                }, 2000);
            } catch (err) {
                console.error('Fallback: Failed to copy', err);
            }
            
            document.body.removeChild(textArea);
        }
    });
});

// ===========================
// Scroll Reveal Animation
// ===========================

const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
        }
    });
}, observerOptions);

// Observe all elements with scroll-reveal class
document.addEventListener('DOMContentLoaded', () => {
    const revealElements = document.querySelectorAll('.scroll-reveal');
    revealElements.forEach(el => observer.observe(el));
});

// ===========================
// Smooth Scroll for Anchor Links
// ===========================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        
        // Don't prevent default for just "#"
        if (href === '#') return;
        
        e.preventDefault();
        
        const target = document.querySelector(href);
        if (target) {
            const navbarHeight = navbar.offsetHeight;
            const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            if (navLinks && navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            }
        }
    });
});

// ===========================
// Animate Progress Bars on Scroll
// ===========================

const progressBars = document.querySelectorAll('.progress-fill');

const progressObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const bar = entry.target;
            const width = bar.style.width;
            bar.style.width = '0';
            
            setTimeout(() => {
                bar.style.width = width;
            }, 100);
            
            progressObserver.unobserve(bar);
        }
    });
}, { threshold: 0.5 });

progressBars.forEach(bar => {
    progressObserver.observe(bar);
});

// ===========================
// Feature Cards Animation on Scroll
// ===========================

const featureCards = document.querySelectorAll('.feature-card');

const featureObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.style.opacity = '1';
            }, index * 100);
            featureObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

featureCards.forEach(card => {
    featureObserver.observe(card);
});

// ===========================
// Parallax Effect for Hero Section
// ===========================

const heroBackground = document.querySelector('.hero-background');

window.addEventListener('scroll', () => {
    if (heroBackground && window.pageYOffset < window.innerHeight) {
        const scrolled = window.pageYOffset;
        heroBackground.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// ===========================
// Dynamic Stats Counter Animation
// ===========================

const stats = document.querySelectorAll('.stat-value');

const animateStats = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const stat = entry.target;
            const text = stat.textContent;
            
            // Simple animation for stats (you can enhance this)
            stat.style.opacity = '0';
            setTimeout(() => {
                stat.style.transition = 'opacity 0.5s ease-out';
                stat.style.opacity = '1';
            }, 100);
            
            observer.unobserve(stat);
        }
    });
};

const statsObserver = new IntersectionObserver(animateStats, { threshold: 0.5 });
stats.forEach(stat => statsObserver.observe(stat));

// ===========================
// Add Hover Effect to Cards
// ===========================

const cards = document.querySelectorAll('.feature-card, .demo-card, .community-card, .benchmark-card');

cards.forEach(card => {
    card.addEventListener('mouseenter', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const glow = document.createElement('div');
        glow.style.position = 'absolute';
        glow.style.left = `${x}px`;
        glow.style.top = `${y}px`;
        glow.style.width = '1px';
        glow.style.height = '1px';
        glow.style.background = 'radial-gradient(circle, rgba(99, 102, 241, 0.3) 0%, transparent 70%)';
        glow.style.borderRadius = '50%';
        glow.style.transform = 'translate(-50%, -50%) scale(0)';
        glow.style.transition = 'transform 0.6s ease-out, opacity 0.6s ease-out';
        glow.style.pointerEvents = 'none';
        glow.style.zIndex = '0';
        
        card.style.position = 'relative';
        card.style.overflow = 'hidden';
        card.appendChild(glow);
        
        requestAnimationFrame(() => {
            glow.style.transform = 'translate(-50%, -50%) scale(200)';
            glow.style.opacity = '0';
        });
        
        setTimeout(() => {
            if (glow.parentNode === card) {
                card.removeChild(glow);
            }
        }, 600);
    });
});

// ===========================
// Keyboard Navigation Enhancement
// ===========================

document.addEventListener('keydown', (e) => {
    // Tab navigation helper
    if (e.key === 'Tab') {
        document.body.classList.add('keyboard-nav');
    }
});

document.addEventListener('mousedown', () => {
    document.body.classList.remove('keyboard-nav');
});

// ===========================
// Performance Optimization: Debounce Scroll Events
// ===========================

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debounce to scroll-heavy operations
const debouncedScroll = debounce(() => {
    // Any additional scroll-based operations can go here
}, 10);

window.addEventListener('scroll', debouncedScroll);

// ===========================
// Easter Egg: Konami Code
// ===========================

let konamiCode = [];
const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

document.addEventListener('keydown', (e) => {
    konamiCode.push(e.key);
    konamiCode = konamiCode.slice(-10);
    
    if (konamiCode.join(',') === konamiSequence.join(',')) {
        // Easter egg activated!
        const stars = document.querySelector('.stars');
        if (stars) {
            stars.style.animation = 'twinkle 1s ease-in-out infinite';
            setTimeout(() => {
                stars.style.animation = 'twinkle 20s ease-in-out infinite';
            }, 5000);
        }
        
        // Show a fun message
        const message = document.createElement('div');
        message.textContent = '⭐ Starward activated! ⭐';
        message.style.position = 'fixed';
        message.style.top = '50%';
        message.style.left = '50%';
        message.style.transform = 'translate(-50%, -50%)';
        message.style.padding = '2rem 3rem';
        message.style.background = 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)';
        message.style.color = 'white';
        message.style.fontSize = '2rem';
        message.style.fontWeight = 'bold';
        message.style.borderRadius = '1rem';
        message.style.boxShadow = '0 20px 60px rgba(99, 102, 241, 0.5)';
        message.style.zIndex = '10000';
        message.style.opacity = '0';
        message.style.transition = 'opacity 0.5s ease-out';
        
        document.body.appendChild(message);
        
        requestAnimationFrame(() => {
            message.style.opacity = '1';
        });
        
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                document.body.removeChild(message);
            }, 500);
        }, 3000);
        
        konamiCode = [];
    }
});

// ===========================
// Initialize Tooltips (if needed in future)
// ===========================

function initTooltips() {
    const tooltipTriggers = document.querySelectorAll('[data-tooltip]');
    
    tooltipTriggers.forEach(trigger => {
        trigger.addEventListener('mouseenter', (e) => {
            const tooltipText = trigger.getAttribute('data-tooltip');
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = tooltipText;
            tooltip.style.position = 'absolute';
            tooltip.style.background = 'var(--bg-card)';
            tooltip.style.color = 'var(--text-primary)';
            tooltip.style.padding = '0.5rem 1rem';
            tooltip.style.borderRadius = 'var(--radius-md)';
            tooltip.style.fontSize = '0.875rem';
            tooltip.style.zIndex = '1000';
            tooltip.style.pointerEvents = 'none';
            tooltip.style.whiteSpace = 'nowrap';
            tooltip.style.boxShadow = 'var(--shadow-lg)';
            
            document.body.appendChild(tooltip);
            
            const rect = trigger.getBoundingClientRect();
            const tooltipRect = tooltip.getBoundingClientRect();
            
            tooltip.style.left = `${rect.left + rect.width / 2 - tooltipRect.width / 2}px`;
            tooltip.style.top = `${rect.top - tooltipRect.height - 10}px`;
            
            trigger._tooltip = tooltip;
        });
        
        trigger.addEventListener('mouseleave', () => {
            if (trigger._tooltip) {
                document.body.removeChild(trigger._tooltip);
                trigger._tooltip = null;
            }
        });
    });
}

// Initialize tooltips when DOM is ready
document.addEventListener('DOMContentLoaded', initTooltips);

// ===========================
// Console Welcome Message
// ===========================

console.log(
    '%c⭐ Starward %c- Deterministic Cloud Emulator',
    'font-size: 20px; font-weight: bold; background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;',
    'font-size: 14px; color: #a1a1aa;'
);
console.log(
    '%cInterested in contributing? Check out https://github.com/NickScherbakov/starward',
    'font-size: 12px; color: #6366f1;'
);

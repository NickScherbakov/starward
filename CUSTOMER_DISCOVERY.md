# Customer Discovery Plan for Starward

**Goal:** Interview 50 potential buyers to validate product-market fit before building features.

**Timeline:** Nov 11 - Dec 8, 2025 (4 weeks)

---

## 🎯 Ideal Customer Profile (ICP)

**Target Buyer:**
```yaml
Company:
  Stage: Series A/B (raised $5-30M)
  Team: 30-100 engineers
  Stack: Python/Node.js + AWS (S3, SQS, Lambda, DynamoDB)
  Pain: Slow CI/CD (30+ min), flaky tests, $10k+/mo AWS dev spend
  
Decision Maker:
  Title: VP Engineering, Engineering Manager, DevOps Lead
  Age: 28-45
  Background: Worked at tech companies, knows cloud pain
  Authority: Can approve $1-5k/month tools
  
Triggers:
  - Just raised funding (have budget)
  - Scaling team rapidly (hiring 5+ devs)
  - Migration to microservices (need better testing)
  - Compliance requirements (need isolated envs)
```  

---

## 📋 Target List: 50 Companies

### **Tier 1: Russian/CIS Startups (20 companies)**
*Easier to reach, respond in Russian, understand local context*

#### Fintech & Payments
1. **Rowi** - Series A, payment infrastructure, ~50 devs
   - LinkedIn: Search "VP Engineering Rowi"
   - Pain: Payment testing, PCI compliance envs
   
2. **Modulbank** - Acquired by Tinkoff but has independent dev team
   - Contact: DevOps Lead via LinkedIn
   - Pain: Banking regulations, isolated test environments

3. **CloudPayments** - Payment gateway, ~60 devs
   - Pain: Multi-environment testing, fraud detection

4. **Yandex.Money (YooMoney)** - If has small autonomous teams
   - Pain: High-volume transaction testing

5. **QIWI** - Wallet & payments (infrastructure team)
   - Pain: Legacy system integration testing

#### SaaS & Enterprise Tools
6. **Unisender** - Email marketing platform, ~40 devs
   - Pain: High-volume email simulation, deliverability testing

7. **SendPulse** - Multi-channel marketing automation
   - Pain: SMS/Email/Push testing across channels

8. **Carrot quest** - Customer messaging platform
   - Pain: Real-time messaging, webhook testing

9. **Aimylogic (Just AI)** - Conversational AI platform
   - Pain: NLP pipeline testing, multi-environment

10. **Acrobits** - VoIP/telephony (if dev team in CIS)
    - Pain: Telecom integration testing

#### E-commerce & Logistics
11. **Whoosh** - Delivery service, Series B, ~80 devs
    - Pain: Logistics simulation, real-time routing tests

12. **Samokat Tech** - Grocery delivery (if independent)
    - Pain: Inventory management, order orchestration

13. **Ozon Technology** - E-commerce platform teams
    - Pain: Microservices testing, high load simulation

14. **Wildberries Tech** - If accessible teams
    - Pain: Catalog management, search testing

#### DevTools & Infrastructure
15. **Qase.io** - Test management SaaS, remote team
    - Pain: "Eating own dog food" - testing their test platform

16. **GitVerse** - Russian GitHub alternative
    - Pain: CI/CD infrastructure, runner orchestration

17. **Yandex.Cloud** - Cloud provider (AWS competitor)
    - Pain: Ironically might use AWS internally for tooling

18. **Selectel** - Cloud/hosting provider
    - Pain: Multi-cloud testing

#### AI/ML & Data
19. **Just AI** - Conversational AI
    - Pain: Model deployment pipelines

20. **Neuronet** - ML platform (if exists)
    - Pain: Data pipeline testing

---

### **Tier 2: European Startups (15 companies)**
*English-speaking, faster decision cycles, higher budgets*

#### UK 🇬🇧
21. **Monzo** - Digital bank, ~800 devs (target small teams)
    - Contact: Team leads via LinkedIn
    - Pain: Microservices testing, compliance

22. **GoCardless** - Payments, Series E, ~250 devs
    - Pain: Payment reconciliation testing

23. **Revolut** - Fintech (infrastructure teams)
    - Pain: Multi-region deployments

24. **Veriff** - Identity verification
    - Pain: Document processing pipelines

#### Germany 🇩🇪
25. **N26** - Mobile bank, Series D
    - Pain: Banking compliance, isolated envs

26. **SumUp** - Payment processing
    - Pain: POS terminal integration testing

27. **Contentful** - Headless CMS, AWS-heavy
    - Pain: Content delivery, CDN testing

28. **Personio** - HR software
    - Pain: Data privacy (GDPR) testing

#### France 🇫🇷
29. **Qonto** - Business banking
    - Pain: Transaction testing, fraud detection

30. **Algolia** - Search API, heavy AWS usage
    - Pain: Search index testing, performance

31. **Ledger** - Crypto hardware wallets (backend team)
    - Pain: Blockchain integration testing

#### Netherlands 🇳🇱
32. **Mollie** - Payment service provider
    - Pain: Multi-currency, multi-method testing

33. **Adyen** - Payments (if smaller teams accessible)
    - Pain: Global payment methods simulation

#### Nordics 🇸🇪🇫🇮🇩🇰
34. **Epidemic Sound** - Music licensing, Sweden
    - Pain: Media processing pipelines

35. **Wolt** - Food delivery, Finland (DoorDash owned)
    - Pain: Real-time order orchestration

---

### **Tier 3: US Startups (10 companies)**
*Highest budgets, hardest to reach, validate pricing*

#### West Coast
36. **Plaid** - Fintech API, Series D
    - Pain: Bank integration testing

37. **Retool** - Internal tools platform
    - Pain: Database connectors testing

38. **Temporal** - Workflow orchestration
    - Pain: Testing their own product (ironic)

39. **Doppler** - Secrets management
    - Pain: Multi-environment secret sync

40. **Render** - Cloud platform (PaaS)
    - Pain: Infrastructure orchestration

#### East Coast
41. **Datadog** - Observability (DevOps teams)
    - Pain: Agent testing across clouds

42. **LaunchDarkly** - Feature flags
    - Pain: Multi-environment flag testing

43. **Astronomer** - Airflow platform
    - Pain: DAG testing, data pipelines

#### Remote-First
44. **GitLab** - DevOps platform
    - Pain: CI/CD runner testing

45. **HashiCorp** - Terraform (ironic - they need local cloud!)
    - Pain: Provider testing

---

### **Tier 4: Consultancies & Agencies (5 companies)**
*Can become resellers, multiple client projects*

46. **EPAM Systems** - Target DevOps practice leads
    - Pain: Client project setup speed
    - Opportunity: Resell to clients

47. **Luxoft** - Cloud migration teams
    - Pain: Migration testing before prod

48. **TEAM International** - AWS consulting practice
    - Pain: Demo environments for sales

49. **Andersenlab** - Cloud consulting (CIS focus)
    - Pain: Onboarding clients to AWS

50. **Reksoft** - DevOps services
    - Pain: Multi-client AWS management

---

## 🔍 Research Sources

### Finding Companies
- [ ] **Crunchbase:** Filter "Series A/B" + "Software" + "Raised last 2 years"
- [ ] **LinkedIn Sales Navigator:** "VP Engineering" + "50-100 employees" + "AWS"
- [ ] **AngelList/Wellfound:** Active job postings = growing team
- [ ] **vc.ru:** Russian startup funding news
- [ ] **TechCrunch:** European/US funding rounds
- [ ] **ProductHunt:** Recently launched products
- [ ] **AWS Case Studies:** Public AWS users
- [ ] **Y Combinator:** W24, S24, W25 batches

### Finding Contacts
- [ ] LinkedIn: "{Title} at {Company}"
- [ ] Apollo.io: Email finder
- [ ] Hunter.io: Email patterns
- [ ] Company "About" pages: Team listings
- [ ] GitHub: Check company org members
- [ ] Twitter: Follow engineering accounts

---

## 📧 Outreach Templates

### LinkedIn Message (Russian)
```
Привет, {Name}!

Делаю open-source альтернативу LocalStack — инструмент для 
локального тестирования AWS сервисов (S3, Lambda, DynamoDB). 

Основная фишка — детерминированные тесты (zero flakiness) 
и 10x быстрее прогоны CI/CD.

Можно 15 минут созвониться? Хочу понять:
- Как вы сейчас тестируете AWS-интеграции
- Что болит больше всего с LocalStack/реальным AWS
- Какие фичи были бы критичны для вашей команды

Не продаю ничего — проект в early stage, собираю feedback 
от лидов инженерных команд.

Вот репозиторий: github.com/NickScherbakov/starward

Спасибо!
Nick
```

### LinkedIn Message (English)
```
Hi {Name},

I'm building an open-source LocalStack alternative focused on:
- Deterministic testing (zero flaky tests)
- 10x faster CI/CD for AWS services
- Chaos engineering built-in

Would you have 15 min for a quick call? I'd love to understand:
- How you currently test AWS integrations
- Pain points with LocalStack/real AWS
- What features would be critical for your team

Not selling anything—just gathering feedback from engineering 
leaders at this stage.

Here's the repo: github.com/NickScherbakov/starward

Thanks!
Nick
```

### Email Subject Lines (A/B Test These)
- "Quick question about AWS testing at {Company}"
- "LocalStack alternative - 15 min feedback?"
- "How does {Company} test AWS locally?"
- "AWS testing pain points - 3 quick questions"

### Email Body (If LinkedIn doesn't work)
```
Subject: Quick question about AWS testing at {Company}

Hi {Name},

I came across {Company}'s engineering blog / saw your talk at 
{Conference} / noticed you're hiring DevOps engineers.

I'm building Starward — an open-source tool for local AWS testing 
with focus on deterministic snapshots and chaos engineering.

Before building more features, I'm talking to engineering leaders 
at companies like yours to understand:

1. How do you test AWS integrations today? (LocalStack? Real AWS?)
2. What's the biggest frustration with your current approach?
3. If you could wave a magic wand, what would you fix?

Would you have 15 minutes this week for a call?

Not pitching anything — genuinely want to learn and potentially 
make this useful for teams like yours.

Here's the repo: https://github.com/NickScherbakov/starward

Best,
Nick

P.S. Happy to share what I learn from other teams (anonymized).
```

---

## 🎤 Interview Script (15 minutes)

### **Opening (2 min)**
```
"Thanks for taking the time, {Name}! 

Quick context: I'm building Starward — think LocalStack but with 
focus on deterministic tests and built-in chaos engineering.

I want to learn how teams like yours actually work with AWS in 
dev/test. This is pure discovery — no pitch, just questions.

Sound good? Let's dive in."
```

### **Part 1: Current State (5 min)**

**Q1: How do you currently test code that talks to AWS?**
- [ ] LocalStack
- [ ] Real AWS (dev accounts)
- [ ] Mocks/stubs
- [ ] Combination

*Follow-up:* "What made you choose this approach?"

**Q2: Walk me through your typical CI/CD flow for a service that uses S3 and SQS.**
- How long does it take?
- Where do tests run? (GitHub Actions? Jenkins?)
- Do you hit real AWS or mocks?

**Q3: Do you have flaky tests related to AWS services?**
- How often?
- Which services are worst offenders?
- How do you handle them?

**Q4: What's your monthly AWS spend on dev/test environments?**
- Ballpark: $1k / $5k / $10k+ / "no idea"
- Ever had a surprise bill incident?

---

### **Part 2: Pain Points (5 min)**

**Q5: What's the #1 frustration with your current AWS testing setup?**
- Speed?
- Reliability?
- Cost?
- Setup complexity?
- API coverage gaps?

**Q6: If you use LocalStack, what do you like/dislike about it?**
- Missing features?
- Bugs/quirks?
- Pricing concerns?

**Q7: How do new engineers on your team learn AWS?**
- Do they experiment locally or jump into dev AWS?
- Any incidents from learning mistakes?

---

### **Part 3: Solution Validation (3 min)**

**Q8: Imagine I could guarantee:**
- All AWS tests run locally in 30 seconds
- 100% deterministic (snapshot/restore state)
- Built-in chaos testing (latency injection, failures)

**What would that be worth to you?**
- Time saved per week?
- Dollar value?

**Q9: What's more important for your team:**
- [ ] API coverage (100% AWS parity)
- [ ] Reliability (no flakes, perfect snapshots)
- [ ] Speed (subsecond operations)
- [ ] Features (chaos, IAM simulation, cost profiling)

**Q10: Hypothetically, would you pay $2,000/month if it:**
- Saved 10 engineer-hours/week
- Eliminated flaky tests
- Cut dev AWS costs by $5k/month

- [ ] Yes, immediately
- [ ] Maybe, need to see it work
- [ ] No, too expensive
- [ ] No, LocalStack works fine

---

### **Closing (2 min)**
```
"This is super helpful! Last few things:

1. Can I add you to our early access list? 
   (You'd get free Team plan for 3 months when we launch)

2. Would you be open to a 30-min demo when we have a working 
   prototype? (Probably 3-4 weeks)

3. Any other folks on your team or in your network I should 
   talk to about this?

Thanks again, {Name}. I'll send you a summary of what I'm 
learning from these interviews — might be useful for you too."
```

**After call:**
- [ ] Send thank you email within 24 hours
- [ ] Add to CRM with detailed notes
- [ ] Send calendar invite for demo (if interested)
- [ ] Ask for intro to other contacts

---

## 📊 Success Metrics

### **Week 1: Nov 11-17**
- [ ] 30 LinkedIn connection requests sent
- [ ] 20 personalized messages sent
- [ ] 10 email outreaches
- [ ] 8 responses received (40% response rate)
- [ ] 3 calls scheduled

**Deliverable:** Outreach tracker spreadsheet with all contacts

---

### **Week 2: Nov 18-24**
- [ ] 5 customer interviews completed
- [ ] Interview notes documented (template below)
- [ ] 2 "would pay $1k+/month" validations
- [ ] 1 design partner identified
- [ ] 10 more outreach messages

**Deliverable:** First synthesis - top 3 pain points

---

### **Week 3: Nov 25 - Dec 1**
- [ ] 10 total interviews completed
- [ ] 3 design partners committed (free beta)
- [ ] Pricing hypothesis validated ($1-5k range)
- [ ] Top 5 must-have features identified

**Deliverable:** Refined ICP document

---

### **Week 4: Dec 2-8**
- [ ] 15 total interviews
- [ ] 5 design partners onboarded
- [ ] 2 LOIs (letter of intent to buy when ready)
- [ ] Feature roadmap prioritized based on feedback
- [ ] Decision: Build or pivot?

**Deliverable:** Go/No-Go memo

---

## 📝 Interview Notes Template

After each call, fill this out (takes 10 min):

```markdown
## Interview #{N} - {Company} - {Date}

### Contact Info
- **Name:** {Full Name}
- **Title:** {Exact title}
- **Company:** {Company Name}
- **Stage:** Series A/B/C / Bootstrap / Public
- **Team Size:** ~{N} total engineers
- **LinkedIn:** {URL}
- **Email:** {email}

---

### Current Setup
**AWS Services Used:**
- [ ] S3
- [ ] Lambda
- [ ] DynamoDB
- [ ] SQS
- [ ] Other: ___________

**Testing Approach:**
- Current tool: LocalStack / Real AWS / Mocks / Hybrid
- CI/CD platform: GitHub Actions / GitLab / Jenkins / Circle
- Avg CI time: X minutes
- Monthly dev AWS spend: $X (or "unknown")

**Team Context:**
- Backend languages: Python / Node / Java / Go
- Microservices: Yes / No
- Deploy frequency: X times/day

---

### Pain Points (Ranked by Severity)
1. **{Biggest Pain}**
   - Frequency: Daily / Weekly / Monthly
   - Impact: Blocks deploys / Slows CI / Costs money
   - Quote: "{Exact words they used}"

2. **{Second Pain}**
   - ...

3. **{Third Pain}**
   - ...

**LocalStack Specific Issues** (if they use it):
- Missing features: ___________
- Bugs: ___________
- Pricing concerns: ___________

---

### Solution Validation

**Willingness to Pay:**
- [ ] YES - Would pay $1-5k/month if it works
- [ ] MAYBE - Need to see demo/trial
- [ ] NO - Happy with current setup
- [ ] NO - Price too high

**Price Sensitivity:**
- Max budget mentioned: $____/month
- ROI expectation: Must save X hours/week

**Must-Have Features:**
1. ___________
2. ___________
3. ___________

**Nice-to-Have:**
1. ___________
2. ___________

**Critical Quote on Value:**
"{If you could do X, that would save us Y hours per week, 
which is worth $Z to us}"

---

### Design Partner Potential
- [ ] **YES** - Excited, wants early access
- [ ] **MAYBE** - Interested but cautious
- [ ] **NO** - Polite but not interested

**If YES, next steps:**
- [ ] Add to beta list
- [ ] Schedule demo (date: ______)
- [ ] Get intro to other team members
- [ ] Ask for testimonial after trial

---

### Referrals
"Who else should I talk to about this?"
- Name 1: {Name, Title, Company} - intro: Yes/No
- Name 2: ...

---

### Follow-Up Actions
- [ ] Send thank you email (within 24h)
- [ ] Send learning synthesis (week 2/4)
- [ ] Schedule demo (if design partner)
- [ ] Add to CRM with tags: Hot/Warm/Cold

---

### Raw Notes / Transcript
{Paste detailed notes or recording transcript here}

---

### Reflection
**Surprised by:** ___________
**Validated assumption:** ___________
**Invalidated assumption:** ___________
**New insight:** ___________
```

---

## 🛠️ Tools & CRM Setup

### **Simple CRM (Google Sheets)**

Create spreadsheet with columns:

| Company | Contact | Title | LinkedIn | Email | Stage | Priority | Status | Next Action | Interview Date | Notes Link |
|---------|---------|-------|----------|-------|-------|----------|--------|-------------|----------------|------------|
| Rowi | Ivan P. | VP Eng | url | email | Series A | Hot | Interviewed | Send demo | 2025-11-15 | link |

**Status values:**
- Not Contacted
- Messaged (LinkedIn)
- Messaged (Email)
- Responded
- Call Scheduled
- Interviewed
- Design Partner
- Dead (Not Interested)

**Priority:**
- 🔥 Hot (strong fit, responded)
- ☀️ Warm (good fit, no response yet)
- ❄️ Cold (low fit or no response after 2 touches)

---

### **Email Tracking**
- Use **Mailtrack** (free Chrome extension) to see opens
- Track open rates by subject line → optimize

---

### **Calendar**
- **Calendly** free tier for scheduling
- Link: calendly.com/nickscherbakov/customer-discovery
- Buffer: 15 min between calls
- Availability: 3-4 slots per day max

---

### **Note-Taking**
- Record calls (with permission): "Mind if I record for notes?"
- Use Otter.ai / Google Meet auto-transcribe
- Alternatively: Take notes in template during call

---

## 🚩 Red Flags to Watch

### **If 80%+ say:** "We're happy with LocalStack"
**→ Problem:** Positioning issue
**→ Fix:** Find differentiation (chaos, determinism, speed)

### **If everyone wants:** Features you can't build in 6 months
**→ Problem:** Scope mismatch
**→ Fix:** Focus on narrow beachhead (just S3+SQS?)

### **If no one will pay:** $1,000+/month
**→ Problem:** Value prop too weak OR wrong market
**→ Fix:** Target bigger companies OR add more value

### **If SMBs want:** Enterprise features (SSO, on-prem)
**→ Problem:** Targeting wrong segment
**→ Fix:** Go upmarket OR simplify offering

### **If 50%+ say:** "We just use real AWS dev accounts"
**→ Problem:** Pain not strong enough
**→ Fix:** Emphasize speed/cost/determinism more

---

## ✅ Success Criteria (By Dec 8)

You should have:
- [x] **15+ interviews completed** with decision makers
- [x] **3-5 design partners** committed to free beta
- [x] **2+ companies** saying "we'd pay $X when ready"
- [x] **Clear top-3 pain points** validated across interviews
- [x] **Validated pricing** in $1-5k/month range
- [x] **Top-5 must-have features** identified
- [x] **1-2 customer quotes** for marketing

**If you hit these → You have PMF hypothesis worth building.**

**If not:**
- < 5 interviews: Outreach problem (fix messaging)
- 0 "would pay": Value prop problem (pivot or deeper discovery)
- No design partners: Trust problem (build credibility first)

---

## 📈 Weekly Rituals

### **Monday Morning**
- Review last week's metrics
- Plan 10 new outreach targets
- Send follow-ups to non-responders

### **Wednesday Midday**
- Synthesize interview notes from week
- Update CRM with new learnings
- Share insights with any advisors/mentors

### **Friday Afternoon**
- Review success metrics
- Write weekly summary:
  - Interviews: X
  - Key learnings: ...
  - Next week focus: ...
- Celebrate small wins 🎉

---

## 💬 Sample Learning Synthesis (Send to Interviewees)

After Week 2, send this to everyone you've talked to:

```
Subject: What I'm learning from AWS testing interviews

Hi {Name},

Quick update on what I'm hearing from engineering leaders 
like you about AWS testing:

**Top 3 Pain Points:**
1. CI/CD slowness (avg 35 min per run mentioned)
2. Flaky tests from real AWS (46% reported this)
3. LocalStack missing features (Lambda layers, IAM)

**Surprising Insights:**
- Most teams spending $8-15k/mo on dev AWS (!)
- Determinism > API coverage (everyone wants reliable tests)
- Chaos testing is a "nice-to-have" not "must-have"

**What I'm Building First:**
Based on feedback, focusing on:
- S3 + SQS + Lambda (core 3 services)
- Snapshot/restore in <10ms (determinism)
- Drop-in LocalStack replacement (easy migration)

**Thanks for your input!** This is shaping the roadmap.

I'll reach out when we have a prototype (mid-Dec).

Best,
Nick

P.S. If you know other eng leaders facing AWS testing pain, 
I'd love an intro!
```

---

## 🎯 Next Steps After Customer Discovery

### **If Validation is Strong (Dec 9+)**

1. **Build MVP (4-6 weeks)**
   - Core S3 service (5 operations)
   - Snapshot engine
   - FastAPI server
   - 1 working example (Terraform)

2. **Design Partner Beta (Jan 2026)**
   - Onboard 3-5 companies
   - Weekly check-ins
   - Iterate based on feedback

3. **Launch (Feb 2026)**
   - ProductHunt
   - HackerNews "Show HN"
   - Dev.to article
   - Tweet thread

### **If Validation is Weak**

- **Pivot options:**
  - Narrower niche (just fintech? just Terraform users?)
  - Different problem (not testing but cost optimization?)
  - Different buyer (platform teams not backend devs?)

- **Kill criteria:**
  - < 5 interviews after 50 outreach attempts
  - 0 people willing to pay $500+/month
  - "Happy with LocalStack" from 90%+ respondents

---

**Start Date:** Nov 11, 2025  
**Owner:** @NickScherbakov  
**Status:** Ready to Execute

---

**Remember:** The goal is to LEARN, not to SELL. Be genuinely curious. 

Good luck! 🚀

# Santa Fresh Financial Model - Restructuring Action Plan

**Date:** January 29, 2026
**Based On:** Completed PROJECT_DATA_COLLECTION_QUESTIONNAIRE.md
**Approach:** Model structure customization (NO hard-coded values)

---

## 🎯 CORE PRINCIPLE: FLEXIBLE INPUT MODEL

**User Requirement:** "It's important that I get to put in the figures in the assumption page, because as we continue writing the project, figures may change, so let's not hard code any figures and give me the flexibility to input my very own figures."

**Implementation:**
- Assumptions sheet = 100% user-editable inputs
- All values referenced from Assumptions (no hard-coded constants in formulas)
- Model structure reflects Santa Fresh operational reality
- Placeholder values (or blank cells) for user to populate
- Complete flexibility to update any figure at any time

---

## 📋 MODEL RESTRUCTURING REQUIREMENTS

### Current Model vs. Santa Fresh Requirements

#### ✅ What Current Model Has Right:
1. **Control panel architecture** - Single Assumptions sheet for all inputs
2. **13-worksheet structure** - Good foundation (Dashboard, P&L, Cash Flow, Returns, etc.)
3. **Medium granularity** - Aligns with user's Option B preference
4. **DFI-standard outputs** - IRR, NPV, DSCR, development impact

#### 🔄 What Needs Restructuring:

### PRIORITY 1: Assumptions Sheet Reorganization

**Current Structure Issues:**
- Generic "seed processing" assumptions don't match potato value chain reality
- Missing: Dual seed pathways (conventional vs TPS nursery)
- Missing: Fresh-pack vs frozen line differentiation
- Missing: Animal feed production (not biogas)
- Missing: 4 specific regional depots
- Missing: Seeds-on-credit program mechanics

**Required New Structure:**

```
ASSUMPTIONS SHEET - SANTA FRESH POTATO VALUE CHAIN
═══════════════════════════════════════════════════

SECTION A: PROJECT TIMELINE & PHASING
├── Model start year
├── Model horizon (years)
├── Phase 1 construction duration (months)
├── Phase 2 construction duration (months)
├── Phase 3 construction duration (months)
└── Operations start dates by phase

SECTION B: REVENUE STREAMS & PRODUCTS
├── B1: Fresh-Pack Table Potatoes
│   ├── Annual target volume (tonnes) - Year 1, 2, 3+
│   ├── Selling price (XAF/kg)
│   ├── Price escalation (%/year)
│   └── Customer payment terms (days)
├── B2: Frozen French Fries
│   ├── Annual target volume (tonnes) - Year 1, 2, 3+
│   ├── Selling price (XAF/kg)
│   ├── Price escalation (%/year)
│   └── Customer payment terms (days)
├── B3: Certified Seed Sales
│   ├── Annual sales volume (tonnes)
│   ├── Selling price (XAF/kg)
│   └── Price escalation (%/year)
├── B4: Animal Feed Pellets (Byproduct)
│   ├── Feed production per tonne processed (kg/tonne)
│   ├── Feed selling price (XAF/kg)
│   └── Feed price escalation (%/year)
└── B5: Revenue Seasonality (Monthly % distribution - Jan to Dec)

SECTION C: PROCESSING CAPACITY & UTILIZATION
├── C1: Fresh-Pack Line
│   ├── Installed capacity (tonnes/hour)
│   ├── Operating hours per day
│   ├── Operating days per year
│   ├── Year 1 utilization (%)
│   ├── Year 2 utilization (%)
│   └── Year 3+ utilization (%)
├── C2: Frozen French Fry Line
│   ├── Installed capacity (tonnes/hour raw input)
│   ├── Fry conversion rate (raw to finished %)
│   ├── Operating hours per day
│   ├── Operating days per year
│   ├── Year 1 utilization (%)
│   ├── Year 2 utilization (%)
│   └── Year 3+ utilization (%)
└── C3: Processing Yield Factors
    ├── Fresh-pack yield (% of raw input)
    ├── Frozen fry yield (% of raw input)
    ├── Peeling loss rate (%)
    └── Reject rate (%)

SECTION D: RAW MATERIAL SOURCING - WARE POTATOES
├── Annual ware potato requirement (tonnes) - calculated from processing
├── Farmgate price - processing grade (XAF/kg)
├── Farmgate price - table stock (XAF/kg)
├── Raw material price escalation (%/year)
├── Farmer payment terms (days)
├── % sourced from outgrowers
├── % sourced from EIC farm
├── % sourced from spot market
└── Ware potato seasonality (monthly % distribution)

SECTION E: SEED OPERATIONS
├── E1: Traditional Seed Potatoes (Agrico/HZPC)
│   ├── Annual G0 import volume (tonnes)
│   ├── G0 import price (XAF/kg)
│   ├── Multiplication ratio (G0 → G1)
│   ├── Seed multiplication area (hectares)
│   ├── Seed yield (tonnes/ha)
│   ├── % sold to outgrowers
│   ├── % used internally
│   └── Seed price to farmers (XAF/kg)
├── E2: True Potato Seeds - TPS (Solynta)
│   ├── Deploy TPS pathway? (Yes/No toggle)
│   ├── Annual TPS import (number of seeds)
│   ├── TPS cost per seed (XAF)
│   ├── Nursery capacity (seedlings/year)
│   ├── Cost per seedling produced (XAF)
│   ├── Seedling price to farmers (XAF)
│   └── Hectares supported by TPS
└── E3: Seeds-on-Credit Program
    ├── Credit period (days)
    ├── Interest rate/markup (%)
    ├── Expected default rate (%)
    └── Recovery rate on defaults (%)

SECTION F: OUTGROWER NETWORK
├── Current number of farmers
├── Target farmers - Year 1
├── Target farmers - Year 2
├── Target farmers - Year 3+
├── Average farm size per farmer (hectares)
├── Target yield with certified seed (tonnes/ha)
├── Baseline yield without certified seed (tonnes/ha)
├── Input package cost per farmer (XAF/ha)
├── Extension cost per farmer (XAF/year)
├── Free fertilizer distribution (tonnes/farmer/year)
└── Fertilizer value to farmers (XAF/tonne)

SECTION G: EIC-OWNED NUCLEUS FARM
├── Total farm size (hectares)
├── Annual land lease cost (XAF/ha)
├── Hectares for seed multiplication
├── Hectares for ware potato production
├── Hectares for rotation crops/other uses
├── Farm operating cost (XAF/ha/year)
└── Farm equipment maintenance (XAF/year)

SECTION H: OPERATING COSTS - LABOR
├── H1: Management & Administration
│   ├── Number of staff
│   └── Total monthly payroll (XAF/month)
├── H2: Production (Factory Workers)
│   ├── Number of staff
│   └── Total monthly payroll (XAF/month)
├── H3: QC & Laboratory
│   ├── Number of staff
│   └── Total monthly payroll (XAF/month)
├── H4: Logistics & Distribution
│   ├── Number of staff
│   └── Total monthly payroll (XAF/month)
├── H5: Sales & Marketing
│   ├── Number of staff
│   └── Total monthly payroll (XAF/month)
├── H6: Field Agents (Outgrower Support)
│   ├── Number of staff
│   └── Total monthly payroll (XAF/month)
├── H7: Security & Maintenance
│   ├── Number of staff
│   └── Total monthly payroll (XAF/month)
└── Labor cost escalation (%/year)

SECTION I: OPERATING COSTS - UTILITIES
├── I1: Electricity
│   ├── Grid electricity consumption (kWh/year)
│   ├── Grid electricity tariff (XAF/kWh)
│   ├── Generator backup hours (hours/year)
│   ├── Generator fuel consumption (liters/hour)
│   └── Generator efficiency (kWh/liter diesel)
├── I2: Water
│   ├── Water consumption (m³/year)
│   ├── Water tariff (XAF/m³)
│   └── Water recycling rate (%)
├── I3: Diesel (Fleet & Generator)
│   ├── Fleet diesel consumption (liters/year)
│   ├── Diesel price (XAF/liter)
│   └── Diesel price escalation (%/year)
└── Utility cost escalation (%/year)

SECTION J: OPERATING COSTS - PROCESSING CONSUMABLES
├── J1: Frying oil (for frozen line)
│   ├── Oil consumption per tonne frozen fries (liters/tonne)
│   ├── Oil price (XAF/liter)
│   └── Oil price escalation (%/year)
├── J2: Packaging Materials - Fresh-Pack
│   ├── Bags/boxes per tonne (units/tonne)
│   ├── Average cost per unit (XAF/unit)
│   └── Packaging price escalation (%/year)
├── J3: Packaging Materials - Frozen Fries
│   ├── Boxes per tonne (units/tonne)
│   ├── Average cost per unit (XAF/unit)
│   └── Packaging price escalation (%/year)
├── J4: Processing Additives
│   ├── Salt & seasonings cost (XAF/tonne processed)
│   ├── Anti-oxidants cost (XAF/tonne processed)
│   └── Additives price escalation (%/year)
├── J5: Cleaning & Sanitation
│   ├── Annual cleaning chemicals cost (XAF/year)
│   └── Escalation (%/year)
├── J6: Spare Parts & Maintenance
│   ├── Annual maintenance supplies (XAF/year)
│   └── Escalation (%/year)
└── J7: QC Lab Supplies
    ├── Annual lab supplies cost (XAF/year)
    └── Escalation (%/year)

SECTION K: OPERATING COSTS - OTHER
├── Insurance (% of total assets/year)
├── Professional services (XAF/year)
├── Marketing & advertising - Year 1 (XAF/year)
├── Marketing & advertising - Year 2+ (XAF/year)
├── Office supplies & admin utilities (XAF/year)
├── Depot rent (4 depots total - XAF/year)
├── Communication (phone, internet) (XAF/year)
├── Travel & transportation (XAF/year)
├── Training & development (XAF/year)
├── Licensing & permits (XAF/year)
├── Bank fees & transaction costs (XAF/year)
├── Waste disposal (XAF/year)
└── General cost inflation (%/year)

SECTION L: WASTE VALORIZATION - ANIMAL FEED
├── Organic waste generation rate (kg/tonne processed)
├── Feed pelletizer operating cost (XAF/tonne feed)
├── Feed pelletizer capacity utilization (%)
└── [Revenue from feed sales in Section B4]

SECTION M: CAPITAL EXPENDITURE - BY PHASE & CATEGORY
├── M1: Phase 1 - Foundation Infrastructure (Year 0-1)
│   ├── Land lease prepayment (XAF)
│   ├── Site development & civil works (XAF)
│   ├── Factory building (m² and XAF)
│   ├── Office building (m² and XAF)
│   ├── Warehouse buildings (m² and XAF)
│   ├── Pre-processing equipment (grouped) (XAF)
│   ├── Climate storage - Curing cells (XAF)
│   ├── Climate storage - Long-term cells (XAF)
│   ├── Climate storage - Activation cells (XAF)
│   ├── Priva climate control system (XAF)
│   ├── Fresh-pack processing line (complete) (XAF)
│   ├── Animal feed pelletizer (XAF)
│   ├── Finished goods - Ambient warehouse (XAF)
│   ├── Water treatment plant (WTP) (XAF)
│   ├── Wastewater treatment plant (WWTP) (XAF)
│   ├── Power - Backup generators (XAF)
│   ├── Power - Solar (optional) (XAF)
│   ├── Farm equipment & machinery (XAF)
│   ├── Nursery facility (TPS - conditional) (XAF)
│   ├── Reefer trucks - Phase 1 (number × cost per unit)
│   ├── Delivery vans - Phase 1 (number × cost per unit)
│   ├── On-site fuel depot (XAF)
│   ├── Furniture, fixtures & IT (XAF)
│   ├── Pre-operating expenses (XAF)
│   └── Phase 1 contingency (%)
├── M2: Phase 2 - Frozen Line & Initial Depot (Year 2)
│   ├── Frozen french fry line (complete) (XAF)
│   ├── Finished goods - Frozen cold store (XAF)
│   ├── Regional depot - Douala (XAF)
│   ├── Reefer trucks - Phase 2 (number × cost)
│   ├── Delivery vans - Phase 2 (number × cost)
│   └── Phase 2 contingency (%)
└── M3: Phase 3 - Regional Depot Expansion (Year 3)
    ├── Regional depot - Yaoundé (XAF)
    ├── Regional depot - Bamenda (XAF)
    ├── Regional depot - Bafoussam (XAF)
    ├── Delivery vans - Phase 3 (number × cost)
    ├── TPS nursery scale-up (if validated) (XAF)
    └── Phase 3 contingency (%)

SECTION N: REGIONAL DEPOT OPERATING COSTS
├── N1: Douala Depot
│   ├── Cold storage capacity (tonnes)
│   ├── Staff salaries (XAF/month)
│   ├── Electricity (XAF/month)
│   ├── Rent (XAF/month)
│   └── Security & maintenance (XAF/month)
├── N2: Yaoundé Depot
│   ├── Cold storage capacity (tonnes)
│   ├── Staff salaries (XAF/month)
│   ├── Electricity (XAF/month)
│   ├── Rent (XAF/month)
│   └── Security & maintenance (XAF/month)
├── N3: Bamenda Depot
│   ├── Cold storage capacity (tonnes)
│   ├── Staff salaries (XAF/month)
│   ├── Electricity (XAF/month)
│   ├── Rent (XAF/month)
│   └── Security & maintenance (XAF/month)
└── N4: Bafoussam Depot
    ├── Cold storage capacity (tonnes)
    ├── Staff salaries (XAF/month)
    ├── Electricity (XAF/month)
    ├── Rent (XAF/month)
    └── Security & maintenance (XAF/month)

SECTION O: WORKING CAPITAL PARAMETERS
├── Raw materials inventory (days)
├── Finished goods inventory - Fresh-pack (days)
├── Finished goods inventory - Frozen (days)
├── Accounts receivable - weighted average (days)
├── Accounts payable - suppliers (days)
├── Accounts payable - farmers (days)
├── Seeds-on-credit receivables (days)
└── Seasonal working capital peak multiplier

SECTION P: FINANCING STRUCTURE
├── P1: Total Project Cost
│   ├── Total CAPEX (calculated from Section M)
│   └── Initial working capital (calculated from Section O)
├── P2: Funding Sources (% of total)
│   ├── Sponsor equity (%)
│   ├── Senior debt (%)
│   ├── Subordinated debt/mezzanine (%)
│   └── Grant / Technical assistance (%)
├── P3: Senior Debt Terms
│   ├── Interest rate (%)
│   ├── Tenor (years)
│   ├── Grace period (years)
│   ├── Arrangement fee (%)
│   └── Repayment structure (equal principal/annuity toggle)
└── P4: Subordinated Debt Terms
    ├── Interest rate (%)
    ├── Tenor (years)
    ├── Grace period (years)
    └── Repayment structure

SECTION Q: TAXATION & INCENTIVES
├── Q1: Corporate Income Tax
│   ├── Standard CIT rate (%)
│   ├── Tax holiday duration (years)
│   ├── Reduced rate after holiday (%)
│   ├── Tax credit during operation (%)
│   └── Tax loss carryforward (years)
├── Q2: Other Taxes
│   ├── VAT rate (%)
│   ├── VAT on sales (Yes/No toggle)
│   ├── VAT recoverable on purchases (%)
│   ├── Withholding tax - interest (%)
│   ├── Withholding tax - dividends (%)
│   ├── Import duties - standard (%)
│   └── Import duty exemption (Yes/No toggle for incentive period)
└── Q3: Investment Incentive Period
    ├── Installation phase (years) - full duty exemption
    └── Operation phase benefits (years)

SECTION R: DEPRECIATION & ASSET LIFE
├── Depreciation method (straight-line/declining toggle)
├── Buildings useful life (years)
├── Buildings residual value (%)
├── Heavy machinery useful life (years)
├── Heavy machinery residual value (%)
├── Light equipment useful life (years)
├── Light equipment residual value (%)
├── Vehicles useful life (years)
├── Vehicles residual value (%)
├── Furniture & fixtures useful life (years)
├── Furniture & fixtures residual value (%)
├── IT equipment useful life (years)
└── IT equipment residual value (%)

SECTION S: MACROECONOMIC ASSUMPTIONS
├── XAF/USD exchange rate (current)
├── XAF/EUR exchange rate (655.957 - fixed peg)
├── Expected XAF/USD change (%/year)
├── General inflation rate (%/year)
├── Discount rate for NPV (WACC %)
├── Terminal growth rate (%)
└── Risk-free rate (%)

SECTION T: SCENARIO ANALYSIS - TOGGLES
├── Active scenario (Base/Downside/Upside - dropdown)
├── T1: Downside Scenario Adjustments
│   ├── Yield adjustment (%)
│   ├── Price adjustment (%)
│   ├── CAPEX overrun (%)
│   ├── Operating cost increase (%)
│   ├── Ramp-up delay (months)
│   └── Capacity utilization (% of base)
└── T2: Upside Scenario Adjustments
    ├── Yield adjustment (%)
    ├── Price adjustment (%)
    ├── CAPEX savings (%)
    ├── Operating cost reduction (%)
    ├── Accelerated ramp-up (months)
    └── Capacity utilization (% of base)

SECTION U: DEVELOPMENT IMPACT PARAMETERS
├── U1: Employment
│   ├── Construction phase jobs (number)
│   ├── Operations permanent jobs (number)
│   ├── % women in workforce
│   ├── Average monthly salary (XAF)
│   └── Indirect jobs multiplier
├── U2: Farmer Impact
│   ├── Baseline farmer income (XAF/year)
│   ├── Project farmer income (XAF/year)
│   └── % women farmers
└── U3: Economic Impact
    ├── Import substitution value (calculated)
    ├── Export revenue (calculated)
    ├── Local content (% of costs)
    └── CO₂ reduction (tonnes/year)
```

---

## 🔧 FORMULA LOGIC CHANGES REQUIRED

### 1. Revenue Sheet
**Current:** Generic "seed output × price"
**New Required:**
```
Revenue =
  + (Fresh-pack volume × Fresh-pack price)
  + (Frozen fries volume × Frozen price)
  + (Certified seed sales × Seed price)
  + (Animal feed production × Feed price)

Apply monthly seasonality from Assumptions
Apply ramp-up utilization curves from Assumptions
```

### 2. Operating Costs Sheet
**Current:** Generic processing costs
**New Required:**
```
Raw Materials =
  Annual throughput (calculated from capacity × utilization) × Farmgate price
  Apply ware potato seasonality

Labor Costs =
  Sum of 7 department payrolls from Assumptions
  Scale with ramp-up phase

Utilities =
  Electricity (grid + generator based on hours)
  Water (consumption - recycled portion)
  Diesel (fleet + generator)

Processing Consumables =
  Frying oil (frozen line only, per tonne frozen output)
  Packaging (fresh-pack + frozen, differentiated)
  Additives, cleaning, spare parts, QC supplies

Depot Operating Costs =
  4 depots × (staff + electricity + rent + maintenance)
  Phase in based on Phase 2-3 timing
```

### 3. CAPEX Schedule Sheet
**Current:** 5 phases generic
**New Required:**
```
Phase 1 (Year 0-1): Seed/farm/fresh-pack/storage/WTP/WWTP foundation
Phase 2 (Year 2): Frozen line + Douala depot
Phase 3 (Year 3): 3 additional depots + fleet expansion

Total CAPEX = Sum of all line items × (1 + contingency %)
Each line item pulls from Assumptions Section M
```

### 4. Debt Schedule Sheet
**Current:** Generic senior debt
**New Required:**
```
Total Debt = (Total Project Cost × Senior Debt %) + (Total × Mezzanine %)

Senior Debt Amortization:
  Grace period: Interest-only for X years
  Repayment: Equal principal or annuity based on toggle
  Interest rate from Assumptions

Subordinated Debt Amortization:
  Longer grace period
  Higher interest rate
  Subordinated to senior debt cash flow priority
```

### 5. Working Capital Sheet
**New Required:**
```
Current Assets =
  + Raw materials inventory (throughput/365 × days from Assumptions)
  + Finished goods - Fresh (sales/365 × days)
  + Finished goods - Frozen (sales/365 × days)
  + Accounts receivable (revenue/365 × days)
  + Seeds-on-credit receivables (seed sales/365 × credit days)

Current Liabilities =
  + Accounts payable - suppliers (purchases/365 × days)
  + Accounts payable - farmers (farmgate payments/365 × days)

Net Working Capital = Current Assets - Current Liabilities
Apply seasonal multiplier during harvest months
```

### 6. Development Impact Sheet
**New Required:**
```
Jobs Created =
  Direct operations (from Assumptions Section U1)
  Construction phase (temporary)
  Indirect (outgrower network: farmers × family workers)
  Induced (logistics, retail, food service multipliers)

Farmer Income Impact =
  # Farmers × (Project income - Baseline income)

Import Substitution =
  Frozen fries volume × Import price benchmark
  Certified seed volume × Import price benchmark

Export Revenue =
  (Revenue × Export % from customer mix)

Women Participation =
  % women in workforce × total jobs
  % women farmers × total farmers
```

---

## 📊 OUTPUT SHEETS - MODIFICATIONS

### 1. Dashboard Sheet
**Add:**
- Fresh-pack vs Frozen revenue split visualization
- 4 Regional depot status indicators
- Farmer network growth curve (actual vs target)
- Animal feed valorization metrics
- Phase 1/2/3 milestone tracker

### 2. Returns Analysis Sheet
**Enhance:**
- Project IRR (all cash flows)
- Equity IRR (post-debt service)
- DSCR by year (with covenant threshold line)
- NPV sensitivity to discount rate
- Break-even analysis: Volume, price, utilization
- Payback period (debt + equity)

### 3. Sensitivity Analysis Sheet
**Tornado chart drivers:**
1. Capacity utilization / farmer yields
2. Farmgate ware potato price
3. Fresh-pack selling price
4. Frozen fries selling price
5. CAPEX overruns
6. Operating cost increases
7. Exchange rate (XAF/USD)

**Two-way sensitivity tables:**
- Equity IRR: Capacity utilization vs Product prices
- DSCR: Throughput vs Farmgate costs
- NPV: CAPEX vs Revenue

---

## 🎨 USER EXPERIENCE ENHANCEMENTS

### 1. Assumptions Sheet - Color Coding
- **BLUE cells** = User inputs (editable)
- **YELLOW cells** = Auto-calculated from other assumptions (locked)
- **GREEN cells** = Scenario toggles (Base/Downside/Upside selector)
- **WHITE cells** = Labels and headers (locked)

### 2. Assumptions Sheet - Input Validation
- Dropdown lists where appropriate (Yes/No, scenario selector, repayment structure)
- Reasonable range checks (e.g., utilization 0-100%, interest rates 0-30%)
- Unit labels next to inputs (XAF, %, tonnes, hectares, etc.)

### 3. Assumptions Sheet - Navigation
- Collapsible sections (Group rows for easy navigation)
- Hyperlink index at top of sheet linking to each section
- "Back to Top" button at end of each section

### 4. Documentation Sheet - User Guide
**Add instructions for:**
- How to input values in Assumptions
- How to switch scenarios (Base/Downside/Upside)
- How to interpret Dashboard outputs
- How to use Sensitivity Analysis
- Key assumptions and their impact
- Model logic flow diagram

---

## ✅ DELIVERABLES CHECKLIST

### Excel Model Components:
- [ ] Restructured Assumptions sheet (Sections A-U)
- [ ] Modified Revenue sheet (fresh-pack + frozen + seed + feed)
- [ ] Modified Operating Costs sheet (7 labor categories + utilities + consumables + depots)
- [ ] Modified CAPEX Schedule (Phase 1/2/3 with detailed line items)
- [ ] Modified Debt Schedule (senior + subordinated + grant)
- [ ] New/Enhanced Working Capital sheet (seeds-on-credit, seasonal multiplier)
- [ ] Modified P&L Statement (multi-revenue streams, detailed costs)
- [ ] Modified Cash Flow (phased CAPEX, seasonal working capital)
- [ ] Enhanced Returns Analysis (IRR/NPV/DSCR/break-even)
- [ ] Enhanced Development Impact (jobs, farmers, import substitution, exports)
- [ ] Enhanced Sensitivity Analysis (tornado charts, two-way tables)
- [ ] Enhanced Dashboard (fresh vs frozen split, depot status, farmer network, phase tracker)
- [ ] Updated Documentation (user guide, assumptions memo, model logic)

### Supporting Annexes (Separate Files):
- [ ] Detailed CAPEX Breakdown (equipment vendor quotes ready to populate)
- [ ] Detailed OPEX Breakdown (cost categories with calculation notes)
- [ ] Assumptions Memorandum (document rationale for key inputs)
- [ ] Model Navigation Guide (how to use the model)

### Quality Assurance:
- [ ] Formula audit (zero errors, no #REF!, no #VALUE!)
- [ ] Circular reference check (zero circular references)
- [ ] Google Sheets compatibility test
- [ ] Scenario toggle test (Base/Downside/Upside switch correctly)
- [ ] Sensitivity analysis functionality test

---

## ⏱️ ESTIMATED IMPLEMENTATION TIME

**Phase 1: Assumptions Sheet Restructuring** (Day 1-2)
- Build Sections A-U structure
- Create input cells (all blank/placeholder for user to populate)
- Add dropdowns, validation, color coding
- Add navigation aids

**Phase 2: Formula Logic Updates** (Day 2-3)
- Update all calculation sheets to reference new Assumptions structure
- Implement fresh-pack + frozen differentiation
- Implement animal feed valorization logic
- Implement regional depot cost rollup
- Implement seeds-on-credit working capital logic

**Phase 3: Output Enhancements** (Day 3-4)
- Update Dashboard with Santa Fresh specific visualizations
- Enhance Sensitivity Analysis (tornado charts, two-way tables)
- Enhance Development Impact metrics
- Update Documentation sheet

**Phase 4: Quality Assurance** (Day 4-5)
- Comprehensive formula audit
- Test scenario switching
- Test with sample values (user can then replace)
- Generate preliminary outputs for validation

**Total Time: 4-5 days** for complete restructuring + testing

---

## 🔄 USER WORKFLOW AFTER MODEL DELIVERY

1. **Receive blank model** with full structure
2. **Populate Assumptions sheet** with your figures as they are finalized:
   - Start with Phase 1 CAPEX (as vendor quotes come in)
   - Add processing capacity targets (as technical specs are confirmed)
   - Add financing terms (as DFI discussions progress)
   - Add operating cost estimates (as budgets are refined)
3. **Review calculated outputs** (Dashboard, P&L, Cash Flow, Returns)
4. **Iterate on assumptions** as project planning evolves
5. **Run scenarios** (Base/Downside/Upside) for risk analysis
6. **Generate outputs** (PDF dashboards for DFI submission)

---

## 📝 CRITICAL DESIGN NOTES

**For Model Builder (Me):**

1. **NO HARD-CODED VALUES** in any formulas except:
   - Mathematical constants (365 days, 12 months, etc.)
   - Unit conversions (1000 kg/tonne, etc.)

2. **ALL operational assumptions** must pull from Assumptions sheet:
   - Prices → Assumptions
   - Volumes → Assumptions
   - Costs → Assumptions
   - Timing → Assumptions
   - Rates → Assumptions

3. **Calculated cells** (e.g., "Total CAPEX") should:
   - Reference Assumptions inputs
   - Be clearly labeled as "CALCULATED"
   - Be protected/locked to prevent accidental editing

4. **Scenario logic:**
   - Single dropdown in Assumptions selects scenario
   - IF statements apply adjustments: `=Assumptions!C50 * (1 + ScenarioAdjustment)`
   - Base case = no adjustment (multiplier = 1.0)

5. **Flexibility for future changes:**
   - If user wants to add a new revenue stream later, structure should accommodate
   - If user wants to change phasing (add Phase 4), structure should accommodate
   - If user wants to add more depots, structure should accommodate

---

## ✅ READY TO PROCEED?

**Confirm before I start building:**

1. ✅ You want Sections A-U in Assumptions (as outlined above)?
2. ✅ You want NO hard-coded values (all inputs blank/placeholder)?
3. ✅ You want medium granularity (20-30 cost categories, grouped CAPEX)?
4. ✅ You want scenario analysis with Base/Downside/Upside toggle?
5. ✅ Target completion: ~4-5 days for full restructure + testing?
6. ✅ Delivery format: Excel .xlsx (primary) + documentation?

If yes to all, I'll begin building immediately.

**First step:** Restructure the Assumptions sheet with blank/placeholder inputs following Sections A-U structure.

**Questions before I start:**
- Do you want me to keep the current model as a backup (Financial_Model_v3.0_ORIGINAL.xlsx) before modifying?
- Any specific Assumptions sections you want prioritized first (e.g., CAPEX, Revenue, Operating Costs)?
- Preferred format for placeholder values: Leave blank, use "100" as placeholder, or use "TBD" text?

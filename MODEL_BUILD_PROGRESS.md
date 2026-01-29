# Santa Fresh Financial Model - Build Progress Tracker

**Model Version:** 4.0
**Project:** EIC Integrated Potato Value Chain
**Started:** January 29, 2026
**Target Completion:** February 3-4, 2026

---

## 🎯 Overall Progress: 40% Complete

```
████████████░░░░░░░░░░░░░░░░░░  40%
```

---

## ✅ PHASE 1: ASSUMPTIONS SHEET STRUCTURE (COMPLETE)

**Status:** ✅ **100% COMPLETE** (Day 1 - January 29, 2026)

### Deliverables:
- [✅] 21 sections (A-U) covering entire operational flow
- [✅] 426 rows with ~300+ input parameters
- [✅] All inputs blank/placeholder for user population
- [✅] Color coding (Blue = inputs, Yellow = calculated, Green = toggles)
- [✅] Medium granularity (20-30 cost categories as requested)

### Key Features Implemented:
- Dual revenue streams (fresh-pack, frozen, seeds, feed)
- Dual seed pathways (conventional + TPS nursery)
- Seeds-on-credit program mechanics
- Animal feed valorization (NOT biogas)
- 4 regional depots (Douala, Yaoundé, Bamenda, Bafoussam)
- Phased CAPEX (Phase 1/2/3)
- Monthly seasonality (revenue and supply)
- Scenario analysis toggles (Base/Downside/Upside)

### Files:
- ✅ `Santa_Fresh_Financial_Model_v4.0.xlsx` (Assumptions sheet complete)
- ✅ `build_santa_fresh_model.py` (base builder script)
- ✅ `build_santa_fresh_complete.py` (complete builder with all sections)
- ✅ Backup: `Financial_Model_Agricultural_Processing_v3.0_BEFORE_RESTRUCTURE.xlsx`

---

## 🔄 PHASE 2: CALCULATION SHEETS & FORMULA LOGIC (IN PROGRESS)

**Status:** 🔄 **IN PROGRESS** (Day 1-3)

**Target Completion:** January 31, 2026

### Calculation Sheets to Build:

#### Sheet 1: Calculations (Derived Values)
**Status:** ⏳ Pending
- [ ] Total CAPEX calculations (Phase 1 + 2 + 3 with contingency)
- [ ] Total annual ware potato requirement (from processing throughput)
- [ ] Annual processing throughput (capacity × utilization × hours × days)
- [ ] G1 seed production (G0 import × multiplication ratio)
- [ ] Animal feed production (waste generation rate × throughput)
- [ ] Weighted average payment terms (by customer segment)

#### Sheet 2: Revenue
**Status:** ⏳ Pending
- [ ] Fresh-pack revenue (volume × price, by year)
- [ ] Frozen fries revenue (volume × price, by year)
- [ ] Certified seed revenue (sales × price)
- [ ] Animal feed revenue (production × price)
- [ ] Revenue by month (applying seasonality %)
- [ ] Total revenue by year (Year 1-10)
- [ ] Revenue growth analysis

#### Sheet 3: Raw Materials Cost
**Status:** ⏳ Pending
- [ ] Ware potato purchases (throughput × farmgate price)
- [ ] Ware potato sourcing mix (outgrower/EIC farm/spot market)
- [ ] Monthly ware potato purchases (applying supply seasonality)
- [ ] Ware potato cost escalation by year
- [ ] Farmer payment timing (accounts payable calculation)

#### Sheet 4: Operating Costs
**Status:** ⏳ Pending
- [ ] Labor costs (7 departments aggregated by year)
- [ ] Utilities (electricity grid + generator, water, diesel)
- [ ] Processing consumables (oil, packaging, additives, cleaning, maintenance, QC)
- [ ] Animal feed pelletizer operating costs
- [ ] Other operating costs (insurance, professional services, marketing, admin, depots, etc.)
- [ ] Operating cost escalation by year
- [ ] Total OPEX by year

#### Sheet 5: Seed Operations
**Status:** ⏳ Pending
- [ ] Traditional seed (G0 import cost, multiplication cost, storage)
- [ ] TPS nursery operations (conditional on toggle)
- [ ] Seeds-on-credit receivables (credit period, defaults, recovery)
- [ ] Seed distribution to outgrowers vs external sales
- [ ] Outgrower input package costs
- [ ] Extension services costs

#### Sheet 6: Regional Depot Costs
**Status:** ⏳ Pending
- [ ] Douala depot operations (staff, electricity, rent, maintenance)
- [ ] Yaoundé depot operations
- [ ] Bamenda depot operations
- [ ] Bafoussam depot operations
- [ ] Depot cost phasing (Douala in Phase 2, others in Phase 3)
- [ ] Total depot operating costs by year

#### Sheet 7: CAPEX Schedule
**Status:** ⏳ Pending
- [ ] Phase 1 CAPEX breakdown (land, buildings, equipment, fleet, WTP/WWTP, etc.)
- [ ] Phase 2 CAPEX breakdown (frozen line, cold store, Douala depot, additional fleet)
- [ ] Phase 3 CAPEX breakdown (3 depots, fleet expansion, TPS scale-up)
- [ ] Contingency calculations (by phase)
- [ ] Total CAPEX by year (Year 0, 1, 2, 3+)
- [ ] CAPEX timing and phasing logic
- [ ] Asset classification (buildings, heavy machinery, light equipment, vehicles)

#### Sheet 8: Depreciation Schedule
**Status:** ⏳ Pending
- [ ] Asset categorization by useful life
- [ ] Straight-line depreciation calculation
- [ ] Accumulated depreciation tracking
- [ ] Net book value by year
- [ ] Residual value calculations
- [ ] Depreciation expense by year (for P&L)

#### Sheet 9: Working Capital
**Status:** ⏳ Pending
- [ ] Raw materials inventory (throughput × days)
- [ ] Finished goods inventory - Fresh-pack (sales × days)
- [ ] Finished goods inventory - Frozen (sales × days)
- [ ] Accounts receivable (revenue × days)
- [ ] Seeds-on-credit receivables (seed sales × credit days)
- [ ] Accounts payable - Suppliers (purchases × days)
- [ ] Accounts payable - Farmers (farmgate purchases × days)
- [ ] Seasonal working capital peak (multiplier application)
- [ ] Working capital changes by year (for cash flow)

#### Sheet 10: Financing & Debt Schedule
**Status:** ⏳ Pending
- [ ] Total project cost (CAPEX + initial WC)
- [ ] Funding sources (equity, senior debt, mezzanine, grant) by %
- [ ] Senior debt drawdown schedule
- [ ] Senior debt interest calculation (rate × outstanding balance)
- [ ] Senior debt principal repayment (post-grace period)
- [ ] Senior debt balance by year
- [ ] Mezzanine debt drawdown, interest, repayment, balance
- [ ] Total debt service by year (interest + principal)
- [ ] Debt service coverage ratio (DSCR) calculation

#### Sheet 11: Taxation
**Status:** ⏳ Pending
- [ ] Taxable income calculation (EBITDA - depreciation - interest)
- [ ] Tax loss carryforward tracking
- [ ] CIT calculation (with tax holiday and reduced rate periods)
- [ ] Tax credit application (during operation phase)
- [ ] VAT on sales and purchases (recoverable calculation)
- [ ] Withholding taxes (interest, dividends)
- [ ] Net tax payable by year

#### Sheet 12: P&L Statement
**Status:** ⏳ Pending
- [ ] Revenue (total from Revenue sheet)
- [ ] Raw materials cost (from Raw Materials sheet)
- [ ] Gross margin
- [ ] Operating expenses (labor, utilities, consumables, other OPEX)
- [ ] EBITDA
- [ ] Depreciation
- [ ] EBIT
- [ ] Interest expense (from Debt Schedule)
- [ ] EBT (Earnings Before Tax)
- [ ] Tax expense (from Taxation sheet)
- [ ] Net income
- [ ] P&L by year (Year 1-10)

#### Sheet 13: Cash Flow Statement
**Status:** ⏳ Pending
- [ ] Operating cash flow (Net income + depreciation - working capital changes)
- [ ] Investing cash flow (CAPEX by year)
- [ ] Financing cash flow (debt drawdown, debt repayment, equity injection, dividends)
- [ ] Net cash flow by year
- [ ] Cumulative cash flow
- [ ] Free cash flow to equity (FCFE)
- [ ] Free cash flow to project (FCFF)

#### Sheet 14: Returns Analysis
**Status:** ⏳ Pending
- [ ] Project IRR (all cash flows)
- [ ] Equity IRR (post-debt cash flows)
- [ ] NPV @ discount rate (from Assumptions)
- [ ] DSCR by year (with covenant tracking)
- [ ] Payback period (equity payback, debt payback)
- [ ] Break-even analysis (volume, price, utilization)

#### Sheet 15: Development Impact
**Status:** ⏳ Pending
- [ ] Direct jobs created (construction phase, operations phase)
- [ ] Indirect jobs (outgrower farmers × family workers, logistics, downstream)
- [ ] Women employment (% of workforce × total jobs)
- [ ] Farmer income impact (# farmers × income increase)
- [ ] Women farmers (% × total farmers)
- [ ] Import substitution value (frozen fries + seeds)
- [ ] Export revenue (% of sales × total revenue)
- [ ] Local content (% of costs sourced locally)
- [ ] CO₂ reduction (import displacement calculation)

---

## ⏳ PHASE 3: OUTPUT ENHANCEMENTS (PENDING)

**Status:** ⏳ Pending (Day 3-4)

**Target Completion:** February 2, 2026

### Enhancements to Build:

#### Dashboard Sheet
- [ ] Executive KPI summary (IRR, NPV, DSCR, Revenue, EBITDA, Jobs)
- [ ] Fresh-pack vs Frozen revenue split chart
- [ ] 4 Regional depot status indicators
- [ ] Farmer network growth curve (target vs actual)
- [ ] Animal feed valorization metrics
- [ ] Phase 1/2/3 milestone tracker
- [ ] Development impact scorecard

#### Sensitivity Analysis Sheet
- [ ] Tornado chart: Equity IRR sensitivity to 7 key variables
  1. Capacity utilization / farmer yields
  2. Farmgate ware potato price
  3. Fresh-pack selling price
  4. Frozen fries selling price
  5. CAPEX overruns
  6. Operating cost increases
  7. Exchange rate (XAF/USD)
- [ ] Two-way sensitivity table: Equity IRR (Utilization × Product Prices)
- [ ] Two-way sensitivity table: DSCR (Throughput × Farmgate Costs)
- [ ] Two-way sensitivity table: NPV (CAPEX × Revenue)

#### Scenario Comparison
- [ ] Base case outputs (IRR, NPV, DSCR, Revenue, Costs, Net Income)
- [ ] Downside case outputs
- [ ] Upside case outputs
- [ ] Side-by-side comparison table
- [ ] Scenario summary chart

---

## ⏳ PHASE 4: QUALITY ASSURANCE (PENDING)

**Status:** ⏳ Pending (Day 4)

**Target Completion:** February 3, 2026

### QA Checklist:

- [ ] Formula audit (zero errors: #REF!, #VALUE!, #DIV/0!, #NAME?, #NUM!, #N/A, #NULL!)
- [ ] Circular reference check (zero circular references)
- [ ] Scenario toggle test (Base/Downside/Upside switch correctly)
- [ ] Sensitivity analysis functionality test
- [ ] TPS toggle test (enable/disable TPS pathway)
- [ ] Phase timing test (Phase 1/2/3 trigger correctly)
- [ ] Google Sheets compatibility test
- [ ] Sample data population test (enter test values, verify calculations)
- [ ] Audit trail documentation

---

## ⏳ PHASE 5: DOCUMENTATION (PENDING)

**Status:** ⏳ Pending (Day 4-5)

**Target Completion:** February 4, 2026

### Documentation Deliverables:

#### User Guide (Documentation Sheet in Excel)
- [ ] How to use the model (navigation, input entry, scenario switching)
- [ ] Assumptions sheet guide (section-by-section explanation)
- [ ] Output interpretation guide (Dashboard, P&L, Cash Flow, Returns)
- [ ] Sensitivity analysis guide (how to read tornado charts)
- [ ] Common troubleshooting tips

#### Assumptions Memorandum (Separate Word/PDF)
- [ ] Rationale for key assumptions (yields, prices, capacity utilization, CAPEX, financing terms)
- [ ] Benchmarking sources (CIP Malawi, Agrico Kenya, regional comparables)
- [ ] Risk factors and sensitivities
- [ ] Scenario definitions (Base, Downside, Upside)

#### Model Navigation Guide
- [ ] Sheet flow diagram (data flow from Assumptions → Calculations → Outputs)
- [ ] Formula logic documentation (key calculation methodologies)
- [ ] Color coding reference
- [ ] Keyboard shortcuts and tips

#### CAPEX/OPEX Annex (Separate Excel)
- [ ] Detailed CAPEX breakdown by line item (equipment vendor quotes ready to populate)
- [ ] Detailed OPEX breakdown by category (calculation notes)
- [ ] Regional depot specifications (capacity, staffing, costs)

---

## 📊 DAILY PROGRESS LOG

### Day 1: January 29, 2026 ✅

**Completed:**
- ✅ Created backup of v3.0 model
- ✅ Built complete Assumptions sheet structure (21 sections, 426 rows)
- ✅ Committed to git and pushed to remote
- ✅ Verified structure (all sections A-U present)

**Time:** ~2 hours
**Progress:** 40% → Phase 1 complete

**Files Created:**
- `Santa_Fresh_Financial_Model_v4.0.xlsx`
- `build_santa_fresh_model.py`
- `build_santa_fresh_complete.py`
- Backup: `Financial_Model_Agricultural_Processing_v3.0_BEFORE_RESTRUCTURE.xlsx`

---

### Day 2: January 30, 2026 (Planned)

**Planned Work:**
- [ ] Build Calculations sheet (derived values)
- [ ] Build Revenue sheet
- [ ] Build Raw Materials Cost sheet
- [ ] Build Operating Costs sheet
- [ ] Build Seed Operations sheet
- [ ] Build Regional Depot Costs sheet

**Target:** Complete 6 calculation sheets (30% of Phase 2)

---

### Day 3: January 31, 2026 (Planned)

**Planned Work:**
- [ ] Build CAPEX Schedule sheet
- [ ] Build Depreciation Schedule sheet
- [ ] Build Working Capital sheet
- [ ] Build Financing & Debt Schedule sheet
- [ ] Build Taxation sheet
- [ ] Build P&L Statement sheet
- [ ] Build Cash Flow Statement sheet

**Target:** Complete remaining 7 calculation sheets + 2 financial statements (Phase 2 complete)

---

### Day 4: February 1-2, 2026 (Planned)

**Planned Work:**
- [ ] Build Returns Analysis sheet
- [ ] Build Development Impact sheet
- [ ] Enhance Dashboard sheet
- [ ] Build Sensitivity Analysis sheet
- [ ] Build Scenario Comparison
- [ ] Comprehensive QA testing

**Target:** Complete Phase 3 (output enhancements) + Phase 4 (QA)

---

### Day 5: February 3-4, 2026 (Planned)

**Planned Work:**
- [ ] Create User Guide (Documentation sheet)
- [ ] Create Assumptions Memorandum
- [ ] Create Model Navigation Guide
- [ ] Create CAPEX/OPEX Annex
- [ ] Final review and delivery

**Target:** Complete Phase 5 (documentation) + Final delivery

---

## 🎯 COMPLETION CRITERIA

The model will be considered complete when:

1. ✅ All 21 Assumptions sections (A-U) are built and formatted
2. ⏳ All 15 calculation/financial statement sheets are built with correct formula logic
3. ⏳ All formulas reference Assumptions sheet (no hard-coded values)
4. ⏳ Dashboard and enhanced outputs are functional
5. ⏳ Sensitivity analysis and scenario comparison work correctly
6. ⏳ Zero formula errors (comprehensive audit passed)
7. ⏳ Zero circular references
8. ⏳ Google Sheets compatibility verified
9. ⏳ Complete user documentation provided
10. ⏳ User can populate blank Assumptions and see full model calculate

---

## 📁 FILES IN REPOSITORY

**Current Files:**
- `Santa_Fresh_Financial_Model_v4.0.xlsx` - Main model (Assumptions complete, calculations in progress)
- `Santa_Fresh_Financial_Model_v4.0_WIP.xlsx` - Intermediate WIP file (Sections A-C only)
- `Financial_Model_Agricultural_Processing.xlsx` - Original v3.0 model (current baseline)
- `Financial_Model_Agricultural_Processing_v3.0_BEFORE_RESTRUCTURE.xlsx` - Backup
- `Financial_Model_Agricultural_Processing_BASIC.xlsx` - Archive (4-sheet version)
- `build_santa_fresh_model.py` - Base model builder script
- `build_santa_fresh_complete.py` - Complete builder with all sections
- `PROJECT_DATA_COLLECTION_QUESTIONNAIRE.md` - Completed user questionnaire
- `MODEL_RESTRUCTURING_ACTION_PLAN.md` - Detailed restructuring plan
- `GAP_ANALYSIS_Potato_Value_Chain.md` - Gap analysis vs operational flow
- `OPERATIONAL_FLOW_vs_MODEL_COMPARISON.md` - Side-by-side comparison

---

## 🔗 NEXT STEPS

**Immediate (Day 1-2):**
Continue with Phase 2 - building calculation sheets and formula logic.

**User Action:**
- Review Assumptions sheet structure in `Santa_Fresh_Financial_Model_v4.0.xlsx`
- Provide feedback on any missing input categories
- Begin gathering actual figures to populate (vendor quotes, budget estimates, financing terms)

**Builder Action (Me):**
- Continue building calculation sheets
- Ensure all formulas reference Assumptions
- Test scenario switching as sheets are built
- Commit progress daily

---

**Last Updated:** January 29, 2026 - 08:50 UTC
**Next Update:** January 30, 2026 (Day 2 progress)

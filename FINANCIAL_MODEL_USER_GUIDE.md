# Financial Model User Guide
## Agricultural Processing Project - Control Panel Architecture

---

## Overview

This financial model uses a **Control Panel Architecture** where:
- **ALL inputs** are entered in ONE place: the **Assumptions sheet**
- **ALL other sheets** automatically calculate based on these assumptions
- **Blue cells** = your inputs (change these)
- **Yellow cells** = calculations (don't change these)

---

## Quick Start

### Step 1: Open the Model
Open `Financial_Model_Agricultural_Processing.xlsx` in Microsoft Excel or Google Sheets.

### Step 2: Start with the Dashboard
The **Dashboard** sheet gives you a high-level overview:
- Total investment required
- Financing structure (equity, debt, grants)
- Key returns (IRR, NPV, DSCR)
- Critical metrics at a glance

### Step 3: Input Your Data in Assumptions Sheet
Go to the **Assumptions** sheet. This is your control panel.

**ONLY EDIT THE BLUE CELLS** - these are your inputs.

All other worksheets will automatically update when you change assumptions.

---

## The Assumptions Sheet (Control Panel)

### Section A: Project Timeline & Phasing
**What to input:**
- Model start date (when does your project begin?)
- Model horizon (how many years to model? Default: 10 years)
- Construction periods for each phase (in months)

**Example:**
- Start date: January 2026
- Phase 1 (Seed): 18 months
- Phase 2 (Outgrower): 24 months
- Phase 3 (Processing): 36 months

### Section B: Production & Capacity
**What to input:**

**Seed Production:**
- G0 seed import volume (tonnes/year)
- Multiplication ratio (how many times does seed multiply from G0→G1?)
- Example: 100 tonnes G0 × 15x multiplication = 1,500 tonnes G1

**Outgrower Network:**
- Target number of farmers (Year 1, Year 2, Year 3+)
- Hectares per farmer
- Expected yield with certified seed (tonnes/ha)
- Baseline yield without intervention (tonnes/ha)

**Processing Capacity:**
- French fry line capacity (tonnes/hour) - **from your Baixin quote**
- Fresh-pack line capacity (tonnes/hour) - **from your Manter quote**
- Operating hours per day
- Operating days per year
- Capacity utilization ramp-up (Year 1: 40%, Year 2: 60%, Year 3+: 80%)

### Section C: Pricing & Revenue
**What to input:**

**Seed Pricing:**
- G1 certified seed price (XAF per kg)
- Annual price escalation rate (%)

**Ware Potato Pricing:**
- Farmgate price for processing grade potatoes (XAF/kg)
- Farmgate price for table stock (XAF/kg)
- Fresh-pack retail price (XAF/kg)
- **Get current market prices from Santa, Douala, Yaoundé**

**Processed Products:**
- Frozen french fries price (XAF/kg) - **benchmark against imports**
- Animal feed by-product price (XAF/kg)
- Conversion rates (how much input becomes output?)
  - Fry conversion: 62.5% (typical industry standard)
  - Feed by-product: 80% of waste can be converted

### Section D: Operating Costs
**What to input:**

**Seed Production Costs:**
- G0 import cost (XAF/kg)
- Multiplication cost per kg of output
- Storage costs

**Outgrower Support:**
- Input package cost per farmer (seeds, fertilizer, training)
- Extension services cost per farmer
- Payment terms (immediate, 30 days, etc.)

**Processing Costs (per kg of output):**
- Direct labor
- Utilities (electricity, water)
- Packaging materials
- Quality control
- Maintenance (% of CAPEX per year)

**Overhead & Administration:**
- Management salaries (monthly)
- Administrative staff (monthly)
- Office & utilities
- Insurance (% of assets)
- Professional services (legal, audit, etc.)

**Logistics & Distribution:**
- Transport cost per tonne-km
- Average distribution distance
- Cold storage costs

**Cost Escalation:**
- General inflation rate (%) - applies to all costs annually

### Section E: Capital Expenditure (CAPEX)
**What to input:**

This is where you input YOUR actual project costs.

**Phase 1: Seed Multiplication**
- Aeroponic EGS facility cost
- Cold storage for seeds
- Nucleus farm equipment
- Greenhouse structures
- Contingency (%)

**Phase 2: Outgrower Network**
- Training center
- Field equipment
- Input warehouse
- Working capital facility
- Contingency (%)

**Phase 3: Processing Facility** ⭐ **KEY SECTION**
- **French fry line (from Baixin quote)** - Input the total cost from your PDF
- **Fresh-pack line (from Manter quote)** - Input the total cost from your PDF
- **CA storage facility (10,000T)** - Get quote from suppliers
- Factory building & civil works
- Utilities infrastructure
- Effluent treatment plant
- Contingency (%) - higher for larger phases

**Phase 4: Logistics & Distribution**
- Number of reefer trucks needed
- Cost per reefer truck
- Number of delivery vans
- Cost per van
- Regional cold storage depots
- Contingency (%)

**Phase 5: Circular Economy**
- Feed pelletizer line
- Water recycling system
- Biogas digester
- Contingency (%)

**The model automatically calculates total project CAPEX.**

### Section F: Depreciation
**What to input:**
- Useful life for different asset classes (buildings, machinery, equipment, vehicles)
- Residual value (%)
- Depreciation method (straight-line is default)
- Asset classification (what % of your CAPEX is buildings vs machinery?)

### Section G: Financing Structure
**What to input:**

**Equity:**
- Sponsor equity as % of total CAPEX
- Required equity IRR hurdle rate
- Dividend policy

**Senior Debt (DFI):**
- Senior debt as % of total CAPEX
- Interest rate (fixed %)
- Tenor (years)
- Grace period (years)
- Arrangement fee (%)
- Commitment fee (% on undrawn balance)

**Subordinated Debt / Mezzanine:**
- Mezzanine as % of total CAPEX
- Interest rate (%)
- PIK (Payment-in-Kind) option? (Yes/No)
- PIK rate if applicable
- Tenor (years)
- Grace period (years)

**Grant / Technical Assistance:**
- Grant amount (XAF)
- Purpose (TA, training, etc.)
- Disbursement timing

### Section H: Tax & Incentives (Cameroon)
**What to input:**
- Standard corporate income tax rate (33%)
- Installation phase duration (years)
- Customs duty exemption (Yes/No)
- VAT exemption (Yes/No)
- CIT holiday period (years)
- Reduced CIT rate after holiday (%)
- Tax credit (% - based on project category)
- Loss carry-forward period (years)

**These are set based on Cameroon's Investment Code 2013 and subsequent updates.**

### Section I: Working Capital Assumptions
**What to input:**
- Raw materials inventory (days)
- Finished goods inventory (days)
- Accounts receivable (days)
- Accounts payable (days)
- Farmer payment terms
- Seasonal working capital peak multiplier
- Cash buffer (days of operating costs)

### Section J: Macroeconomic Assumptions
**What to input:**
- XAF/USD exchange rate (for USD reporting)
- General inflation rate (%/year)
- USD reporting required? (Yes/No)
- Discount rate for NPV calculations (%)
- Terminal growth rate (%)

### Section K: Scenario Toggles
**What to input:**
- Active scenario (dropdown: Base, Downside, Upside)

**Downside Scenario Adjustments:**
- Yield reduction (%)
- Price reduction (%)
- CAPEX overrun (%)
- Operating cost increase (%)
- Ramp-up delay (months)

**Upside Scenario Adjustments:**
- Yield improvement (%)
- Price premium (%)
- CAPEX savings (%)
- Operating cost reduction (%)
- Accelerated ramp-up (months)

---

## Other Worksheets (Auto-Calculate)

### Timeline
Shows the full project timeline month-by-month with phases and milestones.

### Revenue
Calculates all revenue streams:
- Seed sales revenue
- Ware potato procurement value
- French fries revenue
- Fresh-pack revenue
- Animal feed by-product revenue

**All formulas link back to Assumptions sheet.**

### Operating Costs
Calculates all operating expenses:
- Seed production costs
- Outgrower support costs
- Processing costs
- Overhead & administration
- Logistics & distribution

**All formulas link back to Assumptions sheet.**

### CAPEX Schedule
Shows capital expenditure by phase and year:
- When each phase spends money
- Cumulative CAPEX over time
- Matches construction periods from Assumptions

### Debt Schedule
Calculates debt dynamics:
- Drawdowns (matched to CAPEX schedule)
- Principal repayments (after grace periods)
- Interest expense
- Commitment fees
- Total debt service by year

### P&L Statement
Standard income statement:
- Revenue
- Operating costs
- EBITDA
- Depreciation
- EBIT
- Interest expense
- EBT (Earnings Before Tax)
- Tax expense
- Net Income

### Returns Analysis
Key financial metrics:
- Project IRR
- Equity IRR
- NPV @ 12%
- Payback period
- EBITDA margins
- Net margins
- Return on assets
- Return on equity
- Debt/Equity ratio
- Interest coverage ratio
- DSCR (Debt Service Coverage Ratio)

### Sensitivity Analysis
Tests how changes in key assumptions affect returns:
- Yield variations
- Pricing variations
- CAPEX variations
- Operating cost variations
- Capacity utilization
- Interest rates
- Ramp-up timing

### Dashboard
Executive summary showing:
- Total investment
- Financing structure
- Key returns
- Critical metrics

---

## How to Use This Model

### Use Case 1: Input Your Own Project Data

**Step 1:** Gather your data
- Baixin equipment quote (French fry line)
- Manter equipment quote (Fresh-pack line)
- CA storage quotes
- Building/construction estimates
- Vehicle costs
- Current market prices (farmgate, retail)
- Financing terms from lenders

**Step 2:** Go to Assumptions sheet

**Step 3:** Input data into BLUE CELLS ONLY
- Start with Section E (CAPEX) - input your actual equipment costs
- Fill in Section C (Pricing) - input current market prices
- Complete Section D (Operating Costs) - estimate your costs
- Configure Section G (Financing) - input your financing terms
- Set Section B (Production & Capacity) - based on equipment specs

**Step 4:** Review other sheets
- Check Revenue sheet - does revenue look reasonable?
- Check Operating Costs sheet - are costs realistic?
- Check P&L Statement - when does profitability happen?
- Check Returns Analysis - acceptable IRR? Positive NPV?
- Check Debt Schedule - manageable debt service?

**Step 5:** Run scenarios
- Change Section K (Scenario Toggles) to test Downside/Upside
- See how sensitive returns are to key assumptions

### Use Case 2: Analyze Different Scenarios

**Base Case:**
- Conservative assumptions
- Moderate capacity utilization
- Market prices

**Downside Case:**
- Lower yields (-20%)
- Lower prices (-15%)
- CAPEX overruns (+15%)
- Higher operating costs (+10%)
- Ramp-up delays (+6 months)

**Upside Case:**
- Higher yields (+10%)
- Premium pricing (+10%)
- CAPEX savings (-5%)
- Operating efficiencies (-5%)
- Faster ramp-up (-3 months)

Change the "Active scenario" dropdown in Section K to switch scenarios.

### Use Case 3: Optimize Financing Structure

**Experiment with:**
- Equity % (Section G)
- Senior debt % (Section G)
- Mezzanine debt % (Section G)
- Interest rates (Section G)
- Grace periods (Section G)

**Watch the impact on:**
- Equity IRR (Returns Analysis sheet)
- DSCR (Returns Analysis sheet)
- Debt service (Debt Schedule sheet)
- Cash flow (P&L Statement)

**Find the optimal structure that:**
- Maximizes equity returns
- Maintains DSCR > 1.2
- Meets lender requirements
- Minimizes financing costs

### Use Case 4: Present to Investors/Lenders

**For Equity Investors:**
- Show Dashboard sheet (high-level overview)
- Show Returns Analysis (Equity IRR, ROE, payback)
- Show Sensitivity Analysis (risk/return profile)
- Highlight upside scenario potential

**For Debt Lenders:**
- Show Debt Schedule (repayment profile)
- Show DSCR calculations (debt coverage)
- Show downside scenario (stress testing)
- Show collateral value (asset base)

**For Government/Grants:**
- Show job creation metrics
- Show farmer impact (outgrower numbers)
- Show food security impact (production volumes)
- Show tax revenue projections

---

## Key Formulas Explained

### Revenue Formula Example
```
French Fries Revenue (Year 3) =
  Processing capacity (tonnes/hour)
  × Operating hours/day
  × Operating days/year
  × Capacity utilization Year 3
  × Fry conversion rate
  × French fries price
  × 1000 (convert tonnes to kg)
```

All inputs come from Assumptions sheet, so changing one assumption automatically updates revenue.

### DSCR Formula
```
DSCR = (EBITDA - Tax - CAPEX) / (Interest + Principal)
```

Lenders typically require DSCR > 1.2 to ensure you can comfortably service debt.

### IRR Calculation
IRR is calculated on cash flows:
- **Project IRR**: Based on total cash flows (all sources)
- **Equity IRR**: Based on equity cash flows only (after debt service)

The model uses Excel's `IRR()` function on the cash flow array.

---

## Common Questions

### Q: Can I add more years to the model?
**A:** Yes. In the Python script (`build_financial_model.py`), change `self.model_years = 10` to your desired number, then re-run the script.

### Q: Can I add more revenue streams?
**A:** Yes. Edit the Revenue sheet and add new rows with formulas linking to Assumptions sheet. Add corresponding assumptions to Section C.

### Q: What if my CAPEX phasing is different?
**A:** Edit Section A (construction periods) in Assumptions. The CAPEX Schedule automatically distributes spending based on these periods.

### Q: How do I add more detail to costs?
**A:** Add new rows to Section D (Operating Costs) in Assumptions. Then add corresponding formulas in the Operating Costs sheet.

### Q: Can I change the currency?
**A:** Yes. The model uses XAF throughout. To convert to USD, use Section J (exchange rate). You can also edit all "XAF" labels to "USD" if preferred.

### Q: What if I don't have all the data yet?
**A:** Use placeholder estimates in the Assumptions sheet. Mark cells with comments (right-click → Insert Comment) noting "TBC" or "Estimate - needs validation".

### Q: How do I share this with my team?
**A:** Save the Excel file to a shared drive or cloud storage (Google Drive, OneDrive, Dropbox). Multiple people can view, but ensure only one person edits Assumptions at a time to avoid conflicts.

---

## Best Practices

### 1. Document Your Assumptions
Add comments to input cells explaining:
- Where the number came from (quote, market data, estimate)
- Date of the assumption
- Any caveats or uncertainties

**How:** Right-click cell → Insert Comment

### 2. Use Named Ranges
For frequently referenced cells, create named ranges:
- Select cell (e.g., C170 "Total CAPEX")
- In Name Box (left of formula bar), type "TotalCAPEX"
- Use in formulas: `=TotalCAPEX*0.25` instead of `=C170*0.25`

### 3. Version Control
Save dated versions:
- `Financial_Model_v1.0_2026-01-23.xlsx` (initial version)
- `Financial_Model_v1.1_2026-02-15.xlsx` (updated CAPEX)
- `Financial_Model_v2.0_2026-03-01.xlsx` (revised financing)

### 4. Regular Reviews
Schedule monthly reviews to:
- Update actual costs vs. budget
- Revise assumptions based on new data
- Re-run scenarios
- Adjust projections

### 5. Sensitivity Testing
Always test these variables:
- Yield (±20%)
- Pricing (±15%)
- CAPEX (±15%)
- Operating costs (±10%)
- Ramp-up timing (±6 months)

If returns are still acceptable in downside case, your project is robust.

---

## Troubleshooting

### Issue: Formulas showing #REF! error
**Solution:** A cell reference was deleted. Check the Assumptions sheet - ensure no rows were deleted.

### Issue: Circular reference warning
**Solution:** The model shouldn't have circular references. If you see this, check for accidental self-referencing formulas.

### Issue: IRR showing #NUM! error
**Solution:** IRR can't calculate if cash flows don't change signs (negative to positive). Ensure your project has both outflows (CAPEX) and inflows (profits).

### Issue: Very slow calculation
**Solution:** Excel is recalculating. For large models:
- Go to Formulas → Calculation Options → Manual
- Recalculate manually with F9 after changes
- Switch back to Automatic when done

### Issue: Different results in Google Sheets vs Excel
**Solution:** Some advanced functions behave differently. Excel is recommended for financial models. If using Sheets:
- Check date formulas (may need adjustment)
- Verify number formatting
- Test IRR calculations

---

## Next Steps

### 1. Populate Your Data
Start filling in Assumptions sheet with your actual project data:
- [ ] CAPEX costs (Section E)
- [ ] Market prices (Section C)
- [ ] Operating costs (Section D)
- [ ] Production targets (Section B)
- [ ] Financing terms (Section G)

### 2. Validate Results
Review auto-calculated sheets:
- [ ] Revenue projections realistic?
- [ ] Costs comprehensive?
- [ ] Returns attractive?
- [ ] Debt serviceable?

### 3. Run Scenarios
Test different cases:
- [ ] Base case
- [ ] Downside case
- [ ] Upside case

### 4. Refine Model
Add project-specific details:
- [ ] More revenue streams?
- [ ] More cost categories?
- [ ] Different phasing?
- [ ] Additional sensitivity variables?

### 5. Present & Decide
Use the model to:
- [ ] Present to board/investors
- [ ] Negotiate with lenders
- [ ] Apply for grants/incentives
- [ ] Make go/no-go decision

---

## Support

For questions or issues with this financial model:

1. **Review this guide** - most questions are answered here
2. **Check the Assumptions sheet** - ensure inputs are correct
3. **Review the Python script** (`build_financial_model.py`) - see how formulas are constructed
4. **Modify the script** - customize to your needs and regenerate

---

## Appendix: Model Specifications

**File:** `Financial_Model_Agricultural_Processing.xlsx`

**Sheets:**
1. Dashboard (executive summary)
2. Assumptions (control panel - all inputs)
3. Timeline (monthly project timeline)
4. Revenue (revenue calculations)
5. Operating Costs (OPEX calculations)
6. CAPEX Schedule (capital expenditure by phase)
7. Debt Schedule (debt dynamics)
8. P&L Statement (income statement)
9. Returns Analysis (key metrics)
10. Sensitivity Analysis (scenario testing)

**Key Features:**
- Control panel architecture (single input sheet)
- Fully formula-driven (no hard-coded values)
- Scenario analysis built-in
- 10-year projection horizon (configurable)
- Multi-phase CAPEX modeling
- Debt amortization schedules
- Tax holiday modeling (Cameroon Investment Code)
- Working capital calculations
- Return metrics (IRR, NPV, DSCR)

**Built with:**
- Python 3.11
- openpyxl library
- python-dateutil library

**Last updated:** January 23, 2026

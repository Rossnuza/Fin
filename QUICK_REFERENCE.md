# Financial Model - Quick Reference Card

## 🎯 The Golden Rule
**ONLY edit BLUE cells in the Assumptions sheet. Everything else auto-calculates.**

---

## ⚡ Quick Start (5 minutes)

1. **Open:** `Financial_Model_Agricultural_Processing.xlsx`
2. **View:** Dashboard sheet (see overview)
3. **Edit:** Assumptions sheet (blue cells only)
4. **Review:** Returns Analysis sheet (see if project makes sense)
5. **Test:** Change scenario dropdown (Assumptions!K45) to "Downside" or "Upside"

---

## 📊 Sheet Navigation

| Sheet | Purpose | Action |
|-------|---------|--------|
| **Dashboard** | Executive summary | View only - shows key metrics |
| **Assumptions** | Control panel | EDIT HERE - all blue cells |
| **Timeline** | Project schedule | View only - auto-calculates |
| **Revenue** | Revenue projections | View only - links to Assumptions |
| **Operating Costs** | Cost projections | View only - links to Assumptions |
| **CAPEX Schedule** | Capital spending | View only - links to Assumptions |
| **Debt Schedule** | Debt dynamics | View only - links to Assumptions |
| **P&L Statement** | Income statement | View only - auto-calculates |
| **Returns Analysis** | Key metrics | View only - IRR, NPV, DSCR |
| **Sensitivity Analysis** | Scenario testing | View only - stress tests |

---

## 🔧 Critical Inputs to Fill In

### Priority 1: CAPEX (Assumptions Section E)
```
Row 145: French fry line (Baixin quote)        → [Your number]
Row 146: Fresh-pack line (Manter quote)       → [Your number]
Row 147: CA storage (10,000T)                 → [Your number]
Row 148: Factory building                     → [Your number]
```

### Priority 2: Pricing (Assumptions Section C)
```
Row 45:  G1 seed price (XAF/kg)               → [Market price]
Row 50:  Farmgate price processing (XAF/kg)   → [Santa prices]
Row 52:  Fresh-pack retail (XAF/kg)           → [Douala/Yaoundé]
Row 56:  Frozen fries price (XAF/kg)          → [Import benchmark]
```

### Priority 3: Capacity (Assumptions Section B)
```
Row 47:  Fry line capacity (tonnes/hour)      → [From Baixin spec]
Row 48:  Fresh-pack capacity (tonnes/hour)    → [From Manter spec]
Row 50-52: Capacity utilization (%)           → [Conservative: 40/60/80]
```

### Priority 4: Financing (Assumptions Section G)
```
Row 186: Sponsor equity (%)                   → [Your equity %]
Row 189: Senior debt (%)                      → [Lender terms]
Row 190: Interest rate (%)                    → [Lender quote]
Row 198: Mezzanine (%)                        → [If applicable]
```

---

## 📈 Key Metrics to Watch

### Returns (Returns Analysis Sheet)
- **Project IRR:** Should be > 15%
- **Equity IRR:** Should be > 20% (investor hurdle)
- **NPV @ 12%:** Should be positive (value creation)
- **Payback:** Should be < 7 years

### Debt Coverage (Returns Analysis Sheet)
- **Min DSCR:** Should be > 1.2 (lender requirement)
- **Avg DSCR:** Should be > 1.5 (comfortable cushion)
- **Interest coverage:** Should be > 3.0x

### Profitability (P&L Statement)
- **EBITDA margin:** Target > 25%
- **Net margin:** Target > 15%
- **Revenue CAGR:** Target > 20%

---

## 🔄 Scenario Testing

### Change scenario:
1. Go to Assumptions sheet
2. Cell C219: Change dropdown from "Base" to "Downside" or "Upside"
3. All sheets auto-update

### What happens:
- **Downside:** -20% yield, -15% price, +15% CAPEX, +6mo delay
- **Upside:** +10% yield, +10% price, -5% CAPEX, -3mo acceleration

### Decision rule:
- If Downside scenario still shows Equity IRR > 15%, project is robust
- If Downside scenario shows negative NPV, project is risky

---

## 🎨 Color Code

| Color | Meaning | Action |
|-------|---------|--------|
| 🔵 Blue | Input cell | Edit these |
| 🟡 Yellow | Calculation | Don't touch |
| 🟢 Green | Section header | Visual guide |
| ⚫ Gray | Column header | Visual guide |
| 🔴 Red | Error/warning | Fix issue |

---

## 🚨 Common Mistakes to Avoid

### ❌ DON'T:
1. Edit yellow cells (calculations)
2. Delete rows in Assumptions sheet (breaks formulas)
3. Change formulas in other sheets (breaks model)
4. Add data outside the Assumptions sheet (loses control)
5. Forget to save versions (use dates: v1.0_2026-01-23)

### ✅ DO:
1. Only edit blue cells in Assumptions
2. Add comments to cells (right-click → Insert Comment)
3. Save dated versions regularly
4. Test scenarios before presenting
5. Document where numbers came from

---

## 🔍 Validation Checklist

Before presenting to investors/lenders:

**Revenue Sanity Check:**
- [ ] Seed revenue = Volume × Price ✓
- [ ] Processing revenue = Capacity × Utilization × Price ✓
- [ ] Total revenue grows reasonably (not 10x overnight) ✓

**Cost Sanity Check:**
- [ ] Operating costs scale with volume ✓
- [ ] Fixed costs are truly fixed ✓
- [ ] Variable costs are truly variable ✓
- [ ] Total costs < 70% of revenue at maturity ✓

**CAPEX Sanity Check:**
- [ ] Phase timing makes sense (don't build processing before seed) ✓
- [ ] Contingencies included (10-15%) ✓
- [ ] Equipment costs verified with quotes ✓
- [ ] Total CAPEX = sum of all phases ✓

**Financing Sanity Check:**
- [ ] Equity + Debt + Grants = Total CAPEX ✓
- [ ] Debt terms match lender quotes ✓
- [ ] Grace periods align with revenue ramp ✓
- [ ] Can service debt in all scenarios ✓

**Returns Sanity Check:**
- [ ] IRR > cost of capital ✓
- [ ] NPV > 0 ✓
- [ ] DSCR > 1.2 in all years ✓
- [ ] Payback within project life ✓

---

## 💡 Pro Tips

### Tip 1: Start Conservative
Use conservative assumptions first (lower revenue, higher costs).
If project still works, you have a robust case.

### Tip 2: Benchmark Everything
- Seed prices → compare to market
- Processing costs → compare to industry standards
- CAPEX → get multiple quotes
- Returns → compare to similar projects

### Tip 3: Stress Test Relentlessly
Change one assumption at a time and see impact:
- What if yield is 20% lower?
- What if prices drop 15%?
- What if CAPEX overruns by 20%?
- What if ramp-up delays 1 year?

### Tip 4: Focus on Key Drivers
The model has 100+ inputs, but only ~10 matter most:
1. Processing capacity (tonnes/hour)
2. Capacity utilization (%)
3. Product prices (XAF/kg)
4. Processing CAPEX (XAF)
5. Operating costs per kg
6. Interest rate (%)
7. Equity % (affects leverage and returns)

### Tip 5: Tell a Story
Numbers alone don't convince. Use the model to tell a story:
- Year 1-2: Building foundation (seed multiplication, farmers)
- Year 3-4: Scaling up (processing comes online)
- Year 5+: Harvesting returns (full capacity, profitable)

---

## 📞 Getting Help

### Model not calculating?
1. Press F9 to force recalculation
2. Check Formulas → Calculation Options → set to Automatic
3. Look for #REF! or #NUM! errors

### Results look wrong?
1. Check Assumptions sheet - any typos in blue cells?
2. Verify units (kg vs tonnes, monthly vs annual)
3. Check Timeline sheet - phases in right order?

### Want to modify model?
1. Read `FINANCIAL_MODEL_USER_GUIDE.md` (comprehensive)
2. Review `build_financial_model.py` (source code)
3. Make changes to Python script and regenerate

---

## 📁 File Structure

```
Fin/
├── Financial_Model_Agricultural_Processing.xlsx    ← The model (edit this)
├── FINANCIAL_MODEL_USER_GUIDE.md                   ← Full documentation
├── QUICK_REFERENCE.md                              ← This file
├── build_financial_model.py                        ← Source code
└── README.md                                        ← Project overview
```

---

## 🎓 Learning Path

### Beginner (Day 1):
1. Open model
2. View Dashboard
3. Go to Assumptions, look at blue cells
4. Change one number, watch other sheets update

### Intermediate (Week 1):
1. Input all your actual data
2. Review all auto-calculated sheets
3. Run Base/Downside/Upside scenarios
4. Present to team

### Advanced (Month 1):
1. Customize assumptions (add rows)
2. Add new revenue streams
3. Modify Python script
4. Build custom reports

---

## 🏆 Success Metrics

Your model is ready for investors when:
- [ ] All blue cells have real data (not placeholders)
- [ ] Sources documented (comments on key cells)
- [ ] Returns attractive in Base case (IRR > 20%)
- [ ] Project survives Downside case (NPV > 0, DSCR > 1.2)
- [ ] Debt fully repaid within tenor
- [ ] Equity achieves target returns
- [ ] Presentation deck references model outputs
- [ ] You can explain every assumption

---

## 🚀 Next Actions

**TODAY:**
- [ ] Open the model
- [ ] Review Dashboard
- [ ] List all data you need to collect

**THIS WEEK:**
- [ ] Get equipment quotes (Baixin, Manter, CA storage)
- [ ] Research market prices (farmgate, retail)
- [ ] Contact lenders for financing terms
- [ ] Input all data into Assumptions sheet

**THIS MONTH:**
- [ ] Validate all assumptions with experts
- [ ] Run multiple scenarios
- [ ] Create investor presentation
- [ ] Present to board/investors

**WITHIN 90 DAYS:**
- [ ] Finalize financing structure
- [ ] Close funding round
- [ ] Start construction

---

**Remember: This model is a living document. Update it regularly as you get better data.**

**Good luck with your project! 🎉**

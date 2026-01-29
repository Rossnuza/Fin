#!/usr/bin/env python3
"""
Santa Fresh Model Builder - Complete Version with All Sections A-U

This extends the base builder to include all 21 sections of the Assumptions sheet.
"""

import sys
sys.path.insert(0, '/home/user/Fin')

from build_santa_fresh_model import SantaFreshModelBuilder

class CompleteSantaFreshBuilder(SantaFreshModelBuilder):
    """Extended builder with complete Assumptions sheet (Sections A-U)"""

    def continue_assumptions_sheet(self, ws, row):
        """Continue building Assumptions from Section D onwards"""

        # ===================================================================
        # SECTION D: RAW MATERIAL SOURCING - WARE POTATOES
        # ===================================================================
        row = self._add_section_header(ws, row, "D. RAW MATERIAL SOURCING - WARE POTATOES")

        ware_potato_params = [
            ("Farmgate price - Processing grade", "", "XAF/kg", ""),
            ("Farmgate price - Table stock", "", "XAF/kg", ""),
            ("Raw material price escalation", "", "%/year", ""),
            ("Farmer payment terms", "", "Days", ""),
            ("% sourced from outgrowers", "", "%", ""),
            ("% sourced from EIC farm", "", "%", ""),
            ("% sourced from spot market", "", "%", ""),
        ]

        for label, value, unit, note in ware_potato_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # D1: Ware Potato Seasonality
        row = self._add_subsection_header(ws, row, "D1: Ware Potato Supply Seasonality")

        months = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']

        for month in months:
            row = self._add_input_row(ws, row, f"{month} supply", "", "% of annual", "")

        row += 1

        # ===================================================================
        # SECTION E: SEED OPERATIONS
        # ===================================================================
        row = self._add_section_header(ws, row, "E. SEED OPERATIONS")

        # E1: Traditional Seed Potatoes
        row = self._add_subsection_header(ws, row, "E1: Traditional Seed Potatoes (Agrico/HZPC)")

        trad_seed_params = [
            ("Annual G0 import volume", "", "Tonnes", ""),
            ("G0 import price", "", "XAF/kg", ""),
            ("Multiplication ratio (G0→G1)", "", "Ratio", "e.g., 15 or 20"),
            ("Seed multiplication area", "", "Hectares", ""),
            ("Seed yield", "", "Tonnes/ha", ""),
            ("% sold to outgrowers", "", "%", ""),
            ("% used internally", "", "%", ""),
            ("Seed price to farmers", "", "XAF/kg", ""),
        ]

        for label, value, unit, note in trad_seed_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # E2: True Potato Seeds (TPS)
        row = self._add_subsection_header(ws, row, "E2: True Potato Seeds - TPS (Solynta)")

        tps_params = [
            ("Deploy TPS pathway?", "", "Yes/No", "Toggle for TPS inclusion"),
            ("Annual TPS import", "", "Seeds", "Number of seeds"),
            ("TPS cost per seed", "", "XAF/seed", ""),
            ("Nursery capacity", "", "Seedlings/year", ""),
            ("Cost per seedling produced", "", "XAF/seedling", ""),
            ("Seedling price to farmers", "", "XAF/seedling", ""),
            ("Hectares supported by TPS", "", "Hectares", ""),
        ]

        for label, value, unit, note in tps_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # E3: Seeds-on-Credit Program
        row = self._add_subsection_header(ws, row, "E3: Seeds-on-Credit Program")

        credit_params = [
            ("Credit period", "", "Days", "From planting to settlement"),
            ("Interest rate/markup", "", "%", ""),
            ("Expected default rate", "", "%", ""),
            ("Recovery rate on defaults", "", "%", ""),
        ]

        for label, value, unit, note in credit_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # ===================================================================
        # SECTION F: OUTGROWER NETWORK
        # ===================================================================
        row = self._add_section_header(ws, row, "F. OUTGROWER NETWORK")

        outgrower_params = [
            ("Current number of farmers", "", "Number", ""),
            ("Target farmers - Year 1", "", "Number", ""),
            ("Target farmers - Year 2", "", "Number", ""),
            ("Target farmers - Year 3+", "", "Number", ""),
            ("Average farm size per farmer", "", "Hectares", ""),
            ("Target yield with certified seed", "", "Tonnes/ha", ""),
            ("Baseline yield without certified seed", "", "Tonnes/ha", ""),
            ("Input package cost per farmer", "", "XAF/ha", ""),
            ("Extension cost per farmer", "", "XAF/year", ""),
            ("Free fertilizer distribution", "", "Tonnes/farmer/year", "Digestate/compost"),
            ("Fertilizer value to farmers", "", "XAF/tonne", "Cost savings"),
        ]

        for label, value, unit, note in outgrower_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # ===================================================================
        # SECTION G: EIC-OWNED NUCLEUS FARM
        # ===================================================================
        row = self._add_section_header(ws, row, "G. EIC-OWNED NUCLEUS FARM")

        farm_params = [
            ("Total farm size", "", "Hectares", ""),
            ("Annual land lease cost", "", "XAF/ha", ""),
            ("Hectares for seed multiplication", "", "Hectares", ""),
            ("Hectares for ware potato production", "", "Hectares", ""),
            ("Hectares for rotation crops/other", "", "Hectares", ""),
            ("Farm operating cost", "", "XAF/ha/year", ""),
            ("Farm equipment maintenance", "", "XAF/year", ""),
        ]

        for label, value, unit, note in farm_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # ===================================================================
        # SECTION H: OPERATING COSTS - LABOR
        # ===================================================================
        row = self._add_section_header(ws, row, "H. OPERATING COSTS - LABOR")

        labor_depts = [
            ("H1: Management & Administration", "staff count", "XAF/month"),
            ("H2: Production (Factory Workers)", "staff count", "XAF/month"),
            ("H3: QC & Laboratory", "staff count", "XAF/month"),
            ("H4: Logistics & Distribution", "staff count", "XAF/month"),
            ("H5: Sales & Marketing", "staff count", "XAF/month"),
            ("H6: Field Agents (Outgrower Support)", "staff count", "XAF/month"),
            ("H7: Security & Maintenance", "staff count", "XAF/month"),
        ]

        for dept, unit1, unit2 in labor_depts:
            row = self._add_subsection_header(ws, row, dept)
            row = self._add_input_row(ws, row, "Number of staff", "", "Number", "")
            row = self._add_input_row(ws, row, "Total monthly payroll", "", "XAF/month", "")
            row += 1

        row = self._add_input_row(ws, row, "Labor cost escalation", "", "%/year", "")

        row += 1

        # ===================================================================
        # SECTION I: OPERATING COSTS - UTILITIES
        # ===================================================================
        row = self._add_section_header(ws, row, "I. OPERATING COSTS - UTILITIES")

        # I1: Electricity
        row = self._add_subsection_header(ws, row, "I1: Electricity")

        electricity_params = [
            ("Grid electricity consumption", "", "kWh/year", ""),
            ("Grid electricity tariff", "", "XAF/kWh", ""),
            ("Generator backup hours", "", "Hours/year", ""),
            ("Generator fuel consumption", "", "Liters/hour", ""),
            ("Generator efficiency", "", "kWh/liter", ""),
        ]

        for label, value, unit, note in electricity_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # I2: Water
        row = self._add_subsection_header(ws, row, "I2: Water")

        water_params = [
            ("Water consumption", "", "m³/year", ""),
            ("Water tariff", "", "XAF/m³", ""),
            ("Water recycling rate", "", "%", "WWTP treated water reused"),
        ]

        for label, value, unit, note in water_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # I3: Diesel
        row = self._add_subsection_header(ws, row, "I3: Diesel (Fleet & Generator)")

        diesel_params = [
            ("Fleet diesel consumption", "", "Liters/year", ""),
            ("Diesel price", "", "XAF/liter", ""),
            ("Diesel price escalation", "", "%/year", ""),
        ]

        for label, value, unit, note in diesel_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1
        row = self._add_input_row(ws, row, "Utility cost escalation", "", "%/year", "")

        row += 1

        # ===================================================================
        # SECTION J: OPERATING COSTS - PROCESSING CONSUMABLES
        # ===================================================================
        row = self._add_section_header(ws, row, "J. OPERATING COSTS - PROCESSING CONSUMABLES")

        # J1: Frying Oil
        row = self._add_subsection_header(ws, row, "J1: Frying Oil (Frozen Line)")

        oil_params = [
            ("Oil consumption per tonne frozen fries", "", "Liters/tonne", ""),
            ("Oil price", "", "XAF/liter", ""),
            ("Oil price escalation", "", "%/year", ""),
        ]

        for label, value, unit, note in oil_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # J2-J7: Other consumables (grouped for brevity)
        consumable_categories = [
            ("J2: Packaging Materials - Fresh-Pack", [
                ("Bags/boxes per tonne", "Units/tonne"),
                ("Average cost per unit", "XAF/unit"),
                ("Packaging price escalation", "%/year"),
            ]),
            ("J3: Packaging Materials - Frozen Fries", [
                ("Boxes per tonne", "Units/tonne"),
                ("Average cost per unit", "XAF/unit"),
                ("Packaging price escalation", "%/year"),
            ]),
            ("J4: Processing Additives", [
                ("Salt & seasonings cost", "XAF/tonne processed"),
                ("Anti-oxidants cost", "XAF/tonne processed"),
                ("Additives price escalation", "%/year"),
            ]),
            ("J5: Cleaning & Sanitation", [
                ("Annual cleaning chemicals cost", "XAF/year"),
                ("Escalation", "%/year"),
            ]),
            ("J6: Spare Parts & Maintenance", [
                ("Annual maintenance supplies", "XAF/year"),
                ("Escalation", "%/year"),
            ]),
            ("J7: QC Lab Supplies", [
                ("Annual lab supplies cost", "XAF/year"),
                ("Escalation", "%/year"),
            ]),
        ]

        for category, params in consumable_categories:
            row = self._add_subsection_header(ws, row, category)
            for label, unit in params:
                row = self._add_input_row(ws, row, label, "", unit, "")
            row += 1

        # ===================================================================
        # SECTION K: OPERATING COSTS - OTHER
        # ===================================================================
        row = self._add_section_header(ws, row, "K. OPERATING COSTS - OTHER")

        other_opex = [
            ("Insurance (% of total assets)", "%/year", ""),
            ("Professional services", "XAF/year", "Legal, audit, consulting"),
            ("Marketing & advertising - Year 1", "XAF/year", "Launch campaign"),
            ("Marketing & advertising - Year 2+", "XAF/year", "Ongoing"),
            ("Office supplies & admin utilities", "XAF/year", ""),
            ("Depot rent (4 depots total)", "XAF/year", ""),
            ("Communication (phone, internet)", "XAF/year", ""),
            ("Travel & transportation", "XAF/year", ""),
            ("Training & development", "XAF/year", ""),
            ("Licensing & permits", "XAF/year", ""),
            ("Bank fees & transaction costs", "XAF/year", ""),
            ("Waste disposal", "XAF/year", ""),
            ("General cost inflation", "%/year", ""),
        ]

        for label, unit, note in other_opex:
            row = self._add_input_row(ws, row, label, "", unit, note)

        row += 1

        print(f"Built Assumptions sheet up to row {row} - Sections D-K complete")

        return ws, row

    def build_model(self):
        """Override to build complete model"""
        print("=" * 70)
        print("SANTA FRESH FINANCIAL MODEL BUILDER - COMPLETE VERSION")
        print("=" * 70)
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        print("[1/6] Building Assumptions sheet (Sections A-C)...")
        ws_assumptions, row = self.create_assumptions_sheet()

        print("[2/6] Building Assumptions sheet (Sections D-K)...")
        ws_assumptions, row = self.continue_assumptions_sheet(ws_assumptions, row)

        print("[3/6] Building Assumptions sheet (Sections L-U)...")
        ws_assumptions, row = self.finalize_assumptions_sheet(ws_assumptions, row)

        print()
        print("Model structure created. Saving...")

        # Save the workbook
        filename = "Santa_Fresh_Financial_Model_v4.0.xlsx"
        self.wb.save(filename)

        print(f"✓ Saved: {filename}")
        print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)

        return filename

    def finalize_assumptions_sheet(self, ws, row):
        """Add final sections L-U"""

        # ===================================================================
        # SECTION L: WASTE VALORIZATION - ANIMAL FEED
        # ===================================================================
        row = self._add_section_header(ws, row, "L. WASTE VALORIZATION - ANIMAL FEED")

        feed_params = [
            ("Feed pelletizer operating cost", "", "XAF/tonne feed", ""),
            ("Feed pelletizer capacity utilization", "", "%", ""),
        ]

        for label, value, unit, note in feed_params:
            row = self._add_input_row(ws, row, label, value, unit, note)

        row += 1

        # ===================================================================
        # SECTION M: CAPITAL EXPENDITURE - BY PHASE
        # ===================================================================
        row = self._add_section_header(ws, row, "M. CAPITAL EXPENDITURE - BY PHASE")

        # M1: Phase 1 - Foundation Infrastructure
        row = self._add_subsection_header(ws, row, "M1: Phase 1 - Foundation Infrastructure (Year 0-1)")

        phase1_capex = [
            ("Land lease prepayment", "XAF"),
            ("Site development & civil works", "XAF"),
            ("Factory building", "XAF"),
            ("Office building", "XAF"),
            ("Warehouse buildings", "XAF"),
            ("Pre-processing equipment (grouped)", "XAF"),
            ("Climate storage - Curing cells", "XAF"),
            ("Climate storage - Long-term cells", "XAF"),
            ("Climate storage - Activation cells", "XAF"),
            ("Priva climate control system", "XAF"),
            ("Fresh-pack processing line (complete)", "XAF"),
            ("Animal feed pelletizer", "XAF"),
            ("Finished goods - Ambient warehouse", "XAF"),
            ("Water treatment plant (WTP)", "XAF"),
            ("Wastewater treatment plant (WWTP)", "XAF"),
            ("Power - Backup generators", "XAF"),
            ("Power - Solar (optional)", "XAF"),
            ("Farm equipment & machinery", "XAF"),
            ("Nursery facility (TPS - conditional)", "XAF"),
            ("Reefer trucks - Phase 1 (number)", "Number"),
            ("Cost per reefer truck", "XAF/unit"),
            ("Delivery vans - Phase 1 (number)", "Number"),
            ("Cost per delivery van", "XAF/unit"),
            ("On-site fuel depot", "XAF"),
            ("Furniture, fixtures & IT", "XAF"),
            ("Pre-operating expenses", "XAF"),
            ("Phase 1 contingency", "%"),
        ]

        for label, unit in phase1_capex:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # M2: Phase 2 - Frozen Line & Initial Depot
        row = self._add_subsection_header(ws, row, "M2: Phase 2 - Frozen Line & Initial Depot (Year 2)")

        phase2_capex = [
            ("Frozen french fry line (complete)", "XAF"),
            ("Finished goods - Frozen cold store", "XAF"),
            ("Regional depot - Douala", "XAF"),
            ("Reefer trucks - Phase 2 (number)", "Number"),
            ("Cost per reefer truck", "XAF/unit"),
            ("Delivery vans - Phase 2 (number)", "Number"),
            ("Cost per delivery van", "XAF/unit"),
            ("Phase 2 contingency", "%"),
        ]

        for label, unit in phase2_capex:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # M3: Phase 3 - Regional Depot Expansion
        row = self._add_subsection_header(ws, row, "M3: Phase 3 - Regional Depot Expansion (Year 3)")

        phase3_capex = [
            ("Regional depot - Yaoundé", "XAF"),
            ("Regional depot - Bamenda", "XAF"),
            ("Regional depot - Bafoussam", "XAF"),
            ("Delivery vans - Phase 3 (number)", "Number"),
            ("Cost per delivery van", "XAF/unit"),
            ("TPS nursery scale-up (if validated)", "XAF"),
            ("Phase 3 contingency", "%"),
        ]

        for label, unit in phase3_capex:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # Continue with sections N-U (depot operating costs, working capital, financing, etc.)
        # For brevity, I'll add abbreviated versions

        # SECTION N: REGIONAL DEPOT OPERATING COSTS
        row = self._add_section_header(ws, row, "N. REGIONAL DEPOT OPERATING COSTS")

        depots = ["Douala", "Yaoundé", "Bamenda", "Bafoussam"]
        for idx, depot in enumerate(depots, 1):
            row = self._add_subsection_header(ws, row, f"N{idx}: {depot} Depot")
            depot_params = [
                ("Cold storage capacity", "Tonnes"),
                ("Staff salaries", "XAF/month"),
                ("Electricity", "XAF/month"),
                ("Rent", "XAF/month"),
                ("Security & maintenance", "XAF/month"),
            ]
            for label, unit in depot_params:
                row = self._add_input_row(ws, row, label, "", unit, "")
            row += 1

        # SECTION O: WORKING CAPITAL PARAMETERS
        row = self._add_section_header(ws, row, "O. WORKING CAPITAL PARAMETERS")

        wc_params = [
            ("Raw materials inventory", "Days"),
            ("Finished goods inventory - Fresh-pack", "Days"),
            ("Finished goods inventory - Frozen", "Days"),
            ("Accounts receivable - weighted average", "Days"),
            ("Accounts payable - suppliers", "Days"),
            ("Accounts payable - farmers", "Days"),
            ("Seeds-on-credit receivables", "Days"),
            ("Seasonal working capital peak multiplier", "Multiplier"),
        ]

        for label, unit in wc_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # SECTION P: FINANCING STRUCTURE
        row = self._add_section_header(ws, row, "P. FINANCING STRUCTURE")

        financing_params = [
            ("Sponsor equity", "%"),
            ("Senior debt", "%"),
            ("Subordinated debt/mezzanine", "%"),
            ("Grant / Technical assistance", "%"),
            ("Senior debt - Interest rate", "%"),
            ("Senior debt - Tenor", "Years"),
            ("Senior debt - Grace period", "Years"),
            ("Senior debt - Arrangement fee", "%"),
            ("Subordinated debt - Interest rate", "%"),
            ("Subordinated debt - Tenor", "Years"),
            ("Subordinated debt - Grace period", "Years"),
        ]

        for label, unit in financing_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # SECTION Q: TAXATION & INCENTIVES
        row = self._add_section_header(ws, row, "Q. TAXATION & INCENTIVES")

        tax_params = [
            ("Standard CIT rate", "%"),
            ("Tax holiday duration", "Years"),
            ("Reduced rate after holiday", "%"),
            ("Tax credit during operation", "%"),
            ("Tax loss carryforward", "Years"),
            ("VAT rate", "%"),
            ("VAT recoverable on purchases", "%"),
            ("Withholding tax - interest", "%"),
            ("Withholding tax - dividends", "%"),
            ("Import duties - standard", "%"),
            ("Import duty exemption period", "Years"),
        ]

        for label, unit in tax_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # SECTION R: DEPRECIATION & ASSET LIFE
        row = self._add_section_header(ws, row, "R. DEPRECIATION & ASSET LIFE")

        asset_params = [
            ("Buildings useful life", "Years"),
            ("Buildings residual value", "%"),
            ("Heavy machinery useful life", "Years"),
            ("Heavy machinery residual value", "%"),
            ("Light equipment useful life", "Years"),
            ("Light equipment residual value", "%"),
            ("Vehicles useful life", "Years"),
            ("Vehicles residual value", "%"),
            ("Furniture & fixtures useful life", "Years"),
            ("Furniture & fixtures residual value", "%"),
            ("IT equipment useful life", "Years"),
            ("IT equipment residual value", "%"),
        ]

        for label, unit in asset_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # SECTION S: MACROECONOMIC ASSUMPTIONS
        row = self._add_section_header(ws, row, "S. MACROECONOMIC ASSUMPTIONS")

        macro_params = [
            ("XAF/USD exchange rate (current)", "XAF/USD"),
            ("XAF/EUR exchange rate", "XAF/EUR"),
            ("Expected XAF/USD change", "%/year"),
            ("General inflation rate", "%/year"),
            ("Discount rate for NPV (WACC)", "%"),
            ("Terminal growth rate", "%"),
        ]

        for label, unit in macro_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # SECTION T: SCENARIO ANALYSIS
        row = self._add_section_header(ws, row, "T. SCENARIO ANALYSIS - TOGGLES")

        # Scenario selector (should be dropdown in final version)
        row = self._add_input_row(ws, row, "Active scenario", "", "Base/Downside/Upside", "SELECT SCENARIO")

        row += 1

        row = self._add_subsection_header(ws, row, "T1: Downside Scenario Adjustments")
        downside_params = [
            ("Yield adjustment", "%"),
            ("Price adjustment", "%"),
            ("CAPEX overrun", "%"),
            ("Operating cost increase", "%"),
            ("Ramp-up delay", "Months"),
            ("Capacity utilization", "% of base"),
        ]

        for label, unit in downside_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        row = self._add_subsection_header(ws, row, "T2: Upside Scenario Adjustments")
        upside_params = [
            ("Yield adjustment", "%"),
            ("Price adjustment", "%"),
            ("CAPEX savings", "%"),
            ("Operating cost reduction", "%"),
            ("Accelerated ramp-up", "Months"),
            ("Capacity utilization", "% of base"),
        ]

        for label, unit in upside_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        # SECTION U: DEVELOPMENT IMPACT PARAMETERS
        row = self._add_section_header(ws, row, "U. DEVELOPMENT IMPACT PARAMETERS")

        row = self._add_subsection_header(ws, row, "U1: Employment")
        employment_params = [
            ("Construction phase jobs", "Number"),
            ("Operations permanent jobs", "Number"),
            ("% women in workforce", "%"),
            ("Average monthly salary", "XAF/month"),
            ("Indirect jobs multiplier", "Multiplier"),
        ]

        for label, unit in employment_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        row = self._add_subsection_header(ws, row, "U2: Farmer Impact")
        farmer_params = [
            ("Baseline farmer income", "XAF/year"),
            ("Project farmer income", "XAF/year"),
            ("% women farmers", "%"),
        ]

        for label, unit in farmer_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        row = self._add_subsection_header(ws, row, "U3: Economic Impact")
        economic_params = [
            ("Local content", "% of costs"),
            ("CO₂ reduction", "Tonnes/year"),
        ]

        for label, unit in economic_params:
            row = self._add_input_row(ws, row, label, "", unit, "")

        row += 1

        print(f"Built Assumptions sheet up to row {row} - Sections L-U complete")
        print(f"✓ ASSUMPTIONS SHEET COMPLETE - Total {row} rows")

        return ws, row


if __name__ == "__main__":
    from datetime import datetime
    builder = CompleteSantaFreshBuilder()
    builder.build_model()

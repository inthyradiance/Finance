"""Link REIT (0823.HK): rate sensitivity, DPU drivers and valuation.

All inputs are public figures; sources are listed in README.md.
Update MARKET with the latest close and yields before reusing the numbers.
"""

# FY2025/26 = year ended 31 March 2026 (results announced 28 May 2026). HK$ millions unless noted.
FY26 = {
    "dpu_hkd": 2.5361,          # distribution per unit, HK$ (HK 253.61 cents, -6.9% YoY)
    "distributable": 6577,      # total distributable amount (-6.4% YoY)
    "npi": 10230,               # net property income (-3.7% YoY)
    "total_debt": 56700,        # total debt, face value
    "fixed_share": 0.600,       # share of debt at fixed rates
    "avg_cost": 0.0344,         # average all-in borrowing cost
    "nav_per_unit": 57.75,      # HK$
}
FY25 = {
    "distributable": 7025,
    "npi": 10619,
    "total_debt": 53500,
    "fixed_share": 0.669,
    "avg_cost": 0.0358,
}
MARKET = {
    "price": 39.30,             # HK$ close, 27 Oct 2026
    "hkgb_10y": 0.04164,        # 10-year HKGB, average accepted yield at the 21 Oct 2026 tender
    "hibor_3m": 0.0324,         # 27 Oct 2026
}
HK_PROFITS_TAX = 0.165
SHOCK = 0.01                    # +100bp on floating-rate debt


def rate_sensitivity(fy, distributable, after_tax):
    """Change in distributable amount (as a share) for a +100bp move on floating-rate debt."""
    extra_interest = fy["total_debt"] * (1 - fy["fixed_share"]) * SHOCK
    if after_tax:
        extra_interest *= 1 - HK_PROFITS_TAX
    return extra_interest / distributable, extra_interest


def main():
    units_m = FY26["distributable"] / FY26["dpu_hkd"]
    dist_yield = FY26["dpu_hkd"] / MARKET["price"]
    spread_bp = (dist_yield - MARKET["hkgb_10y"]) * 1e4
    p_nav = MARKET["price"] / FY26["nav_per_unit"]

    s26_pre, hit_pre = rate_sensitivity(FY26, FY26["distributable"], after_tax=False)
    s26_post, hit_post = rate_sensitivity(FY26, FY26["distributable"], after_tax=True)
    s25_pre, _ = rate_sensitivity(FY25, FY25["distributable"], after_tax=False)

    npi_drop = FY25["npi"] - FY26["npi"]
    dist_drop = FY25["distributable"] - FY26["distributable"]

    print("Valuation (price HK$%.2f)" % MARKET["price"])
    print(f"  Units implied by DPU          {units_m:,.0f}m")
    print(f"  Distribution yield            {dist_yield:.2%}")
    print(f"  Spread over 10Y HKGB          {spread_bp:.0f}bp")
    print(f"  Spread over 3M HIBOR          {(dist_yield - MARKET['hibor_3m']) * 1e4:.0f}bp")
    print(f"  Price / NAV                   {p_nav:.2f}x ({1 - p_nav:.0%} discount)")
    print()
    print("Rate sensitivity: +100bp on floating-rate debt")
    print(f"  Floating-rate debt            HK${FY26['total_debt'] * (1 - FY26['fixed_share']):,.0f}m")
    print(f"  Extra interest                HK${hit_pre:,.0f}m pre-tax, HK${hit_post:,.0f}m after tax")
    print(f"  DPU impact FY26               -{s26_pre:.1%} pre-tax, -{s26_post:.1%} after tax "
          f"(-HK${hit_post / units_m * 100:.1f} cents)")
    print(f"  DPU impact FY25 (66.9% fixed) -{s25_pre:.1%} pre-tax")
    print()
    print("What drove the decline")
    print(f"  Distributable amount          -HK${dist_drop:,.0f}m")
    print(f"  Net property income           -HK${npi_drop:,.0f}m ({npi_drop / dist_drop:.0%} of the fall)")
    print(f"  Average borrowing cost        {FY25['avg_cost']:.2%} -> {FY26['avg_cost']:.2%}")


if __name__ == "__main__":
    main()

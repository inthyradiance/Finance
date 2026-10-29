# Link REIT (0823.HK): rents, not rates, drive the distribution

*Independent research note, 29 October 2026. Prices as at the 27 October 2026 close. For learning purposes, not investment advice.*

## Bottom line

- **Rates are a secondary risk.** With 40% of HK$56.7bn debt at floating rates, a 100bp rise in floating rates would cut DPU by about 3% (2.9% after tax, 3.4% before).
- **Rents are the main driver.** FY2025/26 DPU fell 6.9% because net property income fell 3.7% on negative rental reversion (Hong Kong retail: –8.2%). The average borrowing cost actually improved, from 3.58% to 3.44%.
- **The valuation already pays for a lot.** At HK$39.30 the units yield 6.45%, about 230bp over 10-year HKGBs, at a 32% discount to NAV. That supports income-focused holders, but a re-rating needs evidence that rental reversion is bottoming.

## Key numbers

| | FY2024/25 | FY2025/26 |
|---|---|---|
| DPU (HK cents) | ~272.4 | 253.61 (–6.9%) |
| Total distributable amount (HK$m) | ~7,027 | 6,577 (–6.4%) |
| Net property income (HK$m) | ~10,623 | 10,230 (–3.7%) |
| Total debt, face value (HK$bn) | 53.5 | 56.7 |
| Debt at fixed rates | 66.9% | 60.0% |
| Average all-in borrowing cost | 3.58% | 3.44% |
| Net gearing | 21.5% | 23.9% |
| NAV per unit (HK$) | 63.30 | 57.75 |
| Hong Kong retail rental reversion | | –8.2% |

FY2024/25 DPU, distributable amount and NPI are implied from the reported FY2025/26 figures and their year-on-year changes.

Market data, late October 2026: unit price HK$39.30 (27 Oct); 10-year HKGB 4.164% (average accepted yield at the 21 Oct tender); 3-month HIBOR 3.24% (27 Oct).

## Rate sensitivity

- Floating-rate debt: 40% × HK$56.7bn = HK$22.7bn.
- +100bp adds HK$227m of interest a year, or HK$189m after 16.5% Hong Kong profits tax.
- Against HK$6,577m of distributable amount, that is –2.9% after tax (about HK 7.3 cents per unit).
- Sensitivity rose over the year: Link cut its fixed-rate share from 66.9% to 60.0%, within its 50–70% policy band. The same shock would have cost about 2.5% (pre-tax) a year earlier, against 3.4% now.

Simplifications: the shock applies to all floating-rate debt, although part of it is not in HK$ and so is not priced off HIBOR; it ignores fixed-rate debt that reprices as it matures (average debt maturity 3.5 years) and interest earned on cash.

## What drove the DPU decline

Distributable amount fell by about HK$450m. Net property income fell by about HK$393m, so lower rents explain most of the fall. Funding costs did not add to it: the average borrowing cost fell, even though total debt rose by HK$3.2bn. NAV fell 8.8% on lower property valuations, which also pushed net gearing up to 23.9%.

## Valuation

- **Yield:** 253.61 cents / HK$39.30 = 6.45%.
- **Spread:** 6.45% – 4.16% = about 230bp over 10-year HKGBs, and about 320bp over 3-month HIBOR.
- **Price/NAV:** 0.68x, a 32% discount. The market is pricing either further valuation cuts or lower long-run returns on the portfolio.

## What to watch

1. **Interim results for the six months to 30 September 2026** (expected in November): is Hong Kong retail rental reversion still negative, and by how much?
2. **HIBOR and 10-year HKGB yields:** the 10-year HKGB yield is near its highest since early 2025, which narrows the spread that income investors earn.
3. **Capital management:** disposals and buybacks, which management highlighted at the annual results.

## Reproduce

```bash
python link_reit_analysis.py
```

Update the `MARKET` inputs (price, 10-year HKGB yield, HIBOR) to the latest values before reusing the figures.

## Sources

- Link REIT, [Annual Results 2025/2026 announcement (HKEX)](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0528/2026052800355.pdf) and [analyst presentation](https://www.linkreit.com/-/media/linkreit/investor-relations/financial-reports-and-presentations/presentations/2025-2026/presentation/20260527_ar202526-annual-results-presentation.pdf?rev=a9a8ca7cfd054fe292106dea3855a759)
- Link REIT, [annual results press release (debt, fixed-rate share, borrowing cost)](https://www.linkreit.com/en/media/news-releases/link-reit-delivers-solid-results-amid-challenging-conditions/)
- The Standard, [Link REIT's distribution dips 6.4pc for the year ended March](https://www.thestandard.com.hk/finance/article/333207/Link-REITs-distribution-dips-64pc-for-the-year-ended-March-eyes-disposals-buybacks)
- Mingtiandi, [Link REIT to continue divestments as property income falls 3.7%](https://www.mingtiandi.com/real-estate/finance/link-reit-to-continue-divestments-as-property-income-falls-3-7/)
- MarketScreener, [Link REIT quote (27 Oct 2026 close)](https://www.marketscreener.com/quote/stock/LINK-REAL-ESTATE-INVESTME-6498337/)
- HKSAR Government, [results of the 10-year HKGB tender, 21 Oct 2026](https://www.info.gov.hk/gia/general/202610/21/P2026102100515.htm)
- HKAB, [HKD interest settlement rates (HIBOR)](https://www.hkab.org.hk/en/rates/hibor)

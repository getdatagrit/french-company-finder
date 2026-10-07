# French Company Finder - Sirene Financials

French company lead lists from Sirene screened by net result and revenue, with net margin, size, matching establishment and optional directors.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/french-company-finder) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/french-company-finder/)

**from $5.60 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

French Company Finder searches the official Sirene register of French companies and returns each company as a clean record: identity, legal form, activity code, size, employer flag, head office address with coordinates, and the latest published financials. Beyond a plain lookup you can screen companies by profitability: filter on net result (profitable or loss-making) as well as revenue, and every record comes with the net margin already calculated. Location filters are checked on every record, so a company is returned only when it has an open establishment in the place you asked for. Export the data as JSON, CSV or Excel, call it through the Apify API, or plug it into n8n, Make and AI agents through MCP.

## Quick start

1. Open [French Company Finder - Sirene Financials on Apify Store](https://apify.com/datagrit/french-company-finder) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "queries": [
    "logiciel"
  ],
  "departments": [
    "69"
  ],
  "minRevenue": 1000000,
  "maxItems": 25
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `queries` | array | Company names, activities or keywords, for example boulangerie or logiciel. Each term is searched separately. Leave empty when you search by filters or by SIREN/SIRET number only. If the input has no search term, no number and no filter at all, the Actor runs a small free example search (boulangerie in department 75) and says so in the status message. |
| `sirens` | array | Look up specific companies by 9-digit SIREN or 14-digit SIRET. These lookups ignore the filters below and also return closed companies; a SIRET returns exactly that establishment. Numbers that are not in the public register get a free status row and are listed in the status message; when the input has only numbers and none exists, the run fails. |
| `departments` | array | French department codes, for example 75 for Paris, 69 for Rhône or 2A for Corse-du-Sud. A company is returned when it has an establishment in one of these departments; with "Only active companies" on (default) that establishment must be open. The establishment is returned in the matchedEstablishment fields. Switch on "Head office only" to require the head office itself. |
| `regions` | array | INSEE region codes, for example 11 for Île-de-France or 84 for Auvergne-Rhône-Alpes. Same rule as departments: an establishment in the region, open when "Only active companies" is on, or the head office when "Head office only" is on. |
| `postalCodes` | array | Postal codes, for example 75011. Same rule as departments: an establishment with this postal code, open when "Only active companies" is on, or the head office when "Head office only" is on. |
| `headOfficeOnly` | boolean | Keep only companies whose head office is in the requested departments, regions or postal codes. Off by default: any establishment of the company in the location counts. |
| `activityCodes` | array | Main activity codes in the NAF classification, for example 62.01Z for computer programming or 10.71C for bakeries. |
| `companySizes` | array | Official size category: PME (small and medium), ETI (mid-sized) or GE (large). |
| `employeeBands` | array | INSEE employee band codes, for example 11 for 10-19 employees, 12 for 20-49, 21 for 50-99, 22 for 100-199. |
| `legalForms` | array | INSEE legal form codes, for example 5710 for SAS, 5499 for SARL or 5599 for SA. |
| `minRevenue` | integer | Only companies whose latest published revenue is at least this amount. Only companies that file their accounts publicly have revenue data. |
| `maxRevenue` | integer | Only companies whose latest published revenue is at most this amount. |
| `minNetResult` | integer | Only companies whose latest net result is at least this amount. Use 1 to keep only profitable companies. |
| `maxNetResult` | integer | Only companies whose latest net result is at most this amount. Use 0 to find loss-making companies. |
| `onlyActive` | boolean | Skip companies that have ceased activity. With a location filter it also skips companies whose establishments in the location are all closed, and the status message counts them. |
| `employersOnly` | boolean | Keep only companies flagged as employers: the head office is registered as an employer or the company employee band shows at least one employee (the isEmployer field). Checked by the Actor on every record. |
| `socialEconomyOnly` | boolean | Keep only companies flagged as part of the social and solidarity economy (the isSocialEconomy field). |
| `includeDirectors` | boolean | Adds the names and roles of the directors listed in the register. Off by default because it contains personal data; when you switch it on you are responsible for using it in line with data protection law. |
| `maxItems` | integer | Stop after this many companies in total. The register search returns at most 10,000 results per search. |
| `proxyConfiguration` | object | Optional proxy. Leave disabled: the Sirene search API is public and needs none. |

## Output

| Field | Type | Description |
|---|---|---|
| `query` | string | The search term or number this result came from; null for filter-only searches. |
| `siren` | string | Nine-digit company identifier. |
| `name` | string | Company display name. |
| `legalName` | string | Registered company name. |
| `acronym` | string | Registered acronym when there is one. |
| `isActive` | boolean | True while the company is active, false when it has ceased activity. |
| `creationDate` | string | Date of creation, YYYY-MM-DD. |
| `closureDate` | string | Date of cessation, YYYY-MM-DD. |
| `legalFormCode` | string | INSEE legal form code. |
| `legalForm` | string | Legal form label for the common codes; null when the code is not in the built-in list. |
| `activityCode` | string | Main activity code, NAF rev. 2. |
| `sectionCode` | string | Letter of the activity section. |
| `companySize` | string | PME, ETI or GE. |
| `employeeBandCode` | string | INSEE employee band code. |
| `employeeBand` | string | Employee band label. |
| `employeeBandYear` | number | Year the employee band refers to. |
| `establishments` | number | Number of establishments ever registered. |
| `establishmentsOpen` | number | Number of establishments currently open. |
| `headOfficeSiret` | string | Fourteen-digit identifier of the head office. |
| `address` | string | Head office address. |
| `postalCode` | string | Head office postal code. |
| `city` | string | Head office city. |
| `departmentCode` | string | Department code of the head office. |
| `regionCode` | string | INSEE region code of the head office. |
| `latitude` | number | Head office latitude. |
| `longitude` | number | Head office longitude. |
| `vatNumber` | string | Intra-community VAT number. |
| `revenue` | number | Latest published revenue in EUR. |
| `revenueYear` | number | Financial year of the latest revenue. |
| `netResult` | number | Latest net result in EUR. |
| `netMarginPct` | number | Net result divided by revenue. |
| `isSocialEconomy` | boolean | Part of the social and solidarity economy. |
| `isOrganic` | boolean | Registered in the organic agency register. |
| `isEmployer` | boolean | True when the head office is registered as an employer or the company employee band shows at least one employee; false when the head office is registered as a non-employer or the band says the company has no employees; null when the register has neither. |
| `isAssociation` | boolean | Is an association. |
| `matchedEstablishmentSiret` | string | Establishment in your location filter (or the SIRET you looked up); empty when no location filter is used. The head office is used when it is in the location; otherwise another establishment there. It can differ from the head office. |
| `matchedEstablishmentAddress` | string | Address of the matched establishment. |
| `matchedEstablishmentPostalCode` | string | Postal code of the matched establishment. |
| `matchedEstablishmentCity` | string | City of the matched establishment. |
| `matchedEstablishmentDepartment` | string | Department of the matched establishment, from its INSEE commune code. |
| `matchedEstablishmentRegion` | string | INSEE region code of the matched establishment. |
| `matchedEstablishmentIsHeadOffice` | boolean | True when the matched establishment is the head office. |
| `matchedEstablishmentIsActive` | boolean | Whether the matched establishment is open. Always true while "Only active companies" is on (companies whose establishments in the location are all closed are skipped); can be false when you switch that option off or look up the SIRET of a closed establishment. |
| `matchedEstablishmentClosureDate` | string | Closure date of the matched establishment, YYYY-MM-DD; null while it is open. |
| `matchedEstablishmentsListed` | integer | Number of establishments of this company in the location found in the register response (the head office plus the matching establishments). The Actor asks the register for up to 100 matching establishments per company, so 100 means 100 or more. Empty when no location filter is used. |
| `directorCount` | number | Number of directors listed in the register (names only when requested). |
| `directors` | string | Names and roles joined with semicolons; only when directors are requested. |
| `sourceUrl` | string | Public company page. |
| `updatedAt` | string | Last update of the record in the register. |
| `found` | boolean | False only for the single status row emitted when a search has no results. |
| `scrapedAt` | string | ISO 8601 timestamp of extraction. |

Sample record:

```json
{
  "query": "boulangerie",
  "siren": "403052111",
  "name": "BOULANGERIES PAUL",
  "legalName": "BOULANGERIES PAUL",
  "acronym": null,
  "isActive": true,
  "creationDate": "1995-12-07",
  "closureDate": null,
  "legalFormCode": "5710",
  "legalForm": "Simplified joint-stock company (SAS)",
  "activityCode": "10.71A",
  "sectionCode": "C",
  "companySize": "ETI",
  "employeeBandCode": "41",
  "employeeBand": "500-999 employees",
  "employeeBandYear": 2023,
  "establishments": 315,
  "establishmentsOpen": 125,
  "headOfficeSiret": "40305211102616",
  "address": "344 AVENUE DE LA MARNE 59700 MARCQ-EN-BARŒUL",
  "postalCode": "59700",
  "city": "MARCQ-EN-BARŒUL",
  "departmentCode": "59",
  "regionCode": "32",
  "latitude": 50.678029398,
  "longitude": 3.1169136021,
  "vatNumber": "FR32403052111",
  "revenue": 73611839,
  "revenueYear": 2024,
  "netResult": -2197350,
  "netMarginPct": -3,
  "isSocialEconomy": false,
  "isOrganic": false,
  "isEmployer": true,
  "isAssociation": false,
  "matchedEstablishmentSiret": "32868651400105",
  "matchedEstablishmentAddress": "17 AV CHARLES DE GAULLE 69370 SAINT-DIDIER-AU-MONT-D OR",
  "matchedEstablishmentPostalCode": "69370",
  "matchedEstablishmentCity": "SAINT-DIDIER-AU-MONT-D OR",
  "matchedEstablishmentDepartment": "69",
  "matchedEstablishmentRegion": "84",
  "matchedEstablishmentIsHeadOffice": false,
  "matchedEstablishmentIsActive": true,
  "matchedEstablishmentClosureDate": null,
  "matchedEstablishmentsListed": 1,
  "directorCount": 4,
  "directors": null,
  "sourceUrl": "https://annuaire-entreprises.data.gouv.fr/entreprise/403052111",
  "updatedAt": "2026-09-17T04:38:04",
  "found": true,
  "scrapedAt": "2026-09-30T08:00:00.000Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~french-company-finder/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries":["logiciel"],"departments":["69"],"minRevenue":1000000,"maxItems":25}'
```

## FAQ

**How do I find one specific company?**  
Paste its SIREN or SIRET number. Number lookups ignore the filters and also return closed companies and closed establishments. A SIRET lookup returns exactly that establishment.

**What if a number does not exist?**  
The run lists the numbers that are not in the public register in its status message and adds a free status row for each. If the input contains only numbers and none of them exists, the run fails with that list, so a scheduled run cannot turn green on a wrong input. Companies that opted out of public listing are not in the register.

**Why is revenue empty for some companies?**  
Many companies do not publish their accounts, and the register only holds what is filed publicly. The status message says how many returned companies have revenue.

**How fresh is the data?**  
Every run reads the live register.

**Can I schedule it?**  
Yes, use Apify schedules or call the Actor from your own workflow.

**Something looks wrong.**  
Open an issue with the input you used; changes at the source are fixed quickly.

## More from datagrit

- [IRS 990 Nonprofit Officers and Compensation](https://github.com/getdatagrit/irs-990-officer-compensation) - Named officers, directors and key employees with pay, hours and titles from IRS e-filed 990, 990-EZ and 990-PF returns.
- [Poland KRS New Company Registrations Feed](https://github.com/getdatagrit/poland-krs-new-companies) - Newly registered Polish companies, foundations and associations from the official KRS court register: NIP, address, PKD, capital, email, with filters and change detection.
- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.
- [UK Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/uk-contract-expiry-radar) - UK public contracts ending soon with incumbent supplier, buyer, value and contact - recompete leads from Contracts Finder award notices.
- [Ashby Salary Scraper - Startup Job Pay Ranges](https://github.com/getdatagrit/ashby-salary-scraper) - Ashby job postings with normalized annual salary ranges, equity flags and new-since-last-run detection.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/french-company-finder). Examples are MIT licensed.

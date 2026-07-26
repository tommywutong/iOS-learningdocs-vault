---
title: matchingPolicy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/recurrencerule/matchingpolicy
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/matchingpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/matchingpolicy.json'
content_hash: 'sha256:68b6c6a1b12c24b6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RecurrenceRule](../recurrencerule.md)

# matchingPolicy

<sub>Instance Property</sub>

What to do when a recurrence is not a valid date

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var matchingPolicy: Calendar.MatchingPolicy
```

## Discussion

An occurrence may not be a valid date if it falls on a leap day or a leap hour when there is not one. When that happens, we can choose to ignore the occurrence (`.strict`), choose a later time which has the same components (`.nextTimePreservingSmallerComponents`), or find an earlier time (`.previousTimePreservingSmallerComponents`).

For example, consider an event happening every year, starting on the 29th of February 2020. When the matching policy is set to `.strict`, it yields the following recurrences:

- 2020-02-29
- 2024-02-29
- 2028-02-29
- …

With `matchingPolicy` of `.previousTimePreservingSmallerComponents`, we get a result for each year:

- 2020-02-29
- 2021-02-28
- 2022-02-28
- 2023-02-28
- 2024-02-29

Lastly, a `matchingPolicy` of `.nextTimePreservingSmallerComponents` moves invalid occurrences to the day after February 29:

- 2020-02-29
- 2021-03-01
- 2022-03-01
- 2023-03-01
- 2024-02-29

The same logic applies for missing leap hours during daylight saving time switches. For example, consider an event repeating daily, which starts at March 9 2024, 01:30 PST. With a `.strict` matching policy, the event repeats on the following dates, and skips a day:

- 2024-03-09 01:30 PST (09:30 UTC) (on 2024-03-10, there is a missing hour between 1am and 2am)
- 2024-03-11 01:30 PDT (08:30 UTC)
- 2024-03-12 01:30 PDT (08:30 UTC) With `matchingPolicy` of `.previousTimePreservingSmallerComponents`, we get a result for each day:
- 2024-03-09 01:30 PST (09:30 UTC)
- 2024-03-10 02:30 PST (10:30 UTC) (on 2024-03-10, there is a missing hour between 1am and 2am)
- 2024-03-11 01:30 PDT (08:30 UTC)
- 2024-03-12 01:30 PDT (08:30 UTC) Lastly, a `matchingPolicy` of `.nextTimePreservingSmallerComponents` moves invalid occurrences an hour forward:
- 2024-03-09 01:30 PST (09:30 UTC)
- 2024-03-10 00:30 PST (08:30 UTC) (on 2024-03-10, there is a missing hour between 1am and 2am)
- 2024-03-11 01:30 PDT (08:30 UTC)
- 2024-03-12 01:30 PDT (08:30 UTC)

Default value is `.nextTimePreservingSmallerComponents`

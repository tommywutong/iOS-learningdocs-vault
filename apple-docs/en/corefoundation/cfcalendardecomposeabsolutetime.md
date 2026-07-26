---
title: CFCalendarDecomposeAbsoluteTime
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcalendardecomposeabsolutetime
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendardecomposeabsolutetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendardecomposeabsolutetime.json'
content_hash: 'sha256:cf16776b1554a5f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarDecomposeAbsoluteTime

<sub>Function</sub>

Computes the components which are indicated by the componentDesc description string for the given absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern Boolean CFCalendarDecomposeAbsoluteTime(CFCalendarRef calendar, CFAbsoluteTime at, const char *componentDesc, ...);
```

## Parameters

- `calendar` — The calendar to use for the computation.

- `at` — An absolute time.

- `componentDesc` — A string that describes the components provided in the variadic parameters if pointers to storage for each of the desired components. On successful return, the pointers are filled with values of the corresponding components. The type of all units is `int`.

## Return Value

`TRUE` if the function is able to compute the components indicated by the `componentDesc` description string for the given absolute time, and fills the values to the components given in the varargs. Returns `FALSE` if the absolute time falls outside the defined range of the calendar, or the computation cannot be performed.

## Discussion

The Weekday ordinality, when requested, refers to the next larger (than Week) of the requested units. Some computations can take a relatively long time to perform.

The following example shows how to use this function to determine the current year, month, and day, using an existing calendar (`gregorian`):

```objc
CFCalendarDecomposeAbsoluteTime(gregorian, CFAbsoluteTimeGetCurrent(), "yMd",  &year, &month, &day);
```

## See Also

### Calendrical Calculations

- [CFCalendarAddComponents](cfcalendaraddcomponents.md) — Computes the absolute time when specified components are added to a given absolute time.
- [CFCalendarComposeAbsoluteTime](cfcalendarcomposeabsolutetime.md) — Computes the absolute time from components in a description string.
- [CFCalendarGetComponentDifference](cfcalendargetcomponentdifference.md) — Computes the difference between the two absolute times, in terms of specified calendrical components.

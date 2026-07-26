---
title: Component Wrapping Options
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/1533520-component-wrapping-options
source_url: 'https://developer.apple.com/documentation/corefoundation/1533520-component-wrapping-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/1533520-component-wrapping-options.json'
content_hash: 'sha256:7afbca5b2c36a8ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFCalendar](cfcalendar.md)

# Component Wrapping Options

<sub>API Collection</sub>

The wrapping option specifies overflow behavior for calendar components in calendrical calculations

## Overview

The wrapping option specifies overflow behavior for calendar components in calendrical calculations—see [CFCalendarAddComponents](cfcalendaraddcomponents.md) and [CFCalendarGetComponentDifference](cfcalendargetcomponentdifference.md).

## Topics

### Constants

- [kCFCalendarComponentsWrap](kcfcalendarcomponentswrap.md) — Specifies that the components specified for calendar components should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.

## See Also

### Constants

- [CFCalendarUnit](cfcalendarunit.md) — CFCalendarUnit constants are used to specify calendrical units, such as day or month, in various calendar calculations.

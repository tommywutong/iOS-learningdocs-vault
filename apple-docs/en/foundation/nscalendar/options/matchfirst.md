---
title: matchFirst
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/options/matchfirst
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/options/matchfirst'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/options/matchfirst.json'
content_hash: 'sha256:335bda9e91ca8ce7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSCalendar](../../nscalendar.md) · [Options](../options.md)

# matchFirst

<sub>Type Property</sub>

Specifies that, if there are two or more matching times, the operation should return the first occurrence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var matchFirst: NSCalendar.Options { get }
```

## See Also

### Constants

- [NSCalendarWrapComponents](wrapcomponents.md) — Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.
- [NSCalendarMatchStrictly](matchstrictly.md) — Specifies that the operation should travel as far forward or backward as necessary looking for a match.
- [NSCalendarSearchBackwards](searchbackwards.md) — Specifies that the operation should travel backwards to find the previous match before the given date.
- [NSCalendarMatchPreviousTimePreservingSmallerUnits](matchprevioustimepreservingsmallerunits.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _previous_ existing value of the missing unit and preserves the lower units’ values.
- [NSCalendarMatchNextTimePreservingSmallerUnits](matchnexttimepreservingsmallerunits.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _next_ existing value of the missing unit and preserves the lower units’ values.
- [NSCalendarMatchNextTime](matchnexttime.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _next_ existing value of the missing unit and _does not_ preserve the lower units’ values.
- [NSCalendarMatchLast](matchlast.md) — Specifies that, if there are two or more matching times, the operation should return the last occurrence.
- [NSWrapCalendarComponents](../../nswrapcalendarcomponents.md) — Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented. _(deprecated)_

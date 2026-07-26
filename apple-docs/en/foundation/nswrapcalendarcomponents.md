---
title: NSWrapCalendarComponents
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nswrapcalendarcomponents
source_url: 'https://developer.apple.com/documentation/foundation/nswrapcalendarcomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nswrapcalendarcomponents.json'
content_hash: 'sha256:7fdc098745e0977c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSWrapCalendarComponents

<sub>Global Variable</sub>

Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.

> [!warning] Deprecated
> Use [NSCalendarWrapComponents](nscalendar/options/wrapcomponents.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSWrapCalendarComponents: Int { get }
```

## See Also

### Constants

- [NSCalendarWrapComponents](nscalendar/options/wrapcomponents.md) — Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.
- [NSCalendarMatchStrictly](nscalendar/options/matchstrictly.md) — Specifies that the operation should travel as far forward or backward as necessary looking for a match.
- [NSCalendarSearchBackwards](nscalendar/options/searchbackwards.md) — Specifies that the operation should travel backwards to find the previous match before the given date.
- [NSCalendarMatchPreviousTimePreservingSmallerUnits](nscalendar/options/matchprevioustimepreservingsmallerunits.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _previous_ existing value of the missing unit and preserves the lower units’ values.
- [NSCalendarMatchNextTimePreservingSmallerUnits](nscalendar/options/matchnexttimepreservingsmallerunits.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _next_ existing value of the missing unit and preserves the lower units’ values.
- [NSCalendarMatchNextTime](nscalendar/options/matchnexttime.md) — Specifies that, when there is no matching time before the end of the next instance of the next highest unit specified in the given `NSDateComponents` object, this method uses the _next_ existing value of the missing unit and _does not_ preserve the lower units’ values.
- [NSCalendarMatchFirst](nscalendar/options/matchfirst.md) — Specifies that, if there are two or more matching times, the operation should return the first occurrence.
- [NSCalendarMatchLast](nscalendar/options/matchlast.md) — Specifies that, if there are two or more matching times, the operation should return the last occurrence.

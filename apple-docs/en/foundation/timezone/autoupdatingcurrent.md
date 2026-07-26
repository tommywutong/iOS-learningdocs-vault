---
title: autoupdatingCurrent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/timezone/autoupdatingcurrent
source_url: 'https://developer.apple.com/documentation/foundation/timezone/autoupdatingcurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timezone/autoupdatingcurrent.json'
content_hash: 'sha256:c02dbb5148abb095'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TimeZone](../timezone.md)

# autoupdatingCurrent

<sub>Type Property</sub>

The time zone currently used by the system, automatically updating to the user’s current preference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var autoupdatingCurrent: TimeZone { get }
```

## Discussion

If this time zone is mutated, then it no longer tracks the system time zone.

The autoupdating time zone only compares equal to itself.

## See Also

### Getting the Current Time Zone

- [current](current.md) — The time zone currently used by the system.

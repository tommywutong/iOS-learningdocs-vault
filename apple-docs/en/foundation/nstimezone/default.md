---
title: default
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/default
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/default.json'
content_hash: 'sha256:d04d2eacb4288403'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# default

<sub>Type Property</sub>

The default time zone for the current app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var `default`: TimeZone { get set }
```

## Discussion

If no [defaultTimeZone](default.md) time zone has been set, the current system time zone is used. If the current system time zone cannot be determined, the GMT time zone is used instead.

The [defaultTimeZone](default.md) time zone is used by the app for date and time operations. You can set it to cause the app to run as if it were in a different time zone. Setting the [defaultTimeZone](default.md) property clears any value that was previously set.

If you access the [defaultTimeZone](default.md) class property, assign its value to a variable, and set a new [defaultTimeZone](default.md) time zone, the object stored in the variable doesn’t update to reflect the new [defaultTimeZone](default.md) time zone. Contrast this behavior with that of the [localTimeZone](local.md) class property, which returns a proxy object that always reflects the current system time zone.

## See Also

### Working with System Time Zones

- [localTimeZone](local.md) — An object that tracks the current system time zone.
- [systemTimeZone](system.md) — The time zone currently used by the system.
- [+ resetSystemTimeZone](<resetsystemtimezone().md>) — Clears any time zone value cached for the [systemTimeZone](system.md) property.

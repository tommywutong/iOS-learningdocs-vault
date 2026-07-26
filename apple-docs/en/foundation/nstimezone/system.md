---
title: system
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/system
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/system'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/system.json'
content_hash: 'sha256:d01e611ea1de044a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# system

<sub>Type Property</sub>

The time zone currently used by the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var system: TimeZone { get }
```

## Discussion

If the current system time zone cannot be determined, the GMT time zone is used instead.

If you access the [systemTimeZone](system.md) class property, its value is cached by the app and doesn’t update if the user subsequently changes the system time zone. In order for the [systemTimeZone](system.md) property to reflect the new time zone, you must first call the [+ resetSystemTimeZone](<resetsystemtimezone().md>) method to clear the cached value. Then, the next time you access the [systemTimeZone](system.md) property, it returns the current system time zone, and caches that value.

If you access the [systemTimeZone](system.md) class property, assign its value to a variable, and clear the cached value for the property by calling the [+ resetSystemTimeZone](<resetsystemtimezone().md>) method, the object stored in the variable doesn’t update to reflect the new system time zone. Contrast this behavior with that of the [localTimeZone](local.md) class property, which returns a proxy object that always reflects the current system time zone.

## See Also

### Working with System Time Zones

- [localTimeZone](local.md) — An object that tracks the current system time zone.
- [+ resetSystemTimeZone](<resetsystemtimezone().md>) — Clears any time zone value cached for the [systemTimeZone](system.md) property.
- [defaultTimeZone](default.md) — The default time zone for the current app.

---
title: resetSystemTimeZone()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/resetsystemtimezone()
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/resetsystemtimezone()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/resetsystemtimezone%28%29.json'
content_hash: 'sha256:a63298e645523980'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# resetSystemTimeZone()

<sub>Type Method</sub>

Clears any time zone value cached for the [systemTimeZone](system.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func resetSystemTimeZone()
```

## Discussion

If the app has cached the system time zone by accessing the [systemTimeZone](system.md) class property, this method clears that cached value. If you subsequently access the [systemTimeZone](system.md) class property, a new time zone object is created and cached.

## See Also

### Working with System Time Zones

- [localTimeZone](local.md) — An object that tracks the current system time zone.
- [systemTimeZone](system.md) — The time zone currently used by the system.
- [defaultTimeZone](default.md) — The default time zone for the current app.

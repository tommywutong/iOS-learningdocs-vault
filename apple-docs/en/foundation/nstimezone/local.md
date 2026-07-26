---
title: local
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimezone/local
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/local'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/local.json'
content_hash: 'sha256:febb057fff2b5bd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# local

<sub>Type Property</sub>

An object that tracks the current system time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var local: TimeZone { get }
```

## Discussion

Use this property when you want an object that always reflects the current system time zone. Contrast this behavior with that of the [systemTimeZone](system.md) class property, which has its value cached until you manually clear it by calling the [+ resetSystemTimeZone](<resetsystemtimezone().md>) method.

> [!important] Important
> In macOS High Sierra and later, iOS 11 and later, tvOS 11 and later, and watchOS 4 and later, the [localTimeZone](local.md) class property reflects the current system time zone, whereas previously it reflected the [defaultTimeZone](default.md) time zone.

Although the time zone obtained here automatically updates with the system, it provides no indication when system settings change. To receive notification of time zone changes, add an observer to the [NSSystemTimeZoneDidChangeNotification](../nsnotification/name-swift.struct/nssystemtimezonedidchange.md) notification by using the [- addObserver:selector:name:object:](<../notificationcenter/addobserver(__selector_name_object_).md>).

## See Also

### Working with System Time Zones

- [systemTimeZone](system.md) — The time zone currently used by the system.
- [+ resetSystemTimeZone](<resetsystemtimezone().md>) — Clears any time zone value cached for the [systemTimeZone](system.md) property.
- [defaultTimeZone](default.md) — The default time zone for the current app.

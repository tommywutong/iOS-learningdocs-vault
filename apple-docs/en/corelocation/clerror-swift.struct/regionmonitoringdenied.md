---
title: regionMonitoringDenied
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/regionmonitoringdenied
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/regionmonitoringdenied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/regionmonitoringdenied.json'
content_hash: 'sha256:655d77ff308027f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLError](../clerror-swift.struct.md)

# regionMonitoringDenied

<sub>Type Property</sub>

A constant that indicates the user denied access to the region monitoring service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var regionMonitoringDenied: CLError.Code { get }
```

## See Also

### Getting region monitoring errors

- [regionMonitoringFailure](regionmonitoringfailure.md) — A constant that indicates the location manager failed to monitor a registered region.
- [regionMonitoringSetupDelayed](regionmonitoringsetupdelayed.md) — A constant that indicates Core Location couldn’t initialize the region monitoring feature immediately.
- [regionMonitoringResponseDelayed](regionmonitoringresponsedelayed.md) — A constant that indicates Core Location will deliver events but they may be delayed.

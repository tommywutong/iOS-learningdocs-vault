---
title: MKError
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkerror
source_url: 'https://developer.apple.com/documentation/mapkit/mkerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkerror.json'
content_hash: 'sha256:b205fcb0c4f9f40a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKError

<sub>Structure</sub>

Error constants for the MapKit framework.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MKError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Error codes

- [decodingFailed](mkerror/decodingfailed.md) — GeoJSON decoding failed.
- [directionsNotFound](mkerror/directionsnotfound.md) — Directions to the specified location aren’t available.
- [loadingThrottled](mkerror/loadingthrottled.md) — The data didn’t load because data throttling is in effect.
- [placemarkNotFound](mkerror/placemarknotfound.md) — The framework couldn’t find the specified placemark.
- [serverFailure](mkerror/serverfailure.md) — The map server was unable to return the desired information.
- [unknown](mkerror/unknown.md) — An unknown error occurred.
- [Code](mkerror/code.md) — Error constants for the MapKit framework.

### Type Properties

- [errorDomain](mkerror/errordomain.md) — The error domain.

## See Also

### Errors

- [MKErrorDomain](mkerrordomain.md) — The error domain for MapKit.
- [Code](mkerror/code.md) — Error constants for the MapKit framework.

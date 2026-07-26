---
title: MKError.Code
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkerror/code
source_url: 'https://developer.apple.com/documentation/mapkit/mkerror/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkerror/code.json'
content_hash: 'sha256:318b4a056bbe16eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKError](../mkerror.md)

# MKError.Code

<sub>Enumeration</sub>

Error constants for the MapKit framework.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [MKErrorDecodingFailed](code/decodingfailed.md) — GeoJSON decoding failed.
- [MKErrorDirectionsNotFound](code/directionsnotfound.md) — The framework couldn’t find the specified directions.
- [MKErrorLoadingThrottled](code/loadingthrottled.md) — The data didn’t load because data throttling is in effect.
- [MKErrorPlacemarkNotFound](code/placemarknotfound.md) — The specified placemark could not be found.
- [MKErrorServerFailure](code/serverfailure.md) — The map server was unable to return the desired information.
- [MKErrorUnknown](code/unknown.md) — An unknown error occurred.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Errors

- [MKErrorDomain](../mkerrordomain.md) — The error domain for MapKit.
- [MKError](../mkerror.md) — Error constants for the MapKit framework.

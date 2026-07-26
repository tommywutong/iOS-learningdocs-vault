---
title: 'CLLocationCoordinate2DMake(_:_:)'
framework: Core Location
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationcoordinate2dmake(_:_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationcoordinate2dmake(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationcoordinate2dmake%28_%3A_%3A%29.json'
content_hash: 'sha256:e161ecb0211a9db8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationCoordinate2DMake(_:_:)

<sub>Function</sub>

Formats a latitude and longitude value into a coordinate data structure format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CLLocationCoordinate2DMake(_ latitude: CLLocationDegrees, _ longitude: CLLocationDegrees) -> CLLocationCoordinate2D
```

## Parameters

- `latitude` — The latitude for the new coordinate.

- `longitude` — The longitude for the new coordinate.

## Return Value

A coordinate structure encompassing the latitude and longitude values.

## See Also

### Creating a location coordinate

- [init()](<cllocationcoordinate2d/init().md>) — Creates a location coordinate object.
- [init(latitude:longitude:)](<cllocationcoordinate2d/init(latitude_longitude_).md>) — Creates a location coordination object with the specified latitude and longitude values.

---
title: 'string(fromDistance:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkdistanceformatter/string(fromdistance:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkdistanceformatter/string(fromdistance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdistanceformatter/string%28fromdistance%3A%29.json'
content_hash: 'sha256:2c70d02303313a82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDistanceFormatter](../mkdistanceformatter.md)

# string(fromDistance:)

<sub>Instance Method</sub>

Creates a string representation of the specified distance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(fromDistance distance: CLLocationDistance) -> String
```

## Parameters

- `distance` — The distance value that you want to convert to a string.

## Return Value

A user-readable string that describes the distance based on the formatter settings.

## See Also

### Converting distances

- [- distanceFromString:](<distance(from_).md>) — Returns the distance value parsed from the specified string.

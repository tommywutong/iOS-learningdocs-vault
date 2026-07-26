---
title: 'includes(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpointofinterestfilter/includes(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/includes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpointofinterestfilter/includes%28_%3A%29.json'
content_hash: 'sha256:87085a9eccce5326'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPointOfInterestFilter](../mkpointofinterestfilter.md)

# includes(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the filter includes the point of interest category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func includes(_ category: MKPointOfInterestCategory) -> Bool
```

## Parameters

- `category` — A point of interest category that the method checks for inclusion in the filter.

## Return Value

`true` if the filter includes the point of interest category; otherwise, `false`.

## See Also

### Querying filter behavior

- [- excludesCategory:](<excludes(__).md>) — Returns a Boolean value indicating whether the filter excludes the point of interest category.

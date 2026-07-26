---
title: 'including(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/pointofinterestcategories/including(_:)-6flda'
source_url: 'https://developer.apple.com/documentation/mapkit/pointofinterestcategories/including(_:)-6flda'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/pointofinterestcategories/including%28_%3A%29-6flda.json'
content_hash: 'sha256:c4641c04e3e4aa39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [PointOfInterestCategories](../pointofinterestcategories.md)

# including(_:)

<sub>Type Method</sub>

Show only points of interest belonging to certain categories from the provided list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func including(_ categories: MKPointOfInterestCategory...) -> PointOfInterestCategories
```

## Parameters

- `categories` — The points of interest categories to include.

## Return Value

Returns the points of interest to include.

## See Also

### Modifying the categories to include or exclude

- [excluding(_:)](<excluding(__)-16bp0.md>) — Show all points of interest except those belonging to certain categories using the array you provide.
- [excluding(_:)](<excluding(__)-4jo9h.md>) — Show all points of interest except those belonging to certain categories using the list you provide.
- [including(_:)](<including(__)-22f7x.md>) — Show only points of interest belonging to certain categories from the provided array.

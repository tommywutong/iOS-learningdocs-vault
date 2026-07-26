---
title: 'init(placemark:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+（26.0 起废弃）, iPadOS 6.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.9+（26.0 起废弃）, tvOS 9.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkmapitem/init(placemark:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/init(placemark:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/init%28placemark%3A%29.json'
content_hash: 'sha256:498adaa272956c43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# init(placemark:)

<sub>Initializer</sub>

Creates and returns a map item object using the specified placemark object.

> [!warning] Deprecated
> Use init(location:address:)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(placemark: MKPlacemark)
```

## Parameters

- `placemark` — The placemark object corresponding to the desired map location. This parameter can’t be `nil`.

## Return Value

An initialized map item object.

## Discussion

Use this method to create a map item for an existing placemark. Don’t use it to create a map item representing the user’s location. To do that, use the [+ mapItemForCurrentLocation](<forcurrentlocation().md>) method instead.

## See Also

### Creating map items

- [+ mapItemForCurrentLocation](<forcurrentlocation().md>) — Creates and returns a singleton map item object representing the user’s location.

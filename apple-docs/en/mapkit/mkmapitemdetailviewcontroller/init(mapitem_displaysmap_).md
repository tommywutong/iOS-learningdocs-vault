---
title: 'init(mapItem:displaysMap:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitemdetailviewcontroller/init(mapitem:displaysmap:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemdetailviewcontroller/init(mapitem:displaysmap:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemdetailviewcontroller/init%28mapitem%3Adisplaysmap%3A%29.json'
content_hash: 'sha256:ef3da435fe0662b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItemDetailViewController](../mkmapitemdetailviewcontroller.md)

# init(mapItem:displaysMap:)

<sub>Initializer</sub>

Create a map item detail view controller

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(mapItem: MKMapItem?, displaysMap: Bool)
```

## Parameters

- `mapItem` — The map item to display, or `nil` to indicate the item is loading.

- `displaysMap` — Specify `true` to display an inline map with the place information. Specify `false` only if the application is already displaying a map view elsewhere.

## See Also

### Creating a map item detail view controller

- [- initWithMapItem:](<init(mapitem_).md>) — Create a map item detail view controller.

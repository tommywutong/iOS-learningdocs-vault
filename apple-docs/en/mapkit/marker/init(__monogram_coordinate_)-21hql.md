---
title: 'init(_:monogram:coordinate:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/marker/init(_:monogram:coordinate:)-21hql'
source_url: 'https://developer.apple.com/documentation/mapkit/marker/init(_:monogram:coordinate:)-21hql'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/marker/init%28_%3Amonogram%3Acoordinate%3A%29-21hql.json'
content_hash: 'sha256:2e534518dd67c903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Marker](../marker.md)

# init(_:monogram:coordinate:)

<sub>Initializer</sub>

Creates a marker at the given location with the provided title string and monogram.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<S>(_ title: S, monogram: Text, coordinate: CLLocationCoordinate2D) where Label == Label<Text, Text>, S : StringProtocol
```

## Parameters

- `title` — The title of the marker.

- `monogram` — A [Text](../../swiftui/text.md) view that contains up to three characters to display on the marker’s balloon.

- `coordinate` — The coordinate used to display the marker.

## See Also

### Creating a marker

- [init(_:coordinate:)](<init(__coordinate_)-82942.md>) — Creates a marker at the given location with the label you provide.
- [init(_:image:coordinate:)](<init(__image_coordinate_)-36l1p.md>) — Creates a marker at the given location with the provided title and image resource to display as the balloon’s icon.
- [init(_:systemImage:coordinate:)](<init(__systemimage_coordinate_)-50yl4.md>) — Creates a marker at the given location with the provided title and a system image the map displays as the balloon’s icon.
- [init(_:coordinate:)](<init(__coordinate_)-8wxlv.md>) — Creates a marker at the given location with the localized string key you provide.
- [init(_:image:coordinate:)](<init(__image_coordinate_)-28mge.md>) — Creates a marker at the given location with the provided localized title and image resource to display as the balloon’s icon.
- [init(_:monogram:coordinate:)](<init(__monogram_coordinate_)-2ojcy.md>) — Creates a marker at the given location with the provided title key and monogram.
- [init(_:systemImage:coordinate:)](<init(__systemimage_coordinate_)-2t4i0.md>) — Creates a marker at the given location with a localized title, and a system image the map displays as the balloon’s icon.
- [init(coordinate:label:)](<init(coordinate_label_).md>) — Creates a marker at the given location with the provided label.
- [init(item:)](<init(item_).md>) — Creates a marker for a given map item using a MapKit-provided label.

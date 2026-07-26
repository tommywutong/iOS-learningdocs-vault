---
title: 'init(placemark:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clplacemark/init(placemark:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/init(placemark:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/init%28placemark%3A%29.json'
content_hash: 'sha256:1640dbe4bfc1c835'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# init(placemark:)

<sub>Initializer</sub>

Initializes and returns a placemark object from another placemark object.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(placemark: CLPlacemark)
```

## Parameters

- `placemark` — The placemark object to use as the source of the data for the new object.

## Return Value

An initialized placemark object.

## Discussion

You can use this method to transfer information from one placemark object to another placemark object.

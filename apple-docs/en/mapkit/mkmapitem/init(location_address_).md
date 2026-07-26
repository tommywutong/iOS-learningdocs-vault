---
title: 'init(location:address:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitem/init(location:address:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/init(location:address:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/init%28location%3Aaddress%3A%29.json'
content_hash: 'sha256:90d6e195711078e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# init(location:address:)

<sub>Initializer</sub>

Creates and returns a map item object using the specified location and address objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(location: CLLocation, address: MKAddress?)
```

## Parameters

- `location` — A [CLLocation](../../corelocation/cllocation.md).

- `address` — An [MKAddress](../mkaddress.md).

## Return Value

An initialized map item object.

## Discussion

Use this method to create a map item for a specific location. Don’t use it to create a map item representing the current location of someone’s device, instead use the ```MKMapItem/forCurrentLocation()`` method.

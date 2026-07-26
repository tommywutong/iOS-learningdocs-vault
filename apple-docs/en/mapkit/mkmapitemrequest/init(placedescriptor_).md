---
title: 'init(placeDescriptor:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitemrequest/init(placedescriptor:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemrequest/init(placedescriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemrequest/init%28placedescriptor%3A%29.json'
content_hash: 'sha256:a0ad5098ecd1ea38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItemRequest](../mkmapitemrequest.md)

# init(placeDescriptor:)

<sub>Initializer</sub>

Creates a new map item request with the specified place descriptor

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(placeDescriptor: PlaceDescriptor)
```

## Parameters

- `placeDescriptor` — The [PlaceDescriptor](../../geotoolbox/placedescriptor.md) the system should use to try to resolve information about desired map location. This parameter can’t be `nil`.

## Return Value

An initialized map item object.

## Discussion

Use this method to create a `MKMapItemRequest` from a [PlaceDescriptor](../../geotoolbox/placedescriptor.md) which you can then attempt to resolve asynchronously as shown here.

```swift
    Task {
        do {
            let request = MKMapItemRequest(placeDescriptor: descriptor)
            mapItem = try await request.mapItem
        } catch {
            handleLoadError(error, for: descriptor)
        }
    }
```

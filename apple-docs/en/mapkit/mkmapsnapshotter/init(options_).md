---
title: 'init(options:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapsnapshotter/init(options:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/init(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/init%28options%3A%29.json'
content_hash: 'sha256:b568b8eab7f783c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapSnapshotter](../mkmapsnapshotter.md)

# init(options:)

<sub>Initializer</sub>

Creates and returns a snapshotter object based on the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(options: MKMapSnapshotter.Options)
```

## Parameters

- `options` — The options to use when capturing the map imagery. See [Options](options.md). This parameter may not be `nil`.

## Return Value

An initialized snapshotter object.

## See Also

### Creating a snapshotter object

- [Options](options.md) — The options the snapshotter initializer uses to create a snapshotter to capture map-based imagery.

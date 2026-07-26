---
title: 'init(circle:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkcirclerenderer/init(circle:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcirclerenderer/init(circle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcirclerenderer/init%28circle%3A%29.json'
content_hash: 'sha256:d062c778db7bf301'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCircleRenderer](../mkcirclerenderer.md)

# init(circle:)

<sub>Initializer</sub>

Creates a new overlay view using the specified circle overlay object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(circle: MKCircle)
```

## Parameters

- `circle` — The circle overlay containing the information about the circular area for the renderer to draw. The renderer maintains a strong reference to the object you provide. This parameter can’t be `nil`.

## Return Value

An initialized circle renderer object.

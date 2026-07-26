---
title: 'init(scope:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/maplocationcompass/init(scope:)'
source_url: 'https://developer.apple.com/documentation/mapkit/maplocationcompass/init(scope:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/maplocationcompass/init%28scope%3A%29.json'
content_hash: 'sha256:f0b680011ba3cdc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapLocationCompass](../maplocationcompass.md)

# init(scope:)

<sub>Initializer</sub>

Creates a new map location compass with the provided scope.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(scope: Namespace.ID? = nil)
```

## Parameters

- `scope` — The namespace the framework passes to the associated [Map](../map.md) and `MapLocationCompass/mapScope(_:)`. For use outside of `MapLocationCompass/mapControls(_:)`.

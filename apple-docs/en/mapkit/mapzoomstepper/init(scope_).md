---
title: 'init(scope:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 14.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapzoomstepper/init(scope:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapzoomstepper/init(scope:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapzoomstepper/init%28scope%3A%29.json'
content_hash: 'sha256:56fbf71835d9a919'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapZoomStepper](../mapzoomstepper.md)

# init(scope:)

<sub>Initializer</sub>

Creates a new zoom stepper with the scope you specify.

<sub>Mac Catalyst, macOS</sub>

```swift
@MainActor @preconcurrency init(scope: Namespace.ID? = nil)
```

## Parameters

- `scope` — A [Namespace.ID](../../swiftui/namespace/id.md) value that identifies this namespace.

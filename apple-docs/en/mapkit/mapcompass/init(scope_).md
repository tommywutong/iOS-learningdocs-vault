---
title: 'init(scope:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcompass/init(scope:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcompass/init(scope:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcompass/init%28scope%3A%29.json'
content_hash: 'sha256:3670552c8229398d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCompass](../mapcompass.md)

# init(scope:)

<sub>Initializer</sub>

Creates a new map compass with the scope you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(scope: Namespace.ID? = nil)
```

## Parameters

- `scope` — A [Namespace.ID](../../swiftui/namespace/id.md) value that identifies a namespace and that you use to associate this control with a map instance.

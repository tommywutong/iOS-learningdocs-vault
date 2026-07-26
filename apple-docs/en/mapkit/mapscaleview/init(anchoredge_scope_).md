---
title: 'init(anchorEdge:scope:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapscaleview/init(anchoredge:scope:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapscaleview/init(anchoredge:scope:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapscaleview/init%28anchoredge%3Ascope%3A%29.json'
content_hash: 'sha256:375e738ac2be3141'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapScaleView](../mapscaleview.md)

# init(anchorEdge:scope:)

<sub>Initializer</sub>

Creates a map scale view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency init(anchorEdge: HorizontalEdge = .leading, scope: Namespace.ID? = nil)
```

## Parameters

- `anchorEdge` — The fixed edge the scale grows and shrinks from. Use this outside of `Map/mapControls(_:)` view modifier.

- `scope` — A [Namespace.ID](../../swiftui/namespace/id.md) value that identifies this namespace and that you can use to associate this control with a map instance.

## See Also

### Creating a map scale view

- [init(alignment:scope:)](<init(alignment_scope_).md>) — Creates a scale view with the provided alignment and scope.

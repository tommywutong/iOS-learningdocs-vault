---
title: 'init(alignment:scope:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapscaleview/init(alignment:scope:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapscaleview/init(alignment:scope:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapscaleview/init%28alignment%3Ascope%3A%29.json'
content_hash: 'sha256:cec98873ce56d219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapScaleView](../mapscaleview.md)

# init(alignment:scope:)

<sub>Initializer</sub>

Creates a scale view with the provided alignment and scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency init(alignment: HorizontalAlignment = .leading, scope: Namespace.ID? = nil)
```

## Parameters

- `alignment` — The alignment that describes the positioning of the scale view. The default is [leading](../../swiftui/horizontalalignment/leading.md).

- `scope` — A [Namespace.ID](../../swiftui/namespace/id.md) value that identifies this namespace and that you can use to associate this control with a map instance.

## Return Value

An initialized scale view.

## See Also

### Creating a map scale view

- [init(anchorEdge:scope:)](<init(anchoredge_scope_).md>) — Creates a map scale view.

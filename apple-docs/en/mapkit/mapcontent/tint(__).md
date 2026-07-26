---
title: 'tint(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/tint(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/tint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/tint%28_%3A%29.json'
content_hash: 'sha256:5c0a6d68a8967b34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# tint(_:)

<sub>Instance Method</sub>

The tint shape style to apply to map content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func tint<S>(_ tint: S) -> some MapContent where S : ShapeStyle

```

## Parameters

- `tint` — The tint to apply.

## Return Value

Returns [MapContent](../mapcontent.md) with overlays drawn with the [ShapeStyle](../../swiftui/shapestyle.md) you specified.

## See Also

### Setting the content style

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Specifies the shape style used to fill content in drawing map overlays.

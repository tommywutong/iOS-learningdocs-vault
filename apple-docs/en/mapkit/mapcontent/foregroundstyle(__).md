---
title: 'foregroundStyle(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/foregroundstyle(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/foregroundstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/foregroundstyle%28_%3A%29.json'
content_hash: 'sha256:5017eeee2a11d6d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# foregroundStyle(_:)

<sub>Instance Method</sub>

Specifies the shape style used to fill content in drawing map overlays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func foregroundStyle(_ content: some ShapeStyle) -> some MapContent

```

## Parameters

- `content` — The shape style to apply to the overlay.

## Return Value

Returns [MapContent](../mapcontent.md) with the foreground style you specified.

## See Also

### Setting the content style

- [tint(_:)](<tint(__).md>) — The tint shape style to apply to map content.

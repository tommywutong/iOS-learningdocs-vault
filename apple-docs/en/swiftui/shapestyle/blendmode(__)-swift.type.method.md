---
title: 'blendMode(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/blendmode(_:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/blendmode(_:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/blendmode%28_%3A%29-swift.type.method.json'
content_hash: 'sha256:81e7406986a18ddb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# blendMode(_:)

<sub>Type Method</sub>

Returns a new style based on the current style that uses `mode` as its blend mode when drawing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func blendMode(_ mode: BlendMode) -> some ShapeStyle

```

## Discussion

In most contexts the current style is the foreground but e.g. when setting the value of the background style, that becomes the current implicit style.

For example, a circle filled with the current foreground style and the overlay blend mode:

```swift
Circle().fill(.blendMode(.overlay))
```

## See Also

### Configuring the default shape style

- [opacity(_:)](<opacity(__)-swift.type.method.md>) — Returns a new style based on the current style that multiplies by `opacity` when drawing.
- [shadow(_:)](<shadow(__)-swift.type.method.md>) — Returns a shape style that applies the specified shadow style to the current style.

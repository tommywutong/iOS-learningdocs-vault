---
title: 'opacity(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/opacity(_:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/opacity(_:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/opacity%28_%3A%29-swift.type.method.json'
content_hash: 'sha256:b0b9389133095e5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# opacity(_:)

<sub>Type Method</sub>

Returns a new style based on the current style that multiplies by `opacity` when drawing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func opacity(_ opacity: Double) -> some ShapeStyle

```

## Discussion

In most contexts the current style is the foreground but e.g. when setting the value of the background style, that becomes the current implicit style.

For example, a circle filled with the current foreground style at fifty-percent opacity:

```swift
Circle().fill(.opacity(0.5))
```

## See Also

### Configuring the default shape style

- [blendMode(_:)](<blendmode(__)-swift.type.method.md>) — Returns a new style based on the current style that uses `mode` as its blend mode when drawing.
- [shadow(_:)](<shadow(__)-swift.type.method.md>) — Returns a shape style that applies the specified shadow style to the current style.

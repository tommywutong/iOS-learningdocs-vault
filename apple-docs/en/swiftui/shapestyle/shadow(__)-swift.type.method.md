---
title: 'shadow(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/shadow(_:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/shadow(_:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/shadow%28_%3A%29-swift.type.method.json'
content_hash: 'sha256:65d1396e007df561'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# shadow(_:)

<sub>Type Method</sub>

Returns a shape style that applies the specified shadow style to the current style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func shadow(_ style: ShadowStyle) -> some ShapeStyle

```

## Parameters

- `style` — The shadow style to apply.

## Return Value

A new shape style based on the current style that uses the specified shadow style.

## Discussion

In most contexts the current style is the foreground, but not always. For example, when setting the value of the background style, that becomes the current implicit style.

The following example creates a circle filled with the current foreground style that uses an inner shadow:

```swift
Circle().fill(.shadow(.inner(radius: 1, y: 1)))
```

## See Also

### Configuring the default shape style

- [blendMode(_:)](<blendmode(__)-swift.type.method.md>) — Returns a new style based on the current style that uses `mode` as its blend mode when drawing.
- [opacity(_:)](<opacity(__)-swift.type.method.md>) — Returns a new style based on the current style that multiplies by `opacity` when drawing.

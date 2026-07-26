---
title: 'shadow(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shapestyle/shadow(_:)-swift.method'
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/shadow(_:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/shadow%28_%3A%29-swift.method.json'
content_hash: 'sha256:c8a09a89cae86c2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# shadow(_:)

<sub>Instance Method</sub>

Applies the specified shadow effect to the shape style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func shadow(_ style: ShadowStyle) -> some ShapeStyle

```

## Parameters

- `style` — The shadow style to apply.

## Return Value

A new shape style that uses the specified shadow style.

## Discussion

For example, you can create a rectangle that adds a drop shadow to the [red](red.md) shape style.

```swift
Rectangle().fill(.red.shadow(.drop(radius: 2, y: 3)))
```

## See Also

### Modifying a shape style

- [blendMode(_:)](<blendmode(__)-swift.method.md>) — Returns a new style based on `self` that applies the specified blend mode when drawing.
- [opacity(_:)](<opacity(__)-swift.method.md>) — Returns a new style based on `self` that multiplies by the specified opacity when drawing.

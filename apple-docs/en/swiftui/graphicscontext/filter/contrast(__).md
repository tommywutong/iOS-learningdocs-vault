---
title: 'contrast(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/contrast(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/contrast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/contrast%28_%3A%29.json'
content_hash: 'sha256:fe793510bc3c390f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# contrast(_:)

<sub>Type Method</sub>

Returns a filter that applies a contrast adjustment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func contrast(_ amount: Double) -> GraphicsContext.Filter
```

## Parameters

- `amount` — An amount to adjust the contrast. A value of zero leaves the result completely gray. A value of one leaves the result unchanged. You can use values greater than one.

## Return Value

A filter that applies a contrast adjustment.

## Discussion

This filter is equivalent to the `contrast` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

## See Also

### Changing brightness and contrast

- [brightness(_:)](<brightness(__).md>) — Returns a filter that applies a brightness adjustment.

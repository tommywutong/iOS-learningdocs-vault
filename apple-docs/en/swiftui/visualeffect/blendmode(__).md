---
title: 'blendMode(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/blendmode(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/blendmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/blendmode%28_%3A%29.json'
content_hash: 'sha256:c89a0009b94b89ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# blendMode(_:)

<sub>Instance Method</sub>

Sets the blend mode for compositing this view with overlapping views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func blendMode(_ blendMode: BlendMode) -> some VisualEffect

```

## Parameters

- `blendMode` — The [BlendMode](../blendmode.md) for compositing.

## Return Value

An effect that applies `blendMode` to this view.

## Discussion

Use `blendMode(_:)` to combine overlapping views and use a different visual effect to produce the result. The [BlendMode](../blendmode.md) enumeration defines many possible effects.

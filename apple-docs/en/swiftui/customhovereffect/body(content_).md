---
title: 'body(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customhovereffect/body(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/body(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/body%28content%3A%29.json'
content_hash: 'sha256:dae321bf25905b82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# body(content:)

<sub>Instance Method</sub>

Defines the effect produced by this effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func body(content: Self.Content) -> Self.Body
```

## Parameters

- `content` — An empty effect you use to compose the custom effect.

## Return Value

A custom effect.

## Discussion

You implement this method to describe a custom effect to apply to a view. `content` is an empty effect you use to build your effect, which will later be applied to a View, or combined with other `CustomHoverEffect`s.

## Default Implementations

### CustomHoverEffect Implementations

- [body(content:)](<body(content_)-1hbi3.md>) — Defines the effect produced by this effect.

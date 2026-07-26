---
title: 'init(delegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerinteraction/init(delegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerinteraction/init(delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerinteraction/init%28delegate%3A%29.json'
content_hash: 'sha256:b561c1cf07923d81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerInteraction](../uipointerinteraction.md)

# init(delegate:)

<sub>Initializer</sub>

Initializes a pointer interaction object with a specified delegate object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(delegate: (any UIPointerInteractionDelegate)?)
```

## Parameters

- `delegate` — An object the framework calls to respond to pointer movements.

## Discussion

If you create a `UIPointerInteraction` without a delegate by passing `nil` to the initializer, UIKit automatically applies a pointer effect it deems appropriate to the view. Initializing with `nil` is the equivalent of creating a `UIPointerStyle` with [UIPointerEffect.automatic(_:)](<../uipointereffect-swift.enum/automatic(__).md>). Based on the view’s appearance, `.automatic` transforms into one of the concrete effects (`.highlight`, `.lift`, `.hover`).

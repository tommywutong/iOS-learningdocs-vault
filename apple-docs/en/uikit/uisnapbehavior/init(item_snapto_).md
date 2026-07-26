---
title: 'init(item:snapTo:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisnapbehavior/init(item:snapto:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisnapbehavior/init(item:snapto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisnapbehavior/init%28item%3Asnapto%3A%29.json'
content_hash: 'sha256:c4b4b92f54f1b70a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISnapBehavior](../uisnapbehavior.md)

# init(item:snapTo:)

<sub>Initializer</sub>

Initializes a snap behavior with a dynamic item and a snap point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(item: any UIDynamicItem, snapTo point: CGPoint)
```

## Parameters

- `item` — The dynamic item that you want to apply a snap behavior to.

- `point` — The point that you want the dynamic item to snap to. The coordinate system for the `point` parameter depends on how you initialize the dynamic animator you’re adding the snap behavior to, as described in the overview of [UIDynamicAnimator](../uidynamicanimator.md).

## Return Value

The initialized snap behavior, or `nil` if there was a problem initializing the object.

## Discussion

At the conclusion of a snap, the rotation value (as indicated by the [transform](../uidynamicitem/transform.md) property) for a dynamic item is `0`.

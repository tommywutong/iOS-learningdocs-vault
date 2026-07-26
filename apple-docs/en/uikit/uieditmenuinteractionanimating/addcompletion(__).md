---
title: 'addCompletion(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteractionanimating/addcompletion(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteractionanimating/addcompletion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteractionanimating/addcompletion%28_%3A%29.json'
content_hash: 'sha256:183c96030b9c6633'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteractionAnimating](../uieditmenuinteractionanimating.md)

# addCompletion(_:)

<sub>Instance Method</sub>

Adds a closure to perform operations when the edit menu interaction presentation animations are complete.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func addCompletion(_ completion: @escaping () -> Void)
```

## Parameters

- `completion` — A closure that performs operations after the animations complete.

## See Also

### Adding Animations

- [- addAnimations:](<addanimations(__).md>) — Adds a closure that performs animations to run alongside the edit menu interaction presentation.

---
title: 'addAnimations(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteractionanimating/addanimations(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteractionanimating/addanimations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteractionanimating/addanimations%28_%3A%29.json'
content_hash: 'sha256:7a35cb7294e1519d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteractionAnimating](../uieditmenuinteractionanimating.md)

# addAnimations(_:)

<sub>Instance Method</sub>

Adds a closure that performs animations to run alongside the edit menu interaction presentation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func addAnimations(_ animations: @escaping () -> Void)
```

## Parameters

- `animations` — A closure that performs animations.

## See Also

### Adding Animations

- [- addCompletion:](<addcompletion(__).md>) — Adds a closure to perform operations when the edit menu interaction presentation animations are complete.

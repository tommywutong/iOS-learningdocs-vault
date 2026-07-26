---
title: 'addCompletion(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraganimating/addcompletion(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraganimating/addcompletion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraganimating/addcompletion%28_%3A%29.json'
content_hash: 'sha256:ffe336dac2ae7d34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragAnimating](../uidraganimating.md)

# addCompletion(_:)

<sub>Instance Method</sub>

Adds an animation completion block to run when a view animation has ended.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func addCompletion(_ completion: @escaping (UIViewAnimatingPosition) -> Void)
```

## Parameters

- `completion` — A block that sets animatable view properties.

## See Also

### Adding animations

- [- addAnimations:](<addanimations(__).md>) — Adds an animation block for modifying a view animation while it’s running.

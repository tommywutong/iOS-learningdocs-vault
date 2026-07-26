---
title: 'animate(alongsideChanges:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextcursordroppositionanimator/animate(alongsidechanges:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextcursordroppositionanimator/animate(alongsidechanges:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextcursordroppositionanimator/animate%28alongsidechanges%3Acompletion%3A%29.json'
content_hash: 'sha256:76fc00f99cb6a0c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextCursorDropPositionAnimator](../uitextcursordroppositionanimator.md)

# animate(alongsideChanges:completion:)

<sub>Instance Method</sub>

Optionally, provide an animation block or completion block to run alongside cursor appearance or position update animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func animate(alongsideChanges animation: (() -> Void)?, completion: (() -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func animate(alongsideChanges animation: (() -> Void)?) async
```

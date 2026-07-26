---
title: 'displayLink(target:selector:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwindowscene/displaylink(target:selector:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/displaylink(target:selector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/displaylink%28target%3Aselector%3A%29.json'
content_hash: 'sha256:afadf5c4621a82c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# displayLink(target:selector:)

<sub>Instance Method</sub>

Creates a display link targeting the display associated with this scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func displayLink(target: Any, selector sel: Selector) -> CADisplayLink?
```

## Parameters

- `target` — An object that is the target of the display link callback.

- `sel` — A selector on `target` to call when the display link fires.

## Return Value

A new display link, or `nil` only in exceptional cases where the system cannot construct a display link.

## Discussion

The returned display link is automatically retargeted when the scene moves between displays.

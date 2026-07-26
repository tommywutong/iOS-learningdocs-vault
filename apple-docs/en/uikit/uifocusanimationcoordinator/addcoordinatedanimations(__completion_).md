---
title: 'addCoordinatedAnimations(_:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusanimationcoordinator/addcoordinatedanimations(_:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator/addcoordinatedanimations(_:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusanimationcoordinator/addcoordinatedanimations%28_%3Acompletion%3A%29.json'
content_hash: 'sha256:5f11d0352c1d4b26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusAnimationCoordinator](../uifocusanimationcoordinator.md)

# addCoordinatedAnimations(_:completion:)

<sub>Instance Method</sub>

Specifies the animations to coordinate with the active focus animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addCoordinatedAnimations(_ animations: (() -> Void)?, completion: (() -> Void)? = nil)
```

## Parameters

- `animations` — The animation to be run.

- `completion` — A block object to be executed after the main animation completes. Any animations specified are run in the same animation context as the main animation.

## Discussion

Use this method to coordinate your custom animations with the system animations for adding or removing focus.

Unless the duration time is inherited, the specified animations may not run in the same context as the main animation. It is perfectly legitimate to specify only a completion block.

## See Also

### Adding animations to focus updates

- [- addCoordinatedFocusingAnimations:completion:](<addcoordinatedfocusinganimations(__completion_).md>) — Runs the specified set of animations together with the system animations for adding focus to an item.
- [- addCoordinatedUnfocusingAnimations:completion:](<addcoordinatedunfocusinganimations(__completion_).md>) — Runs the specified set of animations together with the system animations for removing focus from an item.
- [UIFocusAnimationContext](../uifocusanimationcontext.md) — Information about focusing animations being performed by the system.

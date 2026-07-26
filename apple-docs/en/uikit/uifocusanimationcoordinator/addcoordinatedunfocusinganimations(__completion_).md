---
title: 'addCoordinatedUnfocusingAnimations(_:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusanimationcoordinator/addcoordinatedunfocusinganimations(_:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator/addcoordinatedunfocusinganimations(_:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusanimationcoordinator/addcoordinatedunfocusinganimations%28_%3Acompletion%3A%29.json'
content_hash: 'sha256:374381ced2504b44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusAnimationCoordinator](../uifocusanimationcoordinator.md)

# addCoordinatedUnfocusingAnimations(_:completion:)

<sub>Instance Method</sub>

Runs the specified set of animations together with the system animations for removing focus from an item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addCoordinatedUnfocusingAnimations(_ animations: ((any UIFocusAnimationContext) -> Void)?, completion: (() -> Void)? = nil)
```

## Parameters

- `animations` — A block object containing your unfocus-related animations. This block has no return value and takes the following parameter: - **context** — An object containing information about the main animations. Use this information to configure your custom animations. For more information, see [UIFocusAnimationContext](../uifocusanimationcontext.md).

- `completion` — The block object to execute after the main animation completes. The specified animations are run in the same animation context as the main animation.

## Discussion

When focus is being removed from an item, use this method to coordinate your custom animations with the system animations.  The animations you specify are run in the same animation block as the system animations. Use the information in the `context` parameter to determine any custom behaviors for your animations. For example, you might configure your animations to run in half the time as the main animation and start after a short delay.

## See Also

### Adding animations to focus updates

- [- addCoordinatedFocusingAnimations:completion:](<addcoordinatedfocusinganimations(__completion_).md>) — Runs the specified set of animations together with the system animations for adding focus to an item.
- [- addCoordinatedAnimations:completion:](<addcoordinatedanimations(__completion_).md>) — Specifies the animations to coordinate with the active focus animation.
- [UIFocusAnimationContext](../uifocusanimationcontext.md) — Information about focusing animations being performed by the system.

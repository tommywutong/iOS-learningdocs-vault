---
title: followsUndockedKeyboard
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeyboardlayoutguide/followsundockedkeyboard
source_url: 'https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/followsundockedkeyboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyboardlayoutguide/followsundockedkeyboard.json'
content_hash: 'sha256:edd6e040997e2426'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyboardLayoutGuide](../uikeyboardlayoutguide.md)

# followsUndockedKeyboard

<sub>Instance Property</sub>

A Boolean value that determines if the layout guide tracks the keyboard when it’s undocked from the bottom of the screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var followsUndockedKeyboard: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md); the guide tracks the keyboard only when docked. When the keyboard is off screen or undocked, the guide’s [topAnchor](../uilayoutguide/topanchor.md) matches the [bottomAnchor](../uilayoutguide/bottomanchor.md) of [safeAreaLayoutGuide](../uiview/safearealayoutguide.md). To follow all keyboard anchors even when undocked or floating, set [followsUndockedKeyboard](followsundockedkeyboard.md) to [true](../../swift/true.md).

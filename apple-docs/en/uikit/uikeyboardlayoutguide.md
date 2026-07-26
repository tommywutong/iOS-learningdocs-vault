---
title: UIKeyboardLayoutGuide
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeyboardlayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyboardlayoutguide.json'
content_hash: 'sha256:ec0cc2d1d2403611'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKeyboardLayoutGuide

<sub>Class</sub>

A layout guide that represents the space the keyboard occupies in your app’s layout.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIKeyboardLayoutGuide
```

## Overview

Configure the keyboard layout guide, and activate or deactivate constraints so your app’s layout adjusts to the keyboard in different situations. See [Adjusting your layout with keyboard layout guide](adjusting-your-layout-with-keyboard-layout-guide.md) for an example of how to dynamically respond to keyboard presentation, dismissal, and movement.

## Relationships

- **Inherits From**: [UITrackingLayoutGuide](uitrackinglayoutguide.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## Topics

### Supporting floating and undocked keyboards

- [followsUndockedKeyboard](uikeyboardlayoutguide/followsundockedkeyboard.md) — A Boolean value that determines if the layout guide tracks the keyboard when it’s undocked from the bottom of the screen.

### Adjusting dismissal sensitivity

- [keyboardDismissPadding](uikeyboardlayoutguide/keyboarddismisspadding.md) — A value that adds padding above the keyboard to increase the size of the touch area for the scrolling dismissal gesture.

### Configuring safe area usage

- [usesBottomSafeArea](uikeyboardlayoutguide/usesbottomsafearea.md) — A Boolean value that indicates whether the layout guide uses the view’s safe area layout guide.

## See Also

### Keyboard layout

- [Adjusting your layout with keyboard layout guide](adjusting-your-layout-with-keyboard-layout-guide.md) — Respond dynamically to keyboard movement by using the tracking features of the keyboard layout guide.
- [UITrackingLayoutGuide](uitrackinglayoutguide.md) — A layout guide that automatically activates and deactivates layout constraints depending on its proximity to edges.

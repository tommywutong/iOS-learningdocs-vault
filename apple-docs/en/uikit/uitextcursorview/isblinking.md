---
title: isBlinking
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextcursorview/isblinking
source_url: 'https://developer.apple.com/documentation/uikit/uitextcursorview/isblinking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextcursorview/isblinking.json'
content_hash: 'sha256:d22ad4bc5076220e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextCursorView](../uitextcursorview.md)

# isBlinking

<sub>Instance Property</sub>

A Boolean value that determines whether the blink animation is running.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isBlinking: Bool { get set }
```

## Discussion

Set this property to [true](../../swift/true.md) when you want the system to start animating the blink effect for the insertion point cursor. Set the property to [false](../../swift/false.md) to stop the blink animation.

## See Also

### Determining the animation state

- [- resetBlinkAnimation](<resetblinkanimation().md>) — Resets the blink animation to avoid glitches while someone is typing.

---
title: resetBlinkAnimation()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextcursorview/resetblinkanimation()
source_url: 'https://developer.apple.com/documentation/uikit/uitextcursorview/resetblinkanimation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextcursorview/resetblinkanimation%28%29.json'
content_hash: 'sha256:81f7cfb88edca949'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextCursorView](../uitextcursorview.md)

# resetBlinkAnimation()

<sub>Instance Method</sub>

Resets the blink animation to avoid glitches while someone is typing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resetBlinkAnimation()
```

## Discussion

When the cursor is moving in your text view, call this method to prevent the insertion point from blinking.

## See Also

### Determining the animation state

- [blinking](isblinking.md) — A Boolean value that determines whether the blink animation is running.

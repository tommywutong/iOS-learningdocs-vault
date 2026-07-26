---
title: endFloatingCursor()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/endfloatingcursor()
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/endfloatingcursor()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/endfloatingcursor%28%29.json'
content_hash: 'sha256:93acdd0f98c1ccf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# endFloatingCursor()

<sub>Instance Method</sub>

Tells the object when the gesture that the system uses to manipulate the cursor ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func endFloatingCursor()
```

## Discussion

UIKit calls this method at the end of the two-finger pan gesture used to pick up the cursor. You can use this method to clean up the visual state of your text view.

If you do not implement this method, UIKit provides visual feedback only when the selection changes.

## See Also

### Managing the floating cursor

- [- beginFloatingCursorAtPoint:](<beginfloatingcursor(at_).md>) — Tells the object when the gesture that the system uses to manipulate the cursor begins.
- [- updateFloatingCursorAtPoint:](<updatefloatingcursor(at_).md>) — Tells the object that the floating cursor moved to a new location.

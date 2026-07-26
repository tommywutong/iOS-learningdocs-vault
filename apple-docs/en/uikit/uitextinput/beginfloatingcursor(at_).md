---
title: 'beginFloatingCursor(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/beginfloatingcursor(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/beginfloatingcursor(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/beginfloatingcursor%28at%3A%29.json'
content_hash: 'sha256:c7dcd85a019ca4c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# beginFloatingCursor(at:)

<sub>Instance Method</sub>

Tells the object when the gesture that the system uses to manipulate the cursor begins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func beginFloatingCursor(at point: CGPoint)
```

## Parameters

- `point` — The point at which the gesture occurred in your view. This point is in the coordinate space of the view in the [textInputView](textinputview.md) property.

## Discussion

UIKit calls this method when the user begins to perform a two-finger pan gesture to pick up the cursor. You can use this method to update the visual state of your text view. For example, you might use this method to display custom visual feedback for cursor movements.

If you do not implement this method, UIKit provides visual feedback only when the selection changes.

## See Also

### Managing the floating cursor

- [- updateFloatingCursorAtPoint:](<updatefloatingcursor(at_).md>) — Tells the object that the floating cursor moved to a new location.
- [- endFloatingCursor](<endfloatingcursor().md>) — Tells the object when the gesture that the system uses to manipulate the cursor ends.

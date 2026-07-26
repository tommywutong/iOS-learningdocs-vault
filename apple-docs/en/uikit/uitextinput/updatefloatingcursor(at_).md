---
title: 'updateFloatingCursor(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/updatefloatingcursor(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/updatefloatingcursor(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/updatefloatingcursor%28at%3A%29.json'
content_hash: 'sha256:a23352ead6417c10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# updateFloatingCursor(at:)

<sub>Instance Method</sub>

Tells the object that the floating cursor moved to a new location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func updateFloatingCursor(at point: CGPoint)
```

## Parameters

- `point` — The new touch point in the underlying view. This point is in the coordinate space of the view in the [textInputView](textinputview.md) property.

## Discussion

UIKit calls this method when the touch location changes for the two-finger pan gesture used to move the cursor. You can use this method to update the visual state of your text view. For example, you might use this method to display custom visual feedback for cursor movements.This method may be called multiple times while the user’s fingers are moving, so your implementation should be fast. If you do not implement this method, UIKit provides visual feedback only when the selection changes.

## See Also

### Managing the floating cursor

- [- beginFloatingCursorAtPoint:](<beginfloatingcursor(at_).md>) — Tells the object when the gesture that the system uses to manipulate the cursor begins.
- [- endFloatingCursor](<endfloatingcursor().md>) — Tells the object when the gesture that the system uses to manipulate the cursor ends.

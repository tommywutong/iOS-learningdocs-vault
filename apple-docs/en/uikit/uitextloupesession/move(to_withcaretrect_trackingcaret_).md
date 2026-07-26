---
title: 'move(to:withCaretRect:trackingCaret:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextloupesession/move(to:withcaretrect:trackingcaret:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextloupesession/move(to:withcaretrect:trackingcaret:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextloupesession/move%28to%3Awithcaretrect%3Atrackingcaret%3A%29.json'
content_hash: 'sha256:9f77720ab302d0a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextLoupeSession](../uitextloupesession.md)

# move(to:withCaretRect:trackingCaret:)

<sub>Instance Method</sub>

Moves the loupe to the specified point in the session’s associated view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func move(to point: CGPoint, withCaretRect caretRect: CGRect, trackingCaret tracksCaret: Bool)
```

## Parameters

- `point` — The new location you want to magnify with the loupe. When creating the loupe with a gesture recognizer, specify the location of the gesture.

- `caretRect` — The current position of the caret handle. Specify [CGRectNull](../../coregraphics/cgrectnull.md) if the view doesn’t contain a selection or the caret isn’t visible.

- `tracksCaret` — `true` if you want the loupe to track the movements of the caret. If you specify `true`, provide a valid rectangle in the `caretRect` parameter. Specify `false` to continue tracking the location of touch events.

## Discussion

Call this method repeatedly from a gesture recognizer when the touch location changes.

## See Also

### Updating the loupe during the session

- [- invalidate](<invalidate().md>) — Hides the loupe and cleans up any session-related state.

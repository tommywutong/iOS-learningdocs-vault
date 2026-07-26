---
title: invalidate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextloupesession/invalidate()
source_url: 'https://developer.apple.com/documentation/uikit/uitextloupesession/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextloupesession/invalidate%28%29.json'
content_hash: 'sha256:b5b0a3fef2060da3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextLoupeSession](../uitextloupesession.md)

# invalidate()

<sub>Instance Method</sub>

Hides the loupe and cleans up any session-related state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func invalidate()
```

## Discussion

Call this method when you’re ready to hide the loupe. After calling this method, you can remove your reference to the session.

## See Also

### Updating the loupe during the session

- [- moveToPoint:withCaretRect:trackingCaret:](<move(to_withcaretrect_trackingcaret_).md>) — Moves the loupe to the specified point in the session’s associated view.

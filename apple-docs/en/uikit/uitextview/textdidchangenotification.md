---
title: textDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/textdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/textdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/textdidchangenotification.json'
content_hash: 'sha256:74e48d6c520439c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# textDidChangeNotification

<sub>Type Property</sub>

A notification that alerts observers when the text in a text view changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let textDidChangeNotification: NSNotification.Name
```

## Discussion

The affected view is stored in the `object` parameter of the notification. The `userInfo` dictionary is not used.

## See Also

### Managing the editing behavior

- [editable](iseditable.md) — A Boolean value that indicates whether the text view is editable.
- [allowsEditingTextAttributes](allowseditingtextattributes.md) — A Boolean value that indicates whether the text view allows the user to edit style information.
- [UITextViewTextDidBeginEditingNotification](textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text view.
- [UITextViewTextDidEndEditingNotification](textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text view.

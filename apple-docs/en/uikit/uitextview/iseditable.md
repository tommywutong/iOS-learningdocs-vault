---
title: isEditable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/iseditable
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/iseditable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/iseditable.json'
content_hash: 'sha256:ee25adb78c0c6e91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# isEditable

<sub>Instance Property</sub>

A Boolean value that indicates whether the text view is editable.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isEditable: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md).

## See Also

### Managing the editing behavior

- [allowsEditingTextAttributes](allowseditingtextattributes.md) — A Boolean value that indicates whether the text view allows the user to edit style information.
- [UITextViewTextDidBeginEditingNotification](textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text view.
- [UITextViewTextDidChangeNotification](textdidchangenotification.md) — A notification that alerts observers when the text in a text view changes.
- [UITextViewTextDidEndEditingNotification](textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text view.

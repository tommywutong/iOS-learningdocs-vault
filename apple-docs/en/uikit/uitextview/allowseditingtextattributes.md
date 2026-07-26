---
title: allowsEditingTextAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/allowseditingtextattributes
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/allowseditingtextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/allowseditingtextattributes.json'
content_hash: 'sha256:58b82f3eede5733a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# allowsEditingTextAttributes

<sub>Instance Property</sub>

A Boolean value that indicates whether the text view allows the user to edit style information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsEditingTextAttributes: Bool { get set }
```

## Discussion

When set to [true](../../swift/true.md), the text view allows the user to change the basic styling of the currently selected text. The available style options are listed in the edit menu and only apply to the selection.

The default value of this property is [false](../../swift/false.md).

## See Also

### Managing the editing behavior

- [editable](iseditable.md) — A Boolean value that indicates whether the text view is editable.
- [UITextViewTextDidBeginEditingNotification](textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text view.
- [UITextViewTextDidChangeNotification](textdidchangenotification.md) — A notification that alerts observers when the text in a text view changes.
- [UITextViewTextDidEndEditingNotification](textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text view.

---
title: clearsOnBeginEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/clearsonbeginediting
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/clearsonbeginediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/clearsonbeginediting.json'
content_hash: 'sha256:fdc1ccaa99d311c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# clearsOnBeginEditing

<sub>Instance Property</sub>

A Boolean value that determines whether the text field removes old text when editing begins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var clearsOnBeginEditing: Bool { get set }
```

## Discussion

If this property is set to [true](../../swift/true.md), the text field’s previous text is cleared when the user selects the text field to begin editing. If [false](../../swift/false.md), the text field places an insertion point at the place where the user tapped the field.

> [!note] Note
> Even if this property is set to [true](../../swift/true.md), the text field delegate can override this behavior by returning [false](../../swift/false.md) from its [- textFieldShouldClear:](<../uitextfielddelegate/textfieldshouldclear(__).md>) method.

## See Also

### Managing the editing behavior

- [editing](isediting.md) — A Boolean value that indicates whether the text field is currently in edit mode.
- [clearsOnInsertion](clearsoninsertion.md) — A Boolean value that determines whether inserting text replaces the previous contents.
- [allowsEditingTextAttributes](allowseditingtextattributes.md) — A Boolean value that determines whether the user can edit the attributes of the text in the text field.
- [DidEndEditingReason](didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
- [UITextFieldDidEndEditingReasonKey](didendeditingreasonuserinfokey.md) — A key that indicates the reason for ending editing in a text field.
- [UITextFieldTextDidBeginEditingNotification](textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text field.
- [UITextFieldTextDidChangeNotification](textdidchangenotification.md) — A notification that alerts observers when the text in a text field changes.
- [UITextFieldTextDidEndEditingNotification](textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text field.

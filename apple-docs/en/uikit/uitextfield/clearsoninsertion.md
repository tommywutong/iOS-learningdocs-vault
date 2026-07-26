---
title: clearsOnInsertion
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/clearsoninsertion
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/clearsoninsertion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/clearsoninsertion.json'
content_hash: 'sha256:26bba8a7c7ff206e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# clearsOnInsertion

<sub>Instance Property</sub>

A Boolean value that determines whether inserting text replaces the previous contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var clearsOnInsertion: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). When the value of this property is [true](../../swift/true.md) and the text field is in editing mode, the selection UI is hidden and inserting new text clears the contents of the text field and sets the value of this property back to [false](../../swift/false.md).

## See Also

### Managing the editing behavior

- [editing](isediting.md) — A Boolean value that indicates whether the text field is currently in edit mode.
- [clearsOnBeginEditing](clearsonbeginediting.md) — A Boolean value that determines whether the text field removes old text when editing begins.
- [allowsEditingTextAttributes](allowseditingtextattributes.md) — A Boolean value that determines whether the user can edit the attributes of the text in the text field.
- [DidEndEditingReason](didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
- [UITextFieldDidEndEditingReasonKey](didendeditingreasonuserinfokey.md) — A key that indicates the reason for ending editing in a text field.
- [UITextFieldTextDidBeginEditingNotification](textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text field.
- [UITextFieldTextDidChangeNotification](textdidchangenotification.md) — A notification that alerts observers when the text in a text field changes.
- [UITextFieldTextDidEndEditingNotification](textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text field.

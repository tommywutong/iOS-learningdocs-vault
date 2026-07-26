---
title: textDidEndEditingNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/textdidendeditingnotification
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/textdidendeditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/textdidendeditingnotification.json'
content_hash: 'sha256:38a05a4125ec24bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# textDidEndEditingNotification

<sub>Type Property</sub>

A notification that alerts observers when the editing session ends for a text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let textDidEndEditingNotification: NSNotification.Name
```

## Discussion

The affected text field is stored in the `object` parameter of the notification. The `userInfo` dictionary is not used.

## See Also

### Managing the editing behavior

- [editing](isediting.md) — A Boolean value that indicates whether the text field is currently in edit mode.
- [clearsOnBeginEditing](clearsonbeginediting.md) — A Boolean value that determines whether the text field removes old text when editing begins.
- [clearsOnInsertion](clearsoninsertion.md) — A Boolean value that determines whether inserting text replaces the previous contents.
- [allowsEditingTextAttributes](allowseditingtextattributes.md) — A Boolean value that determines whether the user can edit the attributes of the text in the text field.
- [DidEndEditingReason](didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
- [UITextFieldDidEndEditingReasonKey](didendeditingreasonuserinfokey.md) — A key that indicates the reason for ending editing in a text field.
- [UITextFieldTextDidBeginEditingNotification](textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text field.
- [UITextFieldTextDidChangeNotification](textdidchangenotification.md) — A notification that alerts observers when the text in a text field changes.

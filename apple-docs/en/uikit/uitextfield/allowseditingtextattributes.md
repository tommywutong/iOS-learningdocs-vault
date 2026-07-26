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
doc_path: /documentation/uikit/uitextfield/allowseditingtextattributes
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/allowseditingtextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/allowseditingtextattributes.json'
content_hash: 'sha256:54e964b2f5f3c07a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# allowsEditingTextAttributes

<sub>Instance Property</sub>

A Boolean value that determines whether the user can edit the attributes of the text in the text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsEditingTextAttributes: Bool { get set }
```

## Discussion

If this property is set to [true](../../swift/true.md), the user may edit the style information of the text. In addition, pasting styled text into the text field retains any embedded style information. If [false](../../swift/false.md), the text field prohibits the editing of style information and strips style information from any pasted text. However, you can still set the style information programmatically using the methods of this class.

The default value of this property is [false](../../swift/false.md).

## See Also

### Managing the editing behavior

- [editing](isediting.md) — A Boolean value that indicates whether the text field is currently in edit mode.
- [clearsOnBeginEditing](clearsonbeginediting.md) — A Boolean value that determines whether the text field removes old text when editing begins.
- [clearsOnInsertion](clearsoninsertion.md) — A Boolean value that determines whether inserting text replaces the previous contents.
- [DidEndEditingReason](didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
- [UITextFieldDidEndEditingReasonKey](didendeditingreasonuserinfokey.md) — A key that indicates the reason for ending editing in a text field.
- [UITextFieldTextDidBeginEditingNotification](textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text field.
- [UITextFieldTextDidChangeNotification](textdidchangenotification.md) — A notification that alerts observers when the text in a text field changes.
- [UITextFieldTextDidEndEditingNotification](textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text field.

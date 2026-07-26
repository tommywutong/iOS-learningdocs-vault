---
title: UITextField.DidEndEditingReason
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/didendeditingreason
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/didendeditingreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/didendeditingreason.json'
content_hash: 'sha256:b29e0f20f1cd00da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# UITextField.DidEndEditingReason

<sub>Enumeration</sub>

Constants that indicate the reason for ending editing in a text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum DidEndEditingReason
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextFieldDidEndEditingReasonCommitted](didendeditingreason/committed.md) — The text field changes were accepted by the user.
- [UITextFieldDidEndEditingReasonCancelled](didendeditingreason/cancelled.md) — The text field changes were aborted.

### Initializers

- [init(rawValue:)](<didendeditingreason/init(rawvalue_).md>)

## See Also

### Managing the editing behavior

- [editing](isediting.md) — A Boolean value that indicates whether the text field is currently in edit mode.
- [clearsOnBeginEditing](clearsonbeginediting.md) — A Boolean value that determines whether the text field removes old text when editing begins.
- [clearsOnInsertion](clearsoninsertion.md) — A Boolean value that determines whether inserting text replaces the previous contents.
- [allowsEditingTextAttributes](allowseditingtextattributes.md) — A Boolean value that determines whether the user can edit the attributes of the text in the text field.
- [UITextFieldDidEndEditingReasonKey](didendeditingreasonuserinfokey.md) — A key that indicates the reason for ending editing in a text field.
- [UITextFieldTextDidBeginEditingNotification](textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text field.
- [UITextFieldTextDidChangeNotification](textdidchangenotification.md) — A notification that alerts observers when the text in a text field changes.
- [UITextFieldTextDidEndEditingNotification](textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text field.

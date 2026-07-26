---
title: UIActivityViewController.CollaborationModeRestriction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityviewcontroller/collaborationmoderestriction
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/collaborationmoderestriction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityviewcontroller/collaborationmoderestriction.json'
content_hash: 'sha256:acdb54d4c6c7a72e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityViewController](../uiactivityviewcontroller.md)

# UIActivityViewController.CollaborationModeRestriction

<sub>Class</sub>

An object that disables the sharing mode and optionally displays an alert.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class CollaborationModeRestriction
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md)

## Topics

### Creating a disabled mode

- [- initWithDisabledMode:](<collaborationmoderestriction/init(disabledmode_).md>) — Copies the provided disabled mode.
- [- initWithDisabledMode:alertTitle:alertMessage:](<collaborationmoderestriction/init(disabledmode_alerttitle_alertmessage_).md>) — Creates a disabled mode that displays an alert when someone tries to select that mode.
- [- initWithDisabledMode:alertTitle:alertMessage:alertDismissButtonTitle:](<collaborationmoderestriction/init(disabledmode_alerttitle_alertmessage_alertdismissbuttontitle_).md>) — Creates a disabled mode that displays an alert with a customized dismiss button.
- [- initWithDisabledMode:alertTitle:alertMessage:alertDismissButtonTitle:alertRecoverySuggestionButtonTitle:alertRecoverySuggestionButtonLaunchURL:](<collaborationmoderestriction/init(disabledmode_alerttitle_alertmessage_alertdismissbuttontitle_alertrecoverysuggestionbuttontitle_alertrecoverysuggestionbuttonlaunch_).md>) — Creates a disabled mode that displays an alert with a recovery suggestion.

### Accessing the disabled mode’s properties

- [alertDismissButtonTitle](collaborationmoderestriction/alertdismissbuttontitle.md) — A title for the alert’s dismiss button.
- [alertMessage](collaborationmoderestriction/alertmessage.md) — A message displayed by the alert
- [alertRecoverySuggestionButtonLaunchURL](collaborationmoderestriction/alertrecoverysuggestionbuttonlaunchurl.md) — A launch URL that the system passes to your app when someone taps the recovery suggestion button.
- [alertRecoverySuggestionButtonTitle](collaborationmoderestriction/alertrecoverysuggestionbuttontitle.md) — A title for the alert’s recovery suggestion button.
- [alertTitle](collaborationmoderestriction/alerttitle.md) — A title for the alert that the system displays when someone selects the disabled mode.
- [disabledMode](collaborationmoderestriction/disabledmode.md) — The mode that is disabled.
- [- description](<collaborationmoderestriction/description().md>) — Returns a description of the disabled mode.

### Initializers

- [init(coder:)](<collaborationmoderestriction/init(coder_).md>)
- [init(disabledMode:alertTitle:alertMessage:alertDismissButtonTitle:alertRecoverySuggestionButtonTitle:alertRecoverySuggestionButtonLaunchURL:)](<collaborationmoderestriction/init(disabledmode_alerttitle_alertmessage_alertdismissbuttontitle_alertrecoverysuggestionbuttontitle_alertrecoverysuggestionbuttonlaunchurl_).md>)

## See Also

### Restricting the sharing mode

- [UIActivityCollaborationMode](../uiactivitycollaborationmode.md) — A value that defines how the system shares an item.

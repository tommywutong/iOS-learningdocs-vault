---
title: UISceneClosureConfirmation
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uisceneclosureconfirmation
source_url: 'https://developer.apple.com/documentation/uikit/uisceneclosureconfirmation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneclosureconfirmation.json'
content_hash: 'sha256:45249ed7733fff9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneClosureConfirmation

<sub>Class</sub>

A configuration specifying a confirmation dialog that will be shown before a user action will result in destruction of the scene session and the disconnection of the scene.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UISceneClosureConfirmation
```

## Overview

By default, the confirmation dialog includes a “Close” button (which closes the scene) and a “Cancel” button (which keeps the scene open). You can replace either of these default buttons by providing custom actions. Use a `UIAlertAction` with style `.destructive` to replace the “Close” button, or style `.cancel` to replace the “Cancel” button.

Example:

A property of this type is found on `UIWindowScene`. A scene setting its `closureConfirmation` may look something like

```
let closeAction = UIAlertAction(title:"End meeting for all", style:.destructive, handler: nil)
let cancelAction = UIAlertAction(title:"Stay in meeting", style:.cancel, handler:nil)
let myAction = UIAlertAction(title:"Leave & Assign new host", style:.default) { action in
   // work to do before the window closes
}
var closureConfirmation: UISceneClosureConfirmation =
   UISceneClosureConfirmation(title:"Leave or End meeting?",
                              message:"You are the host. Would you like to end the meeting for all participants?",
                              actions:[closeAction, cancelAction, myAction])

windowScene.closureConfirmation = closureConfirmation
```

With this property set, upon user initiated close, the system will present the closure confirmation dialog.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init(coder:)](<uisceneclosureconfirmation/init(coder_).md>) _(beta)_
- [+ confirmationWithTitle:message:actions:](<uisceneclosureconfirmation/init(title_message_actions_).md>) — Creates a scene closure confirmation with the provided parameters. _(beta)_

## See Also

### Activation and destruction

- [UISceneActivationConditions](uisceneactivationconditions.md) — The set of conditions that define when UIKit activates the current scene.
- [ActivationRequestOptions](uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.

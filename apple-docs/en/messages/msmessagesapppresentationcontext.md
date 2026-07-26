---
title: MSMessagesAppPresentationContext
framework: Messages
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/messages/msmessagesapppresentationcontext
source_url: 'https://developer.apple.com/documentation/messages/msmessagesapppresentationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/messages/msmessagesapppresentationcontext.json'
content_hash: 'sha256:b59b52f0c9f9900b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Messages](../messages.md)

# MSMessagesAppPresentationContext

<sub>Enumeration</sub>

Presentation contexts describing where your iMessage app appears.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum MSMessagesAppPresentationContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Presentation Contexts

- [MSMessagesAppPresentationContextMedia](msmessagesapppresentationcontext/media.md) — A constant that indicates the iMessage app appears inside the Stickers app throughout iOS including in Messages, FaceTime, the emoji keyboard, and Markup.
- [MSMessagesAppPresentationContextMessages](msmessagesapppresentationcontext/messages.md) — A constant that indicates the iMessage app appears in Messages in the list of iMessage apps that appears when you press the plus button.

### Initializers

- [init(rawValue:)](<msmessagesapppresentationcontext/init(rawvalue_).md>)

## See Also

### Working with Presentation Styles and Contexts

- [presentationStyle](msmessagesappviewcontroller/presentationstyle.md) — The extension’s current presentation style.
- [- requestPresentationStyle:](<msmessagesappviewcontroller/requestpresentationstyle(__).md>) — Asks the extension’s user interface to transition to the provided style.
- [- willTransitionToPresentationStyle:](<msmessagesappviewcontroller/willtransition(to_).md>) — Tells the view controller that the extension is about to transition to a new presentation style.
- [- didTransitionToPresentationStyle:](<msmessagesappviewcontroller/didtransition(to_).md>) — Tells the view controller that the extension has transitioned to a new presentation style.
- [MSMessagesAppPresentationStyle](msmessagesapppresentationstyle.md) — Presentation styles that describe your iMessage app’s appearance.
- [presentationContext](msmessagesappviewcontroller/presentationcontext.md) — The context describing where your iMessage app is presented.

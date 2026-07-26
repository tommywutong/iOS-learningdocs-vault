---
title: UNError.Code
framework: User Notifications
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unerror/code
source_url: 'https://developer.apple.com/documentation/usernotifications/unerror/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unerror/code.json'
content_hash: 'sha256:f984b8d212a6004c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNError](../unerror.md)

# UNError.Code

<sub>Enumeration</sub>

Constants that identify notification errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UNErrorCodeNotificationsNotAllowed](code/notificationsnotallowed.md) — Notifications aren’t allowed.
- [UNErrorCodeAttachmentInvalidURL](code/attachmentinvalidurl.md) — The URL for an attachment was invalid.
- [UNErrorCodeAttachmentUnrecognizedType](code/attachmentunrecognizedtype.md) — The file type of an attachment isn’t supported.
- [UNErrorCodeAttachmentInvalidFileSize](code/attachmentinvalidfilesize.md) — An attachment is too large.
- [UNErrorCodeAttachmentNotInDataStore](code/attachmentnotindatastore.md) — The specified attachment isn’t in the system data store.
- [UNErrorCodeAttachmentMoveIntoDataStoreFailed](code/attachmentmoveintodatastorefailed.md) — An error occurred when trying to move an attachment to the system data store.
- [UNErrorCodeAttachmentCorrupt](code/attachmentcorrupt.md) — The file for an attachment is corrupt.
- [UNErrorCodeNotificationInvalidNoDate](code/notificationinvalidnodate.md) — The notification doesn’t have an associated date, but should.
- [UNErrorCodeNotificationInvalidNoContent](code/notificationinvalidnocontent.md) — The notification has no user-facing content, but should.
- [UNErrorCodeContentProvidingInvalid](code/contentprovidinginvalid.md)
- [UNErrorCodeContentProvidingObjectNotAllowed](code/contentprovidingobjectnotallowed.md)

### Enumeration Cases

- [UNErrorCodeBadgeInputInvalid](code/badgeinputinvalid.md)

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Handling errors

- [UNError](../unerror.md) — An object that represents a notification error.
- [UNErrorDomain](../unerrordomain.md) — The error domain for notifications.

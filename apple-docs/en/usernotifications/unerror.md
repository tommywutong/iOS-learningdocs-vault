---
title: UNError
framework: User Notifications
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unerror
source_url: 'https://developer.apple.com/documentation/usernotifications/unerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unerror.json'
content_hash: 'sha256:00c1be38fc4c95e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNError

<sub>Structure</sub>

An object that represents a notification error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UNError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [notificationsNotAllowed](unerror/notificationsnotallowed.md) — Notifications are not allowed.
- [attachmentInvalidURL](unerror/attachmentinvalidurl.md) — The URL for an attachment was invalid.
- [attachmentUnrecognizedType](unerror/attachmentunrecognizedtype.md) — The file type of an attachment is not supported.
- [attachmentInvalidFileSize](unerror/attachmentinvalidfilesize.md) — An attachment is too large.
- [attachmentNotInDataStore](unerror/attachmentnotindatastore.md) — The specified attachment is not in the system data store.
- [attachmentMoveIntoDataStoreFailed](unerror/attachmentmoveintodatastorefailed.md) — An error occurred when trying to move an attachment to the system data store.
- [attachmentCorrupt](unerror/attachmentcorrupt.md) — The file for an attachment is corrupt.
- [notificationInvalidNoDate](unerror/notificationinvalidnodate.md) — The notification does not have an associated date, but should.
- [notificationInvalidNoContent](unerror/notificationinvalidnocontent.md) — The notification has no user-facing content, but should.
- [contentProvidingInvalid](unerror/contentprovidinginvalid.md)
- [contentProvidingObjectNotAllowed](unerror/contentprovidingobjectnotallowed.md)
- [badgeInputInvalid](unerror/badgeinputinvalid.md)

### Error Information

- [errorDomain](unerror/errordomain.md)
- [UNErrorDomain](unerrordomain.md) — The error domain for notifications.
- [Code](unerror/code.md) — Constants that identify notification errors.

## See Also

### Handling errors

- [Code](unerror/code.md) — Constants that identify notification errors.
- [UNErrorDomain](unerrordomain.md) — The error domain for notifications.

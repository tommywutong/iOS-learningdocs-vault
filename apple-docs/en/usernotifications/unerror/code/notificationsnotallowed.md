---
title: UNError.Code.notificationsNotAllowed
framework: User Notifications
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unerror/code/notificationsnotallowed
source_url: 'https://developer.apple.com/documentation/usernotifications/unerror/code/notificationsnotallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unerror/code/notificationsnotallowed.json'
content_hash: 'sha256:5e6a52a36295cd2a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [User Notifications](../../../usernotifications.md) · [UNError](../../unerror.md) · [Code](../code.md)

# UNError.Code.notificationsNotAllowed

<sub>Case</sub>

Notifications aren’t allowed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case notificationsNotAllowed
```

## Discussion

This error occurs when you try to submit a notification request and your app or app extension isn’t authorized to schedule notifications.

## See Also

### Constants

- [UNErrorCodeAttachmentInvalidURL](attachmentinvalidurl.md) — The URL for an attachment was invalid.
- [UNErrorCodeAttachmentUnrecognizedType](attachmentunrecognizedtype.md) — The file type of an attachment isn’t supported.
- [UNErrorCodeAttachmentInvalidFileSize](attachmentinvalidfilesize.md) — An attachment is too large.
- [UNErrorCodeAttachmentNotInDataStore](attachmentnotindatastore.md) — The specified attachment isn’t in the system data store.
- [UNErrorCodeAttachmentMoveIntoDataStoreFailed](attachmentmoveintodatastorefailed.md) — An error occurred when trying to move an attachment to the system data store.
- [UNErrorCodeAttachmentCorrupt](attachmentcorrupt.md) — The file for an attachment is corrupt.
- [UNErrorCodeNotificationInvalidNoDate](notificationinvalidnodate.md) — The notification doesn’t have an associated date, but should.
- [UNErrorCodeNotificationInvalidNoContent](notificationinvalidnocontent.md) — The notification has no user-facing content, but should.
- [UNErrorCodeContentProvidingInvalid](contentprovidinginvalid.md)
- [UNErrorCodeContentProvidingObjectNotAllowed](contentprovidingobjectnotallowed.md)

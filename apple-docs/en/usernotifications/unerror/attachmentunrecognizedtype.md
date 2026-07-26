---
title: attachmentUnrecognizedType
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unerror/attachmentunrecognizedtype
source_url: 'https://developer.apple.com/documentation/usernotifications/unerror/attachmentunrecognizedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unerror/attachmentunrecognizedtype.json'
content_hash: 'sha256:144ee669c507dd1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNError](../unerror.md)

# attachmentUnrecognizedType

<sub>Type Property</sub>

The file type of an attachment is not supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var attachmentUnrecognizedType: UNError.Code { get }
```

## See Also

### Type Properties

- [notificationsNotAllowed](notificationsnotallowed.md) — Notifications are not allowed.
- [attachmentInvalidURL](attachmentinvalidurl.md) — The URL for an attachment was invalid.
- [attachmentInvalidFileSize](attachmentinvalidfilesize.md) — An attachment is too large.
- [attachmentNotInDataStore](attachmentnotindatastore.md) — The specified attachment is not in the system data store.
- [attachmentMoveIntoDataStoreFailed](attachmentmoveintodatastorefailed.md) — An error occurred when trying to move an attachment to the system data store.
- [attachmentCorrupt](attachmentcorrupt.md) — The file for an attachment is corrupt.
- [notificationInvalidNoDate](notificationinvalidnodate.md) — The notification does not have an associated date, but should.
- [notificationInvalidNoContent](notificationinvalidnocontent.md) — The notification has no user-facing content, but should.
- [contentProvidingInvalid](contentprovidinginvalid.md)
- [contentProvidingObjectNotAllowed](contentprovidingobjectnotallowed.md)
- [badgeInputInvalid](badgeinputinvalid.md)

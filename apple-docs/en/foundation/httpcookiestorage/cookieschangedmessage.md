---
title: HTTPCookieStorage.CookiesChangedMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookiestorage/cookieschangedmessage
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/cookieschangedmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/cookieschangedmessage.json'
content_hash: 'sha256:8bf5c5378f441329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# HTTPCookieStorage.CookiesChangedMessage

<sub>Structure</sub>

A message a cookie storage instance sends when its cookies change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CookiesChangedMessage
```

## Overview

Observe this message with the identifier [cookiesChanged](../notificationcenter/messageidentifier/cookieschanged.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [HTTPCookieStorage](../httpcookiestorage.md).

This message interoperates with the notification [NSHTTPCookieManagerCookiesChangedNotification](../nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<cookieschangedmessage/init().md>) — Creates a message that the cookies in a cookie storage instance changed.

## See Also

### Tracking cookie storage changes

- [NSHTTPCookieManagerCookiesChangedNotification](../nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged.md) — A notification posted when the cookies stored in the cookie storage have changed.
- [NSHTTPCookieManagerAcceptPolicyChangedNotification](../nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged.md) — A notification posted when the acceptance policy of the cookie storage has changed. _(deprecated)_

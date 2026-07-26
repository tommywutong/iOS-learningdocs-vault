---
title: cookiesChanged
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/cookieschanged
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/cookieschanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/cookieschanged.json'
content_hash: 'sha256:02dd66591968167f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# cookiesChanged

<sub>Type Property</sub>

An identifier for a message about a cookie storage instance’s cookies changing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var cookiesChanged: NotificationCenter.BaseMessageIdentifier<HTTPCookieStorage.CookiesChangedMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [CookiesChangedMessage](../../httpcookiestorage/cookieschangedmessage.md).

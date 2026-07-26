---
title: sizeLimitExceeded
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/sizelimitexceeded
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/sizelimitexceeded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/sizelimitexceeded.json'
content_hash: 'sha256:592b56fe7a7f2868'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# sizeLimitExceeded

<sub>Type Property</sub>

An identifier for a message about a user defaults database exceeding its maximum size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var sizeLimitExceeded: NotificationCenter.BaseMessageIdentifier<UserDefaults.SizeLimitExceededMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [SizeLimitExceededMessage](../../userdefaults/sizelimitexceededmessage.md).

## See Also

### Identifying defaults messages

- [didChange](didchange-187tw.md) — An identifier for a message about a change in a user defaults setting.

---
title: willResignActive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/willresignactive-9z4xc
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/willresignactive-9z4xc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/willresignactive-9z4xc.json'
content_hash: 'sha256:aa7f96150c6bf36d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# willResignActive

<sub>Type Property</sub>

An identifier for a message about a host app moving from the active to the inactive state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var willResignActive: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.WillResignActiveMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [WillResignActiveMessage](../../nsextensioncontext/willresignactivemessage.md).

## See Also

### Identifying extension messages

- [didBecomeActive](didbecomeactive-79dvm.md) — An identifier for a message about a host app moving from the inactive to the active state.
- [didEnterBackground](didenterbackground-5gdtk.md) — An identifier for a message about a host app beginning to run in the background.
- [willEnterForeground](willenterforeground-p1og.md) — An identifier for a message about a host app preparing to run in the foreground.

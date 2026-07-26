---
title: didEnterBackground
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/didenterbackground-5gdtk
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didenterbackground-5gdtk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/didenterbackground-5gdtk.json'
content_hash: 'sha256:4c7483401ebbb136'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# didEnterBackground

<sub>Type Property</sub>

An identifier for a message about a host app beginning to run in the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var didEnterBackground: NotificationCenter.BaseMessageIdentifier<NSExtensionContext.DidEnterBackgroundMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [DidEnterBackgroundMessage](../../nsextensioncontext/didenterbackgroundmessage.md).

## See Also

### Identifying extension messages

- [didBecomeActive](didbecomeactive-79dvm.md) — An identifier for a message about a host app moving from the inactive to the active state.
- [willResignActive](willresignactive-9z4xc.md) — An identifier for a message about a host app moving from the active to the inactive state.
- [willEnterForeground](willenterforeground-p1og.md) — An identifier for a message about a host app preparing to run in the foreground.

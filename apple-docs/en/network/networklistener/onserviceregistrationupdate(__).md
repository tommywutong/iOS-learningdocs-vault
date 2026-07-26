---
title: 'onServiceRegistrationUpdate(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networklistener/onserviceregistrationupdate(_:)'
source_url: 'https://developer.apple.com/documentation/network/networklistener/onserviceregistrationupdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/onserviceregistrationupdate%28_%3A%29.json'
content_hash: 'sha256:76118471b3eb24f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# onServiceRegistrationUpdate(_:)

<sub>Instance Method</sub>

Set a closure to be called when the listener has added or removed a registered service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult final func onServiceRegistrationUpdate(_ handler: @escaping @isolated(any) @Sendable (NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.ServiceRegistrationChange) -> Void) -> Self
```

## Parameters

- `handler` — A handler to be called when a registered service changes.

## Discussion

The closure may be called multiple times until the listener is cancelled.

The closure inherits the isolation domain of the caller.

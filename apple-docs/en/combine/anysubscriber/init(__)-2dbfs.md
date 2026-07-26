---
title: 'init(_:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/anysubscriber/init(_:)-2dbfs'
source_url: 'https://developer.apple.com/documentation/combine/anysubscriber/init(_:)-2dbfs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/anysubscriber/init%28_%3A%29-2dbfs.json'
content_hash: 'sha256:a0dcffda3ccf40bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [AnySubscriber](../anysubscriber.md)

# init(_:)

<sub>Initializer</sub>

Creates a type-erasing subscriber to wrap an existing subscriber.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ s: S) where Input == S.Input, Failure == S.Failure, S : Subscriber
```

## Parameters

- `s` — The subscriber to type-erase.

## See Also

### Creating a type-erased subscriber

- [init(_:)](<init(__)-3t3eh.md>) — Creates a type-erasing subscriber to wrap an existing subscriber.
- [init(receiveSubscription:receiveValue:receiveCompletion:)](<init(receivesubscription_receivevalue_receivecompletion_).md>) — Creates a type-erasing subscriber that executes the provided closures.

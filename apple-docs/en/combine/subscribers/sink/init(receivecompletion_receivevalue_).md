---
title: 'init(receiveCompletion:receiveValue:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/sink/init(receivecompletion:receivevalue:)'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/sink/init(receivecompletion:receivevalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/sink/init%28receivecompletion%3Areceivevalue%3A%29.json'
content_hash: 'sha256:48e90afd65195316'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Sink](../sink.md)

# init(receiveCompletion:receiveValue:)

<sub>Initializer</sub>

Initializes a sink with the provided closures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(receiveCompletion: @escaping (Subscribers.Completion<Failure>) -> Void, receiveValue: @escaping (Input) -> Void)
```

## Parameters

- `receiveCompletion` — The closure to execute on completion.

- `receiveValue` — The closure to execute on receipt of a value.

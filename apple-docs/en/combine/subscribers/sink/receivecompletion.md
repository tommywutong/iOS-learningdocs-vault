---
title: receiveCompletion
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers/sink/receivecompletion
source_url: 'https://developer.apple.com/documentation/combine/subscribers/sink/receivecompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/sink/receivecompletion.json'
content_hash: 'sha256:14abeebb1b838b31'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Sink](../sink.md)

# receiveCompletion

<sub>Instance Property</sub>

The closure to execute on completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var receiveCompletion: (Subscribers.Completion<Failure>) -> Void { get }
```

## See Also

### Inspecting subscriber properties

- [receiveValue](receivevalue.md) — The closure to execute on receipt of a value.

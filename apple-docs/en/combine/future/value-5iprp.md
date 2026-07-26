---
title: value
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/future/value-5iprp
source_url: 'https://developer.apple.com/documentation/combine/future/value-5iprp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/future/value-5iprp.json'
content_hash: 'sha256:fa4e2ca288c655c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Future](../future.md)

# value

<sub>Instance Property</sub>

The published value of the future or an error, delivered asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var value: Output { get async throws }
```

## Discussion

This property subscribes to the `Future` and delivers the value asynchronously when the `Future` publishes it. If the `Future` terminates with an error, the awaiting caller receives the error instead. Use this property when you want to the `async`-`await` syntax with a `Future` whose [Failure](../publisher/failure.md) type is not [Never](../../swift/never.md).

## See Also

### Accessing the value asynchronously

- [value](value-9iwjz.md) — The published value of the future, delivered asynchronously.

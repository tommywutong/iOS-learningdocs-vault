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
doc_path: /documentation/combine/future/value-9iwjz
source_url: 'https://developer.apple.com/documentation/combine/future/value-9iwjz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/future/value-9iwjz.json'
content_hash: 'sha256:db9dfa1ca73c4fb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Future](../future.md)

# value

<sub>Instance Property</sub>

The published value of the future, delivered asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var value: Output { get async }
```

## Discussion

This property subscribes to the `Future` and delivers the value asynchronously when the `Future` publishes it. Use this property when you want to use the `async`-`await` syntax with a `Future`.

## See Also

### Accessing the value asynchronously

- [value](value-5iprp.md) — The published value of the future or an error, delivered asynchronously.

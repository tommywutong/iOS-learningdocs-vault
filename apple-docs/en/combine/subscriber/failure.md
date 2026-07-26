---
title: Failure
framework: Combine
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscriber/failure
source_url: 'https://developer.apple.com/documentation/combine/subscriber/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscriber/failure.json'
content_hash: 'sha256:28350e5381e1f125'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscriber](../subscriber.md)

# Failure

<sub>Associated Type</sub>

The kind of errors this subscriber might receive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Failure : Error
```

## Discussion

Use `Never` if this `Subscriber` cannot receive errors.

## See Also

### Declaring supporting types

- [Input](input.md) — The kind of values this subscriber receives.

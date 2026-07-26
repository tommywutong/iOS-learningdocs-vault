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
doc_path: /documentation/combine/publisher/failure
source_url: 'https://developer.apple.com/documentation/combine/publisher/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/failure.json'
content_hash: 'sha256:b2c8272e18d01e60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# Failure

<sub>Associated Type</sub>

The kind of errors this publisher might publish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Failure : Error
```

## Discussion

Use `Never` if this `Publisher` does not publish errors.

## See Also

### Declaring supporting types

- [Output](output.md) — The kind of values published by this publisher.

---
title: 'Publishers.BufferingStrategy.customError(_:)'
framework: Combine
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/bufferingstrategy/customerror(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/bufferingstrategy/customerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/bufferingstrategy/customerror%28_%3A%29.json'
content_hash: 'sha256:16ca18b812124faa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [BufferingStrategy](../bufferingstrategy.md)

# Publishers.BufferingStrategy.customError(_:)

<sub>Case</sub>

When the buffer is full, execute the closure to provide a custom error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case customError(() -> Failure)
```

## See Also

### Buffering strategies

- [Publishers.BufferingStrategy.dropNewest](dropnewest.md) — When the buffer is full, discard the newly received element.
- [Publishers.BufferingStrategy.dropOldest](dropoldest.md) — When the buffer is full, discard the oldest element in the buffer.

---
title: Publishers.BufferingStrategy.dropOldest
framework: Combine
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/bufferingstrategy/dropoldest
source_url: 'https://developer.apple.com/documentation/combine/publishers/bufferingstrategy/dropoldest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/bufferingstrategy/dropoldest.json'
content_hash: 'sha256:43919d9f61a9f661'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [BufferingStrategy](../bufferingstrategy.md)

# Publishers.BufferingStrategy.dropOldest

<sub>Case</sub>

When the buffer is full, discard the oldest element in the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case dropOldest
```

## See Also

### Buffering strategies

- [Publishers.BufferingStrategy.dropNewest](dropnewest.md) — When the buffer is full, discard the newly received element.
- [Publishers.BufferingStrategy.customError(_:)](<customerror(__).md>) — When the buffer is full, execute the closure to provide a custom error.

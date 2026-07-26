---
title: Publishers.BufferingStrategy.dropNewest
framework: Combine
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/bufferingstrategy/dropnewest
source_url: 'https://developer.apple.com/documentation/combine/publishers/bufferingstrategy/dropnewest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/bufferingstrategy/dropnewest.json'
content_hash: 'sha256:6b1bd7a9c325a82a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [BufferingStrategy](../bufferingstrategy.md)

# Publishers.BufferingStrategy.dropNewest

<sub>Case</sub>

When the buffer is full, discard the newly received element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case dropNewest
```

## See Also

### Buffering strategies

- [Publishers.BufferingStrategy.dropOldest](dropoldest.md) — When the buffer is full, discard the oldest element in the buffer.
- [Publishers.BufferingStrategy.customError(_:)](<customerror(__).md>) — When the buffer is full, execute the closure to provide a custom error.

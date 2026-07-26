---
title: 'last(where:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/last(where:)'
source_url: 'https://developer.apple.com/documentation/combine/just/last(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/last%28where%3A%29.json'
content_hash: 'sha256:e739a89179d29386'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# last(where:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func last(where predicate: (Output) -> Bool) -> Optional<Output>.Publisher
```

## See Also

### Selecting specific elements

- [first()](<first().md>)
- [first(where:)](<first(where_).md>)
- [last()](<last().md>)
- [output(at:)](<output(at_).md>)
- [output(in:)](<output(in_).md>)

---
title: 'first(where:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/first(where:)'
source_url: 'https://developer.apple.com/documentation/combine/just/first(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/first%28where%3A%29.json'
content_hash: 'sha256:1c8d9137f9ebb8d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# first(where:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func first(where predicate: (Output) -> Bool) -> Optional<Output>.Publisher
```

## See Also

### Selecting specific elements

- [first()](<first().md>)
- [last()](<last().md>)
- [last(where:)](<last(where_).md>)
- [output(at:)](<output(at_).md>)
- [output(in:)](<output(in_).md>)

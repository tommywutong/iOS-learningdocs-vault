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
doc_path: '/documentation/combine/publishers/sequence/first(where:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/first(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/first%28where%3A%29.json'
content_hash: 'sha256:2c67fc1398824d08'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# first(where:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func first(where predicate: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher
```

## See Also

### Selecting specific elements

- [first()](<first().md>)
- [last()](<last().md>)
- [last(where:)](<last(where_).md>)
- [output(at:)](<output(at_)-3r7zo.md>)
- [output(at:)](<output(at_)-9kto7.md>)
- [output(in:)](<output(in_)-6g2zc.md>)
- [output(in:)](<output(in_)-8l6yw.md>)

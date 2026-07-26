---
title: 'output(in:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/output(in:)'
source_url: 'https://developer.apple.com/documentation/combine/just/output(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/output%28in%3A%29.json'
content_hash: 'sha256:89a6734e7a2c3637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# output(in:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func output<R>(in range: R) -> Optional<Output>.Publisher where R : RangeExpression, R.Bound == Int
```

## See Also

### Selecting specific elements

- [first()](<first().md>)
- [first(where:)](<first(where_).md>)
- [last()](<last().md>)
- [last(where:)](<last(where_).md>)
- [output(at:)](<output(at_).md>)

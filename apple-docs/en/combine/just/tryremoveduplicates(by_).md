---
title: 'tryRemoveDuplicates(by:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/tryremoveduplicates(by:)'
source_url: 'https://developer.apple.com/documentation/combine/just/tryremoveduplicates(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/tryremoveduplicates%28by%3A%29.json'
content_hash: 'sha256:f474cbedc2bb3d91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# tryRemoveDuplicates(by:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryRemoveDuplicates(by predicate: (Output, Output) throws -> Bool) -> Result<Output, any Error>.Publisher
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>)
- [compactMap(_:)](<compactmap(__).md>)
- [removeDuplicates()](<removeduplicates().md>)
- [removeDuplicates(by:)](<removeduplicates(by_).md>)
- [replaceEmpty(with:)](<replaceempty(with_).md>)
- [replaceError(with:)](<replaceerror(with_).md>)

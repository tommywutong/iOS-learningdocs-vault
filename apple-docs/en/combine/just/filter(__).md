---
title: 'filter(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/filter(_:)'
source_url: 'https://developer.apple.com/documentation/combine/just/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/filter%28_%3A%29.json'
content_hash: 'sha256:718aaf335d9fc7dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# filter(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(_ isIncluded: (Output) -> Bool) -> Optional<Output>.Publisher
```

## See Also

### Filtering elements

- [compactMap(_:)](<compactmap(__).md>)
- [removeDuplicates()](<removeduplicates().md>)
- [removeDuplicates(by:)](<removeduplicates(by_).md>)
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>)
- [replaceEmpty(with:)](<replaceempty(with_).md>)
- [replaceError(with:)](<replaceerror(with_).md>)

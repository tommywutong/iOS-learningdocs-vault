---
title: 'index(before:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/emptycollection/index(before:)'
source_url: 'https://developer.apple.com/documentation/swift/emptycollection/index(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/emptycollection/index%28before%3A%29.json'
content_hash: 'sha256:e550cfdfbcfee2a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EmptyCollection](../emptycollection.md)

# index(before:)

<sub>Instance Method</sub>

Always traps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(before i: EmptyCollection<Element>.Index) -> EmptyCollection<Element>.Index
```

## Discussion

`EmptyCollection` does not have any element indices, so it is not possible to advance indices.

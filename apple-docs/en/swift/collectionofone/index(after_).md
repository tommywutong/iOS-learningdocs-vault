---
title: 'index(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collectionofone/index(after:)'
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/index(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/index%28after%3A%29.json'
content_hash: 'sha256:8981d5170d956229'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionOfOne](../collectionofone.md)

# index(after:)

<sub>Instance Method</sub>

Returns the position immediately after the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(after i: CollectionOfOne<Element>.Index) -> CollectionOfOne<Element>.Index
```

## Parameters

- `i` — A valid index of the collection. `i` must be `0`.

## Return Value

The index value immediately after `i`.

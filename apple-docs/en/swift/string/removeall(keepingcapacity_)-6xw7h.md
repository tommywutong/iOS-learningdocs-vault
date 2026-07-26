---
title: 'removeAll(keepingCapacity:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/removeall(keepingcapacity:)-6xw7h'
source_url: 'https://developer.apple.com/documentation/swift/string/removeall(keepingcapacity:)-6xw7h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/removeall%28keepingcapacity%3A%29-6xw7h.json'
content_hash: 'sha256:86ab5fa17e2b8413'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# removeAll(keepingCapacity:)

<sub>Instance Method</sub>

Removes all elements from the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeAll(keepingCapacity keepCapacity: Bool = false)
```

## Parameters

- `keepCapacity` — Pass `true` to request that the collection avoid releasing its storage. Retaining the collection’s storage can be a useful optimization when you’re planning to grow the collection again. The default value is `false`.

## Discussion

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

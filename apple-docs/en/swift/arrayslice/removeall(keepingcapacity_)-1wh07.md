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
doc_path: '/documentation/swift/arrayslice/removeall(keepingcapacity:)-1wh07'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/removeall(keepingcapacity:)-1wh07'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/removeall%28keepingcapacity%3A%29-1wh07.json'
content_hash: 'sha256:fdf0fb25407b179b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

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

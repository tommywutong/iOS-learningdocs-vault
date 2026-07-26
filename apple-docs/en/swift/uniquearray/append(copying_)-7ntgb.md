---
title: 'append(copying:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/append(copying:)-7ntgb'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/append(copying:)-7ntgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/append%28copying%3A%29-7ntgb.json'
content_hash: 'sha256:0382a2e802fbc459'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# append(copying:)

<sub>Instance Method</sub>

Copies the elements of a sequence to the end of this array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(copying newElements: some Sequence<Element>)
```

## Parameters

- `newElements` — The new elements to copy into the array.

## Discussion

If the array does not have sufficient capacity to hold enough elements, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate. If the input sequence does not provide a precise estimate of its count, then the array’s storage may need to be resized more than once.

> [!abstract] Complexity
> O(_m_), where _m_ is the length of `newElements`, when amortized over many invocations over the same array.

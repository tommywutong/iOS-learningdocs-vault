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
doc_path: '/documentation/swift/uniquearray/append(copying:)-1qhpn'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/append(copying:)-1qhpn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/append%28copying%3A%29-1qhpn.json'
content_hash: 'sha256:cf0fcc51a57b7981'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# append(copying:)

<sub>Instance Method</sub>

Copies the elements of a buffer to the end of this array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(copying newElements: UnsafeBufferPointer<Element>)
```

## Parameters

- `newElements` — A fully initialized buffer whose contents to copy into the array.

## Discussion

If the array does not have sufficient capacity to hold all items in the source buffer, then this automatically grows the array’s capacity, using a geometric growth rate.

> [!abstract] Complexity
> O(`newElements.count`) when amortized over many invocations on the same array.

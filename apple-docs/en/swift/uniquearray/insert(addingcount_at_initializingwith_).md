---
title: 'insert(addingCount:at:initializingWith:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/insert(addingcount:at:initializingwith:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/insert(addingcount:at:initializingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/insert%28addingcount%3Aat%3Ainitializingwith%3A%29.json'
content_hash: 'sha256:4251f5bb19541493'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# insert(addingCount:at:initializingWith:)

<sub>Instance Method</sub>

Inserts a given number of new items into this array at the specified position, using a callback to directly initialize array storage by populating an output span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert<E>(addingCount newItemCount: Int, at index: Int, initializingWith initializer: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `index` — The position at which to insert the new items. `index` must be a valid index in the array.

## Discussion

Existing elements in the array’s storage are moved towards the back as needed to make room for the new items.

If the array does not have sufficient capacity to hold the new elements, then this operation reallocates storage to extend its capacity, using a geometric growth rate.

```swift
var buffer = UniqueArray<Int>()
buffer.append([-999, 999])
var i = 0
buffer.insert(capacity: 3, at: 1) { target in
  while !target.isFull {
    target.append(i)
    i += 1
  }
}
// `buffer` now contains [-999, 0, 1, 2, 999]
```

> [!abstract] Complexity
> O(`self.count` + `count`)

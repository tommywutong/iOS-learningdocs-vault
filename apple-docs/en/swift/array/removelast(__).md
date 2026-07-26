---
title: 'removeLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/removelast(_:)'
source_url: 'https://developer.apple.com/documentation/swift/array/removelast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/removelast%28_%3A%29.json'
content_hash: 'sha256:4960fd111c6e1444'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# removeLast(_:)

<sub>Instance Method</sub>

Removes the specified number of elements from the end of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeLast(_ k: Int)
```

## Parameters

- `k` — The number of elements to remove from the collection. `k` must be greater than or equal to zero and must not exceed the number of elements in the collection.

## Discussion

Attempting to remove more elements than exist in the collection triggers a runtime error.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> [!abstract] Complexity
> O(_k_), where _k_ is the specified number of elements.

## See Also

### Removing Elements

- [remove(at:)](<remove(at_).md>) — Removes and returns the element at the specified position.
- [removeFirst()](<removefirst().md>) — Removes and returns the first element of the collection.
- [removeFirst(_:)](<removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removeLast()](<removelast().md>) — Removes and returns the last element of the collection.
- [removeSubrange(_:)](<removesubrange(__)-8may1.md>) — Removes the elements in the specified subrange from the collection.
- [removeSubrange(_:)](<removesubrange(__)-9twou.md>) — Removes the elements in the specified subrange from the collection.
- [removeAll(where:)](<removeall(where_)-5k61r.md>) — Removes all the elements that satisfy the given predicate.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all elements from the array.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.

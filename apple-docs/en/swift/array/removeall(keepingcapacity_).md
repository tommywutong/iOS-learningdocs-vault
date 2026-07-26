---
title: 'removeAll(keepingCapacity:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/removeall(keepingcapacity:)'
source_url: 'https://developer.apple.com/documentation/swift/array/removeall(keepingcapacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/removeall%28keepingcapacity%3A%29.json'
content_hash: 'sha256:94ea57acdc7a9a78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# removeAll(keepingCapacity:)

<sub>Instance Method</sub>

Removes all elements from the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeAll(keepingCapacity keepCapacity: Bool = false)
```

## Parameters

- `keepCapacity` — Pass `true` to keep the existing capacity of the array after removing its elements. The default value is `false`.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the array.

## See Also

### Removing Elements

- [remove(at:)](<remove(at_).md>) — Removes and returns the element at the specified position.
- [removeFirst()](<removefirst().md>) — Removes and returns the first element of the collection.
- [removeFirst(_:)](<removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removeLast()](<removelast().md>) — Removes and returns the last element of the collection.
- [removeLast(_:)](<removelast(__).md>) — Removes the specified number of elements from the end of the collection.
- [removeSubrange(_:)](<removesubrange(__)-8may1.md>) — Removes the elements in the specified subrange from the collection.
- [removeSubrange(_:)](<removesubrange(__)-9twou.md>) — Removes the elements in the specified subrange from the collection.
- [removeAll(where:)](<removeall(where_)-5k61r.md>) — Removes all the elements that satisfy the given predicate.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.

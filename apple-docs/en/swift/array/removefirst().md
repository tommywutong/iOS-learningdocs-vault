---
title: removeFirst()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/removefirst()
source_url: 'https://developer.apple.com/documentation/swift/array/removefirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/removefirst%28%29.json'
content_hash: 'sha256:5856a9697f993882'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# removeFirst()

<sub>Instance Method</sub>

Removes and returns the first element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeFirst() -> Self.Element
```

## Return Value

The removed element.

## Discussion

The collection must not be empty.

```swift
var bugs = ["Aphid", "Bumblebee", "Cicada", "Damselfly", "Earwig"]
bugs.removeFirst()
print(bugs)
// Prints "["Bumblebee", "Cicada", "Damselfly", "Earwig"]"
```

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

## See Also

### Removing Elements

- [remove(at:)](<remove(at_).md>) — Removes and returns the element at the specified position.
- [removeFirst(_:)](<removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removeLast()](<removelast().md>) — Removes and returns the last element of the collection.
- [removeLast(_:)](<removelast(__).md>) — Removes the specified number of elements from the end of the collection.
- [removeSubrange(_:)](<removesubrange(__)-8may1.md>) — Removes the elements in the specified subrange from the collection.
- [removeSubrange(_:)](<removesubrange(__)-9twou.md>) — Removes the elements in the specified subrange from the collection.
- [removeAll(where:)](<removeall(where_)-5k61r.md>) — Removes all the elements that satisfy the given predicate.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all elements from the array.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.

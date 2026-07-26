---
title: 'removeSubrange(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/removesubrange(_:)-9twou'
source_url: 'https://developer.apple.com/documentation/swift/array/removesubrange(_:)-9twou'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/removesubrange%28_%3A%29-9twou.json'
content_hash: 'sha256:3350b505bb33c262'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# removeSubrange(_:)

<sub>Instance Method</sub>

Removes the elements in the specified subrange from the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeSubrange<R>(_ bounds: R) where R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `bounds` — The range of the collection to be removed. The bounds of the range must be valid indices of the collection.

## Discussion

All the elements following the specified position are moved to close the gap. This example removes three elements from the middle of an array of measurements.

```swift
var measurements = [1.2, 1.5, 2.9, 1.2, 1.5]
measurements.removeSubrange(1..<4)
print(measurements)
// Prints "[1.2, 1.5]"
```

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

## See Also

### Removing Elements

- [remove(at:)](<remove(at_).md>) — Removes and returns the element at the specified position.
- [removeFirst()](<removefirst().md>) — Removes and returns the first element of the collection.
- [removeFirst(_:)](<removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removeLast()](<removelast().md>) — Removes and returns the last element of the collection.
- [removeLast(_:)](<removelast(__).md>) — Removes the specified number of elements from the end of the collection.
- [removeSubrange(_:)](<removesubrange(__)-8may1.md>) — Removes the elements in the specified subrange from the collection.
- [removeAll(where:)](<removeall(where_)-5k61r.md>) — Removes all the elements that satisfy the given predicate.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all elements from the array.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.

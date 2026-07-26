---
title: 'dropLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/droplast(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/droplast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/droplast%28_%3A%29.json'
content_hash: 'sha256:8983efc9f5df01ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# dropLast(_:)

<sub>Instance Method</sub>

Returns a subsequence containing all but the specified number of final elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropLast(_ k: Int) -> Self.SubSequence
```

## Parameters

- `k` — The number of elements to drop off the end of the collection. `k` must be greater than or equal to zero.

## Return Value

A subsequence that leaves off `k` elements from the end.

## Discussion

If the number of elements to drop exceeds the number of elements in the collection, the result is an empty subsequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the number of elements to drop.

## See Also

### Removing Substrings

- [remove(at:)](<remove(at_).md>) — Removes and returns the character at the specified position.
- [remove(at:)](<remove(at_)-5g0wm.md>) — Removes and returns the element at the specified position.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Replaces this string with the empty string.
- [removeAll(where:)](<removeall(where_).md>) — Removes all the elements that satisfy the given predicate.
- [removeFirst()](<removefirst().md>) — Removes and returns the first element of the collection.
- [removeFirst(_:)](<removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removeLast()](<removelast().md>) — Removes and returns the last element of the collection.
- [removeLast(_:)](<removelast(__).md>) — Removes the specified number of elements from the end of the collection.
- [removeSubrange(_:)](<removesubrange(__).md>) — Removes the characters in the given range.
- [removeSubrange(_:)](<removesubrange(__)-8maxn.md>) — Removes the elements in the specified subrange from the collection.
- [removeSubrange(_:)](<removesubrange(__)-9twng.md>) — Removes the elements in the specified subrange from the collection.
- [drop(while:)](<drop(while_).md>) — Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Returns a subsequence containing all but the given number of initial elements.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.

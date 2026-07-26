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
doc_path: /documentation/swift/string/removefirst()
source_url: 'https://developer.apple.com/documentation/swift/string/removefirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/removefirst%28%29.json'
content_hash: 'sha256:a7cd8a024e9ca08e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

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

### Removing Substrings

- [remove(at:)](<remove(at_).md>) — Removes and returns the character at the specified position.
- [remove(at:)](<remove(at_)-5g0wm.md>) — Removes and returns the element at the specified position.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Replaces this string with the empty string.
- [removeAll(where:)](<removeall(where_).md>) — Removes all the elements that satisfy the given predicate.
- [removeFirst(_:)](<removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removeLast()](<removelast().md>) — Removes and returns the last element of the collection.
- [removeLast(_:)](<removelast(__).md>) — Removes the specified number of elements from the end of the collection.
- [removeSubrange(_:)](<removesubrange(__).md>) — Removes the characters in the given range.
- [removeSubrange(_:)](<removesubrange(__)-8maxn.md>) — Removes the elements in the specified subrange from the collection.
- [removeSubrange(_:)](<removesubrange(__)-9twng.md>) — Removes the elements in the specified subrange from the collection.
- [drop(while:)](<drop(while_).md>) — Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Returns a subsequence containing all but the given number of initial elements.
- [dropLast(_:)](<droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.

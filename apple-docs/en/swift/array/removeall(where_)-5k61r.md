---
title: 'removeAll(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/removeall(where:)-5k61r'
source_url: 'https://developer.apple.com/documentation/swift/array/removeall(where:)-5k61r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/removeall%28where%3A%29-5k61r.json'
content_hash: 'sha256:80775904f7525f51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# removeAll(where:)

<sub>Instance Method</sub>

Removes all the elements that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeAll(where shouldBeRemoved: (Self.Element) throws -> Bool) rethrows
```

## Parameters

- `shouldBeRemoved` — A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element should be removed from the collection.

## Discussion

Use this method to remove every element in a collection that meets particular criteria. The order of the remaining elements is preserved. This example removes all the vowels from a string:

```swift
var phrase = "The rain in Spain stays mainly in the plain."

let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
phrase.removeAll(where: { vowels.contains($0) })
// phrase == "Th rn n Spn stys mnly n th pln."
```

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
- [removeSubrange(_:)](<removesubrange(__)-9twou.md>) — Removes the elements in the specified subrange from the collection.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all elements from the array.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.

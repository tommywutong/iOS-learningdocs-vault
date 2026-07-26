---
title: 'firstIndex(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/firstindex(where:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/firstindex(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/firstindex%28where%3A%29.json'
content_hash: 'sha256:12442b353f8e91f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# firstIndex(where:)

<sub>Instance Method</sub>

Returns the first index in which an element of the collection satisfies the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstIndex(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Index?
```

## Parameters

- `predicate` — A closure that takes an element as its argument and returns a Boolean value that indicates whether the passed element represents a match.

## Return Value

The index of the first element for which `predicate` returns `true`. If no elements in the collection satisfy the given predicate, returns `nil`.

## Discussion

You can use the predicate to find an element of a type that doesn’t conform to the `Equatable` protocol or to find an element that matches particular criteria. Here’s an example that finds a student name that begins with the letter “A”:

```swift
let students = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
if let i = students.firstIndex(where: { $0.hasPrefix("A") }) {
    print("\(students[i]) starts with 'A'!")
}
// Prints "Abena starts with 'A'!"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

## See Also

### Finding Elements

- [contains(where:)](<contains(where_).md>) — Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.

---
title: sorted()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/sorted()
source_url: 'https://developer.apple.com/documentation/swift/array/sorted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/sorted%28%29.json'
content_hash: 'sha256:f2247c596ccc18ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# sorted()

<sub>Instance Method</sub>

Returns the elements of the sequence, sorted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sorted() -> [Self.Element]
```

## Return Value

A sorted array of the sequence’s elements.

## Discussion

You can sort any sequence of elements that conform to the `Comparable` protocol by calling this method. Elements are sorted in ascending order.

Here’s an example of sorting a list of students’ names. Strings in Swift conform to the `Comparable` protocol, so the names are sorted in ascending order according to the less-than operator (`<`).

```swift
let students: Set = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
let sortedStudents = students.sorted()
print(sortedStudents)
// Prints "["Abena", "Akosua", "Kofi", "Kweku", "Peter"]"
```

To sort the elements of your sequence in descending order, pass the greater-than operator (`>`) to the `sorted(by:)` method.

```swift
let descendingStudents = students.sorted(by: >)
print(descendingStudents)
// Prints "["Peter", "Kweku", "Kofi", "Akosua", "Abena"]"
```

The sorting algorithm is guaranteed to be stable. A stable sort preserves the relative order of elements that compare as equal.

> [!abstract] Complexity
> O(_n_ log _n_), where _n_ is the length of the sequence.

## See Also

### Reordering an Array’s Elements

- [sort()](<sort().md>) — Sorts the collection in place.
- [sort(by:)](<sort(by_).md>) — Sorts the collection in place, using the given predicate as the comparison between elements.
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [reverse()](<reverse().md>) — Reverses the elements of the collection in place.
- [reversed()](<reversed().md>) — Returns a view presenting the elements of the collection in reverse order.
- [shuffle()](<shuffle().md>) — Shuffles the collection in place.
- [shuffle(using:)](<shuffle(using_).md>) — Shuffles the collection in place, using the given generator as a source for randomness.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [partition(by:)](<partition(by_)-90po8.md>) — Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [swapAt(_:_:)](<swapat(____).md>) — Exchanges the values at the specified indices of the collection.

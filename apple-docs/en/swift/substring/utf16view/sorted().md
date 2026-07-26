---
title: sorted()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/utf16view/sorted()
source_url: 'https://developer.apple.com/documentation/swift/substring/utf16view/sorted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/utf16view/sorted%28%29.json'
content_hash: 'sha256:a5895633b05f9205'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UTF16View](../utf16view.md)

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

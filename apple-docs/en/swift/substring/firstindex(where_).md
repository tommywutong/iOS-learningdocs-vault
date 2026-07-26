---
title: 'firstIndex(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/firstindex(where:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/firstindex(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/firstindex%28where%3A%29.json'
content_hash: 'sha256:371afc84c54c8c6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

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

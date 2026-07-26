---
title: 'sorted(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/sorted(by:)'
source_url: 'https://developer.apple.com/documentation/swift/array/sorted(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/sorted%28by%3A%29.json'
content_hash: 'sha256:5bc3c45aa83c9b68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# sorted(by:)

<sub>Instance Method</sub>

Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sorted(by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]
```

## Parameters

- `areInIncreasingOrder` — A predicate that returns `true` if its first argument should be ordered before its second argument; otherwise, `false`.

## Return Value

A sorted array of the sequence’s elements.

## Discussion

When you want to sort a sequence of elements that don’t conform to the `Comparable` protocol, pass a predicate to this method that returns `true` when the first element should be ordered before the second. The elements of the resulting array are ordered according to the given predicate.

In the following example, the predicate provides an ordering for an array of a custom `HTTPResponse` type. The predicate orders errors before successes and sorts the error responses by their error code.

```swift
enum HTTPResponse {
    case ok
    case error(Int)
}

let responses: [HTTPResponse] = [.error(500), .ok, .ok, .error(404), .error(403)]
let sortedResponses = responses.sorted {
    switch ($0, $1) {
    // Order errors by code
    case let (.error(aCode), .error(bCode)):
        return aCode < bCode

    // All successes are equivalent, so none is before any other
    case (.ok, .ok): return false

    // Order errors before successes
    case (.error, .ok): return true
    case (.ok, .error): return false
    }
}
print(sortedResponses)
// Prints "[.error(403), .error(404), .error(500), .ok, .ok]"
```

You also use this method to sort elements that conform to the `Comparable` protocol in descending order. To sort your sequence in descending order, pass the greater-than operator (`>`) as the `areInIncreasingOrder` parameter.

```swift
let students: Set = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
let descendingStudents = students.sorted(by: >)
print(descendingStudents)
// Prints "["Peter", "Kweku", "Kofi", "Akosua", "Abena"]"
```

Calling the related `sorted()` method is equivalent to calling this method and passing the less-than operator (`<`) as the predicate.

```swift
print(students.sorted())
// Prints "["Abena", "Akosua", "Kofi", "Kweku", "Peter"]"
print(students.sorted(by: <))
// Prints "["Abena", "Akosua", "Kofi", "Kweku", "Peter"]"
```

The predicate must be a _strict weak ordering_ over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)
- If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)
- Two elements are _incomparable_ if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

The sorting algorithm is guaranteed to be stable. A stable sort preserves the relative order of elements for which `areInIncreasingOrder` does not establish an order.

> [!abstract] Complexity
> O(_n_ log _n_), where _n_ is the length of the sequence.

## See Also

### Reordering an Array’s Elements

- [sort()](<sort().md>) — Sorts the collection in place.
- [sort(by:)](<sort(by_).md>) — Sorts the collection in place, using the given predicate as the comparison between elements.
- [sorted()](<sorted().md>) — Returns the elements of the sequence, sorted.
- [reverse()](<reverse().md>) — Reverses the elements of the collection in place.
- [reversed()](<reversed().md>) — Returns a view presenting the elements of the collection in reverse order.
- [shuffle()](<shuffle().md>) — Shuffles the collection in place.
- [shuffle(using:)](<shuffle(using_).md>) — Shuffles the collection in place, using the given generator as a source for randomness.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [partition(by:)](<partition(by_)-90po8.md>) — Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [swapAt(_:_:)](<swapat(____).md>) — Exchanges the values at the specified indices of the collection.

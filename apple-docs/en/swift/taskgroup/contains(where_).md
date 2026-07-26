---
title: 'contains(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskgroup/contains(where:)'
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/contains(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/contains%28where%3A%29.json'
content_hash: 'sha256:9b0b04f490e08a97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# contains(where:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(where predicate: (Self.Element) async throws -> Bool) async rethrows -> Bool
```

## Parameters

- `predicate` — A closure that takes an element of the asynchronous sequence as its argument and returns a Boolean value that indicates whether the passed element represents a match.

## Return Value

`true` if the sequence contains an element that satisfies predicate; otherwise, `false`.

## Discussion

You can use the predicate to check for an element of a type that doesn’t conform to the `Equatable` protocol, or to find an element that satisfies a general condition.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `contains(where:)` method checks to see whether the sequence produces a value divisible by `3`:

```swift
let containsDivisibleByThree = await Counter(howHigh: 10)
    .contains { $0 % 3 == 0 }
print(containsDivisibleByThree)
// Prints "true"
```

The predicate executes each time the asynchronous sequence produces an element, until either the predicate finds a match or the sequence ends.

## See Also

### Accessing an Asynchronous Sequence of Results

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [compactMap(_:)](<compactmap(__)-944od.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<compactmap(__)-7mgj1.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [contains(_:)](<contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [drop(while:)](<drop(while_).md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [filter(_:)](<filter(__).md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [flatMap(_:)](<flatmap(__)-vhi3.md>) — Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [map(_:)](<map(__)-58nsr.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [map(_:)](<map(__)-4a4kq.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [max()](<max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [min()](<min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.

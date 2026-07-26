---
title: 'prefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskgroup/prefix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/prefix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/prefix%28_%3A%29.json'
content_hash: 'sha256:bd35ece7d5b52262'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# prefix(_:)

<sub>Instance Method</sub>

Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(_ count: Int) -> AsyncPrefixSequence<Self>
```

## Parameters

- `count` — The maximum number of elements to return. The value of `count` must be greater than or equal to zero.

## Return Value

An asynchronous sequence starting at the beginning of the base sequence with at most `count` elements.

## Discussion

Use `prefix(_:)` to reduce the number of elements produced by the asynchronous sequence.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `prefix(_:)` method causes the modified sequence to pass through the first six values, then end.

```swift
for await number in Counter(howHigh: 10).prefix(6) {
    print(number, terminator: " ")
}
// Prints "1 2 3 4 5 6 "
```

If the count passed to `prefix(_:)` exceeds the number of elements in the base sequence, the result contains all of the elements in the sequence.

## See Also

### Accessing an Asynchronous Sequence of Results

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [compactMap(_:)](<compactmap(__)-944od.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<compactmap(__)-7mgj1.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [contains(_:)](<contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [drop(while:)](<drop(while_).md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [filter(_:)](<filter(__).md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [flatMap(_:)](<flatmap(__)-vhi3.md>) — Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [map(_:)](<map(__)-58nsr.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [map(_:)](<map(__)-4a4kq.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [max()](<max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.

---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingtaskgroup/map(_:)-58nrv'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/map(_:)-58nrv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/map%28_%3A%29-58nrv.json'
content_hash: 'sha256:762df8999df2a508'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# map(_:)

<sub>Instance Method</sub>

Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func map<Transformed>(_ transform: @escaping @Sendable (Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>
```

## Parameters

- `transform` — A mapping closure. `transform` accepts an element of this sequence as its parameter and returns a transformed value of the same or of a different type. `transform` can also throw an error, which ends the transformed sequence.

## Return Value

An asynchronous sequence that contains, in order, the elements produced by the `transform` closure.

## Discussion

Use the `map(_:)` method to transform every element received from a base asynchronous sequence. Typically, you use this to transform from one type of element to another.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `5`. The closure provided to the `map(_:)` method takes each `Int` and looks up a corresponding `String` from a `romanNumeralDict` dictionary. This means the outer `for await in` loop iterates over `String` instances instead of the underlying `Int` values that `Counter` produces. Also, the dictionary doesn’t provide a key for `4`, and the closure throws an error for any key it can’t look up, so receiving this value from `Counter` ends the modified sequence with an error.

```swift
let romanNumeralDict: [Int: String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]

do {
    let stream = Counter(howHigh: 5)
        .map { (value) throws -> String in
            guard let roman = romanNumeralDict[value] else {
                throw MyError()
            }
            return roman
        }
    for try await numeral in stream {
        print(numeral, terminator: " ")
    }
} catch {
    print("Error: \(error)")
}
// Prints "I II III Error: MyError() "
```

## See Also

### Accessing an Asynchronous Sequence of Results

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [compactMap(_:)](<compactmap(__)-944nh.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<compactmap(__)-7mgi5.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [contains(_:)](<contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [drop(while:)](<drop(while_).md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [filter(_:)](<filter(__).md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [map(_:)](<map(__)-4a4ju.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [max()](<max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [min()](<min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.

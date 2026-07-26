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
doc_path: '/documentation/swift/asyncstream/map(_:)-58nsf'
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/map(_:)-58nsf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/map%28_%3A%29-58nsf.json'
content_hash: 'sha256:2197dcce99fc2e34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncStream](../asyncstream.md)

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

### Transforming a Sequence

- [map(_:)](<map(__)-4a4la.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [compactMap(_:)](<compactmap(__)-7mgjd.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<compactmap(__)-944op.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [flatMap(_:)](<flatmap(__)-vhhr.md>) — Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.

---
title: 'tryMap(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/trymap(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/trymap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/trymap%28_%3A%29.json'
content_hash: 'sha256:1247efca0f41d6e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryMap(_:)

<sub>Instance Method</sub>

Transforms all elements from the upstream publisher with a provided error-throwing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryMap<T>(_ transform: @escaping (Self.Output) throws -> T) -> Publishers.TryMap<Self, T>
```

## Parameters

- `transform` — A closure that takes one element as its parameter and returns a new element. If the closure throws an error, the publisher fails with the thrown error.

## Return Value

A publisher that uses the provided closure to map elements from the upstream publisher to new elements that it then publishes.

## Discussion

Combine’s [tryMap(_:)](<trymap(__).md>) operator performs a function similar to that of [map(_:)](<../../swift/sequence/map(__).md>) in the Swift standard library: it uses a closure to transform each element it receives from the upstream publisher. You use [tryMap(_:)](<trymap(__).md>) to transform from one kind of element to another, and to terminate publishing when the map’s closure throws an error.

The following example uses an array of numbers as the source for a collection based publisher. A [tryMap(_:)](<trymap(__).md>) operator consumes each integer from the publisher and uses a dictionary to transform it from its Arabic numeral to a Roman equivalent, as a [String](../../swift/string.md). If the [tryMap(_:)](<trymap(__).md>)’s closure fails to look up a Roman numeral, it throws an error. The [tryMap(_:)](<trymap(__).md>) operator catches this error and terminates publishing, sending a [Subscribers.Completion.failure(_:)](<../subscribers/completion/failure(__).md>) that wraps the error.

```swift
struct ParseError: Error {}
func romanNumeral(from:Int) throws -> String {
    let romanNumeralDict: [Int : String] =
        [1:"I", 2:"II", 3:"III", 4:"IV", 5:"V"]
    guard let numeral = romanNumeralDict[from] else {
        throw ParseError()
    }
    return numeral
}
let numbers = [5, 4, 3, 2, 1, 0]
cancellable = numbers.publisher
    .tryMap { try romanNumeral(from: $0) }
    .sink(
        receiveCompletion: { print ("completion: \($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "V IV III II I completion: failure(ParseError())"
```

If your closure doesn’t throw, use [map(_:)](<map(__)-99evh.md>) instead.

## See Also

### Mapping elements

- [map(_:)](<map(__)-99evh.md>) — Transforms all elements from the upstream publisher with a provided closure.
- [mapError(_:)](<maperror(__).md>) — Converts any failure from the upstream publisher into a new error.
- [replaceNil(with:)](<replacenil(with_).md>) — Replaces nil elements in the stream with the provided element.
- [scan(_:_:)](<scan(____).md>) — Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [tryScan(_:_:)](<tryscan(____).md>) — Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [setFailureType(to:)](<setfailuretype(to_).md>) — Changes the failure type declared by the upstream publisher.

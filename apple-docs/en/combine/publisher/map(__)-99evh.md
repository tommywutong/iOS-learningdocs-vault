---
title: 'map(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/map(_:)-99evh'
source_url: 'https://developer.apple.com/documentation/combine/publisher/map(_:)-99evh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/map%28_%3A%29-99evh.json'
content_hash: 'sha256:0f3e2465a42c55a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# map(_:)

<sub>Instance Method</sub>

Transforms all elements from the upstream publisher with a provided closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<T>(_ transform: @escaping (Self.Output) -> T) -> Publishers.Map<Self, T>
```

## Parameters

- `transform` — A closure that takes one element as its parameter and returns a new element.

## Return Value

A publisher that uses the provided closure to map elements from the upstream publisher to new elements that it then publishes.

## Discussion

Combine’s [map(_:)](<map(__)-99evh.md>) operator performs a function similar to that of [map(_:)](<../../swift/sequence/map(__).md>) in the Swift standard library: it uses a closure to transform each element it receives from the upstream publisher. You use [map(_:)](<map(__)-99evh.md>) to transform from one kind of element to another.

The following example uses an array of numbers as the source for a collection based publisher. A [map(_:)](<map(__)-99evh.md>) operator consumes each integer from the publisher and uses a dictionary to transform it from its Arabic numeral to a Roman equivalent, as a [String](../../swift/string.md). If the [map(_:)](<map(__)-99evh.md>)’s closure fails to look up a Roman numeral, it returns the string `(unknown)`.

```swift
let numbers = [5, 4, 3, 2, 1, 0]
let romanNumeralDict: [Int : String] =
   [1:"I", 2:"II", 3:"III", 4:"IV", 5:"V"]
cancellable = numbers.publisher
    .map { romanNumeralDict[$0] ?? "(unknown)" }
    .sink { print("\($0)", terminator: " ") }

// Prints: "V IV III II I (unknown)"
```

If your closure can throw an error, use Combine’s [tryMap(_:)](<trymap(__).md>) operator instead.

## See Also

### Mapping elements

- [tryMap(_:)](<trymap(__).md>) — Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [mapError(_:)](<maperror(__).md>) — Converts any failure from the upstream publisher into a new error.
- [replaceNil(with:)](<replacenil(with_).md>) — Replaces nil elements in the stream with the provided element.
- [scan(_:_:)](<scan(____).md>) — Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [tryScan(_:_:)](<tryscan(____).md>) — Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [setFailureType(to:)](<setfailuretype(to_).md>) — Changes the failure type declared by the upstream publisher.

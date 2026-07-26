---
title: 'scan(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/scan(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/scan(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/scan%28_%3A_%3A%29.json'
content_hash: 'sha256:347cbeb03ef554b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# scan(_:_:)

<sub>Instance Method</sub>

Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scan<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Self.Output) -> T) -> Publishers.Scan<Self, T>
```

## Parameters

- `initialResult` — The previous result returned by the `nextPartialResult` closure.

- `nextPartialResult` — A closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

## Return Value

A publisher that transforms elements by applying a closure that receives its previous return value and the next element from the upstream publisher.

## Discussion

Use [scan(_:_:)](<scan(____).md>) to accumulate all previously-published values into a single value, which you then combine with each newly-published value.

The following example logs a running total of all values received from the sequence publisher.

```swift
let range = (0...5)
cancellable = range.publisher
    .scan(0) { return $0 + $1 }
    .sink { print ("\($0)", terminator: " ") }
 // Prints: "0 1 3 6 10 15 ".
```

## See Also

### Mapping elements

- [map(_:)](<map(__)-99evh.md>) — Transforms all elements from the upstream publisher with a provided closure.
- [tryMap(_:)](<trymap(__).md>) — Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [mapError(_:)](<maperror(__).md>) — Converts any failure from the upstream publisher into a new error.
- [replaceNil(with:)](<replacenil(with_).md>) — Replaces nil elements in the stream with the provided element.
- [tryScan(_:_:)](<tryscan(____).md>) — Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [setFailureType(to:)](<setfailuretype(to_).md>) — Changes the failure type declared by the upstream publisher.

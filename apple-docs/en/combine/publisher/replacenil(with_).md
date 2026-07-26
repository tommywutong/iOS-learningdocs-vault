---
title: 'replaceNil(with:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/replacenil(with:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/replacenil(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/replacenil%28with%3A%29.json'
content_hash: 'sha256:211c34ebf95ac84f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# replaceNil(with:)

<sub>Instance Method</sub>

Replaces nil elements in the stream with the provided element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceNil<T>(with output: T) -> Publishers.Map<Self, T> where Self.Output == T?
```

## Parameters

- `output` — The element to use when replacing `nil`.

## Return Value

A publisher that replaces `nil` elements from the upstream publisher with the provided element.

## Discussion

The [replaceNil(with:)](<replacenil(with_).md>) operator enables replacement of `nil` values in a stream with a substitute value. In the example below, a collection publisher contains a nil value. The [replaceNil(with:)](<replacenil(with_).md>) operator replaces this with `0.0`.

```swift
let numbers: [Double?] = [1.0, 2.0, nil, 3.0]
numbers.publisher
    .replaceNil(with: 0.0)
    .sink { print("\($0)", terminator: " ") }

// Prints: "Optional(1.0) Optional(2.0) Optional(0.0) Optional(3.0)"
```

## See Also

### Mapping elements

- [map(_:)](<map(__)-99evh.md>) — Transforms all elements from the upstream publisher with a provided closure.
- [tryMap(_:)](<trymap(__).md>) — Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [mapError(_:)](<maperror(__).md>) — Converts any failure from the upstream publisher into a new error.
- [scan(_:_:)](<scan(____).md>) — Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [tryScan(_:_:)](<tryscan(____).md>) — Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [setFailureType(to:)](<setfailuretype(to_).md>) — Changes the failure type declared by the upstream publisher.

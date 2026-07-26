---
title: 'setFailureType(to:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/setfailuretype(to:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/setfailuretype(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/setfailuretype%28to%3A%29.json'
content_hash: 'sha256:eae4834c99a9d2f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# setFailureType(to:)

<sub>Instance Method</sub>

Changes the failure type declared by the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setFailureType<E>(to failureType: E.Type) -> Publishers.SetFailureType<Self, E> where E : Error
```

## Parameters

- `failureType` — The `Failure` type presented by this publisher.

## Return Value

A publisher that appears to send the specified failure type.

## Discussion

Use [setFailureType(to:)](<setfailuretype(to_).md>) when you need set the error type of a publisher that cannot fail.

Conversely, if the upstream can fail, you would use [mapError(_:)](<maperror(__).md>) to provide instructions on converting the error types to needed by the downstream publisher’s inputs.

The following example has two publishers with mismatched error types: `pub1`’s error type is [Never](../../swift/never.md), and `pub2`’s error type is [Error](../../swift/error.md). Because of the mismatch, the [combineLatest(_:)](<combinelatest(__).md>) operator requires that `pub1` use [setFailureType(to:)](<setfailuretype(to_).md>) to make it appear that `pub1` can produce the [Error](../../swift/error.md) type, like `pub2` can.

```swift
let pub1 = [0, 1, 2, 3, 4, 5].publisher
let pub2 = CurrentValueSubject<Int, Error>(0)
let cancellable = pub1
    .setFailureType(to: Error.self)
    .combineLatest(pub2)
    .sink(
        receiveCompletion: { print ("completed: \($0)") },
        receiveValue: { print ("value: \($0)")}
     )

// Prints: "value: (5, 0)".
```

## See Also

### Mapping elements

- [map(_:)](<map(__)-99evh.md>) — Transforms all elements from the upstream publisher with a provided closure.
- [tryMap(_:)](<trymap(__).md>) — Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [mapError(_:)](<maperror(__).md>) — Converts any failure from the upstream publisher into a new error.
- [replaceNil(with:)](<replacenil(with_).md>) — Replaces nil elements in the stream with the provided element.
- [scan(_:_:)](<scan(____).md>) — Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [tryScan(_:_:)](<tryscan(____).md>) — Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.

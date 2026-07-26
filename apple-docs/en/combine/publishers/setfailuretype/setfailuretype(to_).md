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
doc_path: '/documentation/combine/publishers/setfailuretype/setfailuretype(to:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/setfailuretype/setfailuretype(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/setfailuretype/setfailuretype%28to%3A%29.json'
content_hash: 'sha256:d0e768514da93a26'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [SetFailureType](../setfailuretype.md)

# setFailureType(to:)

<sub>Instance Method</sub>

Changes the failure type declared by the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setFailureType<E>(to failure: E.Type) -> Publishers.SetFailureType<Upstream, E> where E : Error
```

## Return Value

A publisher that appears to send the specified failure type.

## Discussion

Use [setFailureType(to:)](<../../publisher/setfailuretype(to_).md>) when you need set the error type of a publisher that cannot fail.

Conversely, if the upstream can fail, you would use [mapError(_:)](<../../publisher/maperror(__).md>) to provide instructions on converting the error types to needed by the downstream publisher’s inputs.

The following example has two publishers with mismatched error types: `pub1`’s error type is [Never](../../../swift/never.md), and `pub2`’s error type is [Error](../../../swift/error.md). Because of the mismatch, the [combineLatest(_:)](<../../publisher/combinelatest(__).md>) operator requires that `pub1` use [setFailureType(to:)](<../../publisher/setfailuretype(to_).md>) to make it appear that `pub1` can produce the [Error](../../../swift/error.md) type, like `pub2` can.

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

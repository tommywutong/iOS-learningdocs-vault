---
title: eraseToAnyPublisher()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/erasetoanypublisher()
source_url: 'https://developer.apple.com/documentation/combine/publisher/erasetoanypublisher()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/erasetoanypublisher%28%29.json'
content_hash: 'sha256:546da34081e39eaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# eraseToAnyPublisher()

<sub>Instance Method</sub>

Wraps this publisher with a type eraser.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func eraseToAnyPublisher() -> AnyPublisher<Self.Output, Self.Failure>
```

## Return Value

An [AnyPublisher](../anypublisher.md) wrapping this publisher.

## Discussion

Use [eraseToAnyPublisher()](<erasetoanypublisher().md>) to expose an instance of [AnyPublisher](../anypublisher.md) to the downstream subscriber, rather than this publisher’s actual type. This form of _type erasure_ preserves abstraction across API boundaries, such as different modules. When you expose your publishers as the [AnyPublisher](../anypublisher.md) type, you can change the underlying implementation over time without affecting existing clients.

The following example shows two types that each have a `publisher` property. `TypeWithSubject` exposes this property as its actual type, [PassthroughSubject](../passthroughsubject.md), while `TypeWithErasedSubject` uses [eraseToAnyPublisher()](<erasetoanypublisher().md>) to expose it as an [AnyPublisher](../anypublisher.md). As seen in the output, a caller from another module can access `TypeWithSubject.publisher` as its native type. This means you can’t change your publisher to a different type without breaking the caller. By comparison, `TypeWithErasedSubject.publisher` appears to callers as an [AnyPublisher](../anypublisher.md), so you can change the underlying publisher type at will.

```swift
public class TypeWithSubject {
    public let publisher: some Publisher = PassthroughSubject<Int,Never>()
}
public class TypeWithErasedSubject {
    public let publisher: some Publisher = PassthroughSubject<Int,Never>()
        .eraseToAnyPublisher()
}

// In another module:
let nonErased = TypeWithSubject()
if let subject = nonErased.publisher as? PassthroughSubject<Int,Never> {
    print("Successfully cast nonErased.publisher.")
}
let erased = TypeWithErasedSubject()
if let subject = erased.publisher as? PassthroughSubject<Int,Never> {
    print("Successfully cast erased.publisher.")
}

// Prints "Successfully cast nonErased.publisher."
```

---
title: Result
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/result
source_url: 'https://developer.apple.com/documentation/swift/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result.json'
content_hash: 'sha256:6f9d9281a0f75171'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Result

<sub>Enumeration</sub>

A value that represents either a success or a failure, including an associated value in each case.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Result<Success, Failure> where Failure : Error, Success : ~Copyable, Success : ~Escapable
```

## Relationships

- **Conforms To**: [Copyable](copyable.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Representing a Result

- [Result.success(_:)](<result/success(__).md>) — A success, storing a `Success` value.
- [Result.failure(_:)](<result/failure(__).md>) — A failure, storing a `Failure` value.
- [Writing Failable Asynchronous APIs](writing-failable-asynchronous-apis.md) — Vend results as part of an API when you can’t return errors synchronously.

### Converting a Throwing Expression to a Result

- [Preserving the Results of a Throwing Expression](preserving-the-results-of-a-throwing-expression.md) — Call the initializer that wraps a throwing expression when you need to serialize or memoize the result.

### Converting a Result to a Throwing Expression

- [get()](<result/get().md>) — Returns the success value as a throwing expression.

### Transforming a Result

- [map(_:)](<result/map(__).md>) — Returns a new result, mapping any success value using the given transformation.
- [mapError(_:)](<result/maperror(__).md>) — Returns a new result, mapping any failure value using the given transformation.
- [flatMap(_:)](<result/flatmap(__).md>) — Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.
- [flatMapError(_:)](<result/flatmaperror(__).md>) — Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.

### Comparing Results

- [==(_:_:)](<result/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](<result/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.

### Publishing a Result

- [publisher](result/publisher-swift.property.md) — A Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.
- [Publisher](result/publisher-swift.struct.md) — The type of a Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.

### Initializers

- [init(catching:)](<result/init(catching_)-1tno.md>) — Creates a new result by evaluating an async throwing closure, capturing the returned value as a success, or any thrown error as a failure.
- [init(catching:)](<result/init(catching_)-62kyq.md>) — Creates a new result by evaluating a throwing closure, capturing the returned value as a success, or any thrown error as a failure.

### Default Implementations

- [Equatable Implementations](result/equatable-implementations.md)
- [Hashable Implementations](result/hashable-implementations.md)

## See Also

### Errors

- [Error](error.md) — A type representing an error value that can be thrown.

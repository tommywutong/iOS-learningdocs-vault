---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/flatmap(_:)'
source_url: 'https://developer.apple.com/documentation/swift/result/flatmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/flatmap%28_%3A%29.json'
content_hash: 'sha256:66dac05091c828d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# flatMap(_:)

<sub>Instance Method</sub>

Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<NewSuccess>(_ transform: (Success) -> Result<NewSuccess, Failure>) -> Result<NewSuccess, Failure> where NewSuccess : ~Copyable
```

## Parameters

- `transform` — A closure that takes the success value of the instance.

## Return Value

A `Result` instance, either from the closure or the previous `.failure`.

## Discussion

Use this method to avoid a nested result when your transformation produces another `Result` type.

In this example, note the difference in the result of using `map` and `flatMap` with a transformation that returns a result type.

```swift
func getNextInteger() -> Result<Int, Error> {
    .success(4)
}
func getNextAfterInteger(_ n: Int) -> Result<Int, Error> {
    .success(n + 1)
}

let result = getNextInteger().map { getNextAfterInteger($0) }
// result == .success(.success(5))

let result = getNextInteger().flatMap { getNextAfterInteger($0) }
// result == .success(5)
```

## See Also

### Transforming a Result

- [map(_:)](<map(__).md>) — Returns a new result, mapping any success value using the given transformation.
- [mapError(_:)](<maperror(__).md>) — Returns a new result, mapping any failure value using the given transformation.
- [flatMapError(_:)](<flatmaperror(__).md>) — Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.

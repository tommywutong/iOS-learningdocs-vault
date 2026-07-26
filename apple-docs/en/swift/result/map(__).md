---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/map(_:)'
source_url: 'https://developer.apple.com/documentation/swift/result/map(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/map%28_%3A%29.json'
content_hash: 'sha256:e31cf2a8fd174c9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# map(_:)

<sub>Instance Method</sub>

Returns a new result, mapping any success value using the given transformation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<NewSuccess>(_ transform: (Success) -> NewSuccess) -> Result<NewSuccess, Failure> where NewSuccess : ~Copyable
```

## Parameters

- `transform` — A closure that takes the success value of this instance.

## Return Value

A `Result` instance with the result of evaluating `transform` as the new success value if this instance represents a success.

## Discussion

Use this method when you need to transform the value of a `Result` instance when it represents a success. The following example transforms the integer success value of a result into a string:

```swift
func getNextInteger() -> Result<Int, Error> { /* ... */ }

let integerResult = getNextInteger()
// integerResult == .success(5)
let stringResult = integerResult.map { String($0) }
// stringResult == .success("5")
```

## See Also

### Transforming a Result

- [mapError(_:)](<maperror(__).md>) — Returns a new result, mapping any failure value using the given transformation.
- [flatMap(_:)](<flatmap(__).md>) — Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.
- [flatMapError(_:)](<flatmaperror(__).md>) — Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.

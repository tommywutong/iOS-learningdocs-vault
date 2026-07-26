---
title: 'mapError(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/maperror(_:)'
source_url: 'https://developer.apple.com/documentation/swift/result/maperror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/maperror%28_%3A%29.json'
content_hash: 'sha256:c9acfcbb9aaba5ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# mapError(_:)

<sub>Instance Method</sub>

Returns a new result, mapping any failure value using the given transformation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func mapError<NewFailure>(_ transform: (Failure) -> NewFailure) -> Result<Success, NewFailure> where NewFailure : Error
```

## Parameters

- `transform` — A closure that takes the failure value of the instance.

## Return Value

A `Result` instance with the result of evaluating `transform` as the new failure value if this instance represents a failure.

## Discussion

Use this method when you need to transform the value of a `Result` instance when it represents a failure. The following example transforms the error value of a result by wrapping it in a custom `Error` type:

```swift
struct DatedError: Error {
    var error: Error
    var date: Date

    init(_ error: Error) {
        self.error = error
        self.date = Date()
    }
}

let result: Result<Int, Error> = // ...
// result == .failure(<error value>)
let resultWithDatedError = result.mapError { DatedError($0) }
// result == .failure(DatedError(error: <error value>, date: <date>))
```

## See Also

### Transforming a Result

- [map(_:)](<map(__).md>) — Returns a new result, mapping any success value using the given transformation.
- [flatMap(_:)](<flatmap(__).md>) — Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.
- [flatMapError(_:)](<flatmaperror(__).md>) — Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.

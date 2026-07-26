---
title: 'flatMapError(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/flatmaperror(_:)'
source_url: 'https://developer.apple.com/documentation/swift/result/flatmaperror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/flatmaperror%28_%3A%29.json'
content_hash: 'sha256:20b43850f48c6c2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# flatMapError(_:)

<sub>Instance Method</sub>

Returns a new result, mapping any failure value using the given transformation and unwrapping the produced result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func flatMapError<NewFailure>(_ transform: (Failure) -> Result<Success, NewFailure>) -> Result<Success, NewFailure> where NewFailure : Error
```

## Parameters

- `transform` — A closure that takes the failure value of the instance.

## Return Value

A `Result` instance, either from the closure or the previous `.success`.

## See Also

### Transforming a Result

- [map(_:)](<map(__).md>) — Returns a new result, mapping any success value using the given transformation.
- [mapError(_:)](<maperror(__).md>) — Returns a new result, mapping any failure value using the given transformation.
- [flatMap(_:)](<flatmap(__).md>) — Returns a new result, mapping any success value using the given transformation and unwrapping the produced result.

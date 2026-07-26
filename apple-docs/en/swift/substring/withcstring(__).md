---
title: 'withCString(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/withcstring(_:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/withcstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/withcstring%28_%3A%29.json'
content_hash: 'sha256:24e1786b407aa78e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# withCString(_:)

<sub>Instance Method</sub>

Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withCString<Result, E>(_ body: (UnsafePointer<CChar>) throws(E) -> Result) throws(E) -> Result where E : Error
```

## Parameters

- `body` — A closure with a pointer parameter that points to a null-terminated sequence of UTF-8 code units. If `body` has a return value, that value is also used as the return value for the `withCString(_:)` method. The pointer argument is valid only for the duration of the method’s execution.

## Return Value

The return value, if any, of the `body` closure parameter.

## Discussion

The pointer passed as an argument to `body` is valid only during the execution of `withCString(_:)`. Do not store or return the pointer for later use.

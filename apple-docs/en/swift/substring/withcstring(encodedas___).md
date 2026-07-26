---
title: 'withCString(encodedAs:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/withcstring(encodedas:_:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/withcstring(encodedas:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/withcstring%28encodedas%3A_%3A%29.json'
content_hash: 'sha256:a5cebf333d57984d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# withCString(encodedAs:_:)

<sub>Instance Method</sub>

Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withCString<Result, TargetEncoding, E>(encodedAs targetEncoding: TargetEncoding.Type, _ body: (UnsafePointer<TargetEncoding.CodeUnit>) throws(E) -> Result) throws(E) -> Result where TargetEncoding : _UnicodeEncoding, E : Error
```

## Parameters

- `targetEncoding` — The encoding in which the code units should be interpreted.

- `body` — A closure with a pointer parameter that points to a null-terminated sequence of code units. If `body` has a return value, that value is also used as the return value for the `withCString(encodedAs:_:)` method. The pointer argument is valid only for the duration of the method’s execution.

## Return Value

The return value, if any, of the `body` closure parameter.

## Discussion

The pointer passed as an argument to `body` is valid only during the execution of `withCString(encodedAs:_:)`. Do not store or return the pointer for later use.

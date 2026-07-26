---
title: 'withPlatformString(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/withplatformstring(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/withplatformstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/withplatformstring%28_%3A%29.json'
content_hash: 'sha256:567034561f61d511'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# withPlatformString(_:)

<sub>Instance Method</sub>

Calls the given closure with a pointer to the contents of the string, represented as a null-terminated platform string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withPlatformString<Result>(_ body: (UnsafePointer<CInterop.PlatformChar>) throws -> Result) rethrows -> Result
```

## Parameters

- `body` — A closure with a pointer parameter that points to a null-terminated platform string. If `body` has a return value, that value is also used as the return value for this method.

## Return Value

The return value, if any, of the `body` closure parameter.

## Discussion

The pointer passed as an argument to `body` is valid only during the execution of this method. Don’t try to store the pointer for later use.

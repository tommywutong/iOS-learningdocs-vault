---
title: unsafeArgv
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/commandline/unsafeargv
source_url: 'https://developer.apple.com/documentation/swift/commandline/unsafeargv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/commandline/unsafeargv.json'
content_hash: 'sha256:86a41ff42acad694'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CommandLine](../commandline.md)

# unsafeArgv

<sub>Type Property</sub>

Access to the raw argv value from C.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var unsafeArgv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?> { get }
```

## Discussion

The value of this property is a `nil`-terminated C array. Including the trailing `nil`, there are [argc](argc.md) `+ 1` elements in the array.

> [!note] Note
> Accessing the argument vector through this pointer is unsafe. Where possible, use [arguments](arguments.md) instead.

## See Also

### Accessing Raw Argument Data

- [argc](argc.md) — Access to the raw argc value from C.

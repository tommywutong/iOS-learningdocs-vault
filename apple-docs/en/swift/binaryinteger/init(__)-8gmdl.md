---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryinteger/init(_:)-8gmdl'
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/init(_:)-8gmdl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/init%28_%3A%29-8gmdl.json'
content_hash: 'sha256:6814fbf8bb4acc6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance from the given integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ source: T) where T : BinaryInteger
```

## Parameters

- `source` — An integer to convert. `source` must be representable in this type.

## Discussion

If the value passed as `source` is not representable in this type, a runtime error may occur.

```swift
let x = -500 as Int
let y = Int32(x)
// y == -500

// -500 is not representable as a 'UInt32' instance
let z = UInt32(x)
// Error
```

## Default Implementations

### BinaryInteger Implementations

- [init(_:)](<init(__)-3cx61.md>) — Creates a new integer value from the given string.
- [init(_:)](<init(__)-5yrn0.md>) — Creates a new instance from the given integer.
- [init(_:)](<init(__)-62cdc.md>)
- [init(_:)](<init(__)-6u4mr.md>) — Creates a new instance from the given integer.

### FixedWidthInteger Implementations

- [init(_:)](<../fixedwidthinteger/init(__).md>) — Convert from an Backtrace.Address.

## See Also

### Converting Integers

- [init(clamping:)](<init(clamping_).md>) — Creates a new instance with the representable value that’s closest to the given integer.
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.

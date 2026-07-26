---
title: base
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/slice/base
source_url: 'https://developer.apple.com/documentation/swift/slice/base'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/base.json'
content_hash: 'sha256:d05db6fefab4ecab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# base

<sub>Instance Property</sub>

The underlying collection of the slice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var base: Base { get }
```

## Discussion

You can use a slice’s `base` property to access its base collection. The following example declares `singleDigits`, a range of single digit integers, and then drops the first element to create a slice of that range, `singleNonZeroDigits`. The `base` property of the slice is equal to `singleDigits`.

```swift
let singleDigits = 0..<10
let singleNonZeroDigits = singleDigits.dropFirst()
// singleNonZeroDigits is a Slice<Range<Int>>

print(singleNonZeroDigits.count)
// Prints "9"
print(singleNonZeroDigits.base.count)
// Prints "10"
print(singleDigits == singleNonZeroDigits.base)
// Prints "true"
```

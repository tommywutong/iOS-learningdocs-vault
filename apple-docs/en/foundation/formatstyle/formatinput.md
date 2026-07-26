---
title: FormatInput
framework: Foundation
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/formatinput
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/formatinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/formatinput.json'
content_hash: 'sha256:0029d12ff67055e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# FormatInput

<sub>Associated Type</sub>

The type this format style accepts as input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype FormatInput
```

## Discussion

Swift type inference uses this value to determine which static accessors are available at a given call point. For example, when you format an [Int32](../../swift/int32.md), you can use the static [number](number-4cj49.md) property that provies a `IntegerFormatStyle<Int32>`, as seen in the following example. This works because the style’s input type `IntegerFormatStyle/FormatInput` is a [BinaryInteger](../../swift/binaryinteger.md) generically constrained to the [Int32](../../swift/int32.md) type.

```swift
let perihelionDistanceToSunInKm: Int32 = 147098291
perihelionDistanceToSunInKm.formatted(.number
    .notation(.scientific)) // "1.470983E8"
```

## See Also

### Declaring input and output types

- [FormatOutput](formatoutput.md) — The type this format style produces as output.

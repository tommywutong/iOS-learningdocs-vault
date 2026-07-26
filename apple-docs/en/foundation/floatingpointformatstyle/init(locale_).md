---
title: 'init(locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/floatingpointformatstyle/init(locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle/init(locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle/init%28locale%3A%29.json'
content_hash: 'sha256:0112f8f8f2490a72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FloatingPointFormatStyle](../floatingpointformatstyle.md)

# init(locale:)

<sub>Initializer</sub>

Creates a floating-point format style that uses the given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `locale` — The locale to use when formatting or parsing floating-point values. Defaults to [autoupdatingCurrent](../locale/autoupdatingcurrent.md).

## Discussion

Create a [FloatingPointFormatStyle](../floatingpointformatstyle.md) when you intend to apply a given style to multiple floating-point values. The following example creates a style that uses the `en_US` locale, which uses three-based grouping and comma separators. It then applies this style to all the [Double](../../swift/double.md) values in an array.

```swift
let enUSstyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
let nums = [100.1, 1000.2, 10000.3, 100000.4, 1000000.5]
let formattedNums = nums.map { enUSstyle.format($0) } // ["100.1", "1,000.2", "10,000.3", "100,000.4", "1,000,000.5"]

```

To format a single integer, you can use the [BinaryFloatingPoint](../../swift/binaryfloatingpoint.md) instance method [formatted(_:)](<../../swift/binaryfloatingpoint/formatted(__)-83x4n.md>), passing in an instance of [FloatingPointFormatStyle](../floatingpointformatstyle.md).

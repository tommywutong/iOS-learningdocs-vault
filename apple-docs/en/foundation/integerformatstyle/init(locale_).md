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
doc_path: '/documentation/foundation/integerformatstyle/init(locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/init(locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/init%28locale%3A%29.json'
content_hash: 'sha256:a51018663fc520e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# init(locale:)

<sub>Initializer</sub>

Creates an integer format style that uses the given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `locale` — The locale to use when formatting or parsing integers. Defaults to [autoupdatingCurrent](../locale/autoupdatingcurrent.md).

## Discussion

Create an [IntegerFormatStyle](../integerformatstyle.md) when you intend to apply a given style to multiple integers. The following example creates a style that uses the `en_US` locale, which uses three-based grouping and comma separators. It then applies this style to all the integers in an array.

```swift
let enUSstyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
let nums = [100, 1000, 10000, 100000, 1000000]
let formattedNums = nums.map { enUSstyle.format($0) } // ["100", "1,000", "10,000", "100,000", "1,000,000"]
```

To format a single integer, you can use the [BinaryInteger](../../swift/binaryinteger.md) instance method [formatted(_:)](<../../swift/binaryinteger/formatted(__)-4qd73.md>), passing in an instance of [IntegerFormatStyle](../integerformatstyle.md).

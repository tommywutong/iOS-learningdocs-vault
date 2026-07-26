---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/locale%28_%3A%29.json'
content_hash: 'sha256:22a4a464d25d7b37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> IntegerFormatStyle<Value>
```

## Parameters

- `locale` — The locale to apply to the format style.

## Return Value

An integer format style modified to use the provided locale.

## Discussion

Use this modifier to change the locale used by an existing format style. To instead determine the locale this format style uses, use the [locale](locale.md) property.

The following example creates a default [IntegerFormatStyle](../integerformatstyle.md) for the `en_US` locale, and applies the [notation(_:)](<notation(__).md>) modifier to use compact name notation. Next, the sample creates a second style based on this first style, but using the German (`DE`) locale. It then applies each style to an array of integers.

```swift
let compactStyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
    .notation(.compactName)
let germanStyle = compactStyle.locale(Locale(identifier:"DE"))
let nums = [100, 1000, 10000, 100000, 1000000]
let enUSCompactNums = nums.map { compactStyle.format($0) } // ["100", "1K", "10K", "100K", "1M"]
let deCompactNums = nums.map { germanStyle.format($0) } // ["100", "1000", "10.000", "100.000", "1 Mio."]
```

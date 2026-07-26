---
title: 'fixed(explicitPositiveSign:uppercase:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogfloatformatting/fixed(explicitpositivesign:uppercase:)'
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting/fixed(explicitpositivesign:uppercase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting/fixed%28explicitpositivesign%3Auppercase%3A%29.json'
content_hash: 'sha256:7b9884a3962bc513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogFloatFormatting](../oslogfloatformatting.md)

# fixed(explicitPositiveSign:uppercase:)

<sub>Type Method</sub>

Creates a custom fixed-point format with a system-determined precision value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func fixed(explicitPositiveSign: Bool = false, uppercase: Bool = false) -> OSLogFloatFormatting
```

## Parameters

- `explicitPositiveSign` — A Boolean value that indicates whether to display a plus (`+`) sign in front of positive numbers.

- `uppercase` — A Boolean value that indicates whether to uppercase letters that are part of the floating-point number. For example, it determines the capitalization of the exponent indicator `e` in the number `1.0e9`, or the letters in special values such as `NaN` and `Inf`.

## Return Value

A custom fixed-point format for floating-point numbers.

## See Also

### Creating a Custom Formatting Object

- [exponential(explicitPositiveSign:uppercase:)](<exponential(explicitpositivesign_uppercase_).md>) — Creates a custom exponential format with a system-determined precision value.
- [exponential(precision:explicitPositiveSign:uppercase:)](<exponential(precision_explicitpositivesign_uppercase_).md>) — Creates a custom exponential format with the specified precision value.
- [fixed(precision:explicitPositiveSign:uppercase:)](<fixed(precision_explicitpositivesign_uppercase_).md>) — Creates a custom fixed-point format with the specified precision value.
- [hex(explicitPositiveSign:uppercase:)](<hex(explicitpositivesign_uppercase_).md>) — Creates a custom hexadecimal format.
- [hybrid(explicitPositiveSign:uppercase:)](<hybrid(explicitpositivesign_uppercase_).md>) — Creates a custom hybrid format with a system-determined precision value.
- [hybrid(precision:explicitPositiveSign:uppercase:)](<hybrid(precision_explicitpositivesign_uppercase_).md>) — Creates a custom hybrid format with the precision value.

---
title: 'decimal(explicitPositiveSign:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogintegerformatting/decimal(explicitpositivesign:)'
source_url: 'https://developer.apple.com/documentation/os/oslogintegerformatting/decimal(explicitpositivesign:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogintegerformatting/decimal%28explicitpositivesign%3A%29.json'
content_hash: 'sha256:a0d09ff6b8a10805'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogIntegerFormatting](../oslogintegerformatting.md)

# decimal(explicitPositiveSign:)

<sub>Type Method</sub>

Creates a decimal format with custom handling of the numerical sign.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decimal(explicitPositiveSign: Bool = false) -> OSLogIntegerFormatting
```

## Parameters

- `explicitPositiveSign` — A Boolean value that indicates whether to display a plus (`+`) sign in front of positive integers.

## Return Value

A custom decimal format for integers.

## See Also

### Creating a Custom Integer Format

- [decimal(explicitPositiveSign:minDigits:)](<decimal(explicitpositivesign_mindigits_).md>) — Creates a decimal format with custom handling of the numerical sign and the minimum number of digits.
- [hex(explicitPositiveSign:includePrefix:uppercase:)](<hex(explicitpositivesign_includeprefix_uppercase_).md>) — Creates a custom hexidecimal format that displays the exact number of digits in the number.
- [hex(explicitPositiveSign:includePrefix:uppercase:minDigits:)](<hex(explicitpositivesign_includeprefix_uppercase_mindigits_).md>) — Creates a custom hexidecimal format that includes a minimum number of digits.
- [octal(explicitPositiveSign:includePrefix:uppercase:)](<octal(explicitpositivesign_includeprefix_uppercase_).md>) — Creates a custom octal format that displays the exact number of digits in the number.
- [octal(explicitPositiveSign:includePrefix:uppercase:minDigits:)](<octal(explicitpositivesign_includeprefix_uppercase_mindigits_).md>) — Creates a custom octal format that includes a minimum number of digits.

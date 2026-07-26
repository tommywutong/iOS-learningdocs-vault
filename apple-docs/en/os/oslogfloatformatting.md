---
title: OSLogFloatFormatting
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogfloatformatting
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting.json'
content_hash: 'sha256:2d837f46850affad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSLogFloatFormatting

<sub>Structure</sub>

The formatting options for double and floating-point numbers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogFloatFormatting
```

## Overview

An [OSLogFloatFormatting](oslogfloatformatting.md) structure encapsulates the formatting details for `double` and `float` values. Use the static [fixed](oslogfloatformatting/fixed.md), [hex](oslogfloatformatting/hex.md), [exponential](oslogfloatformatting/exponential.md), and [hybrid](oslogfloatformatting/hybrid.md) structures to apply default formatting for floating-point values. You can also create new [OSLogFloatFormatting](oslogfloatformatting.md) structures that customize the rules for handling a leading plus sign, precision information, and more.

## Topics

### Getting the Standard Formats

- [fixed](oslogfloatformatting/fixed.md) — The standard fixed-point format option.
- [hex](oslogfloatformatting/hex.md) — The standard hexadecimal format for floating-point values.
- [exponential](oslogfloatformatting/exponential.md) — The standard exponential format option.
- [hybrid](oslogfloatformatting/hybrid.md) — A hybrid option that changes the format according to the size of the number.

### Creating a Custom Formatting Object

- [exponential(explicitPositiveSign:uppercase:)](<oslogfloatformatting/exponential(explicitpositivesign_uppercase_).md>) — Creates a custom exponential format with a system-determined precision value.
- [exponential(precision:explicitPositiveSign:uppercase:)](<oslogfloatformatting/exponential(precision_explicitpositivesign_uppercase_).md>) — Creates a custom exponential format with the specified precision value.
- [fixed(explicitPositiveSign:uppercase:)](<oslogfloatformatting/fixed(explicitpositivesign_uppercase_).md>) — Creates a custom fixed-point format with a system-determined precision value.
- [fixed(precision:explicitPositiveSign:uppercase:)](<oslogfloatformatting/fixed(precision_explicitpositivesign_uppercase_).md>) — Creates a custom fixed-point format with the specified precision value.
- [hex(explicitPositiveSign:uppercase:)](<oslogfloatformatting/hex(explicitpositivesign_uppercase_).md>) — Creates a custom hexadecimal format.
- [hybrid(explicitPositiveSign:uppercase:)](<oslogfloatformatting/hybrid(explicitpositivesign_uppercase_).md>) — Creates a custom hybrid format with a system-determined precision value.
- [hybrid(precision:explicitPositiveSign:uppercase:)](<oslogfloatformatting/hybrid(precision_explicitpositivesign_uppercase_).md>) — Creates a custom hybrid format with the precision value.

## See Also

### Value Formatters

- [OSLogBoolFormat](oslogboolformat.md) — The formatting options for Boolean values.
- [OSLogIntegerFormatting](oslogintegerformatting.md) — The formatting options for integer values.
- [OSLogInt32ExtendedFormat](oslogint32extendedformat.md) — The formatting options for 32-bit integer values.
- [OSLogPointerFormat](oslogpointerformat.md) — The formatting options for pointer data.

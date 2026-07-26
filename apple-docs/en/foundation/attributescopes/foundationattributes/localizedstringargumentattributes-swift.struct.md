---
title: AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct.json'
content_hash: 'sha256:b9191f7714abc478'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [FoundationAttributes](../foundationattributes.md)

# AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes

<sub>Structure</sub>

A type for using a localized string argument as an attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LocalizedStringArgumentAttributes
```

## Overview

You use the this scope’s attributes when creating an attributed string from a [LocalizedStringResource](../../localizedstringresource.md). The process creating the attributed string may not have access to the original arguments passed to the interpolation. Instead, the attributed string marks formatted runs with this type, allowing you to retrieve the original values.

## Topics

### Retrieving localization arguments

- [localizedNumericArgument](localizedstringargumentattributes-swift.struct/localizednumericargument.md) — The value of a numeric argument used to format the run with this attribute.
- [LocalizedNumericArgumentAttribute](localizedstringargumentattributes-swift.struct/localizednumericargumentattribute.md) — A type for a numeric argument used to format the run with this attribute.
- [localizedDateArgument](localizedstringargumentattributes-swift.struct/localizeddateargument.md) — The date value used to format the run with this attribute.
- [LocalizedDateArgumentAttribute](localizedstringargumentattributes-swift.struct/localizeddateargumentattribute.md) — A type for a date argument used to format the run with this attribute.
- [localizedDateIntervalArgument](localizedstringargumentattributes-swift.struct/localizeddateintervalargument.md) — The date interval value used to format the run with this attribute.
- [LocalizedDateIntervalArgumentAttribute](localizedstringargumentattributes-swift.struct/localizeddateintervalargumentattribute.md) — A type for a date interval argument used to format the run with this attribute.
- [localizedURLArgument](localizedstringargumentattributes-swift.struct/localizedurlargument.md) — The URL value used to format the run with this attribute.
- [LocalizedURLArgumentAttribute](localizedstringargumentattributes-swift.struct/localizedurlargumentattribute.md) — A type for a URL argument used to format the run with this attribute.

## See Also

### Using string localization attributes

- [localizedStringArgumentAttributes](localizedstringargumentattributes-swift.property.md) — A property for accessing a localized string argument attribute.

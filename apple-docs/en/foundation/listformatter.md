---
title: ListFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/listformatter
source_url: 'https://developer.apple.com/documentation/foundation/listformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatter.json'
content_hash: 'sha256:697089b77ccc39eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ListFormatter

<sub>Class</sub>

An object that provides locale-correct formatting of a list of items using the appropriate separator and conjunction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ListFormatter
```

## Overview

The list formatter isn’t aware of the context where the formatted string will be used and doesn’t provide capitalization customization of the list items. The formatted result may not be grammatically correct if placed in a sentence, and it should only be used in a standalone manner.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Converting Arrays to Formatted Lists

- [- stringFromItems:](<listformatter/string(from_).md>) — Creates a formatted string for an array of items.
- [- stringForObjectValue:](<listformatter/string(for_).md>) — Creates a formatted string for an array of items.
- [+ localizedStringByJoiningStrings:](<listformatter/localizedstring(byjoining_).md>) — Constructs a formatted string from an array of strings that uses the list format specific to the current locale.

### Configuring Formatter Options

- [itemFormatter](listformatter/itemformatter.md) — An object that formats each item in the list.
- [locale](listformatter/locale.md) — The locale to use when formatting items in the list.

---
title: 'localizedAttributedStringWithFormat:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/localizedattributedstringwithformat:'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/localizedattributedstringwithformat:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/localizedattributedstringwithformat%3A.json'
content_hash: 'sha256:a7e8212cf59b1c9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# localizedAttributedStringWithFormat:

<sub>Type Method</sub>

Creates an attributed string by substituting arguments into a specially formatted string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) localizedAttributedStringWithFormat:(NSAttributedString *) format;
```

## Parameters

- `format` — The format string to use to create the final string. For a list of format specifiers you can include in this string, see [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

## Return Value

A new attributed string that combines the format string with the provided arguments and other information.

## Discussion

Pass an optional list of trailing variadic arguments to substitute into the `format` string.

## See Also

### Creating a formatted string

- [initWithFormat:options:locale:](initwithformat_options_locale_.md) — Initializes an attributed string by substituting arguments into a specially formatted string.
- [initWithFormat:options:locale:arguments:](initwithformat_options_locale_arguments_.md) — Initializes an attributed string by substituting a list of function arguments into a specially formatted string.
- [initWithFormat:options:locale:context:](initwithformat_options_locale_context_.md) — Initializes an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [initWithFormat:options:locale:context:arguments:](initwithformat_options_locale_context_arguments_.md) — Initializes an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.
- [localizedAttributedStringWithFormat:options:](localizedattributedstringwithformat_options_.md) — Creates an attributed string by substituting a list of function arguments into a specially formatted string.
- [localizedAttributedStringWithFormat:context:](localizedattributedstringwithformat_context_.md) — Creates an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [localizedAttributedStringWithFormat:options:context:](localizedattributedstringwithformat_options_context_.md) — Creates an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.
- [NSAttributedStringFormattingOptions](../nsattributedstringformattingoptions.md) — Options to use when creating an attributed string from a format string and variable list of arguments.

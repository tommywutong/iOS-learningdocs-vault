---
title: 'initWithFormat:options:locale:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/initwithformat:options:locale:'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/initwithformat:options:locale:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/initwithformat%3Aoptions%3Alocale%3A.json'
content_hash: 'sha256:7149b2467e3c081f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# initWithFormat:options:locale:

<sub>Instance Method</sub>

Initializes an attributed string by substituting arguments into a specially formatted string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithFormat:(NSAttributedString *) format options:(NSAttributedStringFormattingOptions) options locale:(NSLocale *) locale;
```

## Parameters

- `format` — The format string to use to create the final string. For a list of format specifiers you can include in this string, see [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

- `options` — Options for how to apply attributes to the string’s content.

- `locale` — The locale to use for formatting the string. The locale controls the formatting of region-sensitive values such as numbers and currencies.

## Return Value

An initialized attributed string that combines the format string with the provided arguments and other information.

## Discussion

Pass an optional list of trailing variadic arguments to substitute into the `format` string.

## See Also

### Creating a formatted string

- [initWithFormat:options:locale:arguments:](initwithformat_options_locale_arguments_.md) — Initializes an attributed string by substituting a list of function arguments into a specially formatted string.
- [initWithFormat:options:locale:context:](initwithformat_options_locale_context_.md) — Initializes an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [initWithFormat:options:locale:context:arguments:](initwithformat_options_locale_context_arguments_.md) — Initializes an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.
- [localizedAttributedStringWithFormat:](localizedattributedstringwithformat_.md) — Creates an attributed string by substituting arguments into a specially formatted string.
- [localizedAttributedStringWithFormat:options:](localizedattributedstringwithformat_options_.md) — Creates an attributed string by substituting a list of function arguments into a specially formatted string.
- [localizedAttributedStringWithFormat:context:](localizedattributedstringwithformat_context_.md) — Creates an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [localizedAttributedStringWithFormat:options:context:](localizedattributedstringwithformat_options_context_.md) — Creates an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.
- [NSAttributedStringFormattingOptions](../nsattributedstringformattingoptions.md) — Options to use when creating an attributed string from a format string and variable list of arguments.

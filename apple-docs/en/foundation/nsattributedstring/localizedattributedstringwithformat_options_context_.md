---
title: 'localizedAttributedStringWithFormat:options:context:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/localizedattributedstringwithformat:options:context:'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/localizedattributedstringwithformat:options:context:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/localizedattributedstringwithformat%3Aoptions%3Acontext%3A.json'
content_hash: 'sha256:6c1d84d05138b883'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# localizedAttributedStringWithFormat:options:context:

<sub>Type Method</sub>

Creates an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) localizedAttributedStringWithFormat:(NSAttributedString *) format options:(NSAttributedStringFormattingOptions) options context:(NSDictionary<NSString *,id> *) context;
```

## Parameters

- `format` — The format string to use to create the final string. For a list of format specifiers you can include in this string, see [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

- `options` — Options for how to apply attributes to the string’s content.

- `context` — Additional options to apply to the string.

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
- [localizedAttributedStringWithFormat:](localizedattributedstringwithformat_.md) — Creates an attributed string by substituting arguments into a specially formatted string.
- [localizedAttributedStringWithFormat:options:](localizedattributedstringwithformat_options_.md) — Creates an attributed string by substituting a list of function arguments into a specially formatted string.
- [localizedAttributedStringWithFormat:context:](localizedattributedstringwithformat_context_.md) — Creates an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [NSAttributedStringFormattingOptions](../nsattributedstringformattingoptions.md) — Options to use when creating an attributed string from a format string and variable list of arguments.

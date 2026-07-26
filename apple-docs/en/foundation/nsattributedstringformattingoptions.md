---
title: NSAttributedStringFormattingOptions
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringformattingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringformattingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringformattingoptions.json'
content_hash: 'sha256:a8b7b32e70f8e941'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAttributedStringFormattingOptions

<sub>Enumeration</sub>

Options to use when creating an attributed string from a format string and variable list of arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
enum NSAttributedStringFormattingOptions : NSUInteger;
```

## Topics

### Getting the formatting options

- [NSAttributedStringFormattingApplyReplacementIndexAttribute](nsattributedstringformattingoptions/nsattributedstringformattingapplyreplacementindexattribute.md) — An option to apply to the replaced portions of text in a format string.
- [NSAttributedStringFormattingInsertArgumentAttributesWithoutMerging](nsattributedstringformattingoptions/nsattributedstringformattinginsertargumentattributeswithoutmerging.md) — An option to replace the attributes in a substituted string with those of the provided attributed string.

## See Also

### Creating a formatted string

- [initWithFormat:options:locale:](nsattributedstring/initwithformat_options_locale_.md) — Initializes an attributed string by substituting arguments into a specially formatted string.
- [initWithFormat:options:locale:arguments:](nsattributedstring/initwithformat_options_locale_arguments_.md) — Initializes an attributed string by substituting a list of function arguments into a specially formatted string.
- [initWithFormat:options:locale:context:](nsattributedstring/initwithformat_options_locale_context_.md) — Initializes an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [initWithFormat:options:locale:context:arguments:](nsattributedstring/initwithformat_options_locale_context_arguments_.md) — Initializes an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.
- [localizedAttributedStringWithFormat:](nsattributedstring/localizedattributedstringwithformat_.md) — Creates an attributed string by substituting arguments into a specially formatted string.
- [localizedAttributedStringWithFormat:options:](nsattributedstring/localizedattributedstringwithformat_options_.md) — Creates an attributed string by substituting a list of function arguments into a specially formatted string.
- [localizedAttributedStringWithFormat:context:](nsattributedstring/localizedattributedstringwithformat_context_.md) — Creates an attributed string by substituting arguments into a specially formatted string and applying additional contextual information.
- [localizedAttributedStringWithFormat:options:context:](nsattributedstring/localizedattributedstringwithformat_options_context_.md) — Creates an attributed string by substituting a list of function arguments into a specially formatted string and applying additional contextual information.

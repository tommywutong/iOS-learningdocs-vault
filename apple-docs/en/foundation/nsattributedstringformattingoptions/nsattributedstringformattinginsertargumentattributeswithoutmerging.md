---
title: NSAttributedStringFormattingInsertArgumentAttributesWithoutMerging
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringformattingoptions/nsattributedstringformattinginsertargumentattributeswithoutmerging
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringformattingoptions/nsattributedstringformattinginsertargumentattributeswithoutmerging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringformattingoptions/nsattributedstringformattinginsertargumentattributeswithoutmerging.json'
content_hash: 'sha256:eca1c52c07ca6cd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringFormattingOptions](../nsattributedstringformattingoptions.md)

# NSAttributedStringFormattingInsertArgumentAttributesWithoutMerging

<sub>Enumeration Case</sub>

An option to replace the attributes in a substituted string with those of the provided attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSAttributedStringFormattingInsertArgumentAttributesWithoutMerging
```

## Discussion

This option applies when a format string includes the %@ format string specifier and the substituted value is an attributed string. If you include this option, the creation method prefers the attributes in the substitute attributed string over the attributes in the format string. If you don’t include this option, the creation method prefers the attributes from the format string over those in the substitute string.

Consider a format string `“Name: %@”` that applies a red text color to the substituted value, and consider an attributed string that applies green text using the same attribute. If you don’t include this option, the substituted text in the new string is red. If you include the option, the substituted text is green. This option affects only attributes that are common to both the format string and the substitute string.

If a creation method doesn’t let you specify options, it behaves as if this option isn’t present.

## See Also

### Getting the formatting options

- [NSAttributedStringFormattingApplyReplacementIndexAttribute](nsattributedstringformattingapplyreplacementindexattribute.md) — An option to apply to the replaced portions of text in a format string.

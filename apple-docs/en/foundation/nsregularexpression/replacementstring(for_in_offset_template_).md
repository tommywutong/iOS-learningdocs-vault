---
title: 'replacementString(for:in:offset:template:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/replacementstring(for:in:offset:template:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/replacementstring(for:in:offset:template:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/replacementstring%28for%3Ain%3Aoffset%3Atemplate%3A%29.json'
content_hash: 'sha256:6ae6cb439efa8a50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# replacementString(for:in:offset:template:)

<sub>Instance Method</sub>

Used to perform template substitution for a single result for clients implementing their own replace functionality.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacementString(for result: NSTextCheckingResult, in string: String, offset: Int, template templ: String) -> String
```

## Parameters

- `result` — The result of the single match.

- `string` — The string from which the result was matched.

- `offset` — The offset to be added to the location of the result in the string.

- `templ` — See [Flag Options](../nsregularexpression.md#Flag-Options) for the format of `template`.

## Return Value

A replacement string.

## Discussion

For clients implementing their own replace functionality, this is a method to perform the template substitution for a single result, given the string from which the result was matched, an offset to be added to the location of the result in the string (for example, in cases that modifications to the string moved the result since it was matched), and a replacement template.

This is an advanced method that is used only if you wanted to iterate through a list of matches yourself and do the template replacement for each one, plus maybe some other calculation that you want to do in code, then you would use this at each step.

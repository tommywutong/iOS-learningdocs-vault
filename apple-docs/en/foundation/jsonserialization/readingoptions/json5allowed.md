---
title: json5Allowed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonserialization/readingoptions/json5allowed
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions/json5allowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/readingoptions/json5allowed.json'
content_hash: 'sha256:c7d04d536b818c08'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONSerialization](../../jsonserialization.md) · [ReadingOptions](../readingoptions.md)

# json5Allowed

<sub>Type Property</sub>

Specifies that reading serialized JSON data supports the JSON5 syntax.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var json5Allowed: JSONSerialization.ReadingOptions { get }
```

## Discussion

The JSON5 Data Interchange Format is a superset of JSON that enhances human-readability of the JSON syntax. The JSON5 standard allows the following:

- Single- or double-quoted strings.
- Strings that span multiple lines.
- Single- and multiline comments, using `//` and `/* … */` syntax.
- Enhanced number formatting support, including hexadecimal, leading or trailing decimal point, explicit plus sign, and IEEE 754 positive infinity, negative infinity, and `NaN`.

### Using JSON5 in Attributed Strings

The Markdown syntax supported by [AttributedString](../../attributedstring.md) uses JSON5 to support an extended attribute syntax. Automatic grammar agreement uses this syntax for its `inflect` attribute, as do custom attributes defined by third-party frameworks. Use the syntax `^[text](attribute: value)` to mark ranges of text decorated with a custom attribute, like this:

```other
This is a [Markdown](https://commonmark.org) string with a ^[custom attribute](factor: 10).
```

This example applies a custom attribute called `factor` with a value of `10` to the text “custom attribute” in the resulting attributed string. The portion inside the parentheses is JSON5. [AttributedString](../../attributedstring.md) also uses the [NSJSONReadingTopLevelDictionaryAssumed](topleveldictionaryassumed.md) option; without it, the Markdown string would have to wrap everything inside the parentheses with braces.

## See Also

### Reading Options

- [NSJSONReadingMutableContainers](mutablecontainers.md) — Specifies that arrays and dictionaries in the returned object are mutable.
- [NSJSONReadingMutableLeaves](mutableleaves.md) — Specifies that leaf strings in the JSON object graph are mutable.
- [NSJSONReadingFragmentsAllowed](fragmentsallowed.md) — Specifies that the parser allows top-level objects that aren’t arrays or dictionaries.
- [NSJSONReadingTopLevelDictionaryAssumed](topleveldictionaryassumed.md) — Specifies that the parser assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with curly braces.
- [NSJSONReadingAllowFragments](allowfragments.md) — A deprecated option that specifies that the parser should allow top-level objects that aren’t arrays or dictionaries. _(deprecated)_

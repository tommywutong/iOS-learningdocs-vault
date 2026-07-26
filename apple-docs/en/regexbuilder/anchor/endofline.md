---
title: endOfLine
framework: RegexBuilder
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/anchor/endofline
source_url: 'https://developer.apple.com/documentation/regexbuilder/anchor/endofline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/anchor/endofline.json'
content_hash: 'sha256:f1bb4f3b3d9ecdea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Anchor](../anchor.md)

# endOfLine

<sub>Type Property</sub>

An anchor that matches at the end of a line, including at the end of the input string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var endOfLine: Anchor { get }
```

## Discussion

This anchor is equivalent to `$` in regex syntax when the `m` option has been enabled or `anchorsMatchLineEndings(true)` has been called.

For example, the following regexes are all equivalent:

- `Regex { Anchor.endOfLine }`
- `/(?m)$/` or `/(?m:$)/`
- `/$/.anchorsMatchLineEndings(true)`

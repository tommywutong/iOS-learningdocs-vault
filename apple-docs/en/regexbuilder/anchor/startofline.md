---
title: startOfLine
framework: RegexBuilder
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/anchor/startofline
source_url: 'https://developer.apple.com/documentation/regexbuilder/anchor/startofline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/anchor/startofline.json'
content_hash: 'sha256:e3bbd920bb53ce24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Anchor](../anchor.md)

# startOfLine

<sub>Type Property</sub>

An anchor that matches at the start of a line, including the start of the input string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var startOfLine: Anchor { get }
```

## Discussion

This anchor is equivalent to `^` in regex syntax when the `m` option has been enabled or `anchorsMatchLineEndings(true)` has been called.

For example, the following regexes are all equivalent:

- `Regex { Anchor.startOfLine }`
- `/(?m)^/` or `/(?m:^)/`
- `/^/.anchorsMatchLineEndings(true)`

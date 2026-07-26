---
title: wordBoundary
framework: RegexBuilder
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/anchor/wordboundary
source_url: 'https://developer.apple.com/documentation/regexbuilder/anchor/wordboundary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/anchor/wordboundary.json'
content_hash: 'sha256:1480382c11d51b23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Anchor](../anchor.md)

# wordBoundary

<sub>Type Property</sub>

An anchor that matches at a word boundary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var wordBoundary: Anchor { get }
```

## Discussion

Word boundaries are identified using the Unicode default word boundary algorithm by default. To specify a different word boundary algorithm, use the `wordBoundaryKind(_:)` method.

This anchor is equivalent to `\b` in regex syntax.

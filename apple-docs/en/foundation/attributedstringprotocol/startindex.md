---
title: startIndex
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstringprotocol/startindex
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/startindex.json'
content_hash: 'sha256:813e5f1ed277a18a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# startIndex

<sub>Instance Property</sub>

The position of the first character in a nonempty attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: AttributedString.Index { get }
```

## See Also

### Accessing Indices

- [endIndex](endindex.md) — A string’s past-the-end position — the position one greater than the last valid subscript argument.
- [index(_:offsetByCharacters:)](<index(__offsetbycharacters_).md>) — Returns the position of the character offset a given distance, measured in characters, from a given string index.
- [index(_:offsetByRuns:)](<index(__offsetbyruns_).md>) — Returns the position of the run offset a given number of runs from a given string index.
- [index(_:offsetByUnicodeScalars:)](<index(__offsetbyunicodescalars_).md>) — Returns the position of the Unicode scalar offset a given distance, measured in Unicode scalars, from a given string index.
- [index(afterCharacter:)](<index(aftercharacter_).md>) — Returns the position of the character immediately after another charcter indicated by an index.
- [index(afterRun:)](<index(afterrun_).md>) — Returns the position of the run immediately after a run indicated by an index.
- [index(afterUnicodeScalar:)](<index(afterunicodescalar_).md>) — Returns the position of the Unicode scalar immediately after a Unicode scalar indicated by an index.
- [index(beforeCharacter:)](<index(beforecharacter_).md>) — Returns the position of the character immediately before another charcter indicated by an index.
- [index(beforeRun:)](<index(beforerun_).md>) — Returns the position of the run immediately before a run indicated by an index.
- [index(beforeUnicodeScalar:)](<index(beforeunicodescalar_).md>) — Returns the position of the Unicode scalar immediately before a Unicode scalar indicated by an index.
- [Index](../attributedstring/index.md) — A type that represents the position of a character or code unit within an attributed string.

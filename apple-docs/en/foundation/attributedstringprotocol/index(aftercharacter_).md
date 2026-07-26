---
title: 'index(afterCharacter:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/index(aftercharacter:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/index(aftercharacter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/index%28aftercharacter%3A%29.json'
content_hash: 'sha256:ad3751b7f8c093ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# index(afterCharacter:)

<sub>Instance Method</sub>

Returns the position of the character immediately after another charcter indicated by an index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(afterCharacter i: AttributedString.Index) -> AttributedString.Index
```

## Parameters

- `i` — The index of a character in the attributed string.

## Return Value

The position of the character immediately after the character at index `i`.

## See Also

### Accessing Indices

- [startIndex](startindex.md) — The position of the first character in a nonempty attributed string.
- [endIndex](endindex.md) — A string’s past-the-end position — the position one greater than the last valid subscript argument.
- [index(_:offsetByCharacters:)](<index(__offsetbycharacters_).md>) — Returns the position of the character offset a given distance, measured in characters, from a given string index.
- [index(_:offsetByRuns:)](<index(__offsetbyruns_).md>) — Returns the position of the run offset a given number of runs from a given string index.
- [index(_:offsetByUnicodeScalars:)](<index(__offsetbyunicodescalars_).md>) — Returns the position of the Unicode scalar offset a given distance, measured in Unicode scalars, from a given string index.
- [index(afterRun:)](<index(afterrun_).md>) — Returns the position of the run immediately after a run indicated by an index.
- [index(afterUnicodeScalar:)](<index(afterunicodescalar_).md>) — Returns the position of the Unicode scalar immediately after a Unicode scalar indicated by an index.
- [index(beforeCharacter:)](<index(beforecharacter_).md>) — Returns the position of the character immediately before another charcter indicated by an index.
- [index(beforeRun:)](<index(beforerun_).md>) — Returns the position of the run immediately before a run indicated by an index.
- [index(beforeUnicodeScalar:)](<index(beforeunicodescalar_).md>) — Returns the position of the Unicode scalar immediately before a Unicode scalar indicated by an index.
- [Index](../attributedstring/index.md) — A type that represents the position of a character or code unit within an attributed string.

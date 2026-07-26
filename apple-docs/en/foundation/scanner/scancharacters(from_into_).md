---
title: 'scanCharacters(from:into:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/scanner/scancharacters(from:into:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/scancharacters(from:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/scancharacters%28from%3Ainto%3A%29.json'
content_hash: 'sha256:69f0f6f5aab96ea2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scanCharacters(from:into:)

<sub>Instance Method</sub>

Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scanCharacters(from set: CharacterSet, into result: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

## Parameters

- `set` — The set of characters to scan.

- `result` — Upon return, contains the characters scanned.

## Return Value

[true](../../swift/true.md) if the receiver scanned any characters, otherwise [false](../../swift/false.md).

## Discussion

Invoke this method with `NULL` as `stringValue` to simply scan past a given set of characters.

## See Also

### Scanning Characters and Strings

- [- scanUpToCharactersFromSet:intoString:](<scanuptocharacters(from_into_).md>) — Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_
- [- scanString:intoString:](<scanstring(__into_).md>) — Scans a given string, returning an equivalent string object by reference if a match is found. _(deprecated)_
- [- scanUpToString:intoString:](<scanupto(__into_).md>) — Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_

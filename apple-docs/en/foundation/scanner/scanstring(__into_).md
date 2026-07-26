---
title: 'scanString(_:into:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/scanner/scanstring(_:into:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/scanstring(_:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/scanstring%28_%3Ainto%3A%29.json'
content_hash: 'sha256:34fa824589bedc97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scanString(_:into:)

<sub>Instance Method</sub>

Scans a given string, returning an equivalent string object by reference if a match is found.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scanString(_ string: String, into result: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

## Parameters

- `string` — The string for which to scan at the current scan location.

- `result` — Upon return, if the receiver contains a string equivalent to `string` at the current scan location, contains a string equivalent to `string`.

## Return Value

[true](../../swift/true.md) if `string` matches the characters at the scan location, otherwise [false](../../swift/false.md).

## Discussion

If `string` is present at the current scan location, then the current scan location is advanced to after the string; otherwise the scan location does not change.

Invoke this method with `NULL` as `stringValue` to simply scan past a given string.

## See Also

### Scanning Characters and Strings

- [- scanCharactersFromSet:intoString:](<scancharacters(from_into_).md>) — Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_
- [- scanUpToCharactersFromSet:intoString:](<scanuptocharacters(from_into_).md>) — Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_
- [- scanUpToString:intoString:](<scanupto(__into_).md>) — Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_

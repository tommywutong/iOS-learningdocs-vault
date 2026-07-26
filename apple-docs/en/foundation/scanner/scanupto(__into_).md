---
title: 'scanUpTo(_:into:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/scanner/scanupto(_:into:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/scanupto(_:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/scanupto%28_%3Ainto%3A%29.json'
content_hash: 'sha256:9633a0a21654828c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scanUpTo(_:into:)

<sub>Instance Method</sub>

Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scanUpTo(_ string: String, into result: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

## Parameters

- `string` — The string to scan up to.

- `result` — Upon return, contains any characters that were scanned.

## Return Value

[true](../../swift/true.md) if the receiver scans any characters, otherwise [false](../../swift/false.md).

If the only scanned characters are in the [charactersToBeSkipped](characterstobeskipped.md) character set (which by default is the whitespace and newline character set), then this method returns [false](../../swift/false.md).

## Discussion

If `stopString` is present in the receiver, then on return the scan location is set to the beginning of that string.

If `stopString` is the first string in the receiver, then the method returns [false](../../swift/false.md) and `stringValue` is not changed.

If the search string (`stopString`) isn’t present in the scanner’s source string, the remainder of the source string is put into `stringValue`, the receiver’s `scanLocation` is advanced to the end of the source string, and the method returns [true](../../swift/true.md).

Invoke this method with `NULL` as `stringValue` to simply scan up to a given string.

## See Also

### Scanning Characters and Strings

- [- scanCharactersFromSet:intoString:](<scancharacters(from_into_).md>) — Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_
- [- scanUpToCharactersFromSet:intoString:](<scanuptocharacters(from_into_).md>) — Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_
- [- scanString:intoString:](<scanstring(__into_).md>) — Scans a given string, returning an equivalent string object by reference if a match is found. _(deprecated)_

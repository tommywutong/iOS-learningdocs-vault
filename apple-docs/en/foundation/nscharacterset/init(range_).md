---
title: 'init(range:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscharacterset/init(range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/init(range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/init%28range%3A%29.json'
content_hash: 'sha256:6b6d79edb1c9d890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# init(range:)

<sub>Initializer</sub>

Returns a character set containing characters with Unicode values in a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(range aRange: NSRange)
```

## Parameters

- `aRange` — A range of Unicode values. `aRange.location` is the value of the first character to return; `aRange.location + aRange.length – 1` is the value of the last.

## Return Value

A character set containing characters whose Unicode values are given by `aRange`. If `aRange.length` is `0`, returns an empty character set.

## Discussion

This code excerpt creates a character set object containing the lowercase English alphabetic characters:

```objc
NSRange lcEnglishRange;
NSCharacterSet *lcEnglishLetters;
 
lcEnglishRange.location = (unsigned int)'a';
lcEnglishRange.length = 26;
lcEnglishLetters = [NSCharacterSet characterSetWithRange:lcEnglishRange];
```

## See Also

### Creating a Custom Character Set

- [- initWithCoder:](<init(coder_).md>)
- [+ characterSetWithCharactersInString:](<init(charactersin_).md>) — Returns a character set containing the characters in a given string.
- [NSOpenStepUnicodeReservedBase](../1560803-nsopenstepunicodereservedbase.md) — Specifies lower bound for a Unicode character range reserved for Apple’s corporate use.

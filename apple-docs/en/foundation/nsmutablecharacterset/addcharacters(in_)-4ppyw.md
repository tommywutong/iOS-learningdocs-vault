---
title: 'addCharacters(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablecharacterset/addcharacters(in:)-4ppyw'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecharacterset/addcharacters(in:)-4ppyw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecharacterset/addcharacters%28in%3A%29-4ppyw.json'
content_hash: 'sha256:6805ddce52cfb668'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableCharacterSet](../nsmutablecharacterset.md)

# addCharacters(in:)

<sub>Instance Method</sub>

Adds to the receiver the characters whose Unicode values are in a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addCharacters(in aRange: NSRange)
```

## Parameters

- `aRange` — The range of characters to add. `aRange.location` is the value of the first character to add; `aRange.location + aRange.length – 1` is the value of the last. If `aRange.length` is `0`, this method has no effect.

## Discussion

This code excerpt adds to a character set the lowercase English alphabetic characters:

```objc
NSMutableCharacterSet *aCharacterSet = [[NSMutableCharacterSet alloc] init];
NSRange lcEnglishRange;
 
lcEnglishRange.location = (unsigned int)'a';
lcEnglishRange.length = 26;
[aCharacterSet addCharactersInRange:lcEnglishRange];
```

## See Also

### Related Documentation

- [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i)

### Adding and Removing Characters

- [- removeCharactersInRange:](<removecharacters(in_)-70nqp.md>) — Removes from the receiver the characters whose Unicode values are in a given range.
- [- addCharactersInString:](<addcharacters(in_)-7q02.md>) — Adds to the receiver the characters in a given string.
- [- removeCharactersInString:](<removecharacters(in_)-762gt.md>) — Removes from the receiver the characters in a given string.

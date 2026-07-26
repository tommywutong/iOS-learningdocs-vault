---
title: 'CFStringGetLongCharacterForSurrogatePair(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetlongcharacterforsurrogatepair(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetlongcharacterforsurrogatepair(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetlongcharacterforsurrogatepair%28_%3A_%3A%29.json'
content_hash: 'sha256:30306363f8ffb91c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetLongCharacterForSurrogatePair(_:_:)

<sub>Function</sub>

Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetLongCharacterForSurrogatePair(_ surrogateHigh: UniChar, _ surrogateLow: UniChar) -> UTF32Char
```

## Parameters

- `surrogateHigh` — The high surrogate character.

- `surrogateLow` — The low surrogate character.

## Return Value

A UTF32Char that corresponds to the combination of `surrogateHigh` and `surrogateLow`.

## See Also

### Managing Surrogates

- [CFStringGetSurrogatePairForLongCharacter](<cfstringgetsurrogatepairforlongcharacter(____).md>) — Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.
- [CFStringIsSurrogateHighCharacter](<cfstringissurrogatehighcharacter(__).md>) — Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.
- [CFStringIsSurrogateLowCharacter](<cfstringissurrogatelowcharacter(__).md>) — Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.

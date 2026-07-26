---
title: 'CFStringIsSurrogateLowCharacter(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringissurrogatelowcharacter(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringissurrogatelowcharacter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringissurrogatelowcharacter%28_%3A%29.json'
content_hash: 'sha256:b7646081c730e255'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringIsSurrogateLowCharacter(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringIsSurrogateLowCharacter(_ character: UniChar) -> Bool
```

## Parameters

- `character` — A UTF-16 character.

## Return Value

`true` if `character` is a low character in a surrogate pair, otherwise `false`.

## See Also

### Managing Surrogates

- [CFStringGetLongCharacterForSurrogatePair](<cfstringgetlongcharacterforsurrogatepair(____).md>) — Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.
- [CFStringGetSurrogatePairForLongCharacter](<cfstringgetsurrogatepairforlongcharacter(____).md>) — Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.
- [CFStringIsSurrogateHighCharacter](<cfstringissurrogatehighcharacter(__).md>) — Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.

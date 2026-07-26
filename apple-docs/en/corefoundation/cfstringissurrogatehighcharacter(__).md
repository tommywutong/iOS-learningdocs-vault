---
title: 'CFStringIsSurrogateHighCharacter(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringissurrogatehighcharacter(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringissurrogatehighcharacter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringissurrogatehighcharacter%28_%3A%29.json'
content_hash: 'sha256:882f64a59f7917b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringIsSurrogateHighCharacter(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringIsSurrogateHighCharacter(_ character: UniChar) -> Bool
```

## Parameters

- `character` — A UTF-16 character.

## Return Value

`true` if `character` is a high character in a surrogate pair, otherwise `false`.

## See Also

### Managing Surrogates

- [CFStringGetLongCharacterForSurrogatePair](<cfstringgetlongcharacterforsurrogatepair(____).md>) — Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.
- [CFStringGetSurrogatePairForLongCharacter](<cfstringgetsurrogatepairforlongcharacter(____).md>) — Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.
- [CFStringIsSurrogateLowCharacter](<cfstringissurrogatelowcharacter(__).md>) — Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.

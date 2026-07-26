---
title: 'CFStringGetSurrogatePairForLongCharacter(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetsurrogatepairforlongcharacter(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetsurrogatepairforlongcharacter(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetsurrogatepairforlongcharacter%28_%3A_%3A%29.json'
content_hash: 'sha256:b067f5a34f23093d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetSurrogatePairForLongCharacter(_:_:)

<sub>Function</sub>

Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetSurrogatePairForLongCharacter(_ character: UTF32Char, _ surrogates: UnsafeMutablePointer<UniChar>!) -> Bool
```

## Parameters

- `character` — A UTF-32 character.

- `surrogates` — A buffer to contain the returned surrogate pair. The buffer must have space for at least 2 UTF-16 characters.

## Return Value

`true` if `character` is mapped to a surrogate pair, otherwise `false`.

## See Also

### Managing Surrogates

- [CFStringGetLongCharacterForSurrogatePair](<cfstringgetlongcharacterforsurrogatepair(____).md>) — Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.
- [CFStringIsSurrogateHighCharacter](<cfstringissurrogatehighcharacter(__).md>) — Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.
- [CFStringIsSurrogateLowCharacter](<cfstringissurrogatelowcharacter(__).md>) — Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.

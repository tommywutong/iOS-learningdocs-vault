---
title: 'CFCharacterSetIsSupersetOfSet(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetissupersetofset(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetissupersetofset(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetissupersetofset%28_%3A_%3A%29.json'
content_hash: 'sha256:1856b072202061e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetIsSupersetOfSet(_:_:)

<sub>Function</sub>

Reports whether or not a character set is a superset of another set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetIsSupersetOfSet(_ theSet: CFCharacterSet!, _ theOtherset: CFCharacterSet!) -> Bool
```

## Parameters

- `theSet` — The character set to be checked for the membership of `theOtherSet`.

- `theOtherset` — The character set to be checked whether or not it is a subset of `theSet`.

## Return Value

`true` if `theSet` is a superset of `theOtherSet`, otherwise `false`.

## See Also

### Querying Character Sets

- [CFCharacterSetCreateBitmapRepresentation](<cfcharactersetcreatebitmaprepresentation(____).md>) — Creates a new immutable data with the bitmap representation from the given character set.
- [CFCharacterSetHasMemberInPlane](<cfcharactersethasmemberinplane(____).md>) — Reports whether or not a character set contains at least one member character in the specified plane.
- [CFCharacterSetIsCharacterMember](<cfcharactersetischaractermember(____).md>) — Reports whether or not a given Unicode character is in a character set.
- [CFCharacterSetIsLongCharacterMember](<cfcharactersetislongcharactermember(____).md>) — Reports whether or not a given UTF-32 character is in a character set.

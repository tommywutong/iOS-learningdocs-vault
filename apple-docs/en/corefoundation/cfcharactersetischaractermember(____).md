---
title: 'CFCharacterSetIsCharacterMember(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetischaractermember(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetischaractermember(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetischaractermember%28_%3A_%3A%29.json'
content_hash: 'sha256:eadcf92b5b4e2bf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetIsCharacterMember(_:_:)

<sub>Function</sub>

Reports whether or not a given Unicode character is in a character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetIsCharacterMember(_ theSet: CFCharacterSet!, _ theChar: UniChar) -> Bool
```

## Parameters

- `theSet` — The character set to examine.

- `theChar` — The Unicode character for which to test against the character set. Note that this function takes 16-bit Unicode character value; hence, it does not support access to the non-BMP planes.

## Return Value

`true` if `theSet` contains `theChar`, otherwise `false`.

## See Also

### Querying Character Sets

- [CFCharacterSetCreateBitmapRepresentation](<cfcharactersetcreatebitmaprepresentation(____).md>) — Creates a new immutable data with the bitmap representation from the given character set.
- [CFCharacterSetHasMemberInPlane](<cfcharactersethasmemberinplane(____).md>) — Reports whether or not a character set contains at least one member character in the specified plane.
- [CFCharacterSetIsLongCharacterMember](<cfcharactersetislongcharactermember(____).md>) — Reports whether or not a given UTF-32 character is in a character set.
- [CFCharacterSetIsSupersetOfSet](<cfcharactersetissupersetofset(____).md>) — Reports whether or not a character set is a superset of another set.

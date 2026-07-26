---
title: 'CFCharacterSetHasMemberInPlane(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersethasmemberinplane(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersethasmemberinplane(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersethasmemberinplane%28_%3A_%3A%29.json'
content_hash: 'sha256:071398f7193f5e26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetHasMemberInPlane(_:_:)

<sub>Function</sub>

Reports whether or not a character set contains at least one member character in the specified plane.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetHasMemberInPlane(_ theSet: CFCharacterSet!, _ thePlane: CFIndex) -> Bool
```

## Parameters

- `theSet` — The character set to examine.

- `thePlane` — The plane number to be checked for the membership. The valid value range is from 0 to 16. If the value is outside of the valid plane number range, the behavior is undefined.

## Return Value

`true` if at least one member character is in the specified plane, otherwise `false`.

## See Also

### Querying Character Sets

- [CFCharacterSetCreateBitmapRepresentation](<cfcharactersetcreatebitmaprepresentation(____).md>) — Creates a new immutable data with the bitmap representation from the given character set.
- [CFCharacterSetIsCharacterMember](<cfcharactersetischaractermember(____).md>) — Reports whether or not a given Unicode character is in a character set.
- [CFCharacterSetIsLongCharacterMember](<cfcharactersetislongcharactermember(____).md>) — Reports whether or not a given UTF-32 character is in a character set.
- [CFCharacterSetIsSupersetOfSet](<cfcharactersetissupersetofset(____).md>) — Reports whether or not a character set is a superset of another set.

---
title: familyNames
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/familynames
source_url: 'https://developer.apple.com/documentation/uikit/uifont/familynames'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/familynames.json'
content_hash: 'sha256:a778b2b6cff09e53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# familyNames

<sub>Type Property</sub>

Returns an array of font family names available on the system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class var familyNames: [String] { get }
```

## Return Value

An array of `NSString` objects, each of which contains the name of a font family.

## Discussion

Font family names correspond to the base name of a font, such as `Times New Roman`. You can pass the returned strings to the [+ fontNamesForFamilyName:](<fontnames(forfamilyname_).md>) method to retrieve a list of font names available for that family. You can then use the corresponding font name to retrieve an actual font object.

## See Also

### Getting the Available Font Names

- [+ fontNamesForFamilyName:](<fontnames(forfamilyname_).md>) — Returns an array of font names available in a particular font family.

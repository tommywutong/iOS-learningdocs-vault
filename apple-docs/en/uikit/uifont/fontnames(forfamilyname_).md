---
title: 'fontNames(forFamilyName:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/fontnames(forfamilyname:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/fontnames(forfamilyname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/fontnames%28forfamilyname%3A%29.json'
content_hash: 'sha256:9ae1977ededb56ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# fontNames(forFamilyName:)

<sub>Type Method</sub>

Returns an array of font names available in a particular font family.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func fontNames(forFamilyName familyName: String) -> [String]
```

## Parameters

- `familyName` — The name of the font family. Use the [familyNames](familynames.md) method to get an array of the available font family names on the system.

## Return Value

An array of `NSString` objects, each of which contains a font name associated with the specified family.

## Discussion

You can pass the returned strings as parameters to the [+ fontWithName:size:](<init(name_size_).md>) method to retrieve an actual font object.

## See Also

### Related Documentation

- [+ fontWithName:size:](<init(name_size_).md>) — Creates and returns a font object for the specified font name and size.

### Getting the Available Font Names

- [familyNames](familynames.md) — Returns an array of font family names available on the system.

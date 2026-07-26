---
title: description
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/description
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/description.json'
content_hash: 'sha256:ad7bbb34f3739d9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# description

<sub>Instance Property</sub>

A string that represents the contents of the dictionary, formatted as a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## Discussion

If each key in the dictionary is an `NSString` object, the entries are listed in ascending order by key, otherwise the order in which the entries are listed is undefined.  This property is intended to produce readable output for debugging purposes, not for serializing data. If you want to store dictionary data for later retrieval, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i) and [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## See Also

### Describing a Dictionary

- [descriptionInStringsFileFormat](descriptioninstringsfileformat.md) — A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [- descriptionWithLocale:](<description(withlocale_).md>) — Returns a string object that represents the contents of the dictionary, formatted as a property list.
- [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>) — Returns a string object that represents the contents of the dictionary, formatted as a property list.

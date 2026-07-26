---
title: descriptionInStringsFileFormat
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/descriptioninstringsfileformat
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/descriptioninstringsfileformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/descriptioninstringsfileformat.json'
content_hash: 'sha256:2c242175b8cfe10f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# descriptionInStringsFileFormat

<sub>Instance Property</sub>

A string that represents the contents of the dictionary, formatted in `.strings` file format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var descriptionInStringsFileFormat: String { get }
```

## Discussion

The order in which the entries are listed is undefined.

This method fails unless the dictionary can be represented by a strings resource file. For details, see [String Resources](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6) in [Resource Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i).

## See Also

### Describing a Dictionary

- [description](description.md) — A string that represents the contents of the dictionary, formatted as a property list.
- [- descriptionWithLocale:](<description(withlocale_).md>) — Returns a string object that represents the contents of the dictionary, formatted as a property list.
- [- descriptionWithLocale:indent:](<description(withlocale_indent_).md>) — Returns a string object that represents the contents of the dictionary, formatted as a property list.

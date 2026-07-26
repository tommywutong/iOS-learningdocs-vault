---
title: dictionaryRepresentation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/dictionaryrepresentation
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/dictionaryrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/dictionaryrepresentation.json'
content_hash: 'sha256:8978b535e834de07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# dictionaryRepresentation

<sub>Instance Property</sub>

A dictionary representation of a print-information object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var dictionaryRepresentation: [AnyHashable : Any] { get }
```

## Return Value

A dictionary representation of a `UIPrintInfo` object that can be archived and used to create a new `UIPrintInfo` object. Returns `nil` if no dictionary can be created.

## See Also

### Creating a print info object

- [+ printInfo](<printinfo().md>) — Returns a print-information object initialized with default values.
- [+ printInfoWithDictionary:](<init(dictionary_).md>) — Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [- initWithCoder:](<init(coder_).md>) — Creates a print info object from data in an unarchiver.

---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinfo/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/init%28coder%3A%29.json'
content_hash: 'sha256:450dd6ad9e502c71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# init(coder:)

<sub>Initializer</sub>

Creates a print info object from data in an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## See Also

### Creating a print info object

- [+ printInfo](<printinfo().md>) — Returns a print-information object initialized with default values.
- [+ printInfoWithDictionary:](<init(dictionary_).md>) — Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [dictionaryRepresentation](dictionaryrepresentation.md) — A dictionary representation of a print-information object.

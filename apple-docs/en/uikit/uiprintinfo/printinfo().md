---
title: printInfo()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinfo/printinfo()
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/printinfo()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/printinfo%28%29.json'
content_hash: 'sha256:05080fe46a1e9488'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# printInfo()

<sub>Type Method</sub>

Returns a print-information object initialized with default values.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func printInfo() -> UIPrintInfo
```

## Return Value

An instance of `UIPrintInfo` or `nil` if the object could not be created.

## See Also

### Creating a print info object

- [+ printInfoWithDictionary:](<init(dictionary_).md>) — Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [dictionaryRepresentation](dictionaryrepresentation.md) — A dictionary representation of a print-information object.
- [- initWithCoder:](<init(coder_).md>) — Creates a print info object from data in an unarchiver.

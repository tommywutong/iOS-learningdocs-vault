---
title: 'init(dictionary:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinfo/init(dictionary:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinfo/init(dictionary:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinfo/init%28dictionary%3A%29.json'
content_hash: 'sha256:bc035f685ce8d2a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInfo](../uiprintinfo.md)

# init(dictionary:)

<sub>Initializer</sub>

Returns a print-information object that is initialized with the data in the passed-in dictionary.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(dictionary: [AnyHashable : Any]?)
```

## Parameters

- `dictionary` — A dictionary that contains data to initialize the `UIPrintInfo` object with.

## Return Value

An instance of `UIPrintInfo` or `nil` if the object could not be created.

## Discussion

You use the `dictionary` parameter to initialize a `UIPrintInfo` object with stored print-job information.  Some applications might archive a previous `UIPrintInfo` object and use that for a future print job with this method.

You can later access the dictionary by calling the [dictionaryRepresentation](dictionaryrepresentation.md) method on the `UIPrintInfo` object.

## See Also

### Creating a print info object

- [+ printInfo](<printinfo().md>) — Returns a print-information object initialized with default values.
- [dictionaryRepresentation](dictionaryrepresentation.md) — A dictionary representation of a print-information object.
- [- initWithCoder:](<init(coder_).md>) — Creates a print info object from data in an unarchiver.

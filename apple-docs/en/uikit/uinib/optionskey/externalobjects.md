---
title: externalObjects
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinib/optionskey/externalobjects
source_url: 'https://developer.apple.com/documentation/uikit/uinib/optionskey/externalobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinib/optionskey/externalobjects.json'
content_hash: 'sha256:4666e5e950e7a77d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UINib](../../uinib.md) · [OptionsKey](../optionskey.md)

# externalObjects

<sub>Type Property</sub>

The replacements for any proxy objects in the nib file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let externalObjects: UINib.OptionsKey
```

## Discussion

The value for this key is an [NSDictionary](../../../foundation/nsdictionary.md) object. The keys of the dictionary are the names of any proxy objects in the nib file, and the value for each key is the actual object to use in place of the proxy.

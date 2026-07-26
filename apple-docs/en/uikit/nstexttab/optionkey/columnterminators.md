---
title: columnTerminators
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstexttab/optionkey/columnterminators
source_url: 'https://developer.apple.com/documentation/uikit/nstexttab/optionkey/columnterminators'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexttab/optionkey/columnterminators.json'
content_hash: 'sha256:6ddf6ebc03b25946'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSTextTab](../../nstexttab.md) · [OptionKey](../optionkey.md)

# columnTerminators

<sub>Type Property</sub>

The value is an `NSCharacterSet` object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let columnTerminators: NSTextTab.OptionKey
```

## Discussion

The character set is used to determine the terminating character for a tab column. The tab and newline characters are implied even if they don’t exist in the character set. This attribute is optional.

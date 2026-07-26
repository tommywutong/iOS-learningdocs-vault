---
title: startingItemNumber
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlist/startingitemnumber
source_url: 'https://developer.apple.com/documentation/uikit/nstextlist/startingitemnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlist/startingitemnumber.json'
content_hash: 'sha256:fecb41ff9ffc332c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextList](../nstextlist.md)

# startingItemNumber

<sub>Instance Property</sub>

Sets the starting item number for the text list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var startingItemNumber: Int { get set }
```

## Parameters

- `itemNum` — The item number.

## Discussion

The default value is `1`. This value will be used only for ordered lists, and ignored in other cases.

---
title: setNeedsRevalidate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenusystem/setneedsrevalidate()
source_url: 'https://developer.apple.com/documentation/uikit/uimenusystem/setneedsrevalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenusystem/setneedsrevalidate%28%29.json'
content_hash: 'sha256:7b92d28cc07f71fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuSystem](../uimenusystem.md)

# setNeedsRevalidate()

<sub>Instance Method</sub>

Tells the menu system to validate all of its menus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsRevalidate()
```

## Discussion

Call this method when your app needs to revalidate a menu, such as when the state of your app changes.

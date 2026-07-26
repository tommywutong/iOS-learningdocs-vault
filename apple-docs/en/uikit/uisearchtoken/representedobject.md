---
title: representedObject
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtoken/representedobject
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtoken/representedobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtoken/representedobject.json'
content_hash: 'sha256:948ea57c3e596198'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchToken](../uisearchtoken.md)

# representedObject

<sub>Instance Property</sub>

The object represented by the search token.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var representedObject: Any? { get set }
```

## Discussion

Use this property to keep information required to restore a search from state restoration, paste a search token, or perform the user’s search.

## See Also

### Creating a search token

- [+ tokenWithIcon:text:](<init(icon_text_).md>) — Creates a search token with the specified text and icon (if any).

---
title: whenValues
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiphotosearchsuggestion/whenvalues
source_url: 'https://developer.apple.com/documentation/uikit/uiphotosearchsuggestion/whenvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiphotosearchsuggestion/whenvalues.json'
content_hash: 'sha256:675470e102eefe8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPhotoSearchSuggestion](../uiphotosearchsuggestion.md)

# whenValues

<sub>Instance Property</sub>

Time periods mentioned in the text that can be used to filter photos.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var whenValues: [String] { get }
```

## Discussion

For example, if the user types “photos from last summer,” this array might contain `@[@"last summer"]`.

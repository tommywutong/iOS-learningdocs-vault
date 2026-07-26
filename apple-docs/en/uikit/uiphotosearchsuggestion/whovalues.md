---
title: whoValues
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiphotosearchsuggestion/whovalues
source_url: 'https://developer.apple.com/documentation/uikit/uiphotosearchsuggestion/whovalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiphotosearchsuggestion/whovalues.json'
content_hash: 'sha256:282325838d8cdd52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPhotoSearchSuggestion](../uiphotosearchsuggestion.md)

# whoValues

<sub>Instance Property</sub>

People mentioned in the text that can be used to filter photos.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var whoValues: [String] { get }
```

## Discussion

For example, if the user types “photos with John,” this array might contain `@[@"John"]`.

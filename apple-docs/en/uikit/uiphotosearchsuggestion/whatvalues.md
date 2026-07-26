---
title: whatValues
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiphotosearchsuggestion/whatvalues
source_url: 'https://developer.apple.com/documentation/uikit/uiphotosearchsuggestion/whatvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiphotosearchsuggestion/whatvalues.json'
content_hash: 'sha256:61c1c03bf21f909b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPhotoSearchSuggestion](../uiphotosearchsuggestion.md)

# whatValues

<sub>Instance Property</sub>

Subjects or topics mentioned in the text that can be used to filter photos.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var whatValues: [String] { get }
```

## Discussion

For example, if the user types “photos of food,” this array might contain `@[@"food"]`.

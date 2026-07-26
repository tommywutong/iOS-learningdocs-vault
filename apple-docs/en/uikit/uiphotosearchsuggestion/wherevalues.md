---
title: whereValues
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiphotosearchsuggestion/wherevalues
source_url: 'https://developer.apple.com/documentation/uikit/uiphotosearchsuggestion/wherevalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiphotosearchsuggestion/wherevalues.json'
content_hash: 'sha256:9eda3ffabfdee218'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPhotoSearchSuggestion](../uiphotosearchsuggestion.md)

# whereValues

<sub>Instance Property</sub>

Locations mentioned in the text that can be used to filter photos.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var whereValues: [String] { get }
```

## Discussion

For example, if the user types “pictures from Paris,” this array might contain `@[@"Paris"]`.

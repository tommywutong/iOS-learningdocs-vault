---
title: primaryLanguage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputviewcontroller/primarylanguage
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewcontroller/primarylanguage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewcontroller/primarylanguage.json'
content_hash: 'sha256:ce69778e7d570e8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputViewController](../uiinputviewcontroller.md)

# primaryLanguage

<sub>Instance Property</sub>

The primary language for a custom keyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var primaryLanguage: String? { get set }
```

## Discussion

A BCP 47 language identifier, such as `en-US`. If specified, this value supersedes the `PrimaryLanguage` key in a custom keyboard’s `Info.plist` file.

---
title: 'init(barAppearance:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarappearance/init(barappearance:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarappearance/init(barappearance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarappearance/init%28barappearance%3A%29.json'
content_hash: 'sha256:d483136f6bcc6252'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarAppearance](../uibarappearance.md)

# init(barAppearance:)

<sub>Initializer</sub>

Creates a new bar appearance object by copying relevant data from the specified appearance object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(barAppearance: UIBarAppearance)
```

## Parameters

- `barAppearance` — The bar appearance object from which to copy the relevant properties.

## Return Value

A new bar appearance object containing the relevant properties from the other object.

## Discussion

This method copies over the properties from `barAppearance` that are also relevant to the new bar appearance object.

## See Also

### Creating a custom bar appearance object

- [- initWithIdiom:](<init(idiom_).md>) — Creates a new bar appearance object that targets the specified idiom.
- [- init](<init().md>) — Creates a new bar appearance object containing default values.
- [- initWithCoder:](<init(coder_).md>) — Creates an appearance object from data in an unarchiver.

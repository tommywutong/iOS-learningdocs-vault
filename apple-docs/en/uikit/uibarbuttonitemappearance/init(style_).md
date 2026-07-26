---
title: 'init(style:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitemappearance/init(style:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemappearance/init(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemappearance/init%28style%3A%29.json'
content_hash: 'sha256:bd0e2b78644359bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemAppearance](../uibarbuttonitemappearance.md)

# init(style:)

<sub>Initializer</sub>

Creates an appearance with default values that are appropriate for the specified button style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(style: UIBarButtonItem.Style)
```

## Parameters

- `style` — The button style. UIKit uses this value to configure the default appearance attributes. For a list of possible values, see [Style](../uibarbuttonitem/style-swift.enum.md).

## Return Value

A new bar button item appearance object containing the default appearances for the specified button style.

## See Also

### Creating a bar button item appearance object

- [- init](<init().md>) — Creates an appearance object with default values that are appropriate for a plain button.
- [- initWithCoder:](<init(coder_).md>) — Creates an appearance object from data in an unarchiver.

---
title: defaultContentConfiguration()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlistcell/defaultcontentconfiguration()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/defaultcontentconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlistcell/defaultcontentconfiguration%28%29.json'
content_hash: 'sha256:433d770817d25785'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewListCell](../uicollectionviewlistcell.md)

# defaultContentConfiguration()

<sub>Instance Method</sub>

Retrieves a default list content configuration for the cell’s style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func defaultContentConfiguration() -> UIListContentConfiguration
```

## Return Value

A default list content configuration. The system determines default values for the configuration according to the section where the cell appears.

## Discussion

The default content configuration has preconfigured default styling, but doesn’t contain any content. After you get the default configuration, you assign your content to it, customize any other properties, and assign it to the cell as the current content configuration.

```swift
var content = cell.defaultContentConfiguration()

// Configure content.
content.image = UIImage(systemName: "star")
content.text = "Favorites"

// Customize appearance.
content.imageProperties.tintColor = .purple

cell.contentConfiguration = content
```

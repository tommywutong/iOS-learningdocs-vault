---
title: 'init(traitCollection:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiconfigurationstate-8d7pd/init(traitcollection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationstate-8d7pd/init(traitcollection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationstate-8d7pd/init%28traitcollection%3A%29.json'
content_hash: 'sha256:81726b84566f2d6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationState](../uiconfigurationstate-8d7pd.md)

# init(traitCollection:)

<sub>Initializer</sub>

Creates a view configuration state with the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(traitCollection: UITraitCollection)
```

## Discussion

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [updateConfiguration(using:)](<../uicollectionviewcell/updateconfiguration(using_).md>) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [configurationState](../uicollectionviewcell/configurationstate-4u37h.md) property.

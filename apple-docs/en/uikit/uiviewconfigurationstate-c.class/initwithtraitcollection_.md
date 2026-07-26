---
title: 'initWithTraitCollection:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewconfigurationstate-c.class/initwithtraitcollection:'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewconfigurationstate-c.class/initwithtraitcollection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewconfigurationstate-c.class/initwithtraitcollection%3A.json'
content_hash: 'sha256:e698bde03799f073'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewConfigurationState](../uiviewconfigurationstate-c.class.md)

# initWithTraitCollection:

<sub>Instance Method</sub>

Creates a view configuration state with the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithTraitCollection:(UITraitCollection *) traitCollection;
```

## Discussion

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [updateConfiguration(using:)](<../uicollectionviewcell/updateconfiguration(using_).md>) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [configurationState](../uicollectionviewcell/configurationstate-4u37h.md) property.

## See Also

### Creating a configuration state manually

- [initWithCoder:](initwithcoder_.md) — Creates a view configuration state from data in an unarchiver.

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
doc_path: '/documentation/uikit/uiconfigurationstate-1smq1/initwithtraitcollection:'
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationstate-1smq1/initwithtraitcollection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationstate-1smq1/initwithtraitcollection%3A.json'
content_hash: 'sha256:cbaf8260bc4967cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationState](../uiconfigurationstate-1smq1.md)

# initWithTraitCollection:

<sub>Instance Method</sub>

Creates a configuration state with the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithTraitCollection:(UITraitCollection *) traitCollection;
```

## Discussion

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [updateConfiguration(using:)](<../uicollectionviewcell/updateconfiguration(using_).md>) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [configurationState](../uicollectionviewcell/configurationstate-4u37h.md) property.

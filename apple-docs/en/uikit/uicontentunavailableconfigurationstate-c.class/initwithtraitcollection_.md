---
title: 'initWithTraitCollection:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontentunavailableconfigurationstate-c.class/initwithtraitcollection:'
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableconfigurationstate-c.class/initwithtraitcollection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableconfigurationstate-c.class/initwithtraitcollection%3A.json'
content_hash: 'sha256:92328f6351e10806'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentUnavailableConfigurationState](../uicontentunavailableconfigurationstate-c.class.md)

# initWithTraitCollection:

<sub>Instance Method</sub>

Creates a configuration state with the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithTraitCollection:(UITraitCollection *) traitCollection;
```

## Parameters

- `traitCollection` — The trait collection describing the user interface environment.

## Discussion

Typically, you don’t create a configuration state yourself. To access the current configuration state for a content-unavailable view, read [contentUnavailableConfigurationState](../uiviewcontroller/contentunavailableconfigurationstate-9bvga.md). View controller subclasses can override that property to customize the configuration state returned by the system.

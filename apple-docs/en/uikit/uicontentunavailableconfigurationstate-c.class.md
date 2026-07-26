---
title: UIContentUnavailableConfigurationState
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableconfigurationstate-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableconfigurationstate-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableconfigurationstate-c.class.json'
content_hash: 'sha256:f11c34db2749d61b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentUnavailableConfigurationState

<sub>Class</sub>

An object that encapsulates state for a content-unavailable view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIContentUnavailableConfigurationState : NSObject
```

## Overview

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override [updateContentUnavailableConfigurationUsingState:](uiviewcontroller/updatecontentunavailableconfigurationusingstate_.md) in your view controller subclass and use the state parameter. Outside of this method, you can get a view controller’s configuration state from the [contentUnavailableConfigurationState](uiviewcontroller/contentunavailableconfigurationstate-9bvga.md) property.

You can create your own custom states to add to a content unavailable configuration state by defining a custom state key with [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [UIConfigurationState](uiconfigurationstate-1smq1.md)

## Topics

### Instance Properties

- [searchText](uicontentunavailableconfigurationstate-c.class/searchtext.md) — The search text.
- [traitCollection](uicontentunavailableconfigurationstate-c.class/traitcollection.md) — The traits describing the current user interface environment of the view.

### Instance Methods

- [initWithCoder:](uicontentunavailableconfigurationstate-c.class/initwithcoder_.md) — Creates a configuration state from data in an unarchiver.
- [initWithTraitCollection:](uicontentunavailableconfigurationstate-c.class/initwithtraitcollection_.md) — Creates a configuration state with the specified trait collection.

## See Also

### Unavailable content configurations

- [UIContentUnavailableConfiguration](uicontentunavailableconfiguration-c.class.md) — A content configuration for a content-unavailable view.
- [UIContentUnavailableButtonProperties](uicontentunavailablebuttonproperties.md) — Properties configuring the appearance and behavior of a button in a content-unavailable view.
- [UIContentUnavailableImageProperties](uicontentunavailableimageproperties.md) — Properties configuring the appearance of images in a content-unavailable view.
- [UIContentUnavailableTextProperties](uicontentunavailabletextproperties.md) — Properties configuring the appearance of text in a content-unavailable view.
- [UIContentUnavailableAlignment](uicontentunavailablealignment.md) — Defines the alignment of views in a content-unavailable view.

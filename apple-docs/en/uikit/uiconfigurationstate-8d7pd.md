---
title: UIConfigurationState
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationstate-8d7pd
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationstate-8d7pd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationstate-8d7pd.json'
content_hash: 'sha256:b0c83a14489d6200'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIConfigurationState

<sub>Protocol</sub>

The requirements for an object that encapsulates a view’s state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIConfigurationState
```

## Overview

This protocol provides a blueprint for a configuration state object, which encompasses a trait collection along with all of the common states that affect a view’s appearance. A configuration state encapsulates the inputs that configure a view for any possible state or combination of states. You use a configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [updateConfiguration(using:)](<uicollectionviewcell/updateconfiguration(using_).md>) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [configurationState](uicollectionviewcell/configurationstate-4u37h.md) property.

For more information, see [UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md) and [UICellConfigurationState](uicellconfigurationstate-swift.struct.md).

## Relationships

- **Conforming Types**: [UICellConfigurationState](uicellconfigurationstate-swift.struct.md), [UIContentUnavailableConfigurationState](uicontentunavailableconfigurationstate-swift.struct.md), [UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md)

## Topics

### Managing configuration states

- [traitCollection](uiconfigurationstate-8d7pd/traitcollection.md) — The traits that describe the current layout environment of the view, such as the user interface style and layout direction.
- [subscript(_:)](<uiconfigurationstate-8d7pd/subscript(__).md>) — Accesses custom states by key.

### Creating a configuration state manually

- [init(traitCollection:)](<uiconfigurationstate-8d7pd/init(traitcollection_).md>) — Creates a view configuration state with the specified trait collection.

## See Also

### Configuration states

- [UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md) — A structure that encapsulates a view’s state.
- [UICellConfigurationState](uicellconfigurationstate-swift.struct.md) — A structure that encapsulates a cell’s state.
- [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md) — A key that defines a custom state for a view.

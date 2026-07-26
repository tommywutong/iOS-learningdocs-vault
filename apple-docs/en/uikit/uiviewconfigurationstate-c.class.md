---
title: UIViewConfigurationState
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewconfigurationstate-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uiviewconfigurationstate-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewconfigurationstate-c.class.json'
content_hash: 'sha256:6c2a94dc99199ae2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewConfigurationState

<sub>Class</sub>

A structure that encapsulates a view’s state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIViewConfigurationState : NSObject
```

## Overview

A view configuration state encompasses a trait collection along with all of the common states that affect a view’s appearance — states like selected, focused, or disabled. A view configuration state encapsulates the inputs that configure a view for any possible state or combination of states. You use a view configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [updateConfiguration(using:)](<uicollectionviewcell/updateconfiguration(using_).md>) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [configurationState](uicollectionviewcell/configurationstate-4u37h.md) property.

You can create your own custom states to add to a view configuration state by defining a custom state key using [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UICellConfigurationState](uicellconfigurationstate-c.class.md)

- **Conforms To**: [UIConfigurationState](uiconfigurationstate-1smq1.md)

## Topics

### Managing view configuration states

- [traitCollection](uiviewconfigurationstate-c.class/traitcollection.md) — The traits that describe the current layout environment of the view, such as the user interface style and layout direction.
- [selected](uiviewconfigurationstate-c.class/selected.md) — A Boolean value that indicates whether the view is in a selected state.
- [highlighted](uiviewconfigurationstate-c.class/highlighted.md) — A Boolean value that indicates whether the view is in a highlighted state.
- [focused](uiviewconfigurationstate-c.class/focused.md) — A Boolean value that indicates whether the view is in a focused state.
- [disabled](uiviewconfigurationstate-c.class/disabled.md) — A Boolean value that indicates whether the view is in a disabled state.
- [pinned](uiviewconfigurationstate-c.class/pinned.md) — A Boolean value that indicates whether the view is in a pinned state.

### Creating a configuration state manually

- [initWithTraitCollection:](uiviewconfigurationstate-c.class/initwithtraitcollection_.md) — Creates a view configuration state with the specified trait collection.
- [initWithCoder:](uiviewconfigurationstate-c.class/initwithcoder_.md) — Creates a view configuration state from data in an unarchiver.

## See Also

### Configuration states

- [UICellConfigurationState](uicellconfigurationstate-c.class.md) — An object that encapsulates a cell’s state.
- [UIConfigurationState](uiconfigurationstate-1smq1.md) — The requirements for an object that encapsulates a view’s state.
- [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md) — A key that defines a custom state for a view.

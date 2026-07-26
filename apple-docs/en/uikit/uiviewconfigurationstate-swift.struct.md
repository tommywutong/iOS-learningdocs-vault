---
title: UIViewConfigurationState
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewconfigurationstate-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiviewconfigurationstate-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewconfigurationstate-swift.struct.json'
content_hash: 'sha256:72e0a49fa46077f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewConfigurationState

<sub>Structure</sub>

A structure that encapsulates a view’s state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIViewConfigurationState
```

## Overview

A view configuration state encompasses a trait collection along with all of the common states that affect a view’s appearance — states like selected, focused, or disabled. A view configuration state encapsulates the inputs that configure a view for any possible state or combination of states. You use a view configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [updateConfiguration(using:)](<uicollectionviewcell/updateconfiguration(using_).md>) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [configurationState](uicollectionviewcell/configurationstate-4u37h.md) property.

You can create your own custom states to add to a view configuration state by defining a custom state key using [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [UIConfigurationState](uiconfigurationstate-8d7pd.md)

## Topics

### Managing view configuration states

- [isSelected](uiviewconfigurationstate-swift.struct/isselected.md) — A Boolean value that indicates whether the view is in a selected state.
- [isHighlighted](uiviewconfigurationstate-swift.struct/ishighlighted.md) — A Boolean value that indicates whether the view is in a highlighted state.
- [isFocused](uiviewconfigurationstate-swift.struct/isfocused.md) — A Boolean value that indicates whether the view is in a focused state.
- [isDisabled](uiviewconfigurationstate-swift.struct/isdisabled.md) — A Boolean value that indicates whether the view is in a disabled state.
- [isPinned](uiviewconfigurationstate-swift.struct/ispinned.md) — A Boolean value that indicates whether the view is in a pinned state.

## See Also

### Configuration states

- [UICellConfigurationState](uicellconfigurationstate-swift.struct.md) — A structure that encapsulates a cell’s state.
- [UIConfigurationState](uiconfigurationstate-8d7pd.md) — The requirements for an object that encapsulates a view’s state.
- [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md) — A key that defines a custom state for a view.

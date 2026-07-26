---
title: UIContentUnavailableConfigurationState
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableconfigurationstate-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableconfigurationstate-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableconfigurationstate-swift.struct.json'
content_hash: 'sha256:9df7dc86e31d3aab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentUnavailableConfigurationState

<sub>Structure</sub>

A structure that encapsulates state for a content-unavailable view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIContentUnavailableConfigurationState
```

## Overview

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override [updateContentUnavailableConfiguration(using:)](<uiviewcontroller/updatecontentunavailableconfiguration(using_).md>) in your view controller subclass and use the state parameter. Outside of this method, you can get a view controller’s configuration state from the [contentUnavailableConfigurationState](uiviewcontroller/contentunavailableconfigurationstate-7sczw.md) property.

You can create your own custom states to add to a content-unavailable configuration state by defining a custom state key with [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [UIConfigurationState](uiconfigurationstate-8d7pd.md)

## Topics

### Instance Properties

- [searchText](uicontentunavailableconfigurationstate-swift.struct/searchtext.md) — The search text.

## See Also

### Unavailable content configurations

- [UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md) — A content configuration for a content-unavailable view.

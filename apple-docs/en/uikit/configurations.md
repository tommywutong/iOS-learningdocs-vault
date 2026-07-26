---
title: Configurations
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/configurations
source_url: 'https://developer.apple.com/documentation/uikit/configurations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/configurations.json'
content_hash: 'sha256:cd18373a01de88f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Appearance customization](appearance-customization.md)

# Configurations

<sub>API Collection</sub>

Specify the appearance and content of your views and cells using configurations.

## Overview

Configurations provide a lightweight way to apply content and styling to views without having to manage the rendering of the appearance yourself.

Using a configuration, you can obtain system default styling for a variety of different view states and customize that styling as needed. Then, you assign that configuration to a view that supports configurations, like [UICollectionViewCell](uicollectionviewcell.md), or use it to create a custom content view, like [UIListContentView](uilistcontentview.md). The configuration updates itself when the view’s configuration state changes, causing the view to reflect the new styling for that state.

There are two types of configurations:

- Background configurations, which let you specify the background appearance for a view. For more information, see `UIBackgroundConfiguration`.
- Content configurations, which let you specify content (like image and text) and styling for that content (like tint color and padding). For list-based content, [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md) defines many customization options.

## Topics

### Configuration states

- [UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md) — A structure that encapsulates a view’s state.
- [UICellConfigurationState](uicellconfigurationstate-swift.struct.md) — A structure that encapsulates a cell’s state.
- [UIConfigurationState](uiconfigurationstate-8d7pd.md) — The requirements for an object that encapsulates a view’s state.
- [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md) — A key that defines a custom state for a view.

### Content configurations

- [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md) — A content configuration for a list-based content view.
- [UIListContentView](uilistcontentview.md) — A content view for displaying list-based content.
- [UIContentConfiguration](uicontentconfiguration-9eib5.md) — The requirements for an object that provides the configuration for a content view.
- [UIContentView](uicontentview-5fh3z.md) — The requirements for a content view that you create using a configuration.

### Unavailable content configurations

- [UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md) — A content configuration for a content-unavailable view.
- [UIContentUnavailableConfigurationState](uicontentunavailableconfigurationstate-swift.struct.md) — A structure that encapsulates state for a content-unavailable view.

### Background configurations

- [UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct.md) — A configuration that describes a specific background appearance.

### Color transformers

- [UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct.md) — A transformer that generates a modified output color from an input color.

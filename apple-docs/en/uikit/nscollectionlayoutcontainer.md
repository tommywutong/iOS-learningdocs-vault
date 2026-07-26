---
title: NSCollectionLayoutContainer
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutcontainer
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutcontainer.json'
content_hash: 'sha256:6be4a85527d360a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutContainer

<sub>Protocol</sub>

A protocol used to provide information about the size and content insets of a layout’s container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol NSCollectionLayoutContainer : NSObjectProtocol
```

## Overview

In a section provider, you use the [container](nscollectionlayoutenvironment/container.md) property of the layout environment ([NSCollectionLayoutEnvironment](nscollectionlayoutenvironment.md)) to get information about the container of the layout, such as its size and content insets. Knowing about the container’s size while rendering the layout’s sections helps you make decisions about how to display the layout.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting content size

- [contentSize](nscollectionlayoutcontainer/contentsize.md) — The size of the container before content insets are applied.
- [effectiveContentSize](nscollectionlayoutcontainer/effectivecontentsize.md) — The size of the container after content insets are applied.

### Getting content insets

- [contentInsets](nscollectionlayoutcontainer/contentinsets.md) — The amount of space added around the content of the container to adjust its final size.
- [effectiveContentInsets](nscollectionlayoutcontainer/effectivecontentinsets.md) — The amount of space added around the content of the container to adjust its final size after item content insets are applied.

## See Also

### Size and spacing

- [NSCollectionLayoutDimension](nscollectionlayoutdimension.md) — An individual dimension representing an item’s width or height in a collection view.
- [NSCollectionLayoutSize](nscollectionlayoutsize.md) — The width and the height of an item in a collection view.
- [NSCollectionLayoutSpacing](nscollectionlayoutspacing.md) — An object that defines the space between or around items in a collection view.
- [NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md) — An object that defines the space around the edges of items in a collection view.

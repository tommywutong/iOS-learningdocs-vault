---
title: UIContentView
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentview-3zu2k
source_url: 'https://developer.apple.com/documentation/uikit/uicontentview-3zu2k'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentview-3zu2k.json'
content_hash: 'sha256:d0059e6be497855b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentView

<sub>Protocol</sub>

The requirements for a content view that you create using a configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UIContentView <NSObject>
```

## Overview

This protocol provides a blueprint for a content view object that renders the content and styling that you define with its configuration. The content view’s configuration encapsulates all of the supported properties and behaviors for content view customization. Setting the content view’s [configuration](uicontentview-5fh3z/configuration.md) property applies the new configuration to the view, causing the view to render any updates to its appearance.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIContentUnavailableView](uicontentunavailableview.md), [UIListContentView](uilistcontentview.md)

## Topics

### Managing the content configuration

- [configuration](uicontentview-3zu2k/configuration.md) — The current configuration of the view.

### Determining configuration support

- [supportsConfiguration:](uicontentview-3zu2k/supportsconfiguration_.md) — Determines whether the view is compatible with the provided configuration.

## See Also

### Content configurations

- [UIListContentConfiguration](uilistcontentconfiguration-c.class.md) — A content configuration for a list-based content view.
- [UIListContentView](uilistcontentview.md) — A content view for displaying list-based content.
- [UIContentConfiguration](uicontentconfiguration-2raci.md) — The requirements for an object that provides the configuration for a content view.

---
title: UIContentConfiguration
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentconfiguration-2raci
source_url: 'https://developer.apple.com/documentation/uikit/uicontentconfiguration-2raci'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentconfiguration-2raci.json'
content_hash: 'sha256:b335ff827e8a9816'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentConfiguration

<sub>Protocol</sub>

The requirements for an object that provides the configuration for a content view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UIContentConfiguration <NSObject, NSCopying>
```

## Overview

This protocol provides a blueprint for a content-configuration object, which encompasses default styling and content for a content view. The content configuration encapsulates all of the supported properties and behaviors for content view customization. You use the configuration to create the content view.

## Relationships

- **Inherits From**: [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIContentUnavailableConfiguration](uicontentunavailableconfiguration-c.class.md), [UIListContentConfiguration](uilistcontentconfiguration-c.class.md)

## Topics

### Creating a content configuration

- [makeContentView](uicontentconfiguration-2raci/makecontentview.md) — Creates a new instance of the content view using this configuration.

### Updating a content configuration

- [updatedConfigurationForState:](uicontentconfiguration-2raci/updatedconfigurationforstate_.md) — Generates a configuration for the specified state by applying the configuration’s default values for that state to any properties that you haven’t customized.

## See Also

### Content configurations

- [UIListContentConfiguration](uilistcontentconfiguration-c.class.md) — A content configuration for a list-based content view.
- [UIListContentView](uilistcontentview.md) — A content view for displaying list-based content.
- [UIContentView](uicontentview-3zu2k.md) — The requirements for a content view that you create using a configuration.

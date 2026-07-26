---
title: UIContentConfiguration
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentconfiguration-9eib5
source_url: 'https://developer.apple.com/documentation/uikit/uicontentconfiguration-9eib5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentconfiguration-9eib5.json'
content_hash: 'sha256:086e960461042fd9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentConfiguration

<sub>Protocol</sub>

The requirements for an object that provides the configuration for a content view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIContentConfiguration
```

## Overview

This protocol provides a blueprint for a content-configuration object, which encompasses default styling and content for a content view. The content configuration encapsulates all of the supported properties and behaviors for content view customization. You use the configuration to create the content view.

## Relationships

- **Conforming Types**: [UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md), [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md)

## Topics

### Creating a content configuration

- [makeContentView()](<uicontentconfiguration-9eib5/makecontentview().md>) — Creates a new instance of the content view using this configuration.

### Updating a content configuration

- [updated(for:)](<uicontentconfiguration-9eib5/updated(for_).md>) — Generates a configuration for the specified state by applying the configuration’s default values for that state to any properties that you haven’t customized.

## See Also

### Content configurations

- [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md) — A content configuration for a list-based content view.
- [UIListContentView](uilistcontentview.md) — A content view for displaying list-based content.
- [UIContentView](uicontentview-5fh3z.md) — The requirements for a content view that you create using a configuration.

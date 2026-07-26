---
title: UIActivityItemsConfigurationInteraction
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfigurationinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfigurationinteraction.json'
content_hash: 'sha256:9376bca4fb70da37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityItemsConfigurationInteraction

<sub>Structure</sub>

A structure that describes types of interactions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UIActivityItemsConfigurationInteraction
```

## Overview

Specify which interactions you want the activity view to include in [supportedInteractions](uiactivityitemsconfiguration/supportedinteractions.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Selecting interactions

- [UIActivityItemsConfigurationInteractionCopy](uiactivityitemsconfigurationinteraction/copy.md) — The copy interaction.
- [UIActivityItemsConfigurationInteractionShare](uiactivityitemsconfigurationinteraction/share.md) — The share interaction.

### Creating an interaction type

- [init(_:)](<uiactivityitemsconfigurationinteraction/init(__).md>) — Creates an activity items configuration interaction.
- [init(rawValue:)](<uiactivityitemsconfigurationinteraction/init(rawvalue_).md>) — Creates an activity items configuration interaction with the specified raw value.

## See Also

### Managing supported interactions

- [supportedInteractions](uiactivityitemsconfiguration/supportedinteractions.md) — The types of interactions that the configuration supports.

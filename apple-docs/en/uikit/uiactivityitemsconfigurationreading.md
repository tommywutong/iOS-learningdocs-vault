---
title: UIActivityItemsConfigurationReading
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfigurationreading
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationreading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfigurationreading.json'
content_hash: 'sha256:cbe86d61e96bf4fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityItemsConfigurationReading

<sub>Protocol</sub>

A set of methods adopted by an object so that the object can act as an activity items configuration.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIActivityItemsConfigurationReading : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIActivityItemsConfiguration](uiactivityitemsconfiguration.md)

## Topics

### Managing the Configuration

- [itemProvidersForActivityItemsConfiguration](uiactivityitemsconfigurationreading/itemprovidersforactivityitemsconfiguration.md) — The item providers for the configuration.
- [applicationActivitiesForActivityItemsConfiguration](uiactivityitemsconfigurationreading/applicationactivitiesforactivityitemsconfiguration.md) — The application activities, if any, for the configuration.
- [- activityItemsConfigurationMetadataForKey:](<uiactivityitemsconfigurationreading/activityitemsconfigurationmetadata(key_).md>) — Returns the configuration for the specified metadata key.
- [- activityItemsConfigurationMetadataForItemAtIndex:key:](<uiactivityitemsconfigurationreading/activityitemsconfigurationmetadataforitem(at_key_).md>) — Returns the configuration for a particular item for the specified metadata key.
- [UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey.md) — A structure that defines keys for the metadata associated with an activity items configuration.

### Managing Supported Interactions

- [- activityItemsConfigurationSupportsInteraction:](<uiactivityitemsconfigurationreading/activityitemsconfigurationsupports(interaction_).md>) — Returns a Boolean value that indicates whether the activity items configuration supports the specified type of interaction.
- [UIActivityItemsConfigurationInteraction](uiactivityitemsconfigurationinteraction.md) — A structure that describes types of interactions.

### Managing Previews

- [- activityItemsConfigurationPreviewForItemAtIndex:intent:suggestedSize:](<uiactivityitemsconfigurationreading/activityitemsconfigurationpreviewforitem(at_intent_suggestedsize_).md>) — Returns an activity items configuration preview for the specified item and preview size.
- [UIActivityItemsConfigurationPreviewIntent](uiactivityitemsconfigurationpreviewintent.md) — A structure that specifies the types of activity item previews.

## See Also

### Initializing the activity view controller

- [- initWithActivityItems:applicationActivities:](<uiactivityviewcontroller/init(activityitems_applicationactivities_).md>) — Initializes a new activity view controller object that acts on the specified data.
- [- initWithActivityItemsConfiguration:](<uiactivityviewcontroller/init(activityitemsconfiguration_).md>) — Initializes a new activity view controller object that acts on the specified configuration.
- [UIActivityItemsConfiguration](uiactivityitemsconfiguration.md) — A configuration that allows a responder to export data through a variety of interactions.

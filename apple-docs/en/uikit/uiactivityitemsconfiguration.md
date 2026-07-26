---
title: UIActivityItemsConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfiguration.json'
content_hash: 'sha256:7ec315f3b17c7425'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityItemsConfiguration

<sub>Class</sub>

A configuration that allows a responder to export data through a variety of interactions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIActivityItemsConfiguration
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md)

## Topics

### Creating an activity items configuration

- [- initWithObjects:](<uiactivityitemsconfiguration/init(objects_).md>) — Initializes and returns an activity items configuration with the specified objects.
- [- initWithItemProviders:](<uiactivityitemsconfiguration/init(itemproviders_).md>) — Initializes and returns an activity items configuration with the specified item providers.

### Managing the configuration

- [localObject](uiactivityitemsconfiguration/localobject.md) — A local object that represents the configuration.
- [metadataProvider](uiactivityitemsconfiguration/metadataprovider.md) — A closure that provides metadata for the activity items.
- [perItemMetadataProvider](uiactivityitemsconfiguration/peritemmetadataprovider.md) — A closure that provides metadata for each activity item.
- [applicationActivitiesProvider](uiactivityitemsconfiguration/applicationactivitiesprovider.md) — A closure that provides application acitivites for the activity items.
- [UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey.md) — A structure that defines keys for the metadata associated with an activity items configuration.

### Managing supported interactions

- [supportedInteractions](uiactivityitemsconfiguration/supportedinteractions.md) — The types of interactions that the configuration supports.
- [UIActivityItemsConfigurationInteraction](uiactivityitemsconfigurationinteraction.md) — A structure that describes types of interactions.

### Managing previews

- [previewProvider](uiactivityitemsconfiguration/previewprovider.md) — A closure that provides previews for the activity items.
- [UIActivityItemsConfigurationPreviewIntent](uiactivityitemsconfigurationpreviewintent.md) — A structure that specifies the types of activity item previews.

### Restricting the sharing mode

- [CollaborationModeRestriction](uiactivityviewcontroller/collaborationmoderestriction.md) — An object that disables the sharing mode and optionally displays an alert.
- [UIActivityCollaborationMode](uiactivitycollaborationmode.md) — A value that defines how the system shares an item.

## See Also

### Initializing the activity view controller

- [- initWithActivityItems:applicationActivities:](<uiactivityviewcontroller/init(activityitems_applicationactivities_).md>) — Initializes a new activity view controller object that acts on the specified data.
- [- initWithActivityItemsConfiguration:](<uiactivityviewcontroller/init(activityitemsconfiguration_).md>) — Initializes a new activity view controller object that acts on the specified configuration.
- [UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md) — A set of methods adopted by an object so that the object can act as an activity items configuration.

---
title: UIActivityItemSource
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsource
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsource.json'
content_hash: 'sha256:172bb413320984c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityItemSource

<sub>Protocol</sub>

A set of methods that an activity view controller uses to retrieve the data items to act on.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIActivityItemSource : NSObjectProtocol
```

## Overview

You can use this protocol in situations where you want to provide the data from one of your app’s existing objects instead of creating a separate [UIActivityItemProvider](uiactivityitemprovider.md) object. When implementing this protocol, your object becomes the data provider, providing the view controller with access to the items.

Because the methods of this protocol are executed on your app’s main thread, you should avoid using this protocol in cases where the data objects might take a significant amount of time to create. When creating large data objects, consider using a [UIActivityItemProvider](uiactivityitemprovider.md) object instead.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIActivityItemProvider](uiactivityitemprovider.md)

## Topics

### Getting the data items

- [- activityViewControllerPlaceholderItem:](<uiactivityitemsource/activityviewcontrollerplaceholderitem(__).md>) — Returns the placeholder object for the data.
- [- activityViewController:itemForActivityType:](<uiactivityitemsource/activityviewcontroller(__itemforactivitytype_).md>) — Returns the data object to be acted upon.

### Providing information about the data items

- [- activityViewController:subjectForActivityType:](<uiactivityitemsource/activityviewcontroller(__subjectforactivitytype_).md>) — For activities that support a subject field, returns the subject for the item.
- [- activityViewController:dataTypeIdentifierForActivityType:](<uiactivityitemsource/activityviewcontroller(__datatypeidentifierforactivitytype_).md>) — For items that are provided as data, returns the UTI for the item.
- [- activityViewController:thumbnailImageForActivityType:suggestedSize:](<uiactivityitemsource/activityviewcontroller(__thumbnailimageforactivitytype_suggestedsize_).md>) — For activities that support a preview image, returns a thumbnail preview image for the item.

### Providing metadata for accelerated previews

- [- activityViewControllerLinkMetadata:](<uiactivityitemsource/activityviewcontrollerlinkmetadata(__).md>) — Returns metadata to display in the preview header of the share sheet.

### Instance Methods

- [- activityViewControllerShareRecipients:](<uiactivityitemsource/activityviewcontrollersharerecipients(__).md>)

## See Also

### Services

- [UIActivity](uiactivity.md) — An abstract class that you subclass to implement app-specific services.
- [UIActivityViewController](uiactivityviewcontroller.md) — A view controller that you use to offer standard services from your app.
- [UIActivityItemProvider](uiactivityitemprovider.md) — A proxy for data that passes to an activity view controller.

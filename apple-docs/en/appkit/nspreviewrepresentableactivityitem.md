---
title: NSPreviewRepresentableActivityItem
framework: AppKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/appkit/nspreviewrepresentableactivityitem
source_url: 'https://developer.apple.com/documentation/appkit/nspreviewrepresentableactivityitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nspreviewrepresentableactivityitem.json'
content_hash: 'sha256:ab4d51b2c2604518'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSPreviewRepresentableActivityItem

<sub>Protocol</sub>

An interface you adopt in custom objects that you want to share using the macOS share sheet.

<sub>macOS</sub>

```swift
protocol NSPreviewRepresentableActivityItem : NSObjectProtocol
```

## Overview

Adopt the [NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md) interface in custom types your app makes available for sharing. Use this protocol to specify the item itself and a title and image the share sheet can use to create a preview for your item. To share the item from your app, initialize the [NSSharingServicePicker](nssharingservicepicker.md) object with the object that adopts this protocol.

> [!note] Note
> If your data consists of standard types like strings or images, use an [NSPreviewRepresentingActivityItem](nspreviewrepresentingactivityitem.md) object to specify metadata for those types. If your data consists of URLs, pass them directly to the sharing service picker instead of creating a custom preview item.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSPreviewRepresentingActivityItem](nspreviewrepresentingactivityitem.md)

## Topics

### Providing the Item to Share

- [item](nspreviewrepresentableactivityitem/item.md) — The app-specific item you want to share.

### Providing Metadata About the Item

- [title](nspreviewrepresentableactivityitem/title.md) — A localized string that contains the name of the item.
- [imageProvider](nspreviewrepresentableactivityitem/imageprovider.md) — An object that provides a visual representation of the item.
- [iconProvider](nspreviewrepresentableactivityitem/iconprovider.md) — An object that provides an icon that represents the item’s source.

## See Also

### App Services

- [NSSharingService](nssharingservice.md) — An object that facilitates the sharing of content with social media services, or with apps like Mail or Safari.
- [NSSharingServicePicker](nssharingservicepicker.md) — A list of sharing services that the user can choose from.
- [NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md) — A toolbar item that displays the macOS share sheet.
- [NSServicesMenuRequestor](nsservicesmenurequestor.md) — A set of methods that support interaction with items users can share through a sharing service.
- [NSCloudSharingServiceDelegate](nscloudsharingservicedelegate.md) — A set of methods for responding to the life cycle events of the cloud-sharing service.
- [Services Functions](services-functions.md) — Configure the contents of your app’s Services menu.

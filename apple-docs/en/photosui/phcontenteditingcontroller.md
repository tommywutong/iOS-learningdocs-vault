---
title: PHContentEditingController
framework: PhotosUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.11+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phcontenteditingcontroller
source_url: 'https://developer.apple.com/documentation/photosui/phcontenteditingcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phcontenteditingcontroller.json'
content_hash: 'sha256:6a67c6f2305c7f5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHContentEditingController

<sub>Protocol</sub>

A protocol your custom view controller class implements to provide a user interface for your Photos extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor protocol PHContentEditingController : NSObjectProtocol
```

## Overview

The [PHContentEditingController](phcontenteditingcontroller.md) protocol defines methods you implement in a custom view controller class in order to create a Photos extension. The Photos app hosts your extension’s view controller to provide a user interface for editing photo or video assets.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Working with Adjustment Data

- [- canHandleAdjustmentData:](<phcontenteditingcontroller/canhandle(__).md>) — Asks your extension whether it can continue working with the most recent edit that was made to an asset.

### Performing an Edit

- [- startContentEditingWithInput:placeholderImage:](<phcontenteditingcontroller/startcontentediting(with_placeholderimage_).md>) — Tells your extension that asset data is available for editing.
- [- finishContentEditingWithCompletionHandler:](<phcontenteditingcontroller/finishcontentediting(completionhandler_).md>) — Asks your extension for edited asset data to finish the editing session.

### Canceling an Edit

- [shouldShowCancelConfirmation](phcontenteditingcontroller/shouldshowcancelconfirmation.md) — A Boolean value that determines whether Photos should prompt the user when canceling the editing session.
- [- cancelContentEditing](<phcontenteditingcontroller/cancelcontentediting().md>) — Tells your extension to cancel editing.

## See Also

### Photo Editing Extensions

- [Creating Photo Editing Extensions](../photokit/creating-photo-editing-extensions.md) — Provide custom functionality in the Photos app by bundling an app extension.

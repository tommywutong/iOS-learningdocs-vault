---
title: PHSharedAlbumCustomizationViewController
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photosui/phsharedalbumcustomizationviewcontroller
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumcustomizationviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumcustomizationviewcontroller.json'
content_hash: 'sha256:5c27a9993bea60b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHSharedAlbumCustomizationViewController

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class PHSharedAlbumCustomizationViewController
```

## Overview

This class is used to present the shared album customization view from AppKit-based view controllers.

Only the system photo library is supported, so `albumIdentifier` must be for an album in the system photo library. If `albumIdentifier` is from a different library, showing a customization sheet will fail.

## Relationships

- **Inherits From**: [NSViewController](../appkit/nsviewcontroller.md), [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSEditor](../appkit/nseditor.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSeguePerforming](../appkit/nssegueperforming.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Protocols

- [Delegate](phsharedalbumcustomizationviewcontroller/delegate-swift.protocol.md) _(beta)_

### Initializers

- [- initWithAlbumIdentifier:photoLibrary:](<phsharedalbumcustomizationviewcontroller/init(albumidentifier_photolibrary_).md>) _(beta)_

### Instance Properties

- [albumIdentifier](phsharedalbumcustomizationviewcontroller/albumidentifier.md) — The identifier of the shared album to be customized. _(beta)_
- [delegate](phsharedalbumcustomizationviewcontroller/delegate-swift.property.md) — The delegate to respond to `PHSharedAlbumCustomizationViewController` events. _(beta)_

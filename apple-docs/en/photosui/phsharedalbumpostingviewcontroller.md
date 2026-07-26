---
title: PHSharedAlbumPostingViewController
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photosui/phsharedalbumpostingviewcontroller
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumpostingviewcontroller.json'
content_hash: 'sha256:2e308d6d83fc5282'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHSharedAlbumPostingViewController

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class PHSharedAlbumPostingViewController
```

## Overview

This class is used to present a view for posting assets to a shared album from AppKit-based view controllers.

## Relationships

- **Inherits From**: [NSViewController](../appkit/nsviewcontroller.md), [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSEditor](../appkit/nseditor.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSeguePerforming](../appkit/nssegueperforming.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Protocols

- [Delegate](phsharedalbumpostingviewcontroller/delegate-swift.protocol.md) _(beta)_

### Initializers

- [init(items:defaultAlbumIdentifier:photoLibrary:)](<phsharedalbumpostingviewcontroller/init(items_defaultalbumidentifier_photolibrary_).md>) — Returns a view controller that allows the user to create a new shared album.

### Instance Properties

- [albumIdentifier](phsharedalbumpostingviewcontroller/albumidentifier.md) — The identifier of the shared album that was posted to. _(beta)_
- [delegate](phsharedalbumpostingviewcontroller/delegate-swift.property.md) — The delegate to respond to `PHSharedAlbumPostingViewController` events. _(beta)_

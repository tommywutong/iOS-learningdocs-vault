---
title: PHSharedAlbumCreationViewController
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photosui/phsharedalbumcreationviewcontroller
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumcreationviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumcreationviewcontroller.json'
content_hash: 'sha256:4469beaa04cd2f3f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHSharedAlbumCreationViewController

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class PHSharedAlbumCreationViewController
```

## Overview

This class is used to present the shared album creation view from AppKit-based view controllers.

## Relationships

- **Inherits From**: [NSViewController](../appkit/nsviewcontroller.md), [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSEditor](../appkit/nseditor.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSeguePerforming](../appkit/nssegueperforming.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Protocols

- [Delegate](phsharedalbumcreationviewcontroller/delegate-swift.protocol.md) _(beta)_

### Initializers

- [init(configuration:)](<phsharedalbumcreationviewcontroller/init(configuration_).md>) — Returns a view controller that allows the user to create a new shared album.

### Instance Properties

- [creationResult](phsharedalbumcreationviewcontroller/creationresult.md) — Upon successful album creation, `creationResult` will be non-nil and provide information about the just-created shared album. _(beta)_
- [delegate](phsharedalbumcreationviewcontroller/delegate-swift.property.md) — The delegate to respond to `PHSharedAlbumCreationViewController` events. _(beta)_

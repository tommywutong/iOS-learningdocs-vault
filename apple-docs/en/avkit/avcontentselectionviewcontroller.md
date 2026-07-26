---
title: AVContentSelectionViewController
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentselectionviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avcontentselectionviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentselectionviewcontroller.json'
content_hash: 'sha256:ac1ee0f0c930d01e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVContentSelectionViewController

<sub>Class</sub>

A view controller for providing additional UI to the multiview experience.

<sub>visionOS</sub>

```swift
@MainActor @objc(AVContentSelectionViewController) @preconcurrency class AVContentSelectionViewController
```

## Overview

Subclass or use view controller containment to add additional UI elements to the multiview experience.

## Relationships

- **Inherits From**: [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Creating a view controller.

- [init(coder:)](<avcontentselectionviewcontroller/init(coder_).md>) — Creates a view controller with data in an unarchiver.
- [init(nibName:bundle:)](<avcontentselectionviewcontroller/init(nibname_bundle_).md>) — Creates a view controller with the nib file in the specified bundle.

## See Also

### Providing additional UI

- [contentSelectionViewController](avmultiviewmanager/contentselectionviewcontroller.md) — A view controller that presents a user interface to select additional video content to display.

---
title: UIVideoEditorController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uivideoeditorcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontroller.json'
content_hash: 'sha256:500b5cd457007940'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIVideoEditorController

<sub>Class</sub>

A view controller that manages the system interface for trimming video frames and encoding a previously recorded movie.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIVideoEditorController
```

## Overview

A video editor manages user interactions and provides the filesystem path of the edited movie to your delegate object (see [UIVideoEditorControllerDelegate](uivideoeditorcontrollerdelegate.md)). The features of the [UIVideoEditorController](uivideoeditorcontroller.md) class are available only on devices that support video recording. Use a video editor when your intent is to provide an interface for movie editing. While the [UIImagePickerController](uiimagepickercontroller.md) class also lets a user trim movies, its primary roles are choosing saved pictures and movies, and capturing new pictures and movies.

> [!important] Important
> The `UIVideoEditorController` class supports portrait mode only. This class is intended to be used as-is and doesn’t support subclassing. The view hierarchy for this class is private; don’t modify the view hierarchy. This class doesn’t support modifications to its appearance by use of overlay views.

## Relationships

- **Inherits From**: [UINavigationController](uinavigationcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Managing changes to the video

- [delegate](uivideoeditorcontroller/delegate.md) — The video editor’s delegate object.
- [UIVideoEditorControllerDelegate](uivideoeditorcontrollerdelegate.md) — A set of methods that your delegate object must implement to respond to the video editor.

### Determining editing availability

- [+ canEditVideoAtPath:](<uivideoeditorcontroller/caneditvideo(atpath_).md>) — Returns a Boolean value indicating whether a video file can be edited.

### Configuring the editor

- [videoMaximumDuration](uivideoeditorcontroller/videomaximumduration.md) — The maximum duration, in seconds, permitted for trimmed movies saved by the video editor.
- [videoPath](uivideoeditorcontroller/videopath.md) — The filesystem path to the movie to be loaded by the video editor.
- [videoQuality](uivideoeditorcontroller/videoquality.md) — The video quality to use when saving a trimmed movie.

## See Also

### Images and video

- [UIImagePickerController](uiimagepickercontroller.md) — A view controller that manages the system interfaces for taking pictures, recording movies, and choosing items from the user’s media library.

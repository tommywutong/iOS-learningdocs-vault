---
title: PHPickerViewController
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerviewcontroller
source_url: 'https://developer.apple.com/documentation/photosui/phpickerviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerviewcontroller.json'
content_hash: 'sha256:c55ff61971963c82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHPickerViewController

<sub>Class</sub>

A view controller that provides the user interface for choosing assets from the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class PHPickerViewController
```

## Overview

The `PHPickerViewController` class is an alternative to [UIImagePickerController](../uikit/uiimagepickercontroller.md). `PHPickerViewController` improves stability and reliability, and includes several benefits to developers and users, such as the following:

- Deferred image loading and recovery UI
- Reliable handling of large and complex assets, like RAW and panoramic images
- User-selectable assets that aren’t available for [UIImagePickerController](../uikit/uiimagepickercontroller.md)
- Configuration of the picker to display only Live Photos
- Availability of [PHLivePhoto](../photos/phlivephoto.md) objects without library access
- Stricter validations against invalid inputs

### Observe required viewing standards

As a view controller that the system renders on top of your app, the picker controller requires certain prerequisites for operation that your app needs to observe:

- The picker controller disables user interaction if an app alters its visibility, such as by adjusting the [opacity](../quartzcore/calayer/opacity.md) of its view’s layer. In iOS 17 and later, the picker controller ignores touch events while its opacity is anything other than fully opaque.
- As a system-rendered UI, you can’t subclass [PHPickerViewController](phpickerviewcontroller.md). Its view hierarchy belongs to the system and therefore, the framework provides no access.

## Relationships

- **Inherits From**: [NSViewController](../appkit/nsviewcontroller.md), [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSEditor](../appkit/nseditor.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSeguePerforming](../appkit/nssegueperforming.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Creating a picker

- [init(configuration:)](<phpickerviewcontroller/init(configuration_).md>) — Creates a new picker view controller with the configuration you specify.
- [PHPickerConfiguration](phpickerconfiguration-swift.struct.md) — An object that contains information about how to configure a picker view controller.

### Managing the configuration

- [configuration](phpickerviewcontroller/configuration-17a8p.md) — The configuration you specify when creating the picker.
- [updatePicker(using:)](<phpickerviewcontroller/updatepicker(using_).md>) — Customizes your app’s photo picker according to the given configuration.

### Setting content position and scale

- [- scrollToInitialPosition](<phpickerviewcontroller/scrolltoinitialposition().md>) — Resets the visible photo thumbnails by scrolling the view to the picker’s initial position.
- [- zoomIn](<phpickerviewcontroller/zoomin().md>) — Changes the picker’s content scale by making the photo thumbnails larger in the view.
- [- zoomOut](<phpickerviewcontroller/zoomout().md>) — Changes the picker’s content scale by making the photo thumbnails smaller in the view.

### Responding to user selection

- [delegate](phpickerviewcontroller/delegate-3zqmt.md) — The picker’s delegate object.
- [PHPickerViewControllerDelegate](phpickerviewcontrollerdelegate-5yntc.md) — A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [PHPickerResult](phpickerresult-swift.struct.md) — Types that represent a selected asset from the user’s photo library.

### Deselecting assets

- [- deselectAssetsWithIdentifiers:](<phpickerviewcontroller/deselectassets(withidentifiers_).md>) — Deselects assets that are in a selected state.

### Reordering assets

- [- moveAssetWithIdentifier:afterAssetWithIdentifier:](<phpickerviewcontroller/moveasset(withidentifier_afterassetwithidentifier_).md>) — Reorders assets that are in a selected state.

## See Also

### Photos picker for UIKit, AppKit

- [Selecting Photos and Videos in iOS](../photokit/selecting-photos-and-videos-in-ios.md) — Improve the user experience of finding and selecting assets by using the Photos picker.
- [PHPickerViewControllerDelegate](phpickerviewcontrollerdelegate-5yntc.md) — A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [PHPickerConfiguration](phpickerconfiguration-swift.struct.md) — An object that contains information about how to configure a picker view controller.
- [PHPickerFilter](phpickerfilter-swift.struct.md) — A type that defines the filter to apply to the photo library.
- [PHPickerResult](phpickerresult-swift.struct.md) — Types that represent a selected asset from the user’s photo library.

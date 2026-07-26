---
title: UIFontPickerViewController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontpickerviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller.json'
content_hash: 'sha256:a9486d164de25d7a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFontPickerViewController

<sub>Class</sub>

A view controller that manages the interface for selecting a font that the system provides or the user installs.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIFontPickerViewController
```

## Overview

Use a [UIFontPickerViewController](uifontpickerviewcontroller.md) to provide the user access to all the fonts on their device. Directly querying [UIFont](uifont.md) provides only system fonts, but the user may have additional fonts on their device. When the user selects one of these nonsystem fonts in the font picker, the system grants your app access to the font.

The font picker has several customization options collected into a [Configuration](uifontpickerviewcontroller/configuration-swift.class.md) object. For example, you can set [includeFaces](uifontpickerviewcontroller/configuration-swift.class/includefaces.md) to [true](../swift/true.md) so that the user can select not only the font but a bold or italic face within that font family. Customize the configuration object first, then pass it as an argument in the font picker’s [- initWithConfiguration:](<uifontpickerviewcontroller/init(configuration_).md>) method.

```swift
    func showFontPicker(_ sender: Any) {
        let fontConfig = UIFontPickerViewController.Configuration()
        fontConfig.includeFaces = true
        let fontPicker = UIFontPickerViewController(configuration: fontConfig)
        fontPicker.delegate = self
        self.present(fontPicker, animated: true, completion: nil)
    }
```

When your [UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md) receives [- fontPickerViewControllerDidPickFont:](<uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(__).md>), retrieve information about the user’s selected font from the font picker’s [selectedFontDescriptor](uifontpickerviewcontroller/selectedfontdescriptor.md).

## Relationships

- **Inherits From**: [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Configuring a font picker to display in iOS

- [- initWithConfiguration:](<uifontpickerviewcontroller/init(configuration_).md>) — Creates a controller for a font picker view.
- [configuration](uifontpickerviewcontroller/configuration-swift.property.md) — Settings for fonts the font picker should offer to the user and how to display those fonts.
- [Configuration](uifontpickerviewcontroller/configuration-swift.class.md) — The filters and display settings a font picker view controller uses to set up a font picker.

### Responding to font picker interactions

- [delegate](uifontpickerviewcontroller/delegate.md) — The object that handles messages about the user’s interaction with a font picker.
- [UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md) — A set of optional methods for receiving messages about the user’s interaction with the font picker.
- [selectedFontDescriptor](uifontpickerviewcontroller/selectedfontdescriptor.md) — Information about the font family or face selected by the user in the font picker.

## See Also

### Font picker

- [UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md) — A set of optional methods for receiving messages about the user’s interaction with the font picker.
- [Configuration](uifontpickerviewcontroller/configuration-swift.class.md) — The filters and display settings a font picker view controller uses to set up a font picker.

---
title: UIDocumentPickerExtensionViewController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentpickerextensionviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerextensionviewcontroller.json'
content_hash: 'sha256:35ff2d2d6c4218d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentPickerExtensionViewController

<sub>Class</sub>

The principal class for the Document Picker View Controller extension.

> [!warning] Deprecated
> Use [NSFileProviderExtension](../fileprovider/nsfileproviderextension.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDocumentPickerExtensionViewController
```

## Overview

The Document Picker View Controller extension can perform _import_ and _export_ operations on its own. If you want to support _open_ and _move_ operations, you must pair it with a File Provider extension.

When creating a Document Picker extension, you must subclass [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md) to provide the document picker’s user interface. Your subclass presents a list of available documents and destinations to the user. When the user makes a selection, you trigger the file transfer and pass the selected URL back to the host app.

For more information on creating Document Picker extensions, see [Document Provider](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/FileProvider.html#//apple_ref/doc/uid/TP40014214-CH18).

## Relationships

- **Inherits From**: [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Managing the user interface

- [- dismissGrantingAccessToURL:](<uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to_).md>) — Dismisses the document picker. _(deprecated)_
- [documentPickerMode](uidocumentpickerextensionviewcontroller/documentpickermode.md) — The document picker’s file-transfer operation. (read-only) _(deprecated)_
- [documentStorageURL](uidocumentpickerextensionviewcontroller/documentstorageurl.md) — The root URL for documents provided by the corresponding File Provider extension. (read-only) _(deprecated)_
- [originalURL](uidocumentpickerextensionviewcontroller/originalurl.md) — The URL of the file to be exported. (read-only) _(deprecated)_
- [- prepareForPresentationInMode:](<uidocumentpickerextensionviewcontroller/prepareforpresentation(in_).md>) — Performs any custom configuration of the document picker view controller. _(deprecated)_
- [providerIdentifier](uidocumentpickerextensionviewcontroller/provideridentifier.md) — An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only) _(deprecated)_
- [validTypes](uidocumentpickerextensionviewcontroller/validtypes.md) — An array of valid uniform type identifiers. _(deprecated)_

## See Also

### Document provider

- [NSFileProviderExtension](../fileprovider/nsfileproviderextension.md) — The principal class for the nonreplicated File Provider extension.

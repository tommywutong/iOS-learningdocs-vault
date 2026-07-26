---
title: supportedProjectTypes
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+（10.14 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photosui/phprojectextensioncontroller/supportedprojecttypes
source_url: 'https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/supportedprojecttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectextensioncontroller/supportedprojecttypes.json'
content_hash: 'sha256:79cfc90ab9d2b1a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectExtensionController](../phprojectextensioncontroller.md)

# supportedProjectTypes

<sub>Instance Property</sub>

An array of project types the extension supports.

<sub>macOS</sub>

```swift
optional var supportedProjectTypes: [PHProjectTypeDescription] { get }
```

## Discussion

Extensions can define any number of project types to support. The types appear to users as choices in the Photos app upon initial project creation. To enable this e ntry point into the extension, include the key/value pair `PHProjectExtensionDefinesProjectTypes`: `YES` in the Xcode project’s Info.plist. Once enabled, Photos will ask your extension for its list of supported project types. The option the user selects will be passed to the extension as an attribute of [PHProjectInfo](../phprojectinfo.md).

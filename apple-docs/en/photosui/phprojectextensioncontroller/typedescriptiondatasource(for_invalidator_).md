---
title: 'typeDescriptionDataSource(for:invalidator:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojectextensioncontroller/typedescriptiondatasource(for:invalidator:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/typedescriptiondatasource(for:invalidator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectextensioncontroller/typedescriptiondatasource%28for%3Ainvalidator%3A%29.json'
content_hash: 'sha256:580e3698b9d0dda3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectExtensionController](../phprojectextensioncontroller.md)

# typeDescriptionDataSource(for:invalidator:)

<sub>Instance Method</sub>

Fetches the type description data source to provide the user with more information about the project extension category.

<sub>macOS</sub>

```swift
optional func typeDescriptionDataSource(for category: PHProjectCategory, invalidator: any PHProjectTypeDescriptionInvalidator) -> any PHProjectTypeDescriptionDataSource
```

## Parameters

- `category` — The category in which the user selected the extension.

- `invalidator` — An object used to invalidate information returned from the data source.

## Discussion

Extensions can define any number of project types to support. The types appear to users as choices in the Photos app upon initial project creation. To enable this entry point into the extension, include the key/value pair `PHProjectExtensionDefinesProjectTypes`: `YES` in the Xcode project’s `Info.plist` file. Once enabled, Photos asks your extension for its list of supported project types. The option the user selects is passed to the extension as an attribute of [PHProjectInfo](../phprojectinfo.md).

## See Also

### Tracking the Project Extension Life Cycle

- [- beginProjectWithExtensionContext:projectInfo:completion:](<beginproject(with_projectinfo_completion_).md>) — Provides an opportunity to customize the initial state when the user creates a project using the extension.
- [- finishProjectWithCompletionHandler:](<finishproject(completionhandler_).md>) — Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.
- [- resumeProjectWithExtensionContext:completion:](<resumeproject(with_completion_).md>) — Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.

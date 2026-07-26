---
title: 'beginProject(with:projectInfo:completion:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojectextensioncontroller/beginproject(with:projectinfo:completion:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/beginproject(with:projectinfo:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectextensioncontroller/beginproject%28with%3Aprojectinfo%3Acompletion%3A%29.json'
content_hash: 'sha256:7cf59422843fd3f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectExtensionController](../phprojectextensioncontroller.md)

# beginProject(with:projectInfo:completion:)

<sub>Instance Method</sub>

Provides an opportunity to customize the initial state when the user creates a project using the extension.

<sub>macOS</sub>

```swift
func beginProject(with extensionContext: PHProjectExtensionContext, projectInfo: PHProjectInfo, completion: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>macOS</sub>

```swift
func beginProject(with extensionContext: PHProjectExtensionContext, projectInfo: PHProjectInfo) async throws
```

## Parameters

- `extensionContext` — The extension context with access to the project assets.

- `projectInfo` — Information about the project the extension is called on.

- `completion` — A closure with code you provide that runs on completion.

## See Also

### Tracking the Project Extension Life Cycle

- [- finishProjectWithCompletionHandler:](<finishproject(completionhandler_).md>) — Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.
- [- resumeProjectWithExtensionContext:completion:](<resumeproject(with_completion_).md>) — Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.
- [- typeDescriptionDataSourceForCategory:invalidator:](<typedescriptiondatasource(for_invalidator_).md>) — Fetches the type description data source to provide the user with more information about the project extension category.

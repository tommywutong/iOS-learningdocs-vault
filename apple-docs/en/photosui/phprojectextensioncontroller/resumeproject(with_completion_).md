---
title: 'resumeProject(with:completion:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojectextensioncontroller/resumeproject(with:completion:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/resumeproject(with:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectextensioncontroller/resumeproject%28with%3Acompletion%3A%29.json'
content_hash: 'sha256:2aa2f6c07807b76c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectExtensionController](../phprojectextensioncontroller.md)

# resumeProject(with:completion:)

<sub>Instance Method</sub>

Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.

<sub>macOS</sub>

```swift
func resumeProject(with extensionContext: PHProjectExtensionContext, completion: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>macOS</sub>

```swift
func resumeProject(with extensionContext: PHProjectExtensionContext) async throws
```

## Parameters

- `extensionContext` — The extension context with access to the project assets.

- `completion` — A completion handler to execute upon returning to the extension.

## See Also

### Tracking the Project Extension Life Cycle

- [- beginProjectWithExtensionContext:projectInfo:completion:](<beginproject(with_projectinfo_completion_).md>) — Provides an opportunity to customize the initial state when the user creates a project using the extension.
- [- finishProjectWithCompletionHandler:](<finishproject(completionhandler_).md>) — Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.
- [- typeDescriptionDataSourceForCategory:invalidator:](<typedescriptiondatasource(for_invalidator_).md>) — Fetches the type description data source to provide the user with more information about the project extension category.

---
title: 'finishProject(completionHandler:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojectextensioncontroller/finishproject(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/finishproject(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectextensioncontroller/finishproject%28completionhandler%3A%29.json'
content_hash: 'sha256:85ed437864078036'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectExtensionController](../phprojectextensioncontroller.md)

# finishProject(completionHandler:)

<sub>Instance Method</sub>

Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.

<sub>macOS</sub>

```swift
func finishProject(completionHandler completion: @escaping @Sendable () -> Void)
```

<sub>macOS</sub>

```swift
func finishProject() async
```

## Parameters

- `completion` — A completion handler to execute before exiting the extension.

## See Also

### Tracking the Project Extension Life Cycle

- [- beginProjectWithExtensionContext:projectInfo:completion:](<beginproject(with_projectinfo_completion_).md>) — Provides an opportunity to customize the initial state when the user creates a project using the extension.
- [- resumeProjectWithExtensionContext:completion:](<resumeproject(with_completion_).md>) — Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.
- [- typeDescriptionDataSourceForCategory:invalidator:](<typedescriptiondatasource(for_invalidator_).md>) — Fetches the type description data source to provide the user with more information about the project extension category.

---
title: 'invalidateTypeDescription(for:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojecttypedescriptioninvalidator/invalidatetypedescription(for:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescriptioninvalidator/invalidatetypedescription(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescriptioninvalidator/invalidatetypedescription%28for%3A%29.json'
content_hash: 'sha256:24c0942229707f32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescriptionInvalidator](../phprojecttypedescriptioninvalidator.md)

# invalidateTypeDescription(for:)

<sub>Instance Method</sub>

Invalidates the type description for the given project type.

<sub>macOS</sub>

```swift
func invalidateTypeDescription(for projectType: PHProjectType)
```

## Parameters

- `projectType` — The project type to invalidate.

## Discussion

If you call this method for project types other than [PHProjectTypeUndefined](../phprojecttype/undefined.md), you must implement [- typeDescriptionForProjectType:](<../phprojecttypedescriptiondatasource/typedescription(for_).md>) with functionality for the invalidated project type.

## See Also

### Invalidating a Project Type

- [- invalidateFooterTextForSubtypesOfProjectType:](<invalidatefootertext(forsubtypesof_).md>) — Invalidates the footer text for the subtypes of the given project type.

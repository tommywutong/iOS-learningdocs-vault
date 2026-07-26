---
title: 'invalidateFooterText(forSubtypesOf:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojecttypedescriptioninvalidator/invalidatefootertext(forsubtypesof:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescriptioninvalidator/invalidatefootertext(forsubtypesof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescriptioninvalidator/invalidatefootertext%28forsubtypesof%3A%29.json'
content_hash: 'sha256:b3894a801d5052cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescriptionInvalidator](../phprojecttypedescriptioninvalidator.md)

# invalidateFooterText(forSubtypesOf:)

<sub>Instance Method</sub>

Invalidates the footer text for the subtypes of the given project type.

<sub>macOS</sub>

```swift
func invalidateFooterText(forSubtypesOf projectType: PHProjectType)
```

## Parameters

- `projectType` — The project type whose subtypes you’d like to invalidate.

## Discussion

Use [PHProjectTypeUndefined](../phprojecttype/undefined.md) to invalidate the root-level footer text.

## See Also

### Invalidating a Project Type

- [- invalidateTypeDescriptionForProjectType:](<invalidatetypedescription(for_).md>) — Invalidates the type description for the given project type.

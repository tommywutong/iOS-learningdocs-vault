---
title: 'typeDescription(for:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojecttypedescriptiondatasource/typedescription(for:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource/typedescription(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescriptiondatasource/typedescription%28for%3A%29.json'
content_hash: 'sha256:d9f9a9712a9bd87f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md)

# typeDescription(for:)

<sub>Instance Method</sub>

Provides the updated project type description for previously invalidated project types.

<sub>macOS</sub>

```swift
func typeDescription(for projectType: PHProjectType) -> PHProjectTypeDescription?
```

## Parameters

- `projectType` — The previously invalidated project type whose type description is being requested.

## Return Value

The [PHProjectTypeDescription](../phprojecttypedescription.md) for the given project type.  The returned description’s project type must match the given project type.

## See Also

### Providing Required Fields

- [- subtypesForProjectType:](<subtypes(for_).md>) — Provides the root-level project type descriptions and descriptions of any promised subtypes with [canProvideSubtypes](../phprojecttypedescription/canprovidesubtypes.md) set to `true`.
- [- footerTextForSubtypesOfProjectType:](<footertext(forsubtypesof_).md>) — Provides the footer text for the subtypes of the given project type.

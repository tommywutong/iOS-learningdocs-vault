---
title: 'subtypes(for:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojecttypedescriptiondatasource/subtypes(for:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource/subtypes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescriptiondatasource/subtypes%28for%3A%29.json'
content_hash: 'sha256:60178c95586ededb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md)

# subtypes(for:)

<sub>Instance Method</sub>

Provides the root-level project type descriptions and descriptions of any promised subtypes with [canProvideSubtypes](../phprojecttypedescription/canprovidesubtypes.md) set to `true`.

<sub>macOS</sub>

```swift
func subtypes(for projectType: PHProjectType) -> [PHProjectTypeDescription]
```

## Parameters

- `projectType` — The project type whose subtypes are being requested. The value is [PHProjectTypeUndefined](../phprojecttype/undefined.md) when fetching the root level.

## Return Value

An array of subtype descriptions for the queried project type.

## See Also

### Providing Required Fields

- [- typeDescriptionForProjectType:](<typedescription(for_).md>) — Provides the updated project type description for previously invalidated project types.
- [- footerTextForSubtypesOfProjectType:](<footertext(forsubtypesof_).md>) — Provides the footer text for the subtypes of the given project type.

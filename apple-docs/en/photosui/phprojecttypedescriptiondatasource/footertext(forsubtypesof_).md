---
title: 'footerText(forSubtypesOf:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojecttypedescriptiondatasource/footertext(forsubtypesof:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource/footertext(forsubtypesof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescriptiondatasource/footertext%28forsubtypesof%3A%29.json'
content_hash: 'sha256:ae79aca3e8e0ff76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md)

# footerText(forSubtypesOf:)

<sub>Instance Method</sub>

Provides the footer text for the subtypes of the given project type.

<sub>macOS</sub>

```swift
func footerText(forSubtypesOf projectType: PHProjectType) -> NSAttributedString?
```

## Parameters

- `projectType` — The project type whose footer text is being requested. The value is [PHProjectTypeUndefined](../phprojecttype/undefined.md) when fetching footer text at the root level.

## Return Value

Attributed footer text for the queried project type.

## See Also

### Providing Required Fields

- [- subtypesForProjectType:](<subtypes(for_).md>) — Provides the root-level project type descriptions and descriptions of any promised subtypes with [canProvideSubtypes](../phprojecttypedescription/canprovidesubtypes.md) set to `true`.
- [- typeDescriptionForProjectType:](<typedescription(for_).md>) — Provides the updated project type description for previously invalidated project types.

---
title: sectionContents
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectsection/sectioncontents
source_url: 'https://developer.apple.com/documentation/photosui/phprojectsection/sectioncontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectsection/sectioncontents.json'
content_hash: 'sha256:57ca5671c622457f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectSection](../phprojectsection.md)

# sectionContents

<sub>Instance Property</sub>

An array containing PHProjectionSessionContent objects.

<sub>macOS</sub>

```swift
var sectionContents: [PHProjectSectionContent] { get }
```

## Discussion

The content is ordered by number of elements, from fewest to most. Projects should present only one level of content to the user at a time, because assets are reused within individual content objects.

## See Also

### Determining Section Contents

- [title](title.md) — The optional section title.
- [PHProjectSectionContent](../phprojectsectioncontent.md) — An object containing section elements and layout information for a single level of curation.

---
title: title
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectsection/title
source_url: 'https://developer.apple.com/documentation/photosui/phprojectsection/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectsection/title.json'
content_hash: 'sha256:a4d49121a806117b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectSection](../phprojectsection.md)

# title

<sub>Instance Property</sub>

The optional section title.

<sub>macOS</sub>

```swift
var title: String { get }
```

## Discussion

By default, the title should relate to the content, like the Moment’s name or the geographical location where content was captured. The title can also be an empty string.

## See Also

### Determining Section Contents

- [sectionContents](sectioncontents.md) — An array containing PHProjectionSessionContent objects.
- [PHProjectSectionContent](../phprojectsectioncontent.md) — An object containing section elements and layout information for a single level of curation.

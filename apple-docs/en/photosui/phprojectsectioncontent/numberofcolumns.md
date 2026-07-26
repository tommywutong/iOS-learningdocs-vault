---
title: numberOfColumns
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectsectioncontent/numberofcolumns
source_url: 'https://developer.apple.com/documentation/photosui/phprojectsectioncontent/numberofcolumns'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectsectioncontent/numberofcolumns.json'
content_hash: 'sha256:e6de91dd6b31c52b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectSectionContent](../phprojectsectioncontent.md)

# numberOfColumns

<sub>Instance Property</sub>

The number of columns if section content is displayed in a grid layout.

<sub>macOS</sub>

```swift
var numberOfColumns: Int { get }
```

## Discussion

The number of columns informs the suggested layout of the content, in resolution-independent grid space units. One grid space unit is defined as the width of the project canvas divided by `numberOfColumns`.

## See Also

### Determining Content Properties

- [elements](elements.md) — An array of asset, text, or journal entry elements contained in the content.
- [aspectRatio](aspectratio.md) — The aspect ratio of the full content layout, defined as width over height.
- [cloudAssetIdentifiers](cloudassetidentifiers.md) — An array containing all cloud asset identifiers referenced in the content.
- [backgroundColor](backgroundcolor.md) — The background color of the section content when created from an Apple Print Product.

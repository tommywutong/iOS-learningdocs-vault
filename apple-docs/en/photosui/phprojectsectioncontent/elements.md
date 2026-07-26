---
title: elements
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectsectioncontent/elements
source_url: 'https://developer.apple.com/documentation/photosui/phprojectsectioncontent/elements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectsectioncontent/elements.json'
content_hash: 'sha256:74b20c64ac534831'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectSectionContent](../phprojectsectioncontent.md)

# elements

<sub>Instance Property</sub>

An array of asset, text, or journal entry elements contained in the content.

<sub>macOS</sub>

```swift
var elements: [PHProjectElement] { get }
```

## See Also

### Determining Content Properties

- [numberOfColumns](numberofcolumns.md) — The number of columns if section content is displayed in a grid layout.
- [aspectRatio](aspectratio.md) — The aspect ratio of the full content layout, defined as width over height.
- [cloudAssetIdentifiers](cloudassetidentifiers.md) — An array containing all cloud asset identifiers referenced in the content.
- [backgroundColor](backgroundcolor.md) — The background color of the section content when created from an Apple Print Product.

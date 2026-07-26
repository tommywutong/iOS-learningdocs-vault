---
title: backgroundColor
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectsectioncontent/backgroundcolor
source_url: 'https://developer.apple.com/documentation/photosui/phprojectsectioncontent/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectsectioncontent/backgroundcolor.json'
content_hash: 'sha256:527a1273c3e8074a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectSectionContent](../phprojectsectioncontent.md)

# backgroundColor

<sub>Instance Property</sub>

The background color of the section content when created from an Apple Print Product.

<sub>macOS</sub>

```swift
var backgroundColor: NSColor? { get }
```

## Discussion

This property has no meaning outside of Apple Print Products.

## See Also

### Determining Content Properties

- [elements](elements.md) — An array of asset, text, or journal entry elements contained in the content.
- [numberOfColumns](numberofcolumns.md) — The number of columns if section content is displayed in a grid layout.
- [aspectRatio](aspectratio.md) — The aspect ratio of the full content layout, defined as width over height.
- [cloudAssetIdentifiers](cloudassetidentifiers.md) — An array containing all cloud asset identifiers referenced in the content.

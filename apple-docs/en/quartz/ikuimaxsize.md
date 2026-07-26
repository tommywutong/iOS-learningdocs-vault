---
title: IKUImaxSize
framework: Quartz
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartz/ikuimaxsize
source_url: 'https://developer.apple.com/documentation/quartz/ikuimaxsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartz/ikuimaxsize.json'
content_hash: 'sha256:305a3f49cb06881a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Quartz](../quartz.md)

# IKUImaxSize

<sub>Global Variable</sub>

The maximum size of a filter view.

<sub>macOS</sub>

```swift
let IKUImaxSize: String
```

## Discussion

Controls whose dimensions are the maximum allowable for the filter view.A width or height of `0` indicates that dimension of the view is not restricted. If the size requested is too small, the filter is expected to return a view as small as possible. It is up to the client to verify that the returned view fits into the context.

## See Also

### Constants

- [IKImageBrowserDropOn](ikimagebrowserdropon.md) — Drop the item on the cell.
- [IKImageBrowserDropBefore](ikimagebrowserdropbefore.md) — Drop the item before the cell.
- [IKFilterBrowserDefaultInputImage](ikfilterbrowserdefaultinputimage.md) — The key for the default input image.
- [IKFilterBrowserExcludeCategories](ikfilterbrowserexcludecategories.md) — The key for excluding filter categories.
- [IKFilterBrowserExcludeFilters](ikfilterbrowserexcludefilters.md) — The key for excluding filters.
- [IKFilterBrowserShowCategories](ikfilterbrowsershowcategories.md) — The key for showing categories. The associated value is a  `BOOL` value that determines if the filter browser should show the category list.
- [IKFilterBrowserShowPreview](ikfilterbrowsershowpreview.md) — The associated value is a  `BOOL` value that determines if the filter browser should provide a preview.
- [IKImageBrowserBackgroundColorKey](ikimagebrowserbackgroundcolorkey.md) — A key for the background color of the image browser view.
- [IKImageBrowserCellBackgroundLayer](ikimagebrowsercellbackgroundlayer.md) — Layer displayed in the background.
- [IKImageBrowserCellForegroundLayer](ikimagebrowsercellforegroundlayer.md) — Layer displayed in the foreground.
- [IKImageBrowserCellPlaceHolderLayer](ikimagebrowsercellplaceholderlayer.md) — Layer displayed as a placeholder when an image is not yet available.
- [IKImageBrowserCellSelectionLayer](ikimagebrowsercellselectionlayer.md) — Layer displayed as the selection.
- [IKImageBrowserCellsHighlightedTitleAttributesKey](ikimagebrowsercellshighlightedtitleattributeskey.md) — A key for the highlighted title attribute for an item in the image browser view.
- [IKImageBrowserCellsOutlineColorKey](ikimagebrowsercellsoutlinecolorkey.md) — A key for the outline color for an item in the image browser view.
- [IKImageBrowserCellsSubtitleAttributesKey](ikimagebrowsercellssubtitleattributeskey.md) — A key for  a subtitle attribute for an item in the image browser view.

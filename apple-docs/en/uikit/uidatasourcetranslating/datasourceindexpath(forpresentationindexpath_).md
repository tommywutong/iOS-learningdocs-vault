---
title: 'dataSourceIndexPath(forPresentationIndexPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidatasourcetranslating/datasourceindexpath(forpresentationindexpath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcetranslating/datasourceindexpath(forpresentationindexpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcetranslating/datasourceindexpath%28forpresentationindexpath%3A%29.json'
content_hash: 'sha256:10d04fa17af1d2bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDataSourceTranslating](../uidatasourcetranslating.md)

# dataSourceIndexPath(forPresentationIndexPath:)

<sub>Instance Method</sub>

Translates an index in your presented layout to the equivalent index in your data source object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dataSourceIndexPath(forPresentationIndexPath presentationIndexPath: IndexPath?) -> IndexPath?
```

## Parameters

- `presentationIndexPath` — The index path of an item in your presentation layer.

## Return Value

The index path of the same item in the data source object, or `nil` if the item is no longer in the data source.

## See Also

### Managing item positions

- [- presentationIndexPathForDataSourceIndexPath:](<presentationindexpath(fordatasourceindexpath_).md>) — Translates an index in your data source object to the equivalent index in your presented layout.

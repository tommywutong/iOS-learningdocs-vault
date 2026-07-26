---
title: 'presentationIndexPath(forDataSourceIndexPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidatasourcetranslating/presentationindexpath(fordatasourceindexpath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcetranslating/presentationindexpath(fordatasourceindexpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcetranslating/presentationindexpath%28fordatasourceindexpath%3A%29.json'
content_hash: 'sha256:52b63026ca40e5e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDataSourceTranslating](../uidatasourcetranslating.md)

# presentationIndexPath(forDataSourceIndexPath:)

<sub>Instance Method</sub>

Translates an index in your data source object to the equivalent index in your presented layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func presentationIndexPath(forDataSourceIndexPath dataSourceIndexPath: IndexPath?) -> IndexPath?
```

## Parameters

- `dataSourceIndexPath` — The index path of an item in the data source object.

## Return Value

The index path of the same item in the presentation layer of your object, or `nil` if the item is not in the presentation layer.

## See Also

### Managing item positions

- [- dataSourceIndexPathForPresentationIndexPath:](<datasourceindexpath(forpresentationindexpath_).md>) — Translates an index in your presented layout to the equivalent index in your data source object.

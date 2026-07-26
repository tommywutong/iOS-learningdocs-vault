---
title: 'presentationSectionIndex(forDataSourceSectionIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidatasourcetranslating/presentationsectionindex(fordatasourcesectionindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcetranslating/presentationsectionindex(fordatasourcesectionindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcetranslating/presentationsectionindex%28fordatasourcesectionindex%3A%29.json'
content_hash: 'sha256:c870088efac36b45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDataSourceTranslating](../uidatasourcetranslating.md)

# presentationSectionIndex(forDataSourceSectionIndex:)

<sub>Instance Method</sub>

Translates a section index in your data source object to the equivalent section index in your presented layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func presentationSectionIndex(forDataSourceSectionIndex dataSourceSectionIndex: Int) -> Int
```

## Parameters

- `dataSourceSectionIndex` — The index path of a section in the data source object.

## Return Value

The index path of the same section in the presentation layer of your object, or `nil` if the section is not in the presentation layer.

## See Also

### Managing section positions

- [- dataSourceSectionIndexForPresentationSectionIndex:](<datasourcesectionindex(forpresentationsectionindex_).md>) — Translates a section index in your presented layout to the equivalent section index in your data source object.

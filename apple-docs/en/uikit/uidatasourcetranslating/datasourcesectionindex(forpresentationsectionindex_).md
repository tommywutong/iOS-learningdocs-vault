---
title: 'dataSourceSectionIndex(forPresentationSectionIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidatasourcetranslating/datasourcesectionindex(forpresentationsectionindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcetranslating/datasourcesectionindex(forpresentationsectionindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcetranslating/datasourcesectionindex%28forpresentationsectionindex%3A%29.json'
content_hash: 'sha256:0277bf70cc4e6797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDataSourceTranslating](../uidatasourcetranslating.md)

# dataSourceSectionIndex(forPresentationSectionIndex:)

<sub>Instance Method</sub>

Translates a section index in your presented layout to the equivalent section index in your data source object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dataSourceSectionIndex(forPresentationSectionIndex presentationSectionIndex: Int) -> Int
```

## Parameters

- `presentationSectionIndex` — The index path of a section in your presentation layer.

## Return Value

The index path of the same section in the data source object, or `nil` if the section is no longer in the data source.

## See Also

### Managing section positions

- [- presentationSectionIndexForDataSourceSectionIndex:](<presentationsectionindex(fordatasourcesectionindex_).md>) — Translates a section index in your data source object to the equivalent section index in your presented layout.

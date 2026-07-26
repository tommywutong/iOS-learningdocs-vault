---
title: 'performUsingPresentationValues(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidatasourcetranslating/performusingpresentationvalues(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcetranslating/performusingpresentationvalues(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcetranslating/performusingpresentationvalues%28_%3A%29.json'
content_hash: 'sha256:833da1e85b2a7e2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDataSourceTranslating](../uidatasourcetranslating.md)

# performUsingPresentationValues(_:)

<sub>Instance Method</sub>

Performs actions on the current object using index paths that are relative to the presentation layer of that object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func performUsingPresentationValues(_ actionsToTranslate: () -> Void)
```

## Parameters

- `actionsToTranslate` — A block containing the code you want to execute. Any index paths you specify in this block must be relative to the presentation layer of the object (instead of relative to its data source object). This block takes no parameters and has no return value.

## Discussion

Use this method to perform actions on the current object, when the index paths for those actions are relative to the object’s presentation layer. For example, you might call this method to modify a table view or collection view that has uncommitted updates.

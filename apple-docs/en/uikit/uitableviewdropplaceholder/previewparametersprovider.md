---
title: previewParametersProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropplaceholder/previewparametersprovider
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropplaceholder/previewparametersprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropplaceholder/previewparametersprovider.json'
content_hash: 'sha256:103132ff82378265'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropPlaceholder](../uitableviewdropplaceholder.md)

# previewParametersProvider

<sub>Instance Property</sub>

The handler block that provides the preview parameters for the specified cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var previewParametersProvider: ((UITableViewCell) -> UIDragPreviewParameters?)? { get set }
```

## Discussion

Specify a custom block when you want to provide a custom preview for your placeholder cell. If you don’t specify a block, the table view uses a default preview for the cell.

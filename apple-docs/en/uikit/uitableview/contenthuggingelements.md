---
title: contentHuggingElements
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/contenthuggingelements
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/contenthuggingelements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/contenthuggingelements.json'
content_hash: 'sha256:c033f3e7ffc35722'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# contentHuggingElements

<sub>Instance Property</sub>

A setting that determines which type of items tightly hug their content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentHuggingElements: UITableViewContentHuggingElements { get set }
```

## Discussion

The default value of this property is [UITableViewContentHuggingElementsSectionHeaders](../uitableviewcontenthuggingelements/sectionheaders.md) for plain-style table views in visionOS, and [UITableViewContentHuggingElementsNone](../uitableviewcontenthuggingelements/uitableviewcontenthuggingelementsnone.md) on all other platforms.

When the value of this property is [UITableViewContentHuggingElementsSectionHeaders](../uitableviewcontenthuggingelements/sectionheaders.md), header views tightly hug their content. This means header views don’t stretch to fill the width of the table view if its content’s intrinsic content size is less than the table view’s width.

## See Also

### Managing content-hugging behavior

- [UITableViewContentHuggingElements](../uitableviewcontenthuggingelements.md) — Constants that determine which types of items in a table view tightly hug their content.

---
title: title
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertaction/title
source_url: 'https://developer.apple.com/documentation/uikit/uialertaction/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertaction/title.json'
content_hash: 'sha256:fd5573a2ab77be6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertAction](../uialertaction.md)

# title

<sub>Instance Property</sub>

The title of the action’s button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var title: String? { get }
```

## Discussion

This property is set to the value you specified in the [+ actionWithTitle:style:handler:](<init(title_style_handler_).md>) method.

## See Also

### Getting the action’s attributes

- [style](style-swift.property.md) — The style that applies to the action’s button.
- [enabled](isenabled.md) — A Boolean value indicating whether the action is currently enabled.

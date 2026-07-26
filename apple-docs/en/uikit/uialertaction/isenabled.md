---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertaction/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uialertaction/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertaction/isenabled.json'
content_hash: 'sha256:1b8509ab788fb7a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertAction](../uialertaction.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether the action is currently enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md). Changing the value to [false](../../swift/false.md) causes the action to appear dimmed in the resulting alert. When an action is disabled, taps on the corresponding button have no effect.

## See Also

### Getting the action’s attributes

- [title](title.md) — The title of the action’s button.
- [style](style-swift.property.md) — The style that applies to the action’s button.

---
title: role
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/role-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/role-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/role-swift.property.json'
content_hash: 'sha256:fe29aa394bb6c368'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# role

<sub>Instance Property</sub>

The role of the button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var role: UIButton.Role { get set }
```

## Discussion

Set the [Role](role-swift.enum.md) to define a button as the primary action or the cancel action in a view. Catalyst apps use this role to set the appearance and default key-binding of the buttons.

## See Also

### Specifying the role

- [Role](role-swift.enum.md) — Constants that describe the role of the button.

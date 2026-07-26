---
title: isUserInteractionEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/isuserinteractionenabled
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/isuserinteractionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/isuserinteractionenabled.json'
content_hash: 'sha256:8c14f893aa70e109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# isUserInteractionEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the system ignores and removes user events for this label from the event queue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isUserInteractionEnabled: Bool { get set }
```

## Discussion

[UILabel](../uilabel.md) inherits this property from the [UIView](../uiview.md) parent class. This class changes the default value of this property to [false](../../swift/false.md).

## See Also

### Related Documentation

- [userInteractionEnabled](../uiview/isuserinteractionenabled.md) — A Boolean value that determines whether user events are ignored and removed from the event queue.

### Accessing additional attributes

- [clipsToBounds](../uilabel-clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.

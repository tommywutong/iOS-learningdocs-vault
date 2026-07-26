---
title: 'init(frame:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiswitch/init(frame:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiswitch/init(frame:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswitch/init%28frame%3A%29.json'
content_hash: 'sha256:16811a198e5c052d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwitch](../uiswitch.md)

# init(frame:)

<sub>Initializer</sub>

Creates a switch control.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(frame: CGRect)
```

## Parameters

- `frame` — A rectangle defining the frame of the [UISwitch](../uiswitch.md) object. The size components of this rectangle are ignored.

## Return Value

An initialized [UISwitch](../uiswitch.md) object.

## Discussion

[UISwitch](../uiswitch.md) overrides [- initWithFrame:](<../uiview/init(frame_).md>) and enforces a size appropriate for the control.

## See Also

### Creating a switch

- [- initWithCoder:](<init(coder_).md>) — Creates a switch control from data in an unarchiver.

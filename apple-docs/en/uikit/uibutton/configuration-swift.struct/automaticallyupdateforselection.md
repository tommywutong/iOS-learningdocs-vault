---
title: automaticallyUpdateForSelection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/automaticallyupdateforselection
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/automaticallyupdateforselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/automaticallyupdateforselection.json'
content_hash: 'sha256:c3e2f759ae1a77b3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# automaticallyUpdateForSelection

<sub>Instance Property</sub>

A Boolean value that determines whether the style automatically updates when the button is in a selected state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyUpdateForSelection: Bool { get set }
```

## Discussion

The default value is [true](../../../swift/true.md) for the [plain()](<plain().md>), [gray()](<gray().md>), and [tinted()](<tinted().md>) configurations. Set this value to [false](../../../swift/false.md) to customize the selection behavior.

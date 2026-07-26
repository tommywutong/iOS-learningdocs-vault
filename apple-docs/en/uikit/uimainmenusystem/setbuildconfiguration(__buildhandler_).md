---
title: 'setBuildConfiguration(_:buildHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimainmenusystem/setbuildconfiguration(_:buildhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimainmenusystem/setbuildconfiguration(_:buildhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimainmenusystem/setbuildconfiguration%28_%3Abuildhandler%3A%29.json'
content_hash: 'sha256:b3b69dd3f0481e63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMainMenuSystem](../uimainmenusystem.md)

# setBuildConfiguration(_:buildHandler:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func setBuildConfiguration(_ configuration: UIMainMenuSystem.Configuration, buildHandler: ((any UIMenuBuilder) -> Void)? = nil)
```

## See Also

### Configuring a main menu system

- [Configuration](configuration.md) — A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.

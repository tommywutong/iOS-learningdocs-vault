---
title: isUserAuthenticationEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/systemprotectionmanager-swift.class/isuserauthenticationenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/systemprotectionmanager-swift.class/isuserauthenticationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/systemprotectionmanager-swift.class/isuserauthenticationenabled.json'
content_hash: 'sha256:66632d4f5ae3457c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [SystemProtectionManager](../systemprotectionmanager-swift.class.md)

# isUserAuthenticationEnabled

<sub>Instance Property</sub>

The current status of system user authentication.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isUserAuthenticationEnabled: Bool { get }
```

## Discussion

This value is `true` if the system requires device owner authentication challenges to reveal the content of the scene associated with this manager, `false` otherwise.

> [!note] Note
> This value represents whether protection is enabled in general. It doesn’t indicate the instantaneous state of whether any system-provided shield covers the UI at the moment.

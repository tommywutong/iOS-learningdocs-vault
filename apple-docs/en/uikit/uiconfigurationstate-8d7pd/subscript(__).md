---
title: 'subscript(_:)'
framework: UIKit
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiconfigurationstate-8d7pd/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationstate-8d7pd/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationstate-8d7pd/subscript%28_%3A%29.json'
content_hash: 'sha256:b095a8734744ef73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationState](../uiconfigurationstate-8d7pd.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses custom states by key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
subscript(key: UIConfigurationStateCustomKey) -> AnyHashable? { get set }
```

## See Also

### Managing configuration states

- [traitCollection](traitcollection.md) — The traits that describe the current layout environment of the view, such as the user interface style and layout direction.

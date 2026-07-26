---
title: range
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/context/range
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/context/range'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/context/range.json'
content_hash: 'sha256:4c01f1db7405500c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Context](../context.md)

# range

<sub>Instance Property</sub>

The unique identifier of the context object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var range: NSRange { get }
```

## Discussion

The [Context](../context.md) object initializes the value of this property at creation time. Use this value to identify the context object within your app.

## See Also

### Getting the source text details

- [attributedString](attributedstring.md) — The portion of your view’s text to evaluate.

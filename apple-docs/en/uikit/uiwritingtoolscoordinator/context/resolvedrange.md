---
title: resolvedRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/context/resolvedrange
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/context/resolvedrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/context/resolvedrange.json'
content_hash: 'sha256:6600309cd22f675b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Context](../context.md)

# resolvedRange

<sub>Instance Property</sub>

The actual range of text that Writing Tools might change, which can be different than the range of text you supplied.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var resolvedRange: NSRange { get }
```

## Discussion

After analyzing the text in your context object, Writing Tools sets this property to the portion of [attributedString](attributedstring.md) it might modify. Initially, this property has a location of [NSNotFound](../../../foundation/nsnotfound-4qp9h.md) and a length of `0`, but Writing Tools updates those values before making any changes to the text.

While the Writing Tools operation is active, make sure Writing Tools has exclusive access to the text in this range. Your [Delegate](../delegate-swift.protocol.md) object can make changes to the text as part of incorporating Writing Tools results, but don’t allow changes to come from other sources. For example, don’t let someone edit the text in this range directly until Writing Tools finishes.

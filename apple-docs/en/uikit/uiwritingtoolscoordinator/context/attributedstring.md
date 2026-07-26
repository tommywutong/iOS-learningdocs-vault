---
title: attributedString
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/context/attributedstring
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/context/attributedstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/context/attributedstring.json'
content_hash: 'sha256:4ef5218fa0bc50fb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Context](../context.md)

# attributedString

<sub>Instance Property</sub>

The portion of your view’s text to evaluate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var attributedString: NSAttributedString { get }
```

## Discussion

The `UIWritingToolsCoordinator/Context` object initializes the value of this property at creation time and doesn’t change it during the course of an operation. Instead, it suggests changes to the text in the indicated range and reports those changes to your [Delegate](../delegate-swift.protocol.md) object. Use the methods of your delegate object to integrate those changes back into your view’s text storage.

It’s your responsibility to track the location of this text in your view’s text storage object. When Writing Tools reports changes, it provides range values relative to this string. If you initialize this property with a subset of your view’s content, you must adjust any ranges that Writing Tools provides to get the correct location in your text storage.

## See Also

### Getting the source text details

- [range](range.md) — The unique identifier of the context object.

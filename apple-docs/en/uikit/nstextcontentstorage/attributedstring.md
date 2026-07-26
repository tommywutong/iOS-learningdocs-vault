---
title: attributedString
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentstorage/attributedstring
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstorage/attributedstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstorage/attributedstring.json'
content_hash: 'sha256:3dded48609fb29d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentStorage](../nstextcontentstorage.md)

# attributedString

<sub>Instance Property</sub>

An attributed string that contains the contents of the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var attributedString: NSAttributedString? { get set }
```

## Discussion

The default value of this property is an [NSTextStorage](../nstextstorage.md) object. When you need to change the text in your view, fetch this string and make your changes to it. When making changes, place them in a block and pass them to the [- performEditingTransactionUsingBlock:](<../nstextcontentmanager/performeditingtransaction(__).md>) method. Wrapping changes in an edit transaction gives the rest of the text system an opportunity to respond to those changes. For example, the layout manager uses edit transactions to update the text layout for any content in the visible portion of your view.

If you assign a new value to this property, the object replaces the current string with the one you provide. Don’t set the value of this property to `nil`.

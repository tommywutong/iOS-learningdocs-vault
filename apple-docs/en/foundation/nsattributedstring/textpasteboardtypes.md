---
title: textPasteboardTypes
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.1+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/textpasteboardtypes
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/textpasteboardtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/textpasteboardtypes.json'
content_hash: 'sha256:67e00d0c5375df42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# textPasteboardTypes

<sub>Type Method</sub>

Returns an array of pasteboard types that can be loaded as text.

> [!warning] Deprecated
> Use [textTypes](texttypes.md) instead.

<sub>macOS</sub>

```objc
+ (NSArray *) textPasteboardTypes;
```

## Return Value

An array of `NSString` objects, containing the pasteboard types supported by text classes and those that can be converted to supported pasteboard types through a user-installed filter service.

## Discussion

By default, the list returned by this method includes `NSHTMLPboardType`, `NSRTFPboardType`, `NSRTFDPboardType`, and `NSStringPboardType`.

When creating a subclass of `NSAttributedString` that accepts text data from non-default pasteboard types, override [textUnfilteredPasteboardTypes](textunfilteredpasteboardtypes.md) to notify `NSAttributedString` of the pasteboard types your class supports.

## See Also

### Deprecated Properties

- [textFileTypes](textfiletypes.md) — Returns an array of strings that represent file types that can be loaded as text. _(deprecated)_
- [textUnfilteredFileTypes](textunfilteredfiletypes.md) — Returns an array of strings that represent file types that can be loaded as a text. _(deprecated)_
- [textUnfilteredPasteboardTypes](textunfilteredpasteboardtypes.md) — Returns an array of pasteboard types that can be loaded as text. _(deprecated)_
- [containsAttachments](containsattachments.md) — A Boolean value that indicates whether the attribute string contains any attachment attributes. _(deprecated)_

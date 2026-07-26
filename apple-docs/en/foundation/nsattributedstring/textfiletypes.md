---
title: textFileTypes
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.1+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/textfiletypes
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/textfiletypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/textfiletypes.json'
content_hash: 'sha256:e2e2ea53e76b723c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# textFileTypes

<sub>Type Method</sub>

Returns an array of strings that represent file types that can be loaded as text.

> [!warning] Deprecated
> Use [textTypes](texttypes.md) instead.

<sub>macOS</sub>

```objc
+ (NSArray *) textFileTypes;
```

## Return Value

An array of `NSString` objects, containing file extensions and HFS file types. By default, the list returned by this method includes “`txt`”, “`rtf`”, “`rtfd`”, and “`html`”.

## Discussion

This list includes all file types supported by text classes, plus those types that can be converted to supported file types through a user-installed filter service. The array returned by this method may be passed directly to the `runModalForTypes:` method of [NSOpenPanel](../../appkit/nsopenpanel.md).

When creating a subclass of `NSAttributedString` that accepts text data from non-default file types, override [textUnfilteredTypes](textunfilteredtypes.md) to notify `NSAttributedString` of the file types your class supports.

## See Also

### Deprecated Properties

- [textUnfilteredFileTypes](textunfilteredfiletypes.md) — Returns an array of strings that represent file types that can be loaded as a text. _(deprecated)_
- [textPasteboardTypes](textpasteboardtypes.md) — Returns an array of pasteboard types that can be loaded as text. _(deprecated)_
- [textUnfilteredPasteboardTypes](textunfilteredpasteboardtypes.md) — Returns an array of pasteboard types that can be loaded as text. _(deprecated)_
- [containsAttachments](containsattachments.md) — A Boolean value that indicates whether the attribute string contains any attachment attributes. _(deprecated)_

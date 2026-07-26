---
title: textUnfilteredPasteboardTypes
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.1+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/textunfilteredpasteboardtypes
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/textunfilteredpasteboardtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/textunfilteredpasteboardtypes.json'
content_hash: 'sha256:8ccdfb7ad4056bd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# textUnfilteredPasteboardTypes

<sub>Type Method</sub>

Returns an array of pasteboard types that can be loaded as text.

> [!warning] Deprecated
> Use [textUnfilteredTypes](textunfilteredtypes.md) instead.

<sub>macOS</sub>

```objc
+ (NSArray *) textUnfilteredPasteboardTypes;
```

## Return Value

An array of `NSString` objects, pasteboard types supported by text classes.

## Discussion

This list consists of all pasteboard types supported by text classes, but does not include those that can be converted to supported pasteboard types through a user-installed filter service.

## See Also

### Deprecated Properties

- [textFileTypes](textfiletypes.md) — Returns an array of strings that represent file types that can be loaded as text. _(deprecated)_
- [textUnfilteredFileTypes](textunfilteredfiletypes.md) — Returns an array of strings that represent file types that can be loaded as a text. _(deprecated)_
- [textPasteboardTypes](textpasteboardtypes.md) — Returns an array of pasteboard types that can be loaded as text. _(deprecated)_
- [containsAttachments](containsattachments.md) — A Boolean value that indicates whether the attribute string contains any attachment attributes. _(deprecated)_

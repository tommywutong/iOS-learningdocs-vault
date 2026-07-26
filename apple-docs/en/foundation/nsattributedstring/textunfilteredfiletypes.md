---
title: textUnfilteredFileTypes
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.1+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/textunfilteredfiletypes
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/textunfilteredfiletypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/textunfilteredfiletypes.json'
content_hash: 'sha256:3fe493afdc070824'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# textUnfilteredFileTypes

<sub>Type Method</sub>

Returns an array of strings that represent file types that can be loaded as a text.

> [!warning] Deprecated
> Use [textUnfilteredTypes](textunfilteredtypes.md) instead.

<sub>macOS</sub>

```objc
+ (NSArray *) textUnfilteredFileTypes;
```

## Return Value

An array of `NSString` objects, consisting of all file types supported by text classes, but does not include those types that can be converted to supported file types through a user-installed filter service.

## Discussion

This list consists of all file types supported by text classes, but does not include those types that can be converted to supported file types through a user-installed filter service. In macOS, the array returned by this method may be passed directly to the `runModalForTypes:` method of [NSOpenPanel](../../appkit/nsopenpanel.md).

## See Also

### Deprecated Properties

- [textFileTypes](textfiletypes.md) — Returns an array of strings that represent file types that can be loaded as text. _(deprecated)_
- [textPasteboardTypes](textpasteboardtypes.md) — Returns an array of pasteboard types that can be loaded as text. _(deprecated)_
- [textUnfilteredPasteboardTypes](textunfilteredpasteboardtypes.md) — Returns an array of pasteboard types that can be loaded as text. _(deprecated)_
- [containsAttachments](containsattachments.md) — A Boolean value that indicates whether the attribute string contains any attachment attributes. _(deprecated)_

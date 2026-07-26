---
title: 'setReceiversSpecifier(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmovecommand/setreceiversspecifier(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmovecommand/setreceiversspecifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmovecommand/setreceiversspecifier%28_%3A%29.json'
content_hash: 'sha256:97c1d67e51554ddb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMoveCommand](../nsmovecommand.md)

# setReceiversSpecifier(_:)

<sub>Instance Method</sub>

Sets the receiver’s object specifier.

<sub>Mac Catalyst, macOS</sub>

```swift
func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier?)
```

## Parameters

- `receiversRef` — The receiver’s object specifier.

## Discussion

When evaluated, `receiversRef` indicates the receiver or receivers of the `move` AppleScript command.

This method overrides [receiversSpecifier](../nsscriptcommand/receiversspecifier.md) in [NSScriptCommand](../nsscriptcommand.md). It performs the same function as the overridden method, with a critical difference: it causes the container specifier part of the passed-in object specifier to become the receiver specifier of the command, and the key part of the passed-in object specifier to become the key specifier. If, for example, `receiversRef` is a specifier for `the third paragraph of the first document`, the receiver specifier is `the first document` while the key specifier is `the third paragraph`.

## See Also

### Working with specifiers

- [keySpecifier](keyspecifier.md) — Returns a specifier for the object or objects to be moved.

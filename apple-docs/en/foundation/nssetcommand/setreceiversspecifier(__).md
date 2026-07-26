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
doc_path: '/documentation/foundation/nssetcommand/setreceiversspecifier(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssetcommand/setreceiversspecifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssetcommand/setreceiversspecifier%28_%3A%29.json'
content_hash: 'sha256:6138bb7d22749693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSetCommand](../nssetcommand.md)

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

When the command is executed, it sets attributes or relationships in the objects specified by `receiversRef`.

This method overrides [receiversSpecifier](../nsscriptcommand/receiversspecifier.md) in [NSScriptCommand](../nsscriptcommand.md). It performs the same function as the overridden method, with a critical difference: it causes the container specifier part of the passed-in object specifier to become the receiver specifier of the command, and the key part of the passed-in object specifier to become the key specifier. If, for example, `receiversRef` is a specifier for `the color of the third rectangle`, the receiver specifier is `the third rectangle,` while the key specifier is `the color`.

## See Also

### Working with specifiers

- [keySpecifier](keyspecifier.md) — Returns a specifier that identifies the attribute or relationship that is to be set for the receiver of the `set` AppleScript command.

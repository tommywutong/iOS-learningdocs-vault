---
title: keySpecifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsclonecommand/keyspecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsclonecommand/keyspecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclonecommand/keyspecifier.json'
content_hash: 'sha256:4f6d57beb74e4ee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCloneCommand](../nsclonecommand.md)

# keySpecifier

<sub>Instance Property</sub>

Returns a specifier for the object or objects to be cloned.

<sub>Mac Catalyst, macOS</sub>

```swift
var keySpecifier: NSScriptObjectSpecifier { get }
```

## Return Value

A specifier for the object or objects to be cloned.

## Discussion

For example, the specifier may indicate that a document’s third rectangle should be cloned. The returned specifier is valid only in the context of the `NSCloneCommand` object; for example, if you send the specifier a [containerSpecifier](../nsscriptobjectspecifier/container.md) message, the result is `nil`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### Working with specifiers

- [- setReceiversSpecifier:](<setreceiversspecifier(__).md>) — Sets the receiver’s object specifier;.

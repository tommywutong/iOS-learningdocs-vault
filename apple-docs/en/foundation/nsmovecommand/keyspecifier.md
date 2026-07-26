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
doc_path: /documentation/foundation/nsmovecommand/keyspecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsmovecommand/keyspecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmovecommand/keyspecifier.json'
content_hash: 'sha256:6af8d878167a3258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMoveCommand](../nsmovecommand.md)

# keySpecifier

<sub>Instance Property</sub>

Returns a specifier for the object or objects to be moved.

<sub>Mac Catalyst, macOS</sub>

```swift
var keySpecifier: NSScriptObjectSpecifier { get }
```

## Return Value

A specifier for the object or objects to be moved.

## Discussion

Note that this specifier may be different than the specifier set by [- setReceiversSpecifier:](<setreceiversspecifier(__).md>), which sets the container specifier. For example, for a command such as `move the third circle to the location of the first circle`, the receiver might identify a document (which has a list of graphics), while the key specifier identifies the particular graphic to be moved.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### Working with specifiers

- [- setReceiversSpecifier:](<setreceiversspecifier(__).md>) — Sets the receiver’s object specifier.

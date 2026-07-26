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
doc_path: /documentation/foundation/nsdeletecommand/keyspecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsdeletecommand/keyspecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdeletecommand/keyspecifier.json'
content_hash: 'sha256:b93766929862384f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDeleteCommand](../nsdeletecommand.md)

# keySpecifier

<sub>Instance Property</sub>

Returns a specifier for the object or objects to be deleted.

<sub>Mac Catalyst, macOS</sub>

```swift
var keySpecifier: NSScriptObjectSpecifier { get }
```

## Return Value

A specifier for the object or objects to be deleted.

## Discussion

Note that this may be different than the specifier or specifiers set by [- setReceiversSpecifier:](<setreceiversspecifier(__).md>).

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)

### Working with specifiers

- [- setReceiversSpecifier:](<setreceiversspecifier(__).md>) — Sets the receiver’s object specifier.

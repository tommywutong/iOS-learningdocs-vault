---
title: 'init(commandDescription:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcommand/init(commanddescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/init(commanddescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/init%28commanddescription%3A%29.json'
content_hash: 'sha256:88cac9168fc10b70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# init(commandDescription:)

<sub>Initializer</sub>

Returns an a script command object initialized from the passed command description.

<sub>Mac Catalyst, macOS</sub>

```swift
init(commandDescription commandDef: NSScriptCommandDescription)
```

## Parameters

- `commandDef` — A command description for the command to be created.

## Return Value

A newly initialized instance of `NSScriptCommand` or a subclass.

## Discussion

To make this command object usable, you must set its receiving objects and arguments (if any) after invoking this method.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [receiversSpecifier](receiversspecifier.md) — Sets the object specifier to `receiversSpec` that, when evaluated, indicates the receiver or receivers of the command.
- [arguments](arguments.md) — Sets the arguments of the command to `args`.

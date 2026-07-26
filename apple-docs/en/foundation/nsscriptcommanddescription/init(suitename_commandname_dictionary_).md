---
title: 'init(suiteName:commandName:dictionary:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcommanddescription/init(suitename:commandname:dictionary:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/init(suitename:commandname:dictionary:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/init%28suitename%3Acommandname%3Adictionary%3A%29.json'
content_hash: 'sha256:c72d2ac150bc6555'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# init(suiteName:commandName:dictionary:)

<sub>Initializer</sub>

Initializes and returns a newly allocated instance of `NSScriptCommandDescription`.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(suiteName: String, commandName: String, dictionary commandDeclaration: [AnyHashable : Any]?)
```

## Parameters

- `suiteName` — The name of the suite (in the application’s scriptability information) that the command belongs to. For example, `"AppName Suite"`.

- `commandName` — The name of the script command that this instance describes.

- `commandDeclaration` — A command declaration dictionary of the sort that is valid in script suite property list files. This dictionary provides information about the command such as its argument names and types and return type (if any).

## Return Value

The initialized command description instance. Returns `nil` if the event constant or class name for the command description is missing; also returns `nil` if the return type or argument values are of the wrong type.

## Discussion

This method registers `self` with the application’s global instance of [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md) and also registers all command arguments with the registry.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

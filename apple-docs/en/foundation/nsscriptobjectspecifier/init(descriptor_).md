---
title: 'init(descriptor:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptobjectspecifier/init(descriptor:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/init(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/init%28descriptor%3A%29.json'
content_hash: 'sha256:56783753215e5253'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# init(descriptor:)

<sub>Initializer</sub>

Returns a new object specifier for an Apple event descriptor.

<sub>macOS</sub>

```swift
init?(descriptor: NSAppleEventDescriptor)
```

## Parameters

- `descriptor` — An Apple event descriptor. The descriptor must have the type `typeObjectSpecifier`.

## Return Value

An object specifier, or `nil` if an error occurs.

## Discussion

If `objectSpecifierWithDescriptor:` is invoked and fails during the execution of a script command, information about the error that caused the failure is recorded in `[NSScriptCommand currentCommand]`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

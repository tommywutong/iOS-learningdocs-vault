---
title: 'register(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/register(_:)-5mq91'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/register(_:)-5mq91'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/register%28_%3A%29-5mq91.json'
content_hash: 'sha256:0414a72e7927a943'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# register(_:)

<sub>Instance Method</sub>

Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.

<sub>Mac Catalyst, macOS</sub>

```swift
func register(_ commandDescription: NSScriptCommandDescription)
```

## Discussion

Also registers with the single, shared instance of [NSAppleEventManager](../nsappleeventmanager.md) to handle incoming Apple events that should be handled by the command.

## See Also

### Related Documentation

- [- registerClassDescription:](<register(__)-9aplw.md>) — Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.
- [- loadSuiteWithDictionary:fromBundle:](<loadsuite(with_from_).md>) — Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.

### Getting and Registering Command Descriptions

- [- commandDescriptionsInSuite:](<commanddescriptions(insuite_).md>) — Returns the command descriptions contained in the suite identified by `suiteName`.
- [- commandDescriptionWithAppleEventClass:andAppleEventCode:](<commanddescription(withappleeventclass_andappleeventcode_).md>) — Returns the command description identified by a suite’s four-character Apple event code of the class (`eventClass`) and the four-character Apple event code of the command (`commandCode`).

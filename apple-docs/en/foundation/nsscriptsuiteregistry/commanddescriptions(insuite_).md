---
title: 'commandDescriptions(inSuite:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/commanddescriptions(insuite:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/commanddescriptions(insuite:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/commanddescriptions%28insuite%3A%29.json'
content_hash: 'sha256:2587afb35b0dbf74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# commandDescriptions(inSuite:)

<sub>Instance Method</sub>

Returns the command descriptions contained in the suite identified by `suiteName`.

<sub>Mac Catalyst, macOS</sub>

```swift
func commandDescriptions(inSuite suiteName: String) -> [String : NSScriptCommandDescription]?
```

## Discussion

Each command description (instance of [NSScriptCommandDescription](../nsscriptcommanddescription.md)) in the returned dictionary is identified by command name.

## See Also

### Getting and Registering Command Descriptions

- [- commandDescriptionWithAppleEventClass:andAppleEventCode:](<commanddescription(withappleeventclass_andappleeventcode_).md>) — Returns the command description identified by a suite’s four-character Apple event code of the class (`eventClass`) and the four-character Apple event code of the command (`commandCode`).
- [- registerCommandDescription:](<register(__)-5mq91.md>) — Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.

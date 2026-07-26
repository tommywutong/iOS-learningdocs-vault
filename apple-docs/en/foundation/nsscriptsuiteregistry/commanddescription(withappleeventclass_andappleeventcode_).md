---
title: 'commandDescription(withAppleEventClass:andAppleEventCode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/commanddescription(withappleeventclass:andappleeventcode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/commanddescription(withappleeventclass:andappleeventcode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/commanddescription%28withappleeventclass%3Aandappleeventcode%3A%29.json'
content_hash: 'sha256:42f532f18cd9d685'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# commandDescription(withAppleEventClass:andAppleEventCode:)

<sub>Instance Method</sub>

Returns the command description identified by a suite’s four-character Apple event code of the class (`eventClass`) and the four-character Apple event code of the command (`commandCode`).

<sub>Mac Catalyst, macOS</sub>

```swift
func commandDescription(withAppleEventClass appleEventClassCode: FourCharCode, andAppleEventCode appleEventIDCode: FourCharCode) -> NSScriptCommandDescription?
```

## See Also

### Getting and Registering Command Descriptions

- [- commandDescriptionsInSuite:](<commanddescriptions(insuite_).md>) — Returns the command descriptions contained in the suite identified by `suiteName`.
- [- registerCommandDescription:](<register(__)-5mq91.md>) — Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.

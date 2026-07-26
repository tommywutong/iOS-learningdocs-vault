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
doc_path: '/documentation/foundation/nsscriptsuiteregistry/register(_:)-9aplw'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/register(_:)-9aplw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/register%28_%3A%29-9aplw.json'
content_hash: 'sha256:ec0c583216c0f900'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# register(_:)

<sub>Instance Method</sub>

Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.

<sub>Mac Catalyst, macOS</sub>

```swift
func register(_ classDescription: NSScriptClassDescription)
```

## See Also

### Related Documentation

- [- loadSuiteWithDictionary:fromBundle:](<loadsuite(with_from_).md>) — Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.
- [- registerCommandDescription:](<register(__)-5mq91.md>) — Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.

### Getting and Registering Class Descriptions

- [- classDescriptionsInSuite:](<classdescriptions(insuite_).md>) — Returns the class descriptions contained in the suite identified by `suiteName`.
- [- classDescriptionWithAppleEventCode:](<classdescription(withappleeventcode_).md>) — Returns the class description associated with the given four-character Apple event code, `code`.

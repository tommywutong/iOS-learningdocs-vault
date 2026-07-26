---
title: 'classDescriptions(inSuite:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/classdescriptions(insuite:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/classdescriptions(insuite:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/classdescriptions%28insuite%3A%29.json'
content_hash: 'sha256:ee6d34395b48569c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# classDescriptions(inSuite:)

<sub>Instance Method</sub>

Returns the class descriptions contained in the suite identified by `suiteName`.

<sub>Mac Catalyst, macOS</sub>

```swift
func classDescriptions(inSuite suiteName: String) -> [String : NSScriptClassDescription]?
```

## Discussion

Each class description (instance of [NSScriptClassDescription](../nsscriptclassdescription.md)) in the returned dictionary is identified by class name.

## See Also

### Getting and Registering Class Descriptions

- [- classDescriptionWithAppleEventCode:](<classdescription(withappleeventcode_).md>) — Returns the class description associated with the given four-character Apple event code, `code`.
- [- registerClassDescription:](<register(__)-9aplw.md>) — Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.

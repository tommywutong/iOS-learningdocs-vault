---
title: 'classDescription(withAppleEventCode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/classdescription(withappleeventcode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/classdescription(withappleeventcode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/classdescription%28withappleeventcode%3A%29.json'
content_hash: 'sha256:faac994ff6ad5213'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# classDescription(withAppleEventCode:)

<sub>Instance Method</sub>

Returns the class description associated with the given four-character Apple event code, `code`.

<sub>Mac Catalyst, macOS</sub>

```swift
func classDescription(withAppleEventCode appleEventCode: FourCharCode) -> NSScriptClassDescription?
```

## Discussion

Overriding behavior is important here. Multiple classes can have the same code if the classes have an uninterrupted linear inheritance from one another. For example, if class B is a subclass of A and class C is a subclass of B, and all three classes have the same four-character Apple event code, then this method returns the class description for class C.

## See Also

### Getting and Registering Class Descriptions

- [- classDescriptionsInSuite:](<classdescriptions(insuite_).md>) — Returns the class descriptions contained in the suite identified by `suiteName`.
- [- registerClassDescription:](<register(__)-9aplw.md>) — Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.

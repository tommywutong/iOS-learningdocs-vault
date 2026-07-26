---
title: 'init(suiteName:className:dictionary:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/init(suitename:classname:dictionary:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/init(suitename:classname:dictionary:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/init%28suitename%3Aclassname%3Adictionary%3A%29.json'
content_hash: 'sha256:b444d6c5cac8645b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# init(suiteName:className:dictionary:)

<sub>Initializer</sub>

Initializes and returns a newly allocated instance of `NSScriptClassDescription`.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(suiteName: String, className: String, dictionary classDeclaration: [AnyHashable : Any]?)
```

## Parameters

- `suiteName` — The name of the suite (in the application’s scriptability information) that the class belongs to. For example, `"AppName Suite"`.

- `className` — The name of the class that this instance describes.

- `classDeclaration` — A class declaration dictionary of the sort that is valid in script suite property list files. This dictionary provides information about the class such as its attributes and relationships.

## Return Value

The initialized instance. Returns `nil` if the event code value for the class description itself is missing or is not an `NSString`. Also returns `nil` if the superclass name or any of the subdictionaries of descriptions are not of the right type.

## Discussion

This method registers `self` with the application’s global instance of [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md).

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)

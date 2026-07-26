---
title: 'init(containerClassDescription:containerSpecifier:key:test:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nswhosespecifier/init(containerclassdescription:containerspecifier:key:test:)'
source_url: 'https://developer.apple.com/documentation/foundation/nswhosespecifier/init(containerclassdescription:containerspecifier:key:test:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nswhosespecifier/init%28containerclassdescription%3Acontainerspecifier%3Akey%3Atest%3A%29.json'
content_hash: 'sha256:3bb9946ffe3d0aa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSWhoseSpecifier](../nswhosespecifier.md)

# init(containerClassDescription:containerSpecifier:key:test:)

<sub>Initializer</sub>

Returns an `NSWhoseSpecifier` object initialized with the given attributes.

<sub>Mac Catalyst, macOS</sub>

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, test: NSScriptWhoseTest)
```

## Parameters

- `classDesc` — Class description for the receiver’s container object.

- `container` — An object specifier for the receiver’s container object.

- `property` — The key for the property for which to test.

- `test` — The test condition.

## Return Value

An `NSWhoseSpecifier` object initialized with the given attributes.

## Discussion

Invokes the super class’s [- initWithContainerClassDescription:containerSpecifier:key:](<../nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>) and sets the whose test condition to `test`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

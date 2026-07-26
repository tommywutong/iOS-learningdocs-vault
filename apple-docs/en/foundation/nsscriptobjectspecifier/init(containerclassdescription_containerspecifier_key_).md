---
title: 'init(containerClassDescription:containerSpecifier:key:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/init%28containerclassdescription%3Acontainerspecifier%3Akey%3A%29.json'
content_hash: 'sha256:1f517ce750f3ea78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# init(containerClassDescription:containerSpecifier:key:)

<sub>Initializer</sub>

Returns an `NSScriptObjectSpecifier` object initialized with the given attributes.

<sub>Mac Catalyst, macOS</sub>

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String)
```

## Return Value

An `NSScriptObjectSpecifier` object initialized with container specifier `specifier`, key `key`, and the class description of the object specifier `classDescription`, derived from the value of the specifier’s key.

## Discussion

You should never pass `nil` for the value of `classDescription`. The receiver’s child reference is set to `nil`.

This is the designated initializer for `NSScriptObjectSpecifier`.

## See Also

### Initializing an object specifier

- [- initWithContainerSpecifier:key:](<init(containerspecifier_key_).md>) — Returns an `NSScriptObjectSpecifier` object initialized with a given container specifier  and key.

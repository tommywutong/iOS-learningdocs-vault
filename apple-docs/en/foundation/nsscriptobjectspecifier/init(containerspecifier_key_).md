---
title: 'init(containerSpecifier:key:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptobjectspecifier/init(containerspecifier:key:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/init(containerspecifier:key:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/init%28containerspecifier%3Akey%3A%29.json'
content_hash: 'sha256:9364f450c5c72d0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# init(containerSpecifier:key:)

<sub>Initializer</sub>

Returns an `NSScriptObjectSpecifier` object initialized with a given container specifier  and key.

<sub>Mac Catalyst, macOS</sub>

```swift
convenience init(containerSpecifier container: NSScriptObjectSpecifier, key property: String)
```

## Return Value

An `NSScriptObjectSpecifier` object  initialized with container specifier `specifier` and key `key`.

## Discussion

The class description of the container is set automatically.

## See Also

### Initializing an object specifier

- [- initWithContainerClassDescription:containerSpecifier:key:](<init(containerclassdescription_containerspecifier_key_).md>) — Returns an `NSScriptObjectSpecifier` object initialized with the given attributes.

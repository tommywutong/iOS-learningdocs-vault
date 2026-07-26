---
title: 'init(containerClassDescription:containerSpecifier:key:index:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexspecifier/init(containerclassdescription:containerspecifier:key:index:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexspecifier/init(containerclassdescription:containerspecifier:key:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexspecifier/init%28containerclassdescription%3Acontainerspecifier%3Akey%3Aindex%3A%29.json'
content_hash: 'sha256:5d95648483cba6b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSpecifier](../nsindexspecifier.md)

# init(containerClassDescription:containerSpecifier:key:index:)

<sub>Initializer</sub>

Initializes an allocated [NSIndexSpecifier](../nsindexspecifier.md) object with a class description, container specifier, collection key, and object index.

<sub>Mac Catalyst, macOS</sub>

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, index: Int)
```

## Parameters

- `classDesc` — Description for the container of the collection.

- `container` — Container of the collection.

- `property` — Name of the collection.

- `index` — The object within the `key` collection the index specifier is to identify.

## Return Value

Initialized [NSIndexSpecifier](../nsindexspecifier.md) object with its `index` property set to `objectIndex`.

## Discussion

Invokes the super class’s [- initWithContainerClassDescription:containerSpecifier:key:](<../nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>) method and sets the `index` property of the index specifier to `objectIndex`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

---
title: 'init(containerClassDescription:containerSpecifier:key:start:end:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsrangespecifier/init(containerclassdescription:containerspecifier:key:start:end:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsrangespecifier/init(containerclassdescription:containerspecifier:key:start:end:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrangespecifier/init%28containerclassdescription%3Acontainerspecifier%3Akey%3Astart%3Aend%3A%29.json'
content_hash: 'sha256:e3257ef8809846dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRangeSpecifier](../nsrangespecifier.md)

# init(containerClassDescription:containerSpecifier:key:start:end:)

<sub>Initializer</sub>

Returns a range specifier initialized with the given properties.

<sub>Mac Catalyst, macOS</sub>

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, start startSpec: NSScriptObjectSpecifier?, end endSpec: NSScriptObjectSpecifier?)
```

## Parameters

- `classDesc` — The class description.

- `container` — The container.

- `property` — The property.

- `startSpec` — The object specifier representing the first object of the range.

- `endSpec` — The object specifier representing the last object of the range.

## Return Value

A range specifier initialized with the given properties.

## Discussion

Invokes the super class’s [- initWithContainerClassDescription:containerSpecifier:key:](<../nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>) method and initializes the instance with the object specifiers representing the starting element, `startSpec`, and the ending element, `endSpec`, of a range of elements in the container.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

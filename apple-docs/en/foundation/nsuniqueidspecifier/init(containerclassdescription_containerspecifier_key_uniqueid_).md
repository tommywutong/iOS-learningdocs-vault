---
title: 'init(containerClassDescription:containerSpecifier:key:uniqueID:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuniqueidspecifier/init(containerclassdescription:containerspecifier:key:uniqueid:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/init(containerclassdescription:containerspecifier:key:uniqueid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuniqueidspecifier/init%28containerclassdescription%3Acontainerspecifier%3Akey%3Auniqueid%3A%29.json'
content_hash: 'sha256:8c31fbd10442f0a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUniqueIDSpecifier](../nsuniqueidspecifier.md)

# init(containerClassDescription:containerSpecifier:key:uniqueID:)

<sub>Initializer</sub>

Returns an `NSUniqueIDSpecifier` object, initialized with the given arguments.

<sub>Mac Catalyst, macOS</sub>

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, uniqueID: Any)
```

## Parameters

- `classDesc` — The class description for the new object.

- `container` — The container for the new object.

- `property` — The property for the new object.

- `uniqueID` — The unique ID for the new object. `uniqueID` must be an instance of `NSNumber` or `NSString`. The type should match the declared type of the attribute of the specified scriptable class whose four-character code is `'ID  '`.

## Return Value

An `NSUniqueIDSpecifier` object, initialized with the given arguments.

## Discussion

Invokes the super class’s [- initWithContainerClassDescription:containerSpecifier:key:](<../nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>) method and sets the ID to `uniqueID`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

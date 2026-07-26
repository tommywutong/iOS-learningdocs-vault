---
title: defaultSubcontainerAttributeKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptclassdescription/defaultsubcontainerattributekey
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/defaultsubcontainerattributekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/defaultsubcontainerattributekey.json'
content_hash: 'sha256:034b40eb6e897668'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# defaultSubcontainerAttributeKey

<sub>Instance Property</sub>

Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.

<sub>Mac Catalyst, macOS</sub>

```swift
var defaultSubcontainerAttributeKey: String? { get }
```

## Return Value

The value of the default subcontainer attribute entry. Returns `nil` if the there was no such entry.

## See Also

### Getting basic information about the script class

- [className](classname.md) — Returns the name of the class the receiver describes, as provided at initialization time.
- [implementationClassName](implementationclassname.md) — Returns the name of the Objective-C class instantiated to implement the scripting class.
- [- isLocationRequiredToCreateForKey:](<islocationrequiredtocreate(forkey_).md>) — Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.
- [suiteName](suitename.md) — Returns the name of the receiver’s suite.

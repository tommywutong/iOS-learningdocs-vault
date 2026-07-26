---
title: className
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptclassdescription/classname
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/classname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/classname.json'
content_hash: 'sha256:a7ceb36d261b7046'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# className

<sub>Instance Property</sub>

Returns the name of the class the receiver describes, as provided at initialization time.

<sub>Mac Catalyst, macOS</sub>

```swift
var className: String? { get }
```

## Return Value

A class name. This may be either the human-readable name for the class—that is, the name that is used in a script—or the name of the Objective-C class that is instantiated to implement the class. To reliably obtain the implementation name, use [implementationClassName](implementationclassname.md).

## See Also

### Getting basic information about the script class

- [defaultSubcontainerAttributeKey](defaultsubcontainerattributekey.md) — Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [implementationClassName](implementationclassname.md) — Returns the name of the Objective-C class instantiated to implement the scripting class.
- [- isLocationRequiredToCreateForKey:](<islocationrequiredtocreate(forkey_).md>) — Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.
- [suiteName](suitename.md) — Returns the name of the receiver’s suite.

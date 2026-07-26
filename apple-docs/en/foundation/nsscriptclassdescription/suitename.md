---
title: suiteName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptclassdescription/suitename
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/suitename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/suitename.json'
content_hash: 'sha256:f3fa66a1fa9443a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# suiteName

<sub>Instance Property</sub>

Returns the name of the receiver’s suite.

<sub>Mac Catalyst, macOS</sub>

```swift
var suiteName: String? { get }
```

## Return Value

The receiver’s suite name. Within an application’s scriptability information, named suites contain related sets of information.

## See Also

### Getting basic information about the script class

- [className](classname.md) — Returns the name of the class the receiver describes, as provided at initialization time.
- [defaultSubcontainerAttributeKey](defaultsubcontainerattributekey.md) — Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [implementationClassName](implementationclassname.md) — Returns the name of the Objective-C class instantiated to implement the scripting class.
- [- isLocationRequiredToCreateForKey:](<islocationrequiredtocreate(forkey_).md>) — Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.

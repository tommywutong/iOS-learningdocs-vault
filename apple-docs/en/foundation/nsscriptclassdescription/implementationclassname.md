---
title: implementationClassName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptclassdescription/implementationclassname
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/implementationclassname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/implementationclassname.json'
content_hash: 'sha256:dd6e3ae04c5b1d81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# implementationClassName

<sub>Instance Property</sub>

Returns the name of the Objective-C class instantiated to implement the scripting class.

<sub>Mac Catalyst, macOS</sub>

```swift
var implementationClassName: String? { get }
```

## Return Value

An Objective-C class name.

## Discussion

The name returned by the [className](classname.md) method for an instance of `NSScriptClassDescription` resulting from an sdef class declaration is the human-readable name for the class—that is, the name that is used in a script. To obtain the name of the Objective-C class instantiated to implement the class, use `implementationClassName`.

## See Also

### Getting basic information about the script class

- [className](classname.md) — Returns the name of the class the receiver describes, as provided at initialization time.
- [defaultSubcontainerAttributeKey](defaultsubcontainerattributekey.md) — Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [- isLocationRequiredToCreateForKey:](<islocationrequiredtocreate(forkey_).md>) — Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.
- [suiteName](suitename.md) — Returns the name of the receiver’s suite.

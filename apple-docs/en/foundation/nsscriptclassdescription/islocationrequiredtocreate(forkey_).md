---
title: 'isLocationRequiredToCreate(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/islocationrequiredtocreate(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/islocationrequiredtocreate(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/islocationrequiredtocreate%28forkey%3A%29.json'
content_hash: 'sha256:2f62e1828cc97934'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# isLocationRequiredToCreate(forKey:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func isLocationRequiredToCreate(forKey toManyRelationshipKey: String) -> Bool
```

## Parameters

- `toManyRelationshipKey` — The key for the to-many relationship that may require an insertion location.

## Return Value

[true](../../swift/true.md) if an insertion location must be specified; otherwise, [false](../../swift/false.md).

## Discussion

A script command object that creates a new object in a to-many relationship needs to know whether an explicitly specified insertion location is required. It can get this information from an instance of `NSScriptClassDescription`. For example, `NSMakeCommand` uses this method to determine whether or not a specific `make` AppleScript command must have an `at` parameter.

## See Also

### Getting basic information about the script class

- [className](classname.md) — Returns the name of the class the receiver describes, as provided at initialization time.
- [defaultSubcontainerAttributeKey](defaultsubcontainerattributekey.md) — Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [implementationClassName](implementationclassname.md) — Returns the name of the Objective-C class instantiated to implement the scripting class.
- [suiteName](suitename.md) — Returns the name of the receiver’s suite.

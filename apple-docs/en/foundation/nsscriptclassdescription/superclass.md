---
title: superclass
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptclassdescription/superclass
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/superclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/superclass.json'
content_hash: 'sha256:46b46895f1b878fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# superclass

<sub>Instance Property</sub>

Returns the class description instance for the superclass of the receiver’s class.

<sub>Mac Catalyst, macOS</sub>

```swift
var superclass: NSScriptClassDescription? { get }
```

## Return Value

A class description instance that describes the superclass of the receiver’s class. Returns `nil` if the class has no superclass.

## Discussion

The instance of `NSScriptClassDescription` that describes the superclass can be in the same suite as the receiver or in a different suite.

## See Also

### Getting a Script Class Description

- [+ classDescriptionForClass:](<init(for_).md>) — Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.
- [- classDescriptionForKey:](<forkey(__).md>) — Returns the class description instance for the class type of the specified attribute or relationship.

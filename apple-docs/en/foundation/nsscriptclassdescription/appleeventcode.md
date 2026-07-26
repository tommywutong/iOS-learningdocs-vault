---
title: appleEventCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptclassdescription/appleeventcode
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/appleeventcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/appleeventcode.json'
content_hash: 'sha256:c8cf5d48fd8d6cf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# appleEventCode

<sub>Instance Property</sub>

Returns the Apple event code associated with the receiver’s class.

<sub>Mac Catalyst, macOS</sub>

```swift
var appleEventCode: FourCharCode { get }
```

## Return Value

The Apple event code associated with the receiver’s class. This is the primary code used to identify the class in Apple events.

## See Also

### Getting and comparing Apple event codes

- [- appleEventCodeForKey:](<appleeventcode(forkey_).md>) — Returns the Apple event code for the specified attribute or relationship in the receiver.
- [- matchesAppleEventCode:](<matchesappleeventcode(__).md>) — Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.

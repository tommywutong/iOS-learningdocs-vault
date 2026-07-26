---
title: 'forKey(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/forkey(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/forkey(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/forkey%28_%3A%29.json'
content_hash: 'sha256:038b13f056d01eab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# forKey(_:)

<sub>Instance Method</sub>

Returns the class description instance for the class type of the specified attribute or relationship.

<sub>Mac Catalyst, macOS</sub>

```swift
func forKey(_ key: String) -> NSScriptClassDescription?
```

## Parameters

- `key` — The identifying key for an attribute or relationship of the receiver.

## Return Value

The instance of `NSScriptClassDescription` for the type of the attribute or relationship specified by `key`. Returns `nil` if no scriptable property corresponds to `key`.

## See Also

### Getting a Script Class Description

- [+ classDescriptionForClass:](<init(for_).md>) — Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.
- [superclassDescription](superclass.md) — Returns the class description instance for the superclass of the receiver’s class.

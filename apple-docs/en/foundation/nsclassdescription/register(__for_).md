---
title: 'register(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsclassdescription/register(_:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsclassdescription/register(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclassdescription/register%28_%3Afor%3A%29.json'
content_hash: 'sha256:e9bcd9b283138574'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSClassDescription](../nsclassdescription.md)

# register(_:for:)

<sub>Type Method</sub>

Registers an `NSClassDescription` object for a given class in the `NSClassDescription` cache.

<sub>Mac Catalyst, macOS</sub>

```swift
class func register(_ description: NSClassDescription, for aClass: AnyClass)
```

## Parameters

- `description` — The class description to register.

- `aClass` — The class for which to register `description`.

## Discussion

You should rarely need to directly invoke this method.

## See Also

### Working with class descriptions

- [+ classDescriptionForClass:](<init(for_).md>) — Returns the class description for a given class.
- [+ invalidateClassDescriptionCache](<invalidateclassdescriptioncache().md>) — Removes all `NSClassDescription` objects from the cache.

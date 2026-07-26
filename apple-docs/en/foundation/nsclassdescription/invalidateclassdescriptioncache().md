---
title: invalidateClassDescriptionCache()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsclassdescription/invalidateclassdescriptioncache()
source_url: 'https://developer.apple.com/documentation/foundation/nsclassdescription/invalidateclassdescriptioncache()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclassdescription/invalidateclassdescriptioncache%28%29.json'
content_hash: 'sha256:9e7d4211312e76ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSClassDescription](../nsclassdescription.md)

# invalidateClassDescriptionCache()

<sub>Type Method</sub>

Removes all `NSClassDescription` objects from the cache.

<sub>Mac Catalyst, macOS</sub>

```swift
class func invalidateClassDescriptionCache()
```

## Discussion

You should rarely need to invoke this method. Use it whenever a registered `NSClassDescription` object might be replaced by a different version, such as when you have loaded a new provider of `NSClassDescription` objects, or when you are about to remove a provider of `NSClassDescription` objects.

## See Also

### Working with class descriptions

- [+ classDescriptionForClass:](<init(for_).md>) — Returns the class description for a given class.
- [+ registerClassDescription:forClass:](<register(__for_).md>) — Registers an `NSClassDescription` object for a given class in the `NSClassDescription` cache.

---
title: 'init(for:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/init(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/init(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/init%28for%3A%29.json'
content_hash: 'sha256:1ae20f949c3c085f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# init(for:)

<sub>Initializer</sub>

Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(for aClass: AnyClass)
```

## Parameters

- `aClass` — The class whose description is needed.

## Return Value

The class description for the class specified by `aClass` or, if that class isn’t scriptable, for the class description for the first superclass that is. Returns `nil` if it doesn’t find a scriptable class.

## See Also

### Getting a Script Class Description

- [- classDescriptionForKey:](<forkey(__).md>) — Returns the class description instance for the class type of the specified attribute or relationship.
- [superclassDescription](superclass.md) — Returns the class description instance for the superclass of the receiver’s class.

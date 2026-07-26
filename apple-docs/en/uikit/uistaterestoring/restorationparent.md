---
title: restorationParent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistaterestoring/restorationparent
source_url: 'https://developer.apple.com/documentation/uikit/uistaterestoring/restorationparent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistaterestoring/restorationparent.json'
content_hash: 'sha256:f415d997737dc858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStateRestoring](../uistaterestoring.md)

# restorationParent

<sub>Instance Property</sub>

The parent object used to scope the current object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var restorationParent: (any UIStateRestoring)? { get }
```

## Discussion

Returning an object from this property lets you use the same restoration identifier for objects with similar behavior but different parents. When registering objects, the [+ registerObjectForStateRestoration:restorationIdentifier:](<../uiapplication/registerobject(forstaterestoration_restorationidentifier_).md>) method checks the value of this property, using the value as the containing scope for the object. For example, an object associated with a view controller can make the view controller its parent.

## See Also

### Accessing the object information

- [objectRestorationClass](objectrestorationclass.md) — The class responsible for creating this object when restoring the app’s state.

---
title: objectRestorationClass
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistaterestoring/objectrestorationclass
source_url: 'https://developer.apple.com/documentation/uikit/uistaterestoring/objectrestorationclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistaterestoring/objectrestorationclass.json'
content_hash: 'sha256:d0ed8dda4783cf24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStateRestoring](../uistaterestoring.md)

# objectRestorationClass

<sub>Instance Property</sub>

The class responsible for creating this object when restoring the app’s state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var objectRestorationClass: (any UIObjectRestoration.Type)? { get }
```

## Discussion

If an object has an associated restoration class, the [+ objectWithRestorationIdentifierPath:coder:](<../uiobjectrestoration/object(withrestorationidentifierpath_coder_).md>) method of that class is called during state restoration. That method is responsible for returning the object that matches the provided path identifier information. If this property is`nil`, the object must already exist and be registered with the state restoration engine so that it can be found implicitly. You can register the object using the [+ registerObjectForStateRestoration:restorationIdentifier:](<../uiapplication/registerobject(forstaterestoration_restorationidentifier_).md>) method at launch time.

The restoration class must conform to the [UIObjectRestoration](../uiobjectrestoration.md) protocol.

## See Also

### Accessing the object information

- [restorationParent](restorationparent.md) — The parent object used to scope the current object.

---
title: didLoadNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/didloadnotification
source_url: 'https://developer.apple.com/documentation/foundation/bundle/didloadnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/didloadnotification.json'
content_hash: 'sha256:6ea808cce78c7e6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# didLoadNotification

<sub>Type Property</sub>

A notification that lets observers know when classes are dynamically loaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let didLoadNotification: NSNotification.Name
```

## Discussion

When a request is made to a bundle for a class ([- classNamed:](<classnamed(__).md>) or [principalClass](principalclass.md)), the bundle dynamically loads the executable code file that contains the class implementation and all other class definitions contained in the file. After the module is loaded, the bundle posts the [NSBundleDidLoadNotification](didloadnotification.md).

The notification object is the [Bundle](../bundle.md) instance that dynamically loads classes. The `userInfo` dictionary contains an [NSLoadedClasses](../nsloadedclasses.md) key.

In a typical use of this notification, an object might want to enumerate the `userInfo` array to check if each loaded class conformed to a certain protocol (say, an protocol for a plug-and-play tool set); if a class does conform, the object would create an instance of that class and add the instance to another [NSArray](../nsarray.md) object.

## See Also

### Getting classes from a bundle

- [- classNamed:](<classnamed(__).md>) — Returns the `Class` object for the specified name.
- [principalClass](principalclass.md) — The bundle’s principal class.
- [NSLoadedClasses](../nsloadedclasses.md) — A constant used as a key for the `userInfo` dictionary of a [NSBundleDidLoadNotification](didloadnotification.md) notification that corresponds to an array of names of each class that was loaded.
- [DidLoadMessage](didloadmessage.md) — A message a bundle sends when it dynamically loads a class.

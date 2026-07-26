---
title: NSLoadedClasses
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsloadedclasses
source_url: 'https://developer.apple.com/documentation/foundation/nsloadedclasses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsloadedclasses.json'
content_hash: 'sha256:a53e69e7fd1b0ef9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLoadedClasses

<sub>Global Variable</sub>

A constant used as a key for the `userInfo` dictionary of a [NSBundleDidLoadNotification](bundle/didloadnotification.md) notification that corresponds to an array of names of each class that was loaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSLoadedClasses: String
```

## See Also

### Getting classes from a bundle

- [- classNamed:](<bundle/classnamed(__).md>) — Returns the `Class` object for the specified name.
- [principalClass](bundle/principalclass.md) — The bundle’s principal class.
- [NSBundleDidLoadNotification](bundle/didloadnotification.md) — A notification that lets observers know when classes are dynamically loaded.
- [DidLoadMessage](bundle/didloadmessage.md) — A message a bundle sends when it dynamically loads a class.

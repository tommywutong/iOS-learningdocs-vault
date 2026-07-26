---
title: NSClassDescriptionNeededForClass
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsclassdescriptionneededforclass
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsclassdescriptionneededforclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsclassdescriptionneededforclass.json'
content_hash: 'sha256:69d756b243a7d3f5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSClassDescriptionNeededForClass

<sub>Type Property</sub>

Posted by [+ classDescriptionForClass:](<../../nsclassdescription/init(for_).md>) when a class description cannot be found for a class.

<sub>Mac Catalyst, macOS</sub>

```swift
static let NSClassDescriptionNeededForClass: NSNotification.Name
```

## Discussion

After the notification is processed, [+ classDescriptionForClass:](<../../nsclassdescription/init(for_).md>) checks for a class description again. This checking allows an observer to register class descriptions lazily. The notification is posted only once for any given class, even if the class description remains undefined.

The notification object is the class object for which the class description is requested. This notification does not contain a `userInfo` dictionary.

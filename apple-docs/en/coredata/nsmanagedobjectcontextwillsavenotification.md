---
title: NSManagedObjectContextWillSaveNotification
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontextwillsavenotification
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextwillsavenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextwillsavenotification.json'
content_hash: 'sha256:f8a7d82003a9a75b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectContextWillSaveNotification

<sub>Global Variable</sub>

A notification that posts before a context writes unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const NSManagedObjectContextWillSaveNotification;
```

## Discussion

This notification’s `object` is the context that’s about to save. Only use the notification to operate on the in-process save operation. For example, to insert additional managed objects. Don’t peform any asynchronous work or block the calling thread. [NSManagedObjectContext](nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

There is no `userInfo` dictionary.

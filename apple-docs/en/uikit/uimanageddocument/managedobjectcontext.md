---
title: managedObjectContext
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimanageddocument/managedobjectcontext
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/managedobjectcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/managedobjectcontext.json'
content_hash: 'sha256:fd2d12289a2fa2a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# managedObjectContext

<sub>Instance Property</sub>

The document’s managed object context.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var managedObjectContext: NSManagedObjectContext { get }
```

## Discussion

The document automatically creates a managed object context using its persistent store coordinator.

### Special considerations

You must not use the document’s managed object context in [- writeAdditionalContent:toURL:originalContentsURL:error:](<writeadditionalcontent(__to_originalcontentsurl_).md>), or any of the asynchronous [UIDocument](../uidocument.md) methods.

## See Also

### Managing the Core Data stack

- [- configurePersistentStoreCoordinatorForURL:ofType:modelConfiguration:storeOptions:error:](<configurepersistentstorecoordinator(for_oftype_modelconfiguration_storeoptions_).md>) — Creates or loads the document’s persistent store.
- [managedObjectModel](managedobjectmodel.md) — The document’s managed object model.
- [persistentStoreOptions](persistentstoreoptions.md) — Options used when creating the document’s persistent store.
- [modelConfiguration](modelconfiguration.md) — A model configuration name to be passed when configuring the persistent store.
- [- persistentStoreTypeForFileType:](<persistentstoretype(forfiletype_).md>) — Returns the Core Data store type for a given document file type.

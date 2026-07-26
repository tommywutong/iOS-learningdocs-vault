---
title: managedObjectModel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimanageddocument/managedobjectmodel
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/managedobjectmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/managedobjectmodel.json'
content_hash: 'sha256:18f5b1e27d67082b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# managedObjectModel

<sub>Instance Property</sub>

The document’s managed object model.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var managedObjectModel: NSManagedObjectModel { get }
```

## Discussion

Persistent documents always have a managed object model. The default model is the union of all models in the main bundle. You can specify a configuration to use with [modelConfiguration](modelconfiguration.md). You can subclass [UIManagedDocument](../uimanageddocument.md) to override this method if you need custom behavior.

## See Also

### Managing the Core Data stack

- [- configurePersistentStoreCoordinatorForURL:ofType:modelConfiguration:storeOptions:error:](<configurepersistentstorecoordinator(for_oftype_modelconfiguration_storeoptions_).md>) — Creates or loads the document’s persistent store.
- [managedObjectContext](managedobjectcontext.md) — The document’s managed object context.
- [persistentStoreOptions](persistentstoreoptions.md) — Options used when creating the document’s persistent store.
- [modelConfiguration](modelconfiguration.md) — A model configuration name to be passed when configuring the persistent store.
- [- persistentStoreTypeForFileType:](<persistentstoretype(forfiletype_).md>) — Returns the Core Data store type for a given document file type.

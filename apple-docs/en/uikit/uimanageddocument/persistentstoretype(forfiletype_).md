---
title: 'persistentStoreType(forFileType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimanageddocument/persistentstoretype(forfiletype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/persistentstoretype(forfiletype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/persistentstoretype%28forfiletype%3A%29.json'
content_hash: 'sha256:c57733d6e2bf7519'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# persistentStoreType(forFileType:)

<sub>Instance Method</sub>

Returns the Core Data store type for a given document file type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func persistentStoreType(forFileType fileType: String) -> String
```

## Parameters

- `fileType` — The document file type.

## Return Value

The persistent store type for `fileType`.

## Discussion

Override this method to specify a persistent store type for a given document type.

The default returns [NSSQLiteStoreType](../../coredata/nssqlitestoretype.md).

## See Also

### Managing the Core Data stack

- [- configurePersistentStoreCoordinatorForURL:ofType:modelConfiguration:storeOptions:error:](<configurepersistentstorecoordinator(for_oftype_modelconfiguration_storeoptions_).md>) — Creates or loads the document’s persistent store.
- [managedObjectContext](managedobjectcontext.md) — The document’s managed object context.
- [managedObjectModel](managedobjectmodel.md) — The document’s managed object model.
- [persistentStoreOptions](persistentstoreoptions.md) — Options used when creating the document’s persistent store.
- [modelConfiguration](modelconfiguration.md) — A model configuration name to be passed when configuring the persistent store.

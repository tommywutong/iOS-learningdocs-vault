---
title: persistentStoreOptions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimanageddocument/persistentstoreoptions
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/persistentstoreoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/persistentstoreoptions.json'
content_hash: 'sha256:bf27cfd0597a9620'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# persistentStoreOptions

<sub>Instance Property</sub>

Options used when creating the document’s persistent store.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var persistentStoreOptions: [AnyHashable : Any]? { get set }
```

## Discussion

By default, this value is `nil`.

To support automatic migration, you might pass a dictionary like that shown in the following example.

```objc
NSDictionary *options = @{
    NSMigratePersistentStoresAutomaticallyOption: @YES,
    NSInferMappingModelAutomaticallyOption: @YES
};
<#Managed document instance#>.persistentStoreOptions = options;
```

## See Also

### Managing the Core Data stack

- [- configurePersistentStoreCoordinatorForURL:ofType:modelConfiguration:storeOptions:error:](<configurepersistentstorecoordinator(for_oftype_modelconfiguration_storeoptions_).md>) — Creates or loads the document’s persistent store.
- [managedObjectContext](managedobjectcontext.md) — The document’s managed object context.
- [managedObjectModel](managedobjectmodel.md) — The document’s managed object model.
- [modelConfiguration](modelconfiguration.md) — A model configuration name to be passed when configuring the persistent store.
- [- persistentStoreTypeForFileType:](<persistentstoretype(forfiletype_).md>) — Returns the Core Data store type for a given document file type.

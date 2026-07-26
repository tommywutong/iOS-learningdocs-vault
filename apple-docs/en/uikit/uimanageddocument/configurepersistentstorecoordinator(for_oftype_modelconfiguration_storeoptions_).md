---
title: 'configurePersistentStoreCoordinator(for:ofType:modelConfiguration:storeOptions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimanageddocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/configurepersistentstorecoordinator%28for%3Aoftype%3Amodelconfiguration%3Astoreoptions%3A%29.json'
content_hash: 'sha256:106f373b137a79bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# configurePersistentStoreCoordinator(for:ofType:modelConfiguration:storeOptions:)

<sub>Instance Method</sub>

Creates or loads the document’s persistent store.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func configurePersistentStoreCoordinator(for storeURL: URL, ofType fileType: String, modelConfiguration configuration: String?, storeOptions: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `storeURL` — The URL for the persistent store.

- `fileType` — The document’s file type.

- `configuration` — The managed object model configuration to use.

- `storeOptions` — The options used to configure the persistent store coordinator.

## Discussion

You can override this method if you want customize the creation or loading of the document’s persistent store. For example, you can perform post-migration clean-up — if your app needs to migrate store data to use a new version of the managed object model, you can override this method to make additional modifications to the store after migration.

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Managing the Core Data stack

- [managedObjectContext](managedobjectcontext.md) — The document’s managed object context.
- [managedObjectModel](managedobjectmodel.md) — The document’s managed object model.
- [persistentStoreOptions](persistentstoreoptions.md) — Options used when creating the document’s persistent store.
- [modelConfiguration](modelconfiguration.md) — A model configuration name to be passed when configuring the persistent store.
- [- persistentStoreTypeForFileType:](<persistentstoretype(forfiletype_).md>) — Returns the Core Data store type for a given document file type.

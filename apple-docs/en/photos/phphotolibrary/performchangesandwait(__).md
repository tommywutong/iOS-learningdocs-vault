---
title: 'performChangesAndWait(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/performchangesandwait(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/performchangesandwait(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/performchangesandwait%28_%3A%29.json'
content_hash: 'sha256:16daf6193b42efd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# performChangesAndWait(_:)

<sub>Instance Method</sub>

Synchronously runs a block that requests changes to be performed in the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func performChangesAndWait(_ changeBlock: @escaping () -> Void) throws
```

## Parameters

- `changeBlock` — A block that requests changes to be performed. This block takes no parameters and has no return value.

## Discussion

Do not call this method from the main thread. Your change block, and the work that Photos performs on your behalf to apply the changes it requests, take some time to execute. (Photos may need to prompt the user to perform changes, so this method can block execution indefinitely.) Use this method if you are already performing work on a background queue that results in a change to be applied to the Photos library. To request changes from the main queue, use the [- performChanges:completionHandler:](<performchanges(__completionhandler_).md>) method instead.

> [!note] Note
> For each call to this method, iOS shows an alert asking the user for permission to edit the contents of the photo library. If your app needs to submit several changes at once, combine them into a single change block. For example, to edit the content of multiple existing photos, create multiple [PHAssetChangeRequest](../phassetchangerequest.md) objects and set the [contentEditingOutput](../phassetchangerequest/contenteditingoutput.md) property on each to an independent [PHContentEditingOutput](../phcontenteditingoutput.md) object.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Updating the Library

- [Requesting Changes to the Photo Library](../../photokit/requesting-changes-to-the-photo-library.md) — Create, delete, or modify assets and collections in a photo library by making change requests.
- [- performChanges:completionHandler:](<performchanges(__completionhandler_).md>) — Asynchronously runs a block that requests changes to the photo library.
- [PHChangeRequest](../phchangerequest.md) — The abstract base class of the framework’s photo library change requests.
- [PHAssetChangeRequest](../phassetchangerequest.md) — A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md) — A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md) — A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [PHObjectPlaceholder](../phobjectplaceholder.md) — A read-only proxy object that represents a Photos asset or collection to create.

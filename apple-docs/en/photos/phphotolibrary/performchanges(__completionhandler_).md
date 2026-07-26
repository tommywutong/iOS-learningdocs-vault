---
title: 'performChanges(_:completionHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/performchanges(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/performchanges(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/performchanges%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:ac6a8fb578a9d67c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# performChanges(_:completionHandler:)

<sub>Instance Method</sub>

Asynchronously runs a block that requests changes to the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func performChanges(_ changeBlock: @escaping () -> Void, completionHandler: (@Sendable (Bool, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func performChanges(_ changeBlock: @escaping () -> Void) async throws
```

## Parameters

- `changeBlock` — A block that requests changes to perform. This block takes no parameters and has no return value.

- `completionHandler` — A block that Photos calls after the change block completes and Photos performs the requested changes. The block takes the following parameters: - **success** — `true` if Photos successfully applied the changes requested in the block; otherwise, `false`. - **error** — If an error occurs, an `NSError` object describing the error; otherwise, `nil`.

## Discussion

Photos executes both the change block and the completion handler block on an arbitrary serial queue. To update your app’s UI as a result of a change, dispatch that work to the main queue.

> [!note] Note
> For each call to this method, iOS shows an alert asking the user for permission to edit the contents of the photo library. If your app needs to submit several changes at once, combine them into a single change block. For example, to edit the content of multiple existing photos, create multiple [PHAssetChangeRequest](../phassetchangerequest.md) objects and set the [contentEditingOutput](../phassetchangerequest/contenteditingoutput.md) property on each to an independent [PHContentEditingOutput](../phcontenteditingoutput.md) object.

## See Also

### Updating the Library

- [Requesting Changes to the Photo Library](../../photokit/requesting-changes-to-the-photo-library.md) — Create, delete, or modify assets and collections in a photo library by making change requests.
- [- performChangesAndWait:error:](<performchangesandwait(__).md>) — Synchronously runs a block that requests changes to be performed in the photo library.
- [PHChangeRequest](../phchangerequest.md) — The abstract base class of the framework’s photo library change requests.
- [PHAssetChangeRequest](../phassetchangerequest.md) — A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md) — A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md) — A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [PHObjectPlaceholder](../phobjectplaceholder.md) — A read-only proxy object that represents a Photos asset or collection to create.

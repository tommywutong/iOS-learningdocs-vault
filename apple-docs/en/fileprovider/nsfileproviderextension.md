---
title: NSFileProviderExtension
framework: File Provider
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/fileprovider/nsfileproviderextension
source_url: 'https://developer.apple.com/documentation/fileprovider/nsfileproviderextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/fileprovider/nsfileproviderextension.json'
content_hash: 'sha256:364e9997ecc87874'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [File Provider](../fileprovider.md)

# NSFileProviderExtension

<sub>Class</sub>

The principal class for the nonreplicated File Provider extension.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class NSFileProviderExtension
```

## Overview

To create a nonreplicated File Provider extension, start by creating a subclass of the [NSFileProviderExtension](nsfileproviderextension.md) class. When implementing your [NSFileProviderExtension](nsfileproviderextension.md) subclass, remember:

- Override all of the extension’s methods (except the deprecated methods), even if your implementation is only an empty method.
- Use your method implementations to provide access to the documents and folders managed by your file provider.
- Don’t call `super` in your method implementations.

Don’t use the [NSFileProviderExtension](nsfileproviderextension.md) class in macOS. Instead, create an [NSObject](../objectivec/nsobject-swift.class.md) subclass that adopts the [NSFileProviderReplicatedExtension](nsfileproviderreplicatedextension.md) and [NSFileProviderEnumerating](nsfileproviderenumerating.md) protocols. For more information, see [Replicated File Provider extension](replicated-file-provider-extension.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Working with items and persistent identifiers

- [- persistentIdentifierForItemAtURL:](<nsfileproviderextension/persistentidentifierforitem(at_).md>) — Returns a unique identifier for the given URL.
- [- URLForItemWithPersistentIdentifier:](<nsfileproviderextension/urlforitem(withpersistentidentifier_).md>) — Returns the URL for a given persistent identifier.
- [- itemForIdentifier:error:](<nsfileproviderextension/item(for_).md>) — Returns a description of the item associated with the persistent identifier.
- [- enumeratorForContainerItemIdentifier:error:](<nsfileproviderextension/enumerator(for_).md>) — Returns an enumerator for the specified item.
- [NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md) — A unique identifier for an item managed by the File Provider extension.

### Managing shared files

- [- itemChangedAtURL:](<nsfileproviderextension/itemchanged(at_).md>) — Tells the File Provider extension that a document has changed.
- [- providePlaceholderAtURL:completionHandler:](<nsfileproviderextension/provideplaceholder(at_completionhandler_).md>) — Triggers the creation of a placeholder for the given URL.
- [- startProvidingItemAtURL:completionHandler:](<nsfileproviderextension/startprovidingitem(at_completionhandler_).md>) — Provides an actual file on disk for a placeholder.
- [- stopProvidingItemAtURL:](<nsfileproviderextension/stopprovidingitem(at_).md>) — Tells the File Provider extension that a given document is no longer being accessed.

### Handling actions

- [Providing support for user-driven actions](providing-support-for-user-driven-actions.md) — Override methods to handle user-initiated actions.
- [- createDirectoryWithName:inParentItemIdentifier:completionHandler:](<nsfileproviderextension/createdirectory(withname_inparentitemidentifier_completionhandler_).md>) — Creates a directory with the given name inside the given parent directory.
- [- deleteItemWithIdentifier:completionHandler:](<nsfileproviderextension/deleteitem(withidentifier_completionhandler_).md>) — Permanently deletes an item from the trash.
- [- importDocumentAtURL:toParentItemIdentifier:completionHandler:](<nsfileproviderextension/importdocument(at_toparentitemidentifier_completionhandler_).md>) — Imports a file or package into the given parent directory.
- [- renameItemWithIdentifier:toName:completionHandler:](<nsfileproviderextension/renameitem(withidentifier_toname_completionhandler_).md>) — Renames a document or directory.
- [- reparentItemWithIdentifier:toParentItemWithIdentifier:newName:completionHandler:](<nsfileproviderextension/reparentitem(withidentifier_toparentitemwithidentifier_newname_completionhandler_).md>) — Moves the specified item into the given parent directory.
- [- setFavoriteRank:forItemIdentifier:completionHandler:](<nsfileproviderextension/setfavoriterank(__foritemidentifier_completionhandler_).md>) — Marks a directory as a favorite and sets its relative order in the Favorites list.
- [- setLastUsedDate:forItemIdentifier:completionHandler:](<nsfileproviderextension/setlastuseddate(__foritemidentifier_completionhandler_).md>) — Marks an item as recently used and sets its relative order in the Recents list.
- [- setTagData:forItemIdentifier:completionHandler:](<nsfileproviderextension/settagdata(__foritemidentifier_completionhandler_).md>) — Tags an item.
- [- trashItemWithIdentifier:completionHandler:](<nsfileproviderextension/trashitem(withidentifier_completionhandler_).md>) — Moves an item into the trash.
- [- untrashItemWithIdentifier:toParentItemIdentifier:completionHandler:](<nsfileproviderextension/untrashitem(withidentifier_toparentitemidentifier_completionhandler_).md>) — Moves an item out of the trash.

### Managing domains

- [domain](nsfileproviderextension/domain.md) — The domain managed by this file provider object.

### Accessing thumbnails

- [- fetchThumbnailsForItemIdentifiers:requestedSize:perThumbnailCompletionHandler:completionHandler:](<nsfileproviderextension/fetchthumbnails(for_requestedsize_perthumbnailcompletionhandler_completionhandler_).md>) — Fetches the thumbnails for items that have been enumerated by the file provider.

### Working with services

- [- supportedServiceSourcesForItemIdentifier:error:](<nsfileproviderextension/supportedservicesources(for_).md>) — Return an array of service sources that let the host app perform actions associated with the specified item.
- [NSFileProviderServiceSource](nsfileproviderservicesource.md) — A service that provides a custom communication channel between the host app and the File Provider extension.

### Managing placeholders

- [+ placeholderURLForURL:](<nsfileproviderextension/placeholderurl(for_).md>) — Returns a placeholder URL for a given document URL. _(deprecated)_
- [+ writePlaceholderAtURL:withMetadata:error:](<nsfileproviderextension/writeplaceholder(at_withmetadata_).md>) — Writes a document placeholder with the provided metadata. _(deprecated)_

### Accessing the document storage

- [documentStorageURL](nsfileproviderextension/documentstorageurl.md) — The root URL for all shared documents. _(deprecated)_
- [providerIdentifier](nsfileproviderextension/provideridentifier.md) — A purpose identifier for coordinated reads and writes. _(deprecated)_

## See Also

### Nonreplicated extension

- [Content and Change Tracking](content-and-change-tracking.md) — Create enumerators to specify your file provider’s content, and track changes to that content.

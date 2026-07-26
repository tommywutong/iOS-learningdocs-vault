---
title: 'checkPromisedItemIsReachableAndReturnError(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/checkpromiseditemisreachableandreturnerror(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/checkpromiseditemisreachableandreturnerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/checkpromiseditemisreachableandreturnerror%28_%3A%29.json'
content_hash: 'sha256:280e0bc425a0b806'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# checkPromisedItemIsReachableAndReturnError(_:)

<sub>Instance Method</sub>

Returns whether the promised item can be reached.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func checkPromisedItemIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool
```

## Parameters

- `error` — The error that occurred when the promised item could not be reached.

## Return Value

[true](../../swift/true.md) if the promised item is reachable; otherwise, [false](../../swift/false.md).

## Discussion

This method behaves identically to [- checkResourceIsReachableAndReturnError:](<checkresourceisreachableandreturnerror(__).md>), but works on promised items. A promised item is not guaranteed to have its contents in the file system until you use a file coordinator to perform a coordinated read on its URL, which causes the contents to be downloaded or otherwise generated. Promised item URLs are returned by various APIs, including:

- A metadata query using either the [NSMetadataQueryUbiquitousDataScope](../nsmetadataqueryubiquitousdatascope.md) or [NSMetadataQueryUbiquitousDocumentsScope](../nsmetadataqueryubiquitousdocumentsscope.md) scopes
- The contents of the directory returned by the file manager’s `URLForUbiquitousContainerIdentifier:`
- The URL inside the accessor block of a coordinated read or write operation that used the [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](../nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly.md), [NSFileCoordinatorWritingForDeleting](../nsfilecoordinator/writingoptions/fordeleting.md), [NSFileCoordinatorWritingForMoving](../nsfilecoordinator/writingoptions/formoving.md), or [NSFileCoordinatorWritingContentIndependentMetadataOnly](../nsfilecoordinator/writingoptions/contentindependentmetadataonly.md) options

You must use this method instead of `checkResourceIsReachableAndReturnError` for any URLs returned by these methods.

## See Also

### Related Documentation

- [- checkResourceIsReachableAndReturnError:](<checkresourceisreachableandreturnerror(__).md>) — Returns whether the resource pointed to by a file URL can be reached.

### Working with Promised Items

- [- getPromisedItemResourceValue:forKey:error:](<getpromiseditemresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.
- [- promisedItemResourceValuesForKeys:error:](<promiseditemresourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.

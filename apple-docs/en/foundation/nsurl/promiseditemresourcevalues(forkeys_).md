---
title: 'promisedItemResourceValues(forKeys:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/promiseditemresourcevalues(forkeys:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/promiseditemresourcevalues(forkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/promiseditemresourcevalues%28forkeys%3A%29.json'
content_hash: 'sha256:7a40d2497b2ed959'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# promisedItemResourceValues(forKeys:)

<sub>Instance Method</sub>

Returns the resource values for the properties identified by specified array of keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func promisedItemResourceValues(forKeys keys: [URLResourceKey]) throws -> [URLResourceKey : Any]
```

## Parameters

- `keys` — An array of names of URL resource properties.

## Return Value

A dictionary of resource values indexed by key.

## Discussion

This method behaves identically to [- resourceValuesForKeys:error:](<resourcevalues(forkeys_).md>), but works on promised items. A promised item is not guaranteed to have its contents in the file system until you use a file coordinator to perform a coordinated read on its URL, which causes the contents to be downloaded or otherwise generated. Promised item URLs are returned by various APIs, including:

- A metadata query using either the [NSMetadataQueryUbiquitousDataScope](../nsmetadataqueryubiquitousdatascope.md) or [NSMetadataQueryUbiquitousDocumentsScope](../nsmetadataqueryubiquitousdocumentsscope.md) scopes
- The contents of the directory returned by the file manager’s `URLForUbiquitousContainerIdentifier:`
- The URL inside the accessor block of a coordinated read or write operation that used the [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](../nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly.md), [NSFileCoordinatorWritingForDeleting](../nsfilecoordinator/writingoptions/fordeleting.md), [NSFileCoordinatorWritingForMoving](../nsfilecoordinator/writingoptions/formoving.md), or [NSFileCoordinatorWritingContentIndependentMetadataOnly](../nsfilecoordinator/writingoptions/contentindependentmetadataonly.md) options

You must use this method instead of `resourceValuesForKeys:error:` for any URLs returned by these methods.

This method works for any resource value that is not tied to the item’s contents. Some keys, like [NSURLContentAccessDateKey](../urlresourcekey/contentaccessdatekey.md) or [NSURLGenerationIdentifierKey](../urlresourcekey/generationidentifierkey.md), do not return valid values. If you use one of these keys, the method returns [true](../../swift/true.md), but the value returns `nil`.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- resourceValuesForKeys:error:](<resourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.

### Working with Promised Items

- [- checkPromisedItemIsReachableAndReturnError:](<checkpromiseditemisreachableandreturnerror(__).md>) — Returns whether the promised item can be reached.
- [- getPromisedItemResourceValue:forKey:error:](<getpromiseditemresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.

---
title: 'getPromisedItemResourceValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/getpromiseditemresourcevalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/getpromiseditemresourcevalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/getpromiseditemresourcevalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:e140301368a9aff1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# getPromisedItemResourceValue(_:forKey:)

<sub>Instance Method</sub>

Returns the value of the resource property for the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: URLResourceKey) throws
```

## Parameters

- `value` — The location where the value for the resource property identified by `key` should be stored.

- `key` — The name of one of the URL’s resource properties.

## Discussion

This method behaves identically to [- getResourceValue:forKey:error:](<getresourcevalue(__forkey_).md>), but works on promised items. A promised item is not guaranteed to have its contents in the file system until you use a file coordinator to perform a coordinated read on its URL, which causes the contents to be downloaded or otherwise generated. Promised item URLs are returned by various APIs, including:

- A metadata query using either the [NSMetadataQueryUbiquitousDataScope](../nsmetadataqueryubiquitousdatascope.md) or [NSMetadataQueryUbiquitousDocumentsScope](../nsmetadataqueryubiquitousdocumentsscope.md) scopes
- The contents of the directory returned by the file manager’s `URLForUbiquitousContainerIdentifier:`
- The URL inside the accessor block of a coordinated read or write operation that used the [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](../nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly.md), [NSFileCoordinatorWritingForDeleting](../nsfilecoordinator/writingoptions/fordeleting.md), [NSFileCoordinatorWritingForMoving](../nsfilecoordinator/writingoptions/formoving.md), or [NSFileCoordinatorWritingContentIndependentMetadataOnly](../nsfilecoordinator/writingoptions/contentindependentmetadataonly.md) options

You must use this method instead of `getResourceValue:forKey:error:` for any URLs returned by these methods.

This method works for any resource value that is not tied to the item’s contents. Some keys, like [NSURLContentAccessDateKey](../urlresourcekey/contentaccessdatekey.md) or [NSURLGenerationIdentifierKey](../urlresourcekey/generationidentifierkey.md), do not return valid values. If you use one of these keys, the method returns [true](../../swift/true.md), but the value returns `nil`.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- getResourceValue:forKey:error:](<getresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.

### Working with Promised Items

- [- checkPromisedItemIsReachableAndReturnError:](<checkpromiseditemisreachableandreturnerror(__).md>) — Returns whether the promised item can be reached.
- [- promisedItemResourceValuesForKeys:error:](<promiseditemresourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.

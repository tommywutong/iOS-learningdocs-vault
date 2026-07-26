---
title: 'replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/replaceitem(at:withitemat:backupitemname:options:resultingitemurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/replaceitem(at:withitemat:backupitemname:options:resultingitemurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/replaceitem%28at%3Awithitemat%3Abackupitemname%3Aoptions%3Aresultingitemurl%3A%29.json'
content_hash: 'sha256:49b56a882608c849'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)

<sub>Instance Method</sub>

Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceItem(at originalItemURL: URL, withItemAt newItemURL: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions = [], resultingItemURL resultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws
```

## Parameters

- `originalItemURL` — The item containing the content you want to replace.

- `newItemURL` — The item containing the new content for `originalItemURL`. It is recommended that you put this item in a temporary directory as provided by the OS. If a temporary directory is not available, put this item in a uniquely named directory that is in the same directory as the original item.

- `backupItemName` — If provided, the name used to create a backup of the original item. The backup is placed in the same directory as the original item. If an error occurs during the creation of the backup item, the operation fails. If there is already an item with the same name as the backup item, that item will be removed. The backup item will be removed in the event of success unless the [NSFileManagerItemReplacementWithoutDeletingBackupItem](itemreplacementoptions/withoutdeletingbackupitem.md) option is provided in `options`.

- `options` — The options to use during the replacement. Typically, you pass [NSFileManagerItemReplacementUsingNewMetadataOnly](itemreplacementoptions/usingnewmetadataonly.md) for this parameter, which uses only the metadata from the new item. You can also combine the options described in [ItemReplacementOptions](itemreplacementoptions.md) using the C-bitwise OR operator.

- `resultingURL` — On input, a pointer for a URL object. When the item is replaced, this pointer is set to the URL of the new item. If no new file system object is required, the URL object in this parameter may be the same passed to the `originalItemURL` parameter. However, if a new file system object is required, the URL object may be different. For example, replacing an RTF document with an RTFD document requires the creation of a new file.

## Discussion

By default, the creation date, permissions, Finder label and color, and Spotlight comments of the original item are preserved on the new item. You can configure which metadata is preserved using the `options` parameter.

This method works only when the `originalItemURL` and `newItemURL` parameters are located on the same volume. Attempting to call this method by passing `originalItemURL` and `newItemURL` parameters that have locations on different volumes results in an error. Instead, you can call the [- URLForDirectory:inDomain:appropriateForURL:create:error:](<url(for_in_appropriatefor_create_).md>) method, passing [NSItemReplacementDirectory](searchpathdirectory/itemreplacementdirectory.md) as the search path directory, to get a temporary URL on the destination’s volume that is suitable for use with this method.

If an error occurs and the original item is not in the original location or a temporary location, the resulting error object contains a user info dictionary with the key `"NSFileOriginalItemLocationKey"`. The value assigned to that key is an [NSURL](../nsurl.md) object with the location of the item. The error code is one of the file-related errors described in [NSError Codes](../1448136-nserror-codes.md).

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Replacing items

- [replaceItemAt(_:withItemAt:backupItemName:options:)](<replaceitemat(__withitemat_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [ItemReplacementOptions](itemreplacementoptions.md) — Options for specifying the behavior of file replacement operations.

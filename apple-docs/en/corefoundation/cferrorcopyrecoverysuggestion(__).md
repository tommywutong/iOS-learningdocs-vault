---
title: 'CFErrorCopyRecoverySuggestion(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cferrorcopyrecoverysuggestion(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cferrorcopyrecoverysuggestion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cferrorcopyrecoverysuggestion%28_%3A%29.json'
content_hash: 'sha256:400eb1743a1461b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFErrorCopyRecoverySuggestion(_:)

<sub>Function</sub>

Returns a human presentable recovery suggestion for a given error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFErrorCopyRecoverySuggestion(_ err: CFError!) -> CFString!
```

## Parameters

- `err` — The CFError to examine. If this is not a valid CFError, the behavior is undefined.

## Return Value

A localized, human-presentable recovery suggestion for `err`, or `NULL` if no user-presentable string is available. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This is the string that can be displayed as the “informative” (or “secondary”) message on an alert panel. For example, an error description “Could not save file ‘Letter’ in folder ‘Documents’ because the volume ‘MyDisk’ doesn’t have enough space.” might have a corresponding recovery suggestion, “Remove some files from the volume and try again.”

By default, this function looks for a value for the [kCFErrorLocalizedRecoverySuggestionKey](kcferrorlocalizedrecoverysuggestionkey.md) key in the user info dictionary. Toll-free bridged instances of `NSError` might provide additional behaviors for manufacturing this value.

When you create a CFError, you should try to make sure the return value is human-presentable and localized by providing a value for [kCFErrorLocalizedRecoverySuggestionKey](kcferrorlocalizedrecoverysuggestionkey.md) in the user info dictionary.

## See Also

### Getting Information About an Error

- [CFErrorGetDomain](<cferrorgetdomain(__).md>) — Returns the error domain for a given CFError.
- [CFErrorGetCode](<cferrorgetcode(__).md>) — Returns the error code for a given CFError.
- [CFErrorCopyUserInfo](<cferrorcopyuserinfo(__).md>) — Returns the user info dictionary for a given CFError.
- [CFErrorCopyDescription](<cferrorcopydescription(__).md>) — Returns a human-presentable description for a given error.
- [CFErrorCopyFailureReason](<cferrorcopyfailurereason(__).md>) — Returns a human-presentable failure reason for a given error.

---
title: 'CFErrorCopyUserInfo(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cferrorcopyuserinfo(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cferrorcopyuserinfo(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cferrorcopyuserinfo%28_%3A%29.json'
content_hash: 'sha256:92f1f36b412a96a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFErrorCopyUserInfo(_:)

<sub>Function</sub>

Returns the user info dictionary for a given CFError.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFErrorCopyUserInfo(_ err: CFError!) -> CFDictionary!
```

## Parameters

- `err` — The error to examine. If this is not a valid CFError, the behavior is undefined.

## Return Value

A dictionary containing the same keys and values as in the userInfo dictionary `err` was created with. Returns an empty dictionary if `NULL` was supplied to the create function. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting Information About an Error

- [CFErrorGetDomain](<cferrorgetdomain(__).md>) — Returns the error domain for a given CFError.
- [CFErrorGetCode](<cferrorgetcode(__).md>) — Returns the error code for a given CFError.
- [CFErrorCopyDescription](<cferrorcopydescription(__).md>) — Returns a human-presentable description for a given error.
- [CFErrorCopyFailureReason](<cferrorcopyfailurereason(__).md>) — Returns a human-presentable failure reason for a given error.
- [CFErrorCopyRecoverySuggestion](<cferrorcopyrecoverysuggestion(__).md>) — Returns a human presentable recovery suggestion for a given error.

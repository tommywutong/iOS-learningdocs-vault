---
title: 'CFErrorGetDomain(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cferrorgetdomain(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cferrorgetdomain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cferrorgetdomain%28_%3A%29.json'
content_hash: 'sha256:6f784404ca2541ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFErrorGetDomain(_:)

<sub>Function</sub>

Returns the error domain for a given CFError.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFErrorGetDomain(_ err: CFError!) -> CFErrorDomain!
```

## Parameters

- `err` — The error to examine. If this is not a valid CFError, the behavior is undefined.

## Return Value

The error domain for `err`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Getting Information About an Error

- [CFErrorGetCode](<cferrorgetcode(__).md>) — Returns the error code for a given CFError.
- [CFErrorCopyUserInfo](<cferrorcopyuserinfo(__).md>) — Returns the user info dictionary for a given CFError.
- [CFErrorCopyDescription](<cferrorcopydescription(__).md>) — Returns a human-presentable description for a given error.
- [CFErrorCopyFailureReason](<cferrorcopyfailurereason(__).md>) — Returns a human-presentable failure reason for a given error.
- [CFErrorCopyRecoverySuggestion](<cferrorcopyrecoverysuggestion(__).md>) — Returns a human presentable recovery suggestion for a given error.

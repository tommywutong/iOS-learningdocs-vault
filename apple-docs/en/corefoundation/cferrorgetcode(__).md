---
title: 'CFErrorGetCode(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cferrorgetcode(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cferrorgetcode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cferrorgetcode%28_%3A%29.json'
content_hash: 'sha256:451b75b010389846'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFErrorGetCode(_:)

<sub>Function</sub>

Returns the error code for a given CFError.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFErrorGetCode(_ err: CFError!) -> CFIndex
```

## Parameters

- `err` — The error to examine. If this is not a valid CFError, the behavior is undefined.

## Return Value

The error code of `err`.

## Discussion

Note that this function returns the error code for the specified CFError, not an error return for the current call.

## See Also

### Getting Information About an Error

- [CFErrorGetDomain](<cferrorgetdomain(__).md>) — Returns the error domain for a given CFError.
- [CFErrorCopyUserInfo](<cferrorcopyuserinfo(__).md>) — Returns the user info dictionary for a given CFError.
- [CFErrorCopyDescription](<cferrorcopydescription(__).md>) — Returns a human-presentable description for a given error.
- [CFErrorCopyFailureReason](<cferrorcopyfailurereason(__).md>) — Returns a human-presentable failure reason for a given error.
- [CFErrorCopyRecoverySuggestion](<cferrorcopyrecoverysuggestion(__).md>) — Returns a human presentable recovery suggestion for a given error.

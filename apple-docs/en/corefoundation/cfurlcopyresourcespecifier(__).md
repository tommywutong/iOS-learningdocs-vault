---
title: 'CFURLCopyResourceSpecifier(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcopyresourcespecifier(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcopyresourcespecifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcopyresourcespecifier%28_%3A%29.json'
content_hash: 'sha256:6a269f5370338544'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCopyResourceSpecifier(_:)

<sub>Function</sub>

Returns any additional resource specifiers after the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCopyResourceSpecifier(_ anURL: CFURL!) -> CFString!
```

## Parameters

- `anURL` — The `CFURL` object to examine.

## Return Value

The resource specifiers. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function leaves any percent escape sequences intact. For decomposable URLs, this function returns everything after the path. For URLs that cannot be decomposed, this function returns everything except the scheme itself.

## See Also

### Accessing the Parts of a URL

- [CFURLCanBeDecomposed](<cfurlcanbedecomposed(__).md>) — Determines if the given URL conforms to RFC 1808 and therefore can be decomposed.
- [CFURLCopyFileSystemPath](<cfurlcopyfilesystempath(____).md>) — Returns the path portion of a given URL.
- [CFURLCopyFragment](<cfurlcopyfragment(____).md>) — Returns the fragment from a given URL.
- [CFURLCopyHostName](<cfurlcopyhostname(__).md>) — Returns the host name of a given URL.
- [CFURLCopyLastPathComponent](<cfurlcopylastpathcomponent(__).md>) — Returns the last path component of a given URL.
- [CFURLCopyNetLocation](<cfurlcopynetlocation(__).md>) — Returns the net location portion of a given URL.
- [CFURLCopyParameterString](<cfurlcopyparameterstring(____).md>) — Returns the parameter string from a given URL. _(deprecated)_
- [CFURLCopyPassword](<cfurlcopypassword(__).md>) — Returns the password of a given URL.
- [CFURLCopyPath](<cfurlcopypath(__).md>) — Returns the path portion of a given URL.
- [CFURLCopyPathExtension](<cfurlcopypathextension(__).md>) — Returns the path extension of a given URL.
- [CFURLCopyQueryString](<cfurlcopyquerystring(____).md>) — Returns the query string of a given URL.
- [CFURLCopyScheme](<cfurlcopyscheme(__).md>) — Returns the scheme portion of a given URL.
- [CFURLCopyStrictPath](<cfurlcopystrictpath(____).md>) — Returns the path portion of a given URL.
- [CFURLCopyUserName](<cfurlcopyusername(__).md>) — Returns the user name from a given URL.
- [CFURLGetPortNumber](<cfurlgetportnumber(__).md>) — Returns the port number from a given URL.

---
title: 'CFURLCopyPath(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcopypath(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcopypath(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcopypath%28_%3A%29.json'
content_hash: 'sha256:b0f0fd874f1caa06'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCopyPath(_:)

<sub>Function</sub>

Returns the path portion of a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCopyPath(_ anURL: CFURL!) -> CFString!
```

## Parameters

- `anURL` — The `CFURL` object to examine.

## Return Value

The path of `anURL`, or `NULL` if the URL cannot be decomposed (doesn’t conform to RFC 1808). Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function does not resolve the URL against its base, nor does it replace percent escape sequences. This function’s return value includes any leading slash (giving the path the normal POSIX appearance), if present. If this behavior is not appropriate, use [CFURLCopyStrictPath](<cfurlcopystrictpath(____).md>) whose return value omits any leading slash. You may also want to use the function [CFURLCopyFileSystemPath](<cfurlcopyfilesystempath(____).md>), which returns the URL’s path as a file system path for the given path style. If the path is to be passed to file system calls, you may also want to use the function [CFURLGetFileSystemRepresentation](<cfurlgetfilesystemrepresentation(________).md>), which returns a C string.

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
- [CFURLCopyPathExtension](<cfurlcopypathextension(__).md>) — Returns the path extension of a given URL.
- [CFURLCopyQueryString](<cfurlcopyquerystring(____).md>) — Returns the query string of a given URL.
- [CFURLCopyResourceSpecifier](<cfurlcopyresourcespecifier(__).md>) — Returns any additional resource specifiers after the path.
- [CFURLCopyScheme](<cfurlcopyscheme(__).md>) — Returns the scheme portion of a given URL.
- [CFURLCopyStrictPath](<cfurlcopystrictpath(____).md>) — Returns the path portion of a given URL.
- [CFURLCopyUserName](<cfurlcopyusername(__).md>) — Returns the user name from a given URL.
- [CFURLGetPortNumber](<cfurlgetportnumber(__).md>) — Returns the port number from a given URL.

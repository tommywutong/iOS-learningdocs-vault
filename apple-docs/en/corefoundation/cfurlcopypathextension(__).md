---
title: 'CFURLCopyPathExtension(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcopypathextension(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcopypathextension(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcopypathextension%28_%3A%29.json'
content_hash: 'sha256:d483493426e442eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCopyPathExtension(_:)

<sub>Function</sub>

Returns the path extension of a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCopyPathExtension(_ url: CFURL!) -> CFString!
```

## Parameters

- `url` — The `CFURL` object to examine.

## Return Value

The path extension of `url`, or `NULL` if no extension exists. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The path extension is the portion of the last path component which follows the final period, if there is one. For example, for `http:/www.apple.com/developer/macosx.today.html`, the extension is `html`, and for `http:/www.apple.com/developer`, there is no path extension.

See also [CFURLCopyLastPathComponent](<cfurlcopylastpathcomponent(__).md>).

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
- [CFURLCopyQueryString](<cfurlcopyquerystring(____).md>) — Returns the query string of a given URL.
- [CFURLCopyResourceSpecifier](<cfurlcopyresourcespecifier(__).md>) — Returns any additional resource specifiers after the path.
- [CFURLCopyScheme](<cfurlcopyscheme(__).md>) — Returns the scheme portion of a given URL.
- [CFURLCopyStrictPath](<cfurlcopystrictpath(____).md>) — Returns the path portion of a given URL.
- [CFURLCopyUserName](<cfurlcopyusername(__).md>) — Returns the user name from a given URL.
- [CFURLGetPortNumber](<cfurlgetportnumber(__).md>) — Returns the port number from a given URL.

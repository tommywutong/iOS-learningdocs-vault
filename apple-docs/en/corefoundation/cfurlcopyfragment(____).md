---
title: 'CFURLCopyFragment(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcopyfragment(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcopyfragment(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcopyfragment%28_%3A_%3A%29.json'
content_hash: 'sha256:c7528f0e0e028e7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCopyFragment(_:_:)

<sub>Function</sub>

Returns the fragment from a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCopyFragment(_ anURL: CFURL!, _ charactersToLeaveEscaped: CFString!) -> CFString!
```

## Parameters

- `anURL` — The `CFURL` object whose fragment you want to obtain.

- `charactersToLeaveEscaped` — Characters whose percent escape sequences, such as `%20` for a space character, you want to leave intact. Pass `NULL` to specify that no percent escapes be replaced, or the empty string (`CFSTR("")`) to specify that all be replaced.

## Return Value

The fragment, or `NULL` if no fragment exists. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

A fragment is the text following a “#”. These are generally used to indicate locations within a single file. This function removes all percent escape sequences except those for characters specified in `charactersToLeaveEscaped`.

## See Also

### Accessing the Parts of a URL

- [CFURLCanBeDecomposed](<cfurlcanbedecomposed(__).md>) — Determines if the given URL conforms to RFC 1808 and therefore can be decomposed.
- [CFURLCopyFileSystemPath](<cfurlcopyfilesystempath(____).md>) — Returns the path portion of a given URL.
- [CFURLCopyHostName](<cfurlcopyhostname(__).md>) — Returns the host name of a given URL.
- [CFURLCopyLastPathComponent](<cfurlcopylastpathcomponent(__).md>) — Returns the last path component of a given URL.
- [CFURLCopyNetLocation](<cfurlcopynetlocation(__).md>) — Returns the net location portion of a given URL.
- [CFURLCopyParameterString](<cfurlcopyparameterstring(____).md>) — Returns the parameter string from a given URL. _(deprecated)_
- [CFURLCopyPassword](<cfurlcopypassword(__).md>) — Returns the password of a given URL.
- [CFURLCopyPath](<cfurlcopypath(__).md>) — Returns the path portion of a given URL.
- [CFURLCopyPathExtension](<cfurlcopypathextension(__).md>) — Returns the path extension of a given URL.
- [CFURLCopyQueryString](<cfurlcopyquerystring(____).md>) — Returns the query string of a given URL.
- [CFURLCopyResourceSpecifier](<cfurlcopyresourcespecifier(__).md>) — Returns any additional resource specifiers after the path.
- [CFURLCopyScheme](<cfurlcopyscheme(__).md>) — Returns the scheme portion of a given URL.
- [CFURLCopyStrictPath](<cfurlcopystrictpath(____).md>) — Returns the path portion of a given URL.
- [CFURLCopyUserName](<cfurlcopyusername(__).md>) — Returns the user name from a given URL.
- [CFURLGetPortNumber](<cfurlgetportnumber(__).md>) — Returns the port number from a given URL.

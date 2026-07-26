---
title: 'CFURLGetBaseURL(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlgetbaseurl(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlgetbaseurl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlgetbaseurl%28_%3A%29.json'
content_hash: 'sha256:7cfe754b5ad8620d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLGetBaseURL(_:)

<sub>Function</sub>

Returns the base URL of a given URL if it exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLGetBaseURL(_ anURL: CFURL!) -> CFURL!
```

## Parameters

- `anURL` — The `CFURL` object to examine.

## Return Value

A `CFURL` object representing the base URL of `anURL`. Ownership follows the get rule. See [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Getting URL Properties

- [CFURLGetBytes](<cfurlgetbytes(______).md>) — Returns by reference the byte representation of a URL object.
- [CFURLGetByteRangeForComponent](<cfurlgetbyterangeforcomponent(______).md>) — Returns the range of the specified component in the bytes of a URL.
- [CFURLGetTypeID](<cfurlgettypeid().md>) — Returns the type identifier for the `CFURL` opaque type.
- [CFURLResourceIsReachable](<cfurlresourceisreachable(____).md>) — Returns whether the resource pointed to by a file URL can be reached.

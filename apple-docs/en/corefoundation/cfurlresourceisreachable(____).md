---
title: 'CFURLResourceIsReachable(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlresourceisreachable(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlresourceisreachable(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlresourceisreachable%28_%3A_%3A%29.json'
content_hash: 'sha256:588acf32add113ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLResourceIsReachable(_:_:)

<sub>Function</sub>

Returns whether the resource pointed to by a file URL can be reached.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLResourceIsReachable(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

## Parameters

- `url` — The URL to check.

- `error` — The error that occurred when the resource could not be reached.

## Return Value

`true` if the resource is reachable; otherwise,  `false`.

## Discussion

This function synchronously checks if the file at the provided URL is reachable. Checking reachability is appropriate when making decisions that do not require other immediate operations on the resource, such as periodic maintenance of user interface state that depends on the existence of a specific document. For example, you might remove an item from a download list if the user deletes the file.

If your app must perform operations on the file, such as opening it or copying resource properties, it is more efficient to attempt the operation and handle any failure that may occur.

If this function returns `false`, the object pointer referenced by `error` is populated with additional information.

> [!note] Note
> This method is currently applicable only to URLs for file system resources. For other URL types, this method always returns `false`.

## See Also

### Getting URL Properties

- [CFURLGetBaseURL](<cfurlgetbaseurl(__).md>) — Returns the base URL of a given URL if it exists.
- [CFURLGetBytes](<cfurlgetbytes(______).md>) — Returns by reference the byte representation of a URL object.
- [CFURLGetByteRangeForComponent](<cfurlgetbyterangeforcomponent(______).md>) — Returns the range of the specified component in the bytes of a URL.
- [CFURLGetTypeID](<cfurlgettypeid().md>) — Returns the type identifier for the `CFURL` opaque type.

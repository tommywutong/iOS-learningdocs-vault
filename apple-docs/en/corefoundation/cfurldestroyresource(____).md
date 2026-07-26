---
title: 'CFURLDestroyResource(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfurldestroyresource(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurldestroyresource(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurldestroyresource%28_%3A_%3A%29.json'
content_hash: 'sha256:976fb31ed9678bb4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLDestroyResource(_:_:)

<sub>Function</sub>

Destroys a resource indicated by a given URL.

> [!warning] Deprecated
> Use CFURLGetFileSystemRepresentation and removefile(3) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func CFURLDestroyResource(_ url: CFURL!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Bool
```

## Parameters

- `url` — The `CFURL` object of the resource to destroy.

- `errorCode` — On return, `0` if successful, otherwise an error code indicating the nature of the problem. See [CFURLError](cfurlerror.md) for a list of possible error codes.

## Return Value

`true` if successful, `false` otherwise.

## Discussion

If `url` uses an http scheme, an http `DELETE` request is sent to the resource. If `url` uses a file scheme, then:

- if the reference is a file, the file is deleted;
- if the reference is a directory and the directory is empty, the directory is deleted;
- if the reference is a directory and the directory is not empty, the function returns `false` and `errorCode` contains `kCFURLUnknownError`.

## See Also

### Core Foundation URL Access Utilities Miscellaneous Functions

- [CFURLCreateDataAndPropertiesFromResource](<cfurlcreatedataandpropertiesfromresource(____________).md>) — Loads the data and properties referred to by a given URL. _(deprecated)_
- [CFURLCreatePropertyFromResource](<cfurlcreatepropertyfromresource(________).md>) — Returns a given property specified by a given URL and property string. _(deprecated)_
- [CFURLWriteDataAndPropertiesToResource](<cfurlwritedataandpropertiestoresource(________).md>) — Writes the given data and properties to a given URL. _(deprecated)_

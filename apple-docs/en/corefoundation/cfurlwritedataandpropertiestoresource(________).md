---
title: 'CFURLWriteDataAndPropertiesToResource(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfurlwritedataandpropertiestoresource(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlwritedataandpropertiestoresource(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlwritedataandpropertiestoresource%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:eefe62ef9620413a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLWriteDataAndPropertiesToResource(_:_:_:_:)

<sub>Function</sub>

Writes the given data and properties to a given URL.

> [!warning] Deprecated
> For resource data, use the CFWriteStream API. For file resource properties, use CFURLSetResourcePropertiesForKeys.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func CFURLWriteDataAndPropertiesToResource(_ url: CFURL!, _ dataToWrite: CFData!, _ propertiesToWrite: CFDictionary!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Bool
```

## Parameters

- `url` — The resource to write.

- `dataToWrite` — The data to write. Pass `NULL` to write only properties.

- `propertiesToWrite` — The properties to write. Pass `NULL` to write only data. See [File URL Properties](file-url-properties.md) and [HTTP URL Properties](http-url-properties.md) for the list of available properties.

- `errorCode` — Upon return, `0` if successful, otherwise contains an error code indicating the nature of the problem. See [CFURLError](cfurlerror.md) for a list of possible error codes.

## Return Value

`true` if successful, `false` otherwise.

## Discussion

Properties not present in `propertiesToWrite` are left unchanged, hence if `propertiesToWrite` is `NULL` or empty, the URL’s properties are not changed at all.

If `url` uses a file scheme and it references a file, the contents of `dataToWrite` are written to the referenced file, overwriting any preexisting data, and the file’s properties are modified according to `propertiesToWrite`. If the file does not exist, but all intermediate directories along the path do already exist, the file is created (otherwise it is not).

If `url` uses a file scheme and it references a directory (the last path character is “`/`”), the contents of `dataToWrite` are ignored, but if the parameter value is not `NULL`—and all intermediate directories along the path do already exist—a new directory is created  (otherwise it is not).

If `url` uses an http scheme, an http `PUT` request is sent to the resource with `propertiesToWrite` as the header fields and `dataToWrite` as the data.

## See Also

### Core Foundation URL Access Utilities Miscellaneous Functions

- [CFURLCreateDataAndPropertiesFromResource](<cfurlcreatedataandpropertiesfromresource(____________).md>) — Loads the data and properties referred to by a given URL. _(deprecated)_
- [CFURLCreatePropertyFromResource](<cfurlcreatepropertyfromresource(________).md>) — Returns a given property specified by a given URL and property string. _(deprecated)_
- [CFURLDestroyResource](<cfurldestroyresource(____).md>) — Destroys a resource indicated by a given URL. _(deprecated)_

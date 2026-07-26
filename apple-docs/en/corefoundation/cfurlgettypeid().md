---
title: CFURLGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlgettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlgettypeid%28%29.json'
content_hash: 'sha256:b22f8066488ed060'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLGetTypeID()

<sub>Function</sub>

Returns the type identifier for the `CFURL` opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the `CFURL` opaque type.

## See Also

### Getting URL Properties

- [CFURLGetBaseURL](<cfurlgetbaseurl(__).md>) — Returns the base URL of a given URL if it exists.
- [CFURLGetBytes](<cfurlgetbytes(______).md>) — Returns by reference the byte representation of a URL object.
- [CFURLGetByteRangeForComponent](<cfurlgetbyterangeforcomponent(______).md>) — Returns the range of the specified component in the bytes of a URL.
- [CFURLResourceIsReachable](<cfurlresourceisreachable(____).md>) — Returns whether the resource pointed to by a file URL can be reached.

---
title: 'CFURLGetByteRangeForComponent(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlgetbyterangeforcomponent(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlgetbyterangeforcomponent(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlgetbyterangeforcomponent%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f41f53af7af22572'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLGetByteRangeForComponent(_:_:_:)

<sub>Function</sub>

Returns the range of the specified component in the bytes of a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLGetByteRangeForComponent(_ url: CFURL!, _ component: CFURLComponentType, _ rangeIncludingSeparators: UnsafeMutablePointer<CFRange>!) -> CFRange
```

## Parameters

- `url` — The URL containing `component`.

- `component` — The type of component in `anURL` whose range you want to obtain. See [CFURLComponentType](cfurlcomponenttype.md) for possible values.

- `rangeIncludingSeparators` — Specifies the range of `component` including the sequences that separate component from the previous and next components. If there is no previous or next components, this function will match the range of the component itself. If `anURL` does not contain `component`, `rangeIncludingSeparators` is set to the location where the component would be inserted.

## Return Value

The range of bytes for `component` in the buffer returned by the [CFURLGetBytes](<cfurlgetbytes(______).md>) function. If `anURL` does not contain `component`, the first part of the returned range is set to [kCFNotFound](kcfnotfound.md).

## Discussion

This function is intended to be used in conjunction with the [CFURLGetBytes](<cfurlgetbytes(______).md>) function, since the range returned is only applicable to the bytes returned by [CFURLGetBytes](<cfurlgetbytes(______).md>).

## See Also

### Getting URL Properties

- [CFURLGetBaseURL](<cfurlgetbaseurl(__).md>) — Returns the base URL of a given URL if it exists.
- [CFURLGetBytes](<cfurlgetbytes(______).md>) — Returns by reference the byte representation of a URL object.
- [CFURLGetTypeID](<cfurlgettypeid().md>) — Returns the type identifier for the `CFURL` opaque type.
- [CFURLResourceIsReachable](<cfurlresourceisreachable(____).md>) — Returns whether the resource pointed to by a file URL can be reached.

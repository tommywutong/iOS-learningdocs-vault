---
title: skipInvisibles
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlenumeratoroptions/skipinvisibles
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/skipinvisibles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratoroptions/skipinvisibles.json'
content_hash: 'sha256:81d159f1eb9407e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLEnumeratorOptions](../cfurlenumeratoroptions.md)

# skipInvisibles

<sub>Type Property</sub>

The enumerator skips “hidden” or “invisible” objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var skipInvisibles: CFURLEnumeratorOptions { get }
```

## See Also

### Constants

- [kCFURLEnumeratorDescendRecursively](descendrecursively.md) — The enumerator recurses into each subdirectory enumerated.
- [kCFURLEnumeratorGenerateFileReferenceURLs](generatefilereferenceurls.md) — The enumerator generates file reference URLs instead of file path URLs.
- [kCFURLEnumeratorSkipPackageContents](skippackagecontents.md) — The enumerator skips package directory contents.
- [kCFURLEnumeratorIncludeDirectoriesPreOrder](includedirectoriespreorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [kCFURLEnumeratorIncludeDirectoriesPostOrder](includedirectoriespostorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.

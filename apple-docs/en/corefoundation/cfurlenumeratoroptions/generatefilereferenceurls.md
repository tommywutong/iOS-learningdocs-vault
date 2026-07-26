---
title: generateFileReferenceURLs
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlenumeratoroptions/generatefilereferenceurls
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/generatefilereferenceurls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratoroptions/generatefilereferenceurls.json'
content_hash: 'sha256:692704b8014c3012'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLEnumeratorOptions](../cfurlenumeratoroptions.md)

# generateFileReferenceURLs

<sub>Type Property</sub>

The enumerator generates file reference URLs instead of file path URLs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var generateFileReferenceURLs: CFURLEnumeratorOptions { get }
```

## Discussion

This option applies only to volume enumerators.

## See Also

### Constants

- [kCFURLEnumeratorDescendRecursively](descendrecursively.md) — The enumerator recurses into each subdirectory enumerated.
- [kCFURLEnumeratorSkipInvisibles](skipinvisibles.md) — The enumerator skips “hidden” or “invisible” objects.
- [kCFURLEnumeratorSkipPackageContents](skippackagecontents.md) — The enumerator skips package directory contents.
- [kCFURLEnumeratorIncludeDirectoriesPreOrder](includedirectoriespreorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [kCFURLEnumeratorIncludeDirectoriesPostOrder](includedirectoriespostorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.

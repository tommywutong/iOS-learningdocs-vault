---
title: includeDirectoriesPreOrder
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlenumeratoroptions/includedirectoriespreorder
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/includedirectoriespreorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratoroptions/includedirectoriespreorder.json'
content_hash: 'sha256:c7ddc1edf83af3b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLEnumeratorOptions](../cfurlenumeratoroptions.md)

# includeDirectoriesPreOrder

<sub>Type Property</sub>

If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var includeDirectoriesPreOrder: CFURLEnumeratorOptions { get }
```

## See Also

### Constants

- [kCFURLEnumeratorDescendRecursively](descendrecursively.md) — The enumerator recurses into each subdirectory enumerated.
- [kCFURLEnumeratorSkipInvisibles](skipinvisibles.md) — The enumerator skips “hidden” or “invisible” objects.
- [kCFURLEnumeratorGenerateFileReferenceURLs](generatefilereferenceurls.md) — The enumerator generates file reference URLs instead of file path URLs.
- [kCFURLEnumeratorSkipPackageContents](skippackagecontents.md) — The enumerator skips package directory contents.
- [kCFURLEnumeratorIncludeDirectoriesPostOrder](includedirectoriespostorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.

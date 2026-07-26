---
title: includeDirectoriesPostOrder
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlenumeratoroptions/includedirectoriespostorder
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/includedirectoriespostorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratoroptions/includedirectoriespostorder.json'
content_hash: 'sha256:6e942ccbe1261e1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLEnumeratorOptions](../cfurlenumeratoroptions.md)

# includeDirectoriesPostOrder

<sub>Type Property</sub>

If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var includeDirectoriesPostOrder: CFURLEnumeratorOptions { get }
```

## Discussion

A recursive post-order enumerator returns [kCFURLEnumeratorDirectoryPostOrderSuccess](../cfurlenumeratorresult/directorypostordersuccess.md) when it returns a directory’s URL after returning the directory’s descendents.

## See Also

### Constants

- [kCFURLEnumeratorDescendRecursively](descendrecursively.md) — The enumerator recurses into each subdirectory enumerated.
- [kCFURLEnumeratorSkipInvisibles](skipinvisibles.md) — The enumerator skips “hidden” or “invisible” objects.
- [kCFURLEnumeratorGenerateFileReferenceURLs](generatefilereferenceurls.md) — The enumerator generates file reference URLs instead of file path URLs.
- [kCFURLEnumeratorSkipPackageContents](skippackagecontents.md) — The enumerator skips package directory contents.
- [kCFURLEnumeratorIncludeDirectoriesPreOrder](includedirectoriespreorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.

---
title: descendRecursively
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlenumeratoroptions/descendrecursively
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/descendrecursively'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratoroptions/descendrecursively.json'
content_hash: 'sha256:74e418d8e0d0bcac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLEnumeratorOptions](../cfurlenumeratoroptions.md)

# descendRecursively

<sub>Type Property</sub>

The enumerator recurses into each subdirectory enumerated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var descendRecursively: CFURLEnumeratorOptions { get }
```

## Discussion

This option applies only to directory enumerators.

You can enumerate the directories that a recursive enumerator encounters in pre-order fashion, post-order fashion, or both, by providing a combination of the [kCFURLEnumeratorIncludeDirectoriesPreOrder](includedirectoriespreorder.md) and [kCFURLEnumeratorIncludeDirectoriesPostOrder](includedirectoriespostorder.md) options. If you provide neither option, the recursive enumerator behaves as if it was provided the [kCFURLEnumeratorIncludeDirectoriesPreOrder](includedirectoriespreorder.md) option.

## See Also

### Constants

- [kCFURLEnumeratorSkipInvisibles](skipinvisibles.md) — The enumerator skips “hidden” or “invisible” objects.
- [kCFURLEnumeratorGenerateFileReferenceURLs](generatefilereferenceurls.md) — The enumerator generates file reference URLs instead of file path URLs.
- [kCFURLEnumeratorSkipPackageContents](skippackagecontents.md) — The enumerator skips package directory contents.
- [kCFURLEnumeratorIncludeDirectoriesPreOrder](includedirectoriespreorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [kCFURLEnumeratorIncludeDirectoriesPostOrder](includedirectoriespostorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.

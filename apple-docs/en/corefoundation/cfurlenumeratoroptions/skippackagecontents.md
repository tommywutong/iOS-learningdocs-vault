---
title: skipPackageContents
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlenumeratoroptions/skippackagecontents
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/skippackagecontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratoroptions/skippackagecontents.json'
content_hash: 'sha256:85fd0d44d41cca54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLEnumeratorOptions](../cfurlenumeratoroptions.md)

# skipPackageContents

<sub>Type Property</sub>

The enumerator skips package directory contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var skipPackageContents: CFURLEnumeratorOptions { get }
```

## Discussion

This option applies only to directory enumerators.

## See Also

### Constants

- [kCFURLEnumeratorDescendRecursively](descendrecursively.md) — The enumerator recurses into each subdirectory enumerated.
- [kCFURLEnumeratorSkipInvisibles](skipinvisibles.md) — The enumerator skips “hidden” or “invisible” objects.
- [kCFURLEnumeratorGenerateFileReferenceURLs](generatefilereferenceurls.md) — The enumerator generates file reference URLs instead of file path URLs.
- [kCFURLEnumeratorIncludeDirectoriesPreOrder](includedirectoriespreorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [kCFURLEnumeratorIncludeDirectoriesPostOrder](includedirectoriespostorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.

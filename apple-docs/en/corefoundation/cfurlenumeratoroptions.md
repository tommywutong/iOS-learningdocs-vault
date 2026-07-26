---
title: CFURLEnumeratorOptions
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlenumeratoroptions
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratoroptions.json'
content_hash: 'sha256:3cbb02242fa011da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLEnumeratorOptions

<sub>Structure</sub>

Options for controlling enumerator behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFURLEnumeratorOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFURLEnumeratorDescendRecursively](cfurlenumeratoroptions/descendrecursively.md) — The enumerator recurses into each subdirectory enumerated.
- [kCFURLEnumeratorSkipInvisibles](cfurlenumeratoroptions/skipinvisibles.md) — The enumerator skips “hidden” or “invisible” objects.
- [kCFURLEnumeratorGenerateFileReferenceURLs](cfurlenumeratoroptions/generatefilereferenceurls.md) — The enumerator generates file reference URLs instead of file path URLs.
- [kCFURLEnumeratorSkipPackageContents](cfurlenumeratoroptions/skippackagecontents.md) — The enumerator skips package directory contents.
- [kCFURLEnumeratorIncludeDirectoriesPreOrder](cfurlenumeratoroptions/includedirectoriespreorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [kCFURLEnumeratorIncludeDirectoriesPostOrder](cfurlenumeratoroptions/includedirectoriespostorder.md) — If provided along with the [kCFURLEnumeratorDescendRecursively](cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.

### Initializers

- [init(rawValue:)](<cfurlenumeratoroptions/init(rawvalue_).md>)

### Type Properties

- [kCFURLEnumeratorGenerateRelativePathURLs](cfurlenumeratoroptions/generaterelativepathurls.md)

## See Also

### Enumerations

- [CFFileSecurityClearOptions](cffilesecurityclearoptions.md)
- [CFISO8601DateFormatOptions](cfiso8601dateformatoptions.md)
- [CFRunLoopRunResult](cfrunlooprunresult.md)
- [CFURLEnumeratorResult](cfurlenumeratorresult.md) — Result codes from the [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function.
- [CGRectEdge](cgrectedge.md)

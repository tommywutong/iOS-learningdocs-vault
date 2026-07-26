---
title: CFURLEnumeratorResult
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlenumeratorresult
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratorresult.json'
content_hash: 'sha256:3eb061e82db0e37e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLEnumeratorResult

<sub>Enumeration</sub>

Result codes from the [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFURLEnumeratorResult
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFURLEnumeratorSuccess](cfurlenumeratorresult/success.md) — The enumerator was advanced successfully and returned a valid URL.
- [kCFURLEnumeratorEnd](cfurlenumeratorresult/end.md) — The enumeration is complete.
- [kCFURLEnumeratorError](cfurlenumeratorresult/error.md) — An error occurred during enumeration. The `error` parameter of the function is populated with error information.
- [kCFURLEnumeratorDirectoryPostOrderSuccess](cfurlenumeratorresult/directorypostordersuccess.md) — The recursive post-order enumerator returned the URL for a directory after having returned the URLs for all of the directory’s descendents.

### Initializers

- [init(rawValue:)](<cfurlenumeratorresult/init(rawvalue_).md>)

## See Also

### Enumerations

- [CFFileSecurityClearOptions](cffilesecurityclearoptions.md)
- [CFISO8601DateFormatOptions](cfiso8601dateformatoptions.md)
- [CFRunLoopRunResult](cfrunlooprunresult.md)
- [CFURLEnumeratorOptions](cfurlenumeratoroptions.md) — Options for controlling enumerator behavior.
- [CGRectEdge](cgrectedge.md)

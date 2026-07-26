---
title: NSItemProviderFileOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemproviderfileoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderfileoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderfileoptions.json'
content_hash: 'sha256:8695895d3e66b640'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSItemProviderFileOptions

<sub>Structure</sub>

Data-access specifications that declare how to handle items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSItemProviderFileOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Creating File Options

- [init(rawValue:)](<nsitemproviderfileoptions/init(rawvalue_).md>)

### File Options

- [NSItemProviderFileOptionOpenInPlace](nsitemproviderfileoptions/openinplace.md) — A data-access specification declaring that items should open in place, rather than being copied.

## See Also

### Constants

- [CompletionHandler](nsitemprovider/completionhandler.md) — A block that receives the item provider’s data.
- [LoadHandler](nsitemprovider/loadhandler.md) — A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](options-dictionary-key.md) — Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](keys-for-items-accessed-in-javascript-code.md) — Keys in property list items that the system recieves from or sends to JavaScript code.
- [NSItemProviderErrorDomain](nsitemprovider/errordomain.md) — The error domain associated with the item provider.
- [NSItemProviderReading](nsitemproviderreading.md) — The protocol for implementing a class to allow an item provider to create an instance of the class.
- [NSItemProviderWriting](nsitemproviderwriting.md) — The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md) — Specifications that control which categories of processes can see an item.
- [ErrorCode](nsitemprovider/errorcode.md) — The error codes that describe problems with consuming data from an item provider.

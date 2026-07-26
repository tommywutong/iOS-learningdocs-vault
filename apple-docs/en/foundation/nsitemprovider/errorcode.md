---
title: NSItemProvider.ErrorCode
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/errorcode
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/errorcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/errorcode.json'
content_hash: 'sha256:2517ec8ca3e261df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# NSItemProvider.ErrorCode

<sub>Enumeration</sub>

The error codes that describe problems with consuming data from an item provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ErrorCode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSItemProviderItemUnavailableError](errorcode/itemunavailableerror.md) — An error code indicating that the requested data was unavailable from an item provider.
- [NSItemProviderUnavailableCoercionError](errorcode/unavailablecoercionerror.md) — An error code indicating that the requested data type coercion is unavailable from an item provider.
- [NSItemProviderUnexpectedValueClassError](errorcode/unexpectedvalueclasserror.md) — An error code indicating that type coercion to the requested class failed.
- [NSItemProviderUnknownError](errorcode/unknownerror.md) — An error code indicating an unknown error with consuming data from an item provider.

### Initializers

- [init(rawValue:)](<errorcode/init(rawvalue_).md>)

## See Also

### Constants

- [CompletionHandler](completionhandler.md) — A block that receives the item provider’s data.
- [LoadHandler](loadhandler.md) — A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](../options-dictionary-key.md) — Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](../keys-for-items-accessed-in-javascript-code.md) — Keys in property list items that the system recieves from or sends to JavaScript code.
- [NSItemProviderErrorDomain](errordomain.md) — The error domain associated with the item provider.
- [NSItemProviderFileOptions](../nsitemproviderfileoptions.md) — Data-access specifications that declare how to handle items.
- [NSItemProviderReading](../nsitemproviderreading.md) — The protocol for implementing a class to allow an item provider to create an instance of the class.
- [NSItemProviderWriting](../nsitemproviderwriting.md) — The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [NSItemProviderRepresentationVisibility](../nsitemproviderrepresentationvisibility.md) — Specifications that control which categories of processes can see an item.

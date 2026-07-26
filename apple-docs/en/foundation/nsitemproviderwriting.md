---
title: NSItemProviderWriting
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemproviderwriting
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderwriting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderwriting.json'
content_hash: 'sha256:fe364b3ec3ef2386'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSItemProviderWriting

<sub>Protocol</sub>

The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSItemProviderWriting : NSObjectProtocol
```

## Overview

A source app uses an object that conforms to this protocol to initialize an item provider for a copied or dragged item.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSAttributedString](nsattributedstring.md), [NSMutableString](nsmutablestring.md), [NSString](nsstring.md), [NSURL](nsurl.md), [NSUserActivity](nsuseractivity.md)

## Topics

### Loading data

- [- loadDataWithTypeIdentifier:forItemProviderCompletionHandler:](<nsitemproviderwriting/loaddata(withtypeidentifier_foritemprovidercompletionhandler_).md>) — Loads data of a particular type, identified by the given UTI.

### Getting the writable type identifiers

- [writableTypeIdentifiersForItemProvider](nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.type.property.md) — An array of UTI strings representing the types of data that can be loaded for an item provider.
- [writableTypeIdentifiersForItemProvider](nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.property.md) — An array of UTI strings representing the types of data that can be loaded for an item provider.

### Getting the representation visibility specification

- [+ itemProviderVisibilityForRepresentationWithTypeIdentifier:](<nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier_)-swift.type.method.md>) — Asks the item provider for the default representation visibility specification for the given UTI.
- [- itemProviderVisibilityForRepresentationWithTypeIdentifier:](<nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier_)-swift.method.md>) — Asks the item provider for the representation visibility specification for the given UTI.

## See Also

### Constants

- [CompletionHandler](nsitemprovider/completionhandler.md) — A block that receives the item provider’s data.
- [LoadHandler](nsitemprovider/loadhandler.md) — A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](options-dictionary-key.md) — Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](keys-for-items-accessed-in-javascript-code.md) — Keys in property list items that the system recieves from or sends to JavaScript code.
- [NSItemProviderErrorDomain](nsitemprovider/errordomain.md) — The error domain associated with the item provider.
- [NSItemProviderFileOptions](nsitemproviderfileoptions.md) — Data-access specifications that declare how to handle items.
- [NSItemProviderReading](nsitemproviderreading.md) — The protocol for implementing a class to allow an item provider to create an instance of the class.
- [NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md) — Specifications that control which categories of processes can see an item.
- [ErrorCode](nsitemprovider/errorcode.md) — The error codes that describe problems with consuming data from an item provider.

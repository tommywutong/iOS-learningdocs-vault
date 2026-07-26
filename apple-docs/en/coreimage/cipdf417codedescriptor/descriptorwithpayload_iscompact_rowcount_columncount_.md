---
title: 'descriptorWithPayload:isCompact:rowCount:columnCount:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cipdf417codedescriptor/descriptorwithpayload:iscompact:rowcount:columncount:'
source_url: 'https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/descriptorwithpayload:iscompact:rowcount:columncount:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipdf417codedescriptor/descriptorwithpayload%3Aiscompact%3Arowcount%3Acolumncount%3A.json'
content_hash: 'sha256:2e5bc1e00b6bd16c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPDF417CodeDescriptor](../cipdf417codedescriptor.md)

# descriptorWithPayload:isCompact:rowCount:columnCount:

<sub>Type Method</sub>

Creates an PDF417 code descriptor for the given payload and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) descriptorWithPayload:(NSData *) errorCorrectedPayload isCompact:(BOOL) isCompact rowCount:(NSInteger) rowCount columnCount:(NSInteger) columnCount;
```

## Parameters

- `errorCorrectedPayload` — The data to encode in the PDF417 code symbol.

- `isCompact` — A Boolean indicating whether or not the PDF417 code is compact.

- `rowCount` — The number of rows in the PDF417 code, from 3 to 90.

- `columnCount` — The number of columns in the Aztec code, from 1 to 30.

## Return Value

An autoreleased [CIPDF417CodeDescriptor](../cipdf417codedescriptor.md) instance or `nil` if the parameters are invalid

## See Also

### Creating a Descriptor

- [- initWithPayload:isCompact:rowCount:columnCount:](<init(payload_iscompact_rowcount_columncount_).md>) — Initializes an PDF417 code descriptor for the given payload and parameters.

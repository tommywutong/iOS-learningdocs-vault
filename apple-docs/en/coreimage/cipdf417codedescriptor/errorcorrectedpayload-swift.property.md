---
title: errorCorrectedPayload
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipdf417codedescriptor/errorcorrectedpayload-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/errorcorrectedpayload-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipdf417codedescriptor/errorcorrectedpayload-swift.property.json'
content_hash: 'sha256:1c837984f1ef2928'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPDF417CodeDescriptor](../cipdf417codedescriptor.md)

# errorCorrectedPayload

<sub>Instance Property</sub>

The error-corrected payload containing the data encoded in the PDF417 code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var errorCorrectedPayload: Data { get }
```

## Discussion

The first codeword indicates the number of data codewords in the errorCorrectedPayload.

PDF417 codes are comprised of a start character on the left and a stop character on the right. Each row begins and ends with special characters indicating the current row as well as information about the dimensions of the PDF417 symbol. The errorCorrectedPayload represents the sequence of PDF417 codewords that make up the body of the message. The first codeword indicates the number of codewords in the message. This count includes the “count” codeword and any padding codewords, but does not include the error correction codewords. Each codeword is a 16-bit value in the range of 0…928. The sequence is to be interpreted as described in the PDF417 bar code symbology specification – ISO/IEC 15438:2006(E).

## See Also

### Examining a Descriptor

- [isCompact](iscompact-swift.property.md) — A boolean value telling if the PDF417 code is compact.
- [rowCount](rowcount-swift.property.md) — The number of rows in the PDF417 code symbol.
- [columnCount](columncount-swift.property.md) — The number of columns in the PDF417 code symbol.

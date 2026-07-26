---
title: AVMetadataObject.ObjectType
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataobject/objecttype
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataobject/objecttype.json'
content_hash: 'sha256:b16fca7c17652da7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataObject](../avmetadataobject.md)

# AVMetadataObject.ObjectType

<sub>Structure</sub>

Constants that identify metadata object types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
struct ObjectType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Barcodes

- [AVMetadataObjectTypeCodabarCode](objecttype/codabar.md) — A constant that identifies the Codabar symbology.
- [AVMetadataObjectTypeCode39Code](objecttype/code39.md) — A constant that identifies the Code 39 symbology.
- [AVMetadataObjectTypeCode39Mod43Code](objecttype/code39mod43.md) — A constant that identifies the Code 39 mod 43 symbology.
- [AVMetadataObjectTypeCode93Code](objecttype/code93.md) — A constant that identifies the Code 93 symbology.
- [AVMetadataObjectTypeCode128Code](objecttype/code128.md) — A constant that identifies the Code 128 symbology.
- [AVMetadataObjectTypeEAN8Code](objecttype/ean8.md) — A constant that identifies the EAN-8 symbology.
- [AVMetadataObjectTypeEAN13Code](objecttype/ean13.md) — A constant that identifies the EAN-13 symbology.
- [AVMetadataObjectTypeGS1DataBarCode](objecttype/gs1databar.md) — A constant that identifies the GS1 DataBar symbology.
- [AVMetadataObjectTypeGS1DataBarExpandedCode](objecttype/gs1databarexpanded.md) — A constant that identifies the GS1 DataBar Expanded symbology.
- [AVMetadataObjectTypeGS1DataBarLimitedCode](objecttype/gs1databarlimited.md) — A constant that identifies the GS1 DataBar Limited symbology.
- [AVMetadataObjectTypeInterleaved2of5Code](objecttype/interleaved2of5.md) — A constant that identifies the Interleaved 2 of 5 symbology.
- [AVMetadataObjectTypeITF14Code](objecttype/itf14.md) — A constant that identifies the ITF14 symbology.
- [AVMetadataObjectTypeUPCECode](objecttype/upce.md) — A constant that identifies the UPC-E symbology.

### 2D codes

- [AVMetadataObjectTypeAztecCode](objecttype/aztec.md) — A constant that identifies the Aztec symbology.
- [AVMetadataObjectTypeDataMatrixCode](objecttype/datamatrix.md) — A constant that identifies the DataMatrix symbology.
- [AVMetadataObjectTypeMicroPDF417Code](objecttype/micropdf417.md) — A constant that identifies the Micro PDF417 symbology.
- [AVMetadataObjectTypeMicroQRCode](objecttype/microqr.md) — A constant that identifies the Micro QR symbology.
- [AVMetadataObjectTypePDF417Code](objecttype/pdf417.md) — A constant that identifies the PDF417 symbology.
- [AVMetadataObjectTypeQRCode](objecttype/qr.md) — A constant that identifies the QR symbology.

### Bodies

- [AVMetadataObjectTypeHumanBody](objecttype/humanbody.md) — A constant that identifies human body metadata.
- [AVMetadataObjectTypeHumanFullBody](objecttype/humanfullbody.md) — A constant that identifies human full body metadata.
- [AVMetadataObjectTypeDogHead](objecttype/doghead.md) — An identifier for an instance of a dog head object.
- [AVMetadataObjectTypeDogBody](objecttype/dogbody.md) — A constant that identifies dog body metadata.
- [AVMetadataObjectTypeCatHead](objecttype/cathead.md) — An identifier for an instance of a cat head object.
- [AVMetadataObjectTypeCatBody](objecttype/catbody.md) — A constant that identifies cat body metadata.

### Faces

- [AVMetadataObjectTypeFace](objecttype/face.md) — A constant that identifies face metadata.

### Saliency

- [AVMetadataObjectTypeSalientObject](objecttype/salientobject.md) — A constant that identifies saliency metadata.

### Initializers

- [init(rawValue:)](<objecttype/init(rawvalue_).md>) — Creates a metadata object type with a string value.

## See Also

### Inspecting the metadata

- [bounds](bounds.md) — The bounding rectangle associated with the metadata.
- [duration](duration.md) — The duration of the media associated with this metadata object.
- [time](time.md) — The media time value associated with the metadata object.
- [type](type.md) — The type of metadata that this object provides.
- [fixedFocus](isfixedfocus.md) — A BOOL indicating whether this metadata object represents a fixed focus.
- [cinematicVideoFocusMode](cinematicvideofocusmode.md) — The current focus mode when an object is detected during a Cinematic Video recording.
- [groupID](groupid.md) — An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.
- [objectID](objectid.md) — A unique identifier for each detected object type (face, body, hands, heads and salient objects) in a collection.

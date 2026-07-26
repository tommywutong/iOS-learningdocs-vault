---
title: Machine-readable object types
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/machine-readable-object-types
source_url: 'https://developer.apple.com/documentation/avfoundation/machine-readable-object-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/machine-readable-object-types.json'
content_hash: 'sha256:a5d0a457d514f289'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Additional data capture](additional-data-capture.md) · [Metadata types](metadata-types.md) · [AVMetadataMachineReadableCodeObject](avmetadatamachinereadablecodeobject.md)

# Machine-readable object types

<sub>API Collection</sub>

Constants used to specify the type of barcode to scan.

## Overview

These constants are used in conjunction with the [AVCaptureMetadataOutput](avcapturemetadataoutput.md) class’s [metadataObjectTypes](avcapturemetadataoutput/metadataobjecttypes.md) property to specify the type (“symbology”) of barcode to scan. When a barcode is detected, the type property of `AVMetadataMachineReadableCodeObject` reflects the constant for the detected barcode’s symbology.

## Topics

### Constants

- [AVMetadataObjectTypeUPCECode](avmetadataobject/objecttype/upce.md) — A constant that identifies the UPC-E symbology.
- [AVMetadataObjectTypeCode39Code](avmetadataobject/objecttype/code39.md) — A constant that identifies the Code 39 symbology.
- [AVMetadataObjectTypeCode39Mod43Code](avmetadataobject/objecttype/code39mod43.md) — A constant that identifies the Code 39 mod 43 symbology.
- [AVMetadataObjectTypeEAN13Code](avmetadataobject/objecttype/ean13.md) — A constant that identifies the EAN-13 symbology.
- [AVMetadataObjectTypeEAN8Code](avmetadataobject/objecttype/ean8.md) — A constant that identifies the EAN-8 symbology.
- [AVMetadataObjectTypeCode93Code](avmetadataobject/objecttype/code93.md) — A constant that identifies the Code 93 symbology.
- [AVMetadataObjectTypeCode128Code](avmetadataobject/objecttype/code128.md) — A constant that identifies the Code 128 symbology.
- [AVMetadataObjectTypePDF417Code](avmetadataobject/objecttype/pdf417.md) — A constant that identifies the PDF417 symbology.
- [AVMetadataObjectTypeQRCode](avmetadataobject/objecttype/qr.md) — A constant that identifies the QR symbology.
- [AVMetadataObjectTypeAztecCode](avmetadataobject/objecttype/aztec.md) — A constant that identifies the Aztec symbology.
- [AVMetadataObjectTypeInterleaved2of5Code](avmetadataobject/objecttype/interleaved2of5.md) — A constant that identifies the Interleaved 2 of 5 symbology.
- [AVMetadataObjectTypeITF14Code](avmetadataobject/objecttype/itf14.md) — A constant that identifies the ITF14 symbology.
- [AVMetadataObjectTypeDataMatrixCode](avmetadataobject/objecttype/datamatrix.md) — A constant that identifies the DataMatrix symbology.

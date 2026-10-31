---
title: 机器可读对象类型
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
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [附加数据捕获](additional-data-capture.md) · [元数据类型](metadata-types.md) · [AVMetadataMachineReadableCodeObject](avmetadatamachinereadablecodeobject.md)

# 机器可读对象类型

<sub>API 集合</sub>

用于指定要扫描的条形码类型的常量。

## 概述

这些常量与 [AVCaptureMetadataOutput](avcapturemetadataoutput.md) 类的 [metadataObjectTypes](avcapturemetadataoutput/metadataobjecttypes.md) 属性配合使用，用于指定要扫描的条形码类型（即「编码系统」）。当检测到条形码时，`AVMetadataMachineReadableCodeObject` 的 type 属性会反映所检测到的条形码编码系统对应的常量。

## 主题

### 常量

- [AVMetadataObjectTypeUPCECode](avmetadataobject/objecttype/upce.md) — 标识 UPC-E 编码系统的常量。
- [AVMetadataObjectTypeCode39Code](avmetadataobject/objecttype/code39.md) — 标识 Code 39 编码系统的常量。
- [AVMetadataObjectTypeCode39Mod43Code](avmetadataobject/objecttype/code39mod43.md) — 标识 Code 39 mod 43 编码系统的常量。
- [AVMetadataObjectTypeEAN13Code](avmetadataobject/objecttype/ean13.md) — 标识 EAN-13 编码系统的常量。
- [AVMetadataObjectTypeEAN8Code](avmetadataobject/objecttype/ean8.md) — 标识 EAN-8 编码系统的常量。
- [AVMetadataObjectTypeCode93Code](avmetadataobject/objecttype/code93.md) — 标识 Code 93 编码系统的常量。
- [AVMetadataObjectTypeCode128Code](avmetadataobject/objecttype/code128.md) — 标识 Code 128 编码系统的常量。
- [AVMetadataObjectTypePDF417Code](avmetadataobject/objecttype/pdf417.md) — 标识 PDF417 编码系统的常量。
- [AVMetadataObjectTypeQRCode](avmetadataobject/objecttype/qr.md) — 标识 QR 编码系统的常量。
- [AVMetadataObjectTypeAztecCode](avmetadataobject/objecttype/aztec.md) — 标识 Aztec 编码系统的常量。
- [AVMetadataObjectTypeInterleaved2of5Code](avmetadataobject/objecttype/interleaved2of5.md) — 标识 Interleaved 2 of 5 编码系统的常量。
- [AVMetadataObjectTypeITF14Code](avmetadataobject/objecttype/itf14.md) — 标识 ITF14 编码系统的常量。
- [AVMetadataObjectTypeDataMatrixCode](avmetadataobject/objecttype/datamatrix.md) — 标识 DataMatrix 编码系统的常量。

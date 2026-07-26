---
title: Metadata types
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/metadata-types
source_url: 'https://developer.apple.com/documentation/avfoundation/metadata-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/metadata-types.json'
content_hash: 'sha256:75daaaf400c330fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Additional data capture](additional-data-capture.md)

# Metadata types

<sub>API Collection</sub>

Inspect the supported metadata object types that the framework supports.

## Topics

### 2D and 3D codes

- [AVMetadataMachineReadableCodeObject](avmetadatamachinereadablecodeobject.md) — Barcode information detected by a metadata capture output.

### Faces

- [AVMetadataFaceObject](avmetadatafaceobject.md) — Face information detected by a metadata capture output.

### Heads

- [AVMetadataCatHeadObject](avmetadatacatheadobject.md) — A concrete metadata object subclass representing a cat head.
- [AVMetadataDogHeadObject](avmetadatadogheadobject.md) — A concrete metadata object subclass representing a dog head.

### Bodies

- [AVMetadataBodyObject](avmetadatabodyobject.md) — An abstract class that defines the interface for a metadata body object.
- [AVMetadataCatBodyObject](avmetadatacatbodyobject.md) — An object representing a single detected cat body in a picture.
- [AVMetadataDogBodyObject](avmetadatadogbodyobject.md) — An object representing a single detected dog body in a picture.
- [AVMetadataHumanBodyObject](avmetadatahumanbodyobject.md) — An object representing a single detected human body in a picture.
- [AVMetadataHumanFullBodyObject](avmetadatahumanfullbodyobject.md) — An object that represents a detected human full body in a picture.

### Saliency

- [AVMetadataSalientObject](avmetadatasalientobject.md) — An object representing a single salient area in a picture.

## See Also

### Metadata capture

- [AVCaptureMetadataInput](avcapturemetadatainput.md) — A capture input for providing timed metadata to a capture session.
- [AVCaptureMetadataOutput](avcapturemetadataoutput.md) — A capture output for processing timed metadata produced by a capture session.
- [AVMetadataObject](avmetadataobject.md) — The abstract superclass for objects provided by a metadata capture output.

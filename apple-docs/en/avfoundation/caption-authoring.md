---
title: Caption authoring
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/caption-authoring
source_url: 'https://developer.apple.com/documentation/avfoundation/caption-authoring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/caption-authoring.json'
content_hash: 'sha256:c724d946b3bf2142'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media reading and writing](media-reading-and-writing.md)

# Caption authoring

<sub>API Collection</sub>

Create captions and subtitles in industry-standard formats.

## Topics

### Captions

- [AVCaption](avcaption.md) — An object that represents text to present over a time range.
- [AVMutableCaption](avmutablecaption.md) — A mutable caption subclass that you use to create new captions.

### Regions

- [AVCaptionRegion](avcaptionregion.md) — An object that represents the region in which the system presents a caption.
- [AVMutableCaptionRegion](avmutablecaptionregion.md) — A mutable caption region subclass that you use to create new caption regions.

### Groups

- [AVCaptionGroup](avcaptiongroup.md) — An object that represents zero or more captions that intersect in time.
- [AVCaptionGrouper](avcaptiongrouper.md) — An object that analyzes the temporal overlaps of caption objects to create caption groups for each span of concurrent captions.

### Presentation

- [AVCaptionRenderer](avcaptionrenderer.md) — An object that renders captions for display at a particular time.

### Reading and writing

- [AVAssetReaderOutputCaptionAdaptor](avassetreaderoutputcaptionadaptor.md) — An object that reads caption group objects from an asset track that contains timed text. _(deprecated)_
- [AVAssetWriterInputCaptionAdaptor](avassetwriterinputcaptionadaptor.md) — An object that appends captions to an asset writer input. _(deprecated)_

### Conversion and validation

- [AVCaptionSettingsKey](avcaptionsettingskey.md) — A structure that defines dictionary keys to configure the caption converter and validator.
- [AVCaptionFormatConformer](avcaptionformatconformer.md) — An object that converts a canonical caption to a specific format.
- [AVCaptionConversionValidator](avcaptionconversionvalidator.md) — An object that validates captions for a conversion operation.

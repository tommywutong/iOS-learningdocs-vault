---
title: CAEDRMetadata
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caedrmetadata
source_url: 'https://developer.apple.com/documentation/quartzcore/caedrmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caedrmetadata.json'
content_hash: 'sha256:db5006284ef80b5f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAEDRMetadata

<sub>Class</sub>

Metadata describing how extended dynamic range (EDR) values should be tone mapped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class CAEDRMetadata
```

## Overview

If you need specific tone-mapping behavior, set the [EDRMetadata](cametallayer/edrmetadata.md) property of a [CAMetalLayer](cametallayer.md) to point to an instance of this class.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Retrieving Hybrid-Log Gamma Metadata

- [HLGMetadata](caedrmetadata/hlg.md) — Extended dynamic range (EDR) metadata for the Hybrid Log-Gamma (HLG) transfer function.

### Retrieving HDR10 Metadata

- [+ HDR10MetadataWithDisplayInfo:contentInfo:opticalOutputScale:](<caedrmetadata/hdr10(displayinfo_contentinfo_opticaloutputscale_).md>) — Creates EDR metadata for HDR10 content based on mastering display color information and content light levels.
- [+ HDR10MetadataWithMinLuminance:maxLuminance:opticalOutputScale:](<caedrmetadata/hdr10(minluminance_maxluminance_opticaloutputscale_).md>) — Creates EDR metadata for HDR10 content based on the luminance characteristics of a mastering display.

### Type Properties

- [available](caedrmetadata/isavailable.md)

### Type Methods

- [+ HLGMetadataWithAmbientViewingEnvironment:](<caedrmetadata/hlg(ambientviewingenvironment_).md>)

### Initializers

- [init(coder:)](<caedrmetadata/init(coder_).md>)

## See Also

### Metal and OpenGL

- [CAMetalLayer](cametallayer.md) — A Core Animation layer that Metal can render into, typically displayed onscreen.
- [CAMetalDrawable](cametaldrawable.md) — A Metal drawable associated with a Core Animation layer.
- [CAEAGLLayer](caeagllayer.md) — A layer that supports drawing OpenGL content in iOS and tvOS applications. _(deprecated)_
- [CAOpenGLLayer](caopengllayer.md) — A layer that provides a layer suitable for rendering OpenGL content. _(deprecated)_
- [CARenderer](carenderer.md) — A layer that allows an application to render a layer tree into a Core OpenGL context.

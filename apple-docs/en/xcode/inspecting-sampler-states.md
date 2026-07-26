---
title: Inspecting sampler states
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/inspecting-sampler-states
source_url: 'https://developer.apple.com/documentation/xcode/inspecting-sampler-states'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/inspecting-sampler-states.json'
content_hash: 'sha256:669a7fec8034f8b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal debugger](metal-debugger.md)

# Inspecting sampler states

<sub>Article</sub>

Verify your sampler state configurations by examining their properties.

## Overview

The Metal debugger allows you to inspect a sampler state with the Sampler State viewer. After opening a sampler state, you can view its associated properties and preview the sampling behavior. For more information, see [Inspecting the bound resources for a command](inspecting-the-bound-resources-for-a-command.md) or [Analyzing memory usage](analyzing-memory-usage.md).

### Navigate your sampler state

The Sampler State viewer shows the properties of your sampler state on the left (as configured by [MTLSamplerDescriptor](../metal/mtlsamplerdescriptor.md)) and a preview on the right. The preview illustrates how pixels in a texture appear when using your sampler state.

![](../../../attachments/814897e16f068945b3e238d74cdd1b6c/gputools-metal-debugger-sv-outline@2x.png)

<sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-edge address mode.</sub>

The square region in the center of the preview corresponds to UV coordinates within the range of `0.0` to `1.0`.

![](../../../attachments/50883e4e70e74eb4664a9a4377a816ae/gputools-metal-debugger-sv-outline-green@2x.png)

<sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-edge address mode. The region in bounds is highlighted.</sub>

You can use the preview to quickly verify the configuration for your sampler state. For example, if you want a texture to mirror, but it’s drawing a constant value instead, you can check the sampler state. In the screenshot below, the sampler state is configured to clamp to a border color that’s opaque black, rather than using mirror repeat as the address mode:

![](../../../attachments/947607b5464280b963c5b2aae0363c80/gputools-metal-debugger-sv-nearest-clamp-border-black-plus-overview@2x.png)

<sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-border address mode. The border color is opaque black.</sub>

### Try various combinations

The properties you configure when creating a sampler state determine how a texture looks when sampling it. The properties related to filtering control how pixels combine when the sample footprint is either larger or smaller than a pixel, or when it’s between mipmap levels. The address mode determines the texture coordinate at each pixel when a read falls outside the bounds of a texture. You can try using different combinations of filtering and addressing modes until you achieve your desired look.

| Properties | Preview |
|---|---|
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToEdge](../metal/mtlsampleraddressmode/clamptoedge.md) | ![](../../../attachments/b9f00a20daf0f04a3f7f885f457908c3/gputools-metal-debugger-sv-nearest-clamp@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-edge address mode.</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.mirrorClampToEdge](../metal/mtlsampleraddressmode/mirrorclamptoedge.md) | ![](../../../attachments/fbdbeef91680a8cd6322719b265ae42f/gputools-metal-debugger-sv-nearest-mirror-clamp@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and mirror-clamp-to-edge address mode.</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.repeat](../metal/mtlsampleraddressmode/repeat.md) | ![](../../../attachments/c53b7bf29facfb4610ffc37167a82e26/gputools-metal-debugger-sv-nearest-repeat@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and repeat address mode.</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.mirrorRepeat](../metal/mtlsampleraddressmode/mirrorrepeat.md) | ![](../../../attachments/83abc3f7fc2fe582cafcfcb09d538224/gputools-metal-debugger-sv-nearest-mirror@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and mirror-repeat address mode.</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToZero](../metal/mtlsampleraddressmode/clamptozero.md) | ![](../../../attachments/ef4df8ec925e3e653f21fb4e8374b813/gputools-metal-debugger-sv-nearest-zero@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-zero address mode.</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.opaqueBlack](../metal/mtlsamplerbordercolor/opaqueblack.md) | ![](../../../attachments/ef4df8ec925e3e653f21fb4e8374b813/gputools-metal-debugger-sv-nearest-clamp-border-black@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-border address mode. The border color is opaque black.</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.opaqueWhite](../metal/mtlsamplerbordercolor/opaquewhite.md) | ![](../../../attachments/82d1c051bf85e8d1cfbfe8a22960f47c/gputools-metal-debugger-sv-nearest-clamp-border-white@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-border address mode. The border color is opaque white.</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.transparentBlack](../metal/mtlsamplerbordercolor/transparentblack.md) | ![](../../../attachments/574d56e7b427682155ee48c7a04b3898/gputools-metal-debugger-sv-nearest-clamp-border-transparent@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with nearest filtering and clamp-to-border address mode. The border color is transparent black.</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToEdge](../metal/mtlsampleraddressmode/clamptoedge.md) | ![](../../../attachments/84beb927bfd3cfa7311c3c2fef5e1833/gputools-metal-debugger-sv-linear-clamp@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-edge address mode.</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToEdge](../metal/mtlsampleraddressmode/clamptoedge.md) | ![](../../../attachments/fa81821d87772a5722661d0636aadb2c/gputools-metal-debugger-sv-linear-mirror-clamp@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and mirror-clamp-to-edge address mode.</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.repeat](../metal/mtlsampleraddressmode/repeat.md) | ![](../../../attachments/0b4f5502fbd81fbd0f6d52e97e36550f/gputools-metal-debugger-sv-linear-repeat@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and repeat address mode.</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.mirrorRepeat](../metal/mtlsampleraddressmode/mirrorrepeat.md) | ![](../../../attachments/3b3e6fab82cacc166e20e196a959e97c/gputools-metal-debugger-sv-linear-mirror@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and mirror-repeat address mode.</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToZero](../metal/mtlsampleraddressmode/clamptozero.md) | ![](../../../attachments/5338855da61a2358e21dcd62d2023092/gputools-metal-debugger-sv-linear-zero@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-zero address mode.</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.opaqueBlack](../metal/mtlsamplerbordercolor/opaqueblack.md) | ![](../../../attachments/5338855da61a2358e21dcd62d2023092/gputools-metal-debugger-sv-linear-clamp-border-black@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-border address mode. The border color is opaque black.</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.opaqueWhite](../metal/mtlsamplerbordercolor/opaquewhite.md) | ![](../../../attachments/939248a8d3d668eae179561ed6e798bb/gputools-metal-debugger-sv-linear-clamp-border-white@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-border address mode. The border color is opaque white.</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.transparentBlack](../metal/mtlsamplerbordercolor/transparentblack.md) | ![](../../../attachments/f473b96f45e1282b14919a43ad4149f8/gputools-metal-debugger-sv-linear-clamp-border-transparent@2x.png)  <sub>A screenshot of the Sampler State viewer displaying a sampler state configured with linear filtering and clamp-to-border address mode. The border color is transparent black.</sub> |

## See Also

### Metal resource inspection

- [Inspecting acceleration structures](inspecting-acceleration-structures.md) — Reveal ray intersection bottlenecks by examining your acceleration structures.
- [Inspecting buffers](inspecting-buffers.md) — Confirm your buffer formats by examining buffer content.
- [Inspecting pipeline states](inspecting-pipeline-states.md) — Determine how your render and compute passes behave by examining their properties.
- [Inspecting shaders](inspecting-shaders.md) — Improve your app’s shader performance by examining and editing your shaders.
- [Inspecting textures](inspecting-textures.md) — Discover issues in your textures by examining their content.

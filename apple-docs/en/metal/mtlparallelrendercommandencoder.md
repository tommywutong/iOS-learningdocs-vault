---
title: MTLParallelRenderCommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlparallelrendercommandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlparallelrendercommandencoder.json'
content_hash: 'sha256:a3005beb430045e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLParallelRenderCommandEncoder

<sub>Protocol</sub>

An instance that splits up a single render pass so that it can be simultaneously encoded from multiple threads.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLParallelRenderCommandEncoder : MTLCommandEncoder
```

## Overview

Your app does not define classes that implement this protocol. To create an [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) instance, call the [- parallelRenderCommandEncoderWithDescriptor:](<mtlcommandbuffer/makeparallelrendercommandencoder(descriptor_).md>) method of the [MTLCommandBuffer](mtlcommandbuffer.md) instance that you want to encode the rendering commands into. Then, call the renderCommandEncoder method on this [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) instance to create one or more [MTLRenderCommandEncoder](mtlrendercommandencoder.md) instances. The subordinate [MTLRenderCommandEncoder](mtlrendercommandencoder.md) instances created encode their commands to the same command buffer and target the same [MTLRenderPassAttachmentDescriptor](mtlrenderpassattachmentdescriptor.md) instance. The [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md) instance ensures the attachment load and store actions only occur at the start and end of the entire rendering pass.

You can assign each [MTLRenderCommandEncoder](mtlrendercommandencoder.md) to its own thread and each can encode commands in parallel. You are responsible for any thread synchronization that is required. After all the subordinate encoders have finished encoding their commands, call [- endEncoding](<mtlcommandencoder/endencoding().md>) to execute the commands. The rendering commands are executed in the order that the subordinate encoders were created.

## Relationships

- **Inherits From**: [MTLCommandEncoder](mtlcommandencoder.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a render command encoder

- [- renderCommandEncoder](<mtlparallelrendercommandencoder/makerendercommandencoder().md>) — Create an object that encodes commands that perform graphics rendering operations and may be assigned to a different thread.

### Setting render pass state

- [- setColorStoreAction:atIndex:](<mtlparallelrendercommandencoder/setcolorstoreaction(__index_).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](mtlstoreaction/unknown.md) value specified for a given color attachment.
- [- setColorStoreActionOptions:atIndex:](<mtlparallelrendercommandencoder/setcolorstoreactionoptions(__index_).md>) — Specifies known store action options for a given color attachment. _(deprecated)_
- [- setDepthStoreAction:](<mtlparallelrendercommandencoder/setdepthstoreaction(__).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [- setDepthStoreActionOptions:](<mtlparallelrendercommandencoder/setdepthstoreactionoptions(__).md>) — Specifies known store action options for a given depth attachment. _(deprecated)_
- [- setStencilStoreAction:](<mtlparallelrendercommandencoder/setstencilstoreaction(__).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](mtlstoreaction/unknown.md) value specified for a given stencil attachment.
- [- setStencilStoreActionOptions:](<mtlparallelrendercommandencoder/setstencilstoreactionoptions(__).md>) — Specifies known store action options for a given stencil attachment. _(deprecated)_

## See Also

### Encoding a render pass in parallel

- [MTLLoadAction](mtlloadaction.md) — Types of actions performed for an attachment at the start of a rendering pass.
- [MTLStoreAction](mtlstoreaction.md) — Types of actions performed for an attachment at the end of a rendering pass.
- [MTLStoreActionOptions](mtlstoreactionoptions.md) — Options that modify a store action. _(deprecated)_

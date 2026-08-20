---
title: Metal Best Practices Guide
apple_id: TP40016642
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/LoadandStoreActions.html
archived_at: '2026-07-15T03:48:54.514181Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Best Practices Guide](index.md)



## Load and Store Actions

__Best Practice:__ Set appropriate load and store actions for your render targets.

Actions performed on your Metal render targets must be configured appropriately to avoid costly and unnecessary rendering work at the start (load action) or end (store action) of a rendering pass.

### Choose an Appropriate Load Action

Use the following guidelines to determine the appropriate load action for a particular render target. These guidelines are also summarized in [Table 9-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrqfvjvomq).

- If all the render target pixels are rendered to, choose the [DontCare](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare) action. There are no costs associated with this action, and texture data is always interpreted as undefined.
- If the previous contents of the render target do not need to be preserved and only some of its pixels are rendered to, choose the [Clear](https://developer.apple.com/documentation/metal/mtlloadaction/clear) action. This action incurs the cost of writing a clear value to each pixel.
- If the previous contents of the render target need to be preserved and only some of its pixels are rendered to, choose the [Load](https://developer.apple.com/documentation/metal/mtlloadaction/load) action. This action incurs the cost of loading the previous contents.

__Table 9-1__Choosing a render target load action

| Previous contents preserved | Pixels rendered to | Load action |
| --- | --- | --- |
| N/A | All | [DontCare](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare) |
| No | Some | [Clear](https://developer.apple.com/documentation/metal/mtlloadaction/clear) |
| Yes | Some | [Load](https://developer.apple.com/documentation/metal/mtlloadaction/load) |

### Choose an Appropriate Store Action

Use the following guidelines to determine the appropriate store action for a particular render target.

- If the contents of the render target do not need to be preserved, choose the [DontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) action. There are no costs associated with this action, and texture data is always interpreted as undefined. This is a common case for depth and stencil render targets.
- If the contents of the render target need to be preserved, choose the [Store](https://developer.apple.com/documentation/metal/mtlstoreaction/store) action. This is always the case for drawables and other displayable render targets.
- If the render target is a multisample texture, refer to Table 9-2.

  __Table 9-2__Choosing a render target store action for a multisample texture

| Multisampled contents preserved | Resolve texture specified | Resolved contents preserved | Store action |
| --- | --- | --- | --- |
| Yes | Yes | Yes | [storeAndMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/storeandmultisampleresolve) |
| No | Yes | Yes | [MultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionmultisampleresolve) |
| Yes | No | N/A | [Store](https://developer.apple.com/documentation/metal/mtlstoreaction/store) |
| No | No | N/A | [DontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) |

  > [!NOTE]
  > 

In some cases, the store action of a particular render target may not be known up front. To defer this decision, set the temporary [unknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown) value when you create a [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor) object. You must specify a known store action before you finish encoding your rendering pass, otherwise an error occurs. Setting the [unknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown) value may avoid potential costs incurred by setting the [Store](https://developer.apple.com/documentation/metal/mtlstoreaction/store) store action prematurely.

### Evaluate Actions Between Rendering Passes

Render targets used across multiple rendering passes should be evaluated closely for optimal combinations of store and load actions between rendering passes. Table 9-3 lists these combinations.

__Table 9-3__Store and load actions between rendering passes

| First rendering pass store action | Second rendering pass load action |
| --- | --- |
| [DontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) | One of the following actions:  [DontCare](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare)  [Clear](https://developer.apple.com/documentation/metal/mtlloadaction/clear) |
| One of the following actions:  [Store](https://developer.apple.com/documentation/metal/mtlstoreaction/store)  [MultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionmultisampleresolve)  [storeAndMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/storeandmultisampleresolve) | [Load](https://developer.apple.com/documentation/metal/mtlloadaction/load) |

[Frame Rate (iOS and tvOS)](FrameRate.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrtfvjvomi)

[Render Command Encoders (iOS and tvOS)](RenderCommandEncoders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmzqfvjvomi)

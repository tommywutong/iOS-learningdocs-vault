---
title: Onscreen presentation
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/onscreen-presentation
source_url: 'https://developer.apple.com/documentation/metal/onscreen-presentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/onscreen-presentation.json'
content_hash: 'sha256:9def4574007a42b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# Onscreen presentation

Show the output from a GPU’s rendering pass to the user in your app.

## Overview

A texture contains visual data that you may want to display onscreen, such as a filtered image or a frame of animation in a game. To display a texture on a device’s screen, you need to create or acquire a drawable texture from [Core Animation](../quartzcore.md).

In Metal, a _drawable_ is a texture that bridges the display subsystem within [Core Animation](../quartzcore.md) to Metal. You can use a drawable as the output of a render pass and then present it to a display with its [MTLDrawable](mtldrawable.md) protocol.

> [!note] Note
> You can’t present a texture you directly create in Metal unless you copy its content to a drawable using a blit pass (see [Blit passes](blit-passes.md)).

To display content on a device’s screen, add one of these to your Metal app:

- A [CAMetalLayer](../quartzcore/cametallayer.md) instance within a custom view class
- An [MTKView](../metalkit/mtkview.md) instance

With a [CAMetalLayer](../quartzcore/cametallayer.md) instance, your app can get drawable instances by calling its [nextDrawable()](<../quartzcore/cametallayer/nextdrawable().md>) method. Each drawable conforms to the [CAMetalDrawable](../quartzcore/cametaldrawable.md) protocol, which has a [texture](../quartzcore/cametaldrawable/texture.md) property that a render pass can use as its output. See [Creating a custom Metal view](creating-a-custom-metal-view.md) for more information.

Alternatively, your app can use an [MTKView](../metalkit/mtkview.md) and its [currentDrawable](../metalkit/mtkview/currentdrawable.md) property. This [MetalKit](../metalkit.md) class provides a default implementation of a Metal-aware view that uses an underlying [CAMetalLayer](../quartzcore/cametallayer.md) instance. A [MetalKit](../metalkit.md) view provides a quick and easy way to present your app’s content, but gives you less control than using a [CAMetalLayer](../quartzcore/cametallayer.md) directly. See [Using Metal to draw a view’s contents](using-metal-to-draw-a-view's-contents.md) for more information.

Whichever mechanism you choose, pay close attention to how your app handles drawables. Each drawable comes from a limited and reusable resource pool. A drawable may not always be available when your app requests one. When that happens, [Core Animation](../quartzcore.md) blocks the calling thread until a drawable becomes available — usually at the display’s next refresh interval.

## Topics

### Presenting with core animation

- [Creating a custom Metal view](creating-a-custom-metal-view.md) — Implement a lightweight view for Metal rendering that’s customized to your app’s needs.
- [Reading pixel data from a drawable texture](reading-pixel-data-from-a-drawable-texture.md) — Access texture data from the CPU by copying it to a buffer.
- [Achieving smooth frame rates with a Metal display link](achieving-smooth-frame-rates-with-a-metal-display-link.md) — Pace rendering with minimal input latency while providing essential information to the operating system for power-efficient rendering, thermal mitigation, and the scheduling of sustainable workloads.
- [CAMetalLayer](../quartzcore/cametallayer.md) — A Core Animation layer that Metal can render into, typically displayed onscreen.
- [CAMetalDrawable](../quartzcore/cametaldrawable.md) — A Metal drawable associated with a Core Animation layer.

### Presenting with MetalKit

- [Using Metal to draw a view’s contents](using-metal-to-draw-a-view's-contents.md) — Create a MetalKit view and a render pass to draw the view’s contents.
- [MTKView](../metalkit/mtkview.md) — A specialized view that creates, configures, and displays Metal objects.
- [MTKViewDelegate](../metalkit/mtkviewdelegate.md) — Methods for responding to a MetalKit view’s drawing and resizing events.

## See Also

### Presentation

- [Managing your game window for Metal in macOS](managing-your-game-window-for-metal-in-macos.md) — Set up a window and view for optimally displaying your Metal content.
- [Managing your Metal app window in iPadOS](managing-your-metal-app-window-in-ipados.md) — Set up a window that handles dynamically resizing your Metal content.
- [Adapting your game interface for smaller screens](adapting-your-game-interface-for-smaller-screens.md) — Make text legible on all devices the player chooses to run your game on.
- [HDR content](hdr-content.md) — Take advantage of high dynamic range to present more vibrant colors in your apps and games.

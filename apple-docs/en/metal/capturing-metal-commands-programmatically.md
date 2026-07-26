---
title: Capturing Metal commands programmatically
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 10.15+, Xcode 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/capturing-metal-commands-programmatically
source_url: 'https://developer.apple.com/documentation/metal/capturing-metal-commands-programmatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/capturing-metal-commands-programmatically.json'
content_hash: 'sha256:5a2571613f2299d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# Capturing Metal commands programmatically

<sub>Sample Code</sub>

Invoke a Metal frame capture from your app, then save the resulting GPU trace to a file or view it in Xcode.

## Overview

> [!note] Note
> This sample code project is associated with WWDC 2019 session [606: Delivering Optimized Metal Apps and Games](https://developer.apple.com/videos/play/wwdc2019/606/).

### Configure the sample code project

To run the app:

- Build the project with Xcode 11 or later.

## See Also

### Developer tools

- [Supporting Simulator in a Metal app](supporting-simulator-in-a-metal-app.md) — Configure alternative render paths in your Metal app to enable running your app in Simulator.
- [Logging shader debug messages](logging-shader-debug-messages.md) — Print debugging messages that a shader generates using shader logging.
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md) — Prototype and test your Metal apps in Simulator.
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md) — Fix performance glitches and develop default settings for smooth experiences on Apple platforms using the powerful suite of Metal development tools.
- [Metal debugger](../xcode/metal-debugger.md) — Debug and profile your Metal workload with a GPU trace.
- [Metal developer workflows](../xcode/metal-developer-workflows.md) — Locate and fix issues related to your app’s use of the Metal API and GPU functions.
- [GPU counters and counter sample buffers](gpu-counters-and-counter-sample-buffers.md) — Retrieve runtime data from a GPU device by sampling one or more of its counters.
- [Metal debugging types](metal-debugging-types.md) — Create capture managers and capture scopes, and review a GPU device’s log after it runs a command buffer.

## Download

- [CapturingMetalCommandsProgrammatically.zip](https://docs-assets.developer.apple.com/published/b3b3093326a2/CapturingMetalCommandsProgrammatically.zip)

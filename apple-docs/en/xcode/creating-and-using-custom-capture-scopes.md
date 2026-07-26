---
title: Creating and using custom capture scopes
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-and-using-custom-capture-scopes
source_url: 'https://developer.apple.com/documentation/xcode/creating-and-using-custom-capture-scopes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-and-using-custom-capture-scopes.json'
content_hash: 'sha256:e4fdf9014412efb0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal developer workflows](metal-developer-workflows.md)

# Creating and using custom capture scopes

<sub>Article</sub>

Capture specific GPU commands by using custom capture scopes.

## Overview

When you capture a frame using the default capture scope by clicking the Metal Capture button in Xcode’s debug bar, the resulting capture contains all of the data for a single frame. In some cases, you may want to debug a partial frame rather than an entire frame. You can accomplish this by setting up and using a custom capture scope that lets you choose exactly which Metal commands to record.

> [!note] Note
> Don’t allocate custom capture scopes yourself. Instead, call one of the [MTLCaptureManager](../metal/mtlcapturemanager.md) methods: [makeCaptureScope(device:)](<../metal/mtlcapturemanager/makecapturescope(device_).md>) or [makeCaptureScope(commandQueue:)](<../metal/mtlcapturemanager/makecapturescope(commandqueue_)-1rozd.md>).

### Define capture boundaries

Call [begin()](<../metal/mtlcapturescope/begin().md>) on your capture scope to instruct the Metal debugger to record your app’s subsequent Metal activity. To stop recording a frame and to present the Metal debugger, call [end()](<../metal/mtlcapturescope/end().md>).

```swift
// Create myCaptureScope outside of your rendering loop.
myCaptureScope.begin()

if let commandBuffer = commandQueue.makeCommandBuffer() {
    // Do Metal work.
    commandBuffer.commit()
}

myCaptureScope.end()
```

> [!important] Important
> Create capture scopes outside your rendering or compute loop, situating your calls between [begin()](<../metal/mtlcapturescope/begin().md>) and [end()](<../metal/mtlcapturescope/end().md>). For Metal capture to work correctly, you need to hold a strong reference to an active capture scope for the duration of the work that the capture scope contains.

### Label your capture scope

To identify your custom capture scope when capturing a trace from the Metal Capture popover, set your capture scope’s label property.

```swift
myCaptureScope.label = "My Capture Scope"
```

When you’re ready to capture a frame, click the Metal Capture button in the debug bar. There, you can find your custom capture scope with the matching label available in the list for capturing.

Keep a strong reference to the capture scope in your code for as long as you want the option to be visible in Xcode.

### Make a custom capture scope the default

When you perform a capture from Xcode, it defaults to the capture scope that [defaultCaptureScope](../metal/mtlcapturemanager/defaultcapturescope.md) specifies. If the value of this property is `nil`, Xcode defines the default capture scope using drawable presentation boundaries; for example, using your calls to the methods [present(_:)](<../metal/mtlcommandbuffer/present(__).md>) or [present()](<../metal/mtldrawable/present().md>).

To change the default scope, create an [MTLCaptureScope](../metal/mtlcapturescope.md) instance and assign it to [defaultCaptureScope](../metal/mtlcapturemanager/defaultcapturescope.md).

```swift
MTLCaptureManager.shared().defaultCaptureScope = myCaptureScope
```

## See Also

### Project preparation for debugging

- [Building your project with embedded shader sources](building-your-project-with-embedded-shader-sources.md) — Prepare to debug your project’s shaders by including source code in the build.
- [Naming resources and commands](naming-resources-and-commands.md) — Enhance the debugging of your Metal app using labels and grouping.

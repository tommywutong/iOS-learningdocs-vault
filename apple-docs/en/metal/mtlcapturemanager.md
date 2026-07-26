---
title: MTLCaptureManager
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturemanager
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager.json'
content_hash: 'sha256:062156e9c9361b7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCaptureManager

<sub>Class</sub>

An instance you use to capture Metal command data in your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLCaptureManager
```

## Overview

A capture manager works with the frame capture feature to:

- Capture data about Metal commands programmatically. See [Capturing a Metal workload programmatically](../xcode/capturing-a-metal-workload-programmatically.md).
- Only capture commands that apply to a specific [MTLDevice](mtldevice.md), command queue, or [MTLCaptureScope](mtlcapturescope.md) instance.
- Assign a default [MTLCaptureScope](mtlcapturescope.md) instance for captures you create in Xcode by clicking the Capture GPU workload button in the debug bar, which has an icon with the Metal logo.

The Metal debugger requires you to enable GPU Frame Capture in your project settings; see [Capturing a Metal workload in Xcode](../xcode/capturing-a-metal-workload-in-xcode.md).

> [!important] Important
> The capture manager records commands within the [MTLCommandBuffer](mtlcommandbuffer.md) instance that you create and commit while the capture session is active.

For more information about Metal frame capture, see [Metal debugger](../xcode/metal-debugger.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Obtaining the shared capture manager

- [+ sharedCaptureManager](<mtlcapturemanager/shared().md>) — Provides the shared capture manager for your Metal app.

### Querying support for a capture destination

- [- supportsDestination:](<mtlcapturemanager/supportsdestination(__).md>) — Checks to see whether a particular capture destination is supported.

### Creating a capture scope

- [- newCaptureScopeWithDevice:](<mtlcapturemanager/makecapturescope(device_).md>) — Creates a capture scope for commands submitted to a specific device object.
- [- newCaptureScopeWithCommandQueue:](<mtlcapturemanager/makecapturescope(commandqueue_)-1rozd.md>) — Creates a capture scope for commands submitted to a specific command queue.
- [defaultCaptureScope](mtlcapturemanager/defaultcapturescope.md) — The capture scope to use when a capture is initiated in Xcode.

### Starting capture

- [- startCaptureWithDescriptor:error:](<mtlcapturemanager/startcapture(with_).md>) — Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [- startCaptureWithDevice:](<mtlcapturemanager/startcapture(device_).md>) — Starts capturing any of your app’s Metal commands that are executed by the device object. _(deprecated)_
- [- startCaptureWithCommandQueue:](<mtlcapturemanager/startcapture(commandqueue_).md>) — Starts capturing any of your app’s Metal commands that are executed by the command queue. _(deprecated)_
- [- startCaptureWithScope:](<mtlcapturemanager/startcapture(scope_).md>) — Starts capturing any of your app’s Metal commands that are in the specified capture scope. _(deprecated)_

### Stopping capture

- [- stopCapture](<mtlcapturemanager/stopcapture().md>) — Stops capturing Metal commands.

### Monitoring capture

- [isCapturing](mtlcapturemanager/iscapturing.md) — A Boolean value that indicates whether Metal commands are being captured.

### Instance Methods

- [- newCaptureScopeWithMTL4CommandQueue:](<mtlcapturemanager/makecapturescope(commandqueue_)-9wie3.md>)

## See Also

### Frame capture

- [MTLCaptureDescriptor](mtlcapturedescriptor.md) — A configuration for a Metal capture session.
- [MTLCaptureDestination](mtlcapturedestination.md) — The kinds of destinations for captured command data.
- [MTLCaptureScope](mtlcapturescope.md) — A type that can programmatically customize a GPU frame capture.

---
title: 'init(inputPorts:output:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureconnection/init(inputports:output:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/init(inputports:output:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/init%28inputports%3Aoutput%3A%29.json'
content_hash: 'sha256:9c41a9b8136edd54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# init(inputPorts:output:)

<sub>Initializer</sub>

Creates a capture connection that represents a connection between multiple input ports and an output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(inputPorts ports: [AVCaptureInput.Port], output: AVCaptureOutput)
```

## Parameters

- `ports` — An array of [Port](../avcaptureinput/port.md) instances that relate to [AVCaptureInput](../avcaptureinput.md) instances.

- `output` — An [AVCaptureOutput](../avcaptureoutput.md) instance.

## Return Value

A capture connection that represents a connection between `ports` and `output`.

## Discussion

You can add the connection this method returns to an [AVCaptureSession](../avcapturesession.md) instance with the [- addConnection:](<../avcapturesession/addconnection(__).md>) method.

The [- addInput:](<../avcapturesession/addinput(__).md>): or [- addOutput:](<../avcapturesession/addoutput(__).md>) methods automatically form connections between all compatible inputs and outputs. You don’t need to manually create and add connections to the session unless you use the primitive [- addInputWithNoConnections:](<../avcapturesession/addinputwithnoconnections(__).md>) and [- addOutputWithNoConnections:](<../avcapturesession/addoutputwithnoconnections(__).md>) methods.

## See Also

### Creating a connection

- [- initWithInputPort:videoPreviewLayer:](<init(inputport_videopreviewlayer_).md>) — Creates a capture connection that represents a connection between an input port and a video preview layer.

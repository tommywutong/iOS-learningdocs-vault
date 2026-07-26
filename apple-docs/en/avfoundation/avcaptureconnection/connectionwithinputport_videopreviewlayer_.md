---
title: 'connectionWithInputPort:videoPreviewLayer:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureconnection/connectionwithinputport:videopreviewlayer:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/connectionwithinputport:videopreviewlayer:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/connectionwithinputport%3Avideopreviewlayer%3A.json'
content_hash: 'sha256:e2b9879548c5062d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# connectionWithInputPort:videoPreviewLayer:

<sub>Type Method</sub>

Returns a capture connection that represents a connection between an input port and a video preview layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) connectionWithInputPort:(AVCaptureInputPort *) port videoPreviewLayer:(AVCaptureVideoPreviewLayer *) layer;
```

## Parameters

- `port` — An [Port](../avcaptureinput/port.md) instance that relates to an [AVCaptureInput](../avcaptureinput.md) instance.

- `layer` — An [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md) instance.

## Return Value

A capture connection that represents a connection between `port` and `layer`.

## Discussion

You can add the connection this method returns to an [AVCaptureSession](../avcapturesession.md) instance with the [- addConnection:](<../avcapturesession/addconnection(__).md>) method.

The [- addInput:](<../avcapturesession/addinput(__).md>): or [- addOutput:](<../avcapturesession/addoutput(__).md>) methods automatically form connections between all compatible inputs and outputs. You don’t need to manually create and add connections to the session unless you use the primitive [- addInputWithNoConnections:](<../avcapturesession/addinputwithnoconnections(__).md>) and [- addOutputWithNoConnections:](<../avcapturesession/addoutputwithnoconnections(__).md>) methods.

## See Also

### Creating a connection

- [- initWithInputPorts:output:](<init(inputports_output_).md>) — Creates a capture connection that represents a connection between multiple input ports and an output.
- [connectionWithInputPorts:output:](connectionwithinputports_output_.md) — Returns a capture connection that represents a connection between multiple input ports and an output.
- [- initWithInputPort:videoPreviewLayer:](<init(inputport_videopreviewlayer_).md>) — Creates a capture connection that represents a connection between an input port and a video preview layer.

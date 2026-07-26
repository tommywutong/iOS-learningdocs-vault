---
title: 'init(ofType:context:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cidetector/init(oftype:context:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cidetector/init(oftype:context:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetector/init%28oftype%3Acontext%3Aoptions%3A%29.json'
content_hash: 'sha256:2571efeae93b71b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDetector](../cidetector.md)

# init(ofType:context:options:)

<sub>Initializer</sub>

Creates and returns a configured detector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(ofType type: String, context: CIContext?, options: [String : Any]? = nil)
```

## Parameters

- `type` — A string indicating the kind of detector you are interested in. See [Detector Types](../detector-types.md).

- `context` — A Core Image context that the detector can use when analyzing an image.

- `options` — A dictionary containing details on how you want the detector to be configured. See [Detector Configuration Keys](../detector-configuration-keys.md).

## Return Value

A configured detector.

## Discussion

A [CIDetector](../cidetector.md) object can potentially create and hold a significant amount of resources. Where possible, reuse the same [CIDetector](../cidetector.md) instance. Also, when processing images with a detector object, your application performs better if the [CIContext](../cicontext.md) used to initialize the detector is the same context used to process the [ciImage](../../uikit/uiimage/ciimage.md) objects.

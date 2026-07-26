---
title: 'status(of:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronouskeyvalueloading/status(of:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/status(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronouskeyvalueloading/status%28of%3A%29.json'
content_hash: 'sha256:faf7a7198280e4a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousKeyValueLoading](../avasynchronouskeyvalueloading.md)

# status(of:)

<sub>Instance Method</sub>

Returns a value that indicates the loaded status of a property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func status<T>(of property: AVAsyncProperty<Self, T>) -> AVAsyncProperty<Self, T>.Status
```

## Parameters

- `property` — A property identifier with a status to check.

## Return Value

A status value.

## Discussion

A status of [AVAsyncProperty.Status.loaded(_:)](<../avasyncproperty/status/loaded(__).md>) provides the property value, and a status of [AVAsyncProperty.Status.failed(_:)](<../avasyncproperty/status/failed(__).md>) provides an error that describes the failure.

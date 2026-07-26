---
title: 'AVAsyncProperty.Status.failed(_:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasyncproperty/status/failed(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasyncproperty/status/failed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasyncproperty/status/failed%28_%3A%29.json'
content_hash: 'sha256:0e8f8785cd501d7b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAsyncProperty](../../avasyncproperty.md) · [Status](../status.md)

# AVAsyncProperty.Status.failed(_:)

<sub>Case</sub>

A property value fails to load.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failed(NSError)
```

## Parameters

- `error` — An error object that describes the failure.

## See Also

### Status values

- [AVAsyncProperty.Status.notYetLoaded](notyetloaded.md) — The system hasn’t loaded a property value.
- [AVAsyncProperty.Status.loading](loading.md) — The system is loading the property.
- [AVAsyncProperty.Status.loaded(_:)](<loaded(__).md>) — A property value is ready to use.

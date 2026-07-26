---
title: 'AVAsyncProperty.Status.loaded(_:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasyncproperty/status/loaded(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasyncproperty/status/loaded(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasyncproperty/status/loaded%28_%3A%29.json'
content_hash: 'sha256:2696ab242e94ed4b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAsyncProperty](../../avasyncproperty.md) · [Status](../status.md)

# AVAsyncProperty.Status.loaded(_:)

<sub>Case</sub>

A property value is ready to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case loaded(Value)
```

## Parameters

- `value` — A value for the property.

## See Also

### Status values

- [AVAsyncProperty.Status.notYetLoaded](notyetloaded.md) — The system hasn’t loaded a property value.
- [AVAsyncProperty.Status.loading](loading.md) — The system is loading the property.
- [AVAsyncProperty.Status.failed(_:)](<failed(__).md>) — A property value fails to load.

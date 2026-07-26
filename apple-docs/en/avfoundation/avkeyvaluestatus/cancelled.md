---
title: AVKeyValueStatus.cancelled
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avkeyvaluestatus/cancelled
source_url: 'https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus/cancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avkeyvaluestatus/cancelled.json'
content_hash: 'sha256:f6c8fc48b688f1db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVKeyValueStatus](../avkeyvaluestatus.md)

# AVKeyValueStatus.cancelled

<sub>Case</sub>

You canceled loading a property value.

> [!warning] Deprecated
> Use AVAsyncProperty.Status instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cancelled
```

## See Also

### Status values

- [AVKeyValueStatusUnknown](unknown.md) — The property value’s status is unknown. _(deprecated)_
- [AVKeyValueStatusLoading](loading.md) — The system is loading the property value. _(deprecated)_
- [AVKeyValueStatusLoaded](loaded.md) — The property value is ready to use. _(deprecated)_
- [AVKeyValueStatusFailed](failed.md) — The system is unable to load the property value. _(deprecated)_

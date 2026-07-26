---
title: AVKeyValueStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avkeyvaluestatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avkeyvaluestatus.json'
content_hash: 'sha256:5d120f37383ab7bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVKeyValueStatus

<sub>Enumeration</sub>

Values that indicate the loaded status of a property.

> [!warning] Deprecated
> Use [Status](avasyncproperty/status.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AVKeyValueStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status values

- [AVKeyValueStatusUnknown](avkeyvaluestatus/unknown.md) — The property value’s status is unknown. _(deprecated)_
- [AVKeyValueStatusLoading](avkeyvaluestatus/loading.md) — The system is loading the property value. _(deprecated)_
- [AVKeyValueStatusLoaded](avkeyvaluestatus/loaded.md) — The property value is ready to use. _(deprecated)_
- [AVKeyValueStatusFailed](avkeyvaluestatus/failed.md) — The system is unable to load the property value. _(deprecated)_
- [AVKeyValueStatusCancelled](avkeyvaluestatus/cancelled.md) — You canceled loading a property value. _(deprecated)_

### Initializers

- [init(rawValue:)](<avkeyvaluestatus/init(rawvalue_).md>) _(deprecated)_

## See Also

### Deprecated

- [Deprecated symbols](avasynchronouskeyvalueloading-deprecated-symbols.md) — Review unsupported symbols and their replacements.
- [- loadValuesAsynchronouslyForKeys:completionHandler:](<avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys_completionhandler_).md>) — Tells the asset to load the values of all of the specified keys that aren’t already loaded. _(deprecated)_
- [- statusOfValueForKey:error:](<avasynchronouskeyvalueloading/statusofvalue(forkey_error_).md>) — Returns a status that indicates whether a property value is immediately available without blocking the calling thread. _(deprecated)_

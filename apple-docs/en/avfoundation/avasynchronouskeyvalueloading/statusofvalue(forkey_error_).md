---
title: 'statusOfValue(forKey:error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasynchronouskeyvalueloading/statusofvalue(forkey:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/statusofvalue(forkey:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronouskeyvalueloading/statusofvalue%28forkey%3Aerror%3A%29.json'
content_hash: 'sha256:a1ae2879568a210d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousKeyValueLoading](../avasynchronouskeyvalueloading.md)

# statusOfValue(forKey:error:)

<sub>Instance Method</sub>

Returns a status that indicates whether a property value is immediately available without blocking the calling thread.

> [!warning] Deprecated
> Use [status(of:)](<status(of_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus
```

## Parameters

- `key` — The property whose status you want.

- `outError` — If the status of the value for the `key` is [AVKeyValueStatusFailed](../avkeyvaluestatus/failed.md), the system sets this pointer to an [NSError](../../foundation/nserror.md) object that describes the failure.

## Return Value

The current status of the requested key.

## See Also

### Deprecated

- [Deprecated symbols](../avasynchronouskeyvalueloading-deprecated-symbols.md) — Review unsupported symbols and their replacements.
- [- loadValuesAsynchronouslyForKeys:completionHandler:](<loadvaluesasynchronously(forkeys_completionhandler_).md>) — Tells the asset to load the values of all of the specified keys that aren’t already loaded. _(deprecated)_
- [AVKeyValueStatus](../avkeyvaluestatus.md) — Values that indicate the loaded status of a property. _(deprecated)_

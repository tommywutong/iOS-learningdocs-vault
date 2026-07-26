---
title: cancelExport()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetexportsession/cancelexport()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/cancelexport()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/cancelexport%28%29.json'
content_hash: 'sha256:e308eabd6756a872'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# cancelExport()

<sub>Instance Method</sub>

Cancels the execution of an export session.

> [!warning] Deprecated
> Use Task.cancel() instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cancelExport()
```

## Discussion

Apple discourages the use of this symbol. Use [cancel()](<../../swift/task/cancel().md>) on the [Task](../../swift/task.md) or parent task that initiated the export instead.

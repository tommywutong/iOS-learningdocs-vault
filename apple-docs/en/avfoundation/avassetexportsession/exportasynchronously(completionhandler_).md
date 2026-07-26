---
title: 'exportAsynchronously(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（18.0 起废弃）, iPadOS 4.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetexportsession/exportasynchronously(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/exportasynchronously(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/exportasynchronously%28completionhandler%3A%29.json'
content_hash: 'sha256:1f05482ba31017d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# exportAsynchronously(completionHandler:)

<sub>Instance Method</sub>

Starts the asynchronous execution of an export session.

> [!warning] Deprecated
> Use [export(to:as:isolation:)](<export(to_as_isolation_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func exportAsynchronously(completionHandler handler: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func export() async
```

## Parameters

- `handler` — A callback the system invokes when it finishes successfully, or in the event of writing failure.

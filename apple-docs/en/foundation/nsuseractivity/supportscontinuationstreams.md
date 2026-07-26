---
title: supportsContinuationStreams
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/supportscontinuationstreams
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/supportscontinuationstreams'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/supportscontinuationstreams.json'
content_hash: 'sha256:465022910dad383d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# supportsContinuationStreams

<sub>Instance Property</sub>

A Boolean value that determines whether the continuing app can request streams to be opened back to the originating app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var supportsContinuationStreams: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md), the continuing app can connect back to the originating app for more information using streams. The default value of this property is [false](../../swift/false.md). It can dynamically be set to [true](../../swift/true.md) to selectively support continuation streams based on the state of the user activity.

## See Also

### Working with continuation streams

- [- getContinuationStreamsWithCompletionHandler:](<getcontinuationstreams(completionhandler_).md>) — Requests streams back to the originating app.

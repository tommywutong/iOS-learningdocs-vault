---
title: UIBackgroundFetchResult
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundfetchresult
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundfetchresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundfetchresult.json'
content_hash: 'sha256:3e66ec5492b07f86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBackgroundFetchResult

<sub>Enumeration</sub>

Constants that indicate the result of a background fetch operation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIBackgroundFetchResult
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIBackgroundFetchResultNewData](uibackgroundfetchresult/newdata.md) — New data was successfully downloaded.
- [UIBackgroundFetchResultNoData](uibackgroundfetchresult/nodata.md) — There was no new data to download.
- [UIBackgroundFetchResultFailed](uibackgroundfetchresult/failed.md) — An attempt to download data was made but that attempt failed.

### Initializers

- [init(rawValue:)](<uibackgroundfetchresult/init(rawvalue_).md>)

## See Also

### Downloading data in the background

- [- application:handleEventsForBackgroundURLSession:completionHandler:](<uiapplicationdelegate/application(__handleeventsforbackgroundurlsession_completionhandler_).md>) — Tells the delegate that events related to a URL session are waiting to be processed.

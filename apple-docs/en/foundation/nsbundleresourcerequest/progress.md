---
title: progress
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsbundleresourcerequest/progress
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/progress.json'
content_hash: 'sha256:0df7e5fac8886a22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# progress

<sub>Instance Property</sub>

A reference to the progress object associated with the specified resource request. (read-only)

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var progress: Progress { get }
```

## Discussion

This [Progress](../progress.md) object will begin updating after [- beginAccessingResourcesWithCompletionHandler:](<beginaccessingresources(completionhandler_).md>) is called.

## See Also

### Related Documentation

- [- beginAccessingResourcesWithCompletionHandler:](<beginaccessingresources(completionhandler_).md>) — Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store. _(deprecated)_

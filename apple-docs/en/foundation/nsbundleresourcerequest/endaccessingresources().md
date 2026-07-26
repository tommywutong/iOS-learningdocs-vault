---
title: endAccessingResources()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsbundleresourcerequest/endaccessingresources()
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/endaccessingresources()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/endaccessingresources%28%29.json'
content_hash: 'sha256:677cfed36c6e3d6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# endAccessingResources()

<sub>Instance Method</sub>

Informs the system that you have finished accessing the resources marked with the tags managed by the request.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func endAccessingResources()
```

## Discussion

Call this method as soon as you have finished using the tags managed by this request. If needed, this method will be called by the system when the resource request object is deallocated.

> [!important] Important
> The callback from [- beginAccessingResourcesWithCompletionHandler:](<beginaccessingresources(completionhandler_).md>) or [- conditionallyBeginAccessingResourcesWithCompletionHandler:](<conditionallybeginaccessingresources(completionhandler_).md>) must have completed before calling [- endAccessingResources](<endaccessingresources().md>).

## See Also

### Requesting resources

- [- beginAccessingResourcesWithCompletionHandler:](<beginaccessingresources(completionhandler_).md>) — Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store. _(deprecated)_
- [- conditionallyBeginAccessingResourcesWithCompletionHandler:](<conditionallybeginaccessingresources(completionhandler_).md>) — Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources. _(deprecated)_

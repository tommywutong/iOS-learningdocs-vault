---
title: 'conditionallyBeginAccessingResources(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/conditionallybeginaccessingresources%28completionhandler%3A%29.json'
content_hash: 'sha256:a873d3ac11e97e8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# conditionallyBeginAccessingResources(completionHandler:)

<sub>Instance Method</sub>

Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func conditionallyBeginAccessingResources(completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func conditionallyBeginAccessingResources() async -> Bool
```

## Parameters

- `completionHandler` — A block called when the availability of the resources has been checked. The block takes the following parameter: - **resourcesAvailable** — Returns [true](../../swift/true.md) if all of the resources marked with the tags managed by the request are already on the device. Returns [false](../../swift/false.md) if any of the resources are not on the device.

## Discussion

If the resources marked with the tags managed by the request are already on the device, you can start accessing them as soon as the completion handler is called with `resourcesAvailable` set to [true](../../swift/true.md). If all of the resources are not already available, you need to call [- beginAccessingResourcesWithCompletionHandler:](<beginaccessingresources(completionhandler_).md>) to download them from the App Store.

> [!important] Important
> If `resourcesAvailable` is [true](../../swift/true.md), do not call [- beginAccessingResourcesWithCompletionHandler:](<beginaccessingresources(completionhandler_).md>). You must call this method or [- beginAccessingResourcesWithCompletionHandler:](<beginaccessingresources(completionhandler_).md>) before accessing any resources marked with the tags managed by the request.

## See Also

### Requesting resources

- [- beginAccessingResourcesWithCompletionHandler:](<beginaccessingresources(completionhandler_).md>) — Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store. _(deprecated)_
- [- endAccessingResources](<endaccessingresources().md>) — Informs the system that you have finished accessing the resources marked with the tags managed by the request. _(deprecated)_

---
title: 'beginAccessingResources(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsbundleresourcerequest/beginaccessingresources(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/beginaccessingresources(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/beginaccessingresources%28completionhandler%3A%29.json'
content_hash: 'sha256:7d121637f6d15368'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# beginAccessingResources(completionHandler:)

<sub>Instance Method</sub>

Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func beginAccessingResources(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func beginAccessingResources() async throws
```

## Parameters

- `completionHandler` — A block called when the resources have finished downloading or if an error occurs. The resources are not available until the completion handler is called with `error` set to `nil`. The block takes the following parameter: - **error** — Set to `nil` if the resources are downloaded successfully; otherwise this parameter holds an [NSError](../nserror.md) object describing the problem that occurred. Errors are usually due to a lack of free space or problems connecting with the App Store.

## Discussion

After calling this method, the resource request downloads any on-demand resources not already on the device. When all the resources are downloaded, they are marked as non-purgeable. The resources are not available to the app until the completion handler is called with no error.

> [!important] Important
> You must call this method or [- conditionallyBeginAccessingResourcesWithCompletionHandler:](<conditionallybeginaccessingresources(completionhandler_).md>) before accessing any resources marked with the tags managed by the request.

## See Also

### Requesting resources

- [- conditionallyBeginAccessingResourcesWithCompletionHandler:](<conditionallybeginaccessingresources(completionhandler_).md>) — Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources. _(deprecated)_
- [- endAccessingResources](<endaccessingresources().md>) — Informs the system that you have finished accessing the resources marked with the tags managed by the request. _(deprecated)_

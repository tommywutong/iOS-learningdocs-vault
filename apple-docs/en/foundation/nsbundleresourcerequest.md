---
title: NSBundleResourceRequest
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsbundleresourcerequest
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest.json'
content_hash: 'sha256:fa3966d701597e26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSBundleResourceRequest

<sub>Class</sub>

A resource manager you use to download content hosted on the App Store at the time your app needs it.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSBundleResourceRequest
```

## Overview

You identify on-demand resources during development by creating string identifiers known as tags and assigning one or more tags to each resource. An [NSBundleResourceRequest](nsbundleresourcerequest.md) object manages the resources marked by one or more tags.

You use the resource request to inform the system when the managed tags are needed and when you have finished accessing them. The resource request manages the downloading of any resources marked with the managed tags that are not already on the device and informs your app when the resources are ready for use.

> [!note] Note
> This class ignores calls from Mac apps built with Mac Catalyst.

The system will not attempt to purge the resources marked with a tag from on-device storage as long as at least one [NSBundleResourceRequest](nsbundleresourcerequest.md) object is managing the tag. Apps can access resources after the completion handler of either [- beginAccessingResourcesWithCompletionHandler:](<nsbundleresourcerequest/beginaccessingresources(completionhandler_).md>) or [- conditionallyBeginAccessingResourcesWithCompletionHandler:](<nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler_).md>) is called successfully. Management ends after a call to [- endAccessingResources](<nsbundleresourcerequest/endaccessingresources().md>) or after the resource request object is deallocated.

Other properties and methods let you track the progress of a download, change the priority of a download, and check whether the resources marked by a set of tags are already on the device. Methods in [Bundle](bundle.md) indicate to the system the relative importance of preserving a tag in memory after it is no longer in use. For more information, see [- setPreservationPriority:forTags:](<bundle/setpreservationpriority(__fortags_).md>) and [- preservationPriorityForTag:](<bundle/preservationpriority(fortag_).md>).

> [!important] Important
> An [NSBundleResourceRequest](nsbundleresourcerequest.md) object can only be used for one successful resource request.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](progressreporting.md)

## Topics

### Initializing a resource request

- [- initWithTags:](<nsbundleresourcerequest/init(tags_).md>) — Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the main bundle. _(deprecated)_
- [- initWithTags:bundle:](<nsbundleresourcerequest/init(tags_bundle_).md>) — Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the specified bundle. _(deprecated)_

### Accessing the configuration

- [bundle](nsbundleresourcerequest/bundle.md) — A reference to the bundle used for storing the downloaded resources. (read-only) _(deprecated)_
- [tags](nsbundleresourcerequest/tags.md) — A set of strings, with each string specifying a tag used to mark on-demand resources managed by the request. (read-only) _(deprecated)_

### Requesting resources

- [- beginAccessingResourcesWithCompletionHandler:](<nsbundleresourcerequest/beginaccessingresources(completionhandler_).md>) — Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store. _(deprecated)_
- [- conditionallyBeginAccessingResourcesWithCompletionHandler:](<nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler_).md>) — Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources. _(deprecated)_
- [- endAccessingResources](<nsbundleresourcerequest/endaccessingresources().md>) — Informs the system that you have finished accessing the resources marked with the tags managed by the request. _(deprecated)_

### Setting the download priority

- [loadingPriority](nsbundleresourcerequest/loadingpriority.md) — A hint to the system of the relative priority of the resource request. _(deprecated)_
- [NSBundleResourceRequestLoadingPriorityUrgent](nsbundleresourcerequestloadingpriorityurgent.md) _(deprecated)_

### Tracking progress

- [progress](nsbundleresourcerequest/progress.md) — A reference to the progress object associated with the specified resource request. (read-only) _(deprecated)_

### Errors

- [NSBundleErrorMaximum](nsbundleerrormaximum-swift.var.md) — The end of the range of error codes reserved for bundle errors.
- [NSBundleErrorMinimum](nsbundleerrorminimum-swift.var.md) — The start of the range of error codes reserved for bundle errors.
- [NSBundleOnDemandResourceExceededMaximumSizeError](nsbundleondemandresourceexceededmaximumsizeerror-swift.var.md) — The application exceeded the amount of on-demand resources content in use at one time.
- [NSBundleOnDemandResourceInvalidTagError](nsbundleondemandresourceinvalidtagerror-swift.var.md) — The application specified a tag that the system couldn’t find in the application tag manifest.
- [NSBundleOnDemandResourceOutOfSpaceError](nsbundleondemandresourceoutofspaceerror-swift.var.md) — Insufficient space available to download the requested on-demand resources.

### Working with notifications

- [NSBundleResourceRequestLowDiskSpaceNotification](nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace.md) — Posted after the system detects that the amount of available disk space is getting low. The notification is posted to the default notification center. _(deprecated)_

### Working with notification messages

- [LowDiskSpaceMessage](nsbundleresourcerequest/lowdiskspacemessage.md) — A message the system sends when it detects the amount of available disk space getting low. _(deprecated)_

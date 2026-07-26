---
title: PHAssetResourceUploadJob.Action
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/action
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/action.json'
content_hash: 'sha256:cea48027f56f899a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# PHAssetResourceUploadJob.Action

<sub>Enumeration</sub>

An action to perform on an upload job.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum Action
```

## Overview

Determine the available jobs for an action by calling the [+ fetchJobsWithAction:options:](<fetchjobs(action_options_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Actions

- [PHAssetResourceUploadJobActionAcknowledge](action/acknowledge.md) — A job that requires acknowledgement.
- [PHAssetResourceUploadJobActionRetry](action/retry.md) — A job to retry processing.

### Initializers

- [init(rawValue:)](<action/init(rawvalue_).md>)

### Enumeration Cases

- [PHAssetResourceUploadJobActionProcess](action/process.md) — A job to process.

## See Also

### Fetching jobs

- [jobLimit](joblimit.md) — The maximum number of unacknowledged upload jobs allowed.
- [+ fetchJobsWithAction:options:](<fetchjobs(action_options_).md>) — Returns all asset resource upload jobs applicable for a given action.

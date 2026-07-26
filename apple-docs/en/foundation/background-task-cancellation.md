---
title: Background task cancellation
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/background-task-cancellation
source_url: 'https://developer.apple.com/documentation/foundation/background-task-cancellation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/background-task-cancellation.json'
content_hash: 'sha256:b14bbe69813daf33'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLSession](urlsession.md)

# Background task cancellation

<sub>API Collection</sub>

Constants that indicate why a background task was canceled.

## Overview

These values are used in conjunction with the [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) key in an [NSError](nserror.md) object’s `userInfo` dictionary.

## Topics

### Cancellation reasons

- [NSURLErrorCancelledReasonBackgroundUpdatesDisabled](nsurlerrorcancelledreasonbackgroundupdatesdisabled.md) — A reason that indicates the system canceled the background task because background tasks are disabled.
- [NSURLErrorCancelledReasonInsufficientSystemResources](nsurlerrorcancelledreasoninsufficientsystemresources.md) — A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.
- [NSURLErrorCancelledReasonUserForceQuitApplication](nsurlerrorcancelledreasonuserforcequitapplication.md) — A reason that indicates the system canceled the background task because the user force-quit the application.

## See Also

### Handling errors

- [URL session error dictionary keys](url-session-error-dictionary-keys.md) — Keys used in conjunction with error objects returned by URL sessions and tasks.

---
title: URL Session Background Task Cancellation Reasons
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/url-session-background-task-cancellation-reasons
source_url: 'https://developer.apple.com/documentation/foundation/url-session-background-task-cancellation-reasons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url-session-background-task-cancellation-reasons.json'
content_hash: 'sha256:ff2e84e42e42a40e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URL Loading System error info keys](url-loading-system-error-info-keys.md)

# URL Session Background Task Cancellation Reasons

<sub>API Collection</sub>

Reasons that indicate why the system canceled a background task.

## Topics

### Cancellation reasons

- [NSURLErrorCancelledReasonBackgroundUpdatesDisabled](nsurlerrorcancelledreasonbackgroundupdatesdisabled.md) — A reason that indicates the system canceled the background task because background tasks are disabled.
- [NSURLErrorCancelledReasonInsufficientSystemResources](nsurlerrorcancelledreasoninsufficientsystemresources.md) — A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.
- [NSURLErrorCancelledReasonUserForceQuitApplication](nsurlerrorcancelledreasonuserforcequitapplication.md) — A reason that indicates the system canceled the background task because the user force-quit the application.

## See Also

### Keys

- [NSURLErrorFailingURLErrorKey](nsurlerrorfailingurlerrorkey.md) — The URL which caused a load to fail.
- [NSURLErrorFailingURLPeerTrustErrorKey](nsurlerrorfailingurlpeertrusterrorkey.md) — The state of a failed SSL handshake.
- [NSURLErrorFailingURLStringErrorKey](nsurlerrorfailingurlstringerrorkey.md) — The URL which caused a load to fail. _(deprecated)_
- [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) — A key in the error dictionary that provides the reason for canceling a background task.
- [NSURLErrorNetworkUnavailableReasonKey](nsurlerrornetworkunavailablereasonkey.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.

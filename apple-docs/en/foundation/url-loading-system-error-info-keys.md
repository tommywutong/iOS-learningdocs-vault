---
title: URL Loading System error info keys
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/url-loading-system-error-info-keys
source_url: 'https://developer.apple.com/documentation/foundation/url-loading-system-error-info-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url-loading-system-error-info-keys.json'
content_hash: 'sha256:ea59e257204bfa68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md)

# URL Loading System error info keys

<sub>API Collection</sub>

Recognize these keys from the user info dictionary of error objects produced by URL Loading APIs.

## Overview

These keys are only present in the [NSURLErrorDomain](nsurlerrordomain.md).

## Topics

### Keys

- [NSURLErrorFailingURLErrorKey](nsurlerrorfailingurlerrorkey.md) — The URL which caused a load to fail.
- [NSURLErrorFailingURLPeerTrustErrorKey](nsurlerrorfailingurlpeertrusterrorkey.md) — The state of a failed SSL handshake.
- [NSURLErrorFailingURLStringErrorKey](nsurlerrorfailingurlstringerrorkey.md) — The URL which caused a load to fail. _(deprecated)_
- [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) — A key in the error dictionary that provides the reason for canceling a background task.
- [URL Session Background Task Cancellation Reasons](url-session-background-task-cancellation-reasons.md) — Reasons that indicate why the system canceled a background task.
- [NSURLErrorNetworkUnavailableReasonKey](nsurlerrornetworkunavailablereasonkey.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.

### Deprecated

- [NSErrorFailingURLStringKey](nserrorfailingurlstringkey.md) — The URL that caused the error. _(deprecated)_

## See Also

### Errors

- [URLError](urlerror.md) — Error codes returned by URL loading APIs.

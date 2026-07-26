---
title: Common Mode Flag
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/common-mode-flag
source_url: 'https://developer.apple.com/documentation/corefoundation/common-mode-flag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/common-mode-flag.json'
content_hash: 'sha256:a6f030b9349e00e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFRunLoop](cfrunloop.md)

# Common Mode Flag

<sub>API Collection</sub>

A run loop pseudo-mode that manages objects monitored in the “common” modes.

## Overview

Run loops never run in this mode. This pseudo-mode is used only as a special set of sources, timers, and observers that is shared by other modes. See Managing Observers for more details.

## Topics

### Constants

- [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) — Objects added to a run loop using this value as the mode are monitored by all run loop modes that have been declared as a member of the set of “common” modes with [CFRunLoopAddCommonMode](<cfrunloopaddcommonmode(____).md>).

## See Also

### Constants

- [CFRunLoopRunInMode Exit Codes](cfrunloopruninmode_exit_codes.md) — Return codes for `CFRunLoopRunInMode`, identifying the reason the run loop exited.
- [Default Run Loop Mode](default-run-loop-mode.md) — Default run loop mode.

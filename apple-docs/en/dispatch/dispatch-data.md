---
title: Dispatch Data
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-data
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-data.json'
content_hash: 'sha256:06db74460102edef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch Data

<sub>API Collection</sub>

An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.

## Overview

The memory buffer managed by this object may be a single contiguous block of memory, or it may consist of multiple discontiguous blocks. For the discontiguous case, the dispatch data object makes it appear as if the memory is contiguous.

## Topics

### Creating a Dispatch Data Object

- [dispatch_data_t](dispatch_data_t.md) — An immutable object representing a contiguous or sparse region of memory.

## See Also

### System Event Monitoring

- [DispatchSource](dispatchsource.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [DispatchIO](dispatchio.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [DispatchData](dispatchdata.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchDataIterator](dispatchdataiterator.md) — A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](dispatch-i-o.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — Defines a common set of properties and methods that are shared with all dispatch source types.

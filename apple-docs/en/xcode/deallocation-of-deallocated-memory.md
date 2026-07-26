---
title: Deallocation of deallocated memory
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/deallocation-of-deallocated-memory
source_url: 'https://developer.apple.com/documentation/xcode/deallocation-of-deallocated-memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/deallocation-of-deallocated-memory.json'
content_hash: 'sha256:d624f9e63e25e381'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# Deallocation of deallocated memory

<sub>Article</sub>

Detects attempts to free deallocated memory.

## Overview

Use this check to detect when you call `free` on deallocated memory, commonly referred to as a _double free_ error. Attempting to deallocate memory more than once can result in a crash or other unpredictable behavior. Available in Xcode 7 and later.

### Deallocation of freed memory in C

In the following example, the code deallocates the `p_int` variable after the call to free its memory:

```occ
int *pointer = malloc(sizeof(int));
free(pointer);
free(pointer); // Error: free called twice with the same memory address 
```

#### Solution

Ensure that you call the `free` function just once for memory you allocate.

## See Also

### Address Sanitizer

- [Use of deallocated memory](use-of-deallocated-memory.md) — Detects the use of deallocated memory.
- [Deallocation of nonallocated memory](deallocation-of-nonallocated-memory.md) — Detects attempts to free nonallocated memory.
- [Use of stack memory after function return](use-of-stack-memory-after-function-return.md) — Detects when you access stack variable memory after its declaring function returns.
- [Use of out-of-scope stack memory](use-of-out-of-scope-stack-memory.md) — Detects access to variables outside of their declared scope.
- [Overflow and underflow of buffers](overflow-and-underflow-of-buffers.md) — Detects when you access memory outside of a buffer’s boundaries.
- [Overflow of C++ containers](overflow-of-c-containers.md) — Detects when you access a C++ container outside its bounds.

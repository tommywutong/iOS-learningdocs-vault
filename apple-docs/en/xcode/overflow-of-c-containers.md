---
title: Overflow of C++ containers
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/overflow-of-c-containers
source_url: 'https://developer.apple.com/documentation/xcode/overflow-of-c-containers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/overflow-of-c-containers.json'
content_hash: 'sha256:7d74c7dad9db5194'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# Overflow of C++ containers

<sub>Article</sub>

Detects when you access a C++ container outside its bounds.

## Overview

Use this check to detect when you access a libc++ container beyond the region `[container.begin(), container.end()]`, even when the accessed memory is in a heap-allocated buffer the container uses internally. Available in Xcode 7 and later.

> [!note] Note
> This check is enabled by default. In Xcode versions prior to version 26, it was disabled by default. See [Disabling Container Overflow Checks](overflow-of-c-containers.md#Disabling-Container-Overflow-Checks) to disable it.

### Vector overflow in C++

In the following example, the `vector` variable has valid indexes in the range `[0,2]`, but the accessed index is `3`, which causes an overflow:

```occ
std::vector<int> vector;
vector.push_back(0);
vector.push_back(1);
vector.push_back(2);
auto *pointer = &vector[0];
return pointer[3]; // Error: out of bounds access for vector
```

#### Solution

Add a bounds check before attempting to access a container at a specific index.

### Disabling Container Overflow Checks

> [!note] Note
> The [Enable C++ Container Overflow Checks](build-settings-reference.md#Enable-C++-Container-Overflow-Checks) build setting no longer has any effect in Xcode 26 onwards.

You may encounter a false-positive ‘Container overflow’ error when code that isn’t compiled with Address Sanitizer modifies a container. For container overflow checks to work correctly, you need to compile all code with Address Sanitizer. If you can’t do this, turn off container overflow checks using one of the following methods:

- **Set the ASAN_OPTIONS Environment Variable** — Set the `ASAN_OPTIONS` environment variable to `detect_container_overflow=0`, or append `:detect_container_overflow=0` to this environment variable if it has already been set. You should do this under the Scheme for Run targets, or Configurations for Test Plans. Note that for UI tests you may need to set this in the XCUIApplication [launchEnvironment](../xcuiautomation/xcuiapplication/launchenvironment.md).
- **Define the __asan_default_options function in your executable** — Use this method when you can’t control your program’s environment variables. Disable container overflow checks by defining the following function in your executable:

```occ
#ifdef __cplusplus
extern "C" {
#endif
#include <sanitizer/asan_interface.h>

__attribute__((used, visibility("default"))) const char *__asan_default_options() {
    return "detect_container_overflow=0";
}
#ifdef __cplusplus
}
#endif
```

If you set the [Exported Symbols File](build-settings-reference.md#Exported-Symbols-File) build setting, then also add `___asan_default_options` to the file to ensure that the system exports the symbol.

If you set the `detect_container_overflow` option in both the `__asan_default_options` function, and the `ASAN_OPTIONS` environment variable, the system uses the value in the environment variable.

## See Also

### Address Sanitizer

- [Use of deallocated memory](use-of-deallocated-memory.md) — Detects the use of deallocated memory.
- [Deallocation of deallocated memory](deallocation-of-deallocated-memory.md) — Detects attempts to free deallocated memory.
- [Deallocation of nonallocated memory](deallocation-of-nonallocated-memory.md) — Detects attempts to free nonallocated memory.
- [Use of stack memory after function return](use-of-stack-memory-after-function-return.md) — Detects when you access stack variable memory after its declaring function returns.
- [Use of out-of-scope stack memory](use-of-out-of-scope-stack-memory.md) — Detects access to variables outside of their declared scope.
- [Overflow and underflow of buffers](overflow-and-underflow-of-buffers.md) — Detects when you access memory outside of a buffer’s boundaries.

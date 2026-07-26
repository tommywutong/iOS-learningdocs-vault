---
title: Working with Concurrency
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/working-with-concurrency
source_url: 'https://developer.apple.com/documentation/security/working-with-concurrency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/working-with-concurrency.json'
content_hash: 'sha256:187f9e3bbb2b0f87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)

# Working with Concurrency

<sub>Article</sub>

Learn about thread safety issues related to the certificate, key, and trust services API.

## Overview

In macOS, some of the functions of this API block while waiting for input from the user (for example, when the user is asked to unlock a keychain or give permission to change trust settings). In general, it is safe to use this API in threads other than your main thread, but avoid calling the functions from multiple operations, work queues, or threads concurrently. Instead, serialize function calls or confine them to a single thread.

In iOS, all the functions in this API are thread-safe and reentrant.

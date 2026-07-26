---
title: Application binary interfaces
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/application-binary-interfaces
source_url: 'https://developer.apple.com/documentation/xcode/application-binary-interfaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/application-binary-interfaces.json'
content_hash: 'sha256:ec305ece526da45c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md)

# Application binary interfaces

Write assembly instructions that adhere to the application binary interfaces of Apple platforms.

## Overview

The CPUs found in Apple products define rules for how to call functions, manage the stack, and perform other operations. If your code includes assembly instructions, you must adhere to these rules to operate correctly with compiler-generated code. If you don’t adhere to them, your code might crash or behave unexpectedly.

## Topics

### 64-bit interfaces

- [Writing ARM64 code for Apple platforms](writing-arm64-code-for-apple-platforms.md) — Create 64-bit ARM assembly language instructions that adhere to the application binary interface (ABI) that Apple platforms support.
- [Writing 64-bit Intel code for Apple Platforms](writing-64-bit-intel-code-for-apple-platforms.md) — Create 64-bit Intel assembly language instructions that adhere to the application binary interface (ABI) that Apple platforms support.

### iOS interfaces

- [Writing ARMv7 code for iOS](writing-armv7-code-for-ios.md) — Create ARMv7 assembly language instructions that adhere to the application binary interface (ABI) that iOS supports.
- [Writing ARMv6 code for iOS](writing-armv6-code-for-ios.md) — Create ARMv6 assembly language instructions that adhere to the application binary interface (ABI) that iOS supports.

## See Also

### Hardware considerations

- [Apple silicon](../apple-silicon.md) — Get the resources you need to create software for Macs with Apple silicon.

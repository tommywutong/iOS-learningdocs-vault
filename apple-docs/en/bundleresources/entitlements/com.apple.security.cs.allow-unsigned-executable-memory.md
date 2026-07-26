---
title: Allow Unsigned Executable Memory Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.cs.allow-unsigned-executable-memory
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.allow-unsigned-executable-memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.cs.allow-unsigned-executable-memory.json'
content_hash: 'sha256:ff8c2c431500c9dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Allow Unsigned Executable Memory Entitlement

<sub>Property List Key</sub>

A Boolean value that indicates whether the app may create writable and executable memory without the restrictions imposed by using the `MAP_JIT` flag.

## Discussion

In rare cases, an app might need to override or patch C code, use the long-deprecated `NSCreateObjectFileImageFromMemory` (which is fundamentally insecure), or use the DVDPlayback framework. Add the [Allow Unsigned Executable Memory Entitlement](com.apple.security.cs.allow-unsigned-executable-memory.md) to enable these use cases. Otherwise, the app might crash or behave in unexpected ways.

> [!important] Important
> Including this entitlement exposes your app to common vulnerabilities in memory-unsafe code languages. Carefully consider whether your app needs this exception.

To add the entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Runtime Exceptions, select Allow Unsigned Executable Memory.

## See Also

### Hardened runtime

- [Allow execution of JIT-compiled code entitlement](com.apple.security.cs.allow-jit.md) — A Boolean value that indicates whether the app may create writable and executable memory using the `MAP_JIT` flag.
- [Allow DYLD environment variables entitlement](com.apple.security.cs.allow-dyld-environment-variables.md) — A Boolean value that indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process.
- [Disable Library Validation Entitlement](com.apple.security.cs.disable-library-validation.md) — A Boolean value that indicates whether the app loads arbitrary plug-ins or frameworks, without requiring code signing.
- [Disable Executable Memory Protection Entitlement](com.apple.security.cs.disable-executable-page-protection.md) — A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.
- [Debugging tool entitlement](com.apple.security.cs.debugger.md) — A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.

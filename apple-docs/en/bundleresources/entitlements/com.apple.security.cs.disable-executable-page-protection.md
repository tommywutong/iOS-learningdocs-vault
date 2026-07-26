---
title: Disable Executable Memory Protection Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.cs.disable-executable-page-protection
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.disable-executable-page-protection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.cs.disable-executable-page-protection.json'
content_hash: 'sha256:d15a7fcedc3117de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Disable Executable Memory Protection Entitlement

<sub>Property List Key</sub>

A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.

## Discussion

The system causes an app that attempts to directly modify sections of its own executable files on disk to forcefully exit. Use the [Disable Executable Memory Protection Entitlement](com.apple.security.cs.disable-executable-page-protection.md) to enable this kind of unsafe software update. Even with this entitlement, however, updates that modify some files but not others may cause unexpected app state. Ensure that you perform updates atomically, with the final app bundle swapped out after app exit.

The entitlement effectively encompasses the behavior provided by the [Allow Unsigned Executable Memory Entitlement](com.apple.security.cs.allow-unsigned-executable-memory.md), but not the [Disable Library Validation Entitlement](com.apple.security.cs.disable-library-validation.md).

> [!warning] Warning
> The [Disable Executable Memory Protection Entitlement](com.apple.security.cs.disable-executable-page-protection.md) is an extreme entitlement that removes a fundamental security protection from your app, making it possible for an attacker to rewrite your app’s executable code without detection. Prefer narrower entitlements if possible.

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Runtime Exceptions, select Disable Executable Memory Protection.

## See Also

### Hardened runtime

- [Allow execution of JIT-compiled code entitlement](com.apple.security.cs.allow-jit.md) — A Boolean value that indicates whether the app may create writable and executable memory using the `MAP_JIT` flag.
- [Allow Unsigned Executable Memory Entitlement](com.apple.security.cs.allow-unsigned-executable-memory.md) — A Boolean value that indicates whether the app may create writable and executable memory without the restrictions imposed by using the `MAP_JIT` flag.
- [Allow DYLD environment variables entitlement](com.apple.security.cs.allow-dyld-environment-variables.md) — A Boolean value that indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process.
- [Disable Library Validation Entitlement](com.apple.security.cs.disable-library-validation.md) — A Boolean value that indicates whether the app loads arbitrary plug-ins or frameworks, without requiring code signing.
- [Debugging tool entitlement](com.apple.security.cs.debugger.md) — A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.

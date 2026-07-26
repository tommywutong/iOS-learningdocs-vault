---
title: Disable Library Validation Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.cs.disable-library-validation
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.disable-library-validation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.cs.disable-library-validation.json'
content_hash: 'sha256:5d39f72ab5956aaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Disable Library Validation Entitlement

<sub>Property List Key</sub>

A Boolean value that indicates whether the app loads arbitrary plug-ins or frameworks, without requiring code signing.

## Discussion

The [Hardened Runtime](../../security/hardened-runtime.md) enables library validation by default. This security-hardening feature prevents a program from loading frameworks, plug-ins, or libraries unless they’re either signed by Apple or signed with the same Team ID as the main executable. The macOS dynamic linker (`dyld`) provides a detailed error message when the system prevents code from loading due to library validation. Use the [Disable Library Validation Entitlement](com.apple.security.cs.disable-library-validation.md) if your program loads plug-ins that are signed by other third-party developers.

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Runtime Exceptions, select Disable Library Validation.

> [!important] Important
> Because library validation is such an important security-hardening feature, Gatekeeper runs extra security checks on programs that have it disabled. If your program is blocked by Gatekeeper, check whether you’ve unnecessarily disabled library validation.

## See Also

### Hardened runtime

- [Allow execution of JIT-compiled code entitlement](com.apple.security.cs.allow-jit.md) — A Boolean value that indicates whether the app may create writable and executable memory using the `MAP_JIT` flag.
- [Allow Unsigned Executable Memory Entitlement](com.apple.security.cs.allow-unsigned-executable-memory.md) — A Boolean value that indicates whether the app may create writable and executable memory without the restrictions imposed by using the `MAP_JIT` flag.
- [Allow DYLD environment variables entitlement](com.apple.security.cs.allow-dyld-environment-variables.md) — A Boolean value that indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process.
- [Disable Executable Memory Protection Entitlement](com.apple.security.cs.disable-executable-page-protection.md) — A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.
- [Debugging tool entitlement](com.apple.security.cs.debugger.md) — A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.

---
title: System Integrity Protection Guide
apple_id: TP40016462
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: Security
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/System_Integrity_Protection_Guide/Introduction/Introduction.html
archived_at: '2026-07-18T02:06:31.672353Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](File%20System%20Protections.md)

# Introduction

System Integrity Protection is a security feature in macOS that protects the system shipped by Apple. By protecting access to system locations and restricting runtime attachment to system processes, this security policy guards against compromise — whether accidental or by malicious code.

macOS applies this security policy to every process running on the system, regardless of whether it’s running with administrative privileges or running unsandboxed.

If your app is distributed through the Mac App Store, System Integrity Protection has no impact because App Sandbox security policies are more restrictive.

If your app is not distributed through the Mac App Store, System Integrity Protection may have an impact.

This document covers the key concepts of System Integrity Protection and explains the implications it has on the design and capabilities of apps.

### System Locations Cannot Be Written To

System files can be modified only by system processes signed with Apple’s code signing identity. App processes should instead write to locations designated for third-party developers.

__Relevant Chapter:__ [File System Protections](File%20System%20Protections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinrsfvbuqmrnknltc)

### System Processes Cannot Be Attached To

System binaries can be modified only by Apple Installer and Software Update from Apple-provided packages, and no longer permit runtime attachment or code injection.

__Relevant Chapter:__ [Runtime Protections](Runtime%20Protections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinrsfvbuqmznknltc)

### Kernel Extensions Must Be Signed

Kernel extensions must be signed with a Developer ID for Signing Kexts certificate.

__Relevant Chapter:__ [Kernel Extensions](Kernel%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinrsfvbuqnbnknltc)

### System Integrity Protection Is Configured On Recovery OS

Security configuration is stored in NVRAM, and applies to the entire machine Persists across OS install. You can enable and disable System Integrity Protection by booting to Recovery OS and running the `csrutil(1)` command.

__Relevant Chapter:__ [Configuring System Integrity Protection](Configuring%20System%20Integrity%20Protection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinrsfvbuqnjnknltc)

Read _[Security Overview](../Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_ to understand the technologies used to make macOS secure.

For more information about kernel extensions, read the _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_.

[Next](File%20System%20Protections.md)


---
title: OS Services Framework Release Notes
apple_id: TP40006667
resource_type: Release Note
platform: macOS
topic: null
technology: CoreServices
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-OS_Services/index.html
archived_at: '2026-07-18T02:50:22.397576Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# OS Services Framework Release Notes for OS X v10.5

This document summarizes changes in the OS Services framework for OS X v10.5 (Leopard) that are of particular interest to software developers. Note that you may be able to find more information on these changes in Apple's developer documentation.

OS Services is a sub-framework of the Core Services umbrella framework. Clients of API in OS Services may link with the Core Services framework or a higher-level umbrella framework (Application Services, Cocoa, or Carbon).

#### Contents:

- [64-Bit Application Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnrxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Identity Services](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnrxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)

### 64-Bit Application Support

OS X Leopard contains 64-bit versions of many system frameworks, including many APIs in OS Services. Some OS Services APIs have been deprecated and are not available to 64-bit applications. The following deprecated OS Services API sets are not available to 64-bit applications:

- NSLCore
- OpenTransport
- Power
- SCSI

In addition, the File Manager `FSSpec` data type is deprecated in OS X Leopard. Consequently all functions with an `FSSpec` argument or result are not available in the 64-bit API. In OS Services, this includes just one additional function: `KCMakeKCRefFromFSSpec`.

All other OS Services APIs are available for use by 64-bit applications.

### Identity Services

Identity Services is a new API set in Leopard. It provides access to the system's user and group database used for managing access controls on OS X. This C API is based on the Core Foundation object runtime and naming conventions. It also uses the new Core Foundation `CFError` facility to report detailed error information to callers (See the _[Core Foundation Release Notes for OS X v10.9](https://developer.apple.com/library/archive/releasenotes/CoreFoundation/RN-CoreFoundation/index.html#//apple_ref/doc/uid/TP40000994)_ for more information about `CFError`). The Identity Services API is modeled around three object classes:

| Class | Function |
| --- | --- |
| `CSIdentity` | Provides access to attributer of a specific user or group |
| `CSIdentityAuthority` | Represents an authoritative repository of user and group information (e.g. the local system database or a network directory server). |
| `CSIdentityQuery` | Coordinates searching for identities using client-specified criteria |

---
title: AuthorizationCopyPrivilegedReference
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.1+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/authorizationcopyprivilegedreference
source_url: 'https://developer.apple.com/documentation/security/authorizationcopyprivilegedreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcopyprivilegedreference.json'
content_hash: 'sha256:3a4238e2eb3612b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationCopyPrivilegedReference

<sub>Function</sub>

Retrieves the authorization reference passed by the AuthorizationExecuteWithPrivileges function.

> [!warning] Deprecated
> Use a `launchd`-launched helper tool and/or the Service Management framework for this functionality.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus AuthorizationCopyPrivilegedReference(AuthorizationRef*authorization, AuthorizationFlags flags);
```

## Parameters

- `authorization` — A pointer to an authorization reference. The Security Server allocates the authorization reference for you, so you do not need to call the function [AuthorizationCreate](<authorizationcreate(________).md>). On return, it points to a copy of the authorization reference used in the call to the [AuthorizationExecuteWithPrivileges](authorizationexecutewithprivileges.md) function.

- `flags` — Reserved options. Pass the [kAuthorizationFlagDefaults](authorizationflags/kauthorizationflagdefaults.md) constant.

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. Use a `launchd`-launched helper tool and/or the Service Management framework for this functionality.

This function retrieves the authorization reference you pass in the function [AuthorizationExecuteWithPrivileges](authorizationexecutewithprivileges.md). The new process can use the authorization reference to verify authorizations obtained by the calling process.

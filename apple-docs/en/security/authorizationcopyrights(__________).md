---
title: 'AuthorizationCopyRights(_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationcopyrights(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationcopyrights(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcopyrights%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8980b87d50306cae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationCopyRights(_:_:_:_:_:)

<sub>Function</sub>

Authorizes and preauthorizes rights synchronously.

<sub>Mac Catalyst, macOS</sub>

```swift
func AuthorizationCopyRights(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>?, _ flags: AuthorizationFlags, _ authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>?) -> OSStatus
```

## Parameters

- `authorization` — An authorization reference referring to the authorization session.

- `rights` — A pointer to a set of authorization rights you create. Pass `nil` if the application requires no rights at this time.

- `environment` — Data used when authorizing or preauthorizing rights. Not used in OS X v10.2 and earlier. In macOS 10.3 and later, you can pass icon or prompt data to be used in the authentication dialog box. In macOS 10.4 and later, you can also pass a user name and password in order to authorize a user without displaying the authentication dialog box. Possible values for this parameter are listed in `Security.framework/Headers/AuthorizationTags.h`. The data passed in this parameter is not stored in the authorization reference; it is used only during authorization. If you are not passing any data in this parameter, pass the constant [kAuthorizationEmptyEnvironment](kauthorizationemptyenvironment.md).

- `flags` — A bit mask for specifying authorization options. Use the following option sets. - Pass the constant [kAuthorizationFlagDefaults](authorizationflags/kauthorizationflagdefaults.md) if no options are necessary. - Specify the [kAuthorizationFlagExtendRights](authorizationflags/extendrights.md) mask to request rights. You can also specify the [kAuthorizationFlagInteractionAllowed](authorizationflags/interactionallowed.md) mask to allow user interaction. - Specify the [kAuthorizationFlagPartialRights](authorizationflags/partialrights.md) and [kAuthorizationFlagExtendRights](authorizationflags/extendrights.md) masks to request partial rights. You can also specify the [kAuthorizationFlagInteractionAllowed](authorizationflags/interactionallowed.md) mask to allow user interaction. - Specify the [kAuthorizationFlagPreAuthorize](authorizationflags/preauthorize.md) and [kAuthorizationFlagExtendRights](authorizationflags/extendrights.md) masks to preauthorize rights. - Specify the [kAuthorizationFlagDestroyRights](authorizationflags/destroyrights.md) mask to prevent the Security Server from preserving the rights obtained during this call.

- `authorizedRights` — A pointer to a newly allocated [AuthorizationRights](authorizationrights.md) structure. On return, this structure contains the rights granted by the Security framework. If you do not require this information, pass `nil`. If you specify the [kAuthorizationFlagPreAuthorize](authorizationflags/preauthorize.md) mask in the `flags` parameter, the method returns all the requested rights, including those not granted, but the flags of the rights that could not be preauthorized include the [kAuthorizationFlagCanNotPreAuthorize](kauthorizationflagcannotpreauthorize.md) bit. Free the memory associated with this set by calling the function [AuthorizationFreeItemSet](<authorizationfreeitemset(__).md>).

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

There are three main reasons to use this function. The first reason is to preauthorize rights by specifying the [kAuthorizationFlagPreAuthorize](authorizationflags/preauthorize.md), [kAuthorizationFlagInteractionAllowed](authorizationflags/interactionallowed.md), and [kAuthorizationFlagExtendRights](authorizationflags/extendrights.md) masks as authorization options. Preauthorization is most useful when a right has a zero timeout. For example, you can preauthorize in the application and if it succeeds, call the helper tool and request authorization. This eliminates calling the helper tool if the Security Server cannot later authorize the specified rights.

The second reason to use this function is to authorize rights before performing a privileged operation by specifying the [kAuthorizationFlagInteractionAllowed](authorizationflags/interactionallowed.md), and [kAuthorizationFlagExtendRights](authorizationflags/extendrights.md) masks as authorization options.

The third reason to use this function is to authorize partial rights. By specifying the [kAuthorizationFlagPartialRights](authorizationflags/partialrights.md), [kAuthorizationFlagInteractionAllowed](authorizationflags/interactionallowed.md), and [kAuthorizationFlagExtendRights](authorizationflags/extendrights.md) masks as authorization options, the Security Server grants all rights it can authorize. On return, the authorized set contains all the rights.

If you do not specify the [kAuthorizationFlagPartialRights](authorizationflags/partialrights.md) mask and the Security Server denies at least one right, then the status of this function on return is [errAuthorizationDenied](errauthorizationdenied.md).

If you do not specify the [kAuthorizationFlagInteractionAllowed](authorizationflags/interactionallowed.md) mask and the Security Server requires user interaction, then the status of this function on return is [errAuthorizationInteractionNotAllowed](errauthorizationinteractionnotallowed.md).

If you specify the [kAuthorizationFlagInteractionAllowed](authorizationflags/interactionallowed.md) mask and the user cancels the authentication process, then the status of this function on return is [errAuthorizationCanceled](errauthorizationcanceled.md).

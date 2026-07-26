---
title: PluginDestroy
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationplugininterface/plugindestroy
source_url: 'https://developer.apple.com/documentation/security/authorizationplugininterface/plugindestroy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationplugininterface/plugindestroy.json'
content_hash: 'sha256:df87e9740c3bfce4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationPluginInterface](../authorizationplugininterface.md)

# PluginDestroy

<sub>Instance Property</sub>

Notifies the plug-in that it is about to be unloaded.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(void *) PluginDestroy;
```

## Parameters

- `inPlugin` — The authorization plug-in reference you assigned to the plug-in in the [AuthorizationPluginCreate](../authorizationplugincreate.md) function.

## Return Value

A result code. Return [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) if the function completes successfully and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error) if any error occurs.

## Discussion

When this function is called, your plug-in should release any resources it is holding and do any other cleanup necessary (such as deleting temporary files) before it is unloaded.

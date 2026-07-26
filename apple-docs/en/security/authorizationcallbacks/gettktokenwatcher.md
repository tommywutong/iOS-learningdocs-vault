---
title: GetTKTokenWatcher
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.13.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/gettktokenwatcher
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/gettktokenwatcher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/gettktokenwatcher.json'
content_hash: 'sha256:2e4ae46dd510a610'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# GetTKTokenWatcher

<sub>Instance Property</sub>

Constructs a token watcher.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const void **) GetTKTokenWatcher;
```

## Parameters

- `inEngine` — An opaque handle that’s passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `outValue` — A pointer the function uses to return the [TKTokenWatcher](../../cryptotokenkit/tktokenwatcher.md) instance.

## Discussion

The caller owns the returned token watcher and is responsible for releasing it.

> [!important] Important
> This function is only available when the callback [version](version.md) is 3 or higher.

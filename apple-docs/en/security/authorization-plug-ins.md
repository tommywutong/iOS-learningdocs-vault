---
title: Authorization Plug-ins
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorization-plug-ins
source_url: 'https://developer.apple.com/documentation/security/authorization-plug-ins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorization-plug-ins.json'
content_hash: 'sha256:7311c8a9b7a641e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# Authorization Plug-ins

<sub>API Collection</sub>

Extend the authorization services API by creating plug-ins that can participate in authorization decisions.

## Overview

Use plug-ins to extend macOS authorization services to perform authorizations in a new way or to implement a new policy that is too complex to be implemented entirely with the authorization policy database.

You must import this API explicitly:

**Swift**

```swift
import Security.AuthorizationPlugin
```

**Objective-C**

```objc
#import <Security/AuthorizationPlugin.h>       
```

> [!note] Note
> When your plug-in needs to interact with the user, subclass the [SFAuthorizationPluginView](../securityinterface/sfauthorizationpluginview.md) class to maintain the look and feel of the system authentication dialogs.

## Topics

### First Steps

- [Extending authorization services with plug-ins](extending-authorization-services-with-plug-ins.md) — Modify the system’s authorization policy with custom code.

### Creating a Plug-in

- [AuthorizationCallbacks Version](authorizationcallbacks-version.md) — The version of the interface implemented by the authorization engine.
- [AuthorizationPluginInterface Version](authorizationplugininterface-version.md) — The version of the interface implemented by the plug-in.

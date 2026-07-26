---
title: Authorization Rights Flags
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorization-rights-flags
source_url: 'https://developer.apple.com/documentation/security/authorization-rights-flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorization-rights-flags.json'
content_hash: 'sha256:dc62092e315abe09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Authorization Services](authorization-services.md)

# Authorization Rights Flags

<sub>API Collection</sub>

Recognize the values the Security Server sets in an authorization item’s flag field.

## Overview

Look for these values in the [flags](authorizationitem/flags.md) field of an [AuthorizationItem](authorizationitem.md), for example among the set of items in the `authorizedRights` parameter returned by a call to the [AuthorizationCopyInfo](<authorizationcopyinfo(______).md>) function.

## Topics

### Constants

- [kAuthorizationFlagCanNotPreAuthorize](kauthorizationflagcannotpreauthorize.md) — Indicates the Security Server could not preauthorizethe right.

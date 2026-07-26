---
title: 'set(_:for:task:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/set(_:for:task:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/set(_:for:task:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/set%28_%3Afor%3Atask%3A%29.json'
content_hash: 'sha256:2d476425b1c65e58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# set(_:for:task:)

<sub>Instance Method</sub>

Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func set(_ credential: URLCredential, for protectionSpace: URLProtectionSpace, task: URLSessionTask)
```

## Parameters

- `credential` — The credential to add. If a credential with the same user name already exists in `space`, then `credential` replaces the existing object.

- `protectionSpace` — The protection space to which to add the credential.

- `task` — The task accessing the specified protection space. Subclasses of [URLCredentialStorage](../urlcredentialstorage.md) may use the request URL or other properties of this task to affect how the default credential is stored.

## See Also

### Adding and removing credentials

- [- removeCredential:forProtectionSpace:](<remove(__for_).md>) — Removes the specified credential from the credential storage for the specified protection space.
- [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>) — Removes the specified credential from the credential storage for the specified protection space using the given options.
- [- removeCredential:forProtectionSpace:options:task:](<remove(__for_options_task_).md>) — Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md) — Key used by the options dictionary passed in [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>).
- [- setCredential:forProtectionSpace:](<set(__for_).md>) — Adds a credential to the credential storage for the specified protection space.

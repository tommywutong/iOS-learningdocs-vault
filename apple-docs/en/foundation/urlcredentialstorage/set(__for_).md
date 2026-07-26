---
title: 'set(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/set(_:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/set(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/set%28_%3Afor%3A%29.json'
content_hash: 'sha256:49052ddb1aa475fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# set(_:for:)

<sub>Instance Method</sub>

Adds a credential to the credential storage for the specified protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func set(_ credential: URLCredential, for space: URLProtectionSpace)
```

## Parameters

- `credential` — The credential to add. If a credential with the same user name already exists in `space`, then `credential` replaces the existing object.

- `space` — The protection space to which to add the credential.

## Discussion

If the credential is not yet in the set for the protection space, it will be added to it.

If you override this method, also override [- setCredential:forProtectionSpace:task:](<set(__for_task_).md>).

## See Also

### Adding and removing credentials

- [- removeCredential:forProtectionSpace:](<remove(__for_).md>) — Removes the specified credential from the credential storage for the specified protection space.
- [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>) — Removes the specified credential from the credential storage for the specified protection space using the given options.
- [- removeCredential:forProtectionSpace:options:task:](<remove(__for_options_task_).md>) — Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md) — Key used by the options dictionary passed in [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>).
- [- setCredential:forProtectionSpace:task:](<set(__for_task_).md>) — Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.

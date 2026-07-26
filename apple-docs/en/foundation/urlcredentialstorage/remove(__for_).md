---
title: 'remove(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/remove(_:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/remove(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/remove%28_%3Afor%3A%29.json'
content_hash: 'sha256:e6a44f9280691aa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# remove(_:for:)

<sub>Instance Method</sub>

Removes the specified credential from the credential storage for the specified protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ credential: URLCredential, for space: URLProtectionSpace)
```

## Parameters

- `credential` — The credential to remove.

- `space` — The protection space from which to remove the credential.

## Discussion

If you override this method, also override [- removeCredential:forProtectionSpace:options:task:](<remove(__for_options_task_).md>).

## See Also

### Adding and removing credentials

- [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>) — Removes the specified credential from the credential storage for the specified protection space using the given options.
- [- removeCredential:forProtectionSpace:options:task:](<remove(__for_options_task_).md>) — Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md) — Key used by the options dictionary passed in [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>).
- [- setCredential:forProtectionSpace:](<set(__for_).md>) — Adds a credential to the credential storage for the specified protection space.
- [- setCredential:forProtectionSpace:task:](<set(__for_task_).md>) — Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.

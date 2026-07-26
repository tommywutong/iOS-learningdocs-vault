---
title: 'remove(_:for:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/remove(_:for:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/remove(_:for:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/remove%28_%3Afor%3Aoptions%3A%29.json'
content_hash: 'sha256:89e5a9ceb988150a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# remove(_:for:options:)

<sub>Instance Method</sub>

Removes the specified credential from the credential storage for the specified protection space using the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ credential: URLCredential, for space: URLProtectionSpace, options: [String : Any]? = nil)
```

## Parameters

- `credential` — The credential to remove.

- `space` — The protection space from which to remove the credential.

- `options` — A dictionary containing options to consider when removing the credential. For possible keys, see [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md). You should use this when trying to delete a credential that has the [NSURLCredentialPersistenceSynchronizable](../urlcredential/persistence-swift.enum/synchronizable.md) policy. > [!note] Note > When credential objects that have a [NSURLCredentialPersistenceSynchronizable](../urlcredential/persistence-swift.enum/synchronizable.md) policy are removed, the credential will be removed on all devices that contain this credential.

## Discussion

The credential is removed from both persistent and temporary storage.

If you override this method, also override [- removeCredential:forProtectionSpace:options:task:](<remove(__for_options_task_).md>).

## See Also

### Adding and removing credentials

- [- removeCredential:forProtectionSpace:](<remove(__for_).md>) — Removes the specified credential from the credential storage for the specified protection space.
- [- removeCredential:forProtectionSpace:options:task:](<remove(__for_options_task_).md>) — Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md) — Key used by the options dictionary passed in [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>).
- [- setCredential:forProtectionSpace:](<set(__for_).md>) — Adds a credential to the credential storage for the specified protection space.
- [- setCredential:forProtectionSpace:task:](<set(__for_task_).md>) — Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.

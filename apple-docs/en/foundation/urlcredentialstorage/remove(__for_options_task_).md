---
title: 'remove(_:for:options:task:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/remove(_:for:options:task:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/remove(_:for:options:task:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/remove%28_%3Afor%3Aoptions%3Atask%3A%29.json'
content_hash: 'sha256:44758093a4066f2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# remove(_:for:options:task:)

<sub>Instance Method</sub>

Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ credential: URLCredential, for protectionSpace: URLProtectionSpace, options: [String : Any]? = nil, task: URLSessionTask)
```

## Parameters

- `credential` — The credential to remove.

- `protectionSpace` — The protection space from which to remove the credential.

- `options` — A dictionary containing options to consider when removing the credential. For possible keys, see [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md). You should use this when trying to delete a credential that has the [NSURLCredentialPersistenceSynchronizable](../urlcredential/persistence-swift.enum/synchronizable.md) policy. > [!note] Note > When credential objects that have a `synchronizable` policy are removed, the credential will be removed on all devices that contain this credential.

- `task` — The task using the protection space that you wish to remove the credential for.

## Discussion

The credential is removed from both persistent and temporary storage.

## See Also

### Adding and removing credentials

- [- removeCredential:forProtectionSpace:](<remove(__for_).md>) — Removes the specified credential from the credential storage for the specified protection space.
- [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>) — Removes the specified credential from the credential storage for the specified protection space using the given options.
- [Dictionary key for credential removal options](../dictionary-key-for-credential-removal-options.md) — Key used by the options dictionary passed in [- removeCredential:forProtectionSpace:options:](<remove(__for_options_).md>).
- [- setCredential:forProtectionSpace:](<set(__for_).md>) — Adds a credential to the credential storage for the specified protection space.
- [- setCredential:forProtectionSpace:task:](<set(__for_task_).md>) — Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.

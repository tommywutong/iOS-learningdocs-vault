---
title: Dictionary key for credential removal options
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dictionary-key-for-credential-removal-options
source_url: 'https://developer.apple.com/documentation/foundation/dictionary-key-for-credential-removal-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dictionary-key-for-credential-removal-options.json'
content_hash: 'sha256:2977e488c1ff6c7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLCredentialStorage](urlcredentialstorage.md)

# Dictionary key for credential removal options

<sub>API Collection</sub>

Key used by the options dictionary passed in [- removeCredential:forProtectionSpace:options:](<urlcredentialstorage/remove(__for_options_).md>).

## Topics

### Options

- [NSURLCredentialStorageRemoveSynchronizableCredentials](nsurlcredentialstorageremovesynchronizablecredentials.md) — The corresponding value is an `NSNumber` object representing a Boolean value that indicates whether credentials which contain the [NSURLCredentialPersistenceSynchronizable](urlcredential/persistence-swift.enum/synchronizable.md) attribute should be removed.

## See Also

### Adding and removing credentials

- [- removeCredential:forProtectionSpace:](<urlcredentialstorage/remove(__for_).md>) — Removes the specified credential from the credential storage for the specified protection space.
- [- removeCredential:forProtectionSpace:options:](<urlcredentialstorage/remove(__for_options_).md>) — Removes the specified credential from the credential storage for the specified protection space using the given options.
- [- removeCredential:forProtectionSpace:options:task:](<urlcredentialstorage/remove(__for_options_task_).md>) — Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [- setCredential:forProtectionSpace:](<urlcredentialstorage/set(__for_).md>) — Adds a credential to the credential storage for the specified protection space.
- [- setCredential:forProtectionSpace:task:](<urlcredentialstorage/set(__for_task_).md>) — Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.

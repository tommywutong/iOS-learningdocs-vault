---
title: URLCredentialStorage
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredentialstorage
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage.json'
content_hash: 'sha256:87fdfc2ed3ee347b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLCredentialStorage

<sub>Class</sub>

The manager of a shared credentials cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLCredentialStorage
```

## Overview

The shared cache stores and retrieves instances of [URLCredential](urlcredential.md). You can store password-based credentials permanently, based on the [Persistence](urlcredential/persistence-swift.enum.md) they were created with. Certificate-based credentials are never stored permanently.

### Subclassing notes

The [URLCredentialStorage](urlcredentialstorage.md) class is meant to be used as-is, but you can subclass it if you have specific needs, such as screening which credentials are stored.

When overriding methods of this class, be aware that methods that take a `task` parameter are preferred to equivalent methods that do not. Therefore, you should override the task-based methods when subclassing, as follows:

- Setting credentials — Override [- setCredential:forProtectionSpace:task:](<urlcredentialstorage/set(__for_task_).md>) instead of or in addition to [- setCredential:forProtectionSpace:](<urlcredentialstorage/set(__for_).md>).
- Getting credentials — Override [- getCredentialsForProtectionSpace:task:completionHandler:](<urlcredentialstorage/getcredentials(for_task_completionhandler_).md>) instead of or in addition to [- credentialsForProtectionSpace:](<urlcredentialstorage/credentials(for_).md>).
- Removing credentials — Override [- removeCredential:forProtectionSpace:options:task:](<urlcredentialstorage/remove(__for_options_task_).md>) instead of or in addition to [- removeCredential:forProtectionSpace:options:](<urlcredentialstorage/remove(__for_options_).md>) and [- removeCredential:forProtectionSpace:](<urlcredentialstorage/remove(__for_).md>).
- Setting default credentials — Override [- setDefaultCredential:forProtectionSpace:task:](<urlcredentialstorage/setdefaultcredential(__for_task_).md>) instead of or in addition to [- setDefaultCredential:forProtectionSpace:](<urlcredentialstorage/setdefaultcredential(__for_).md>).
- Getting default credentials — Override [- getDefaultCredentialForProtectionSpace:task:completionHandler:](<urlcredentialstorage/getdefaultcredential(for_task_completionhandler_).md>) instead of or in addition to [- defaultCredentialForProtectionSpace:](<urlcredentialstorage/defaultcredential(for_).md>).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the credential storage

- [sharedCredentialStorage](urlcredentialstorage/shared.md) — The shared URL credential storage instance.

### Getting and setting default credentials

- [- defaultCredentialForProtectionSpace:](<urlcredentialstorage/defaultcredential(for_).md>) — Returns the default credential for the specified protection space.
- [- getDefaultCredentialForProtectionSpace:task:completionHandler:](<urlcredentialstorage/getdefaultcredential(for_task_completionhandler_).md>) — Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [- setDefaultCredential:forProtectionSpace:](<urlcredentialstorage/setdefaultcredential(__for_).md>) — Sets the default credential for a specified protection space.
- [- setDefaultCredential:forProtectionSpace:task:](<urlcredentialstorage/setdefaultcredential(__for_task_).md>) — Sets the default credential for a given protection space, which is being accessed by the given task.

### Adding and removing credentials

- [- removeCredential:forProtectionSpace:](<urlcredentialstorage/remove(__for_).md>) — Removes the specified credential from the credential storage for the specified protection space.
- [- removeCredential:forProtectionSpace:options:](<urlcredentialstorage/remove(__for_options_).md>) — Removes the specified credential from the credential storage for the specified protection space using the given options.
- [- removeCredential:forProtectionSpace:options:task:](<urlcredentialstorage/remove(__for_options_task_).md>) — Removes the specified credential from the credential storage for the specified protection space, on behalf of the given task and using the given options.
- [Dictionary key for credential removal options](dictionary-key-for-credential-removal-options.md) — Key used by the options dictionary passed in [- removeCredential:forProtectionSpace:options:](<urlcredentialstorage/remove(__for_options_).md>).
- [- setCredential:forProtectionSpace:](<urlcredentialstorage/set(__for_).md>) — Adds a credential to the credential storage for the specified protection space.
- [- setCredential:forProtectionSpace:task:](<urlcredentialstorage/set(__for_task_).md>) — Adds a credential to the credential storage for the specified protection space, on behalf of the specified task.

### Retrieving credentials

- [allCredentials](urlcredentialstorage/allcredentials.md) — The credentials for all available protection spaces.
- [- credentialsForProtectionSpace:](<urlcredentialstorage/credentials(for_).md>) — Returns a dictionary containing the credentials for the specified protection space.
- [- getCredentialsForProtectionSpace:task:completionHandler:](<urlcredentialstorage/getcredentials(for_task_completionhandler_).md>) — Gets a dictionary containing the credentials for the specified protection space, on behalf of the given task, and passes the dictionary to the provided completion handler.

### Tracking credential storage changes

- [NSURLCredentialStorageChangedNotification](nsnotification/name-swift.struct/nsurlcredentialstoragechanged.md) — A notification posted when the set of stored credentials changes. _(deprecated)_

## See Also

### Authentication and credentials

- [Handling an authentication challenge](handling-an-authentication-challenge.md) — Respond appropriately when a server demands authentication for a URL request.
- [URLAuthenticationChallenge](urlauthenticationchallenge.md) — A challenge from a server requiring authentication from the client.
- [URLCredential](urlcredential.md) — `A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.
- [URLProtectionSpace](urlprotectionspace.md) — A server or an area on a server, commonly referred to as a realm, that requires authentication.

---
title: LARightStore
framework: Local Authentication
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/localauthentication/larightstore
source_url: 'https://developer.apple.com/documentation/localauthentication/larightstore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/localauthentication/larightstore.json'
content_hash: 'sha256:444173e5b1a8abc1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Local Authentication](../localauthentication.md)

# LARightStore

<sub>Class</sub>

A container for data protected by a right.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class LARightStore
```

## Overview

Use an [LARightStore](larightstore.md) along with an [LARight](laright.md) to make secrets accessible only after certain conditions, including authentication, are met. Storing secrets this way lets you tie the availability of sensitive resources to the authorization status of the user.

The following stores a named access token behind the default authorization requirements:

```swift
func storeBackendAccessToken(_ token: Data) async throws {
    let loginRight = LARight()
    _ = try await LARightStore.shared.saveRight(loginRight, identifier: "access-token", secret: token)
}
```

The system stores your secret in the keychain and protects it with a unique key in the Secure Enclave. The system associates the key with your right and with an access control list that ensures that the data is only accessible after your access requirements are met.

You can retrieve stored secrets later using the right’s identifier:

```swift
func fetchBackendAccessToken() async throws -> Data {
    let loginRight = try await LARightStore.shared.right(forIdentifier: "access-token")

    // Authorize the right or else the secret is unavailable.
    try await loginRight.authorize(localizedReason: "Access sandcastle competition server")
    return try await loginRight.secret.rawData
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing rights

- [sharedStore](larightstore/shared.md) — A shared object that stores rights.
- [- rightForIdentifier:completion:](<larightstore/right(foridentifier_completion_).md>) — Fetches a previously stored right from the shared right store.

### Storing rights

- [- saveRight:identifier:completion:](<larightstore/saveright(__identifier_completion_).md>) — Saves a right to a persistent right store.
- [- saveRight:identifier:secret:completion:](<larightstore/saveright(__identifier_secret_completion_).md>) — Saves a right to a persistent store along with secret data you supply.

### Removing stored rights

- [- removeRight:completion:](<larightstore/removeright(__completion_).md>) — Removes a right from the right store given an instance of that right.
- [- removeRightForIdentifier:completion:](<larightstore/removeright(foridentifier_completion_).md>) — Removes a right from the right store given its unique identifier.
- [- removeAllRightsWithCompletion:](<larightstore/removeallrights(completion_).md>) — Removes all rights associated with this client from the right store.

## See Also

### Persistence

- [LAPersistedRight](lapersistedright.md) — A right that gates access to a key and a secret.
- [LASecret](lasecret.md) — Data that’s protected by a persisted right.

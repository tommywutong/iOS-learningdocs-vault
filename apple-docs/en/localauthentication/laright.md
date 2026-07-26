---
title: LARight
framework: Local Authentication
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/localauthentication/laright
source_url: 'https://developer.apple.com/documentation/localauthentication/laright'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/localauthentication/laright.json'
content_hash: 'sha256:fc6a9ef6c46cca64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Local Authentication](../localauthentication.md)

# LARight

<sub>Class</sub>

A grouped set of requirements that gate access to a resource or operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class LARight
```

## Overview

Use [LARight](laright.md) instances to protect access to portions of your app that may contain sensitive information. By default, [LARight](laright.md) instances require people to authenticate with Face ID, Touch ID, Apple Watch, or the device passcode. The following creates an [LARight](laright.md) with the default authentication requirements:

```swift
let loginRight = LARight()
    
func login() async throws {
    try await loginRight.authorize(localizedReason: "Access sandcastle competition designs")
}

func logout() async {
    await loginRight.deauthorize()
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [LAPersistedRight](lapersistedright.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Authorizing a right

- [- init](<laright/init().md>) — Creates a right using the default authorization requirements.
- [- initWithRequirement:](<laright/init(requirement_).md>) — Creates a right with the authentication requirements you supply.
- [tag](laright/tag.md) — An integer you use to identify a right.
- [- authorizeWithLocalizedReason:completion:](<laright/authorize(localizedreason_completion_).md>) — Performs an authorization on the right.
- [- authorizeWithLocalizedReason:inPresentationContext:completion:](<laright/authorize(localizedreason_in_completion_).md>) — Performs an authorization on the right with a window context you supply.

### Deauthorizing a right

- [- deauthorizeWithCompletion:](<laright/deauthorize(completion_).md>) — Invalidates a previously authorized right.

### Monitoring authorization status

- [- checkCanAuthorizeWithCompletion:](<laright/checkcanauthorize(completion_).md>) — Checks whether the right has permission to perform authorization.
- [state](laright/state-swift.property.md) — The current authorization state for a right.
- [State](laright/state-swift.enum.md) — The possible states for a right during authorization.

## See Also

### Authentication and access

- [State](laright/state-swift.enum.md) — The possible states for a right during authorization.
- [LAContext](lacontext.md) — A mechanism for evaluating authentication policies and access controls.

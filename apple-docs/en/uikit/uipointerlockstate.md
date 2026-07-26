---
title: UIPointerLockState
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerlockstate
source_url: 'https://developer.apple.com/documentation/uikit/uipointerlockstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerlockstate.json'
content_hash: 'sha256:1bb6ac262de83d68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerLockState

<sub>Class</sub>

An object that contains information about a scene’s pointer lock state.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPointerLockState
```

## Overview

To prevent the pointer from triggering system gestures, for example, bringing up the dock, lock it to your application. Locking the pointer hides the pointer and locks it to just your full-screen application.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Checking the Lock State

- [locked](uipointerlockstate/islocked.md) — A Boolean value that indicates whether the pointer is locked.

### Updating the Lock State

- [UIPointerLockStateDidChangeNotification](uipointerlockstate/didchangenotification.md) — A notification that posts when the value of the locked state for a scene changes.
- [UIPointerLockStateSceneUserInfoKey](uipointerlockstate/sceneuserinfokey.md) — A key that reflects the new locked state.

### Structures

- [DidChangeMessage](uipointerlockstate/didchangemessage.md)

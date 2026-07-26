---
title: UISceneDestructionCondition
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenedestructioncondition
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedestructioncondition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedestructioncondition.json'
content_hash: 'sha256:477ca608d9702369'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneDestructionCondition

<sub>Class</sub>

Specifies when UIKit destroys the current scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UISceneDestructionCondition : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Type Methods

- [systemDisconnection](uiscenedestructioncondition/systemdisconnection.md) — The scene should be destroyed when disconnected by the system. For example, terminating the process, or rebooting the device.
- [userInitiatedDismissal](uiscenedestructioncondition/userinitiateddismissal.md) — The scene should be destroyed when dismissed by the user. For example, swiping home on iOS, or tapping x on visionOS.

## See Also

### Specifying the scene’s destruction conditions

- [destructionConditions](uiscene/destructionconditions-1a41l.md)

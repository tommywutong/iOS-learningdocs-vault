---
title: childBehaviors
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicbehavior/childbehaviors
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicbehavior/childbehaviors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicbehavior/childbehaviors.json'
content_hash: 'sha256:3fbe107a8dc8e8b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicBehavior](../uidynamicbehavior.md)

# childBehaviors

<sub>Instance Property</sub>

Returns the array of dynamic behaviors that are children of a custom dynamic behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var childBehaviors: [UIDynamicBehavior] { get }
```

## Discussion

Only custom subclasses of the class can have child behaviors.

## See Also

### Configuring a dynamic behavior

- [action](action.md) — The block you want to execute during dynamic animation.
- [- addChildBehavior:](<addchildbehavior(__).md>) — Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [- removeChildBehavior:](<removechildbehavior(__).md>) — Removes a child dynamic behavior from a custom dynamic behavior.

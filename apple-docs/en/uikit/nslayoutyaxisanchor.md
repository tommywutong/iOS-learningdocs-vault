---
title: NSLayoutYAxisAnchor
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutyaxisanchor
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutyaxisanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutyaxisanchor.json'
content_hash: 'sha256:3fca627963127139'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSLayoutYAxisAnchor

<sub>Class</sub>

A factory class for creating vertical layout constraint objects using a fluent API.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSLayoutYAxisAnchor
```

## Overview

[NSLayoutYAxisAnchor](nslayoutyaxisanchor.md) adds type information to the methods inherited from [NSLayoutAnchor](nslayoutanchor.md). Specifically, the generic methods declared by [NSLayoutAnchor](nslayoutanchor.md) must now take a matching [NSLayoutYAxisAnchor](nslayoutyaxisanchor.md) object.

**Swift**

```swift
// This constraint is valid
cancelButton.topAnchor.constraintEqualToAnchor(saveButton.topAnchor, constant: 8.0).isActive = true
 
// This constraint generates an incompatible pointer type warning
cancelButton.topAnchor.constraintEqualToAnchor(saveButton.trailingAnchor, constant: 8.0).isActive = true
```

**Objective-C**

```objc
// This constraint is valid
[self.cancelButton.leadingAnchor constraintEqualToAnchor:self.saveButton.trailingAnchor constant: 8.0].active = true;
 
// This constraint generates an incompatible pointer type warning
[self.cancelButton.topAnchor constraintEqualToAnchor:self.saveButton.trailingAnchor constant: 8.0].active = true;
```

For more information on using layout anchors, see [NSLayoutAnchor](nslayoutanchor.md).

## Relationships

- **Inherits From**: [NSLayoutAnchor](nslayoutanchor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Building system spacing constraints

- [- constraintEqualToSystemSpacingBelowAnchor:multiplier:](<nslayoutyaxisanchor/constraint(equaltosystemspacingbelow_multiplier_).md>) — Returns a constraint that defines the specific distance at which the current anchor is positioned below the specified anchor.
- [- constraintGreaterThanOrEqualToSystemSpacingBelowAnchor:multiplier:](<nslayoutyaxisanchor/constraint(greaterthanorequaltosystemspacingbelow_multiplier_).md>) — Returns a constraint that defines the minimum distance by which the current anchor is positioned below the specified anchor.
- [- constraintLessThanOrEqualToSystemSpacingBelowAnchor:multiplier:](<nslayoutyaxisanchor/constraint(lessthanorequaltosystemspacingbelow_multiplier_).md>) — Returns a constraint that defines the maximum distance by which the current anchor is positioned below the specified anchor.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.

### Creating a layout dimension

- [- anchorWithOffsetToAnchor:](<nslayoutyaxisanchor/anchorwithoffset(to_).md>) — Creates a layout dimension object from two anchors.

## See Also

### Related Documentation

- [NSLayoutConstraint](nslayoutconstraint.md) — The relationship between two user interface objects that must be satisfied by the constraint-based layout system.
- [Auto Layout Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html?language=swift#//apple_ref/doc/uid/TP40010853)

### Anchors

- [NSLayoutAnchor](nslayoutanchor.md) — A factory class for creating layout constraint objects using a fluent API.
- [NSLayoutXAxisAnchor](nslayoutxaxisanchor.md) — A factory class for creating horizontal layout constraint objects using a fluent API.
- [NSLAYOUTANCHOR_H](nslayoutanchor_h.md)

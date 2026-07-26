---
title: NSLayoutDimension
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutdimension
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutdimension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutdimension.json'
content_hash: 'sha256:d57ae9fca18c8cf9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSLayoutDimension

<sub>Class</sub>

A factory class for creating size-based layout constraint objects using a fluent API.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSLayoutDimension
```

## Overview

Use these constraints to programmatically define your layout using Auto Layout. All sizes are measured in points. In addition to providing size-specific methods for creating constraints, this class adds type information to the methods inherited from [NSLayoutAnchor](nslayoutanchor.md). Specifically, the generic methods declared by [NSLayoutAnchor](nslayoutanchor.md) must now take a matching [NSLayoutDimension](nslayoutdimension.md) object.

**Swift**

```swift
// This code works as expected.
saveButton.widthAnchor.constraint(equalTo: cancelButton.widthAnchor).isActive = true

// This code generates an incompatible pointer type warning.
saveButton.widthAnchor.constraint(equalTo: cancelButton.leadingAnchor).isActive = true
```

**Objective-C**

```objc
// This code works as expected.
[self.saveButton.widthAnchor constraintEqualToAnchor:self.cancelButton.widthAnchor].active = YES;
 
// This code generates an incompatible pointer type warning.
[self.saveButton.widthAnchor constraintEqualToAnchor:self.cancelButton.leadingAnchor].active = YES;
```

For more information on using layout anchors, see [NSLayoutAnchor](nslayoutanchor.md).

## Relationships

- **Inherits From**: [NSLayoutAnchor](nslayoutanchor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Building constraints

- [- constraintEqualToAnchor:multiplier:](<nslayoutdimension/constraint(equalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as equal to the specified anchor multiplied by the constant.
- [- constraintEqualToAnchor:multiplier:constant:](<nslayoutdimension/constraint(equalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as equal to the specified size attribute multiplied by a constant plus an offset.
- [- constraintEqualToConstant:](<nslayoutdimension/constraint(equaltoconstant_).md>) — Returns a constraint that defines a constant size for the anchor’s size attribute.
- [- constraintGreaterThanOrEqualToAnchor:multiplier:](<nslayoutdimension/constraint(greaterthanorequalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant.
- [- constraintGreaterThanOrEqualToAnchor:multiplier:constant:](<nslayoutdimension/constraint(greaterthanorequalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [- constraintGreaterThanOrEqualToConstant:](<nslayoutdimension/constraint(greaterthanorequaltoconstant_).md>) — Returns a constraint that defines the minimum size for the anchor’s size attribute.
- [- constraintLessThanOrEqualToAnchor:multiplier:](<nslayoutdimension/constraint(lessthanorequalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as less than or equal to the specified anchor multiplied by the constant.
- [- constraintLessThanOrEqualToAnchor:multiplier:constant:](<nslayoutdimension/constraint(lessthanorequalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [- constraintLessThanOrEqualToConstant:](<nslayoutdimension/constraint(lessthanorequaltoconstant_).md>) — Returns a constraint that defines the maximum size for the anchor’s size attribute.

## See Also

### Layout guides

- [UILayoutGuide](uilayoutguide.md) — A rectangular area that can interact with Auto Layout.

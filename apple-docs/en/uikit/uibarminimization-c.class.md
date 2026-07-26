---
title: UIBarMinimization
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uibarminimization-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uibarminimization-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarminimization-c.class.json'
content_hash: 'sha256:62ed34c2ab854091'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBarMinimization

<sub>Class</sub>

A configuration that controls how a navigation bar minimizes in response to scrolling.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIBarMinimization : NSObject
```

## Overview

Access this configuration through `UINavigationItem/navigationBarMinimization` and set its properties to customize minimization.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Instance Properties

- [minimizationBehavior](uibarminimization-c.class/minimizationbehavior.md) — The minimization behavior. _(beta)_
- [restorationBehavior](uibarminimization-c.class/restorationbehavior.md) — The restoration behavior. _(beta)_
- [safeAreaAdjustment](uibarminimization-c.class/safeareaadjustment.md) — The safe area adjustment during minimization. _(beta)_

---
title: UICornerConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicornerconfiguration-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uicornerconfiguration-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerconfiguration-c.class.json'
content_hash: 'sha256:bd07a996f3c03b8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICornerConfiguration

<sub>Class</sub>

A configuration that defines how corner radii are mapped to the corners of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UICornerConfiguration : NSObject
```

## Overview

Create a `UICornerConfiguration` that expresses how you want the corners of your view to appear. Your configuration can apply to corners independently or uniformly, and can form the following types of corners:

- A squared corner
- A rounded corner
- A rounded corner that’s concentric relative to the containing view
- Corners that are rounded to form a capsule

Select a method to create a configuration that describes which corners of your view you want to be uniform and which corners you want to be independent, then provide instances of [UICornerRadius](uicornerradius-c.class.md) as parameters to indicate which type you want each corner to be.

The system uses squared corners by default, so you don’t need to set a configuration to get squared corners.

### Configure a rounded corner

To configure a rounded corner with a fixed radius, provide [fixedRadius:](uicornerradius-c.class/fixedradius_.md) with a value greater than zero for the radius:

```objc
[myView setCornerConfiguration:
 [UICornerConfiguration configurationWithRadius:
  [UICornerRadius fixedRadius:12.0]]];
```

### Configure a concentric rounded corner

To configure a rounded corner that’s concentric relative to the containing view, use [containerConcentricRadius](uicornerradius-c.class/containerconcentricradius.md):

```objc
[myView setCornerConfiguration:
 [UICornerConfiguration configurationWithRadius:
  [UICornerRadius containerConcentricRadius]]];
```

Use [containerConcentricRadiusWithMinimum:](uicornerradius-c.class/containerconcentricradiuswithminimum_.md) to indicate a minimum radius for the rounded corner.

### Configure a corner as a capsule

To configure rounded corners that form a capsule, use [capsuleConfiguration](uicornerconfiguration-c.class/capsuleconfiguration.md):

```objc
[myView setCornerConfiguration:
 [UICornerConfiguration capsuleConfiguration]];
```

Use [capsuleConfigurationWithMaximumRadius:](uicornerconfiguration-c.class/capsuleconfigurationwithmaximumradius_.md) to allow your view to break the capsule paradigm and stretch vertically with an edge if the radius necessary to form a capsule exceeds what you provide.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Configuring independent corners

- [configurationWithRadius:](uicornerconfiguration-c.class/configurationwithradius_.md) — A configuration that applies the given radius independently to all corners.
- [configurationWithTopLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:](uicornerconfiguration-c.class/configurationwithtopleftradius_toprightradius_bottomleftradius_bottomrightradius_.md) — A configuration with independent radii for each corner.

### Configuring corners as a capsule

- [capsuleConfiguration](uicornerconfiguration-c.class/capsuleconfiguration.md) — A configuration that rounds the corners into a capsule shape, scaling with the view’s size.
- [capsuleConfigurationWithMaximumRadius:](uicornerconfiguration-c.class/capsuleconfigurationwithmaximumradius_.md) — A configuration that rounds the corners into a capsule shape, scaling with the view’s size and clamped to the `maximumRadius`.

### Configuring uniform corners

- [configurationWithUniformRadius:](uicornerconfiguration-c.class/configurationwithuniformradius_.md) — A configuration that applies the given radius uniformly to all corners.
- [configurationWithUniformLeftRadius:uniformRightRadius:](uicornerconfiguration-c.class/configurationwithuniformleftradius_uniformrightradius_.md) — A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, and the `rightRadius` uniformly to the top-right and bottom-right corners.
- [configurationWithUniformTopRadius:uniformBottomRadius:](uicornerconfiguration-c.class/configurationwithuniformtopradius_uniformbottomradius_.md) — A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, and the `bottomRadius` uniformly to the bottom-left and bottom-right corners.
- [configurationWithUniformBottomRadius:topLeftRadius:topRightRadius:](uicornerconfiguration-c.class/configurationwithuniformbottomradius_topleftradius_toprightradius_.md) — A configuration that applies the `bottomRadius` uniformly to the bottom-left and bottom-right corners, with optional independent radii for the top-left and top-right corners.
- [configurationWithUniformLeftRadius:topRightRadius:bottomRightRadius:](uicornerconfiguration-c.class/configurationwithuniformleftradius_toprightradius_bottomrightradius_.md) — A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, with optional independent radii for the top-right and bottom-right corners.
- [configurationWithUniformRightRadius:topLeftRadius:bottomLeftRadius:](uicornerconfiguration-c.class/configurationwithuniformrightradius_topleftradius_bottomleftradius_.md) — A configuration that applies the `rightRadius` uniformly to the top-right and bottom-right corners, with optional independent radii for the top-left and bottom-left corners.
- [configurationWithUniformTopRadius:bottomLeftRadius:bottomRightRadius:](uicornerconfiguration-c.class/configurationwithuniformtopradius_bottomleftradius_bottomrightradius_.md) — A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, with optional independent radii for the bottom-left and bottom-right corners.

## See Also

### Configuring a view’s corners

- [cornerConfiguration](uiview/cornerconfiguration-3m8ya.md) — A configuration that defines the corners of the view.
- [UICornerRadius](uicornerradius-c.class.md) — A type that represents the radius the system uses to round a corner.
- [- effectiveRadiusForCorner:](<uiview/effectiveradius(corner_).md>) — Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.

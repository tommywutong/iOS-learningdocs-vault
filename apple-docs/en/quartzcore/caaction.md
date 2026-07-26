---
title: CAAction
framework: Core Animation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caaction
source_url: 'https://developer.apple.com/documentation/quartzcore/caaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caaction.json'
content_hash: 'sha256:0c186c513b4e103e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAAction

<sub>Protocol</sub>

An interface that allows instances to respond to actions triggered by a Core Animation layer change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CAAction
```

## Overview

When queried with an action identifier (a key path, an external action name, or a predefined action identifier) a layer returns the appropriate action object–which must implement the [CAAction](caaction.md) protocol–and sends it a [- runActionForKey:object:arguments:](<caaction/run(forkey_object_arguments_).md>) message.

## Relationships

- **Conforming Types**: [CAAnimation](caanimation.md), [CAAnimationGroup](caanimationgroup.md), [CABasicAnimation](cabasicanimation.md), [CAKeyframeAnimation](cakeyframeanimation.md), [CAPropertyAnimation](capropertyanimation.md), [CASpringAnimation](caspringanimation.md), [CATransition](catransition.md)

## Topics

### Responding to an action

- [- runActionForKey:object:arguments:](<caaction/run(forkey_object_arguments_).md>) — Called to trigger the action specified by the identifier.

## See Also

### Layer Basics

- [CALayer](calayer.md) — An object that manages image-based content and allows you to perform animations on that content.
- [CALayerDelegate](calayerdelegate.md) — Methods your app can implement to respond to layer-related events.
- [CAConstraint](caconstraint.md) — A representation of a single layout constraint between two layers.
- [CALayoutManager](calayoutmanager.md) — Methods that allow an object to manage the layout of a layer and its sublayers.
- [CAConstraintLayoutManager](caconstraintlayoutmanager.md) — An object that provides a constraint-based layout manager.

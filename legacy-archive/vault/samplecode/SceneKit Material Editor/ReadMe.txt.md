---
title: SceneKit Material Editor
apple_id: DTS40012570
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2012-07-31'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitMaterialEditor/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:23:10.917571Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit Material Editor](Scene%20Kit%20Material%20Editor.md)


[Next](SceneKitMaterialEditor-ASCAppDelegate.h.md)[Previous](Scene%20Kit%20Material%20Editor.md)

# ReadMe.txt

```
### Scene Kit Material Editor ###

===========================================================================
DESCRIPTION:

Demonstrates the capabilities of Scene Kit materials. The user interface allows to tweak many SCNMaterial and SCNMaterialProperty properties and offers a live preview on several built-in geometries.

===========================================================================
PACKAGING LIST:

AppDelegate.h/m
This is the main controller for the application and handles the setup of the view and the creation of a scene. It declares properties for Cocoa Bindings extensively used in MainMenu.xib to display rich information about a node's geometry and its materials. An instance of this class resides in MainMenu.xib and uses an IBOutlet reference for the view (which has been wired up through Interface Builder). 

ASCView.h/m
A subclass of SCNView that handles mouse events to rotate a specific node only.

ASCValueTransformers.h/m
Declare and implement value transformers needed in the user interface for bindings.

===========================================================================
Copyright (C) 2012 Apple Inc. All rights reserved.
```

[Next](SceneKitMaterialEditor-ASCAppDelegate.h.md)[Previous](Scene%20Kit%20Material%20Editor.md)


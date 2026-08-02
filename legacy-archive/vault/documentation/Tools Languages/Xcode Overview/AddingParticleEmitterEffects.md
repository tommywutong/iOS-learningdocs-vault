---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/AddingParticleEmitterEffects.html
archived_at: '2026-07-27T06:57:08.063680Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](Adding3DScenes.md)[Previous](AddingImages.md)

## Adding Particle Emitter Effects

Especially useful for developers of iOS and Mac games, Sprite Kit provides a graphics rendering and animation infrastructure. This infrastructure includes particle emitters. Particle emitters can range from a single image that barely moves, to thousands of small particles flying across the screen. You can use particle emitters to simulate fire, rain, smoke, snow, sparks, and other animated effects.

Xcode provides eight particle emitter templates and an editor for manipulating the appearance and behavior of particles.

Create a Sprite Kit–enabled game from the New Project template in Xcode, or use the General pane in the project editor to add the Sprite Kit framework to an existing target. To add a particle emitter to your project, choose File > New > File, and then choose Resource > SpriteKit Particle File.

（原归档配图获取待重试：`AddParticleEmitterFile_2x.png`）

Select the particle template from the pop-up menu, and click Next. Enter a name for the emitter in the Save As field. Select the checkbox associated with your project in the Targets area. Xcode creates a file with the extension `.sks`.

Select your particle emitter file in the project navigator, and Xcode opens the file in the particle emitter editor.

（原归档配图获取待重试：`MagicParticles_2x.png`）

Modify the look and feel of the particles with the Particle Emitter inspector (（原归档配图未能恢复：`ParticleEmitterInspector_2x.png`）). For example, you can change the rate at which particles are created, what a particle looks like, and how it acts after it is created. Changes made to the inspector take effect immediately and can be viewed in the editor.

For more detail, see the _[Particle Emitter Editor Guide](../../IDEs/Particle%20Emitter%20Editor%20Guide/About%20the%20Particle%20Emitter%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezteojx)_.

[Adding Images](AddingImages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjqfvjvomi)

[Adding 3D Scenes](Adding3DScenes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjsfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](Adding3DScenes.md)[Previous](AddingImages.md)

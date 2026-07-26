---
title: RealityKit updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/realitykit
source_url: 'https://developer.apple.com/documentation/updates/realitykit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/realitykit.json'
content_hash: 'sha256:f6e9e11ed7412dde'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# RealityKit updates

<sub>Article</sub>

Learn about important changes in RealityKit.

## Overview

Browse notable changes in [RealityKit](../realitykit.md).

## June 2025

### General

- Create hover effect groups to indicate entities that need to highlight together using [HoverEffectComponent.GroupID](../realitykit/hovereffectcomponent/groupid.md).
- Present popovers from volumes using [PresentationComponent](../realitykit/presentationcomponent.md).
- Manually create instances of entities using [MeshInstancesComponent](../realitykit/meshinstancescomponent.md).
- Animate entities implicitly using [animate(_:body:completion:)](<../realitykit/entity/animate(__body_completion_).md>).
- Create and modify attachments in a more streamlined fashion using [ViewAttachmentComponent](../realitykit/viewattachmentcomponent.md).
- Make entities render behind real-world objects based on depth using [EnvironmentBlendingComponent](../realitykit/environmentblendingcomponent.md).
- Implement post-processing effects using [RealityViewPostProcessEffect](../realitykit/realityviewpostprocesseffect.md) and [PostProcessEffectContext](../realitykit/postprocesseffectcontext.md).
- Attach models together using [attach(_:to:)](<../realitykit/entity/attach(__to_).md>).
- [TextureResource](../realitykit/textureresource.md) now supports AVIF textures and entities you load from USDZ files that contain AVIF textures using [init(named:in:)](<../realitykit/entity/init(named_in_).md>)  so they render correctly.
- Load entities from Data objects using [init(from:configurations:)](<../realitykit/entity/init(from_configurations_).md>).

### Image presentation

- Generate spatial scenes using [ImagePresentationComponent.Spatial3DImage](../realitykit/imagepresentationcomponent/spatial3dimage.md) and present them (along with 2D images and spatial photos) using [ImagePresentationComponent](../realitykit/imagepresentationcomponent.md).
- Receive notifications related to presenting images using [ImagePresentationEvents](../realitykit/imagepresentationevents.md).
- Use [Model3DAsset](../realitykit/model3dasset.md) with [Model3D](../realitykit/model3d.md) to play animations in Model3D Views.

### ARKit integration

- Receive updates about ARKit anchors directly in RealityKit using [AnchorStateEvents](../realitykit/anchorstateevents.md) and [SceneEvents.TrackingStateUpdate](../realitykit/sceneevents/trackingstateupdate.md).

### SwiftUI integration

- Use SwiftUI implicit animations using the [Animation](../swiftui/animation.md) modifier with RealityKit entities and components.
- Keep SwiftUI state in sync with RealityKit state using [Entity.Observable](../realitykit/entity/observable-swift.struct.md).
- Present USD variants in [Model3D](../realitykit/model3d.md) using [Entity.ConfigurationCatalog](../realitykit/entity/configurationcatalog.md).
- Specify the frame sizing and alignment option for RealityView using [RealityViewLayoutOption](../realitykit/realityviewlayoutoption.md).

### Video presentation

- Play spatial video, 180°, 360°, wide-FOV APMP video, and Apple Immersive Video in  [VideoPlayerComponent](../realitykit/videoplayercomponent.md).
- Retrieve the loading status when playing video using [VideoPlayerComponent](../realitykit/videoplayercomponent.md) with [currentRenderingStatus](../realitykit/videoplayercomponent/currentrenderingstatus.md).
- Receive notifications when a video stops playing due to a comfort violation using [VideoPlayerEvents.VideoComfortMitigationDidOccur](../realitykit/videoplayerevents/videocomfortmitigationdidoccur.md).

### Gestures and entity interaction

- Implement six degree of freedom (6DOF) gestures for manipulating entities using [ManipulationComponent](../realitykit/manipulationcomponent.md).
- Leverage [GestureComponent](../realitykit/gesturecomponent.md) to support gestures on individual entities.

## June 2024

### General

- Add artistic lights and shadows to your visionOS app with [PointLightComponent](../realitykit/pointlightcomponent.md), [DirectionalLightComponent](../realitykit/directionallightcomponent.md), [SpotLightComponent](../realitykit/spotlightcomponent.md), and [DynamicLightShadowComponent](../realitykit/dynamiclightshadowcomponent.md).
- Manage spatial tracking in your app with the [SpatialTrackingSession](../realitykit/spatialtrackingsession.md).
- Use [LowLevelMesh](../realitykit/lowlevelmesh.md) to efficiently bring your mesh data to RealityKit, including custom vertex attributes, formats, and layouts.
- Use an [AnimationLibraryComponent](../realitykit/animationlibrarycomponent.md) to store associated animations with an entity that plays the animations.
- Create an  [IKComponent](../realitykit/ikcomponent.md) to animate a skeletal model with an inverse kinematics [IKComponent.Solver](../realitykit/ikcomponent/solver.md).
- Use an [AudioLibraryComponent](../realitykit/audiolibrarycomponent.md) to store associated audio with an entity that plays the audio.
- Stream generated audio in real time with [AudioGeneratorController](../realitykit/audiogeneratorcontroller.md).
- Manage the meshes on your blend shapes with [BlendShapeWeightsComponent](../realitykit/blendshapeweightscomponent.md).
- Create more engaging sound effects by configuring rolloff and reverb with the [SpatialAudioComponent](../realitykit/spatialaudiocomponent.md).
- Customize hover effects when using [HoverEffectComponent](../realitykit/hovereffectcomponent.md), such as spotlight styles, highlight styles, or shader-backed hover effects for additional control over hover behaviors.

### Models and materials

- Optimize material initialization with a [CustomMaterial.Program](../realitykit/custommaterial/program-swift.class.md) to compile backing shaders.
- Use [init(from:)](<../realitykit/textureresource/init(from_).md>) to efficiently update custom texture data in RealityKit, including custom pixel formats, texture types, swizzle, and texture usage.
- Create cube texture resources with [init(cubeFromEquirectangular:named:quality:faceSize:options:)](<../realitykit/textureresource/init(cubefromequirectangular_named_quality_facesize_options_).md>) or [init(cubeFromImage:named:options:)](<../realitykit/textureresource/init(cubefromimage_named_options_).md>).
- Access additional texture resource properties: [arrayLength](../realitykit/textureresource/arraylength.md), [depth](../realitykit/textureresource/depth.md), [pixelFormat](../realitykit/textureresource/pixelformat.md), and [textureType](../realitykit/textureresource/texturetype.md).
- Add a clearcoat to your custom materials with [clearcoatNormal](../realitykit/custommaterial/clearcoatnormal-swift.property.md).

### Physics and simulations

- Apply force effects on rigid bodies with the [ForceEffect](../realitykit/forceeffect.md).
- Create simulations such as hinge and slider joints with [PhysicsJoint](../realitykit/physicsjoint.md).

### Immersive environments

- Anchor dockable videos by attaching a [DockingRegionComponent](../realitykit/dockingregioncomponent.md) to your entity.
- Peer into other immersive worlds with a [PortalComponent](../realitykit/portalcomponent.md), and allow objects from that world to enter yours with [PortalCrossingComponent](../realitykit/portalcrossingcomponent.md).
- Further control the lighting in your environment with [EnvironmentLightingConfigurationComponent](../realitykit/environmentlightingconfigurationcomponent.md).

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.

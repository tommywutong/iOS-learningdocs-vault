---
title: Motion XML File Format
apple_id: TP40007455
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2010-06-24'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/motion_XML_guide/ObjectParm/ObjectParm.html
archived_at: '2026-07-15T05:18:59.610976Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Motion XML File Format](About%20This%20Document.md)


[Next](Channel%20Folders%20and%20Related%20Elements.md)[Previous](The%20Properties%20Parameter.md)

# The Object Parameter

All `scenenode` and `layer` elements contain an `Object` parameter that encodes an object’s unique characteristics. These parameters typically appear in the scene object’s tab in the Inspector and usually labeled “Image,” “Text,” “Behavior,” and so on.

The components of an `Object` parameter are based on a scene object’s `factoryID=` attribute, if present. Thus, you can check the components of an `Object` parameter by using the object’s `factoryID=` to associate the object with a factory. Then make sure the components match the components specified in this chapter.

The scene objects and their `object` parameters listed in this chapter include:

- [layer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltg)
- [mask(Image Mask)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknlti)
- [mask(Shape Mask)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltemi)
- [scenenode(Camera)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltk)
- [scenenode(Light)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltm)
- [scenenode(Clone Layer)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknlto)
- [scenenode(Image Object)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltq)
- [scenenode(Text)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknlts)
- [scenenode(Shape)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcma)
- [scenenode(Generator)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcmi)
- [scenenode(Behavior)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcmq)
- [scenenode(Filter)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcmy)
- [scenenode(Emitter or Replicator)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcna)
- [scenenode(Particle Cell or Replicator Cell)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcni)
- [footage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcnq)
- [clip](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcny)
- [audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcoa)
- [audioTrack](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltcoi)
- [scenenode(Master)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltema)

__**layer**__

**`Object`**
: `Type` (Boolean): 0 if this layer is 2D; 1 if 3D.

****
: `Fixed Resolution` (Boolean): 1 if this layer’s size is specified in fixed resolution; 0 if not.

****
: `Fixed Width` (unsigned integer). The width of this layer; keyframes not supported.

****
: `Fixed Height` (unsigned integer). The height of this layer; keyframes not supported.

****
: `Flatten` (Boolean): 1 if flattened; 0 if not.

****
: `Layer Order` (Boolean): 1 if objects in this layer are sorted by their order in the Layers list; 0 if not.

****
: `Aperture Width`. Used for internal processing; should not be modified.

****
: `Aperture Height`. Used for internal processing: should not be modified.

****
: `Hidden Channel`. Used for internal processing; should not be modified.

__**mask(Image Mask)**__

**`Object`**
: `Mask`–>

****
: `Source Channel` (enumerated): 0: red; 1: green; 2: blue; 3: alpha; 4: luminance.

****
: `Mask Blend Mode` (enumerated): 0: add; 1: subtract; 2: replace; 3: intersect.

****
: `Invert Mask` (Boolean): 1 if enabled; 0 if disabled.

****
: `Stencil` (Boolean): 1 if enabled; 0 if disabled.

****
: `Stretch` (Boolean): 1 if enabled; 0 if disabled.

__**mask(Shape Mask)**__

**`Object`**
: `Shape Animation`–>.

****
: `Shape Type` (enumerated): 0: linear;1: bezier; 2: B-spline.

****
: `Closed` (Boolean): 1 if this mask represents a closed curve; 0 if not.

****
: `Roundness` (float). The roundness the corners of this shape mask.

****
: `Preserve Scale`  (Boolean): 1 if the roundness of this shape mask is scaled by the mask’s scale, 0 if not.

****
: `Preserve Scale` (Boolean): 1 if the roundness of this shape mask is scaled by the mask’s scale; 0 if not.

****
: `Initial Position`. Used for internal processing; should not be modified.

****
: `Fill`–>

****
: `Outline`–>

****
: `Feather` (float). The number of pixels to feather this mask.

****
: `Mask Blend Mode` (enumerated): 0: add; 1: subtract; 2: replace; 3: intersect.

****
: `Invert Mask` (Boolean): 0 if disabled; 1 if enabled

****
: `Initial Scale X`. Used for internal processing; should not be modified.

****
: `Initial Scale Y`. Used for internal processing; should not be modified.

****
: `Use Old B-Spline Model`. Used for internal processing; should not be modified.

****
: `Use Old Antialiasing Method`. Used internally by Motion; should not be modified.

****
: `Mask Color` (enumerated): 0: Red; 1: Green; 2: Blue; 3: Purple; 4: Orange; 5: Magenta; 6: Yellow; 7: Cyan.

__**scenenode(Camera)**__

**`Object`**
: `Camera Type` (enumerated): 0: view point; 1: framing.

****
: `Angle of View` (angle): angle of view, in degrees.

****
: `Near Plane` (float). The position of the near plane for this Camera.

****
: `Far Plane` (float). The position of the far plane for this Camera relative to the Near Plane.

****
: `Near Fade` (float). The offset from the near plane at which fading begins.

****
: `Far Fade` (float). The offset from the far plane at which fading begins.

****
: `Depth of Field`->

__**scenenode(Light)**__

**`Object`**
: `Light Type` (enumerated): 0: ambient; 1: directional; 2: point; 3: spot.

****
: `Color`–>

****
: `Intensity` (float). The intensity of this light.

****
: `Falloff Start` (float). The distance from the center of the light where intensity begins to fall off.

****
: `Falloff` (float). The amount of change in intensity.

****
: `Spot Options`–>

****
: `Shadows`->

__**scenenode(Clone Layer)**__

**`Object`**
: `Clone Layer`–>

__**scenenode(Image Object)**__

**`Object`**
: `Drop Zone` (Boolean): 1 if this scene node serves as a drop zone; 0 if not.

****
: `Fit` (enumerated): 0: fit; 1: center; 2: stretch.

****
: `Replaced`. Used for internal processing; should not be modified.

****
: `Fit Factor`. Used for internal processing; should not be modified.

****
: `Clear`. Used for internal processing; should not be modified.

****
: `Width`. Used for internal processing; should not be modified.

****
: `Height`. Used for internal processing; should not be modified.

__**scenenode(Text)**__

**`Object`**
: `Opacity` (float). Used internally by Motion; should not be modified.

****
: `Tracking` (float). The tracking value for this text object.

****
: `Flatten` (Boolean): 1 if flattened; 0 if not.

****
: `Render Text` (enumerated): 0: In Global 3D; 1: In Local 3D.

****
: `Face Camera` (Boolean): 1 if glyphs always face the camera, 0 if not.

****
: `Layout Method` (enumerated): 0: type; 1: paragraph; 2: path.

****
: `Direction`. Used internally by Motion; should not be modified.

****
: `Alignment` (enumerated): 0: left; 1: center; 2: right.

****
: `Justification` (enumerated): 0: none; 1: partial; 2: full.

****
: `Line Spacing` (float). The line spacing for this text object.

****
: `Anchor Point` (enumerated) : 0: Character; 1: Word; 2: Line; 3: All. The basis for the anchor point position for text sequence animation.

****
: `Position` –>. The position of the anchor point for text sequence animation.

****
: `Type On` –>. The Type On settings for this text object.

****
: `Left Margin` (float). The position of the left margin relative to the Position of the text layout.

****
: `Right Margin` (float). The position of the right margin relative to the Position of the text layout.

****
: `Top Margin` (float). The position of the top margin, relative to the Position of the text layout.

****
: `Bottom Margin` (float). The position of the bottom margin, relative to the Position of the text layout.

****
: `Path Options`–>

****
: `Publish to FCP` (Boolean): 0 if disabled, 1 if enabled.

****
: `Scale` ->

__**scenenode(Shape)**__

**`Object`**
: `Shape Animation`–>

****
: `Shape Type` (enumerated): 0: linear; 1: bezier. 2: B-spline.

****
: `Closed` (Boolean): 1 if this shape represents a closed curve; 0 if not.

****
: `Roundness` (float). The roundness of the corners of this shape.

****
: `Preserve Scale` (Boolean): 1 if the roundness of this shape is scaled by the shape’s scale; 0 if not.

****
: `Initial Position`. Used for internal processing; should not be modified.

****
: `Fill`–>

****
: `Outline`–>

****
: `Feather`–>

****
: `Mask Blend Mode` (enumerated): 0: add. 1: subtract. 2: replace. 3: intersect.

****
: `Invert Mask` (Boolean): 1 if masking area is inverted; 0 if not.

****
: `Initial Scale X`. Used for internal processing; should not be modified.

****
: `Initial Scale Y`. Used for internal processing; should not be modified.

****
: `Use Old B-Spline Model`. Used for internal processing; should not be modified.

****
: `Use Old Antialiasing Method`. Used internally by Motion; should not be modified.

****
: `Mask Color` (enumerated): 0: Red; 1: Green; 2: Blue; 3: Purple; 4: Orange; 5: Magenta; 6: Yellow; 7: Cyan.

__**scenenode(Generator)**__

**`Object`**
: Components of the `object` parameter depend on the particular generator selected. Refer to the Motion UI for details.

__**scenenode(Behavior)**__

**`Object`**
: Components of the `object` parameter depend on the particular behavior selected. Refer to the Motion UI for details.

__**scenenode(Filter)**__

**`Object`**
: Components of the `object` parameter depend on the particular filter selected. Refer to the Motion UI for details.

__**scenenode(Emitter or Replicator)**__

**`Object`**
: `Shape Parameters`–>

****
: `Emission Angle` (angle): the emission angle, in radians; present only for 2D.

****
: `Emission Latitude` (angle): the emission latitude, in radians; present only for 3D.

****
: `Emission Longitude` (angle): the emission longitude, in radians.

****
: `Emission Range` (angle): the emission range, in radians.

****
: `Master Controls`–>

****
: `Tint Color`. Used for internal processing; should not be modified.

****
: `Tint Amount`. Used for internal processing; should not be modified.

****
: `Render Order` (enumerated): used for emitter scenenodes only. 0: oldest first; 1: oldest last.

****
: `Reverse Stacking` (Boolean): 0 if disabled; 1 if enabled. Used for replicator scenenodes only.

****
: `Interleave Particles` (Boolean): 0 if disabled; 1 if enabled. Used for emitter scenenodes only.

****
: `Fill Points`. Used for internal processing; should not be modified.

****
: `Emitter Seed` (unsigned integer). random seed for Shuffle Order parameter. Present only for emitter `scenenodes`.

****
: `Replicate Seed` (unsigned integer). Random seed for Shuffle Order parameter. Present only for replicator `scenenodes`.

****
: `Uniform Distribution`: this parameter is used internally by Motion and should not be changed.

****
: `Preview Position`. Used for internal processing; should not be modified.

****
: `3D` (Boolean): 1 if emitter cells are to be distributed in 3D; 0 if not.

****
: `Render Particles` (enumerated): 0: in global 3D; 1: in local 3D.

****
: `Face Camera` (Boolean): 1 if all cells should face the camera, 0 if not.

****
: `Depth Ordered` (Boolean): 1 if all cells should be drawn from back to front, 0 if drawn in order of emission.

__**scenenode(Particle Cell or Replicator Cell)**__

**Note**
: A particle cell or a replicator cell can represent an individual cell for these scene objects: `Replicator`, `Emitter`, `Paint Stroke`, `Shape`.

**`Object`**
: `Birth Rate` (float). The birth rate for this cell. Used when the parent `scenenode` is an emitter.

****
: `Birth Rate Randomness` (float). Random variant for the Birth Rate parameter.

****
: `Initial Number` (float). The initial number of particle cells; used when the parent `scenenode` is an emitter.

****
: `Life` (float). The life span of a Particle Cell, in seconds.

****
: `Life Randomness` (float). Random variant for the Life parameter.

****
: `Speed` (float). The speed for this cell.

****
: `Speed Randomness` (float). Random variant for the Speed parameter.

****
: `Align Angle` (Boolean): 1 if cells should rotate based on their position on the shape of the replicator; 0 if not. Present only when the parent `scenenode` is a Motion replicator or emitter.

****
: `Brush Align Angle` (Boolean): 1 if cells should rotate based on their position on the length of a paint stroke or shape edge; 0 if not. Present only when the `parent` scenenode is a Motion paint stroke or shape.

****
: `Angle`–>. Present only when the parent `scenenode` is a Motion replicator or emitter.

****
: `Brush Angle`–>. Present only when parent scenenode is a Motion paint stroke or shape.

****
: `Angle End`. This parameter is used for backwards compatibility purposes and should not be modified.

****
: `Angle Over Stroke` (angle). Describes the angle modulation over the length of a paint stroke. Used when the grandparent `scenenode` represents a Motion paint stroke or shape. Must be represented as a curve.

****
: `Angle Randomness`–>. Present only when the parent `scenenode` is a Motion replicator or emitter.

****
: `Brush Angle Randomness`–>. Present only when the parent `scenenode` is a Motion paint stroke or shape.

****
: `Spin` (angle). Amount to spin each cell, in radians.

****
: `Spin Randomness` (angle). Random variant for the Spin parameter.

****
: `Color Mode` (enumerated): 0: original; 1: colorize; 2: over life; 3: pick from color range; 4: take image color.

****
: `Color`–>: used only when Color Mode is Colorize.

****
: `Opacity Over Life`–>. Used when Color Mode is Original or Colorize.

****
: `Color Gradient`–>. Present when Color Mode is Over Pattern and the parent `scenenode` is a replicator.

****
: `Opacity Gradient`–>> Present when Color Mode is Original or Colorize and the parent `scenenode` is a replicator.

****
: `Color Over Life`–>. Present when Color Mode is Over Life.

****
: `Color Range`–>. Present when Color Mode is Pick From Color Range.

****
: `Random Color`> This parameter is used for backward compatibility purposes and should not be modified.

****
: `Color Repetitions` (float). The number of repetitions to choose color. Used only when Color Mode is Over Life.

****
: `Take Image Color`. This parameter is used for backward compatibility purposes and should not be modified.

****
: `Scale`–>

****
: `Scale End`–>

****
: `Scale Randomness`–>

****
: `Premultiplied`. Used for internal processing; should not be modified.

****
: `Additive Blend` (Boolean): 0 if disabled; 1 if enabled.

****
: `Play Frames` (Boolean): 0 if disabled; 1 if enabled.

****
: `Random Start Frame` (Boolean): 0 if disabled; 1 if enabled.

****
: `Source Start Frame` (frame). The frame at which the source media begins. Used when the source is a video clip; not used if the Random Start Frame parameter is enabled.

****
: `Source Frame Offset` (frame). The offset to apply to the Source Start Frame parameter to each replicator cell. Used when the source is a video clip and the grandparent `scenenode` is a replicator.

****
: `Source Start Frame Over Stroke` (frame): the frame to use from the source footage over the length of a paint stroke. Applicable when the grandparent `scenenode` is a paint stroke. Must be represented as a curve.

****
: `Hold Frames` (unsigned integer). The number of frames to hold each frame of source media. Used when the source is a video clip; not used if the Play Frames parameter is disabled.

****
: `Hold Frames Randomness` (unsigned integer). Random variant for the Hold Frames parameter.

****
: `Attach To Emitter` (Boolean): 0 if disabled; 1 if enabled.

****
: `Show Particles As` (enumerated): 0: points; 1: lines; 2: wireframe; 3: image.

****
: `Random Seed` (unsigned integer). Random seed.

****
: `Point Size` (float). The point size. Used when the Show Particles As parameter is set to points.

****
: `Dynamics`. Used for internal processing; should not be modified.

****
: `Spacing` (float). The spacing across particles. Used when the grandparent `scenenode` is a paint stroke.

****
: `Spacing Over Stroke` (float). The spacing curve across the length of a paint stroke. Used only when grandparent `scenenode` is a paint stroke. Must be represented as a curve.

****
: `Width Over Stroke` (float). The width curve across the length of a paint stroke or shape edge. Used only when the grandparent `scenenode` is a Motion paint stroke or shape. Must be represented as a curve.

****
: `Fixed Brush Dabs` (Boolean): 0 if disabled; 1 if enabled. Only used by Paint Strokes.

****
: `Anchor Dabs To` (enumerated): used when parameter Fixed Brush Dabs is disabled. 0: start; 1: start and end.

****
: `Pos Offset`. Used for internal processing; should not be modified.

****
: `Jitter`–>: the jitter amount to apply to each cell. Used when the grandparent `scenenode` is a paint stroke or shape.

****
: `Jitter Over Stroke`–>: the jitter amount to apply to each cell over the length of a paint stroke or shape edge. Used when the grandparent `scenenode` is a Motion paint stroke or shape.

****
: `Particle Source` (id): the id of the media this cell incorporates as its source. Present only when the parent `scenenode` is a Motion emitter or replicator.

****
: `Brush Source` (id): the id of the media this cell incorporates as its source. Present only when the grandparent `scenenode` is a Motion paint stroke or shape.

****
: `Object Source` (id): the id of the media that this cell incorporates as its source. Present only when the parent `scenenode` is a Motion replicator or emitter.

****
: `Hidden channel`. Used for internal processing; should not be modified.

****
: `Obsolete Rotation`. a parameter used for backward compatibility that should not be modified.

****
: `Obsolete Rotation End`. A parameter used for backward compatibility; should not be modified.

****
: `Obsolete Rotation Variance`. A parameter used for backward compatibility; should not be modified.

****
: `Brush Profile`–>. Present only when the grandparent `scenenode` is a Motion paint stroke or shape.

****
: `Hidden Opacity Over Stroke`. This parameter is used internally by Motion and should not be modified. Present only when the grandparent `scenenode` is a Motion paint stroke or shape.

__**footage**__

**`Object`**
: The `Object` parameter for the `footage` element has no subelements.

__**clip**__

**`Object`**
: `Alpha Type`–>

****
: `Invert Alpha` (Boolean): 1 if enabled; 0 if disabled.

****
: `Pixel Aspect Ratio` (float). The pixel aspect ratio for this video clip. No keyframing support.

****
: `Field Order` (enumerated): 0: none; 1: Upper (odd); 2: Lower (even).

****
: `3:2 Pulldown` (enumerated): 0: off; 1: SSWWW; 2: WSSWW; 3: WWSSW; 4: WWWSS; 5: SWWWS.

****
: `Frame Rate` (float). The frame rate for this clip. No keyframing support.

****
: `Fixed Resolution` (Boolean): 1 if the PDF file is displayed at fixed resolution; 0 if not.

****
: `Fixed Width` (unsigned integer). The width of this PDF file. No keyframing support.

****
: `Fixed Height` (unsigned integer). The height of this PDF file. No keyframing support.

****
: `Use Background Color` (Boolean): 0 if disabled; 1 if enabled.

****
: `Background Color`–>

****
: `Crop`–>

****
: `Replace Media File`. Used for internal processing; should not be modified.

****
: `OpenEXR`–>

****
: `Gamma` (float). The gamma value for this clip.

__**audio**__

**`Object`**
: The `Object` parameter for the `audio` element has no subelements.

__**audioTrack**__

**`Object`**
: `Amplitude Mix`. Used for internal processing; should not be modified.

****
: `Amplitude Left`. Used for internal processing; should not be modified.

****
: `Amplitude Right`. Used for internal processing; should not be modified.

****
: `Peak Mix`. Used for internal processing; should not be modified.

****
: `Peak Left`. Used for internal processing; should not be modified.

****
: `Peak Right`. Used for internal processing; should not be modified.

****
: `Track ID`: this value is used internally by Motion and should not be modified.

****
: `Channel ID`: this value is used internally by Motion and should not be modified.

****
: `Channels Layout` (enumerated): 0: mixed; 1: discrete; 2: single channel

****
: `Mute` (Boolean): 1 if muted; 0 if not.

****
: `Solo` (Boolean): 1 if this track is soloed; 0 if not.

****
: `Level` (float). The level of this audio track, adjustable between 0.0 and 2.0, inclusive.

****
: `Pan` (float). The pan position of this audio track.

****
: `Output Bus` (enumerated): 0: stereo; 1: left; 2: right; 3: center; 4: LFE; 5: left surround; 6: right surround.

__**scenenode(Master)**__

**`Object`**
: `Amplitude Mix`. Used for internal processing; should not be modified.

****
: `Amplitude Left`. Used for internal processing; should not be modified.

****
: `Amplitude Right`. Used for internal processing; should not be modified.

****
: `Peak Mix`. Used for internal processing; should not be modified.

****
: `Peak Left`. Used for internal processing; should not be modified.

****
: `Peak Right`. Used for internal processing; should not be modified.

****
: `Mute` (Boolean): 1 if muted; 0 if not.

****
: `Level` (float). The level of this audio track, adjustable between 0.0 and 2.0, inclusive.

****
: `Pan` (float). The pan position of this audio track.

****
: `Output Layout` (enumerated): 0: stereo; 1: 5.1 Surround.

[Next](Channel%20Folders%20and%20Related%20Elements.md)[Previous](The%20Properties%20Parameter.md)


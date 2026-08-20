---
title: Motion XML File Format
apple_id: TP40007455
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2010-06-24'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/motion_XML_guide/PropertiesParm/PropertiesParm.html
archived_at: '2026-07-15T05:19:00.687467Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Motion XML File Format](About%20This%20Document.md)


[Next](The%20Object%20Parameter.md)[Previous](Elements%2C%20Subelements%2C%20and%20Attributes.md)

# The Properties Parameter

The `Properties` parameter described in this chapter corresponds to the Properties tab in the Inspector. It encodes basic properties such as an object’s transform, blending and drop shadow.

The exact components of a `Properties` parameter vary depending on the scene object the parameter is describing.

The following scene objects have a structurally identical `Properties` parameter:

- `mask(Shape)`.
- `scenenode(Emitter).`
- `scenenode(Generator).`
- `scenenode(Replicator).`
- `scenenode(Shape Mask)`.
- `scenenode(Text)`.

Other `Properties` parameters for other scene objects are described below. (See [Other Properties Parameters](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnznknltg).)

__**Transform**__

**Description**
: A scene object’s transformation parameters.

**Attributes**
: `id=`, `flags=`

**Subelements**
: `foldFlags`

****
: `Position`–>. A scene object’s position in world space.

****
: `Rotation`–>. A scene object’s rotation.

****
: `Scale`–>. A scene object’s scale properties.

****
: `Shear`–>. A scene object’s shearing properties.

****
: `Anchor Point`–>. A scene object’s anchor point position.

****
: `Rotation`. A legacy parameter used for backwards compatibility purposes; should not be modified.

**Note**
: For details about these subelements, see [Transform Channels](Channel%20Folders%20and%20Related%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknlte).

__**Blending**__

**Description**
: A scene object’s blending parameters.

**Attributes**
: `id=`, `flags=`

**Subelements**
: `foldFlags`

****
: `Opacity` (percent): the opacity of a scene object.

****
: `Blend Mode` (enumerated). The type of blending used for a scene object. Valid values are: 0: normal; 2: subtract; 3: darken; 4: multiply; 5: color burn; 6: linear burn; 8: add; 9: lighten; 10: screen; 11: color dodge; 12: linear dodge; 14: overlay; 15: soft light; 16: hard light; 17: vivid light; 18: linear light; 19: pin light; 20: hard mix; 22: difference; 23: exclusion; 25: stencil alpha; 26: stencil luma; 27: silhouette alpha; 28: silhouette luma; 29: behind; 31: alpha add; 32: premultiplied mix.

****
: `Preserve Opacity` (Boolean): 0 if disabled; 1 if enabled.

****
: `Casts Reflection` (enumerated): 0: Yes; 1: No; 2: Reflection Only. The reflection setting for a scene object.

__**Lighting**__

**Description**
: A scene object’s lighting parameters.

**Attributes**
: `id=`, `flags=`

**Subelements**
: `foldFlags`

****
: `Shading` (enumerated) : 0: inherited; 1: on; 2: off.

****
: `Highlights`: a parameter used internally by Motion; should not be modified.

__**Shadows**__

**Description**
: A scene object’s shadows parameters. (A Light also has a [Shadows](Channel%20Folders%20and%20Related%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkoa) channel folder.)

**Attributes**
: `id=`, `flags=`

**Subelements**
: `foldFlags`

****
: `Cast Shadows` (Boolean) : 0 if disabled; 1 if enabled.

****
: `Receive Shadows` (Boolean) : 0 if disabled; 1 if enabled.

****
: `Shadows Only` (Boolean) : 0 if disabled; 1 if enabled.

__**Reflection**__

**Description**
: A scene object’s reflection parameters.

**Attributes**
: `id=`, `flags=`

**Subelements**
: `foldFlags`

****
: `Reflectivity` (percent). The reflectivity of a scene object’s surface.

****
: `Blur Amount` (float). The amount of blur of reflected images on a scene object.

****
: `Falloff` ->

****
: `Blend Mode`(enumerated). The type of blending used for a scene object. Valid values are: 0: normal; 2: subtract; 3: darken; 4: multiply; 5: color burn; 6: linear burn; 8: add; 9: lighten; 10: screen; 11: color dodge; 12: linear dodge; 14: overlay; 15: soft light; 16: hard light; 17: vivid light; 18: linear light; 19: pin light; 20: hard mix; 22: difference; 23: exclusion; 25: stencil alpha; 26: stencil luma; 27: silhouette alpha; 28: silhouette luma; 29: behind; 31: alpha add; 32: premultiplied mix.

__**Drop Shadow**__

**Description**
: A scene object’s drop shadow parameters.

**Attributes**
: `id=`, `flags=`

**Subelements**
: `foldFlags`

****
: `Color`–>

****
: `Opacity` (percent). The opacity value for this scene object’s drop shadow.

****
: `Blur` (float). The amount of blur to apply to a scene object’s drop shadow.

****
: `Distance` (float). The offset to apply to this scene object’s drop shadow.

****
: `Angle` (angle). The angle at which to apply this scene object's drop shadow, in radians.

****
: `Fixed Source` (Boolean): 0 if disabled, 1 if enable.

__**Four Corner**__

**Description**
: A scene object’s four-corner transform parameters.

**Attributes**
: `id=`, `flags=`

**Subelements**
: `foldFlags`

****
: `Bottom Left`–>

****
: `Bottom Right`–>

****
: `Top Right`–>

****
: `Top Left`–>

__**Crop**__

**Description**
:  Encodes a scene object's cropping parameters.

**Attributes**
: `id=`, `flags=`

**Subelements**
: `foldFlags`

****
: `Left` (float). The left cropping position.

****
: `Right` (float). The right cropping position.

****
: `Bottom` (float). The bottom cropping position.

****
: `Top` (float). The top cropping position.

__**Timing**__

**Description**
: A parameter used internally by Motion; should not be modified.

The structure of the `Properties` parameter for other scene objects varies according to the object.

__**scenenode(Camera/Light)**__

**`Properties`**
: `Transform` parameters only.

__**scenenode(Image)**__

**`Properties`**
: All parameters listed in [Structurally Identical Properties Parameters](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnznknlte) plus the following:

****
: `Media` (id). The id of the footage node this scene node represents. Keyframes not supported.

****
: `Page Number` (unsigned integer). The page number of the PDF file this scene node represents, if applicable; 0 otherwise.

****
: `Background Color`–>

****
: `Speed` (float). The speed for this movie clip when Constant Speed retiming is used. Keyframes not supported.

****
: `Reverse` (Boolean). Whether or not to play this movie clip in reverse. 1 = true; 0 = false.

****
: `Time Remap` (enumerated). 0: Constant speed retiming; 1: Variable speed retiming.

****
: `Retime Value` (frame). The frame of the movie clip that will be played with respect to the time at each keyframe. Must be represented as a curve. This parameter defaults to a curve with two keypoints, whose `time` elements correspond to the first and last frame of the movie clip (0-based) and whose `value` elements correspond to the first and last frame of the movie clip (1-based).

****
: `Retime Value Cache` (frame). The previously used curve for movie clip retiming. Must be represented as a curve. See `Retime Value`.

****
: `Frame Blending` (enumerated). 0: none; 1: blending; 2: motion-blur blending; 3: optical flow.

****
: `End Condition` (enumerated). 0: none; 1: loop; 2: ping-pong; 3: hold.

****
: `End Duration` (frame). The number of frames to repeat when the `End Condition` is set to Loop. Keyframes not supported.

****
: `Duration Cache` (frame). The previously held value for `End Duration`. Keyframes not supported.

****
: `Layer` (unsigned integer): the index of the layer of the Photoshop file this scene node represents. 0 if not applicable

__**audioTrack**__

**`Properties`**
: `Media` (id): the id of the audio element this audio track represents. No support for keyframing.

****
: `Timing`. A parameter used internally by Motion; should not be modified.

****
: `Retime Value` (frame). The frame of the audio track that will be played with respect to the time at each keyframe. Must be encoded as a `curve`. This parameter defaults to a `curve` with two keypoints whose `time` elements correspond to the first and last frame of the audio track (0-based) and whose `value` elements correspond to the first and last frame of the audio track (1-based).

****
: `Retime Value Cache` (frame). The previously used curve for audio track retiming. Must be encoded as a `curve`. See `Retime Value`.

****
: `Speed` (float). The speed for this audio track when Constant Speed retiming is used. Does not support keyframes.

****
: `Time Remap` (enumerated): 0: Constant speed retiming; 1: Variable speed retiming.

****
: `End Condition` (enumerated): 0: None; 1: Loop; 2: Ping-Pong; 3: Hold.

****
: `End Duration` (integer). The number of frames after the end of the audio track to extend the track by the method selected in `End Condition`.

The following scene objects have a Properties parameter with no subelements:

- `clip`
- `footage`
- `scenenode(Image Mask)`
- `scenenode(Master)`
- `scenenode(Particle Cell)`
- `scenenode(Replicator Cell)`

[Next](The%20Object%20Parameter.md)[Previous](Elements%2C%20Subelements%2C%20and%20Attributes.md)


---
title: Motion XML File Format
apple_id: TP40007455
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2010-06-24'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/motion_XML_guide/ChannelParms/ChannelParms.html
archived_at: '2026-07-15T05:18:59.172715Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Motion XML File Format](About%20This%20Document.md)


[Next](Customizing%20a%20Motion%20XML%20Project%20File.md)[Previous](The%20Object%20Parameter.md)

# Channel Folders and Related Elements

This chapter provides details about channel folders and related elements. It includes the following sections:

- Transform Channels
- [Color Channels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknlts)
- [Text Channels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcoa)
- [Shape, Emitter, Replicator Channels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltenq)
- [Footage and Audio Channels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltimy)
- [Other Channels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltiny)

The channel folders and elements in this section include:

- Position
- [Rotation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknlti)
- [Scale](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltk)
- [Shear](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltm)
- [Anchor Point](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknlto)
- [Bottom Left/Bottom Right/Top Right/Top Left](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltq)

__**Position**__

**Description**
: Encodes a scene object’s position.

**Channels**
: `X` (float). The X position of the object.

****
: `Y` (float). The Y position of the object.

****
: `Z` (float). The Z position of the object.

__**Rotation**__

**Description**
: Encodes an object’s rotation in ZYX order. A rotation parameter with an empty XML tag is maintained for backward compatibility purposes and should not be modified.

**Channels**
: `X` (float). The rotation about the X axis, in radians.

****
: `Y` (float). The rotation about the Y axis, in radians.

****
: `Z` (float). The rotation about the Z axis, in radians.

****
: `Animate` (enumerated): 0: use rotation; 1: use orientation.

__**Scale**__

**Description**
: Encodes an object’s scale.

**Channels**
: `X` (float). The scale factor of the object about the X axis.

****
: `Y` (float). The scale factor of the object about the Y axis.

****
: `Z` (float). The scale factor of the object about the X axis.

__**Shear**__

**Description**
: Encodes an object’s shearing properties.

**Channels**
: `X` (float). The shearing factor of the object about the X axis.

****
: `Y` (float). The shearing factor of the object about the Y axis.

__**Anchor Point**__

**Description**
: Encodes an object’s anchor point.

**Channels**
: `X` (float). The X position of the object’s anchor point.

****
: `Y` (float). The Y position of the object’s anchor point.

****
: `Z` (float). The Z position of the object’s anchor point.

__**Bottom Left/Bottom Right/Top Right/Top Left**__

**Description**
: Encodes each corner of the Four-Corner warping parameter of a scene node.

**Channels**
: `X` (float). The X position of this corner.

****
: `Y` (float). The Y position of this corner.

The channel folders and elements in this section include:

- [Background Color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcma)
- [RGB](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcmi)
- [RGBn](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcmq)
- [Alpha](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcmy)
- [Alphan](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcna)
- [Color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcni)
- [Gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcnq)
- [End](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltcny)
- [Start](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltemy)

__**Background Color**__

**Description**
: Encodes background color for various elements.

**Channels**
: `Red` (float). The value of the Red channel for this background color.

****
: `Green` (float). The value of the Green channel for this background color.

****
: `Blue` (float). The value of the Blue channel for this background color.

****
: `Gamma` (float). The gamma value for this background color.

__**RGB**__

**Description**
: Encodes a series of gradient color tags.

**Attributes**
: `id=`, `flags=`, `factoryID=`

**Subelements**
: `flags`

****
: `RGBn*`–>

__**RGBn**__

**Description**
: Encodes color information specific to a gradient color tag. The `name=` attribute for this parameter is set according to the following convention: for a gradient tag containing m gradient color tags, the first parameter’s name attribute is RGB1; the second is RGB2, and so on, until RGBn, where n is equal to m.

**Channels**
: `flags`

****
: `Offset` (percent). The absolute location of this color tag on a gradient line, represented as a constant curve when not keyframed. This parameter contains a `factoryID=` attribute referring to a channel. Must be represented as a curve.

****
: `Middle` (percent). The relative location of this color tag’s middle point between this color tag and the next, represented as a constant curve when not keyframed. This parameter contains a `factoryID=` attribute referring to a channel. Must be represented as a curve.

****
: `Interpolation` (enumerated). The interpolation method for this color, represented as a constant curve. This parameter contains a factoryID attribute referring to a channel. 0: constant; 1: linear; 2: continuous.

****
: `Color`–>. The color at the offset of this color tag. This color parameter’s subelements, which represent red, green and blue color channels along with a gamma value, must be represented as curves—constant curves when not keyframed. (You cannot keyframe the gamma value.) This parameter contains a `factoryID=` attribute referring to a channel.

__**Alpha**__

**Description**
:  Encodes a series of gradient opacity tags.

**Attributes**
: `id=`, `flags=`, `factoryID=`

**Subelements**
: `flags`

****
: `Alphan*`–>

__**Alphan**__

**Description**
: Encodes color information specific to a gradient opacity tag. For a gradient tag containing m gradient opacity tags, the first parameter’s name attribute is Alpha1; the second is Alpha2, and so on until Alphan, where n is equal to m.

**Subelement**
: `flags`

**Channels**
: `Offset` (percent). The absolute location of this opacity tag on a gradient line, represented as a constant curve when not keyframed. This parameter contains a `factoryID=` attribute referring to a channel.

****
: `Middle` (percent). The relative location of this opacity tag’s middle point between this color tag and the next, represented as a constant curve when not keyframed. This parameter contains a `factoryID=` attribute referring to a channel.

****
: `Interpolation` (enumerated). The interpolation method for this opacity tag, represented as a constant curve. This parameter contains a `factoryID=` attribute referring to a channel. 0: constant; 1: linear; 2: continuous.

****
: `Alpha` (float). The value of the alpha channel at this point, represented as a constant curve when not keyframed. This parameter contains a `factoryID=` attribute referring to a channel.

__**Color**__

**Description**
: Encodes color in Motion. Can be used to represent individual colors or colors for gradient tags.

**Attributes**
: `id=`, `flags=`, `factoryID=`. The `factoryID=` for this channel folder; present only for color channel folders that represent colors for gradient tags.

**Channels**
: `Red` (percent). The amount of red color to contribute to the final output color.

****
: `Green` (percent). The amount of green color to contribute to the final output color.

****
: `Blue` (percent). The amount of blue color to contribute to the final output color.

****
: `Gamma` (float). The gamma value of this color. You cannot keyframe this value.

****
: `Color Mix` (percent). The amount to color each pixel of a LiveFont text style. Present only for the Face channel folder of a text object’s style element. See [Face](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltena).

__**Gradient**__

**Description**
: Encodes information pertaining to a gradient for various Motion objects.

**Subelements**
: `RGB`–>

****
: `Alpha`–>

****
: `Type` (enumerated): 0: linear; 1: radial.

****
: `Start`–>. The starting point for this gradient.

****
: `End`–>. The ending point for this gradient.

__**End**__

**Description**
: The ending point for a gradient.

**Channels**
: `X` (float). The X position of this point.

****
: `Y` (float). The Y position of this point.

__**Start**__

**Description**
: The starting point for a gradient.

**Channels**
: `X` (float). The X position of this point.

****
: `Y` (float). The Y position of this point.

The channel folders and elements in this section include:

- LiveFont Timing
- [Type On](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltema)
- [Path Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltemi)
- [Path](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltemq)
- [Scale](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltimq)
- [Face](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltena)
- [Outline](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknlteni)
- [Glow](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltima)
- [Drop Shadow](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkmy)

__**LiveFont Timing**__

**Description**
: Encodes the parameters for LiveFont timing.

**Channels**
: `Random` (float): a random variant for the order in which LiveFont movies are played. No keyframing supported.

****
: `Random Seed` (unsigned integer): random seed for the Random parameter. No keyframing supported.

****
: `Sequence` (percent). The percentage of a LiveFont movie to play for a character before the subsequent character’s LiveFont movie plays.

****
: `Direction` (enumerated): 0: From Left; 1: From Right; 2: Ping-Pong.

****
: `Speed` (float). The speed at which to play each LiveFont movie in this sequence, where 1.0 is the default speed. No keyframing supported.

****
: `Play` (enumerated): 0: Forward; 1: Backward; 2: Ping-Pong.

****
: `Loop` (unsigned integer). The number of times to loop through each LiveFont movie. No keyframing supported.

****
: `To End` (Boolean).

****
: `Hold First` (positive float). The number of seconds to delay the beginning of each LiveFont movie. No keyframing supported.

****
: `Hold Last` (positive float). The number of seconds to hold the last frame of this font’s LiveFont movie. No keyframing supported.

__**Type On**__

**Description**
: Encodes the Type On characteristics for a text object.

**Channels**
: `Start` (percent): denotes the first letter to draw, as a percentage of the number of letters in the text object.

****
: `End` (percent): denotes the last letter to draw, as a percentage of the number of letters in the text object.

****
: `Fade In` (Boolean): 1 if letters fade in as they are brought on-screen; 0 if not.

__**Path Options**__

**Description**
: Encodes path options for a text object.

**Channels**
: `Path`–>: a container for the curve describing an open spline for a text object.

****
: `Path`–>: a container for the curve describing a closed spline for a text object.

****
: `Path Shape` (enumerated): 0: open spline; 1: closed spline; 2: circle; 3: rectangle; 4: wave; 5: geometry.

****
: `Path Type` (enumerated): affects open and closed spline shapes only. 0: bezier; 1: B-spline.

****
: `Radius`–>: affects circle path shape only.

****
: `Size`–>: affects rectangle path shape only.

****
: `Start Point`–>: affects wave path shape only.

****
: `End Point`–>: affects wave path shape only.

****
: `Amplitude` (float). The amplitude for a wave path. Affects wave path shape only.

****
: `Frequency` (float). The frequency of a wave path. Affects wave path shape only.

****
: `Phase` (angle). The phase of the wave path, in radians. Affects wave path shape only.

****
: `Damping` (float). The damping of the wave path. Affects wave path shape only.

****
: `Shape Source` (id). The id of the geometry source. Affects geometry path shape only.

****
: `Attach To Shape` (Boolean): 1 if enabled; 0 if disabled. Affects wave path shape only.

****
: `Path Offset` (float): amount to offset from beginning of path, in 1/100s of a percent.

****
: `Wrap Around` (Boolean): 1 if enabled; 0 if disabled.

****
: `Inside Path` (Boolean): 1 if enabled; 0 if disabled.

****
: `Align to Path` (Boolean): 1 if enabled; 0 if disabled.

****
: `Align to Text` (Boolean): 1 if enabled; 0 if disabled.

__**Path**__

**Description**
: Encodes the keypoints in a path for a text object. The subelements in this channel folder are X, Y, and Z position parameters, represented as curves. Each keypoint in the curve element representing the X, Y, and Z parameters represents the position of a control point in the text path.

**Subelement**
: `foldFlags`

**Channels**
: `X` (float). The X value of the position of each key point in the text path, as a parametric curve.

****
: `Y` (float). The Y value of the position of each key point in the text path, as a parametric curve.

****
: `Z` (float). The Z value of the position of each key point in the text path, as a parametric curve.

__**Scale**__

**Description**
: Encodes a parameter that determines if character scale affects the layout position for glyphs in a text object.

**Channels**
: `Affects Layout` (Boolean): 0 if scale does not affect layout position, 1 if it does.

__**Face**__

**Description**
: Encodes the Face parameter for text styles.

**Channels**
: `Fill With` (enumerated): 0: color; 1: gradient; 2: texture.

****
: `Color`–>. NOTE: Uniquely for a text object, the `Color` subelement of `Face` includes `Color Mix` (percent), defined as the amount to color each pixel of a LiveFont text style.

****
: `Gradient`–>

****
: `Texture`–>

****
: `Opacity` (percent). The opacity of the glyph face for this text style.

****
: `Blur` ->

****
: `Blur`. Used for backward compatibility; should not be modified.

__**Outline**__

**Description**
: Encodes the Outline parameter for text styles.

**Channels**
: `Fill With` (enumerated): 0: color; 1: gradient; 2: texture.

****
: `Color`–>

****
: `Gradient`–>

****
: `Texture`–>

****
: `Opacity` (percent). The opacity of the outline for this text style.

****
: `Blur` ->

****
: `Blur`. Used for backward compatibility; should not be modified.

****
: `Width` (float). The width of the outline.

****
: `Layer Order` (enumerated): 0: under face; 1: over face.

****
: `Four Corner` –>

__**Glow**__

**Description**
: Encodes the Glow values for text styles.

**Channels**
: `Fill With` (enumerated): 0: color; 1: gradient; 2: texture.

****
: `Color`–>

****
: `Gradient`–>

****
: `Texture`–>

****
: `Opacity` (percent). The opacity of the glow for this text style.

****
: `Blur` ->

****
: `Blur`. Used for backward compatibility; should not be modified.

****
: `Radius` (float). The radius of the glow.

****
: `Scale`–>. The scaling factor of the glow for this text style.

****
: `Offset`–>. The offset of the glow for this text style.

****
: `Layer Order` (enumerated): 0: under face; 1: over face.

****
: `Four Corner` –>

__**Drop Shadow**__

**Description**
: Encodes the Drop Shadow values for a text style.

**Channels**
: `Fill With` (enumerated): 0: color; 1: gradient; 2: texture.

****
: `Color`–>

****
: `Gradient`–>

****
: `Texture`–>

****
: `Opacity` (percent). The opacity of the drop shadow for this text style.

****
: `Blur` ->

****
: `Scale`–>. The scaling factor of the drop shadow for this text style.

****
: `Distance` (float). The distance of the drop shadow for this text style.

****
: `Angle` (radians). The angle of the drop shadow for this text style.

****
: `Fixed Source` (Boolean): 1 if the drop shadow’s distance remains fixed as the camera moves about the text object; 0 if it does not.

****
: `Four Corner`->

The channel folders and elements in this section include:

- Shape Animation
- [Fill](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkna)
- [Fill Color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkni)
- [Start Point](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknlteoa)
- [End Point](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltimi)
- [Angle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknlteoi)
- [Angle Randomness](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgma)
- [Opacity Over Life](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgmi)
- [Brush Profile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgmq)
- [Scale](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgmy)
- [Scale End](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgna)
- [Shape Parameters](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgni)
- [Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgnq)
- [Outline](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgny)
- [Alpha Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgoa)
- [Alpha Color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltgoi)

__**Shape Animation**__

**Description**
: Encodes the X and Y positions of the keypoints in a Motion shape.

**Subelements**
: `curve_X`: specifies the X positions of the keypoints.

****
: `curve_Y`: specifies the Y positions of the keypoints.

__**Fill**__

**Description**
: Encodes the color parameters for shapes.

**Subelements**
: `Fill Mode` (enumerated). 0: Color; 1: Gradient

****
: `Fill Color`->

****
: `Fill Opacity` (float). The opacity of a shape’s color.

****
: `Gradient`->

__**Fill Color**__

**Description**
: Encodes the color of a fill for shapes.

**Channels**
: `Red` (percent). The amount of red color to contribute to the fill color.

****
: `Green` (percent). The amount of green color to contribute to the fill color.

****
: `Blue` (percent). The amount of blue color to contribute to the fill color.

****
: `Gamma` (float). The gamma value of the fill color.

__**Start Point**__

**Description**
: Encodes the starting point for line or wave replicators, or text paths.

**Channels**
: `X` (float). The X coordinate of the starting point.

****
: `Y` (float). The Y coordinate of the starting point.

****
: `Z` (float). The Z coordinate of the starting point.

__**End Point**__

**Description**
: Encodes the ending point for line or wave replicators, or text paths.

**Channels**
: `X` (float). The X coordinate of the ending point.

****
: `Y` (float). The Y coordinate of the ending point.

****
: `Z` (float). The Z coordinate of the ending point.

__**Angle**__

**Description**
: Encodes angle properties for particle cells or replicator cells, in radians.

**Subelement**
: `foldFlags`

**Channels**
: `X` (float). The angle about the X axis to rotate each cell.

****
: `Y` (float). The angle about the Y axis to rotate each cell.

****
: `Z` (float); the angle about the Z axis to rotate each cell. Present for replicator cells in 3D mode only.

****
: `Angle` (angle). The angle about the Z axis to rotate each cell; present in 2D mode only, always present for particle cells.

****
: `Animate` (enumerated): 0: use rotation; 1: use orientation.

__**Angle Randomness**__

**Description**
: Encodes the angle randomness properties for particle cells or replicator cells.

**Subelement**
: `foldFlags`

**Channels**
: `X` (float). The variance to apply to the X axis rotation of each cell.

****
: `Y` (float). The variance to apply to the Y axis rotation of each cell.

****
: `Z` (float). The variance to apply to the Z axis rotation of each cell. Present for replicator cells in 3D mode only.

****
: `Angle Randomness` (angle). The variance to apply to the Z axis rotation of each cell; present in 2D mode only, always present for particle cells.

****
: `Animate` (enumerated): 0: use rotation; 1: use orientation.

__**Opacity Over Life**__

**Description**
: Encodes Opacity Over Life values for various Motion objects, such as particle cells and replicator cells.

**Subelement**
: `foldFlags`

**Channel**
: `RGB`–>

****
: `Alpha`–>

__**Brush Profile**__

**Description**
:  Encodes Brush Profile values for various Motion objects, such as replicator cells for Motion paint strokes and shapes.

**Subelement**
: `foldFlags`

**Channel**
: `RGB`–>

****
: `Alpha`–>

__**Scale**__

**Description**
: Encodes scaling factors for various parameters.

**Subelement**
: `foldFlags`

**Channel**
: `X` (float). The horizontal scale factor.

****
: `Y` (float). The vertical scale factor.

__**Scale End**__

**Description**
: Encodes scaling factor for replicator cells sitting at the edges of a replicator.

**Subelement**
: `foldFlags`

**Channels**
: `X` (float). The horizontal scale factor.

****
: `Y` (float). The vertical scale factor.

__**Shape Parameters**__

**Description**
: Encodes the characteristics of a replicator cell. Many parameters are used by emitters, replicators, shapes and paint strokes. Other parameters are used only by some of these objects. See the Motion Inspector tab for details.

**Channels**
: `Shape` (enumerated). The shape for the replicator. 0: line; 1: rectangle; 2: circle; 3: burst; 4: spiral; 5: wave; 6: geometry; 7: image; 8: box (3D only); 9: sphere (3D only).

****
: `Object Animation`: a parameter used internally by Motion that should not be modified.

****
: `Emit At Points` (Boolean): 0 if disabled, 1 for enabled. Used by emitters.

****
: `Arrangement` (enumerated). The arrangement for rectangle replicators. 0: outline; 1: tile fill; 2: random fill.

****
: `Points` (unsigned integer). The number of cells for the replicator.

****
: `Columns` (unsigned integer). The number of columns for rectangle replicators.

****
: `Rows` (unsigned integer); the number of rows for rectangle replicators.

****
: `Ranks` (unsigned integer); the number of ranks for 3D rectangle replicators.

****
: `Spacing` (float). The spacing between individual cells.

****
: `Spacing Over Stroke`. This parameter is used for backwards compatibility and should not be modified.

****
: `Width` (float). The width of each individual cell.

****
: `Width Over Stroke`. This parameter is used for backwards compatibility and should not be modified.

****
: `Tile Offset` (float). The offset at which to begin placement of rows of cells on this tile-arranged replicator.

****
: `Origin` (enumerated). The build origin for rectangle or image replicators in fill arrangements. 0: upper left; 1: upper right; 2: lower left; 3: lower right; 4: center; 5: left; 6: right; 7: top; 8: bottom.

****
: `Build Style` (enumerated). The rectangle build style in tile arrangement and corner-based origin. 0: across; 1: by row; 2: by column; 3: by rank (valid only for replicators).

****
: `Hidden`: a parameter used internally by Motion that should not be modified.

****
: `Origin` (enumerated). The build origin for line and wave replicators. Not present for emitters. 0: start point; 1: end point; 2: center.

****
: `Build Style` (enumerated). The build style for geometric replicators or rectangle replicators in an outline arrangement; not present for emitters.
0: counter clockwise;
1: clockwise.

****
: `Origin` (enumerated). The build origin for circle, burst, and spiral replicators.
0: center;
1: edge.

****
: `Shuffle Order` (Boolean): 1 if enabled; 0 if disabled; used by replicators.

****
: `Offset` (float). The percentage of the replicator shape at which to begin placing cells.

****
: `Radius` (float). The radius of this spiral or circle, outline-arranged replicator.

****
: `Start Point`–>

****
: `End Point`–>

****
: `Size`. This parameter is used for backward compatibility purposes and should not be modified.

****
: `Size`–>

****
: `Number of Arms` (unsigned integer). The number of arms for this spiral replicator.

****
: `Points Per Arm` (unsigned integer). The number of cells per arm for this spiral replicator.

****
: `Twists` (float). The number of twists for this spiral replicator.

****
: `Amplitude` (float). The amplitude for this wave replicator.

****
: `Frequency` (positive float). The frequency for this wave replicator.

****
: `Phase` (angle). The phase angle for this wave replicator, in radians.

****
: `Damping` (float). The damping factor for this wave replicator.

****
: `Emit At Alpha` (Boolean): 1 if enabled; 0 if disabled; used for emitters.

****
: `Emission Alpha Cutoff` (percent). The alpha cutoff point; used for emitters.

****
: `Shape Source` (id). The id of the geometry to use for this geometry replicator.

****
: `Image Source`(id). The id of the image to use for the image color mode.

__**Size**__

**Description**
: Encodes the size of the rectangle or box defining a replicator’s shape.

**Channels**
: `Width` (float). The width of the rectangle or box.

****
: `Height` (float). The height of the rectangle or box.

****
: `Depth` (float). The depth of the box; used only for 3D replicators.

__**Outline**__

**Description**
: Encodes the outline for Motion shapes.

**Channels**
: `Brush Type` (enumerated):
0: solid;
1: airbrush;
2: image.

****
: `Brush Color`–>. The color of the outline.

****
: `Brush Opacity` (percent). The opacity for the outline.

****
: `Width` (float). The width of the outline.

****
: `Preserve Width` (Boolean): 0 if disabled; 1 if enabled.

****
: `Joint` (enumerated):
0: square;
1: round;
2: bevel.

****
: `Start Cap` (enumerated):
0: square;
1: round;
2: bevel;
3: arrow.

****
: `End Cap` (enumerated):
0: square;
1: round;
2: bevel;
3: arrow.

****
: `Arrow Length` (float). The length of the arrow end cap.

****
: `Arrow Width` (float). The width of the arrow end cap.

****
: `Order` (enumerated):
0: under fill;
1: over fill.

****
: `First Point Offset` (percent). The point at which the outline should begin along the shape.

****
: `Last Point Offset` (percent). The point at which the outline should end along the shape.

****
: `Hidden Stroke Completion`: a parameter used internally by Motion that should not be modified.

****
: `Use Natural Stroke`: a parameter used internally by Motion that should not be modified.

****
: `Offset`: a parameter used internally by Motion that should not be modified.

****
: `Pressure Over Stroke`: a parameter used internally by Motion that should not be modified.

****
: `Tilt Over Stroke`: a parameter used internally by Motion that should not be modified.

****
: `Pen Speed Over Stroke`: a parameter used internally by Motion that should not be modified.

__**Alpha Type**__

**Description**
: Encodes the alpha channel to use for clips.

**Subelement**
: Note: this element does not contain a `foldFlags subelement.`.

**Channels**
: `Alpha Type` (enumerated):
0: none/ignore;
1: straight;
2: premultiplied black;
3: premultiplied white;
4: premultiplied color.

****
: `Alpha Color`–>

__**Alpha Color**__

**Description**
: Encodes the color to use for the alpha channel of a clip.

**Channels**
: `Red` (percent). The amount of red to contribute to the alpha color. Keyframes unsupported.

****
: `Green` (percent). The amount of green to contribute to the alpha color. Keyframes unsupported.

****
: `Blue` (percent). The amount of blue to contribute to the alpha color. Keyframes unsupported.

****
: `Gamma` (float). The gamma value of this color.

The channel folders and elements in this section include:

- [OpenEXR](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltina)
- [Crop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltini)
- [Master Controls](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltinq)

__**OpenEXR**__

**Description**
: Encodes properties related to OpenEXR clips.

**Channels**
: `Exposure` (float). The exposure value for this clip.

****
: `Defog` (float). The defog value for this clip.

****
: `KneeLow` (float). The KneeLow value for this clip.

****
: `KneeHigh` (float). The KneeHigh value for this clip.

__**Crop**__

**Description**
: Encodes cropping information for an image or movie in the Media list.

**Channels**
: `Left` (float). The number of pixels to crop from the left.

****
: `Right` (float). The number of pixels to crop from the right.

****
: `Bottom` (float). The number of pixels to crop from the bottom.

****
: `Top` (float). The number of pixels to crop from the top.

__**Master Controls**__

**Description**
: Encodes information for emitters containing more than one particle cell.

**Channels**
: `Birth Rate` (float). The birth rate for this emitter.

****
: `Hidden`: a parameter used internally by Motion that should not be modified.

****
: `Initial Number` (float). The initial number of cells.

****
: `Life` (float). The lifespan of emitter cells.

****
: `Scale`–>

****
: `Speed` (float). The speed of emitter cells.

****
: `Spin` (float). The spin rate of emitter cells.

The channel folders and elements in this section include:

- [Spot Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltioa)
- [Clone Layer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltioi)
- [Texture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkma)
- [Offset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkmi)
- [Mask](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkmq)
- [Falloff](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltknq)
- [Depth of Field](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkny)
- [Shadows](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltkoa)

__**Blur**__

**Description**
: Encodes blur applied separately in x and y.

**Channels**
: `X` (float). The amount of blur in the x direction

****
: `Y` (float) The amount of blur in the y direction.

__**Spot Options**__

**Description**
: Encodes options for a light scene object.

**Channels**
: `Cone Angle` (float). The angle of the cone.

****
: `Soft Edge` (float). The angle of the soft edge.

__**Clone Layer**__

**Description**
: Encodes a clone layer’s source information.

**Subelement**
: `Source` (id). The id of the layer that this clone Layer uses as its source.

__**Texture**__

**Description**
: Encodes information pertaining to texture for various Motion objects.

**Channels**
: `Image` (id). The id of the media to use as the source for this texture.

****
: `Frame` (frame). The frame of this footage to use as the image for this texture; 0 for images.

****
: `Hold Frame` (Boolean): 0 if disabled; 1 if enabled.

****
: `Offset`–>

****
: `Wrap Mode` (enumerated)
0: none;
1: repeat;
2: mirror.

__**Offset**__

**Description**
: Encodes the offset for various parameters.

**Channels**
: `X` (float). The offset along the X direction.

****
: `Y` (float). The offset along the Y direction.

****
: `Z` (float). The offset along the Z direction. May not appear for parameters with two-dimensional offsets.

__**Mask**__

**Description**
: Encodes the properties of an image mask.

**Channels**
: `Mask Source` (id). The id corresponding to the source for this mask’s shape.

****
: `Frame` (frame). The frame at which to derive the source image for this mask; 0 for image files.

****
: `Hold Frame` (Boolean): 0 if disabled; 1 if enabled.

****
: `Offset`–>

****
: `Wrap Mode` (enumerated):
0: none;
1: repeat;
2: mirror.

__**Falloff**__

**Description**
: Encodes information pertaining to the falloff in reflectivity of a scene object.

**Channels**
: `Begin Distance` (float). The distance inside the reflection at which the falloff begins.

****
: `End Distance` (float). The distance at which the falloff ends.

**Term**
: `Exponent` (float). Controls how quickly a reflection gets fainter as the reflected object gets further away from the reflected surface.

**Term**
: Para

__**Depth of Field**__

**Description**
: Encodes information pertaining to the depth of field effect from a camera.

**Channels**
: `DOF Blur Amount` (float). The amount of blur to apply to out-of-focus objects.

****
: `Focus Offset` (float). The distance from the camera that will be in perfect focus.

****
: `Near Focus` (float). The nearest point of focus, measured in pixels as an offset from the focal distance.

****
: `Far Focus` (float). The farthest point of focus, measured in pixels as an offset from the focal distance.

****
: `Infinite Focus` (Boolean): 1 if the far focus is infinite, 0 if the Far Focus setting is applied.

****
: `Filter` (enumerated): 0: Gaussian; 1: Defocus.

****
: `Filter Shape` (enumerated): 0: Disk; 1: Polygon.

****
: `Sides` (positive integer). The number of sides in the Polygon filter; must be at least 3.

****
: `Depth` (enumerated): 0: Radial; 1: Planar.

__**Shadows**__

**Description**
: Encodes information pertaining to the shadows based on a Light. (A scene object also has [Shadows](The%20Properties%20Parameter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnznknltcni) parameters.)

**Channels**
: `Opacity` (percent). The opacity of shadows based on a Light.

****
: `Softness` (float). The amount of softness of shadows based on a Light.

****
: `Uniform Softness` (Boolean): 0 if softness is based on the distance from a Light, 1 if not.

****
: `Color`->. The color of the shadows based on a Light.

[Next](Customizing%20a%20Motion%20XML%20Project%20File.md)[Previous](The%20Object%20Parameter.md)


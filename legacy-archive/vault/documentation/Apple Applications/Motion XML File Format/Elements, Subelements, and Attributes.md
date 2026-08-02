---
title: Motion XML File Format
apple_id: TP40007455
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2010-06-24'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/motion_XML_guide/ESA/ESA.html
archived_at: '2026-07-15T05:18:59.198203Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Motion XML File Format](About%20This%20Document.md)


[Next](The%20Properties%20Parameter.md)[Previous](Motion%20XML%20Overview.md)

# Elements, Subelements, and Attributes

This chapter provides a general description of the elements, subelements, and attributes that encode scene objects. It includes the following sections:

- Higher-Level Elements
- [Common Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltgmq)
- [CommonReserved Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltgna)
- [Common Timing Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltima)
- [Other Common Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltkni)
- [Curve Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltkoi)
- [Text Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltmma)
- [Common Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltena)
- [More About the id= Attribute](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltmoa)

__**layer**__

**Description**
: A Motion layer (also known in the UI as a group).

**Attributes**
: `name=`, `id=`.

**Subelements**
: `[scenenode* | layer*]*` : layers or scenenodes a layer contains. The order in which `layer` and `scenenode` elements appear follows the Motion scene graph hierarchy.

****
: `mask*` : shape or image masks in the layer.

__**scenenode(Camera)**__

**Description**
: A Motion camera.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: This element does not contain `validTracks` or `filter` subelements.

__**scenenode(Light)**__

**Description**
: A Motion light.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: This element does not contain `validTracks` or `filter` subelements.

__**scenenode(Image)**__

**Description**
: A Motion image object representing a media file such as an image, an image sequence, a movie clip, an Adobe PDF or Photoshop file.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: `numberOfPages` (unsigned integer) : the number of pages in a PDF file. Present only if a PDF file has more than one page.

****
: `linkedObjects` (id): the id of the audioTrack element this movie clip is linked to, if the movie clip contains audio (located after flags). Present only if an audio track is linked to this `scenenode`.

****
: `mask*` : shape or image masks in the layer.

__**scenenode(Text)**__

**Description**
: A Motion text object.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: `paragraphMarginsCached`: the previously used Paragraph layout margins..

****
: `scrollMarginsCached`: the previously used Scroll layout margins.

****
: `crawlMarginsCached`: the previously used Crawl layout margins.

****
: `paragraphStyles+`: information about the formatting of a paragraph in a text layout.

****
: `style+`: styles a text layout incorporates.

****
: `styleRun` : style runs a text layout incorporates.

****
: `text` (string) : the text in a text layout.

****
: `mask*` : shape or image masks in the layer.

****
: `object*`: describes a glyph in a text layout. There must be one object element for every glyph in a text layout.

__**scenenode(Shape)**__

**Description**
: A Motion shape such as a rectangle, circle, curve, line, or paint stroke.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: `scenenode(Replicator)`

****
: `isShapeStyle` : an element used internally by Motion that you should not modify.

****
: `mask*` : shape or image masks in the layer.

__**scenenode(Generator)**__

**Description**
: A Motion generator.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

****
: `pluginUUID=` (UUID) : internal plugin UUID for this generator.

****
: `pluginVersion` (float) : internal plugin version of this generator.

****
: `pluginName` (string) : internal name of this generator.

**Subelements**
: See [Common Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltgmq).

****
: `mask*` : shape or image masks in the layer.

__**scenenode(Emitter)**__

**Description**
:  A Motion emitter. Motion masks, shapes, and paint strokes contain a `scenenode` element whose `name=` attribute is `"Emitter"` and whose `factoryID=` attribute corresponds to a Motion replicator. These are not Motion emitters but rather a special class of Motion replicator used to enhance masks, shapes, and paint strokes. See `scenenode` (replicator).

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: `scenenode(Particle Cell)*` : particle cell sources that this emitter incorporates.

****
: `mask*` : shape or image masks in the layer.

__**scenenode(Replicator)**__

**Description**
: A Motion replicator. May also represent a Motion mask or shape If not specifying a Motion replicator, the `name=` attribute is `"Emitter"` and the `factoryID=` attribute corresponds to a replicator.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: `scenenode(Replicator Cell)*` : replicator cell sources that this replicator incorporates.

****
: `Behavior (“Pen Pressure”)` Note: present only if this replicator represents a shape or paint stroke and incorporates a shape style.

****
: `Behavior ("Pen Speed")` Note: present only if this replicator represents a shape or paint stroke and incorporates a shape style

****
: `mask*` : shape or image masks in the layer.

__**scenenode(Particle Cell)**__

**Description**
: An individual cell from a Motion emitter.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: See [Common Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltgmq).

__**scenenode(Replicator Cell)**__

**Description**
: An individual cell from a Motion replicator. May also specify a Motion mask or shape cell.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: See [Common Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltgmq).

__**footage**__

**Description**
: A top-level element that serves as a folder for a project’s `clip` elements.

**Attributes**
: `id=`, `name=`. The `name=` attribute is set to `"Media Layer"` and should not be changed.

**Subelements**
: `clip*`

__**clip**__

**Description**
: A media file, such as a movie file, image, or audio file, found in the Media tab of the Project pane.

**Attributes**
: `id=`, `name=`.

**Subelements**
: `pathURL` (URL): absolute URL to the file on disk that this clip represents.

****
: `relativeURL` (URL) : the relative URL to the file with respect to the location of the Motion project file. Present only if the source file is not in the same folder as the Motion project file.

****
: `missingWidth` (integer): the width of this file. Used as a placeholder when the file is missing from disk.

****
: `missingHeight` (integer): the height of this file. Used as a placeholder when the file is missing from disk

****
: `missingDuration` (float) : the duration of this file in seconds. Equal to the reciprocal of the project frame rate if the clip represents an image. Used as a placeholder when the file is missing from disk.

****
: `creationDuration` (integer) : duration of this element in frames with respect to the project frame rate. Used as a placeholder for the time line when the file is missing from disk

****
: `mediaID` (UUID): UUID of clip if present in file. Empty if no UUID is present.

__**audio**__

**Description**
: A top-level element that serves as a folder for a project’s `audiotrack` elements.

**Attributes**
: `id=`, `name=`. The `name=` attribute is set to `"Audio Layer"` and should not be changed.

**Subelements**
: `audioTrack*`

****
: `scenenode(Master)`

__**scenenode(Master)**__

**Description**
: A top-level node that represents Motion’s master audio settings.

**Attributes**
: `name=`, `id=`, `factoryID=`, `version=`

**Subelements**
: See [Common Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltgmq).

__**audioTrack**__

**Description**
: An audio track in a Motion project, as found in the Audio tab of the Project pane.

**Attributes**
: `id=`, `name=`

**Subelements**
: `linkedObjects` (id): the id of the `scenenode` element that this `audioTrack` is linked to. Present only if the audio track is linked to a `scenenode` element

__**filter**__

**Description**
: A Motion filter.

**Attributes**
: `name=`, `id=`, `factoryID=`

****
: `pluginUUID=` (UUID) : internal plugin UUID for this filter.

****
: `pluginVersion` (float) : internal plugin version of this filter.

****
: `pluginName` (string) : internal name of this filter.

**Subelements**
: Filter-specific parameters. A complete description of filter parameters is beyond the scope of this document. Refer to the _Motion User Manual_ for details about each filter.

__**behavior**__

**Description**
: A Motion behavior.

**Attributes**
: `name=`, `id=`, `factoryID=`

**Subelements**
: Behavior-specific parameters. A complete description of behavior parameters is beyond the scope of this document. Refer to the _Motion User Manual_ for details about each behavior.

__**mask(Shape)**__

**Description**
: A Motion shape mask.

**Attributes**
: `name=`, `id=`, `factoryID=`

**Subelements**
: `scenenode(Replicator)`

****
: `isShapeStyle` : Motion uses this element internally. You should not modify it.

__**mask(Image)**__

**Description**
: A Motion image mask.

**Attributes**
: `name=`, `id=`, `factoryID=`

**Subelements**
: See [Common Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltgmq).

Many scene objects and parameters contain similar subelements describing general characteristics of the scene object.

Motion uses these subelements for internal processing. You should not change them.

__**override**__

**Description**
: An unsigned integer Motion uses for backward compatibility purposes. You should not modify this element.

__**ignoreBehaviorsBeforeID**__

**Description**
: An integer that Motion uses internally. You should not modify this element.

__**flags**__

**Description**
: An unsigned integer that Motion uses for internal processing. You should not modify this element.

__**foldFlags**__

**Description**
: An unsigned integer that Motion uses for internal processing. You should not modify this element.

__**baseFlags**__

**Description**
: An unsigned integer that Motion uses for internal processing. You should not modify this element.

__**timing**__

**Description**
: An element encoding a scene object’s position on the timeline.

**Attributes**
: `in=` (frame) : the in point of a scene object in the timeline.

****
: `out=` (frame) : the out point of a scene object in the timeline.

****
: `offset=` (frame) : the frame where the media’s first frame begins. This is applicable to Motion image objects referencing movie clips.

**Notes**
: As an example, if a 20-frame movie clip is dropped into the project and its object track slipped so that it begins at frame 30, the `timing` element then appears as:
`<timing in=”30” out=”49” offset=”30” />`.

****
: If the left edge of the object track is moved 5 frames to the right, effectively setting the In point to 35 and the duration to 15 frames, the `timing` element is then:
`<timing in=”35” out=”49” offset=”30” />`.

__**timemarkerset**__

**Description**
: The set of time markers for a scene object.

**Subelement**
: `timemarker*`

__**timemarker**__

**Description**
: Specifies a time marker for a Motion scene object as it appears in the timeline.

**Subelements**
: `inpoint` (frame): the frame where this time marker appears.

****
: `outpoint` (frame): the frame where this time marker ends. This element appears only if the time marker’s duration is greater than 1

****
: `label` (string): the name of this time marker. This element appears if the time marker has an assigned name.

****
: `comment` (string): the comment for this time marker. This element appears if the time marker has an assigned comment.

****
: `color` (enumerated): 0: red; 1: green; 2: blue; 3: purple; 4: orange; 5: yellow; 6: gray; 7: cyan.

****
: `type` (enumerated): 0: standard; 1: DVD menu loop; 2: DVD alpha transition.

__**Properties**__

**Description**
: A `parameter` element with this value for the `name=` attribute specifies a scene object’s unique properties. See [The Properties Parameter](The%20Properties%20Parameter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnznknltc).

__**Object**__

**Description**
: A `parameter` element with this value for the `name=` attribute specifies a scene object’s unique settings. See [The Object Parameter](The%20Object%20Parameter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltc).

__**filter\***__

**Description**
: A filter that this scene object incorporates. To see the XML details of a particular filter, you can include it in a Motion project and then examine the XML project file.

__**behavior\***__

**Description**
: A behavior that this scene object incorporates. To see the XML details of a particular behavior, you can include it in a Motion project and then examine the XML project file.

__**aspectRatio**__

**Description**
: A floating point number that sets the aspect ratio of a scene object

__**enabled**__

**Description**
: A Boolean value. Only appears in the XML file if the value is 0 and object is disabled.

__**locked**__

**Description**
: A Boolean value. Only appears in the XML file if the value is 1 and object is locked.

__**curve**__

**Description**
: A curve for a channel. It represents a channel’s value across time based on keypoints and their interpolation types. In some cases, a `curve` may actually represent a constant value. In this case, its `type=` attribute is not present, but a `value=` attribute is.

**Attributes**
: `type=` (enumerated): the type of value the curve represents: not present: constant 1: spline 3: used for backward-compatibility purposes.

****
: `default=` (dependent on the channel): the default value for this channel.

****
: `value=` (dependent on the channel). The constant value for this channel; used when “Disable Animation” is selected for a channel in the Inspector or Curve Editor.

****
: `parametric=` (Boolean): 1 if a curve is parametric; 0 otherwise (and the attribute is not visible). Used internally by Motion and should no be modified.

****
: `round=` (Boolean): 1 if the curve values are rounded; 0 otherwise. Used internally by Motion and should no be modified.

****
: `retimingExtrapolation=` (Boolean): 1 if a curve is used for retiming footage and has constant timing; 0 otherwise (and not visible).

****
: `value=` (dependent on the channel). Visible only if the value is a constant.

**Subelements**
: `numberOfKeyPoints` (integer): the number of keypoints in this curve

****
: `closed` (Boolean): 1 if the value of the channel this curve represents is interpolated after the last keyframe to values of the first keyframe; 0 otherwise (and not visible). This element is generally used only for curves representing a text object’s path position parameters.

****
: `preExtrapolation` (enumerated): the curve extrapolation method for values before the first keyframe: not visible: constant; 1: linear; 2: Ping-Pong; 3: repeat; 4: progressive repeat.

****
: `postExtrapolation` (enumerated): the curve extrapolation method for values after the last keyframe: not visible: constant;1: linear; 2: Ping-Pong; 3: repeat; 4: progressive repeat.

****
: `keyPoint*`: a keypoint (also known as a keyframe for parameters) for this curve. The number of `keyPoint` elements must equal the value of the `numberOfKeyPoints` element.

__**keyPoint**__

**Description**
: A keypoint for a curve. (Also known as a keyframe for parameters.)

**Attributes**
: `interpolation=` (enumerated): the interpolation method for this keypoint. Not present: bezier; 0: constant; 1: linear; 6: continuous; 7: ease In; 8: ease Out; 13: exponential; 14: logarithmic.

****
: `flags=`

**Subelements**
: `time` (frame): the frame where this keypoint appears on the timeline. For curve elements representing text object paths, the `time` subelement is the index of the keypoint on the text path, starting at 0.

****
: `value` (dependent on the channel): the value of the channel at this keypoint’s time.

****
: `bias` (percent): the bias for the keypoint. Used by `keyPoint` elements for B-spline curves. Visible in the XML file only if the bias is not 1.0

****
: `normal` (float): the normal value of this keypoint, if applicable. For curve elements representing text object paths, the `normal` subelement is used to determine the change in the normal vector of the path at this keypoint.

****
: `inputTangentTime` (float): independent variable for the input handle. Visible in the XML file only if the keypoint is not the first in a curve.

****
: `inputTangentValue` (float): dependent variable for the input handle; Visible in the XML file only if the keypoint is not the first in a curve.

****
: `outputTangentTime` (float): independent variable for the output handle. Visible in the XML file only if the keypoint is not the last in a curve.

****
: `outputTangentValue` (float): dependent variable for the output handle. Visible in the XML file only if the keypoint is not the last in a curve.

__**curve_X curve_Y**__

**Description**
: A container for a series of vertices pertaining to a Motion shape. The element `curve_X` describes the X positions of the vertices of a shape. The element `curve_Y` describes the Y positions of the vertices.

**Subelements**
: `vertex*`: a vertex for this shape in the specified dimension. There must be as many `vertex` elements as points in the shape.

__**vertex**__

**Description**
: A vertex for a Motion shape.

**Attributes**
: `index=` (integer): the index of a vertex in the shape for a given dimension. The first vertex is 0.

****
: `id=`. See [Motion Project File](Motion%20XML%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnbnknlto). The `id=` attributes for the x and y coordinates of a vertex are set according to the following convention: for x coordinates, `id=` begins at 1 and increments by 2; for y coordinates, `id=` begins at 2 and increments by 2. So (1,2) would be the x,y `id=` pair for the first vertex; (3,4) for the second pair; and so on.

****
: `flags=`. See [Motion Project File](Motion%20XML%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnbnknlto).

**Subelements**
: `vertex_folder`: a container for elements describing this vertex.

__**vertex_folder**__

**Description**
: A container of elements describing a vertex. If the positions of a vertex are keyframed, the parameters in `vertex_folder` are curves; otherwise, they are constant values.

**Attributes**
: `name=`(defaults to “Vertex”), `id=`, `flags=`. See [Motion Project File](Motion%20XML%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnbnknlto). The `id=` attributes for the x and y coordinates of a vertex are set according to the following convention: for x coordinates, `id=` begins at 1 and increments by 2; for y coordinates, `id=` begins at 2 and increments by 2. So (1,2) would be the x,y `id=` pair for the first vertex; (3,4) for the second pair; and so on.

**Subelements**
: Several `parameter` subelements specify a `vertex_folder` element.

****
: `Enabled` (Boolean): 1 if this point is enabled, 0 otherwise.

****
: `Value`(float): the value of the vertex that this vertex folder represents.

****
: `Bias`(percent): the point bias for this vertex. Used when this vertex represents a Motion B-Spline curve.

****
: `Input Tangent` (float): the value of the input tangent handle for this vertex. Used when this vertex represents a Motion Bezier curve.

****
: `Output Tangent` (float): the value of the output tangent handle for this vertex. Used when this vertex represents a Motion Bezier curve.

__**font**__

**Description**
: A Motion font name.

**Attributes**
: `type=` (Boolean): 0 if representing a system font; 1 if a LiveFont.

**Notes**
: The font name is specified by a string that provides the PostScript or LiveFont name of a font. System fonts are named as they appear in the Font Book application. LiveFonts are named as they appear in the Family drop-down box of the Format pane in the Inspector. They are prefaced by the font collection. (For example, Skywriter is named “Pro Series/Skywriter,” Chance is named “Collectors Edition/Chance”).

__**style**__

**Description**
: Encodes the features of a text style. (The style element does not contain information regarding the portions of text it affects. See the `styleRun` element.)

**Attributes**
: `name=`, `id=` , `factoryID=` , `version=`. Note: the `name=` attribute is set according to the following convention: for a text layout object containing n styles, the first style will be named Style; the second style will be named Style 1, and so forth until Style (n - 1).

**Subelements**
: `font`

****
: `copyFlags` (unsigned integer) : you should not modify this element that Motion uses internally.

****
: The subelements for style include the following channel folders:

****
: `Size` (float): the size in points of the font referenced in this style.

****
: `Tracking` (float): the tracking amount in pixels for this style.

****
: `Kerning` (float): the kerning amount for this style, in pixels.

****
: `Baseline` (float): the baseline amount for this style, in pixels.

****
: `Slant` (float): the slant amount for this style, in pixels.

****
: `Scale`–>

****
: `Offset`–

****
: `Rotation`–>

****
: Rotation: a parameter used for backward compatibility that should not be modified.

****
: `Monospace` (Boolean): 1 if enabled; 0 if disabled.

****
: `All Caps` (Boolean): 1 if enabled; 0 if disabled.

****
: `All Caps Size` (percent): the size of the capital letters relative to the size of the font.

****
: `Style Preset` : a parameter used internally by Motion that should not be modified.

****
: `Face`–>: a container for the parameters for the style’s face.

****
: `Drop Shadow`–>: a container for the parameters for the style’s drop shadow.

****
: `Outline`–>: a container for the parameters for the style’s outline.

****
: `Glow`–>: a container for the parameters for the style’s glow.

****
: `LiveFont Timing`–>: a container describing the parameters for LiveFont timing.

__**styleRun**__

**Description**
: An element describing the range of characters a particular style affects within a text layout `scenenode`.

**Attributes**
: `style=` (id): the id of the style that this style run incorporates.

****
: `offset=` (unsigned integer): the index of the character where this style run begins, where the index of the first character is 0.

****
: `length=` (unsigned integer): the number of consecutive characters this style run affects.

__**text**__

**Description**
: An element containing the literal string for a text layout object.

**Notes**
: The text for this text layout object; empty if the text layout object contains no text.

__**object**__

**Description**
: Encodes information for a glyph in a text layout object.

**Attributes**
: `value=` (unsigned integer): an decimal ASCII character code.

**`Subelement`**
: `Kerning` (float): the kerning value for this glyph in pixels.

__**paragraphMarginsCached**__

**Description**
: Contains the Paragraph Layout Mode’s previously used margins.

**Attributes**
: `cached=` (Boolean): 1 if margins have been previously set for the Paragraph Layout Mode, 0 if they have not.

****
: `left=` (float): the value of the left margin.

****
: `right=` (float): the value of the right margin.

****
: `top=` (float): the value of the top margin.

****
: `bottom=` (float): the value of the bottom margin.

__**scrollMarginsCached**__

**Description**
: Contains the Scroll Layout Mode’s previously used margins.

**Attributes**
: `cached=` (Boolean): 1 if margins have been previously set for the Scroll Layout Mode, 0 if they have not.

****
: `left=` (float): the value of the left margin.

****
: `right=` (float): the value of the right margin.

****
: `top=` (float): the value of the top margin.

****
: `bottom=` (float): the value of the bottom margin.

__**crawlMarginsCached**__

**Description**
: Contains the Crawl Layout Mode’s previously used margins.

**Attributes**
: `cached=` (Boolean): 1 if margins have been previously set for the Crawl Layout Mode, 0 if they have not.

****
: `left=` (float): the value of the left margin.

****
: `right=` (float): the value of the right margin.

****
: `top=` (float): the value of the top margin.

****
: `bottom=` (float): the value of the bottom margin.

__**paragraphStyle**__

**Description**
: Contains information related to a paragraph in a text layout object. There is one `paragraphStyle` object for every paragraph in the text layout object. A paragraph is defined as a sequence of characters terminated by a carriage return character.

**Subelements**
: `justification` (enumerated). 0: none; 1: partial; 2: full.

****
: `alignment` (enumerated). 0: left; 1: center; 2: right.

****
: `tabStop`

__**tabStop**__

**Description**
: Encodes information for a tab stop in a paragraph.

**Attributes**
: `position=` (unsigned float): the position of this tab stop.

****
: `type=` (enumerated). 0: left; 1: center; 2: right; 3: decimal.

In general, Motion uses the attributes listed here for internal processing. The common attributes include: `name=`, `id=`, `factoryID=`, and `version=`.

__**name=**__

**Description**
: A string encoding a name for a scene object in the Layers list or parameter. The `name=` attribute is written in the language of the system that produced the project file. It is not used internally by Motion to identify a scene object or parameter (see `id=` attribute below). The `name=` attribute of a scene object generally matches the name found in the Layers list of the Project Pane. The `name=` attribute of a parameter generally matches the name found in the Inspector or other relevant UI element.

****
: For instance, a `name=` attribute with the value `Position` in a `parameter` element references the position controls found in the Transform section of the Properties tab in the Inspector. This `parameter` has subelements for X, Y, and Z , also found when the Position control in the Inspector is collapsed.

****
: Generally, you should not modify the `name=` attribute of a `parameter` element. On the other hand, you can change `name=` attributes of elements referring to Motion scene objects, such as `layer` and `scenenode`.

__**id=**__

**Description**
: An unsigned integer identifying an object or parameter. Many elements in the Motion XML file format contain an `id=` attribute. Generally, this attribute is unique to the element and is used internally by Motion to identify its role in the project. You should not modify an `id=` attribute, particularly for `parameter` elements.

__**default=**__

**Description**
: An attribute of parameter elements whose data type depends on the channel. Generally, this attribute should not be modified.

__**factoryID=**__

**Description**
: An unsigned integer identifying a factory. Motion uses this attribute to identify the internal structures of an object by associating the object with a factory. (See [Factories](Motion%20XML%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnbnknlti)). You should not modified this attribute.

__**version=**__

**Description**
: An unsigned integer specifying Motion version information. Some objects contain a `version=` attribute that references the major version of Motion used to create this object. Motion uses this attribute for internal processing. You should not modify it.

The `id=` attributes for `scenenode`, `layer`, `footage`, `audioTrack`, and other elements that specify scene objects may be interrelated.

For example, if a movie clip scene object appears in the scene graph, its Media parameter will refer to a clip element’s `id=` attribute to describe the source media of the movie clip. Additionally, if the movie clip scene object references an audio track, the movie clip scene object will refer to the audio track’s `id=` attribute and vice versa:

__Listing 3-1__  id= Example

```
<scenenode name=”Movie1” id=”10395” factoryID=”1” version=”4”>
  . . .
  <linkedobjects>10397<linkedobjects>
  . . .
  <parameter name=”Object”>
  . . .
    <parameter name=”Media” id=”300” flags=”65552” value=”10393” />
  </parameter>
</scenenode>
<audio name=”Audio Layer” id=”10398”>
  <audioTrack name=”Movie1” id=”10397”>
  . . .
    <linkedobjects>10395<linkedobjects>
    . . .
    <parameter name=”Properties” id=”1” flags=”4112”>
      <parameter name=”Media” id=”104” flags=”65552” value=”10393” />
      . . .
    </parameter>
    . . .
  </audioTrack>
  . . .
</audio>
<footage name=”Media Layer” id=”10394”>
  <clip name=”Movie1” id=”10393”>
  . . .
  </clip>
  . . .
</footage>
```

Since many scene objects may use the same media file as their source, it may be the case that the media parameters for many `scenenode` elements reference the same `clip` element.

As the code sample above shows, the `id=` attribute (10393) for a `clip` element may be referenced by other `scenenode` or `parameter` elements. When modifying the `id=` attribute for a `scenenode` element, you may need to modify the related `scenenode` or `parameter` elements accordingly.

The `id=` attribute of a `parameter` element is used to identify a channel. You should not modify it.

[Next](The%20Properties%20Parameter.md)[Previous](Motion%20XML%20Overview.md)


---
title: Final Cut Pro X XML Format
apple_id: TP40011227
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Adjustments/Adjustments.html
archived_at: '2026-07-27T06:57:08.601567Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X XML Format](About%20Final%20Cut%20Pro%20X%20XML%201.8.md)


[Next](Metadata.md)[Previous](Resources.md)

# Adjustments and Effects

This chapter describes the FCPXML elements you use to apply adjustments and effects, alter parameters, and create animations.

## Adjustments

FCPXML supports adjustment elements to alter the audio and video output of story elements.

You can apply adjustment elements to control:

- Audible adjustments, such as audio volume and panning
- Visual adjustments, including geometrical video transformations, such as position, scale, rotation, crop, pan and zoom, blend mode, and size conforming

Each adjustment element has attributes that affect the adjustment you want to make. You specify the values to override, and all other values remain at their default settings. You can also create animated adjustments by varying attribute values over time. See [Animation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomq) for more details.

Some adjustment attributes expect a multidimensional (or compound) value, such as an (_x_,_y_) point. These attributes are specified with a space separating each value. For example, the two-dimensional values (0,0) or (10,-25) would be specified as “`0 0`” or “`10 -25`”.

__Note:__ When you work with multicam clips, audio adjustments are applied to the entire multicam clip (on the `<mc-clip>` element), while visual adjustments are applied to each angle (on the `<mc-source>` element). In FCPXML 1.3 and earlier, both visual adjustments and audio adjustments were applied to the entire multicam clip (on to the `<mc-clip>` element).

### Audible Adjustments

Audible adjustments control the audible aspects, such as volume and panning, of a story element.

__Table 4-1__  Audible adjustment elements

| Element | Description |
| `<adjust-EQ>` | Specifies the equalization applied to a clip (one of `flat`, `voice_enhance`, `music_enhance`, `loudness`, `hum_reduction`, `bass_boost`, `bass_reduce`, `treble_boost`, or `treble_reduce`). |
| `<adjust-humReduction>` | Applies hum reduction at the frequency, either `50` or `60`, specified by the `frequency` attribute. |
| `<adjust-loudness>` | Modifies the loudness using the following attributes:   - `amount`—The overall loudness amount. - `uniformity`—The dynamic range to adjust. |
| `<adjust-matchEQ>` | Specifies the equalization, in an internal format, applied to match another clip’s frequency characteristics. |
| `<adjust-noiseReduction>` | Applies noise reduction with the amount [`0..100`] specified by the `amount` attribute. |
| `<adjust-panner>` | Modifies the audio panning levels using the following attributes:   - `mode`—The pan mode; see [Pan Modes](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmznknlto) for a list of supported values. - `amount`—The pan amount. - `original_decoded_mix`—The balance between the original and decoded signals. - `ambient_direct_mix`—The balance between the decoded surround and center signals. - `surround_width`—The separation, in dB, between the decoded surround signals. - `left_right_mix`—The balance between the left and right speakers. - `front_back_mix`—The balance between the front and back speakers. - `LFE_balance`—The low-frequency effects signal. - `rotation`—The rotation amount for the surround signals. - `stereo_spread`—The stereo effect amount from the left and right channels to the center and surround speakers. - `attenuate_collapse_mix`—The panning effect amount. - `center_balance`—The balance between the center and surround signals. |
| `<adjust-volume>` | Modifies the volume of a clip in dB (for example, `-6dB`). |

### Visual Adjustments

Visual adjustments control the visual aspects of a story element, such as cropping and other geometrical transformations, and degree of stabilization or rolling shutter reduction applied to the video.

__Table 4-2__  Visual adjustment elements

| Element | Description |
| `<adjust-blend>` | Modifies the compositing blend mode and opacity percentage [`0.0..1.0`] of the visible image using the following attributes:   - `amount`—A fractional value that specifies the opacity amount (for example, `0.75`). - `mode`—An integer value corresponding to a built-in FCP X blend mode; see [Blend Modes](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmznknltk) for a list of supported values. |
| `<adjust-conform>` | Modifies the image size of a clip to fill, fit, or remain unchanged within its container’s frame size. The `type` attribute specifies the conform method to apply, which defaults to `fit`.  With the absence of this adjustment, the clip is _fit_ into the frame size. |
| `<adjust-corners>` | Modifies the corners of the visible image, adding a distort (or skew) effect using the `botLeft`, `topLeft`, `topRight`, and `botRight` attributes. These attributes are two-dimensional (_x__y_) values expressed as a percentage of frame height. |
| `<adjust-crop>` | Modifies the visible image width and height by cropping, trimming, or panning. This element has the following attributes:   - `enabled`—Enables (1, the default) or disables (0) this crop adjustment. - `mode`—Specifies the active crop mode (one of `trim`, `crop`, or `pan`). Only one crop mode is active at any given time. You define crop modes through the following child elements, whose attribute values (`left`, `top`, `right`, and `bottom`) are expressed as a percentage of the original frame height:    - `<crop-rect>`—Defines the crop values.   - `<trim-rect>`—Defines the trim values.   - `<pan-rect>`—Defines the pan and zoom animation (“Ken Burns” effect) values. |
| `<adjust-rollingShutter>` | Modifies the rolling shutter reduction applied to a clip. The `amount` attribute specifies the reduction amount, which defaults to `none`. |
| `<adjust-stabilization>` | Modifies the stabilization applied to a clip. The `type` attribute specifies the stabilization type, which defaults to `automatic`. |
| `<adjust-transform>` | Modifies the visible image by resizing, moving, or rotating using the following attributes:   - `enabled`—Enables (1, the default) or disables (0) this transform adjustment. - `position`—A two-dimensional (_x__y_) value that specifies the amount to move the frame in each dimension from its original location. These values are percentages based on the original frame height. For example, if the original frame height is 1,080 pixels, specifying `position="10 10"` moves the frame 108 pixels to the right and 108 pixels up. - `scale`—A two-dimensional (_x__y_) value that specifies the percentage amount to resize the frame in each dimension from its original frame size (for example, “`25 25`”). - `rotation`—The amount, in degrees, to rotate the frame. A positive value rotates counterclockwise and a negative value rotates clockwise (for example, `-180`). - `anchor`—A two-dimensional (_x__y_) value that offsets the origin of the video image and its center of rotation. This value is expressed as a percentage of the scaled image height and defaults to “`0 0`”. |

### 360 Adjustments

360 adjustments control the spherical aspects of a story element, such as where to place a non-360 clip in a 360 project, the viewable portion of a 360 clip in a non-360 project, and the default orientation of a 360 clip in a 360 project.

__Table 4-3__  360 adjustment elements

| Element | Description |
| `<adjust-360-transform>` | Specifies where to position a non-360 clip in a 360 project’s sphere. This element has the following attributes:   - `enabled`—Enables (1, the default) or disables (0) this orientation adjustment. - `coordinates`—Indicates whether the position of the clip is specified in cartesian coordinates or spherical coordinates. This attribute is required. - `latitude`—For spherical coordinates, the amount, in degrees, of tilt. A positive value tilts the position of the clip upward and a negative value tilts downward. - `longitude`—For spherical coordinates, the amount, in degrees, of pan. A positive value pans the position of the clip to the left and a negative value pans to the right. - `distance`—Adjusts the distance between the non-360 clip and the center of the project’s sphere. As the value increases, the non-360 clip moves farther from the center. - `xPosition`, `yPosition`, and `zPosition`—For cartesian coordinates, the position of the clip relative to the sphere of the project timeline. - `xOrientation`, `yOrientation`, and `zOrientation`—The amount, in degrees, of tilt, pan, or roll of the clip at the position in the sphere of the project determined by the coordinate parameters. - `autoOrient`—A value of 1 (the default) indicates the clip image is automatically oriented toward the view point. - `convergence`—For a stereoscopic 360 project, the value, between -1.0 and 1.0, moves the left/right eye projections relative to each other. - `interaxial`—For a stereoscopic 360 project, the value, between 0 and 1.0, specifies how much stereoscopic depth is rendered in the scene. |
| `<adjust-orientation>` | Specifies what part of a spherical clip is to be used in a non-360 project. This element has the following attributes:   - `enabled`—Enables (1, the default) or disables (0) this orientation adjustment. - `tilt`—The amount, in degrees, of tilt. A positive value tilts the view upward and a negative value tilts downward. - `pan`—The amount, in degrees, of pan. A positive value pans the view to the left and a negative value pans to the right. - `roll`—The amount, in degrees, of roll. A positive value rolls the view counter-clockwise and a negative value rolls it clockwise. - `fieldOfView`—The horizontal field of view, measured in degrees. When the value increases, you can see more of the spherical clip. |
| `<adjust-reorient>` | Reorients a spherical clip within a 360 project. It changes the direction the camera was pointing. This also assists leveling the horizon of the clip. This element has the following attributes:   - `enabled`—Enables (1, the default) or disables (0) this orientation adjustment. - `tilt`—The amount, in degrees, of tilt. A positive value tilts the camera down and a negative value tilts the camera up. - `pan`—The amount, in degrees, of pan. A positive value pans the camera right and a negative value pans the camera left. - `roll`—The amount, in degrees, of roll. A positive value rolls the camera clockwise and a negative value rolls the camera counter clockwise. - `convergence`—A positive integer that moves the left/right eye images relative to each other. A positive value moves them farther apart and a negative value moves them closer together. |

## Effects

Use filters, text styles, and transitions to apply effects to certain story elements in your events and projects. For a list of story elements, see [Table 2-1](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvoni).

### Filters

Filter effects, such as audio and video, are applied to certain story elements using the filter elements listed in Table 4-4.

__Note:__ In Final Cut Pro X 10.2, color correction behaves as other video filters do and can be inserted anywhere in a series of video filters.

__Table 4-4__  Filter elements

| Element | Description |
| `<filter-audio>` | A reference to an audio effect. |
| `<filter-video>` | A reference to a video effect. |

Refer to the Document Type Definition (DTD) for specific information on the filter types each parent element supports.

__Note:__ In FCPXML 1.3 and later, the `<filter-audio>` and `<filter-video>` elements represent audio or video filters respectively. Prior to FCPXML 1.3, a single `<filter>` element represented both audio and video filters.

In FCPXML 1.5, color filters are described with the `<filter-video>` element and its subelements. (In FCPXML 1.4 and 1.3, the `<adjust-color>` element was used.)

You apply video filters to elements that represent visual media (`<video>`, `<text>`, `<clip>`, and `<ref-clip>` elements). For multicam clips, apply the video filters on the individual angles (represented by `<mc-source>` elements).

You apply audio filters to elements that represent audible media (`<audio>`, `<clip>`, `<ref-clip>`, `<audio-source>`, and `<audio-aux-source>` elements). For multicam clips, apply the audio filters to the entire multicam clip (represented by `<mc-clip>` elements).

#### Masked Filters

A video filter can be applied to a region designated by a collection of masks. You use the `<filter-video-mask>` element to apply the masks. Table 4-5 lists the available mask elements used to define masks.

__Table 4-5__  Mask elements

| Element | Description |
| `<mask-isolation>` | Specifies a color isolation mask. |
| `<mask-shape>` | Specifies a mask for a region using a super ellipse shape. |

The mask elements are combined to define a single region to which the effect applies. The actual video filter is described with a `<video-filter>` element as a child of the `<filter-video-mask>` element.

#### Color Filters

Color correction, as well as color matching and color balance effects, are described by the `<filter-video>` element. That element references an associated `<effect>` element in the resource section that designates the particular effect. In addition to the Color Board effect, Final Cut Pro X 10.4 adds Color Curves, Color Wheel, and Hue/Saturation Curves as color correction effects.

You can apply color correction with a collection of video filter masks. The `<filter-video-mask>` element describes both the filter and the masks, and can have up to two `<filter-video>` child elements. Different color correction parameters can be applied to the inside (the first `<filter-video>` element) and the outside (the second `<filter-video>` element) of the mask.

__Note:__ Final Cut Pro X supports the American Society of Cinematographers Color Decision List (ASC CDL) format for the exchange of basic primary color grading information between equipment and software from different manufacturers.

Final Cut Pro X v10.2 and later export ASC CDL information as an XML comment (as a child of the associated `<filter-video>` element) if a color correction is applied to a clip in your project. (Prior versions of Final Cut Pro X exported ASC CDL information with the `<info-asc-cdl>` element as a child of the associated `<clip>` element.)

The ASC CDL information describes the primary color correction in ASC CDL format as three components: slope, offset, and power. Each component is represented as a vector of red, green, and blue adjustment values (for example, “`1.0 1.0 1.0`”).

The following is an example export of ASC CDL information:

```
<filter-video ref=“r1” name=“Color Correction”>
    <!-- info-asc-cdl:  slope="1.05 1.05 1.05” offset="0.0275 0.0275 0.0275” power="1.25 1.2 1”  -->
</filter-video>
```

### Transitions

A transition is an effect that combines zero (a transition that stands by itself), one, or two neighboring elements. You apply transition effects with the `<transition>` story element. The `offset` and `duration` attributes define the position and extent of the transition effect. The `<filter-video>` and `<filter-audio>` filter elements specify the effect to apply. See [Table 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomjs).

__Note:__ When an audio filter specifies an audio cross fade, the cross fade does not take effect on either side if the clip has audio specific timing set by the `audioStart` or `audioDuration` attributes. This is known as a J- or L-cut, depending on which side of the transition it occurs.

## Titles and Captions

Use the `<text>` element to describe a block of text that appears in a title or caption on a timeline. See [Table 2-1](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvoni) for `<title>` and `<caption>` elements. You can have one or more text blocks in a title or caption.

The `<text>` element can have the attributes listed in Table 4-6 when describing a caption text block.

__Table 4-6__  Text element caption attributes

| Element | Description |
| `display-style` | Specifies how a CEA caption text block appears during playback. Valid values are:   - `pop-on`—displays all text at once. - `paint-on`—displays text one character at a time as if it’s being written in real-time. - `roll-up`—displays one line of text at a time, and new lines roll up from the bottom. |
| `roll-up-height` | Specifies the number of lines to use for the roll-up animation. |
| `position` | Specifies the relative position of a CEA caption text block in the video frame (for example “`4 1`”). |
| `placement` | Specifies the relative position of an ITT subtitle text block in the video frame. Valid values are: `top`, `bottom`, `left`, and `right`. |
| `alignment` | Specifies the relative position of a CEA-608 caption text block in the video frame. Valid values are: `left`, `center`, and `right`. |

A text block can have different text styles. Use the `<text-style>` and `<text-style-def>` elements to describe the text style for each portion.

### Text Styles

Title and caption text, represented by the `<title>` and `<caption>` elements—see [Table 2-1](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvoni)—can have text styles, such as font size and alignment. You apply these styles with the elements listed in Table 4-7.

__Table 4-7__  Text style elements

| Element | Description |
| `<text-style>` | Defines the text formatting to apply to a `<title>`, `<caption>`, or `<text>` element. Use the `ref` attribute to reference a text style definition. Use the other attributes to specify the text style settings.  If a text style definition is referenced, any attributes specified in this element override the values in the text style definition. |
| `<text-style-def>` | Defines a set of text style attributes that can be shared with (referenced by) multiple `<text-style>` elements. This element has the following attributes:   - `id`—The local identifier for this text style definition. - `name`—The name for this text style definition.   Each `<text-style>` child element specifies the text style to apply. |

You use the `<text>` element to create a series of text segments in a title or caption. For each segment you can apply different text styles using the `<text-style>` element.

The following example XML uses text style definitions to create a text effect:

```
<title offset="0s" ref="r2" name="Continuous: Title with styles, including font and size." duration="10s" start="0s">
    <text>
        <text-style ref="ts1">Title with styles, including </text-style>
        <text-style ref="ts2">font</text-style>
        <text-style ref="ts1"> and </text-style>
        <text-style ref="ts3">size</text-style>
        <text-style ref="ts1">.</text-style>
    </text>
    <text-style-def id="ts1">
        <text-style font="Helvetica" fontSize="72" fontFace="Regular" fontColor="1 1 1 1" strokeColor="1 0 0 1" strokeWidth="1" alignment="center"/>
    </text-style-def>
    <text-style-def id="ts2">
        <text-style font="Capitals" fontSize="72" fontFace="Regular" fontColor="1 1 1 1" bold="1" strokeColor="1 0 0 1" strokeWidth="1" alignment="center"/>
    </text-style-def>
    <text-style-def id="ts3">
        <text-style font="Helvetica" fontSize="120" fontFace="Regular" fontColor="1 1 1 1" strokeColor="1 0 0 1" strokeWidth="1" alignment="center"/>
    </text-style-def>
</title>
```

3D text geometry and appearance are described with one or more `<param>` elements as children of the `<text-style>` element, each specifying a respective parameter.

```
<text-style-def id="ts1">
    <text-style font="Helvetica" fontSize="63" fontFace="Regular" fontColor="1 0.999974 0.999991 1" alignment="center">
        <param name="Lighting" key="527">
            <param name="Environment" key="512">
                <param name="Intensity" key="514" value="0.8"/>
                <param name="Rotation" key="516" value="0 247 0 0 (Use Rotation)"/>
                <param name="Contrast" key="517" value="62"/>
                <param name="Saturation" key="525" value="47"/>
            </param>
        </param>
        <param name="Material" key="material:Basic">
            <param name="Layer" key="layer:Finish:1 (Enamel)">
                <param name="Highlight Color" key="127" value="0.838246 0.965254 0.503887"/>
            </param>
            <param name="Layer" key="layer:Substance:3 (Plastic)">
                <param name="Type" key="4" value="0 (Shiny)"/>
                <param name="Color" key="106" value="0.813144 0.729297 0.994205"/>
            </param>
        </param>
    </text-style>
</text-style-def>
```

The following example XML represents a CEA-608 caption:

```
<caption name="CEA-608 English caption with color and underline." lane="1" offset="2225223/24000s" duration="48048/24000s"
       start="3600s" role="CEA-608?captionFormat=CEA608.en-US">
    <text position="4 1" display-style="pop-on" alignment="left">
        <text-style ref="ts1">CEA-608 English caption with</text-style>
        <text-style ref="ts3">color</text-style>
        <text-style ref="ts1"> and </text-style>
        <text-style ref="ts4">underline</text-style>
        <text-style ref="ts1">.</text-style>
    </text>
    <text-style-def id="ts1">
        <text-style fontFace="Regular" fontColor="1 1 1 1" backgroundColor="0 0 0 1"/>
    </text-style-def>
    <text-style-def id="ts3">
        <text-style fontFace="Regular" fontColor="0 0 1 1" backgroundColor="0 0 0 1"/>
    </text-style-def>
    <text-style-def id="ts4">
        <text-style fontFace="Regular" fontColor="1 1 1 1" backgroundColor="0 0 0 1" underline="1"/>
    </text-style-def>
</caption>
```

The following example XML represents an ITT subtitle:

```
<caption name="Belgian French subtitle with color and bold style." lane="1" offset="29029/300s" duration="48048/24000s"
       start="3600s" role="My ITT?captionFormat=ITT.fr-BE">
    <text placement="bottom">
        <text-style ref="ts5">Belgian French subtitle with </text-style>
        <text-style ref="ts6">color</text-style>
        <text-style ref="ts5"> and </text-style>
        <text-style ref="ts7">bold style</text-style>
        <text-style ref="ts5">.</text-style>
    </text>
    <text-style-def id="ts5">
        <text-style fontFace="Regular" fontColor="1 1 1 1" backgroundColor="0 0 0 1"/>
    </text-style-def>
    <text-style-def id="ts6">
        <text-style fontFace="Regular" fontColor="1 0.684918 0.63397 1" backgroundColor="0 0 0 1"/>
    </text-style-def>
    <text-style-def id="ts7">
        <text-style fontColor="1 1 1 1" bold="1" backgroundColor="0 0 0 1"/>
    </text-style-def>
</caption>
```

## Adjustment Attributes and Effect Parameters

You can specify the value of certain adjustment attributes and effect parameters and change them for the entire duration of the parent element. You do this by adding a parameter (`<param>`) element for each adjustment attribute or effect parameter you would like to change.

You can also use the `<param>` element to create keyframe animations by changing adjustment attributes and effect parameters over time. See [Animation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomq) for more details.

The following elements may contain `<param>` child elements:

- Adjustment elements—`<adjust-blend>`, `<adjust-corners>`, `<adjust-EQ>`, `<adjust-panner>`, `<adjust-stabilization>`, `<adjust-transform>`, `<adjust-volume>`, `<crop-rect>`, and `<trim-rect>`
- Effect elements—`<filter-audio>` and `<filter-video>`
- Story elements—`<title>` and `<video>`

The `<param>` element attributes are defined in Table 4-8.

__Table 4-8__  Parameter element attributes

| Attribute | Description |
| `name` | For adjustments, this case-sensitive string identifies the parent attribute to override. For an effect parameter, this is for informational purposes only. |
| `key` | A string that identifies a parameter in the effect implementation. This is ignored when the `<param>` element is used for an adjustment. |
| `value` | The new value to apply to the adjustment attribute (optional) or the effect parameter. This value overrides the value specified by the parent adjustment attribute. |

For example, the following XML adjusts the audio volume of a clip by –3dB:

```
<audio>
    <adjust-volume>
        <param name="amount" value="-3dB"/>
    </adjust-volume>
</audio>
```

Some adjustments and effects allow preserving parameter information in an internal binary format using the `<data>` element.

__Table 4-9__  Data element

| Element | Description |
| `<data>` | Specifies binary parameter data. |

Some effect parameters allow structured data. This information is represented with a series of nested `<param>` elements as children of the effect parameter you want to override. See the _Lighting_ parameter of the 3D text XML snippet in the [Text Styles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomrq) section for an example.

## Animation

Create animations by changing certain adjustment attributes and effect parameters over time. You do this by adding a `<param>` element—see [Adjustment Attributes and Effect Parameters](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvonq)—and the keyframe related elements, for each adjustment attribute or effect parameter you want to override. Table 4-10 describes the keyframe animation elements.

__Table 4-10__  Keyframe animation elements

| Attribute | Description |
| `<keyframe>` | Specifies a keyframe point along an animation path. This element has the following attributes:   - `curve`—Specifies whether the interpolated values around the keyframe are linear or smooth. The default is `smooth`. - `interp`—The animation speed over the keyframe. The default is `linear`. - `time`—The keyframe time (for example, “`0s`”). - `value`—The keyframe value (for example, “`-5 10`”). |
| `<keyframeAnimation>` | Specifies an animation path using points described by child `<keyframe>` elements. |

To produce a keyframe animation, you specify the time points and values for each keyframe using the `time` and `value` attributes of the `<keyframe>` element. The Final Cut Pro X application interpolates the values between them.

The following example performs a position and scale transform adjustment animation using keyframes:

```
<adjust-transform position="-10 10">
    <param name="position">
        <keyframeAnimation>
            <keyframe time="0s" value="-5 10"/>
            <keyframe time="10s" value="10 20"/>
        </keyframeAnimation>
    </param>
    <param name="scale">
        <keyframeAnimation>
            <keyframe time="0s" value="1 1"/>
            <keyframe time="10s" value="0.75 0.75"/>
        </keyframeAnimation>
    </param>
</adjust-transform>
```

Initially, at `time=0s`, the frame is moved left 5 percent and up 10 percent (“`-5 10`”) of the project’s height from the original location, with no change in size (“`1 1`”). At `time=10s`, the frame has moved 10 percent right and 20 percent up (“`10 20`”) of the project’s height from the original location, with a 25 percent (“`0.75 0.75`”) reduction in size from the original (“`1 1`”). See [Table 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomy) for more information on the `<adjust-transform>` element.

Final Cut Pro X determines the parameter value based on the following priority (with 1 being the highest priority):

1. The `value` and `time` attributes of the `<keyframe>` element (for a particular time)
2. The `value` attribute of the `<param>` element
3. The respective attribute of the adjustment, if applicable

In the previous example, it does not matter that the `position` attribute of the `<adjust-transform>` element has a value of “`-10 10`” because the keyframe defined at `time=0s` (in the `<keyframe>` element) takes priority and overrides the value to “`-5 10`”.

[Next](Metadata.md)[Previous](Resources.md)

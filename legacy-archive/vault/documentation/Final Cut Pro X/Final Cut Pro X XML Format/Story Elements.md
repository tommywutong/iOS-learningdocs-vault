---
title: Final Cut Pro X XML Format
apple_id: TP40011227
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/StoryElements/StoryElements.html
archived_at: '2026-07-27T06:57:08.505438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X XML Format](About%20Final%20Cut%20Pro%20X%20XML%201.8.md)


[Next](Resources.md)[Previous](FCPXML%20Concepts.md)

# Story Elements

Story elements are the building blocks of your Final Cut Pro X events and projects.

## Structure

An `<event>` element or `<project>` element may include the story elements listed in Table 2-1.

__Table 2-1__  Story elements

| Element | Description |
| `<clip>` | A container for editing or compositing media and other story elements. |
| `<asset-clip>` | A clip referencing a single media asset.  The `start` and `duration` attributes apply to all media components in the asset.  The `audio-role` and `video-role` attributes specify the main role. Subroles are generated using the main role name followed by a numerical suffix, for example `dialogue.dialogue-1`, `dialogue.dialogue-2` and so on. |
| `<sync-clip>` | A clip whose contained and anchored items are synchronized. The `<sync-source>` element describes the audio components for the synchronized clip. |
| `<audio>` | A reference to audio data from an `<asset>` or `<effect>`. Attributes include:   - `role`—Assigns a role to the audio media component. Format is _main-role.subrole_. - `srcID`—References the specific audio source (or track) in the asset. The default is `1`. - `srcCh`—Identifies specific audio source channels in the asset. Value is a comma-separated series of 1-based channel indices. - `outCh`—Specifies output channels to send the audio. Value is a comma-separated series of channel tags: `L`, `R`, `C`, `LFE`, `Ls`, `Rs`, and `X`.   See [Audio Components](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvona) for more information. |
| `<video>` | A reference to video data from an `<asset>` or `<effect>`. Attributes include:   - `role`—Assigns a role to the video media component. Format is _main-role.subrole_. - `srcID`—References the specific video source in the asset. The default is `1`. |
| `<mc-clip>` | A reference to audio/video data from a `<multicam>` media source. |
| `<ref-clip>` | A reference to audio/video data from a `<sequence>` media source. |
| `<gap>` | A placeholder element with no intrinsic audio or video data. |
| `<transition>` | An effect that combines zero, one, or two neighboring elements. |
| `<title>` | A title with custom text elements.  The `role` attribute assigns a role to the underlying media component. Format is _main-role.subrole_. |
| `<caption>` | A caption/subtitle with custom text elements.  The `role` attribute assigns a role to the underlying media component. Format is _role-name_`?captionFormat=`_captionFormat.subrole_.  See [Roles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomrq) for more information. |
| `<spine>` | A container that schedules elements sequentially in time. |
| `<audition>` | A container of alternative elements, exactly one of which is currently active.  When exported, the XML lists the currently active item as the first child in the audition container. |
| `<sequence>` | A container representing the top-level sequence for a Final Cut Pro X project or compound clip. |

You can _anchor_ one or more other elements to each story element. An anchored item has a positive or negative `lane` index that positions the item either above or below its base element in the timeline.

For video elements, lane order also implies compositing order—items with higher lane indexes composite over elements with lower lane indexes. For audio elements, lane order does not affect compositing. Items that reside inside (rather than above or below) a container are called _contained items_ and have an implied lane index of zero.

Events and projects can also contain filters that apply effects to certain elements. See [Effects](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvooi).

### Timeline

The `<sequence>` and `<clip>` story elements, and the `<multicam>` media element create a new timeline and use the attributes listed in Table 2-2 to define its characteristics.

__Table 2-2__  Timeline attributes

| Attribute | Description |
| `format` | A reference to the video format defined by the `<format>` element. |
| `tcFormat` | The timecode display format, either drop frame (`DF`) or nondrop frame (`NDF`, the default). |
| `tcStart` | The timecode origin represented as a time value. See [Timing Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomq). |

The `<sequence>` element can also contain the attributes in Table 2-3 to define the audio characteristics of the new timeline:

__Table 2-3__  Timeline audio attributes

| Attribute | Description |
| `audioLayout` | The audio channel layout, one of `mono`, `stereo` (the default), or `surround`. |
| `audioRate` | The audio sample rate (one of `32k`, `44.1k`, `48k`, `88k`, `96k`, `176.4k`, or `192k`); the default is `48k`. |

__Note:__ The `audioLayout` attribute for the top-level `<sequence>` element in a project must be either `stereo` or `surround`.

When audio in a project timeline is rendered to an export output, channels from each audio component are assigned to channels defined by the `audioLayout` attribute of the `<sequence>` element. Some rules are:

- For a mono component, the audio is split into two channels for a stereo layout, or assigned to the center channel if the layout is surround.
- For a stereo component, the audio is mixed for a mono layout, or assigned to the left and right channels for surround.
- For a surround component, the audio is mixed down as appropriate for a stereo or mono layout.

### Annotations and Notes

Events and projects can contain the annotations (keyword, markers, and so on) in Table 2-4. Many story elements can contain annotations over a range of time, specified with the `start` and `duration` attributes.

__Table 2-4__  Annotation elements

| Element | Description |
| `<keyword>` | An annotation that applies a keyword to a range of time. |
| `<marker>` | An annotation (with optional _to-do_ flag) that applies a text marker to a range of time. |
| `<chapter-marker>` | An annotation that applies to a range of time and indicates a chapter. |
| `<analysis-marker>` | An annotation that indicates the result of scene analysis to determine the number of people present and the shot and stabilization types. |
| `<rating>` | A `favorite` or `reject` annotation that applies to a range of time. |

Descriptive notes apply to an entire element and are defined by the `<note>` element.

__Table 2-5__  Note element

| Element | Description |
| `<note>` | An annotation that applies to an entire element. |

### Roles

Final Cut Pro X allows users to assign a role to a media component to distinguish the nature of the media component from other components. Use the `role` attribute of the `<video>`, `<audio>`, `<title>`, and `<caption>` elements to assign the element a role. The `role` attribute format is _main-role.sub-role_.

For captions, the main role must include the caption format in the following form:

```
roleName?captionFormat=captionFormat
```

The subrole must reflect the particular language tag (and optional region tag) for the caption role, for example, `en` or `en-US`.

Table 2-6 provides details on these values.

__Table 2-6__  Caption role value components

| Component | Description |
| _roleName_ | The caption role name. This component:   - Must not contain the `“.”` or `“?”` characters - Must not be only an `“_”` character   __Note:__ The caption role name can be edited by the user in the Role Editor. |
| _captionFormat_ | The caption format. Valid values are: `ITT` or `CEA608`. |
| _sub-role_ | The language tag (and optional region tag) for the subrole.  Only a subset of language tags are supported by Final Cut Pro X. Unsupported language tags are automatically mapped to `en` (i.e., English).  Language codes are formatted according to RFC 5646 (a part of BCP 47). |

The following are some caption role examples:

- `"ITT Subtitles?captionFormat=ITT.en"`—The English language subrole of an ITT format caption role named `ITT Subtitles`.
- `"My Subtitles?captionFormat=ITT.fr-CA"`—The French (Canada) language subrole of an ITT format caption role named `My Subtitles`.
- `"CEA-608 Captions?captionFormat=CEA608.it"`—The Italian language subrole of a CEA608 format caption role named `CEA-608 Captions`.

## Timing Attributes

Each story element has up to three time values, listed in Table 2-7, that you use to schedule the element (and its contained or anchored items) in a timeline.

__Table 2-7__  Time value attributes

| Attribute | Description |
| `offset` | An element’s location in parent time (or base element’s time for an anchor). |
| `duration` | An element’s extent in parent time. |
| `start` | The start of an element’s local timeline (to schedule its contained and anchored items). |

The time range for contained items is limited by their parent. The time range for anchored items is not limited by their parent; however, anchored items may be limited by an ancestor that either directly or indirectly contains the parent.

Time values are expressed as a rational number of seconds with a 64-bit numerator and a 32-bit denominator. Frame rates for NTSC-compatible media, for example, use a frame duration of `1001/30000s` (29.97 fps) or `1001/60000s` (59.94 fps). If a time value is equal to a whole number of seconds, the fraction may be reduced into whole seconds (for example, `5s`).

Timing attribute values are expected to be a multiple of the frame duration for the respective timeline. Otherwise, Final Cut Pro X has to insert a gap to maintain the specified timing upon import. A warning message appears when this happens.

### Time Maps

Use a time map to adjust, or remap, the playback speed of an element. A time map is defined with the `<timeMap>` element, which contains one or more `<timept>` elements that specify the new timing. The parent element’s playback speed is adjusted over a range of time using points on a curve to interpolate values. For example, if the local time range for a clip is originally 0-5s, then the time map for playing this clip at 50 percent speed, followed by playback at -50 percent speed, might look as follows:

```
<timeMap>
    <timept time="0s" value="0s" interp="linear"/>
    <timept time="10s" value="5s" interp="linear"/>    <!-- In 0-10s, play the original 0-5s -->
    <timept time="20s" value="0s" interp="linear"/>    <!-- In 10-20s, play the original 5-0s -->
</timeMap>
```

A time map affects only an element’s own duration and the offsets of the element’s anchored items; it does not modify the offsets of the element’s contained items (such as items with `lane=0`).

### Rate Conforming

When the timeline frame rate and the media frame rate are certain combinations (see Table 2-8), Final Cut Pro X automatically applies rate conforming by converting the media frame rate to match the timeline frame rate. As a result, the duration is also adjusted. When this occurs, the Rate Conform section appears in the application’s Video Inspector. You use the `<conform-rate>` element to indicate rate conforming.

__Note:__ In FCPXML 1.2, rate conforming was applied using a `<timeMap>` element with a `rateConform` attribute value of `1`.

Table 2-8 illustrates how Final Cut Pro X applies rate conforming.

__Table 2-8__  Rate conforming

| Media  frame  rate | __Timeline frame rate__ | | | | |
| 23.98p | 24p | 25p  25i  50p | 29.97p  59.94p  29.97i | 30p  60p |
| 23.98p | - | 24p | 25p | - | - |
| 24p | 23.98p | - | 25p | - | - |
| 25p | 23.98p | 24p | - | - | - |
| 29.97p | - | - | - | - | 30p |
| 30p | - | - | - | 29.97p | - |
| 50p | 47.96p | 48p | - | - | - |
| 59.94p | - | - | - | - | 60p |
| 60p | - | - | - | 59.94p | - |
| 25i | 47.96p | 48p | - | - | - |
| 29.97i | - | - | - | - | 60p |

### Frame Sampling

Final Cut Pro X uses frame sampling to adjust playback speed for time maps and rate conforming. The `frameSampling` attribute accepts one of `floor`, `nearest-neighbor`, `frame-blending`, `optical-flow-classic`, or `optical-flow`. If both time maps and rate conforming are used on the same clip, the frame sampling method must be the same.

__Note:__ The Final Cut Pro X UI uses the term _retime_ to refer to a time map.

## Audio Components

For clips with audio, you use the elements listed in Table 2-9 and their attributes listed in [Table 2-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomrr) to specify the configuration of an audio component, such as:

- Enabling/Disabling the component
- Mute ranges
- Volume, and other audio adjustments
- Audio filters
- Roles
- Channel mapping

__Table 2-9__  Audio component elements

| Element | Description |
| `<audio-channel-source>` | Defines an audio component by its source channels. |
| `<audio-role-source>` | Defines an audio component by its role. |
| `<mute>` | Suppresses audio output for the audio component over a range of time. |

The `<audio-channel-source>` element defines an audio component for `<clip>` and `<asset-clip>` elements in terms of source channels in the underlying assets. The `<audio-role-source>` element defines an audio component for `<ref-clip>` and `<mc-clip>` elements in terms of roles assigned in a compound clip or a multicam clip.

You can use the `<mute>` element (see [Table 2-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomjr)), `<filter-audio>` element (see [Filters](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomjy)), or other audible adjustments (see [Audible Adjustments](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomjv)) as children of the `<audio-channel-source>` or `<audio-role-source>` elements to specify mute ranges or audio effects.

The `<audio-channel-source>` and `<audio-role-source>` elements use the attributes listed in Table 2-10 to define their configuration.

__Table 2-10__  Audio component attributes

| Element | Description |
| `role` | Assigns a role to the audio component for `<audio-channel-source>`. Specifies the role in the underlying media the audio component represents for `<audio-role-source>`. |
| `start` | The start time for the audio component. If absent, the start time is derived based on the parent container timing. |
| `duration` | The duration of the audio component. If absent, the duration is derived based on the parent container timing. |
| `active`\* | Specifies whether the audio component is active (1, the default) or inactive (0). If inactive, the audio component no longer participates in the audio mix and is no longer displayed in the timeline (the data is preserved). |
| `enabled`\* | Specifies whether the audio component is enabled (1, the default) or disabled (0). |
||  |  |
| --- | --- |
| \* An audio component can be both active and disabled. In this case the audio component data remains in the project and can be enabled when needed. | |

The `<audio-channel-source>` element uses the attributes listed in Table 2-11 to define its audio channel configuration.

__Table 2-11__  Audio channel attributes

| Element | Description |
| `srcCh` | The audio source channels in the containing `<clip>` element, such as `"1, 2"`. Channels from underlying assets are sorted by their `srcID` and then by their `srcCh`. |
| `outCh` | An indication of how the audio source channels are assigned to the output, such as `"L, R"`. |

In Listing 2-1, the audio on the primary timeline is reconfigured as dual mono, while the audio on the anchored item is mapped to reverse stereo. Additionally, the last 1 second of the anchored audio is muted. The two mono audio components on the primary timeline get their roles assigned as `dialogue.dialogue-1` and `dialog.dialogue-2`, while the reverse stereo audio component in the anchored item gets its role assigned as `music.music-1`.

__Listing 2-1__  Audio component by source channels

```
<asset-clip name="MyVideo" ref="r2" start="0s" duration="5s" audioRole="dialogue">
    <asset-clip name="MyAudio" ref="r3" lane="-1" start="10s" duration="5s" audioRole="music">
        <audio-channel-source role="music.music-1" srcCh="2, 1">
            <mute start="14s" duration="1s"/>
        </audio-channel-source>
    </asset-clip>
    <audio-channel-source role="dialogue.dialogue-1" srcCh="1"/>
    <audio-channel-source role="dialogue.dialogue-2" srcCh="2"/>
</asset-clip>
```

### Audio Components in Compound Clips

When you reference a compound clip in a timeline, you can manipulate its audio components by roles. By default, components from the compound clip with the same main role are merged into a single component. You can override this behavior to see the individual subroles by setting the `<ref-clip>` element’s `useAudioSubroles` attribute to 1.

In Listing 2-2, the `<ref-clip>` element references a compound clip, created from the clip in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomjt). Because the `useAudioSubroles` attribute is set to `1`, all subroles are accessible. The two components with the `dialogue` subroles have the `Rumble Reducer` effect applied on each. The volume on the component with the `music.music-1` subrole is turned down by `6dB`.

__Listing 2-2__  Audio component from a compound clip

```
<ref-clip name="MyCompoundClip" ref="r1" duration="5s" useAudioSubroles="1">
    <audio-role-source role="dialogue.dialogue-1">
        <filter-audio ref="r6" name="Rumble Reducer"/>
    </audio-role-source>
    <audio-role-source role="dialogue.dialogue-2">
        <filter-audio ref="r6" name="Rumble Reducer"/>
    </audio-role-source>
    <audio-role-source role="music.music-1">
        <adjust-volume amount="-6dB"/>
    </audio-role-source>
</ref-clip>
```

[Next](Resources.md)[Previous](FCPXML%20Concepts.md)

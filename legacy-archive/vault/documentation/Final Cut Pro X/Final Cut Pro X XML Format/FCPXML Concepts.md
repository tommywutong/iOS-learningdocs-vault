---
title: Final Cut Pro X XML Format
apple_id: TP40011227
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/EventsandProjects/EventsandProjects.html
archived_at: '2026-07-27T06:57:08.466957Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X XML Format](About%20Final%20Cut%20Pro%20X%20XML%201.8.md)


[Next](Story%20Elements.md)[Previous](About%20Final%20Cut%20Pro%20X%20XML%201.8.md)

# FCPXML Concepts

Here is a list of Final Cut Pro X terms you’ll encounter throughout this document:

- A _clip_ is a reference to media, such as a video, audio, or still image file, that allows you to edit and annotate the media without directly modifying it. A clip controls which portions of the media you would like to use, and it allows you to organize the media based on keywords you have applied. Clips can also contain other clips to represent composite media.
- Use a Final Cut Pro X _project_ and its primary container, a _sequence_, to build a finished movie. The sequence defines your movie’s final appearance. You build a sequence by bringing clips into it from one or more events, or by creating new clips within the sequence. You adjust and arrange the clips, along with other story elements in the sequence, to produce your movie. Every clip in a project is unique to that project (not shared), but referenced media always resides in an event and may be shared across more than one project.
- Use a Final Cut Pro X _event_ to store and organize clips and projects. You can import media files into a new or existing event. You can copy these files into an event’s own media folder, or reference them in their original locations. Final Cut Pro X tracks each imported file as an asset and ensures your event contains at least one clip per asset.
- Use a Final Cut Pro X _library_ to organize your events. The library is a container that you use to keep track of all events, projects, and media related to your work.

Refer to [Final Cut Pro X Help](http://help.apple.com/finalcutpro/) for more information on Final Cut Pro X concepts.

## Document Structure

An FCPXML document represents one of the following Final Cut Pro X objects:

- A single library.
- A set of events.
- A set of clips, which may contain keywords or smart collections.

Refer to [Importing XML](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvomju) for FCPXML examples.

The root top-level container element is `<fcpxml>`. The root element contains the following:

- An optional `<import-options>` element. See [Import Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvooa).
- A `<resources>` element. See [Resources](Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomi).
- One of the following:

  - A `<library>` element. A `<library>` element contains a list of `<event>` elements (see [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvomjr)).

    __Note:__ As of FCPXML 1.4, an FCPXML document is _self-contained_ and allows multiple events, but does not allow references to objects in another library.
  - Or, a series of `<event>` elements. An `<event>` element contains story elements and `<project>` elements discussed in the following bullet (see [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvomjr)).
  - Or, a combination of story elements and `<project>` elements:

    - Story elements: `<clip>`, `<audition>`, `<mc-clip>`, `<ref-clip>`, `<sync-clip>`, or `<asset-clip>`. See [Story Elements](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomi).
    - A `<project>` element representing a timeline in a Final Cut Pro X project. A `<project>` element contains a `<sequence>` element (see [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvomjr) and [Table 2-1](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvoni)).

      __Note:__ As of FCPXML 1.4, the `<project>` element now only defines a project timeline; events are now represented by an `<event>` element.
    - Collection elements: `<smart-collection>`, `<keyword-collection>`, or `<collection-folder>`. See [Collections](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvony).

Some of the child elements that appear under the `<fcpxml>` element are summarized in Table 1-1, while others are listed in [Table 2-1](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvoni).

__Table 1-1__  Descendants of the `<fcpxml>` element

| Element | Description |
| `<event>` | A single event in a library. The `name` attribute specifies the name of the event. |
| `<import-options>` | A container for options related to importing events and projects. See [Import Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvooa). |
| `<library>` | A single library. This element has the following attributes:   - `colorProcessing`—Specifies whether the library supports `standard`, `wide`, or `wide-hdr` color gamut. The default is `standard`. - `location`—Specifies the URL of the library on export, but is ignored during import. Refer to the `library location` import option in [Import Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvooa). |
| `<project>` | A project timeline. The `name` attribute specifies the name of the project. |
| `<resources>` | A container for relevant data that events and projects depend on, such as media assets, video formats, and effects. See [Resources](Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomi) for details on the supported resource types. |

## Collections

An event may group clips into keyword and smart collections, and a library may group clips into smart collections. Collections are represented by the elements in Table 1-2 as children of the `<event>` or `<library>` element.

__Note:__ Only `<smart-collection>` elements can appear as child elements of the `<library>` element.

__Table 1-2__  Collection elements

| Element | Description |
| `<collection-folder>` | A container to group other collection elements. |
| `<keyword-collection>` | Group clips and projects based on matching keywords. |
| `<smart-collection>` | Group clips and projects matching various search criteria. Matching criteria elements are listed in [Table 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvomjq). |

Smart collections use the elements listed in Table 1-3 to specify matching criteria for grouping clips and projects.

__Table 1-3__  Smart collection match elements

| Element | Description |
| `<match-clip>` | Match clips based on type (one of `audition`, `synchronized`, `compound`, `multicam`, `layeredGraphic`, or `project`). |
| `<match-keywords>` | Match clips based on assigned keywords. |
| `<match-media>` | Match clips or projects based on media type (one of `audioOnly`, `stills`, `videoOnly`, or `videoWithAudio`). |
| `<match-property>` | Match clips or projects based on media format and metadata properties. |
| `<match-ratings>` | Match clips based on assigned ratings. |
| `<match-roles>` | Match clips based on assigned roles. |
| `<match-shot>` | Match clips based on assigned shot type. |
| `<match-stabilization>` | Match clips based on the stabilization type. |
| `<match-text>` | Match clips or projects based on the specified text. |
| `<match-time>` | Match clips or projects created or imported based on a specific date. |
| `<match-timeRange>` | Match clips or projects created or imported based on a range of time. |

## Importing XML

You can import an FCPXML document into Final Cut Pro X in the following ways:

- Choose File > Import XML from the Final Cut Pro X menu and specify the library where the FCPXML is imported into.
- Double-click an FCPXML document in Finder. You can specify the library to import into using the Final Cut Pro X Library chooser dialog. Alternatively, the FCPXML document itself can specify the library using the `library location` import option. See [Import Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvooa).
- Sent from another application. You can specify the library to import into using the Final Cut Pro X Library chooser dialog. Alternatively the FCPXML document itself can specify the library using the `library location` import option. See [Import Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvooa).
- Drag-and-drop objects from another application. The dragged objects are imported into the drop target in the Final Cut Pro X application. The types of dragged objects determine where you can drop them. See _[Final Cut Pro X Workflows Developer Guide](../Final%20Cut%20Pro%20X%20Workflows%20Developer%20Guide/About%20Final%20Cut%20Pro%20X%20Workflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobr)_ for more information.

### Importing a Library

Listing 1-1 shows FCPXML representing a library.

__Listing 1-1__  A library with a simple project as FCPXML

```
<fcpxml version="1.7">
    <!-- Resources -->
    <resources>
        <asset id="r1" src="file:///Volumes/Media/MyMovie.mov" start="0s" duration="10s" hasVideo="1" hasAudio="1" format="r2" audioSources="1" audioChannels="2" audioRate="48000"/>
        <format id="r2" name="FFVideoFormat1080p30"/>
    </resources>
    <library>
        <!-- Events -->
        <event name="MyEvent">
            <project name="MyProject">
                <!-- Project Story Elements -->
                <sequence format="r2">
                    <spine>
                        <asset-clip name="MyMovie" ref="r1" start="0s" duration="5s" audioRole="dialogue"/>
                    </spine>
                </sequence>
            </project>
            <!-- Clips -->
            <asset-clip name="MyMovie" ref="r1" format="r2" duration="5s" audioRole="dialogue"/>
        </event>
    </library>
</fcpxml>
```

In Listing 1-1, the library has an event named `MyEvent` that in turn has a project named `MyProject`. The `MyProject` project uses two resources:

- A reference to an external asset located at `/Volumes/Media/MyMovie.mov`
- A built-in video format, `FFVideoFormat1080p30`

When Final Cut Pro X imports the FCPXML in Listing 1-1, it:

- Creates a new event called `MyEvent` in the library the user chooses. If an event named `MyEvent` already exists in the chosen library, Final Cut Pro X imports the project into that event.
- Imports `MyMovie.mov` into `MyEvent` by either copying or linking, depending on the application preference, and creates a browser clip referencing the imported asset.
- Creates a new project called `MyProject` with a sequence using a 1080p, 30 fps video format specified by `FFVideoFormat1080p30`. If a project named `MyProject` already exists in the event named `MyEvent`, Final Cut Pro X asks whether you want to create a new project or replace the existing project. Creating a new project appends a numerical suffix to the project name, for example `MyProject 1`.

  __Note:__ The choice you make regarding whether to create or replace projects is applied to all conflicts detected during the import.
- Inserts the first 5 seconds of video and audio from `MyMovie.mov` into the project timeline.

### Importing Events

Listing 1-2 shows FCPXML representing an event.

__Listing 1-2__  An event with multiple clips as FCPXML

```
<fcpxml version="1.7">
    <!-- Resources -->
    <resources>
        <format id="r1" name="FFVideoFormat1080p30"/>
        <asset id="r2" src="file:///Volumes/Media/MyMovie1.mov" start="0s" duration="10s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000"/>
        <asset id="r3" src="file:///Volumes/Media/MyMovie2.mov" start="0s" duration="20s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000"/>
        <asset id="r4" src="file:///Volumes/Media/MyMovie3.mov" start="10s" duration="40s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000"/>
    </resources>
    <!-- Events -->
    <event name="MyEvent">
        <!-- Clips -->
        <asset-clip name="MyMovie1" ref="r2" format="r1" duration="5s" audioRole="dialogue"/>
        <asset-clip name="MyMovie2" ref="r3" format="r1" duration="15s" audioRole="dialogue"/>
        <asset-clip name="MyMovie3" ref="r4" format="r1" duration="30s" audioRole="dialogue"/>
    </event>
</fcpxml>
```

In Listing 1-2, the event `MyEvent` uses these resources:

- Three external assets named `MyMovie1.mov`, `MyMovie2.mov`, and `MyMovie3.mov` located at `/Volumes/Media/`
- A built-in video format, `FFVideoFormat1080p30`

When Final Cut Pro X imports this FCPXML, it:

- Creates a new event called `MyEvent` in the library you choose. If an event named `MyEvent` already exists in the chosen library, Final Cut Pro X imports the clips into that event.
- Imports `MyMovie1.mov`, `MyMovie2.mov`, and `MyMovie3.mov` into `MyEvent` by either copying or linking, depending on the application preference.
- Creates three clips (`MyMovie1`, `MyMovie2`, and `MyMovie3`) containing audio and video data from the imported media and using a 1080p, 30 fps video format specified by `FFVideoFormat1080p30`. If a clip already exists, with the same name in the event named `MyEvent`, Final Cut Pro X asks whether you want to create a new clip or replace the existing clip. Creating a new clip appends a numerical suffix to the clip name, for example, `MyMovie1 1`.

  __Note:__ The choice you make regarding whether to create or replace projects is applied to all conflicts detected during the import.

### Importing Clips

Listing 1-3 shows FCPXML representing a group of clips.

__Listing 1-3__  A group of clips as FCPXML

```
<fcpxml version="1.7">
    <!-- Resources -->
    <resources>
        <format id="r1" name="FFVideoFormat1080p30"/>
        <asset id="r2" src="file:///Volumes/Media/MyMovie1.mov" start="0s" duration="10s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000"/>
        <asset id="r3" src="file:///Volumes/Media/MyMovie2.mov" start="0s" duration="20s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000"/>
        <asset id="r4" src="file:///Volumes/Media/MyMovie3.mov" start="10s" duration="40s" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000"/>
    </resources>
    <!-- Clips -->
    <asset-clip name="MyMovie1" ref="r2" format="r1" duration="5s" audioRole="dialogue"/>
    <asset-clip name="MyMovie2" ref="r3" format="r1" duration="15s" audioRole="dialogue"/>
    <asset-clip name="MyMovie3" ref="r4" format="r1" duration="30s" audioRole="dialogue"/>
</fcpxml>
```

In Listing 1-3, the group of clips uses these resources:

- Three external assets named `MyMovie1.mov`, `MyMovie2.mov`, and `MyMovie3.mov` located at `/Volumes/Media/`
- A built-in video format, `FFVideoFormat1080p30`

When Final Cut Pro X imports this FCPXML, it:

- Creates a new event using the current date, such as `10-17-16`, as the name in the library you choose. If there is already an event with that name in the chosen library, Final Cut Pro X creates another event in the library and appends a numerical suffix to the name, such as `10-17-16 1`.
- Imports `MyMovie1.mov`, `MyMovie2.mov`, and `MyMovie3.mov` into the new event by either copying or linking, depending on the application preference.
- Creates three clips (`MyMovie1`, `MyMovie2`, and `MyMovie3`) containing audio and video data from the imported media and using a 1080p, 30 fps video format specified by `FFVideoFormat1080p30`.

### Importing Collections

Listing 1-4 shows FCPXML representing an event with collections.

__Listing 1-4__  An event with collections as FCPXML

```
<fcpxml version="1.7">
    <!-- Resources -->
    <resources>
        <format id="r1" name="FFVideoFormat1080p30"/>
        <asset id="r2" name="MyMovie1" src="file:///Volumes/Media/MyMovie1.mov" start="0s" duration="10s" hasVideo="1" format="r1" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"/>
        <asset id="r3" name="MyMovie2" src="file:///Volumes/Media/MyMovie2.mov" start="0s" duration="20s" hasVideo="1" format="r1" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"/>
        <asset id="r4" name="MyMovie3" src="file:///Volumes/Media/MyMovie3.mov" start="10s" duration="40s" hasVideo="1" format="r1" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"/>
    </resources>
    <event name="MyEvent">
        <!-- Clips -->
        <asset-clip name="MyMovie1" ref="r2" duration="10s" audioRole="dialogue" format="r1">
            <keyword start="5s" duration="2s" value="MyKeyword1"/>
        </asset-clip>
        <asset-clip name="MyMovie2" ref="r3" duration="20s" audioRole="dialogue" format="r1">
            <keyword start="3s" duration="12s" value="MyKeyword2"/>
        </asset-clip>
        <asset-clip name="MyMovie3" ref="r4" duration="40s" start="10s" audioRole="dialogue" format="r1">
            <keyword start="45s" duration="5s" value="MyKeyword3"/>
        </asset-clip>
        <!-- Collections -->
        <keyword-collection name="MyKeyword1"/>
        <keyword-collection name="MyKeyword2"/>
        <keyword-collection name="MyKeyword3"/>
    </event>
</fcpxml>
```

In Listing 1-4, the event `MyEvent` uses these resources:

- Three external assets named `MyMovie1.mov`, `MyMovie2.mov`, and `MyMovie3.mov` located at `/Volumes/Media/`
- A built-in video format, `FFVideoFormat1080p30`

When Final Cut Pro X imports this FCPXML, it:

- Creates a new event called `MyEvent` in the library you choose. If an event named `MyEvent` already exists in the chosen library, Final Cut Pro X imports the collection into that event.
- Imports `MyMovie1.mov`, `MyMovie2.mov`, and `MyMovie3.mov` into `MyEvent` by either copying or linking, depending on the application preference.
- Creates three clips (`MyMovie1`, `MyMovie2`, and `MyMovie3`) containing audio and video data from the imported media and using a 1080p, 30 fps video format specified by `FFVideoFormat1080p30`.
- Adds keywords (`MyKeyword1`, `MyKeyword2`, and `MyKeyword3`) over the specified time range to the respective clips.
- Creates keyword collections (`MyKeyword1`, `MyKeyword2`, and `MyKeyword3`) in `MyEvent`.

## Import Options

The `<import-options>` element, as a child of the `<fcpxml>` element, can contain zero or more `<option>` elements that describe options for importing events and projects.

__Table 1-4__  Option element attributes

| Attribute | Description |
| `key` | A string that identifies one of the following import options:   - `copy assets`—Copy (1) or link (0) assets referenced in the imported XML. - `library location`—The location (URL) of the library to which to add the event or project. If the specified URL represents a directory, the default library name is used. If no library exists at the location specified, a new library is created. - `suppress warnings`—Suppress (≥1) or show (0) warnings generated during import. |
| `value` | The value for the import option. |

[Next](Story%20Elements.md)[Previous](About%20Final%20Cut%20Pro%20X%20XML%201.8.md)

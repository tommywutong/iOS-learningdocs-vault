---
title: Final Cut Pro X XML Format
apple_id: TP40011227
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Resources/Resources.html
archived_at: '2026-07-27T06:57:08.556501Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X XML Format](About%20Final%20Cut%20Pro%20X%20XML%201.8.md)


[Next](Adjustments%20and%20Effects.md)[Previous](Story%20Elements.md)

# Resources

An FCPXML document contains multiple references to shared resources, such as media files, video formats, and effects. You define references to shared resources in the `<resources>` element, a child of the `<fcpxml>` element.

__Note:__ In FCPXML 1.4, the `<resources>` element is an immediate child of the `<fcpxml>` element, and contains the resources used by events included in the XML.

In FCPXML 1.3 and earlier, the `<resources>` element is a child of the `<project>` element, and contains the resources used by that project.

## Structure

The `<resources>` element can include the child elements in Table 3-1.

__Table 3-1__  Resource elements

| Element | Description |
| `<asset>` | A reference to a media file managed by a library. |
| `<effect>` | A reference to an effect plug-in (for example, FxPlug, Motion document, or Audio Unit).  The `src` attribute specifies the location of a Motion template, when templates are managed in the library or another external location. |
| `<format>` | A reference to a Final Cut Pro X video format definition. |
| `<media>` | A reference to a new or existing media definition in a library. The child element, either `<multicam>` or `<sequence>`, specifies whether this is a multicam or compound clip. |

Each resource has an `id` attribute that specifies a _local identifier_ for use within the FCPXML document. For example, an asset resource with a local identifier of `r1` might be declared as follows:

```
<asset id="r1" name="MyMovieFile" src="file:///path/to/MyMovieFile.mov"/>
```

The `src` attribute is expected to be a string that specifies an absolute file URL conforming to RFC 2396, or a relative URL based on the location of the FCPXML document itself (for example, `./Media/MyMovie.mov`).

Later in the same FCPXML document, a video or audio element that uses the asset can refer to it by its local identifier.

```
<video ref="r1" ... >
```

__Note:__ Third-party tools may use any string for a local identifier as long as the string begins with a letter and no two resources in the same FCPXML document share the same local identifier.

For most resources, Final Cut Pro X also assigns a lengthier _unique identifier_ that it writes when exporting the FCPXML document. This unique identifier is stored as a `uid` attribute in the resource.

__Note:__ Except for assets, unique identifiers are managed by Final Cut Pro X and should not be generated or altered by third-party tools. See [Media Assets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomry) for discussions on asset unique identifiers.

Final Cut Pro X has both a local identifier and a unique identifier so that it can distinguish between resources that already exist and resources that are imported for the first time. Exported FCPXML documents that refer to existing resources have unique identifiers assigned by Final Cut Pro X, whereas imported FCPXML documents containing new resources only have local identifiers. A local identifier provides an identity for a new resource in an FCPXML document before Final Cut Pro X assigns it a permanent unique identifier.

## Media Assets

The `<asset>` element specifies a reference to a media file.

__Table 3-2__  Asset element attributes

| Attribute | Description |
| `uid` | The unique identifier of the asset. It is recommended to use a UUID or a string with a reverse DNS prefix to ensure uniqueness.  __Note:__ Final Cut Pro X reserves strings containing only uppercase hexadecimal characters for internal identifiers. A third party tool must not use these strings when assigning its own asset identifiers. |

Some `<asset>` element attributes are optional (or implied) because their values can be derived from the respective media file. However, the asset file may be offline when Final Cut Pro X tries to access it, therefore, it is recommended that you specify the attributes listed in Table 3-3 for all assets.

__Table 3-3__  Asset element offline attributes

| Attribute | Description |
| `hasVideo` | Specifies whether the asset has video. |
| `hasAudio` | Specifies whether the asset has audio. |
| `audioSources` | The number of audio sources (or tracks) in the asset. |
| `audioChannels` | The number of audio channels in an audio source (or track). |
| `audioRate` | The asset’s audio rate. |

The `<asset>` element has the attributes listed in Table 3-4 that you can use to override the information in the asset file.

__Table 3-4__  Asset element override attributes

| Attribute | Description |
| `colorSpaceOverride` | Specifies the color space to use. Color space is described in terms of its three components, as discussed later in this section. See [Well Known Color Space Triplets](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmznknltcma) for the list of valid values.  For still images, the value can be `sRGB IEC61966-2.1` or `Adobe RGB (1998)`, in addition to those described in terms of components. |
| `customLUTOverride` | Specifies a combination of color primaries and transfer functions specific to a particular camera manufacturer. The value can be one of the following:   - A built-in custom camera Log or processing mode. For example, `64 (Panasonic_VLog_VGamut)`. - A custom LUT. For example, `LUT:f9814a42eb75c58d9d9dc2a5344bd423 (FilmConvert-Justine-3D-LUT)`. |
| `projectionOverride` | Specifies the projection type for the asset. Valid values are `none`, `equirectangular`, `cubic`, `fisheye`, and `back-to-back fisheye`. |
| `stereoscopicOverride` | Specifies the stereoscopic mode for the asset. Valid values are `mono`, `side by side`, and `over under`. |

Third party tools can assign a unique identifier with the `uid` attribute of the `<asset>` element. This allows you to reference the same asset in a subsequent XML import, even if the URL specified by the `src` attribute is different. Final Cut Pro X locates the asset using the `uid` attribute value and relinks the media. The asset now uses the media file at the new URL.

This enables a workflow where the initial XML import uses the proxy media that is currently available to allow the editor to start working. Then, when the respective high resolution media becomes available, a second XML import can be used to replace the proxy media with the high resolution media. For this to work, the proxy and the high resolution media must be compatible, meaning their frame rates match and the high resolution media covers the time range of the proxy media. If desired, you can also go back from the high resolution media to the proxy media, as long as the two medias are compatible.

There can be a situation where an importing XML includes a media asset with its unique identifier assigned by a third party tool, yet the media asset has already been imported manually into Final Cut Pro X by the user. In such a case, Final Cut Pro X finds the asset through the URL specified by the `src` attribute and assigns the unique identifier from the importing XML to the asset already imported into Final Cut Pro X overriding the unique identifier generated by Final Cut Pro X. This is only possible when the media asset imported has a unique identifier assigned by Final Cut Pro X. Refer to [Table 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomrw) for unique identifiers that can be assigned by a third party tool.

## Media Formats

The `<format>` element specifies the video format for a timeline. This element has a reference to one of the predefined video formats listed in [Video Formats](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmznknltg) through the `name` attribute, or it can describe a custom format using the attributes in Table 3-5.

__Note:__ For audio only assets, use the `FFFrameRateUndefined` format.

Starting in FCPXML 1.7, format attributes in Table 3-5 override the values of a predefined format identified by the `name` attribute.

__Note:__ In FCPXML 1.6 and earlier, the `<format>` element attributes were ignored if the `name` attribute was specified.

__Table 3-5__  Format element attributes

| Attribute | Description |
| `fieldOrder` | The field order for interlaced (`upper first` or `lower first`), or progressive video (`progressive`). |
| `frameDuration` | The frame duration as a time value. |
| `height` | The video frame height, in pixels. |
| `paspH` | The relative width of a pixel when video is encoded with non-square pixels. |
| `paspV` | The relative height of a pixel when video is encoded with non-square pixels. |
| `width` | The video frame width, in pixels. |
| `colorSpace` | The asset’s color space, as discussed later in this section. |
| `projection` | The projection type, `none` for a traditional project or media, `equirectangular` or `cubic` for a 360 project or media. |
| `stereoscopic` | The type of stereoscopic mode: `none`, `side by side`, or `over under`. |

In FCPXML 1.7, color space is described in terms of its components (color primaries, transfer function, and YCbCr matrix). Each component is encoded as an integer value, and combined in a triplet with a hyphen (-) as the delimiter. For example, `1-1-1` represents the standard Rec. 709 color profile, and `9-1-9` is the standard Rec. 2020 color profile in SDR with the traditional Rec. 709 transfer function. For specific encoded values consult ISO/IEC 23001-8.

When Final Cut Pro X exports FCPXML, it appends the name of the color space in parentheses to the triplet above for well known color spaces. For example `1-1-1 (Rec. 709)` or `9-1-9 (Rec. 2020)`. On import, Final Cut Pro X only uses the triplet and ignores the name within the parentheses.

The color space of a project or a multicam sequence can be one of those listed in [Well Known Color Space Triplets](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmznknltcma).

The `colorSpace` attribute of the `<format>` element and the `colorSpaceOverride` attribute of the `<asset>` element use this syntax for specifying the color space.

Still image color spaces cannot be represented in terms of components, so the triplet syntax isn’t valid. Instead, you can use one of following values for the `colorSpaceOverride` attribute:

- `sRGB IEC61966-2.1`
- `Adobe RGB (1998)`

## Bookmark Data

A security-scoped bookmark, associated with an `<asset>` element, is required for sandboxed applications that need to access a media asset (file-system resource) outside the sandboxed environment. Refer to the _Security-Scoped Bookmarks and Persistent Resource Access_ section in the _[App Sandbox Design Guide](../../Security/App%20Sandbox%20Design%20Guide/About%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobt)_ for more information.

Because of this requirement, Final Cut Pro X creates a document-scoped bookmark (see Table 3-6) for each media asset the user grants access to, and includes this bookmark data in the `<asset>` element when exporting an FCPXML document. See [Using Bookmark Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomrt) for more information.

When your application exports an FCPXML document, it is recommended that you add bookmark data to each `<asset>` element. See [Creating Bookmark Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomru) for more information.

__Table 3-6__  Bookmark element

| Element | Description |
| `<bookmark>` | A Base64-encoded string that represents security-scoped bookmark data. It is used by a sandboxed application to reference an asset outside the sandboxed environment.  A bookmark is associated with an `<asset>` element. |

### Using Bookmark Data

Follow these steps to use a security-scoped bookmark in a sandboxed application:

1. Decode the bookmark data.

   The bookmark data in the bookmark element is Base64-encoded so you must first decode the bookmark before it can be used.
2. Resolve the decoded bookmark data into a security-scoped URL that points to the media asset.
3. Indicate that you want to use the security-scoped URL to access the file-system resource.
4. Access the file-system resource using the security-scoped URL in your application.
5. Release the file-system resource.

These steps are outlined in the following code snippet (refer to _[NSURL Class Reference](https://developer.apple.com/documentation/foundation/nsurl)_ for details on the NSURL methods used):

```
// Decode the Base64 bookmark data
NSData* decodedBookmark = [[NSData alloc] initWithBase64EncodedString:bookmark options:NSDataBase64DecodingIgnoreUnknownCharacters];

// Resolve the decoded bookmark data into a security-scoped URL.
NSError* err = nil;
NSURL* url = [NSURL URLByResolvingBookmarkData:decodedBookmark
                                       options:NSURLBookmarkResolutionWithSecurityScope
                                 relativeToURL:sourceURL
                           bookmarkDataIsStale:nil
                                         error:&err];

if (url) {
    // Indicate that you want to access the file-system resource.
    [url startAccessingSecurityScopedResource];

    // Use the resolved security scoped URL.
    ...

    // Release the file-system resource when you are done.
    [url stopAccessingSecurityScopedResource];
}

// Release the decoded bookmark data
[decodedBookmark release];
```

__Note:__ To use security-scoped bookmarks, your application must have the `com.apple.security.files.bookmarks.document-scope` entitlement set to `true`. For more details see [Enabling Security-Scoped Bookmark and URL Access](../../Miscellaneous/Entitlement%20Key%20Reference/Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcoa).

### Creating Bookmark Data

When you export an FCPXML document as a file, you create a security-scoped bookmark relative to the containing document. When you export an FCPXML document for drag-and-drop, you create an unscoped bookmark.

Follow these steps to create bookmark data:

1. Start accessing the security-scoped resource. This ensures that the relevant operating system resources are available.
2. Create the bookmark data for the media asset URL.

   Use the `NSURLBookmarkCreationWithSecurityScope` option if you are generating a security-scoped bookmark for an FCPXML document stored in a file. The URL for the containing document file is required. For drag-and-drop there is no containing file, so set the option to 0 to generate an un-scoped bookmark.
3. Stop accessing the security scoped resource. This releases the relevant operating system resources required to create the bookmark data.

These steps are outlined in the following code snippet (refer to _[NSURL Class Reference](https://developer.apple.com/documentation/foundation/nsurl)_ for details on the NSURL methods used):

```
NSURL* assetURL = myAssetURL();
NSURL* documentURL = useSecurityScopedBookmark ? myDocumentURL() : nil;
NSURLBookmarkCreationOptions options = useSecurityScopedBookmark ? NSURLBookmarkCreationWithSecurityScope : 0;
NSError* err = nil;

// Start accessing security scoped resource
[assetURL startAccessingSecurityScopedResource];

// Create bookmark
NSData    * bookmark = [assetURL bookmarkDataWithOptions:options
                       includingResourceValuesForKeys:nil
                                        relativeToURL:documentURL
                                                error:&err];

// Stop accessing security scoped resource
[assetURL stopAccessingSecurityScopedResource];
```

## Multicam Media

You can use a `<multicam>` media element to assemble footage from multiple cameras, or angles, that are synchronized in time. A `<multicam>` element contains one or more `<mc-angle>` elements that each manage a series of other story elements.

__Table 3-7__  Multicam media elements

| Element | Description |
| `<multicam>` | A root container for _angles_ of related media, organized as `<mc-angle>` elements. |
| `<mc-angle>` | A container of story elements organized sequentially in time. |

The `<multicam>` element appears as a child element under a `<media>` element (as a resource).

Listing 3-1 shows a multicam definition with two angle definitions, `a1` and `a2`:

__Listing 3-1__  Multicam definition with two angles

```
<resources>
    <media id="r1" name="MyMulticamClip">
        <multicam format="r2">
            <mc-angle name="MyMovie1" angleID="a1">
                <asset-clip name="MyMovie1" offset="0s" ref="r3" duration="10s" audioRole="dialogue"/>
            </mc-angle>
            <mc-angle name="MyMovie2" angleID="a2">
                <asset-clip name="MyMovie2" offset="0s" ref="r4" duration="20s" audioRole="dialogue"/>
            </mc-angle>
        </multicam>
    </media>
    <format id="r2" name="FFVideoFormat1080p30"/>
    <asset id="r3" name="MyMovie1" src="file:///Volumes/Media/MyMovie1.mov" start="0s" duration="10s" hasVideo="1" format="r2" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"/>
    <asset id="r4" name="MyMovie2" src="file:///Volumes/Media/MyMovie2.mov" start="0s" duration="20s" hasVideo="1" format="r2" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"/>
</resources>
```

### Using Multicam Media

To use the multicam media as a clip, add an `<mc-clip>` element that references the media in the timeline.

Each `<mc-clip>` element can use audio and video from the same angle, or combine the audio and video from separate angles from the same `<multicam>` container. You use `<mc-source>` elements to specify which angle the audio, video, or both come from.

__Table 3-8__  Multicam source element

| Element | Description |
| `<mc-source>` | Specifies which angle a particular part of the clip comes from. This element has the following attributes:   - `angleID`—Specifies the angle. - `srcEnable`—Indicates which source to use, if any, from the angle (one of `audio`, `video`, `all`, or `none`). |

The following example references the multicam media defined in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomy):

```
<mc-clip ref="r4" name="MC Clip" duration="10s">
    <mc-source angleID="a1" srcEnable="all"/>
</mc-clip>
```

__Note:__ In FCPXML 1.1, you specified the angle using the `videoAngleID` and `audioAngleID` attributes of the `<mc-clip>` element. In FCPXML 1.2, you used the `<mc-source>` element’s `angleID` attribute.

### Audio Components and Multicam

When you use a multicam clip in your project timeline, you can also specify the configuration of audio components, such as:

- Enabling or disabling the component
- Mute ranges
- Volume and other audio adjustments
- Audio filters

Listing 3-2 is an example multicam project based on [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomy), with two multicam clips whose audio components are reconfigured. The first clip has its audio trimmed at both ends as a JL cut. The second angle in the second clip has its audio muted for 5 seconds in its middle section.

__Listing 3-2__  Multicam project with two multicam clips and reconfigured audio

```
<project name="MyProject">
    <sequence duration="40s" format="r2">
        <spine>
            <mc-clip name="MyMulticamClip" offset="0s" ref="r1" duration="20s">
                <mc-source angleID="a1" srcEnable="all">
                    <audio-role-source role="dialogue.dialogue-1" start="1s" duration="18s"/>
                </mc-source>
            </mc-clip>
            <mc-clip name="MyMulticamClip" offset="20s" ref="r1" duration="20s">
                <mc-source angleID="a1" srcEnable="video"/>
                <mc-source angleID="a2" srcEnable="audio">
                    <audio-role-source role="dialogue.dialogue-1">
                        <mute start="5s" duration="10s"/>
                    </audio-role-source>
                </mc-source>
            </mc-clip>
        </spine>
    </sequence>
</project>
```

__Note:__ As of FCPXML 1.2, `<mc-source>` elements no longer support audio filters. Instead, you apply audio filters to an `<mc-clip>` element, which applies the effect to all active audio source angles, or to an `<audio-source>` element, which only applies the effect to the individual audio source, if active. Existing FCPXML 1.1 projects with audio angles on an `<mc-clip>` element are converted to 1.2 and later format on import.

In FCPXML 1.6, the `<audio-role-source>` element must be used to apply audible adjustments and audio filters to an audio component identified by its role.

[Next](Adjustments%20and%20Effects.md)[Previous](Story%20Elements.md)

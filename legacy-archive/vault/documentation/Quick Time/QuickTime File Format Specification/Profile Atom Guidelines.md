---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFAppenF/QTFFAppenF.html
archived_at: '2026-07-27T06:57:06.827362Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Audio%20Priming%20-%20Handling%20Encoder%20Delay%20in%20AAC.md)[Previous](Summary%20of%20VR%20World%20and%20Node%20Atom%20Types.md)

# Profile Atom Guidelines

__Note:__ Profile atoms are deprecated in the QuickTime file format. The information that follows is intended to document existing content containing profile atoms and should not be used for new development.

This appendix introduces and defines some of the ways that profile information about a QuickTime movie file can be summarized in a profile atom near the beginning of the file, so that software reading the file can easily determine some aspects of its features and complexity.

The information in this appendix should not be seen as a replacement for, or even a functional overlap with, the definition of the file-type atom. The file-type atom expresses which specifications a file is compatible with: reading software should not attempt to play files unless they are compatible with one or more specifications the reader implements, and should not refuse to play a file if it is marked as so compatible. However, reading software may use profiling information to issue warnings, request user decisions, and so on.

Reading software should not present excessive warnings to the user in the absence of summarized features. Additionally, readers are encouraged to try to play content even though crucial profile information is missing or incomplete.

Profiles may exist at the movie level or the track level. Track-level profiles summarize features of that track only. Movie-level profiles may summarize features across tracks or summarize features that are only relevant at the movie level (for example, the movie’s maximum bit rate).

If the movie contains runtime variables that might affect a feature, such as the presence of alternate tracks that would affect the movie bit-rate, the affected feature should either be absent or report the worst case (for example, the highest bit-rate).

If a feature value cannot be accurately represented (for example, the value is not an integer, but the field is formatted as an integer) then the value should be rounded up to the nearest representable value.

## About This Appendix

The technical content of this appendix begins with a discussion of the structure of the profile atom, which holds an array of feature codes and values. Next is an enumeration of the currently included profile features, each described in a feature description section.

The responsibilities placed upon a writer of a movie (such as QuickTime or a consumer electronics (CE) device) are described in the feature’s Writer Responsibilities section. A description of the algorithm to be used to calculate values is provided.

The feature’s Reader Responsibilities section explains how reading software should interpret the value. In some cases, there are warnings to indicate how the reader must not use the value (for example, not interpreting the maximum bit rate value as the current bit rate).

## Profile Atom Specification

### Definition

**Atom type**
: `'prfl'`

**Container**
: Movie atom (`'moov'`)
or track atom (`'trak'`)

**Mandatory**
: No

**Quantity**
: Zero or one

At the movie level, the profile atom must occur within the movie atom before the movie header atom. A reader may stop the search for the profile atom once the profile atom or the movie header atom is found. Because new atoms may be introduced into the movie atom (type `'moov'`) in the future, a reader must not expect the first child atom of the movie atom to be either the profile (type `'prfl'`) or the movie header (`'mvhd'`) atom. This rule allows for new atoms in the future but still accommodates readers that do not want to perform an exhaustive enumeration of all the child atoms in a movie atom.

The profile atom expresses profiles or feature codes for features that occur in the movie. The list is not necessarily exhaustive, and there may be multiple profile values recorded for the same profile code. For example, if there are two independent sequences of MPEG-4 video in the movie, using different profile-level IDs, both might be recorded here.

Each feature is either universal or is documented in a specific specification, identified by a brand as used in the file type atom. The only brands that should occur in a given profile atom are the universal brand or brands that occur in the file type atom in the same file.

Feature value ranges should in general never include an unknown point; if the value of a feature is unknown, the feature should be absent from the profile atom.

Feature values should be deducible by fairly simple inspection of the rest of the movie: for example, extracting the profile-level ID from a video header, or calculations using information from the sample table (for example, overall average bit rate by summing the sample sizes and the sample durations). It is not appropriate to have features which cannot be computed, or only computed with difficulty (e.g. a buffer model estimation which requires emulating a video decoder on the entire bit stream). The algorithm to extract or deduce the feature value from the rest of the file must be defined.

Empty slots in the profile atom structure must be filled with zeroes.

If there are multiple parts of the file to which the same feature apply, yet they have different feature values, then either there must be entries for each occurrence or none at all. For example, if there are two MPEG-4 visual sequences, using different visual profiles, there are either two profile entries in the profile table (one for each sequence) or none at all. Features must not be partially documented.

Profile atoms may also occur at the track level. A track-level profile atom must occur within the track atom before the track header atom (`'tkhd'`). A reader should stop searching for a track’s profile atom if either the profile or the track header atom is found, ignoring any other atoms present.

A track profile atom should only summarize features within that track. If track profile atoms exist, a movie profile atom can be built largely by copying feature entries from the profile atom of the movie’s tracks to the profile atom at the movie level. It is possible to have multiple track profiles with different values which must be resolved to a single value for the movie as whole, however—such as multiple video tracks with different maximum bit rates—so not all features can be copied directly from the track to the movie profile. Additionally, the movie profile may summarize features that cannot occur at the track level, such as total movie bit rate.

When building a movie profile, you must include either all instances of a track-level feature or no instances of that feature. For example, if you have multiple video tracks that use different codecs, you must either include an entry at the movie level for each codec, or put no codec feature entries at the movie level at all.

[Figure F-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywteobzguyq) shows the layout of the profile atom.

__Figure F-1__  The layout of a profile atom

（原归档配图获取待重试：`qtff_10.gif`）

### Syntax

```
aligned(8) class ProfileAtom
    extends FullAtom('prfl') {
    unsigned int(32) feature-record-count;
    for (i=1; i<feature-record-count; i++) {
        unsigned int(32) reserved = 0;
        unsigned int(32) part-ID;
        unsigned int(32) feature-code;
        unsigned int(32) feature-value
    }
}
```

### Semantics

**`reserved`**
: A 32-bit field that must be set to zero.

**`part-ID`**
: Either a brand identifier that occurs in the file-type atom of the same file, indicating a feature that is specific to this brand, or the value 0x20202020 (four ASCII spaces) indicating a universal feature that can be found in any file type that allows the profile atom. The value 0 is reserved for an empty slot.

**`feature-code`**
: A four-character code either documented here (universal features), or in the specification identified by the brand. The value of 0 is reserved for an empty slot with no meaningful `feature-value`.

**`feature-value`**
: Either a value from an enumerated set (for example, 1 or 0 for true or false, or an MPEG-4 profile-level ID) or a value that can compared (for example, bit rate as an integer or dimensions as a 32-bit packed structure).

The profile atom is a full atom, so it has an 8-bit version and 24 bits of flags. For this specification, the version is 0 and the flags have the value 0. A reader compliant with this specification should treat any profile atom with a nonzero version value as if it did not exist.

[Figure F-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywteojrheya) shows the layout of a typical feature.

__Figure F-2__  Layout of a typical feature

（原归档配图获取待重试：`qtff_12.gif`）

## Universal Features

A feature consists of four fields: a reserved field, which is set to zero; a part-ID, which specifies which brand the feature belongs to; a feature code, which identifies the feature; and a value field, which holds the feature value).

The part-ID can be either universal or brand-specific. Universal features have a part-ID of four ASCII spaces (0x20202020). Brand-specific features have a part-ID for a particular brand, which is taken from the Compatible_brands field of the file type atom. Brand-specific features of QuickTime files have a part-ID of `'qt  '`. All features listed in this section are universal features; that is, they can be used in any file that includes a profile atom.

It is permissible to use the feature code of 0x00000000 as a placeholder, paired with a feature value of 0x00000000 for one or more features. Readers should simply ignore features having a feature code of zero.

No feature will exist to describe the unit of other features, such as bit rate. The device should consider the magnitude and tailor its display appropriately.

This specification describes only how features are stored in files. It does not require that the values of features be reported (for example, in a user interface) in the same manner as they are stored, or require that they be reported at all.

### Table of Features

[Table F-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtgmbtguyq) lists the universal features described in this appendix.

__Table F-1__  Universal features

| Brand | Code | Description | Profile Parent |
| 0x20202020 | mvbr | [Maximum Video Bit Rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemrrgu2q) | Movie or Video Track |
| 0x20202020 | avvb | [Average Video Bit Rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemrtgq4q) | Movie or Video Track |
| 0x20202020 | mabr | [Maximum Audio Bit Rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemrvgqzq) | Movie or Track |
| 0x20202020 | avab | [Average Audio Bit Rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemrxgm3q) | Movie or Sound Track |
| 0x20202020 | vfmt | [QuickTime Video Codec Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemrzgmyq) | Movie or Video Track |
| 0x20202020 | afmt | [QuickTime Audio Codec Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemzrgi2q) | Movie or Video Track |
| 0x20202020 | m4vp | [MPEG-4 Video Profile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemztgizq) | Movie or Video Track |
| 0x20202020 | mp4v | [MPEG-4 Video Codec](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemzvge3q) | Movie or Video Track |
| 0x20202020 | m4vo | [MPEG-4 Video Object Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywteojygm4q) | Movie or Video Track |
| 0x20202020 | mp4a | [MPEG-4 Audio Codec](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtemzzga2q) | Movie or Sound Track |
| 0x20202020 | mvsz | [Maximum Video Size in a Movie](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywteojugi2q) | Movie |
| 0x20202020 | tvsz | [Maximum Video Size in a Track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywteobtgy4q) | Movie or Video Track |
| 0x20202020 | vfps | [Maximum Video Frame Rate in a Single Track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtenbshezq) | Movie or Video Track |
| 0x20202020 | tafr | [Average Video Frame Rate in a Single Track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywteojvg4ya) | Movie or Video Track |
| 0x20202020 | vvfp | [Video Variable Frame Rate Indication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtenbuha3q) | Movie or Video Track |
| 0x20202020 | ausr | [Audio Sample Rate for a Sample Entry](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtenbwhayq) | Movie or Sound Track |
| 0x20202020 | avbr | [Audio Variable Bit Rate Indication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtenrwg43a) | Movie or Sound Track |
| 0x20202020 | achc | [Audio Channel Count](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrsgywtenrygi3q) | Movie or Sound Track |

### Maximum Video Bit Rate

**Containing profile atom**
: Track (video), movie

**Reserved**
: 0x00000000

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'mvbr'`

**`feature-value`**
: Unsigned `int(32)` indicating maximum video bit rate in bits per second

#### Feature Values

The value is an unsigned 32-bit integer indicating the maximum video bit rate in bits per second. The value may be larger than the actual video bit rate, so it should not be interpreted as a bit rate that will actually occur.

Example: 1 Mbps = 1000000.

#### Writer Responsibilities

A writer of the maximum video bit rate should record a value that is equal to or greater than the actual bit rate for the video track. A writer (such as a CE device) may choose to record a constant value so long as that value is greater than or equal to the bit rate that may be encoded. It is also permitted to record a value set by the video encoder during initialization, so long as the value is never exceeded.

#### Feature Value Algorithm

Apple recommends a sliding average over 1 second calculated from the sample tables.

If the feature is written for a newly encoded track (as by a CE device), it is permitted to record a value used to initialize the video encoder so long as the value is never exceeded. If the video track is edited and the maximum video bit rate recalculated, it may be calculated as a sliding average over 1 second, based on the sample table.

This can be calculated in the following manner:

1. For each sample, calculate the average 1-second bit rate; choose the shortest run of samples, including the candidate sample, that comprise 1 second or more of video, then divide the total data size of those samples by their total duration.
2. Choose the maximum value from the list of calculated 1-second averages.

#### Reader Responsibilities

A reader of the maximum video bit rate feature value should compare the recorded value with its own limits to determine if the content can be played. The reader should not perform an equality comparison (=) but instead a relative comparison (<, <=, >, or >=).

The recorded value may be larger than the actual maximum video bit rate. Since this value may be an over-estimate, the reader should not use it as a basis for refusing to play the file, though a warning may be appropriate. To determine the actual bit rate, the reader may need to perform an inspection of the video track’s sample table.

#### Comments

The value of this feature should be deducible from information found in the sample table. Track edits must be considered in its calculation; if the track is edited, this value must be recalculated. Even though this value may exceed the actual maximum video bit rate, writers should attempt to minimize any over-estimation.

### Average Video Bit Rate

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'avvb'`

**`feature-value`**
: Unsigned `int(32)` indicating average video bit rate in bits per second

#### Feature Values

The value is an unsigned 32-bit integer indicating the average video bit rate in bits per second.

Example: 1 Mbps = 1000000.

#### Writer Responsibilities

A writer of the average video bit rate feature should record a value that is equal to or greater than the average bit rate for the video track, measured across all media samples. A writer (such as a CE device) may choose to record a constant value so long as that value is greater than or equal to the average bit rate that may be encoded. It is also permitted to record a value set by the video encoder during initialization so long as the value equals or exceeds the average calculated from the resulting file.

#### Feature Value Algorithm

Ideally, the long-term average: total sample sizes divided by total sample durations.

If the feature is written for a newly encoded track (as by a CE device), it is permitted to record a value used to initialize the video encoder. If the video track is edited and the average video bit rate recalculated, it may be calculated as an overall average based on the sample table.

#### Reader Responsibilities

A reader of the average video bit rate feature value should compare the recorded value with its own limits to determine if the content can be played. The reader should not perform an equality comparison (=) but instead a relative comparison (<, <=, >, or >=).

Because a writer may record a larger value than the actual video bit rate, a reader should not interpret this as the actual video bit rate. To determine the current or actual bit rate, the reader may need to perform an inspection of the video track's sample table.

#### Comments

The value of this feature should be deducible from information found in the sample table. Track edits must be considered in its calculation. Note that for highly variable bit rate video, the average rate may not be a typical rate.

### Maximum Audio Bit Rate

**Containing profile atom**
: Track (sound), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'mabr'`

**`feature-value`**
: Unsigned `int(32)` indicating maximum audio bit rate in bits per second

#### Feature Values

The value is an unsigned 32-bit integer indicating the maximum audio bit rate in bits per second that must be supported to guarantee playback of the audio. The actual maximum bit rate may be smaller, so a reader should not display this as the current bit rate.

Example: 128 kbps = 128000.

#### Writer Responsibilities

A writer of the maximum audio bit rate feature should record a value that is equal to or greater than the current bit rate for the sound track. While the value may exceed the actual maximum bit-rate, the writer should attempt to minimize any over-estimation.

While recording the precise bit rate is preferred, it is not required. A writer (such as a CE device) may choose instead to record a constant value so long as that value is greater than or equal to the bit rate that may be encoded. It is also permitted to record a value set by the audio encoder during initialization so long as the value is never exceeded.

#### Feature Value Algorithm

Apple recommends a sliding average over 1 second calculated from the sample tables.

If the feature is written for a newly encoded track (as by a CE device), it is permitted to record a value used to initialize the audio encoder so long as the value is never exceeded.

If the sound track is edited, and the audio bit rate is not constant, the maximum audio bit rate must be recalculated. Note that editing can change the duration of media samples, resulting in non-constant bit rate audio even when the sound track is encoded using a constant bit rate encoder. Maximum bit rate may be calculated as a sliding average over 1 second, based on the sample table. This can be calculated in the following manner:

1. For each sample, calculate the average 1-second bit rate; choose the shortest run of samples, including the candidate sample, that comprise 1 second or more of audio, then divide the total data size of those samples by their total duration.
2. Choose the maximum value from the list of calculated 1-second averages.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own limits to determine if the content can be played. The reader should not perform an equality comparison (=) but instead a relative comparison (<, <=, >, or >=).

Because this value may be an over-estimate of the true maximum bit rate, the reader should not refuse to play a file on the basis of this value, although a warning may be appropriate. To determine the current or actual bit rate, the reader may need to perform an inspection of the video track's sample table.

### Average Audio Bit Rate

**Containing profile atom**
: Track (sound), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'avab'`

**`feature-value`**
: Unsigned `int(32)` indicating average audio bit rate in bits per second

#### Feature Values

The value is an unsigned 32-bit integer indicating the average audio bit rate in bits per second.

Example: 128 kbps = 128000.

#### Writer Responsibilities

A writer of the average audio bit rate feature should record a value that is equal to or greater than the average bit rate for the sound track, measured across all media samples. A writer (such as a CE device) may choose to record a constant value so long as that value is greater than or equal to the average bit rate that may be encoded. It is also permitted to record a value set by the audio encoder during initialization so long as the value is never exceeded on average.

#### Feature Value Algorithm

Normally, the long-term average: total sample sizes divided by total sample durations.

If the feature is written for a newly encoded track (as by a CE device), it is permitted to record a value used to initialize the audio encoder. If the sound track is edited and the average video bit rate recalculated, it may be calculated as an overall average based on the sample table.

#### Reader Responsibilities

A reader of the average audio bit rate feature value should compare the recorded value with its own limits to determine if the content can be played. The reader should not perform an equality comparison (=) but instead a relative comparison (<, <=, >, or >=).

#### Comments

The value of this feature should be deducible from information found in the sample table. Track edits normally need not be considered in the calculation for constant bit rate audio, but must be considered for variable bit rate audio or when track or movie segments containing constant bit rate audio are edited to alter their duration.

### QuickTime Video Codec Type

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'vfmt'`

**`feature-value`**
: Unsigned `int(32)` (a four-character-code) holding the QuickTime video codec type copied from the `ImageDescription` structure’s `cType` field

#### Feature Values

This is the four-character-code found in a video sample description.

Examples: 'mp4v', 'jpeg'.

#### Writer Responsibilities

A writer of the QuickTime video codec type feature should record the four-character code corresponding to the QuickTime video format type or types also recorded in the video track’s sample descriptions.

__Note:__ A writer that records the QuickTime Video Codec type for the 'mp4v' codec is encouraged also to write the MPEG-4 Video Profile feature.

#### Feature Value Algorithm

The feature value is the video codec type read from a QuickTime ImageDescription’s `cType` field. If there are multiple sample descriptions with different video codec types, multiple video codec type features should be recorded in the profile atom.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value by an equality comparison (using =) with the format codes supported by the reader.

### QuickTime Audio Codec Type

**Containing profile atom**
: Track (sound), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'afmt'`

**`feature-value`**
: Unsigned `int(32)` (a four-character-code) holding the QuickTime audio codec type copied from `SoundDescription` structure’s `dataFormat` field

#### Feature Values

This is the four-character-code found in a sound sample description.

Examples: 'mp4a', 'twos'.

#### Writer Responsibilities

A writer of the QuickTime audio codec type feature should record the four-character-code corresponding to the QuickTime audio format type or types also recorded in the sound track’s sample descriptions.

__Note:__ A writer that records the QuickTime Audio Codec type for the 'mp4a' codec is encouraged also to write the MPEG-4 Audio Codec feature.

#### Feature Value Algorithm

The feature value is the audio codec type read from a `SoundDescription` structure’s `dataFormat` field. If there are multiple sample descriptions with different audio codec types, either all QuickTime Audio Codec Type features must be recorded in the profile atom or none must be recorded.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value by an equality comparison (using =) with the format codes supported by the reader.

### MPEG-4 Video Profile

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'m4vp'`

**`feature-value`**
: Unsigned `int(32)` where least significant 8 bits hold the `profile_and_level_indication` from the `visual_object_sequence`, as defined in specification ISO/IEC 14496-2, retrieved from the video parameters for the MPEG-4 video codec description. The top 24 bits must be set to 0.

#### Feature Values

The least significant 8 bits hold the value. The most significant 24 bits of the feature value should be set to 0.

#### Writer Responsibilities

A writer of the MPEG-4 video profile feature should record the 8 bits corresponding to the `profile_and_level_indication` from the `visual_object_sequence`, as defined in specification ISO/IEC 14496-2, found in the video parameters encoded in the esds of the MPEG-4 video codec sample description (with QuickTime codec type 'mp4v').

__Note:__ A writer that records the MPEG-4 video profile feature is encouraged also to write the QuickTime Video Codec Type feature.

#### Feature Value Algorithm

The feature value is the `profile_and_level_indication` from the `visual_object_sequence`, as defined in specification ISO/IEC 14496-2, retrieved from the video parameters for the MPEG-4 video codec description.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with the set of profiles and levels supported by the reader.

#### Comments

This feature may be present only if MPEG-4 video is used. Normally, the video codec type profile entry will also record that MPEG-4 video is present, unless no codec types are present (when, for example, an exhaustive list cannot be formed).

### MPEG-4 Video Codec

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'mp4v'`

**`feature-value`**
: Unsigned `int(32)` where the least significant 4 bits holds the `visual_object_type`  as found in the `VisualObject` (as defined in specification ISO/IEC 14496-2, subclause 6.2.2) found in the esds of the MPEG-4 video codec (QuickTime type 'mp4v') sample description

#### Feature Values

The least significant 4 bits hold the value. The most significant 28 bits of the feature value should be set to 0.

The list of visual object type constants is defined in specification ISO/IEC 14496-2, subclause 6.3.2.

Example: Video ID is indicated by the value 1.

#### Writer Responsibilities

A writer of the MPEG-4 Video Codec feature should record the 4 bits corresponding to the `visual_object_type` found in the `VisualObject` within the `ES_descriptor`'s video `DecoderSpecificConfig`. The most significant 28 bits of the value should be set to 0.

__Note:__ A writer that records the MPEG-4 Video Codec feature is encouraged also to write the QuickTime Video Codec Type feature.

#### Feature Value Algorithm

The MPEG-4 video codec is the 4 bits of the `visual_object_type` found in the `VisualObject`. See ISO/IEC 14496-2, subclause 6.2.2. The `VisualObject` is found in the MPEG-4 Elementary Stream Descriptor Atom within the `'esds'` sample description atom of the video sample description for the QuickTime video codec of type 'mp4v'.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with the set of MPEG-4 video decoders supported by the reader.

#### Comments

Because the QuickTime `'mp4v'` codec may implement multiple video decoders defined in specification ISO/IEC 14496 in the future, this feature allows the reader to determine the specific video decoder needed to interpret the video bit-stream.

### MPEG-4 Video Object Type

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'m4vo'`

**`feature-value`**
: Unsigned `int(32)` where the least significant 8 bits hold the `video_object_type_indication`  found in the `VideoObjectLayer` (Described in ISO/IEC 14496-2, subclause 6.2.3). The `VideoObjectLayer` is found in the MPEG-4 Elementary Stream Descriptor Atom within the `'esds'` sample description atom of the video sample description for the QuickTime video codec of type `'mp4v'`.

#### Feature Values

The value is a video object type constant that indicates a set of video tools. The list of video object type constants is defined in specification ISO/IEC 14496-2, subclause 6.3.3. The least significant 8 bits hold the value. The most significant 24 bits should be set to 0.

Example: The Simple Object Type video object is indicated by the value 1.

#### Writer Responsibilities

A writer of the MPEG-4 Video Object Type feature should record the 8 bits corresponding to the `video_object_type_indication` found in the `VideoObjectLayer` within the ES_descriptor’s video `DecoderSpecificConfig`. The most significant 24 bits of the value should be set to 0.This feature should be written only for MPEG-4 video of video object type 1 (Video ID). If the MPEG-4 video does not use Video ID (1) for `visual_object_type`, the esds will have no `VideoObjectLayer` and consequently no `video_object_type_indication`.
In this case, no MPEG-4 Video Object Type feature should be written.

__Note:__ A writer that records the MPEG-4 Video Object Type feature for encoded video using the Video ID visual object type is encouraged to write the MPEG-4 Video Codec and MPEG-4 Video Profile features as well.

#### Feature Value Algorithm

The MPEG-4 video object type is the least significant 8 bits of the `video_object_type_indication`  found in the `VideoObjectLayer`. See ISO/IEC 14496-2, subclause 6.2.3. The `VideoObjecLayer` is found in the MPEG-4 Elementary Stream Descriptor Atom within the `'esds'` sample description atom of the video sample description for the QuickTime video codec of type 'mp4v'.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with the set of MPEG-4 video tools supported by the reader.

### MPEG-4 Audio Codec

**Containing profile atom**
: Track (sound), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'mp4a'`

**`feature-value`**
: Unsigned `int(32)` where least significant 5 bits hold the `AudioObjectType` as found in the `AudioSpecificInfo` (as defined in specification ISO/IEC 14496-3, subclause 1.6) found in the esds of the MPEG-4 audio codec (QuickTime type `'mp4a'`) sample description

#### Feature Values

The least significant 5 bits hold the value. The most significant 27 bits of the feature value should be set to 0.

The list of audio object type constants is defined in specification ISO/IEC 14496-3, subclause 1.5.1.1.

Examples: AAC LC is indicated by the value 2, CELP is indicated by the value 8.

#### Writer Responsibilities

A writer of the MPEG-4 Audio Codec feature should record the 5 bits corresponding to the `AudioObjectType` found in the `ES_descriptor`'s audio `DecoderSpecificConfig`. The most significant 27 bits of the value should be set to 0.

__Note:__ A writer that records the MPEG-4 Audio Codec feature is encouraged also to write the QuickTime Audio Codec Type feature.

#### Feature Value Algorithm

The MPEG-4 audio codec value is the 5 bits of the `AudioObjectType` found in the `AudioSpecificInfo` (a `DecoderSpecificInfo`). See specification ISO/IEC 14496, subclause 1.6. The `AudioSpecificInfo` is found in the MPEG-4 Elementary Stream Descriptor Atom within the `siDecompressionParam` atom of the audio sample description for the QuickTime audio codec of type `'mp4a'`.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with the set of MPEG-4 audio decoders supported by the reader.

#### Comments

Because the QuickTime `'mp4a'` codec may implement multiple audio decoders defined in specification ISO/IEC 14496 in the future, this feature allows the reader to determine the specific audio decoder needed to interpret the audio bit stream. The MPEG-4 Audio Codec feature should be present only if the `'mp4a'` audio codec is used in a sound track.

### Maximum Video Size in a Movie

**Containing profile atom**
: Movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'mvsz'`

**`feature-value`**
: A 32-bit packed structure holding width and height of the largest bounds needed to display the movie

#### Feature Values

A packed structure in a 32-bit value:

```
struct {
    unsigned integer(16) width;
    unsigned integer(16) height;
};
```

In big-endian order, the top 16 bits correspond to the width. The lower 16 bits correspond to the height.

#### Writer Responsibilities

A writer of the Maximum Movie Video Size feature should record a value that is equal to or greater than the display size needed by the movie—the actual width and height needed to display the movie at its normal size, taking into account all matrices (all track matrices and the movie matrix).

A writer (such as a CE device) may choose to record a constant size based upon its current recording mode even if the actual size recorded in the movie is smaller.

#### Feature Value Algorithm

This value is calculated by examining the dimensions of all visual tracks and computing the maximum combined dimensions, including the effect of track matrices and the movie matrix. For example, if two video tracks play side-by-side in the movie, and the tracks and movie all use the identity matrix, this value will be the largest of the two tracks’ heights and their combined width.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own video size limits.

The reader should not interpret the value of this feature as the current video size. To determine the current video size, the reader should use the dimensions of all currently displaying video tracks, their matrices, and the movie matrix.

#### Comments

The width and height correspond to the maximum visual area needed to display the movie.

The summarized width and height should take into account all components of all track matrices and the movie matrix. The goal is to understand the maximum contribution of all tracks to the movie’s bounds.

For the case where there is a single video track with an identity track matrix, the movie’s maximum video size feature would typically have the same value as the track’s maximum video size feature.

### Maximum Video Size in a Track

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'tvsz'`

**`feature-value`**
: A 32-bit packed structure holding width and height of the largest picture buffer needed for a video track.

#### Feature Values

A packed structure in a 32-bit value:

```
struct {
    unsigned integer(16) width;
    unsigned integer(16) height;
};
```

In big-endian order, the top 16 bits correspond to the width. The lower 16 bits correspond to the height.

#### Writer Responsibilities

A writer of the Maximum Track Video Size feature should record a value that is equal to or greater than the largest height and width of any sample description in the video track. This does not include the effect of any scaling or offset applied by the track matrix and may not be the same as the track height and track width.

A writer (such as a CE device) may choose to record a constant size based upon its current recording mode even if the actual size recorded in the track is smaller.

#### Feature Value Algorithm

Examine all sample descriptions for the track, and use the maximum width and maximum height found in any sample. The maximum width and maximum height may come from independent sample descriptions.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own image buffer limits.

The reader should not interpret the value of this feature as the current video size. To determine the current video size, the reader should use the dimensions of all currently displaying video tracks, their matrices, and the movie matrix.

#### Comments

The width and height correspond to the largest image buffer dimensions needed for a visual track. When present in a movie-level profile, these atoms document the maximum video size found in each of the movie’s tracks.

The summarized width and height do not take into account any scaling or translation caused by the track or movie matrices, and are not necessarily the same as the track height and width.

For the case where there is a single video track with an identity track and matrix and an identity movie matrix, the movie’s maximum video size feature would have the same value as the track’s feature.

__Warning:__
Use of the "clean aperture" sample description extension does not affect the value of the track visual size, as the picture buffer is needed immediately after decoding, prior to any clean aperture clipping.

### Maximum Video Frame Rate in a Single Track

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'vfps'`

**`feature-value`**
: An unsigned fixed-point (16.16) number holding the maximum video frame rate

#### Feature Values

This is an unsigned fixed-point (16.16) number holding the maximum video frame rate. The integer portion of the number can range from 0 to 65535.

Examples: 25 fps = 0x00190000; 24 fps = 0x00180000; 29.97 = 0x001DF853 (close approximation of a 30000/1001 ratio). The value may be rounded up to the nearest integer.

#### Writer Responsibilities

A writer of the Maximum Video Frame Rate feature should record a 16.16 fixed-point value that is equal to or greater than the current video frame rate. A writer (such as a CE device) may choose to record a constant for the feature based on its current recording mode, even if the actual frame rate is less.

A writer of a new video track (such as a CE device recorder) may set the maximum frame rate feature value to a value set during video encoder initialization, so long as this frame rate is never exceeded.

If the current calculated frame rate is fractional (such as 22.3 fps), a writer may choose to round the value up to the nearest integer value (such as 23.0 fps for 22.3 fps).

A writer calculating the video frame rate using the video track’s sample table should not consider the first or the last sample duration if they differ from the other sample durations. The reason for this is that captured movie files often have longer or shorter first and last sample durations. By not considering them in the calculation, a more accurate calculation is achieved.

#### Feature Value Algorithm

This feature value may be calculated as the inverse of the smallest sample duration in the video track or tracks.

If the value is written for a newly recorded video track it may be a value established during initialization of the video encoder, so long as the frame rate is not exceeded.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own video frame rate limits. It should not expect exact values.

The reader should not interpret the value of this feature as the current frame rate. To determine the current frame rate, the reader should use the video track’s sample table.

#### Comments

A writer may choose to round up any fractional value of the fixed-point number to the nearest 16-bit integer leaving the lower 16 bits of the Fixed value set to 0. So, in the case of the 29.97 approximation of 0x001DF853, the writer could round this up to 0x001E0000 (which equals 30).

### Average Video Frame Rate in a Single Track

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'tafr'`

**`feature-value`**
: An unsigned fixed-point (16.16) number holding the average video frame rate

#### Feature Values

This is an unsigned fixed-point (16.16) number holding the average video frame rate. The integer portion of the number can range from 0 to 65535.

Examples: 25 fps = 0x00190000; 24 fps = 0x00180000; 29.97 = 0x001DF853 (close approximation of a 30000/1001 ratio). The value may be rounded up to the nearest integer.

When present in a movie-level profile, these atoms document the average video frame rate of each track in the movie.

#### Writer Responsibilities

A writer of the Average Video Frame Rate feature should record a 16.16 fixed-point value that is equal to or greater than the average video frame rate. A writer (such as a CE device) may choose to record a constant for the feature based on its current recording mode, even if the actual frame rate is less.

A writer of a new video track (such as a CE device recorder) may set the average frame rate feature value to a value set during video encoder initialization, so long as this frame rate is not exceeded by the actual average, as determined by the feature value algorithm described below.

If the average calculated frame rate is fractional (such as 22.3 fps), a writer may choose to round the value up to the nearest integer value (such as 23.0 fps for 22.3 fps).

#### Feature Value Algorithm

This feature value is calculated by dividing the the total number of frames (samples) by the duration of the track. It is permissible to omit the first and last frames from this calculation, as they may have significantly different duration than the average.

#### Reader Responsibilities

A reader of this feature code should understand that each frame is a video sample with its own independent and explicit duration. While it is possible for all frames to have the same duration, it is equally possible for the duration of any frame to be radically different from any other. Therefore, the average frame rate may not always be meaningful information.

The reader should not interpret the value of this feature as the current frame rate. To determine the current frame rate, the reader should use the video track’s sample table.

#### Comments

A writer may choose to round up any fractional value of the fixed-point number to the nearest 16-bit integer leaving the lower 16 bits of the Fixed value set to 0. So, in the case of the 29.97 approximation of 0x001DF853, the writer could round this up to 0x001E0000 (which equals 30).

### Video Variable Frame Rate Indication

**Containing profile atom**
: Track (video), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'vvfp'`

**`feature-value`**
: Unsigned `int(32)` holding the value 0 if the frame rate is constant or the value 1 if the frame durations vary

#### Feature Values

The feature value holds one of the following two values: 0 if all video samples have the same display duration, or 1 if any video samples vary in duration.

#### Writer Responsibilities

A writer of the Video Variable Frame Rate Indication feature should compare the video track sample durations. If all considered durations have the same value, the value 0 indicating constant frame rate should be recorded. If any durations differ, the value 1 should be recorded for the feature. No other value should be recorded.

#### Feature Value Algorithm

If the Time to Sample table records a constant duration for all samples, then record 0, else record 1.

#### Reader Responsibilities

A reader of this feature code should only expect the values 0 or 1.

### Audio Sample Rate for a Sample Entry

**Containing profile atom**
: Track (sound), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'ausr'`

**`feature-value`**
: Unsigned `int(32)` holding the audio sample rate in units per second (for example, 44100 for 44.1 kHz)

#### Feature Values

This feature value is an unsigned 32-bit integer holding the audio sample rate in units per seconds (cycles per second). The value should be rounded up to the nearest integer if it has a fractional portion.

Examples: 24 kHz = 24000, 44.1 kHz = 44100.

#### Writer Responsibilities

A writer of the Audio Sample Rate feature should record the integer portion (rounded up if there is a fractional portion) of the audio sample rate found in a sound track’s `SoundDescription` structure.

If multiple audio sample rates are used in the movie, then either all must recorded in the profile atom, or none must be recorded.

#### Feature Value Algorithm

This is the integer portion of the sample rate from a QuickTime audio sample description (rounded up if there is a fractional portion). If the sample rate is greater than 64 kHz, the integer portion can be recorded here.

If a sample rate has a fractional portion, the writer should round up to the nearest integer. So, the 22254.54545 value that may occur in QuickTime audio as a Fixed value represented as 0x56EE8BA3 can be recorded as 22255.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own audio sample rate limits. If the reader only supports discrete values (such as 44100), it can perform equality comparisons (=). If the reader supports ranges of audio sample rates (such as all rates less than or equal to 32000), the reader can perform relative comparisons (<, <=, >, or >=).

### Audio Variable Bit Rate Indication

**Containing profile atom**
: Track (sound), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'avbr'`

**`feature-value`**
: Unsigned `int(32)` holding the value 0 if the audio is constant bit rate or 1 if the audio is variable bit rate

#### Feature Values

The feature value holds one of the following two values: 0 if the audio is constant bit rate, or 1 if the audio is variable bit rate.

#### Writer Responsibilities

A writer of the Audio Variable Bit Rate Indication feature should determine if the audio frames are constant or variable bit rate in nature and record either 0 or 1, respectively.

#### Feature Value Algorithm

Consult the audio sample descriptions. If the `compressionID` field in the sample descriptions is 0 or -1, then the audio is constant bit rate. If the field is -2, then the same algorithm as for video applies: if all the samples have both constant duration and constant size, then the audio is constant bit rate; otherwise it is variable.

#### Reader Responsibilities

A reader of this feature code should only expect the values 0 or 1.

### Audio Channel Count

**Containing profile atom**
: Track (sound), movie

**`part-ID`**
: 0x20202020 (universal feature)

**`feature-code`**
: `'achc'`

**`feature-value`**
: Unsigned `int(32)` holding the number of audio channels

#### Feature Values

The feature value is an unsigned 32-bit integer holding the number of audio channels encoded by a Sound Track in the movie. For monaural, the value would be 1. For stereo, the value would be 2. Note that the audio channel count is a standard field in the sound sample description.

#### Writer Responsibilities

A writer of the Audio Channel Count feature should determine the number of audio channels encoded in the sound track or tracks of the movie.

#### Feature Value Algorithm

Consult the audio sample descriptions.

#### Reader Responsibilities

The reader should be prepared to either play the specified number of channels or to map the audio to the number of channels the reader supports (for example, mixing down stereo sound for a monaural speaker).

[Next](Audio%20Priming%20-%20Handling%20Encoder%20Delay%20in%20AAC.md)[Previous](Summary%20of%20VR%20World%20and%20Node%20Atom%20Types.md)

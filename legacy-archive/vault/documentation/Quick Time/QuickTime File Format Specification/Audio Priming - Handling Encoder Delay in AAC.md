---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFAppenG/QTFFAppenG.html
archived_at: '2026-07-27T06:57:06.847121Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Document%20Revision%20History.md)[Previous](Profile%20Atom%20Guidelines.md)

# Audio Priming - Handling Encoder Delay in AAC

This appendix describes temporal positioning of a source audio signal after AAC encoding into a sound track for QuickTime media files. The mechanisms described here are specified in ISO MPEG-4 standards (ISO/IEC 14496-12, 2008) and are used here with additional constraints.

__Note on language use:__

AAC implementations typically represent 1024 _PCM_ audio samples in one _AAC_ packet (synonymous in this context with a QuickTime media sample, and also referred to in ISO documents as an “access unit”). The terms “sample” and “audio sample” in this appendix are used to refer to PCM samples. For the encoded audio data, the terms “AAC packet” and QuickTime “media sample” are used.

## Background – AAC Encoding

AAC requires data beyond the source PCM audio samples in order to correctly encode and decode audio samples due to the nature of the encoding algorithm. AAC encoding uses a transform over consecutive sets of 2048 audio samples, applied every 1024 audio samples (overlapped). For correct audio to be decoded, both transforms for any period of 1024 audio samples are needed. For this reason, encoders add at least 1024 samples of silence before the first ‘true’ audio sample, and often add more. This is called variously “priming”, “priming samples”, or “encoder delay”. A couple of definitions for use in this discussion:

- _Encoder delay_ is the delay incurred during encoding to produce properly formed, encoded audio packets. It typically refers to the number of silent media samples (priming samples) added to the front of an AAC encoded bitstream.
- _Decoder delay_ is the number of “pre-roll” audio samples required to reproduce an encoded source audio signal for a given time index. For AAC this number is typically 1024 and is algorithmically based. This is in contrast to encoder delay which is determined by the encoder and encoding configuration used. However, decoder delay establishes the minimum encoder delay possible (that is, 1024 for AAC).

The common practice is to propagate the encoder delay in the AAC bitstream. When these audio packets are then decoded back to the PCM domain, the source waveform represented will be offset in its entirety by this encoder delay amount. Since encoded audio packets hold a fixed number of audio samples (for instance, 1024 samples) additional trailing or ‘remainder’ silent samples following the last source sample are required so as to pad the final audio packet to the required length.

[Figure G-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknltg) gives an example of a typical encoded AAC audio bitstream. The upper portion of the illustration represents the AAC encoded domain with equal-sized AAC packets, the lower portion represents the PCM sample domain:

__Figure G-1__  AAC encoded audio

（原归档配图获取待重试：`aac_encoded_bit_stream.jpg`）

The source audio to be encoded, shown as the red waveform, is 5389 samples long. You can see how it is represented with the blue priming and remainder samples against the fixed size access units–AAC packets–drawn above it.

This data will be represented in 8 AAC packets, where each packet represents 1024 audio samples. The total duration represented by these 8 AAC packets is 8192 audio samples (note that this is longer than the duration of the source audio).

The result breaks down into the following values:

- 2112 priming samples at the start—Required to correctly encode the start of the audio.
- 5389 samples of actual audio.
- 691 remainder samples—Required to pad out to the AAC packet size.

Therefore, to correctly extract the original 5389 samples of source audio, the first 2112 samples of priming and the last 691 samples of the remainder must be removed.

- 8192 - 2112 - 691 = 5389 original source samples.

## The Timing and Synchronization Problem

If an audio playback system attempting to synchronize AAC encoded audio and video does not compensate for encoder delay (that is, does not discard the silent priming samples), the audio and video will be out of synchronization. In the example above, it will be off by 2112 samples—The audio will be 2112 samples behind the video because the first real audio sample is actually the 2113th sample after the beginning of the decoded PCM data.

Therefore, a playback system must trim the silent priming samples to preserve correct synchronization. This trimming by the playback system should be done in two places:

- When playback first begins
- When the playback position is moved to another location. For example, the user skips ahead or back to another part of the media and begins playback from that new location.

## Historical Solution—Implicit Encoder Delay

In the original AAC implementations, as stated above the common practice was to propagate the encoder delay in the provided AAC bitstream. With these original implementations, the most common delay used was 2112 audio samples. An AAC bitstream would therefore generally be 3 AAC packets larger than what was theoretically required by the original signal.

A playback implementation would then need to discard these first 2112 silent samples from the decoded output since they contain none of the original source audio data; these samples are an artifact of the encoding/decoding process.

Because there was no explicit way to represent the extent of the priming or remainder samples with the first implementations of an AAC bitstream, Apple chose to assume that the AAC bitstream always contained an encoding delay with a fixed number of samples and advised developers accordingly. A fixed encoder delay of 2112 samples was chosen because at that time this was the common encoding delay used, for various reasons, by most of the shipping implementations of AAC encoders (commercial and otherwise).

__Note:__

The lack of explicit representation for encoder delay and remainder samples is not a problem unique to AAC encoding. With MPEG-4 and ADTS/MPEG-2 bitstreams and file containers, there is still no satisfactory, explicit representation for either the encoder delay or remainder samples. MP3 also has these data dependencies and delays in its bitstream, as do proprietary codecs such as AC-3 and others.

In all of these cases the conventional solution is as described above: an implicit assumption is made about the size of the encoder delay and the playback engine is required to trim this designated number of samples from its output at the start of playback. Adjustments must also be made for the remainder samples as required.

In summary, the historical technique to handle the timing and synchronization problem is to assume an _implicit_ 2112 sample standard encoder delay in AAC data streams and indicate start time—the first media sample or AAC packet—in the sound track edit list (see [Edit List Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjvheza)) at the start of encoder delay.

## Using Track Structures to Represent Encoder Delay Explicitly

In QuickTime movie files (.mov) and related MPEG-4 files, AAC encoded audio is carried in a sound track as a series of media samples—each media sample corresponding to an AAC encoded audio packet. A track uses an edit list (see [Edit List Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjvheza)) to indicate the range of time from the media samples to present. The edit list atom along with additional atoms known as Sample Group Structures, introduced in [Sample Group Structures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknlti), can now be used to explicitly represent encoder delay.

__Important:__ A _complete_ implementation using the sample group structures is required to explicitly represent the placement of the source signal in the encoded track. An incomplete implementation will result in unspecified interpretation by Apple software and tools. In the absence of the sample group structures, the classic solution of expecting an implicit encoding delay of 2112 samples and the edit list to start at the beginning of encoder delay will be assumed as described in the previous section.

### Edit List Atom

See [Edit Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjvg44q) and [Edit List Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjvheza) for details of edit lists in track atom structures.

A sound track of AAC encoded audio uses an edit list to indicate the placement of the source signal in the time represented by the encoded AAC packets. The media time field of the edit list must indicate the first sample to be presented and will correspond in time to the first audio sample following the encoder delay in that track. The edit list track duration field should be set to the duration of the source waveform in media samples. The edit list must not extend into the encoder delay or into any remainder samples of the encoded sound track. Note that for a single waveform encoded into a sound track, the sound track requires only a single edit list atom with one entry.

__Note:__ Track duration uses the movie timescale instead of the media timescale used by media time. If the media timescale and movie timescale differ, the track duration may not be sample accurate.

### Sample Group Structures

__Note:__ This implementation of sample group structures in QuickTime is designed to be compatible with the ISO Sample Group Structures definition and allow for future generalization. A full description of ISO 14996-12 Sample Group Structures is not required in order to provide explicit encoder delay representation. A short description of the more general characteristics of these structures is included in the descriptions below, followed by the information required for use with QuickTime.

Sample group structures of roll-group type with a constant roll distance are used to represent decoder dependencies for AAC encoded media. The sample group structures are intended to serve two purposes:

- To indicate the amount of decoder delay in AAC packets
- To signal to readers parsing QuickTime movies that the sound track includes explicit information for encoder delay and remainder samples for the AAC packets encoded in the file

  __Note:__ The effect of using sample group structures in the track in this manner is that the edit list’s media time and track duration fields do not include encoder delay, as specified above in [Edit List Atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknltm).

Two sample group structure atoms are used to represent the amount of encoder delay and remainder samples which must be trimmed.

#### Sample Group Description Atom

Sample group description atoms give information about the characteristics of sample groups. The sample group description atom has an atom type of `‘sgpd’`.

__In a general case:__

Each instance of a sample group description atom has a type code that distinguishes different sample groupings. There can be multiple instances of this atom if there is more than one sample grouping for the samples in a track. At most one instance of a sample group description with a particular grouping type exists in a track. An associated sample-to-group atom has the same value associated with that grouping type. The information or “payload data” is stored in the sample group description atom, after the entry count, as an array of entries for which the meanings vary according to the characteristics of grouping type.

For use in AAC encoder delay representation, there is one instance of a sample group description atom in a given QuickTime sound track with grouping type `‘roll’`. The specifics for audio data (`AudioRollRecovery()`) are used and articulate the rolling decode dependency. Because the sample group description atom for this purpose is describing the entirety of the AAC audio stream, the payload data field resolves to a single signed 16-bit integer representing the roll distance, which is set to -1. In other words, one AAC packet (1024 encoded PCM audio samples) preceding the media sample is indicated as being of the same type as the encoded source data, allowing the decode transform to operate over the required two AAC packets for the first media sample specified in the edit list.

__Note:__ The payload data value (roll distance in this use) of -1 is a typical value for existing AAC codecs, but the payload data can have other values. Codecs could use alternative values depending upon their implementation details.

[Figure G-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknltcny) shows the layout of this atom.

__Figure G-2__  The layout of a sample group description atom

（原归档配图未能恢复：`sample_group_description_atom.jpg`）

The sample group description atom contains the following data elements:

**Size**
: A 32-bit integer that specifies the number of bytes in this sample group description atom.

**Type**
: A 32-bit integer that identifies the atom type, set to `'sgpd'`.

**Version**
: A 1-byte specification of the version of this sample group description, set to 1.

**Flags**
: A 3-byte reserved space, set to 0

**Grouping type**
: A 32-bit integer that identifies the grouping type of this sample group description, set to `‘roll’`.

**Default length**
: A 32-bit integer indicating the length of the group entry in the payload data, set to 2 (bytes).

**Entry count**
: A 32-bit integer giving the number of entries in the payload data field, set to 1.

**Payload data**
: A 16-bit signed integer giving the roll distance, set to -1 value for AAC audio.

#### Sample-To-Group Atoms

Sample-to-group atoms are used to find the group that a sample belongs to and the associated description of that sample group. The sample-to-group atom has an atom type of `‘sbgp’`.

__In a general case:__

There may be multiple instances of sample-to-group atoms if there is more than one sample grouping for the samples in a track. Each instance of the sample-to group atom has a grouping type code that distinguishes different sample groupings. Within a track there can be at most one instance of this atom with a particular grouping type. An associated sample group description atom indicates the same value for the grouping type.

The sample-to-group atom contains a table with a sample count and group description index pairs. The sample count is the number of media samples in the run of samples with the same sample group description. The group description index is an index into the array of payload data entries in the associated sample group description atom's payload data table, the association defined by having the same grouping type value.

For use in AAC encoder delay representation, there is one sample-to-group atom instance in a given QuickTime sound track with grouping type `‘roll’` matching the single instance of the sample group description atom. The entry count field value is set to 1, indicating one entry in the table data array. That entry is describing all the AAC packets in the track. The sample count in the table data array is typically the same as the sample size atom’s number of entries field, see [Sample Size Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjxgeya), which represents the number of media samples in the track (in this use, AAC packets). For AAC encoder delay representation, the only entry in the associated sample group description atom’s payload data table is the first, which provides the value of 1 for the group description index.

[Figure G-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknltema) shows the layout of this atom.

__Figure G-3__  The layout of a sample-to-group atom

（原归档配图获取待重试：`sample-to-group_atom.jpg`）

The sample-to-group atom contains the following data elements:

**Size**
: A 32-bit integer that specifies the number of bytes in this sample-to-group atom.

**Type**
: A 32-bit integer that identifies the atom type; set to `'sbgp'`.

**Version**
: A 1-byte specification of the version of this sample-to-group atom, set to 0

**Flags**
: A 3-byte reserved space, set to 0.

**Grouping type**
: A 32-bit integer identifying the grouping type, set to `‘roll’`.

**Entry count**
: A 32-bit integer giving the number of entries in the table table data that follows.

**Table data**
: A table of sample count and group description index pairs as shown in [Figure G-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknltemi).

__Figure G-4__  The layout of the table data format

（原归档配图未能恢复：`sample_count_group_desc_index.jpg`）

**Sample count**
: A 32-bit integer that provides the number of consecutive media samples with the same sample group descriptor. The value is typically the same as in the sample size atom’s number of entries field.

**Group description index**
: A 32-bit integer the value of which is the index into the sample group description atom’s payload data table which describes the samples in this group. The index ranges from 1 to the number of payload data entries in the sample group description atom, or takes the value 0 to indicate that this group of samples is a member of no group of this type.

## Example—Representing Encoder Delay Explicitly

Consider the following example of a typical case of PCM source sound data to be encoded as AAC:

The goal is to represent the temporal position of 5 seconds of 48kHz PCM audio encoded in a 48kHz AAC sound track. Assume a media timescale of 48000 and an encoder delay of 2112. For convenience, assume a movie timescale of 48000 as well.

### Audio Data

Source PCM audio data prior to encoding:

- Sample rate: 48000 per second
- Sample count: 240000 PCM samples (5 seconds)
- Duration in timescale ticks: 240000 (with media timescale the same as sample rate)

AAC in the encoded sound track:

- Encoder delay: 2112 audio samples
- Samples per AAC packet: 1024
- Decoder delay: 1024 samples (or 1 AAC packet)
- Number of AAC packets: 237 (=((2112+240000) / 1024) rounded up to an integer value)
- Sample count: 242688 (= 237 \* 1024)
- Remainder samples: 576 (= 242688 - (2112 + 240000))

The transformation from source PCM to encoded AAC results in a sound track with 237 AAC media samples corresponding to 242688 PCM audio samples if decoded and presented in its entirety. Of that total, only 240000 audio samples of source starting at sample offset 2112 (skipping the first 2111 samples) are to be presented. From this, the edit list atom and sample group atom described in [Track Structures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknltena) are used to represent the encoder delay.

### Track Structures

Based on the [Audio Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknltemy), the following edit list and sample group atoms are used to represent the encoder delay.

The edit list atom contains this data:

- Size: 28
- Type: `‘elst’`
- Version: 0
- Flags: 0
- Entry count: 1
- Number of entries: 1

with this table data:

- Track duration: 240000 (source duration)
- Media time: 2112 (accounts for the encoder delay)
- Media rate: 1.0

__Note:__ For this example, the conventional encoder delay value of 2112 audio samples has been used. Alternative encoder delay values can also be explicitly represented with this mechanism, depending upon codec implementation.

The sample group description atom contains this data:

- Size: 26
- Type: `‘sgpd’`
- Version: 1
- Flags: 0
- Grouping type: `‘roll’`
- Default length: 2
- Entry count: 1

with this table data:

- payload data: -1

__Note:__ Recall that the payload data value could be an alternative value, depending upon the particular codec in use. -1 is typical for current AAC codecs.

And the sample-to-group atom contains this data:

- Size: 22
- Type: `‘sbgp’`
- Version: 0
- Flags: 0
- Grouping type: `‘roll’`
- Entry count: 1

with this table data:

- Sample count: 237 (number of AAC packets representing the encoder delay, original audio samples, and remainder audio samples)
- Group description index: 1 (corresponds to first and only entry in the sample group description atom’s payload data table for these sample units)

Other things to note from this example:

- You cannot use the edit list by itself to determine the encoder delay or remainder sample count. The sample group atoms provide the encoder delay. The placement of the end of the edit in a compressed audio packet allows calculation of the remainder samples.
- If the encoder delay was the theoretical minimum for AAC of 1024, then the media time field value in the edit list table data shown in this example would be 1024, not 2112.

## Summary—Using Track Structures to Represent Encoder Delay

When using sample group structures in representing encoder delay for AAC sound tracks:

- Include a version 1 sample group description atom with grouping type set to `‘roll’`. Set default length to 2 (bytes) for audio entries. Follow that with the payload data: the typical value is -1, meaning one preceding AAC packet, which is the theoretical minimum decoder delay of 1024 samples.
- Include a version 0 sample-to-group atom with a `'roll'` grouping type. By including this, you associate the AAC packets with the corresponding sample group description atom. All AAC packets including the encoder delay must be associated with the sample group in the table data’s sample count field. Typically, the sample count for this sample-to-group atom’s table data corresponds with the number of media samples in the track.

These two sample group structure atoms in addition to the edit list atom, properly composed, form a complete implementation to explicitly represent the temporal position of the source audio samples in an AAC encoded track.

[Next](Document%20Revision%20History.md)[Previous](Profile%20Atom%20Guidelines.md)

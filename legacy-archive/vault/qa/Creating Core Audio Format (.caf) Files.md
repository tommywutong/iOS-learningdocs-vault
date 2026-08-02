---
title: Creating Core Audio Format (.caf) Files
apple_id: DTS40008152
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2009-01-07'
source_url: https://developer.apple.com/library/archive/qa/qa1534/_index.html
archived_at: '2026-07-18T02:32:15.233086Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1534

# Creating Core Audio Format (.caf) Files

## Q:  I'm trying to author Core Audio Format files using QuickTime Player but it doesn't have a .caf file exporter. How can I create .caf files on Mac OS X?

A: I'm trying to author Core Audio Format files using QuickTime Player but it doesn't have a .caf file exporter. How can I create .caf files on Mac OS X?

While QuickTime supports importing Core Audio Format (`.caf`) files, it does not currently provide an audio exporter capable of creating these files.

The easiest way to create a Core Audio Format file is by using the `afconvert` tool located in `/usr/bin/`.

`afconvert` (a.k.a. Audio File Convert) will convert a source audio file to a new audio file and supports a large set of file formats, data formats and encoding options.

For example, Listing 1 demonstrates how you might use `afconvert` from the Terminal to create a `.caf` file containing AAC audio encoded with an average data rate of 192kbps.

__Listing 1__  Convert an .aif file to a .caf file.

```
afconvert -v -f 'caff' -d aac -s 1 -b 192000 MySource.aif MyOutput.caf
```



```
NAME      afconvert -- Audio File Convert  SYNOPSIS      afconvert [option...] input_file [output_file]  DESCRIPTION      Audio File Convert will convert a source audio file to a new audio file of the specified file type containing audio data of the specified data type.  OPTIONS (may appear before or after arguments)      { -f | --file } file_format:         '3gpp' = 3GP Audio (.3gp)                    data_formats: 'aac ' 'samr'          '3gp2' = 3GPP2 Audio (.3g2)                    data_formats: 'aac ' 'samr'          'adts' = AAC ADTS (.aac, .adts)                    data_formats: 'aac '          'ac-3' = AC3 (.ac3)                    data_formats: 'ac-3'          'AIFC' = AIFC (.aifc, .aiff, .aif)                    data_formats: I8 BEI16 BEI24 BEI32 BEF32                                   BEF64 UI8 'ulaw' 'alaw' 'MAC3' 'MAC6'                                   'ima4' 'QDMC' 'QDM2' 'Qclp' 'agsm'          'AIFF' = AIFF (.aiff, .aif)                    data_formats: I8 BEI16 BEI24 BEI32          'amrf' = AMR (.amr)                    data_formats: 'samr'          'caff' = Apple CAF (.caf)                    data_formats: '.mp1' '.mp2' '.mp3' 'MAC3' 'MAC6'                                   'QDM2' 'QDMC' 'Qclp' 'Qclq' 'aac ' 'aacl'                                   'agsm' 'alac' 'alaw' 'drms' 'dvca' 'dvi '                                   'dvi8' 'ilbc' 'ima4' 'lpc ' I8 BEI16                                   BEI24 BEI32 BEF32 BEF64 LEI16 LEI24                                   LEI32 LEF32 LEF64 'ms\x00\x02' 'ms\x00\x11' 'ms\x001'                                   'ms\x00U' 'samr' 'ulaw' 'vdva'          'MPG1' = MPEG Layer 1 (.mp1, .mpeg, .mpa)                    data_formats: '.mp1'          'MPG2' = MPEG Layer 2 (.mp2, .mpeg, .mpa)                    data_formats: '.mp2'          'MPG3' = MPEG Layer 3 (.mp3, .mpeg, .mpa)                    data_formats: '.mp3'          'mp4f' = MPEG4 Audio (.mp4)                    data_formats: 'aac ' 'aacl'          'm4af' = MPEG4 Audio (.m4a)                    data_formats: 'aac ' 'aacl' 'alac'          'NeXT' = NeXT/Sun (.snd, .au)                    data_formats: I8 BEI16 BEI24 BEI32 BEF32                                   BEF64 'ulaw'          'Sd2f' = Sound Designer II (.sd2)                    data_formats: I8 BEI16 BEI24 BEI32          'WAVE' = WAVE (.wav)                    data_formats: UI8 LEI16 LEI24 LEI32 LEF32                                   LEF64 'ulaw' 'alaw'      { -d | --data } data_format[@sample_rate_hz][/format_flags][#frames_per_packet] :         [-][BE|LE]{F|[U]I}{8|16|24|32|64} (PCM)             e.g. BEI16   F32@44100         or a data format appropriate to file format, as above         format_flags: hex digits, e.g. '80'         Frames per packet can be specified for some encoders, e.g.: samr#12     { -c | --channels } number_of_channels         add/remove channels without regard to order     { -l | --channellayout } layout_tag         layout_tag: name of a constant from CoreAudioTypes.h           (prefix "kAudioChannelLayoutTag_" may be omitted)         if specified once, applies to output file; if twice, the first           applies to the input file, the second to the output file     { -b | --bitrate } bit_rate_bps          e.g. 128000     { -q | --quality } codec_quality         codec_quality: 0-127     { -r | --src-quality } src_quality         src_quality (sample rate converter quality): 0-127     { --src-complexity } src_complexity         src_complexity (sample rate converter complexity): line, norm, bats     { -v | --verbose }         print progress verbosely     { -s | --strategy } strategy         bitrate allocation strategy for encoding an audio track         0 for CBR, 1 for ABR, 2 for VBR_constrained, 3 for VBR     { -t | --tag }         If encoding to CAF, store the source file's format and name in a user chunk.         If decoding from CAF, use the destination format and filename found in a user chunk.     --read-track track_index         For input files containing multiple tracks, the index (0..n-1) of the track         to read and convert.     --prime-method method         decode priming method (see AudioConverter.h)     --no-filler         don't page-align audio data in the output file     { -u | --userproperty } property value         set an arbitrary property to a given value         property must be a four char code         value is a signed 32-bit integer         A maximum of 8 properties may be set         e.g. use '-u vbrq <sound_quality>' to set the sound quality level (<sound_quality>: 0-127)               for VBR encoding strategy (i.e., -s 3)      { -h | --help }         print help
```


[Introduction to Apple Core Audio Format Specification](https://developer.apple.com/documentation/MusicAudio/Reference/CAFSpec/CAF_intro/chapter_1_section_1.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-01-07 | New document that describes how to use afconvert to create .caf files |


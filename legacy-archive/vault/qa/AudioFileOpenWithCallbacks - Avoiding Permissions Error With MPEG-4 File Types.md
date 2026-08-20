---
title: AudioFileOpenWithCallbacks - Avoiding Permissions Error With MPEG-4 File Types
apple_id: DTS40009346
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/qa/qa1676/_index.html
archived_at: '2026-07-18T02:33:45.403190Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1676

# AudioFileOpenWithCallbacks - Avoiding Permissions Error With MPEG-4 File Types

## Q:  We're using `AudioFileOpenWithCallbacks` for playback of audio data stored in memory and provide the appropriate procedures for reading, writing and so on. However, we encounter a `kAudioFilePermissionsError` when working with MPEG-4 file containers. What's wrong?

A: We're using `AudioFileOpenWithCallbacks` for playback of audio data stored in memory and provide the appropriate procedures for reading, writing and so on. However, we encounter a `kAudioFilePermissionsError` when working with MPEG-4 file containers. What's wrong?

`AudioFileOpenWithCallbacks` will open an audio file (represented by the `AudioFileID` opaque data type) using callbacks you provide for reading data, writing data and getting/setting size information. These callbacks may be used to provide audio file data from a source other than a physical file (for example memory) and lets you take advantage of the standard AudioFile APIs such as `AudioFileReadPackets` to work with this audio data.

__Listing 1__  `AudioFileOpenWithCallbacks`

```
OSStatus AudioFileOpenWithCallbacks(void *inClientData,                                     AudioFile_ReadProc inReadFunc,                                     AudioFile_WriteProc inWriteFunc,                                     AudioFile_GetSizeProc inGetSizeFunc,                                     AudioFile_SetSizeProc inSetSizeFunc,                                     AudioFileTypeID inFileTypeHint,                                     AudioFileID *outAudioFile); Parameters:  inClientData - A pointer to a constant passed to your callbacks. The constant should contain any information you use to manage the state for reading data from the file.  inReadFunc - A callback function invoked when the audio file object wants to read data.  inWriteFunc - A callback function called when the audio file object wants to write data.  inGetSizeFunc - A callback function called when the audio file object wants to know the file size.  inSetSizeFunc - A callback function called when the audio file object wants to set the file size.  inFileTypeHint - A hint about the type of the designated file. For example, kAudioFileAAC_ADTSType, kAudioFileMP3Type and so on.  outAudioFile - On output, a pointer to the newly opened file ID.
```


There is however a limitation when working with MPEG-4 file types which include; .mp4 (`kAudioFileMPEG4Type`), .m4a (`kAudioFileM4AType`), .3g2 (`kAudioFile3GP2Type`) and .3gp (`kAudioFile3GPType`).

AudioFile does __not__ currently support writing to existing files of these types.

Therefore, if you provide the `inWriteFunc` procedure it is an indication to `AudioFileOpenWithCallbacks` that the file is being opened for writing, which in turn results in the `kAudioFilePermissionsError` being returned.

Since you can't write to these files, the `AudioFile_WriteProc` is not required and should not be used. Setting the `inWriteFunc` to `NULL` solves the problem.

__Listing 2__  `AudioFileOpenWithCallbacks` with a `NULL` `inWriteFunc` and `inSetSizeFunc`

```
static OSStatus MyAudioFile_ReadProc(void *inClientData, SInt64   inPosition, UInt32 requestCount,                                      void *buffer, UInt32 *actualCount) {     // this is my read proc.     ... }  {     ...      AudioFileID myAudioFileID = 0;     OSStatus result;      result = AudioFileOpenWithCallbacks(self, MyAudioFile_ReadProc, NULL, MyAudioFile_GetSizeProc, NULL,                                         kAudioFileMPEG4Type, &myAudioFileID);      ... }
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-27 | New document that describes how to avoid a kAudioFilePermissionsError error with MPEG-4 files when using AudioFileOpenWithCallbacks. |


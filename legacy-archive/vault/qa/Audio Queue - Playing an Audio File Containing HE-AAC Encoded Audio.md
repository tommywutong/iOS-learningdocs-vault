---
title: Audio Queue - Playing an Audio File Containing HE-AAC Encoded Audio
apple_id: DTS40008751
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2009-04-21'
source_url: https://developer.apple.com/library/archive/qa/qa1639/_index.html
archived_at: '2026-07-18T02:33:02.937240Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1639

# Audio Queue - Playing an Audio File Containing HE-AAC Encoded Audio

## Q:  I'm trying to play an HE-AACv1 encoded audio file, but `kAudioFilePropertyDataFormat` reports the format as plain 'aac '. How do I retrieve the appropriate `AudioStreamBasicDescription` to configure the Audio Queue correctly?

A: I'm trying to play an HE-AACv1 encoded audio file, but `kAudioFilePropertyDataFormat` reports the format as plain 'aac '. How do I retrieve the appropriate `AudioStreamBasicDescription` to configure the Audio Queue correctly?

HE-AAC is a layered format and has at its core the base layer of AAC. The encoded data for a layered audio format can be made of several layers that could have different sample rates, different channel layouts and may be decoded to multiple destination formats. Any AAC decoder would be able to decode the AAC base layer of an HE-AAC bitstream.

Core Audio represents this layering through the notion of an audio format list containing one or more audio format list items, each item representing an available format of the encoded data in the file.

For example, a hypothetical file encoded as HE-AACv1 may return an audio format list containing two audio format list items, describing the available formats as:

- HE-AAC, 44.1KHz, 2 channels (enhanced layer): Format ID 'aach'
- AAC, 22.05KHz, 2 channels (base layer): Format ID 'aac '

In other words, the encoded data in the file may be rendered as either HE-AAC or AAC-LC.

The audio format list for an audio file is retrieved by calling `AudioFileGetProperty` using the `kAudioFilePropertyFormatList` property.

The `kAudioFilePropertyFormatList` property will return an array of `AudioFormatListItem` structures (declared in `AudioToolbox/AudioFormat.h`), one for each alternate format represented as a `AudioStreamBasicDescription`, `AudioChannelLayoutTag` pair.


```
/*!     @struct		AudioFormatListItem     @abstract   this struct is used as output from the kAudioFormatProperty_FormatList property     @field      mASBD                      an AudioStreamBasicDescription     @field      mChannelLayoutTag                      an AudioChannelLayoutTag */ struct AudioFormatListItem {     AudioStreamBasicDescription		mASBD;     AudioChannelLayoutTag		mChannelLayoutTag; }; typedef struct AudioFormatListItem AudioFormatListItem;
```

You could then choose the appropriate `AudioStreamBasicDescription` to use with `AudioQueueNewOutput` when creating a new Audio Queue object for playback.

Since platform capabilities can vary (HE-AAC decoding may be available on one platform but not on another), Core Audio also has the notion of a first playable format. The first playable format is the highest quality (or best) format the platform is capable of playing back as determined at run-time.

Use the `AudioFormatGetProperty` API with the `kAudioFormatProperty_FirstPlayableFormatFromList` property to retrieve an index value for the `AudioFormatListItem` in the audio format list array that describes the highest quality format the device is capable of playing back.

Here's the same audio format list from before with index values added.

- Index 0 - HE-AAC, 44.1KHz, 2 channels (enhanced layer): Format ID 'aach'
- Index 1 - AAC, 22.05KHz, 2 channels (base layer): Format ID 'aac '

Listing 1 demonstrates how the `kAudioFilePropertyFormatList` and `kAudioFormatProperty_FirstPlayableFormatFromList` properties can be used together to easily retrieve the richest (or best) supported audio format description for playback.

__Listing 1__

```c
#include "CAStreamBasicDescription.h"  AudioFormatListItem GetFirstPlayableAudioFormatForFile(AudioFileID inFileID) {     AudioFormatListItem *formatListPtr = NULL;     AudioFormatListItem formatItem = {0};     UInt32 propertySize;      OSStatus status = noErr;      if (NULL == inFileID) return formatItem;      status = AudioFileGetPropertyInfo(inFileID, kAudioFilePropertyFormatList, &propertySize, NULL);     if (noErr == status) {          // allocate memory for the format list items         formatListPtr = (AudioFormatListItem *)malloc(propertySize);         if (NULL == formatListPtr) return formatItem;          // get the list of Audio Format List Item's         status = AudioFileGetProperty(inFileID, kAudioFilePropertyFormatList, &propertySize, formatListPtr);         if (noErr == status) {             // print out some helpful information             UInt32 numFormats = propertySize / sizeof(AudioFormatListItem);             printf ("This file has a %d layered data format:\n", numFormats);             for (unsigned int i = 0; i < numFormats; ++i) {                 CAStreamBasicDescription(formatListPtr[i].mASBD).Print();             }              UInt32 itemIndex;             UInt32 indexSize = sizeof(itemIndex);              // get the index number of the first playable format -- this index number will be for             // the highest quality layer the platform is capable of playing             status = AudioFormatGetProperty(kAudioFormatProperty_FirstPlayableFormatFromList, propertySize,                                             formatListPtr, &indexSize, &itemIndex);             if (noErr == status) {                 printf ("Returning AudioFormatListItem at index %d.\n", itemIndex);                 // copy the format item at index we want returned                 formatItem =  formatListPtr[itemIndex];             }         }          free(formatListPtr);     }      return formatItem; }
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-04-21 | First Version |
|  | New document that describes how to use the FormatList property to chose the richest available format for AQ playback. |


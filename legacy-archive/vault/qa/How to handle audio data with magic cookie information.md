---
title: How to handle audio data with magic cookie information
apple_id: DTS10002342
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-08-09'
source_url: https://developer.apple.com/library/archive/qa/qa1318/_index.html
archived_at: '2026-07-18T02:30:22.677972Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1318

# How to handle audio data with magic cookie information

## Q:  How do I handle audio data with magic cookies when using an AudioConverter?

A: Some audio formats have a magic cookie associated with them that is required to decompress audio data. The term "Magic cookie" (some times called magic number(s)) refers to information included in audio file header used to describe data formats. When converting audio data you must check to see if the format of the audio data you are attempting to convert has a magic cookie. If the audio data format has a magic cookie associated with it, you must add this information to the instance of the audio converter being used. This is done by using the `AudioConverterSetProperty` API along with the `kAudioConverterDecompressionMagicCookie` property and the magic cookie data blob. This is needed to correctly decompress the Audio File.

__Listing 1__  Using Magic Cookie information with Audio Converters.

```
 AudioConverterRef *conv;
   AudioFileID *musicFileID;
   UInt32    magicCookieSize = 0;
   //...
   // Open a new AudioFile and create a new AudioConverter here.
   // ...
   //Get Magic Cookie info(if exists) and pass it to converter
   err = AudioFileGetPropertyInfo(*musicFileID,
                                        kAudioFilePropertyMagicCookieData,
                                        &amp;magicCookieSize,
                                        NULL);

     if (err == noErr)
    {
        void *magicCookie = calloc (1, magicCookieSize);
        if (magicCookie)
        {
            err = AudioFileGetProperty (*musicFileID,
                                  kAudioFilePropertyMagicCookieData,
                                  &amp;magicCookieSize,
                                  magicCookie);

            // Give the AudioConverter the magic cookie decompression
            //params if any exist
            if (err == noErr)
            {
                err = AudioConverterSetProperty( *conv,
                     kAudioConverterDecompressionMagicCookie,
                     magicCookieSize,
                     magicCookie);
            }
            if (magicCookie) free(magicCookie);
        }
    } else //OK if audio doesn't need magic cookie data
        err = noErr; //reset error status
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-09 | Editorial |
| 2011-07-18 | Editorial |
| 2003-10-22 | New document that how to handle sound files with magic cookies when using an AudioConverter. |


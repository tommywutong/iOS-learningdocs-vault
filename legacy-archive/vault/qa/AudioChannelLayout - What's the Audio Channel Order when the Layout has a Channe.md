---
title: AudioChannelLayout - What's the Audio Channel Order when the Layout has a Channel
  Bitmap?
apple_id: DTS40008612
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2009-04-12'
source_url: https://developer.apple.com/library/archive/qa/qa1638/_index.html
archived_at: '2026-07-18T02:33:02.902046Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1638

# AudioChannelLayout - What's the Audio Channel Order when the Layout has a Channel Bitmap?

## Q:  My multichannel QuickTime audio Track has an `AudioChannelLayout` with a channel bitmap. The `mChannelLayoutTag` is `kAudioChannelLayoutTag_UseChannelBitmap` and the `mChannelBitmap` field contains the value 0x3F-- Left, Right, Center, LFEScreen, LeftSurround, RightSurround. How do I know what order these channels appear in the audio buffer?

A: My multichannel QuickTime audio Track has an `AudioChannelLayout` with a channel bitmap. The `mChannelLayoutTag` is `kAudioChannelLayoutTag_UseChannelBitmap` and the `mChannelBitmap` field contains the value 0x3F-- Left, Right, Center, LFEScreen, LeftSurround, RightSurround. How do I know what order these channels appear in the audio buffer?

If an `AudioChannelLayout` has a bitmap, there is only one order the channels present can be in. This order is commonly known as USB order and is the same order the bits are defined in the Channel Bitmap Constants enumeration, see `CoreAudio/CoreAudioTypes.h`.


```
/*!     @enum           Channel Bitmap Constants     @abstract       These constants are for use in the mChannelBitmap field of an                     AudioChannelLayout structure. */ enum {     kAudioChannelBit_Left                       = (1L<<0),     kAudioChannelBit_Right                      = (1L<<1),     kAudioChannelBit_Center                     = (1L<<2),     kAudioChannelBit_LFEScreen                  = (1L<<3),     kAudioChannelBit_LeftSurround               = (1L<<4),     kAudioChannelBit_RightSurround              = (1L<<5),  ... };
```

Therefore, in the bitmap described above, the first channel is Left, then Right, then Center, then LFE, then Left Surround and finally Right Surround.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-04-12 | New document that explains the audio channel order when a channel layout is tagged as kAudioChannelLayoutTag_UseChannelBitmap. |


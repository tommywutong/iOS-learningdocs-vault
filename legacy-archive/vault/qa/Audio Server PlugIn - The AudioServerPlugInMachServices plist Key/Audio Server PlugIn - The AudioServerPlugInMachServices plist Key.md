---
title: Audio Server PlugIn - The AudioServerPlugIn_MachServices plist Key
apple_id: DTS40014015
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2013-11-19'
source_url: https://developer.apple.com/library/archive/qa/qa1811/_index.html
archived_at: '2026-07-18T02:34:53.444176Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1811

# Audio Server PlugIn - The AudioServerPlugIn_MachServices plist Key

## Q:  How does my user-space plug-in talk to other processes?

A: An AudioServerPlugIn operates in a limited environment. First and foremost, an AudioServerPlugIn may not make any calls to the client HAL API in the CoreAudio.framework. This will result in undefined (but generally bad) behavior.

Further, the host process is sandboxed. As such, an AudioServerPlugIn may only read files in its bundle in addition to the system libraries and frameworks. It may not access user documents or write to any filesystem locations other than the system's cache and temporary directories as derived through Apple API. The host provides a means for the plug-in to store and retrieve data from persistent storage.

An AudioServerPlugIn may communicate with other processes on the system. However, the plug-in must list the name of the mach services to be accessed in the plug-in bundle's `info.plist` in a key named "`AudioServerPlugIn_MachServices`". The value of this key is an array of the names of the mach services that need to be accessed.

__Figure 1__  AudioServerPlugIn_MachServices Usage.

!!

```
<key>AudioServerPlugIn_MachServices</key>
<array>
 <string>com.yourcompanynamehere.audio.HypotheticalAudioDriverXPCService</string>
</array>
```

See the `AudioServerPlugIn.h` header file for further details regarding Audio Server plug-ins.

[Core Audio User-Space Driver Examples](https://developer.apple.com/library/mac/samplecode/AudioDriverExamples/Introduction/Intro.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-11-19 | First Version |
|  | New document that discusses the use of the AudioServerPlugIn_MachServices key to talk to other processes. |


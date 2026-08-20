---
title: qtstreaming.win
apple_id: DTS10001052
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreaming.win/Listings/Readme_txt.html
archived_at: '2026-07-26T19:53:06.404856Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreaming.win](qtstreaming.win.md)


[Next](ComponentVideoRTP-RTPMPComponentVideo-Headers-ComponentVideoPayload.h.md)[Previous](qtstreaming.win.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Readme.txt

```
GETTING STARTED

    The projects in this folder are all MS-Dev Visual C/C++ projects
    that expect to find the QuickTime header files and libraries in the
    folder QTDevWin, which is assumed to be in the parent of the parent
    of the folder containing the .dsw files. If you have placed the required
    header files and libraries elsewhere, you will need to change
    the access paths of the projects.

QUICKTIME STREAMING SAMPLE CODE

    This folder contains sample code for QuickTime Streaming
    RTPMediaPacketizer components and RTPReassembler components.
    These components packetize or reassemble multimedia data that
    is streamed over RTP.

Sample Code Organization

    The sample code is organized into four MS-Dev Visual C/C++
    (version 5.0) projects, two for Component Video RTP components and
    two for IMA Audio RTP components.  Each project defines two
    targets, Release and Debug versions of a Win32 packetizer DLL or
    a Win32 reassembler DLL.

Building Win32 Component (.qtx) Files

    Each Win32 component file can be built in three stages.  First
    build the DLL, then build the QTML resources using Rez.exe
    (included in the QuickTime SDK), and, finally, combine the DLL
    and resources into a single .qtx file using RezWack.exe (also
    in the QuickTime SDK).

    Each project contains two batch files to facilitate this
    process, one for each DLL target. The batch files are called
    automatically when you rebuild the project.
```

[Next](ComponentVideoRTP-RTPMPComponentVideo-Headers-ComponentVideoPayload.h.md)[Previous](qtstreaming.win.md)


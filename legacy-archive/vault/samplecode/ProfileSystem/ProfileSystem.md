---
title: ProfileSystem
apple_id: DTS10003566
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreFoundation
published: '2005-05-05'
source_url: https://developer.apple.com/library/archive/samplecode/ProfileSystem/Introduction/Intro.html
archived_at: '2026-07-18T03:19:36.721834Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# ProfileSystem

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2005-05-05 Shows how to obtain the same information that System Profiler displays. |
| __Build Requirements:__ | Mac OS X 10.3.8, XCode 1.1 |
| __Runtime Requirements:__ | Mac OS X 10.3.8 or greater |

ProfileSystem demonstrates the use of the system_profiler shell command and how it can be called by a Core Foundation application to retrieve the same information that is displayed in the System Profiler utility. The sample uses the UNIX popen call to open a stream and read the results of the system_profiler command. The resultant data is then read into a buffer and converted to a CFArray using the CFPropertyListCreateFromXMLData call. For this sample, the CFArray is then parsed for specific information about PCI and USB devices.

[Next](main.c.md)


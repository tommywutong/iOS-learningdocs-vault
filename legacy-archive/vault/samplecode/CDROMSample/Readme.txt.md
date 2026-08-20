---
title: CDROMSample
apple_id: DTS10000423
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2011-05-05'
source_url: https://developer.apple.com/library/archive/samplecode/CDROMSample/Listings/Readme_txt.html
archived_at: '2026-07-18T03:02:24.975236Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CDROMSample](CDROMSample.md)


[Next](CDROMSample-CDROMSample.c.md)[Previous](CDROMSample.md)

# Readme.txt

```
CDROMSample
Command-line tool demonstrating how to use IOKitLib to find CD-ROM media mounted on the system. It also shows how to open, read raw sectors from, and close the drive.

Version: 1.3 - 10/17/2002

Techniques shown are:
- Finding ejectable CD-ROM media
- Locating the BSD /dev/rdisk* node name corresponding to that media 
- Opening the /dev/rdisk* node
- Retrieving the media's preferred block size
- Reading a sector from the media 
- Closing the device 

Note that /dev/*disk* nodes for removable media are owned by the currently logged in user. Nodes for non-removable media are owned by root. 

Version: 1.4 - 8/17/2005

- Updated to produce a universal binary.
- Use kIOMasterPortDefault instead of older IOMasterPort function.

Version: 1.5 - 04/27/2011

- Now builds with Xcode 4.
```

[Next](CDROMSample-CDROMSample.c.md)[Previous](CDROMSample.md)


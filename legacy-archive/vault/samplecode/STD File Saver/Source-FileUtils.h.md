---
title: STD File Saver
apple_id: DTS10000307
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/STD_File_Saver/Listings/Source_FileUtils_h.html
archived_at: '2026-07-18T03:22:47.702249Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [STD File Saver](STD%20File%20Saver.md)


[Next](Source-MyPACK.r.md)[Previous](Source-FileUtils.c.md)

# Source/FileUtils.h

```
OSErr SelectOutputFile(FSSpec *fileSpec);
OSErr OpenOutputFile(FSSpec *fileSpec, short *refnum, Boolean isResource);
OSErr CloseOutputFile(short refnum, Boolean isResource);
OSErr WritePictData(short refnum, Handle pictHandle, short pageNum, Boolean isResource);
OSErr WriteCLUTData(short refnum);
```

[Next](Source-MyPACK.r.md)[Previous](Source-FileUtils.c.md)


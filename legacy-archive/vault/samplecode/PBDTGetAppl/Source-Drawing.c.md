---
title: PBDTGetAppl
apple_id: DTS10000042
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBDTGetAppl/Listings/Source_Drawing_c.html
archived_at: '2026-07-18T03:18:19.759710Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBDTGetAppl](PBDTGetAppl.md)


[Next](Source-ErrMsg.c.md)[Previous](Headers-MenuDispatch.h.md)

# Source/Drawing.c

```swift
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------
    The Update Event Handler calls this routine when it
    is time to update a window.

    The window to be updated is passed in, just draw it, or case on window type
    or whatever.    
    You don't have to erase first, it has been done for you by the update event handler

    Also, the printing routine will call this too.

    This is not really using a document model architecture.

*/

void DrawImage(GrafPtr graf)
{
    PicHandle   pict;

    pict = GetPicture(128);
    DrawPicture(pict,&graf->portRect);  
}
```

[Next](Source-ErrMsg.c.md)[Previous](Headers-MenuDispatch.h.md)


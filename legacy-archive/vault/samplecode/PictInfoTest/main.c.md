---
title: PictInfoTest
apple_id: DTS10000146
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PictInfoTest/Listings/main_c.html
archived_at: '2026-07-18T03:19:00.260472Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PictInfoTest](PictInfoTest.md)


[Next](Commands.c.md)[Previous](PictInfoTest.md)

# main.c

```
void InitToolbox(void);

void InitToolbox()
{
    InitGraf((Ptr) &qd.thePort);
    InitFonts();
    InitWindows();
    InitMenus();
    FlushEvents(everyEvent,0);
    TEInit();
    InitDialogs(0L);
    InitCursor();
}

main()
{
    InitToolbox();

    return 0;
}
```

[Next](Commands.c.md)[Previous](PictInfoTest.md)


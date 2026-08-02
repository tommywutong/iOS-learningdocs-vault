---
title: Notification Hacks
apple_id: DTS10000194
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Notification_Hacks/Listings/GestaltTalk_GestaltTalkSelector_c.html
archived_at: '2026-07-18T03:17:05.628165Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Notification Hacks](Notification%20Hacks.md)


[Next](https://developer.apple.com/library/archive/samplecode/Notification_Hacks/Listings/NotificationMon_%C3%86%C2%92_Headers_Event_h.html)[Previous](GestaltTalk-GestaltTalkCommands.c.md)

# GestaltTalk/GestaltTalkSelector.c

```
/*

    GestaltTalkSelector.c
    ---------------------

    This selector returns the address to GestaltTalk globals,
    which includes a pointer to the data buffer.

*/

pascal OSErr GestaltTalkGestalt(long selector, long *response)
{

    asm {
            bsr.s   @skipStorage        ; skip over the data and push address
            dc.l    0x00                ; this is the gestaltTalk globals record
            dc.l    0x00                ;
            dc.l    0x00
            dc.l    0x00
            dc.l    0x00
        @skipStorage:
            movea.l response,a0
            move.l  (sp)+,(a0)          ; put the address of data into response
    }
    return  0;
}
```

[Next](https://developer.apple.com/library/archive/samplecode/Notification_Hacks/Listings/NotificationMon_%C3%86%C2%92_Headers_Event_h.html)[Previous](GestaltTalk-GestaltTalkCommands.c.md)


---
title: ExampleVideoPanel
apple_id: DTS10000800
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ExampleVideoPanel/Listings/Includes_ExampleVideoPanelDispatch_h.html
archived_at: '2026-07-18T03:07:57.975626Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ExampleVideoPanel](ExampleVideoPanel.md)


[Next](Includes-ExampleVideoPanelPrivate.h.md)[Previous](Includes-ExampleVideoPanel.h.md)

# Includes/ExampleVideoPanelDispatch.h

```
    ComponentComment ("SGPanelDispatch.h for the SG panel")

    ComponentSelectorOffset (6)

    ComponentRangeCount (3)
    ComponentRangeShift (8)
    ComponentRangeMask  (FF)

    ComponentStorageType (Handle)

    ComponentRangeBegin (0)
        ComponentError (Target)
        ComponentError (Register)
        StdComponentCall    (Version)
        StdComponentCall    (CanDo)
        StdComponentCall    (Close)
        StdComponentCall    (Open)
    ComponentRangeEnd (0)


    ComponentRangeUnused (1)
    ComponentRangeUnused (2)

    ComponentRangeBegin (3)
        ComponentCall                       (PanelGetDitl)
        ComponentCall                       (PanelGetTitle)
        ComponentCall                       (PanelCanRun)
        ComponentCall                       (PanelInstall)
        ComponentCall                       (PanelEvent)
        ComponentCall                       (PanelItem)
        ComponentCall                       (PanelRemove)
        ComponentCall                       (PanelSetGrabber)
        ComponentCall                       (PanelSetResFile)
        ComponentCall                       (PanelGetSettings)
        ComponentCall                       (PanelSetSettings)
        ComponentCall                       (PanelValidateInput)
        ComponentError                      (PanelSetEventFilter)
    ComponentRangeEnd (3)
```

[Next](Includes-ExampleVideoPanelPrivate.h.md)[Previous](Includes-ExampleVideoPanel.h.md)


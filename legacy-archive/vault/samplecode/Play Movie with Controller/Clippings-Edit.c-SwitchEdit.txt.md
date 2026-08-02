---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Clippings_Edit_c_SwitchEdit_txt.html
archived_at: '2026-07-18T03:19:10.182609Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Clippings-Events.c-Draw.txt.md)[Previous](Clippings-Edit.c-SelectNone.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Clippings/Edit.c/SwitchEdit.txt

```
        case IDM_EDITUNDO:
            MCUndo(myMC);
            (**myWindowObject).fIsDirty = true;
            break;

        case IDM_EDITCUT:
            myEditMovie = MCCut(myMC);
            (**myWindowObject).fIsDirty = true;
            break;

        case IDM_EDITCOPY:
            myEditMovie = MCCopy(myMC);
            break;

        case IDM_EDITPASTE:
            MCPaste(myMC, NULL);
            (**myWindowObject).fIsDirty = true;
            break;

        case IDM_EDITCLEAR:
            MCClear(myMC);
            (**myWindowObject).fIsDirty = true;
            break;

        case IDM_EDITSELECTALL:
            SelectAllMovie(myMC);
            break;

        case IDM_EDITSELECTNONE:
            SelectNoneMovie(myMC);
            break;
```

[Next](Clippings-Events.c-Draw.txt.md)[Previous](Clippings-Edit.c-SelectNone.txt.md)


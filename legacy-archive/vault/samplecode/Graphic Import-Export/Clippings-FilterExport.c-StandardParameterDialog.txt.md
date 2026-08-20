---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_FilterExport_c_StandardParameterDialog_txt.html
archived_at: '2026-07-18T03:10:57.969123Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-FilterExport.c-Step1.txt.md)[Previous](Clippings-FilterExport.c-SetOutputFile.txt.md)

# Clippings/FilterExport.c/StandardParameterDialog.txt

```
    err = QTCreateStandardParameterDialog( videoFilterList, // list of effects
                                           videoFilter,     // on return, this atom container holds an effect description for the effect selected 
                                           pdOptionsCollectOneValue | // options to control the behavior of the dialog
                                           pdOptionsModalDialogBox,
                                           &dialog );       // returns a reference to the dialog box

    // set up a preview for the source
    // creates a new QuickDraw picture handle containing the image currently in use by the graphics import component
    err = GraphicsImportGetAsPicture( importer, &previewParameter.sourcePicture );
    previewParameter.sourceID = 1;

    // change some of the default behaviors of the standard parameter dialog box.
    QTStandardParameterDialogDoAction( dialog,                      // dialog box reference
                                       pdActionSetPreviewPicture,   // action to perform
                                       &previewParameter );         // the (optional) parameter to the action

    // show the dialog and run it                               
    // passing a NULL event here causes QuickTime to take over until the dialog is dismissed
    err = QTIsStandardParameterDialogEvent( NULL, dialog );
    QTDismissStandardParameterDialog( dialog );

    // codecParameterDialogConfirm means OK was hit, userCanceledErr means Cancel was hit.
    if( codecParameterDialogConfirm == err )
        err = noErr;
    else goto bail;
```

[Next](Clippings-FilterExport.c-Step1.txt.md)[Previous](Clippings-FilterExport.c-SetOutputFile.txt.md)


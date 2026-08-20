---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_file_h.html
archived_at: '2026-07-18T03:27:22.368280Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblerglobals.h.md)[Previous](TumblerSource-Tumblerfile.c.md)

# TumblerSource/Tumbler_file.h

```
// Tumbler_file.h
//
// file related function prototypes for the Tumbler application
//
// Modification History
//
//  11/26/94        nick        initial cut - symantec proto_helper app, add defines


#ifndef _Tumbler_FILE_H_
#define _Tumbler_FILE_H_

// wrappers 
void        DoNewDocument(void);
OSErr       DoOpenFile(FSSpec *theFile);
void        DoOpenDocument(DocumentPtr theDocument);
Boolean     DoSaveAsDocument(DocumentPtr theDocument);
Boolean     DidSaveDocument(DocumentPtr theDocument);
void        DoRevertDocument(DocumentPtr theDocument);
short       ReadDocumentFile(DocumentPtr theDocument, TQ3Boolean isText) ;
PicHandle   OpenPICTFile( FSSpec *theFile ) ;
void        DoImport3DMFDocument(DocumentPtr theDocument) ;

// metafile i/o routines
TQ3Status   Tumbler_ReadScene(  TQ3FileObject   file, 
                                    short           isText, 
                                    TQ3SharedObject *viewHints, 
                                    TQ3Object       *model) ;

void        Tumbler_WriteScene(     TQ3FileObject       file,
                                        short               textMode,
                                        DocumentPtr         theDocument) ;

#endif
```

[Next](TumblerSource-Tumblerglobals.h.md)[Previous](TumblerSource-Tumblerfile.c.md)


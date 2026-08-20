---
title: Setting default open Finder window
apple_id: DTS10003808
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2006-01-03'
source_url: https://developer.apple.com/library/archive/qa/qa1449/_index.html
archived_at: '2026-07-18T02:30:49.045831Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1449

# Setting default open Finder window

## Q:  How do I set the default Finder window to open when a disk is mounted?

A: How do I set the default Finder window to open when a disk is mounted?

The Finder can automatically open specified folders when disks are mounted. This is especially useful when distributing software via CD or disk image.

The third UInt32 of the VolumeHeader's finderInfo field contains the directory ID of a directory whose window should be displayed in the Finder when the volume is mounted, or zero if no directory window should be opened. The Mac OS X Finder does not modify this field.

__Listing 1__  Setting the volume frOpenChain.

```swift
//	Command line tool takes one argument, the path to the directory the Finder will open upon disk mount: //	SetOpenWindow path/to/directory/to/open  #include <CoreServices/CoreServices.h>  int	main( int argc, const char *argv[] ) {     OSStatus		err;     FSRef			dirFSRef;     FSCatalogInfo	fsCatalogInfo;     FSVolumeInfo	fsVolumeInfo;      //	Create an FSRef to the passed in folder we want to automatically open on disk mount     err	= FSPathMakeRef( (const UInt8 *)argv[1], &dirFSRef, NULL );     if ( err != noErr ) goto Bail;     err	= FSGetCatalogInfo( &dirFSRef, kFSCatInfoGettableInfo, &fsCatalogInfo, NULL, NULL, NULL );     if ( err != noErr ) goto Bail;      //	In traditional Mac OS, frOpenChain is a list of windows to open. We zero it out for completeness     ((ExtendedFolderInfo*)&fsCatalogInfo.extFinderInfo)->reserved1	= 0;     err	= FSSetCatalogInfo( &dirFSRef, kFSCatInfoFinderXInfo, &fsCatalogInfo );     if ( err != noErr ) goto Bail;      //	Get the volume finderInfo     err	= FSGetVolumeInfo( fsCatalogInfo.volume, 0, NULL, kFSVolInfoFinderInfo, &fsVolumeInfo, NULL, NULL );     if ( err != noErr ) goto Bail;      //	Set the new folder ID     ((UInt32*)&(fsVolumeInfo.finderInfo))[2] = fsCatalogInfo.nodeID;     err	= FSSetVolumeInfo( fsCatalogInfo.volume, kFSVolInfoFinderInfo, &fsVolumeInfo );     if ( err != noErr ) goto Bail;  Bail:     return( err ); }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-01-03 | New document that how to set the default Finder window to open when a disk is mounted |


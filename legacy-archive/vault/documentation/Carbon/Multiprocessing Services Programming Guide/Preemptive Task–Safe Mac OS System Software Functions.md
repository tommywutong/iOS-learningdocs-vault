---
title: Multiprocessing Services Programming Guide
apple_id: TP40000853
resource_type: Guide
platform: macOS
topic: null
technology: CoreServices
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Multitasking_MultiproServ/appendixa/appendixa.html
archived_at: '2026-07-15T05:23:37.822966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Multiprocessing Services Programming Guide](Introduction%20to%20Multiprocessing%20Services%20Programming%20Guide.md)


[Next](Calculating%20the%20Intertask%20Signaling%20Time.md)[Previous](Using%20Multiprocessing%20Services.md)

# Preemptive Task–Safe Mac OS System Software Functions

This appendix lists Mac OS 9 system software calls that you can call directly from a Multiprocessing Services task without using a remote procedure call. Other system software functions are not preemptive task–safe, so you must call them through a callback as described in [Making Remote Procedure Calls](Using%20Multiprocessing%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomq).

These preemptive task–safe functions cause the calling task to block until the call is completed. However, unlike a remote procedure call, the called function does not have to wait until the calling process receives processor time; it executes asynchronously as if it was an interrupt call.

This appendix contains the following tables of functions::

- Device Manager functions: Table A-1
- File Manager:

  - Table A-2, “Preemptive task–safe HFS Plus parameter block functions”
  - Table A-3, “Preemptive task–safe HFS Plus file system reference functions”
  - Table A-4, “Preemptive task–safe HFS parameter block functions”
  - Table A-5, “Preemptive task–safe high-level HFS functions”
  - Table A-6, “Preemptive task–safe file system specification functions”
- Device Manager and File Manager shared functions: Table A-7
- Miscellaneous functions: Table A-8

  __Table A-1__  Preemptive task–safe Device Manager functions

  | Name | Comments |
  | `PBOpenSync` | Not supported in Carbon, so you should not use this function for File Manager open requests. For file open requests, you should call `PBHOpenDFSync`, `PBHOpenDF`, `PBOpenForkSync`, or `FSOpenFork` instead. May be handled by the File Manager in Mac OS 9. |
  | `PBControlSync` |  |
  | `PBStatusSync` |  |
  | `PBKillIOSync` |  |

  __Table A-2__  Preemptive task–safe HFS Plus parameter block functions

  | Name | Comments |
  | `PBMakeFSRefSync` |  |
  | `PBMakeFSRefUnicodeSync` |  |
  | `PBCompareFSRefsSync` |  |
  | `PBCreateFileUnicodeSync` |  |
  | `PBCreateDirectoryUnicodeSync` |  |
  | `PBDeleteObjectSync` |  |
  | `PBMoveObjectSync` |  |
  | `PBExchangeObjectsSync` |  |
  | `PBRenameUnicodeSync` |  |
  | `PBGetCatalogInfoSync` |  |
  | `PBSetCatalogInfoSync` |  |
  | `PBOpenIteratorSync` |  |
  | `PBCloseIteratorSync` |  |
  | `PBGetCatalogInfoBulkSync` |  |
  | `PBCatalogSearchSync` |  |
  | `PBCreateForkSync` |  |
  | `PBDeleteForkSync` |  |
  | `PBIterateForksSync` |  |
  | `PBOpenForkSync` |  |
  | `PBReadForkSync` |  |
  | `PBWriteForkSync` |  |
  | `PBGetForkPositionSync` |  |
  | `PBSetForkPositionSync` |  |
  | `PBGetForkSizeSync` |  |
  | `PBSetForkSizeSync` |  |
  | `PBAllocateForkSync` |  |
  | `PBFlushForkSync` |  |
  | `PBCloseForkSync` |  |
  | `PBGetForkCBInfoSync` |  |
  | `PBGetVolumeInfoSync` |  |
  | `PBSetVolumeInfoSync` |  |

  __Table A-3__  Preemptive task–safe HFS Plus file system reference functions

  | Name | Comments |
  | `FSpMakeFSRef` |  |
  | `FSMakeFSRefUnicode` |  |
  | `FSCompareFSRefs` |  |
  | `FSCreateFileUnicode` |  |
  | `FSCreateDirectoryUnicode` |  |
  | `FSDeleteObject` |  |
  | `FSMoveObject` |  |
  | `FSExchangeObjects` |  |
  | `FSRenameUnicode` |  |
  | `FSGetCatalogInfo` |  |
  | `FSSetCatalogInfo` |  |
  | `FSOpenIterator` |  |
  | `FSCloseIterator` |  |
  | `FSGetCatalogInfoBulk` |  |
  | `FSCatalogSearch` |  |
  | `FSCreateFork` |  |
  | `FSDeleteFork` |  |
  | `FSIterateForks` |  |
  | `FSOpenFork` |  |
  | `FSReadFork` |  |
  | `FSWriteFork` |  |
  | `FSGetForkPosition` |  |
  | `FSSetForkPosition` |  |
  | `FSGetForkSize` |  |
  | `FSSetForkSize` |  |
  | `FSAllocateFork` |  |
  | `FSFlushFork` |  |
  | `FSCloseFork` |  |
  | `FSGetForkCBInfo` |  |
  | `FSGetVolumeInfo` |  |
  | `FSSetVolumeInfo` |  |
  | `FSGetDataForkName` |  |
  | `FSGetResourceForkName` |  |

  __Table A-4__  Preemptive task–safe HFS parameter block functions

  | Name | Comments |
  | `PBXGetVolInfoSync` |  |
  | `PBFlushVolSync` |  |
  | `PBAllocateSync` |  |
  | `PBGetEOFSync` |  |
  | `PBSetEOFSync` |  |
  | `PBGetFPosSync` |  |
  | `PBSetFPosSync` |  |
  | `PBFlushFileSync` |  |
  | `PBCatSearchSync` |  |
  | `PBHSetVolSync` |  |
  | `PBHGetVolSync` |  |
  | `PBCatMoveSync` |  |
  | `PBDirCreateSync` |  |
  | `PBGetFCBInfoSync` |  |
  | `PBGetCatInfoSync` |  |
  | `PBSetCatInfoSync` |  |
  | `PBAllocContigSync` |  |
  | `PBLockRangeSync` |  |
  | `PBUnlockRangeSync` |  |
  | `PBSetVInfoSync` |  |
  | `PBHGetVInfoSync` |  |
  | `PBHOpenSync` |  |
  | `PBHOpenRFSync` |  |
  | `PBHOpenDFSync` |  |
  | `PBHCreateSync` |  |
  | `PBHDeleteSync` |  |
  | `PBHRenameSync` |  |
  | `PBHRstFLockSync` |  |
  | `PBHSetFLockSync` |  |
  | `PBHGetFInfoSync` |  |
  | `PBHSetFInfoSync` |  |
  | `PBMakeFSSpecSync` |  |
  | `PBHGetVolParmsSync` |  |
  | `PBHGetLogInInfoSync` |  |
  | `PBHGetDirAccessSync` |  |
  | `PBHSetDirAccessSync` |  |
  | `PBHMapIDSync` |  |
  | `PBHMapNameSync` |  |
  | `PBHCopyFileSync` |  |
  | `PBHMoveRenameSync` |  |
  | `PBHOpenDenySync` |  |
  | `PBHOpenRFDenySync` |  |
  | `PBGetXCatInfoSync` |  |
  | `PBExchangeFilesSync` |  |
  | `PBCreateFileIDRefSync` |  |
  | `PBResolveFileIDRefSync` |  |
  | `PBDeleteFileIDRefSync` |  |
  | `PBGetForeignPrivsSync` |  |
  | `PBSetForeignPrivsSync` |  |
  | `PBDTAddIconSync` |  |
  | `PBDTGetIconSync` |  |
  | `PBDTGetIconInfoSync` |  |
  | `PBDTAddAPPLSync` |  |
  | `PBDTRemoveAPPLSync` |  |
  | `PBDTGetAPPLSync` |  |
  | `PBDTSetCommentSync` |  |
  | `PBDTRemoveCommentSync` |  |
  | `PBDTGetCommentSync` |  |
  | `PBDTFlushSync` |  |
  | `PBDTResetSync` |  |
  | `PBDTGetInfoSync` |  |
  | `PBDTDeleteSync` |  |
  | `PBShareSync` |  |
  | `PBUnshareSync` |  |
  | `PBGetUGEntrySync` |  |

  __Table A-5__  Preemptive task–safe high-level HFS functions

  | Name | Comments |
  | `FSClose` |  |
  | `FSRead` |  |
  | `FSWrite` |  |
  | `FlushVol` |  |
  | `Allocate` |  |
  | `GetEOF` |  |
  | `SetEOF` |  |
  | `GetFPos` |  |
  | `SetFPos` |  |
  | `HGetVol` |  |
  | `HSetVol` |  |
  | `HOpen` |  |
  | `HOpenDF` |  |
  | `HOpenRF` |  |
  | `AllocContig` |  |
  | `HCreate` |  |
  | `DirCreate` |  |
  | `HDelete` |  |
  | `HGetFInfo` |  |
  | `HSetFInfo` |  |
  | `HSetFLock` |  |
  | `HRstFLock` |  |
  | `HRename` |  |
  | `CatMove` |  |

  __Table A-6__  Preemptive task–safe file system specification functions

  | Name | Comments |
  | `FSMakeFSSpec` |  |
  | `FSpOpenDF` |  |
  | `FSpOpenRF` |  |
  | `FSpCreate` |  |
  | `FSpDirCreate` |  |
  | `FSpDelete` |  |
  | `FSpGetFInfo` |  |
  | `FSpSetFInfo` |  |
  | `FSpSetFLock` |  |
  | `FSpRstFLock` |  |
  | `FSpRename` |  |
  | `FSpCatMove` |  |
  | `FSpExchangeFiles` |  |

  __Table A-7__  Preemptive task–safe functions shared by the Device Manager and File Manager

  | Name | Comments |
  | `PBCloseSync` |  |
  | `PBReadSync` |  |
  | `PBWriteSync` |  |

  __Table A-8__  Miscellaneous preemptive task–safe functions

  | Name | Comments |
  | `DTInstall` | Deferred Task Manager function |
  | `WakeUpProcess` | Process Manager function |

[Next](Calculating%20the%20Intertask%20Signaling%20Time.md)[Previous](Using%20Multiprocessing%20Services.md)


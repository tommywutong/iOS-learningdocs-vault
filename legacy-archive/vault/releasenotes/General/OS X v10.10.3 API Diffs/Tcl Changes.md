---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Tcl.html
archived_at: '2026-07-18T02:52:43.132427Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Tcl Changes

## Tcl

Added TclPlatStubs.init()Added TclStubHooks.init()Added TclStubs.init()Added Tcl_CallFrame.init()Added Tcl_CallFrame.init(nsPtr: UnsafeMutablePointer<Tcl_Namespace>, dummy1: Int32, dummy2: Int32, dummy3: UnsafeMutablePointer<Void>, dummy4: UnsafeMutablePointer<Void>, dummy5: UnsafeMutablePointer<Void>, dummy6: Int32, dummy7: UnsafeMutablePointer<Void>, dummy8: UnsafeMutablePointer<Void>, dummy9: Int32, dummy10: UnsafeMutablePointer<Void>, dummy11: UnsafeMutablePointer<Void>, dummy12: UnsafeMutablePointer<Void>, dummy13: UnsafeMutablePointer<Void>)Added Tcl_ChannelType.init()Added Tcl_ChannelType.init(typeName: UnsafeMutablePointer<Int8>, version: Tcl_ChannelTypeVersion, closeProc: CFunctionPointer<Tcl_DriverCloseProc>, inputProc: CFunctionPointer<Tcl_DriverInputProc>, outputProc: CFunctionPointer<Tcl_DriverOutputProc>, seekProc: CFunctionPointer<Tcl_DriverSeekProc>, setOptionProc: CFunctionPointer<Tcl_DriverSetOptionProc>, getOptionProc: CFunctionPointer<Tcl_DriverGetOptionProc>, watchProc: CFunctionPointer<Tcl_DriverWatchProc>, getHandleProc: CFunctionPointer<Tcl_DriverGetHandleProc>, close2Proc: CFunctionPointer<Tcl_DriverClose2Proc>, blockModeProc: CFunctionPointer<Tcl_DriverBlockModeProc>, flushProc: CFunctionPointer<Tcl_DriverFlushProc>, handlerProc: CFunctionPointer<Tcl_DriverHandlerProc>, wideSeekProc: CFunctionPointer<Tcl_DriverWideSeekProc>, threadActionProc: CFunctionPointer<Tcl_DriverThreadActionProc>, truncateProc: CFunctionPointer<Tcl_DriverTruncateProc>)Added Tcl_CmdInfo.init()Added Tcl_CmdInfo.init(isNativeObjectProc: Int32, objProc: CFunctionPointer<Tcl_ObjCmdProc>, objClientData: ClientData, proc: CFunctionPointer<Tcl_CmdProc>, clientData: ClientData, deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>, deleteData: ClientData, namespacePtr: UnsafeMutablePointer<Tcl_Namespace>)Added Tcl_Config.init()Added Tcl_Config.init(key: UnsafePointer<Int8>, value: UnsafePointer<Int8>)Added Tcl_DString.init()Added Tcl_DString.init(string: UnsafeMutablePointer<Int8>, length: Int32, spaceAvl: Int32, staticSpace:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added Tcl_DictSearch.init()Added Tcl_DictSearch.init(next: UnsafeMutablePointer<Void>, epoch: Int32, dictionaryPtr: Tcl_Dict)Added Tcl_EncodingType.init()Added Tcl_EncodingType.init(encodingName: UnsafePointer<Int8>, toUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>, fromUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>, freeProc: CFunctionPointer<Tcl_EncodingFreeProc>, clientData: ClientData, nullSize: Int32)Added Tcl_Event.init()Added Tcl_Event.init(proc: CFunctionPointer<Tcl_EventProc>, nextPtr: UnsafeMutablePointer<Tcl_Event>)Added Tcl_Filesystem.init()Added Tcl_Filesystem.init(typeName: UnsafePointer<Int8>, structureLength: Int32, version: Tcl_FSVersion, pathInFilesystemProc: CFunctionPointer<Tcl_FSPathInFilesystemProc>, dupInternalRepProc: CFunctionPointer<Tcl_FSDupInternalRepProc>, freeInternalRepProc: CFunctionPointer<Tcl_FSFreeInternalRepProc>, internalToNormalizedProc: CFunctionPointer<Tcl_FSInternalToNormalizedProc>, createInternalRepProc: CFunctionPointer<Tcl_FSCreateInternalRepProc>, normalizePathProc: CFunctionPointer<Tcl_FSNormalizePathProc>, filesystemPathTypeProc: CFunctionPointer<Tcl_FSFilesystemPathTypeProc>, filesystemSeparatorProc: CFunctionPointer<Tcl_FSFilesystemSeparatorProc>, statProc: CFunctionPointer<Tcl_FSStatProc>, accessProc: CFunctionPointer<Tcl_FSAccessProc>, openFileChannelProc: CFunctionPointer<Tcl_FSOpenFileChannelProc>, matchInDirectoryProc: CFunctionPointer<Tcl_FSMatchInDirectoryProc>, utimeProc: CFunctionPointer<Tcl_FSUtimeProc>, linkProc: CFunctionPointer<Tcl_FSLinkProc>, listVolumesProc: CFunctionPointer<Tcl_FSListVolumesProc>, fileAttrStringsProc: CFunctionPointer<Tcl_FSFileAttrStringsProc>, fileAttrsGetProc: CFunctionPointer<Tcl_FSFileAttrsGetProc>, fileAttrsSetProc: CFunctionPointer<Tcl_FSFileAttrsSetProc>, createDirectoryProc: CFunctionPointer<Tcl_FSCreateDirectoryProc>, removeDirectoryProc: CFunctionPointer<Tcl_FSRemoveDirectoryProc>, deleteFileProc: CFunctionPointer<Tcl_FSDeleteFileProc>, copyFileProc: CFunctionPointer<Tcl_FSCopyFileProc>, renameFileProc: CFunctionPointer<Tcl_FSRenameFileProc>, copyDirectoryProc: CFunctionPointer<Tcl_FSCopyDirectoryProc>, lstatProc: CFunctionPointer<Tcl_FSLstatProc>, loadFileProc: CFunctionPointer<Tcl_FSLoadFileProc>, getCwdProc: CFunctionPointer<Tcl_FSGetCwdProc>, chdirProc: CFunctionPointer<Tcl_FSChdirProc>)Added Tcl_GlobTypeData.init()Added Tcl_GlobTypeData.init(type: Int32, perm: Int32, macType: UnsafeMutablePointer<Tcl_Obj>, macCreator: UnsafeMutablePointer<Tcl_Obj>)Added Tcl_HashEntry.init()Added Tcl_HashKeyType.init()Added Tcl_HashKeyType.init(version: Int32, flags: Int32, hashKeyProc: CFunctionPointer<Tcl_HashKeyProc>, compareKeysProc: CFunctionPointer<Tcl_CompareHashKeysProc>, allocEntryProc: CFunctionPointer<Tcl_AllocHashEntryProc>, freeEntryProc: CFunctionPointer<Tcl_FreeHashEntryProc>)Added Tcl_HashSearch.init()Added Tcl_HashSearch.init(tablePtr: UnsafeMutablePointer<Tcl_HashTable>, nextIndex: Int32, nextEntryPtr: UnsafeMutablePointer<Tcl_HashEntry>)Added Tcl_HashTable.init()Added Tcl_HashTable.init(buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>, staticBuckets:(UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>), numBuckets: Int32, numEntries: Int32, rebuildSize: Int32, downShift: Int32, mask: Int32, keyType: Int32, findProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)>, createProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)>, typePtr: UnsafeMutablePointer<Tcl_HashKeyType>)Added Tcl_Interp.init()Added Tcl_Interp.init(result: UnsafeMutablePointer<Int8>, freeProc: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)>, errorLine: Int32)Added Tcl_Namespace.init()Added Tcl_Namespace.init(name: UnsafeMutablePointer<Int8>, fullName: UnsafeMutablePointer<Int8>, clientData: ClientData, deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>, parentPtr: UnsafeMutablePointer<Tcl_Namespace>)Added Tcl_NotifierProcs.init()Added Tcl_NotifierProcs.init(setTimerProc: CFunctionPointer<Tcl_SetTimerProc>, waitForEventProc: CFunctionPointer<Tcl_WaitForEventProc>, createFileHandlerProc: CFunctionPointer<Tcl_CreateFileHandlerProc>, deleteFileHandlerProc: CFunctionPointer<Tcl_DeleteFileHandlerProc>, initNotifierProc: CFunctionPointer<Tcl_InitNotifierProc>, finalizeNotifierProc: CFunctionPointer<Tcl_FinalizeNotifierProc>, alertNotifierProc: CFunctionPointer<Tcl_AlertNotifierProc>, serviceModeHookProc: CFunctionPointer<Tcl_ServiceModeHookProc>)Added Tcl_Obj.init()Added Tcl_ObjType.init()Added Tcl_ObjType.init(name: UnsafeMutablePointer<Int8>, freeIntRepProc: CFunctionPointer<Tcl_FreeInternalRepProc>, dupIntRepProc: CFunctionPointer<Tcl_DupInternalRepProc>, updateStringProc: CFunctionPointer<Tcl_UpdateStringProc>, setFromAnyProc: CFunctionPointer<Tcl_SetFromAnyProc>)Added Tcl_Parse.init()Added Tcl_Parse.init(commentStart: UnsafePointer<Int8>, commentSize: Int32, commandStart: UnsafePointer<Int8>, commandSize: Int32, numWords: Int32, tokenPtr: UnsafeMutablePointer<Tcl_Token>, numTokens: Int32, tokensAvailable: Int32, errorType: Int32, string: UnsafePointer<Int8>, end: UnsafePointer<Int8>, interp: UnsafeMutablePointer<Tcl_Interp>, term: UnsafePointer<Int8>, incomplete: Int32, staticTokens:(Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token))Added Tcl_RegExpIndices.init()Added Tcl_RegExpIndices.init(start: Int, end: Int)Added Tcl_RegExpInfo.init()Added Tcl_RegExpInfo.init(nsubs: Int32, matches: UnsafeMutablePointer<Tcl_RegExpIndices>, extendStart: Int, reserved: Int)Added Tcl_SavedResult.init()Added Tcl_SavedResult.init(result: UnsafeMutablePointer<Int8>, freeProc: CFunctionPointer<Tcl_FreeProc>, objResultPtr: UnsafeMutablePointer<Tcl_Obj>, appendResult: UnsafeMutablePointer<Int8>, appendAvl: Int32, appendUsed: Int32, resultSpace:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added Tcl_Time.init()Added Tcl_Time.init(sec: Int, usec: Int)Added Tcl_Token.init()Added Tcl_Token.init(type: Int32, start: UnsafePointer<Int8>, size: Int32, numComponents: Int32)Added Tcl_Value.init()Added Tcl_Value.init(type: Tcl_ValueType, intValue: Int, doubleValue: Double, wideValue: Tcl_WideInt)Added mp_int.init()Added mp_int.init(used: Int32, alloc: Int32, sign: Int32, dp: UnsafeMutablePointer<mp_digit>)Modified TclPlatStubs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TclPlatStubs {     var magic: Int32     var hooks: COpaquePointer } ``` |
| To | ``` struct TclPlatStubs {     var magic: Int32     var hooks: COpaquePointer     init() } ``` |

Modified TclStubHooks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TclStubHooks {     var tclPlatStubs: UnsafePointer<TclPlatStubs>     var tclIntStubs: COpaquePointer     var tclIntPlatStubs: COpaquePointer } ``` |
| To | ``` struct TclStubHooks {     var tclPlatStubs: UnsafeMutablePointer<TclPlatStubs>     var tclIntStubs: COpaquePointer     var tclIntPlatStubs: COpaquePointer     init() } ``` |

Modified TclStubHooks.tclPlatStubs

|  | Declaration |
| --- | --- |
| From | ``` var tclPlatStubs: UnsafePointer<TclPlatStubs> ``` |
| To | ``` var tclPlatStubs: UnsafeMutablePointer<TclPlatStubs> ``` |

Modified TclStubs.hooks

|  | Declaration |
| --- | --- |
| From | ``` var hooks: UnsafePointer<TclStubHooks> ``` |
| To | ``` var hooks: UnsafeMutablePointer<TclStubHooks> ``` |

Modified TclStubs.reserved188

|  | Declaration |
| --- | --- |
| From | ``` var reserved188: UnsafePointer<()> ``` |
| To | ``` var reserved188: UnsafeMutablePointer<Void> ``` |

Modified TclStubs.reserved285

|  | Declaration |
| --- | --- |
| From | ``` var reserved285: UnsafePointer<()> ``` |
| To | ``` var reserved285: UnsafeMutablePointer<Void> ``` |

Modified TclStubs.tclFreeObj

|  | Declaration |
| --- | --- |
| From | ``` var tclFreeObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tclFreeObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_Access

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Access: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Access: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_AddErrorInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AddErrorInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_AddErrorInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_AddObjErrorInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AddObjErrorInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_AddObjErrorInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_Alloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Alloc: CFunctionPointer<((UInt32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_Alloc: CFunctionPointer<((UInt32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_AllocStatBuf

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AllocStatBuf: CFunctionPointer<(() -> UnsafePointer<Tcl_StatBuf>)> ``` |
| To | ``` var tcl_AllocStatBuf: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_StatBuf>)> ``` |

Modified TclStubs.tcl_AllowExceptions

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AllowExceptions: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_AllowExceptions: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |

Modified TclStubs.tcl_AppendAllObjTypes

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendAllObjTypes: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_AppendAllObjTypes: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_AppendElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendElement: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_AppendElement: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_AppendExportList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendExportList: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Namespace>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_AppendExportList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_AppendFormatToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendFormatToObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_AppendFormatToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_AppendLimitedToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendLimitedToObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, Int32, Int32, ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_AppendLimitedToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, Int32, UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_AppendObjToErrorInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendObjToErrorInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_AppendObjToErrorInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_AppendObjToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendObjToObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_AppendObjToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_AppendResultVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendResultVA: CFunctionPointer<((UnsafePointer<Tcl_Interp>, CVaListPointer) -> Void)> ``` |
| To | ``` var tcl_AppendResultVA: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)> ``` |

Modified TclStubs.tcl_AppendStringsToObjVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendStringsToObjVA: CFunctionPointer<((UnsafePointer<Tcl_Obj>, CVaListPointer) -> Void)> ``` |
| To | ``` var tcl_AppendStringsToObjVA: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, CVaListPointer) -> Void)> ``` |

Modified TclStubs.tcl_AppendToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendToObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_AppendToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_AppendUnicodeToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendUnicodeToObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Tcl_UniChar>, Int32) -> Void)> ``` |
| To | ``` var tcl_AppendUnicodeToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_AsyncInvoke

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AsyncInvoke: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_AsyncInvoke: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_AttemptAlloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptAlloc: CFunctionPointer<((UInt32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_AttemptAlloc: CFunctionPointer<((UInt32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_AttemptDbCkalloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptDbCkalloc: CFunctionPointer<((UInt32, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_AttemptDbCkalloc: CFunctionPointer<((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_AttemptDbCkrealloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptDbCkrealloc: CFunctionPointer<((UnsafePointer<Int8>, UInt32, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_AttemptDbCkrealloc: CFunctionPointer<((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_AttemptRealloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptRealloc: CFunctionPointer<((UnsafePointer<Int8>, UInt32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_AttemptRealloc: CFunctionPointer<((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_AttemptSetObjLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptSetObjLength: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32) -> Int32)> ``` |
| To | ``` var tcl_AttemptSetObjLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_BackgroundError

|  | Declaration |
| --- | --- |
| From | ``` var tcl_BackgroundError: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_BackgroundError: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |

Modified TclStubs.tcl_Backslash

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Backslash: CFunctionPointer<((ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> Int8)> ``` |
| To | ``` var tcl_Backslash: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int8)> ``` |

Modified TclStubs.tcl_BadChannelOption

|  | Declaration |
| --- | --- |
| From | ``` var tcl_BadChannelOption: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_BadChannelOption: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_CallWhenDeleted

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CallWhenDeleted: CFunctionPointer<((UnsafePointer<Tcl_Interp>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CallWhenDeleted: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |

Modified TclStubs.tcl_ChannelBlockModeProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelBlockModeProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverBlockModeProc>)> ``` |
| To | ``` var tcl_ChannelBlockModeProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverBlockModeProc>)> ``` |

Modified TclStubs.tcl_ChannelClose2Proc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelClose2Proc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverClose2Proc>)> ``` |
| To | ``` var tcl_ChannelClose2Proc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverClose2Proc>)> ``` |

Modified TclStubs.tcl_ChannelCloseProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelCloseProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverCloseProc>)> ``` |
| To | ``` var tcl_ChannelCloseProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverCloseProc>)> ``` |

Modified TclStubs.tcl_ChannelFlushProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelFlushProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverFlushProc>)> ``` |
| To | ``` var tcl_ChannelFlushProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverFlushProc>)> ``` |

Modified TclStubs.tcl_ChannelGetHandleProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelGetHandleProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetHandleProc>)> ``` |
| To | ``` var tcl_ChannelGetHandleProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetHandleProc>)> ``` |

Modified TclStubs.tcl_ChannelGetOptionProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelGetOptionProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetOptionProc>)> ``` |
| To | ``` var tcl_ChannelGetOptionProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetOptionProc>)> ``` |

Modified TclStubs.tcl_ChannelHandlerProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelHandlerProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverHandlerProc>)> ``` |
| To | ``` var tcl_ChannelHandlerProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverHandlerProc>)> ``` |

Modified TclStubs.tcl_ChannelInputProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelInputProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverInputProc>)> ``` |
| To | ``` var tcl_ChannelInputProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverInputProc>)> ``` |

Modified TclStubs.tcl_ChannelName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelName: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ChannelName: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_ChannelOutputProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelOutputProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverOutputProc>)> ``` |
| To | ``` var tcl_ChannelOutputProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverOutputProc>)> ``` |

Modified TclStubs.tcl_ChannelSeekProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelSeekProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSeekProc>)> ``` |
| To | ``` var tcl_ChannelSeekProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSeekProc>)> ``` |

Modified TclStubs.tcl_ChannelSetOptionProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelSetOptionProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSetOptionProc>)> ``` |
| To | ``` var tcl_ChannelSetOptionProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSetOptionProc>)> ``` |

Modified TclStubs.tcl_ChannelThreadActionProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelThreadActionProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverThreadActionProc>)> ``` |
| To | ``` var tcl_ChannelThreadActionProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverThreadActionProc>)> ``` |

Modified TclStubs.tcl_ChannelTruncateProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelTruncateProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverTruncateProc>)> ``` |
| To | ``` var tcl_ChannelTruncateProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverTruncateProc>)> ``` |

Modified TclStubs.tcl_ChannelVersion

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelVersion: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion)> ``` |
| To | ``` var tcl_ChannelVersion: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion)> ``` |

Modified TclStubs.tcl_ChannelWatchProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelWatchProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWatchProc>)> ``` |
| To | ``` var tcl_ChannelWatchProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWatchProc>)> ``` |

Modified TclStubs.tcl_ChannelWideSeekProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelWideSeekProc: CFunctionPointer<((ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWideSeekProc>)> ``` |
| To | ``` var tcl_ChannelWideSeekProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWideSeekProc>)> ``` |

Modified TclStubs.tcl_Chdir

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Chdir: CFunctionPointer<((ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_Chdir: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_Close

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Close: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_Close: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |

Modified TclStubs.tcl_CommandComplete

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CommandComplete: CFunctionPointer<((ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_CommandComplete: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_CommandTraceInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CommandTraceInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> ClientData)> ``` |
| To | ``` var tcl_CommandTraceInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> ClientData)> ``` |

Modified TclStubs.tcl_Concat

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Concat: CFunctionPointer<((Int32, ConstUnsafePointer<ConstUnsafePointer<Int8>>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_Concat: CFunctionPointer<((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_ConcatObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConcatObj: CFunctionPointer<((Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_ConcatObj: CFunctionPointer<((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_ConditionFinalize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConditionFinalize: CFunctionPointer<((UnsafePointer<Tcl_Condition>) -> Void)> ``` |
| To | ``` var tcl_ConditionFinalize: CFunctionPointer<((UnsafeMutablePointer<Tcl_Condition>) -> Void)> ``` |

Modified TclStubs.tcl_ConditionNotify

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConditionNotify: CFunctionPointer<((UnsafePointer<Tcl_Condition>) -> Void)> ``` |
| To | ``` var tcl_ConditionNotify: CFunctionPointer<((UnsafeMutablePointer<Tcl_Condition>) -> Void)> ``` |

Modified TclStubs.tcl_ConditionWait

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConditionWait: CFunctionPointer<((UnsafePointer<Tcl_Condition>, UnsafePointer<Tcl_Mutex>, UnsafePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_ConditionWait: CFunctionPointer<((UnsafeMutablePointer<Tcl_Condition>, UnsafeMutablePointer<Tcl_Mutex>, UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |

Modified TclStubs.tcl_ConvertCountedElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConvertCountedElement: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_ConvertCountedElement: CFunctionPointer<((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_ConvertElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConvertElement: CFunctionPointer<((ConstUnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_ConvertElement: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_ConvertToType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConvertToType: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_ObjType>) -> Int32)> ``` |
| To | ``` var tcl_ConvertToType: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_ObjType>) -> Int32)> ``` |

Modified TclStubs.tcl_CreateAlias

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateAlias: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, ConstUnsafePointer<ConstUnsafePointer<Int8>>) -> Int32)> ``` |
| To | ``` var tcl_CreateAlias: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafePointer<Int8>>) -> Int32)> ``` |

Modified TclStubs.tcl_CreateAliasObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateAliasObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_CreateAliasObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_CreateChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateChannel: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>, ConstUnsafePointer<Int8>, ClientData, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_CreateChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_ChannelType>, UnsafePointer<Int8>, ClientData, Int32) -> Tcl_Channel)> ``` |

Modified TclStubs.tcl_CreateCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, CFunctionPointer<Tcl_CmdProc>, ClientData, CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command)> ``` |
| To | ``` var tcl_CreateCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_CmdProc>, ClientData, CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command)> ``` |

Modified TclStubs.tcl_CreateEncoding

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateEncoding: CFunctionPointer<((ConstUnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding)> ``` |
| To | ``` var tcl_CreateEncoding: CFunctionPointer<((UnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding)> ``` |

Modified TclStubs.tcl_CreateEnsemble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateEnsemble: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_Namespace>, Int32) -> Tcl_Command)> ``` |
| To | ``` var tcl_CreateEnsemble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)> ``` |

Modified TclStubs.tcl_CreateHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateHashEntry: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> UnsafePointer<Tcl_HashEntry>)> ``` |
| To | ``` var tcl_CreateHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |

Modified TclStubs.tcl_CreateInterp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateInterp: CFunctionPointer<(() -> UnsafePointer<Tcl_Interp>)> ``` |
| To | ``` var tcl_CreateInterp: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Interp>)> ``` |

Modified TclStubs.tcl_CreateMathFunc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateMathFunc: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Tcl_ValueType>, CFunctionPointer<Tcl_MathProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CreateMathFunc: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_ValueType>, CFunctionPointer<Tcl_MathProc>, ClientData) -> Void)> ``` |

Modified TclStubs.tcl_CreateNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateNamespace: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ClientData, CFunctionPointer<Tcl_NamespaceDeleteProc>) -> UnsafePointer<Tcl_Namespace>)> ``` |
| To | ``` var tcl_CreateNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ClientData, CFunctionPointer<Tcl_NamespaceDeleteProc>) -> UnsafeMutablePointer<Tcl_Namespace>)> ``` |

Modified TclStubs.tcl_CreateObjCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateObjCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, CFunctionPointer<Tcl_ObjCmdProc>, ClientData, CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command)> ``` |
| To | ``` var tcl_CreateObjCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_ObjCmdProc>, ClientData, CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command)> ``` |

Modified TclStubs.tcl_CreateObjTrace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateObjTrace: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, Int32, CFunctionPointer<Tcl_CmdObjTraceProc>, ClientData, CFunctionPointer<Tcl_CmdObjTraceDeleteProc>) -> Tcl_Trace)> ``` |
| To | ``` var tcl_CreateObjTrace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32, CFunctionPointer<Tcl_CmdObjTraceProc>, ClientData, CFunctionPointer<Tcl_CmdObjTraceDeleteProc>) -> Tcl_Trace)> ``` |

Modified TclStubs.tcl_CreateSlave

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateSlave: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Interp>)> ``` |
| To | ``` var tcl_CreateSlave: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Interp>)> ``` |

Modified TclStubs.tcl_CreateThread

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateThread: CFunctionPointer<((UnsafePointer<Tcl_ThreadId>, CFunctionPointer<Tcl_ThreadCreateProc>, ClientData, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_CreateThread: CFunctionPointer<((UnsafeMutablePointer<Tcl_ThreadId>, CFunctionPointer<Tcl_ThreadCreateProc>, ClientData, Int32, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_CreateTrace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateTrace: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_CmdTraceProc>, ClientData) -> Tcl_Trace)> ``` |
| To | ``` var tcl_CreateTrace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_CmdTraceProc>, ClientData) -> Tcl_Trace)> ``` |

Modified TclStubs.tcl_DStringAppend

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringAppend: CFunctionPointer<((UnsafePointer<Tcl_DString>, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_DStringAppend: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_DStringAppendElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringAppendElement: CFunctionPointer<((UnsafePointer<Tcl_DString>, ConstUnsafePointer<Int8>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_DStringAppendElement: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_DStringEndSublist

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringEndSublist: CFunctionPointer<((UnsafePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringEndSublist: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |

Modified TclStubs.tcl_DStringFree

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringFree: CFunctionPointer<((UnsafePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringFree: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |

Modified TclStubs.tcl_DStringGetResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringGetResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringGetResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |

Modified TclStubs.tcl_DStringInit

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringInit: CFunctionPointer<((UnsafePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringInit: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |

Modified TclStubs.tcl_DStringResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |

Modified TclStubs.tcl_DStringSetLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringSetLength: CFunctionPointer<((UnsafePointer<Tcl_DString>, Int32) -> Void)> ``` |
| To | ``` var tcl_DStringSetLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_DStringStartSublist

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringStartSublist: CFunctionPointer<((UnsafePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringStartSublist: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |

Modified TclStubs.tcl_DbCkalloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbCkalloc: CFunctionPointer<((UInt32, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_DbCkalloc: CFunctionPointer<((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_DbCkfree

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbCkfree: CFunctionPointer<((UnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_DbCkfree: CFunctionPointer<((UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_DbCkrealloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbCkrealloc: CFunctionPointer<((UnsafePointer<Int8>, UInt32, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_DbCkrealloc: CFunctionPointer<((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_DbDecrRefCount

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbDecrRefCount: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_DbDecrRefCount: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_DbIncrRefCount

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbIncrRefCount: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_DbIncrRefCount: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_DbIsShared

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbIsShared: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_DbIsShared: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_DbNewBignumObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewBignumObj: CFunctionPointer<((UnsafePointer<mp_int>, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewBignumObj: CFunctionPointer<((UnsafeMutablePointer<mp_int>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewBooleanObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewBooleanObj: CFunctionPointer<((Int32, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewBooleanObj: CFunctionPointer<((Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewByteArrayObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewByteArrayObj: CFunctionPointer<((ConstUnsafePointer<UInt8>, Int32, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewByteArrayObj: CFunctionPointer<((UnsafePointer<UInt8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewDictObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewDictObj: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewDictObj: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewDoubleObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewDoubleObj: CFunctionPointer<((Double, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewDoubleObj: CFunctionPointer<((Double, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewListObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewListObj: CFunctionPointer<((Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewListObj: CFunctionPointer<((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewLongObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewLongObj: CFunctionPointer<((Int, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewLongObj: CFunctionPointer<((Int, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewObj: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewObj: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewStringObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewStringObj: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewStringObj: CFunctionPointer<((UnsafePointer<Int8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DbNewWideIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewWideIntObj: CFunctionPointer<((Tcl_WideInt, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewWideIntObj: CFunctionPointer<((Tcl_WideInt, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_DeleteAssocData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteAssocData: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_DeleteAssocData: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_DeleteCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_DeleteCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_DeleteCommandFromToken

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteCommandFromToken: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command) -> Int32)> ``` |
| To | ``` var tcl_DeleteCommandFromToken: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> Int32)> ``` |

Modified TclStubs.tcl_DeleteHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteHashEntry: CFunctionPointer<((UnsafePointer<Tcl_HashEntry>) -> Void)> ``` |
| To | ``` var tcl_DeleteHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)> ``` |

Modified TclStubs.tcl_DeleteHashTable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteHashTable: CFunctionPointer<((UnsafePointer<Tcl_HashTable>) -> Void)> ``` |
| To | ``` var tcl_DeleteHashTable: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>) -> Void)> ``` |

Modified TclStubs.tcl_DeleteInterp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteInterp: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_DeleteInterp: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |

Modified TclStubs.tcl_DeleteNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteNamespace: CFunctionPointer<((UnsafePointer<Tcl_Namespace>) -> Void)> ``` |
| To | ``` var tcl_DeleteNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Namespace>) -> Void)> ``` |

Modified TclStubs.tcl_DeleteTrace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteTrace: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Trace) -> Void)> ``` |
| To | ``` var tcl_DeleteTrace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Trace) -> Void)> ``` |

Modified TclStubs.tcl_DetachChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DetachChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_DetachChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |

Modified TclStubs.tcl_DetachPids

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DetachPids: CFunctionPointer<((Int32, UnsafePointer<Tcl_Pid>) -> Void)> ``` |
| To | ``` var tcl_DetachPids: CFunctionPointer<((Int32, UnsafeMutablePointer<Tcl_Pid>) -> Void)> ``` |

Modified TclStubs.tcl_DictObjDone

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjDone: CFunctionPointer<((UnsafePointer<Tcl_DictSearch>) -> Void)> ``` |
| To | ``` var tcl_DictObjDone: CFunctionPointer<((UnsafeMutablePointer<Tcl_DictSearch>) -> Void)> ``` |

Modified TclStubs.tcl_DictObjFirst

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjFirst: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_DictSearch>, UnsafePointer<UnsafePointer<Tcl_Obj>>, UnsafePointer<UnsafePointer<Tcl_Obj>>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_DictObjFirst: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_DictObjGet

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjGet: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_DictObjGet: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_DictObjNext

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjNext: CFunctionPointer<((UnsafePointer<Tcl_DictSearch>, UnsafePointer<UnsafePointer<Tcl_Obj>>, UnsafePointer<UnsafePointer<Tcl_Obj>>, UnsafePointer<Int32>) -> Void)> ``` |
| To | ``` var tcl_DictObjNext: CFunctionPointer<((UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Void)> ``` |

Modified TclStubs.tcl_DictObjPut

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjPut: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_DictObjPut: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_DictObjPutKeyList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjPutKeyList: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_DictObjPutKeyList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_DictObjRemove

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjRemove: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_DictObjRemove: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_DictObjRemoveKeyList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjRemoveKeyList: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_DictObjRemoveKeyList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_DictObjSize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjSize: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_DictObjSize: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_DiscardResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DiscardResult: CFunctionPointer<((UnsafePointer<Tcl_SavedResult>) -> Void)> ``` |
| To | ``` var tcl_DiscardResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_SavedResult>) -> Void)> ``` |

Modified TclStubs.tcl_DontCallWhenDeleted

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DontCallWhenDeleted: CFunctionPointer<((UnsafePointer<Tcl_Interp>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DontCallWhenDeleted: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |

Modified TclStubs.tcl_DumpActiveMemory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DumpActiveMemory: CFunctionPointer<((ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_DumpActiveMemory: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_DuplicateObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DuplicateObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DuplicateObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_ErrnoId

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ErrnoId: CFunctionPointer<(() -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ErrnoId: CFunctionPointer<(() -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_ErrnoMsg

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ErrnoMsg: CFunctionPointer<((Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ErrnoMsg: CFunctionPointer<((Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_Eval

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Eval: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_Eval: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_EvalEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalEx: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_EvalEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_EvalFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalFile: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_EvalFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_EvalObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_EvalObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_EvalObjEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalObjEx: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32) -> Int32)> ``` |
| To | ``` var tcl_EvalObjEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_EvalObjv

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalObjv: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, Int32) -> Int32)> ``` |
| To | ``` var tcl_EvalObjv: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_EvalTokens

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalTokens: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Token>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_EvalTokens: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_EvalTokensStandard

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalTokensStandard: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Token>, Int32) -> Int32)> ``` |
| To | ``` var tcl_EvalTokensStandard: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_Export

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Export: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Namespace>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Export: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_ExposeCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExposeCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_ExposeCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_ExprBoolean

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprBoolean: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ExprBoolean: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_ExprBooleanObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprBooleanObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ExprBooleanObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_ExprDouble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprDouble: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Double>) -> Int32)> ``` |
| To | ``` var tcl_ExprDouble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)> ``` |

Modified TclStubs.tcl_ExprDoubleObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprDoubleObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Double>) -> Int32)> ``` |
| To | ``` var tcl_ExprDoubleObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)> ``` |

Modified TclStubs.tcl_ExprLong

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprLong: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Int>) -> Int32)> ``` |
| To | ``` var tcl_ExprLong: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int>) -> Int32)> ``` |

Modified TclStubs.tcl_ExprLongObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprLongObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Int>) -> Int32)> ``` |
| To | ``` var tcl_ExprLongObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)> ``` |

Modified TclStubs.tcl_ExprObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_ExprObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_ExprString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprString: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_ExprString: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_ExternalToUtf

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExternalToUtf: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Encoding, ConstUnsafePointer<Int8>, Int32, Int32, UnsafePointer<Tcl_EncodingState>, UnsafePointer<Int8>, Int32, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ExternalToUtf: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_ExternalToUtfDString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExternalToUtfDString: CFunctionPointer<((Tcl_Encoding, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ExternalToUtfDString: CFunctionPointer<((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_FSAccess

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSAccess: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32) -> Int32)> ``` |
| To | ``` var tcl_FSAccess: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_FSChdir

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSChdir: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSChdir: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSConvertToPathType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSConvertToPathType: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSConvertToPathType: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSCopyDirectory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSCopyDirectory: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_FSCopyDirectory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_FSCopyFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSCopyFile: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSCopyFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSCreateDirectory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSCreateDirectory: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSCreateDirectory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSData: CFunctionPointer<((UnsafePointer<Tcl_Filesystem>) -> ClientData)> ``` |
| To | ``` var tcl_FSData: CFunctionPointer<((UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)> ``` |

Modified TclStubs.tcl_FSDeleteFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSDeleteFile: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSDeleteFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSEqualPaths

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSEqualPaths: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSEqualPaths: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSEvalFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSEvalFile: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSEvalFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSEvalFileEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSEvalFileEx: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_FSEvalFileEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_FSFileAttrStrings

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSFileAttrStrings: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<ConstUnsafePointer<Int8>>)> ``` |
| To | ``` var tcl_FSFileAttrStrings: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)> ``` |

Modified TclStubs.tcl_FSFileAttrsGet

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSFileAttrsGet: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, UnsafePointer<Tcl_Obj>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_FSFileAttrsGet: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_FSFileAttrsSet

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSFileAttrsSet: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSFileAttrsSet: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSFileSystemInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSFileSystemInfo: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSFileSystemInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSGetCwd

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetCwd: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSGetCwd: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSGetFileSystemForPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetFileSystemForPath: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Filesystem>)> ``` |
| To | ``` var tcl_FSGetFileSystemForPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Filesystem>)> ``` |

Modified TclStubs.tcl_FSGetInternalRep

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetInternalRep: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Filesystem>) -> ClientData)> ``` |
| To | ``` var tcl_FSGetInternalRep: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)> ``` |

Modified TclStubs.tcl_FSGetNativePath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetNativePath: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_FSGetNativePath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_FSGetNormalizedPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetNormalizedPath: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSGetNormalizedPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSGetPathType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetPathType: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> Tcl_PathType)> ``` |
| To | ``` var tcl_FSGetPathType: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Tcl_PathType)> ``` |

Modified TclStubs.tcl_FSGetTranslatedPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetTranslatedPath: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSGetTranslatedPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSGetTranslatedStringPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetTranslatedStringPath: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_FSGetTranslatedStringPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_FSJoinPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSJoinPath: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSJoinPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSJoinToPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSJoinToPath: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSJoinToPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSLink

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSLink: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSLink: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSListVolumes

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSListVolumes: CFunctionPointer<(() -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSListVolumes: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSLoadFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSLoadFile: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, UnsafePointer<CFunctionPointer<Tcl_PackageInitProc>>, UnsafePointer<CFunctionPointer<Tcl_PackageInitProc>>, UnsafePointer<Tcl_LoadHandle>, UnsafePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32)> ``` |
| To | ``` var tcl_FSLoadFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32)> ``` |

Modified TclStubs.tcl_FSLstat

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSLstat: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_StatBuf>) -> Int32)> ``` |
| To | ``` var tcl_FSLstat: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)> ``` |

Modified TclStubs.tcl_FSMatchInDirectory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSMatchInDirectory: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_GlobTypeData>) -> Int32)> ``` |
| To | ``` var tcl_FSMatchInDirectory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)> ``` |

Modified TclStubs.tcl_FSMountsChanged

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSMountsChanged: CFunctionPointer<((UnsafePointer<Tcl_Filesystem>) -> Void)> ``` |
| To | ``` var tcl_FSMountsChanged: CFunctionPointer<((UnsafeMutablePointer<Tcl_Filesystem>) -> Void)> ``` |

Modified TclStubs.tcl_FSNewNativePath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSNewNativePath: CFunctionPointer<((UnsafePointer<Tcl_Filesystem>, ClientData) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSNewNativePath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Filesystem>, ClientData) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSOpenFileChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSOpenFileChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_FSOpenFileChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)> ``` |

Modified TclStubs.tcl_FSPathSeparator

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSPathSeparator: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSPathSeparator: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSRegister

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSRegister: CFunctionPointer<((ClientData, UnsafePointer<Tcl_Filesystem>) -> Int32)> ``` |
| To | ``` var tcl_FSRegister: CFunctionPointer<((ClientData, UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)> ``` |

Modified TclStubs.tcl_FSRemoveDirectory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSRemoveDirectory: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_FSRemoveDirectory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_FSRenameFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSRenameFile: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSRenameFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_FSSplitPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSSplitPath: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSSplitPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_FSStat

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSStat: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_StatBuf>) -> Int32)> ``` |
| To | ``` var tcl_FSStat: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)> ``` |

Modified TclStubs.tcl_FSUnregister

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSUnregister: CFunctionPointer<((UnsafePointer<Tcl_Filesystem>) -> Int32)> ``` |
| To | ``` var tcl_FSUnregister: CFunctionPointer<((UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)> ``` |

Modified TclStubs.tcl_FSUtime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSUtime: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<utimbuf>) -> Int32)> ``` |
| To | ``` var tcl_FSUtime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)> ``` |

Modified TclStubs.tcl_FindCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_Namespace>, Int32) -> Tcl_Command)> ``` |
| To | ``` var tcl_FindCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)> ``` |

Modified TclStubs.tcl_FindEnsemble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindEnsemble: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32) -> Tcl_Command)> ``` |
| To | ``` var tcl_FindEnsemble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_Command)> ``` |

Modified TclStubs.tcl_FindExecutable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindExecutable: CFunctionPointer<((ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_FindExecutable: CFunctionPointer<((UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_FindHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindHashEntry: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_HashEntry>)> ``` |
| To | ``` var tcl_FindHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |

Modified TclStubs.tcl_FindNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindNamespace: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_Namespace>, Int32) -> UnsafePointer<Tcl_Namespace>)> ``` |
| To | ``` var tcl_FindNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> UnsafeMutablePointer<Tcl_Namespace>)> ``` |

Modified TclStubs.tcl_FirstHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FirstHashEntry: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, UnsafePointer<Tcl_HashSearch>) -> UnsafePointer<Tcl_HashEntry>)> ``` |
| To | ``` var tcl_FirstHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |

Modified TclStubs.tcl_ForgetImport

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ForgetImport: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Namespace>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_ForgetImport: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_Format

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Format: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_Format: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_Free

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Free: CFunctionPointer<((UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_Free: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_FreeParse

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FreeParse: CFunctionPointer<((UnsafePointer<Tcl_Parse>) -> Void)> ``` |
| To | ``` var tcl_FreeParse: CFunctionPointer<((UnsafeMutablePointer<Tcl_Parse>) -> Void)> ``` |

Modified TclStubs.tcl_FreeResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FreeResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_FreeResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |

Modified TclStubs.tcl_GetAlias

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetAlias: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<UnsafePointer<Tcl_Interp>>, UnsafePointer<ConstUnsafePointer<Int8>>, UnsafePointer<Int32>, UnsafePointer<UnsafePointer<ConstUnsafePointer<Int8>>>) -> Int32)> ``` |
| To | ``` var tcl_GetAlias: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)> ``` |

Modified TclStubs.tcl_GetAliasObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetAliasObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<UnsafePointer<Tcl_Interp>>, UnsafePointer<ConstUnsafePointer<Int8>>, UnsafePointer<Int32>, UnsafePointer<UnsafePointer<UnsafePointer<Tcl_Obj>>>) -> Int32)> ``` |
| To | ``` var tcl_GetAliasObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)> ``` |

Modified TclStubs.tcl_GetAllocMutex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetAllocMutex: CFunctionPointer<(() -> UnsafePointer<Tcl_Mutex>)> ``` |
| To | ``` var tcl_GetAllocMutex: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Mutex>)> ``` |

Modified TclStubs.tcl_GetAssocData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetAssocData: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<CFunctionPointer<Tcl_InterpDeleteProc>>) -> ClientData)> ``` |
| To | ``` var tcl_GetAssocData: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<CFunctionPointer<Tcl_InterpDeleteProc>>) -> ClientData)> ``` |

Modified TclStubs.tcl_GetBignumFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetBignumFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<mp_int>) -> Int32)> ``` |
| To | ``` var tcl_GetBignumFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)> ``` |

Modified TclStubs.tcl_GetBoolean

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetBoolean: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetBoolean: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_GetBooleanFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetBooleanFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetBooleanFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_GetByteArrayFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetByteArrayFromObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> UnsafePointer<UInt8>)> ``` |
| To | ``` var tcl_GetByteArrayFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<UInt8>)> ``` |

Modified TclStubs.tcl_GetChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> Tcl_Channel)> ``` |
| To | ``` var tcl_GetChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Tcl_Channel)> ``` |

Modified TclStubs.tcl_GetChannelError

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelError: CFunctionPointer<((Tcl_Channel, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Void)> ``` |
| To | ``` var tcl_GetChannelError: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)> ``` |

Modified TclStubs.tcl_GetChannelErrorInterp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelErrorInterp: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Void)> ``` |
| To | ``` var tcl_GetChannelErrorInterp: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)> ``` |

Modified TclStubs.tcl_GetChannelHandle

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelHandle: CFunctionPointer<((Tcl_Channel, Int32, UnsafePointer<ClientData>) -> Int32)> ``` |
| To | ``` var tcl_GetChannelHandle: CFunctionPointer<((Tcl_Channel, Int32, UnsafeMutablePointer<ClientData>) -> Int32)> ``` |

Modified TclStubs.tcl_GetChannelName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelName: CFunctionPointer<((Tcl_Channel) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetChannelName: CFunctionPointer<((Tcl_Channel) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetChannelNames

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelNames: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_GetChannelNames: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_GetChannelNamesEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelNamesEx: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_GetChannelNamesEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_GetChannelOption

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelOption: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Channel, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_DString>) -> Int32)> ``` |
| To | ``` var tcl_GetChannelOption: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)> ``` |

Modified TclStubs.tcl_GetChannelType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelType: CFunctionPointer<((Tcl_Channel) -> UnsafePointer<Tcl_ChannelType>)> ``` |
| To | ``` var tcl_GetChannelType: CFunctionPointer<((Tcl_Channel) -> UnsafeMutablePointer<Tcl_ChannelType>)> ``` |

Modified TclStubs.tcl_GetCharLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCharLength: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_GetCharLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_GetCommandFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Tcl_Command)> ``` |
| To | ``` var tcl_GetCommandFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Tcl_Command)> ``` |

Modified TclStubs.tcl_GetCommandFullName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandFullName: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_GetCommandFullName: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_GetCommandInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_CmdInfo>) -> Int32)> ``` |
| To | ``` var tcl_GetCommandInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)> ``` |

Modified TclStubs.tcl_GetCommandInfoFromToken

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandInfoFromToken: CFunctionPointer<((Tcl_Command, UnsafePointer<Tcl_CmdInfo>) -> Int32)> ``` |
| To | ``` var tcl_GetCommandInfoFromToken: CFunctionPointer<((Tcl_Command, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)> ``` |

Modified TclStubs.tcl_GetCommandName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandName: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetCommandName: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetCurrentNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCurrentNamespace: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Namespace>)> ``` |
| To | ``` var tcl_GetCurrentNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)> ``` |

Modified TclStubs.tcl_GetCwd

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCwd: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetCwd: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetDefaultEncodingDir

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetDefaultEncodingDir: CFunctionPointer<(() -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetDefaultEncodingDir: CFunctionPointer<(() -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetDouble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetDouble: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Double>) -> Int32)> ``` |
| To | ``` var tcl_GetDouble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)> ``` |

Modified TclStubs.tcl_GetDoubleFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetDoubleFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Double>) -> Int32)> ``` |
| To | ``` var tcl_GetDoubleFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)> ``` |

Modified TclStubs.tcl_GetEncoding

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncoding: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Tcl_Encoding)> ``` |
| To | ``` var tcl_GetEncoding: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_Encoding)> ``` |

Modified TclStubs.tcl_GetEncodingFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Encoding>) -> Int32)> ``` |
| To | ``` var tcl_GetEncodingFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Encoding>) -> Int32)> ``` |

Modified TclStubs.tcl_GetEncodingName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingName: CFunctionPointer<((Tcl_Encoding) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetEncodingName: CFunctionPointer<((Tcl_Encoding) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetEncodingNameFromEnvironment

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingNameFromEnvironment: CFunctionPointer<((UnsafePointer<Tcl_DString>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetEncodingNameFromEnvironment: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetEncodingNames

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingNames: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_GetEncodingNames: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |

Modified TclStubs.tcl_GetEncodingSearchPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingSearchPath: CFunctionPointer<(() -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetEncodingSearchPath: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_GetEnsembleFlags

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleFlags: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleFlags: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_GetEnsembleMappingDict

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleMappingDict: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleMappingDict: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_GetEnsembleNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleNamespace: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<UnsafePointer<Tcl_Namespace>>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Namespace>>) -> Int32)> ``` |

Modified TclStubs.tcl_GetEnsembleSubcommandList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleSubcommandList: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleSubcommandList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_GetEnsembleUnknownHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleUnknownHandler: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleUnknownHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_GetGlobalNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetGlobalNamespace: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Namespace>)> ``` |
| To | ``` var tcl_GetGlobalNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)> ``` |

Modified TclStubs.tcl_GetHostName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetHostName: CFunctionPointer<(() -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetHostName: CFunctionPointer<(() -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetIndexFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetIndexFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<ConstUnsafePointer<Int8>>, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetIndexFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_GetIndexFromObjStruct

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetIndexFromObjStruct: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, ConstUnsafePointer<()>, Int32, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetIndexFromObjStruct: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Void>, Int32, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_GetInt

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetInt: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetInt: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_GetIntFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetIntFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetIntFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_GetInterpPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetInterpPath: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_GetInterpPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_GetLongFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetLongFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Int>) -> Int32)> ``` |
| To | ``` var tcl_GetLongFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)> ``` |

Modified TclStubs.tcl_GetMaster

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetMaster: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Interp>)> ``` |
| To | ``` var tcl_GetMaster: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Interp>)> ``` |

Modified TclStubs.tcl_GetMathFuncInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetMathFuncInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>, UnsafePointer<UnsafePointer<Tcl_ValueType>>, UnsafePointer<CFunctionPointer<Tcl_MathProc>>, UnsafePointer<ClientData>) -> Int32)> ``` |
| To | ``` var tcl_GetMathFuncInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, UnsafeMutablePointer<CFunctionPointer<Tcl_MathProc>>, UnsafeMutablePointer<ClientData>) -> Int32)> ``` |

Modified TclStubs.tcl_GetNameOfExecutable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetNameOfExecutable: CFunctionPointer<(() -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetNameOfExecutable: CFunctionPointer<(() -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetNamespaceUnknownHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetNamespaceUnknownHandler: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Namespace>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetNamespaceUnknownHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_GetObjResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetObjResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetObjResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_GetObjType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetObjType: CFunctionPointer<((ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_ObjType>)> ``` |
| To | ``` var tcl_GetObjType: CFunctionPointer<((UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_ObjType>)> ``` |

Modified TclStubs.tcl_GetOpenFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetOpenFile: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, Int32, UnsafePointer<ClientData>) -> Int32)> ``` |
| To | ``` var tcl_GetOpenFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<ClientData>) -> Int32)> ``` |

Modified TclStubs.tcl_GetPathType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetPathType: CFunctionPointer<((ConstUnsafePointer<Int8>) -> Tcl_PathType)> ``` |
| To | ``` var tcl_GetPathType: CFunctionPointer<((UnsafePointer<Int8>) -> Tcl_PathType)> ``` |

Modified TclStubs.tcl_GetRange

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetRange: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetRange: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_GetRegExpFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetRegExpFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32) -> Tcl_RegExp)> ``` |
| To | ``` var tcl_GetRegExpFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_RegExp)> ``` |

Modified TclStubs.tcl_GetReturnOptions

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetReturnOptions: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetReturnOptions: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_GetSlave

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetSlave: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_Interp>)> ``` |
| To | ``` var tcl_GetSlave: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Interp>)> ``` |

Modified TclStubs.tcl_GetString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetString: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetString: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetStringFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetStringFromObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetStringFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetStringResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetStringResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetStringResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetThreadData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetThreadData: CFunctionPointer<((UnsafePointer<Tcl_ThreadDataKey>, Int32) -> UnsafePointer<()>)> ``` |
| To | ``` var tcl_GetThreadData: CFunctionPointer<((UnsafeMutablePointer<Tcl_ThreadDataKey>, Int32) -> UnsafeMutablePointer<Void>)> ``` |

Modified TclStubs.tcl_GetTime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetTime: CFunctionPointer<((UnsafePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_GetTime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |

Modified TclStubs.tcl_GetUniChar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetUniChar: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32) -> Tcl_UniChar)> ``` |
| To | ``` var tcl_GetUniChar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_UniChar)> ``` |

Modified TclStubs.tcl_GetUnicode

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetUnicode: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_UniChar>)> ``` |
| To | ``` var tcl_GetUnicode: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_UniChar>)> ``` |

Modified TclStubs.tcl_GetUnicodeFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetUnicodeFromObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> UnsafePointer<Tcl_UniChar>)> ``` |
| To | ``` var tcl_GetUnicodeFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_UniChar>)> ``` |

Modified TclStubs.tcl_GetVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetVar2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_GetVar2Ex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetVar2Ex: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetVar2Ex: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_GetVersion

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetVersion: CFunctionPointer<((UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Int32>) -> Void)> ``` |
| To | ``` var tcl_GetVersion: CFunctionPointer<((UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Void)> ``` |

Modified TclStubs.tcl_GetWideIntFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetWideIntFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_WideInt>) -> Int32)> ``` |
| To | ``` var tcl_GetWideIntFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_WideInt>) -> Int32)> ``` |

Modified TclStubs.tcl_Gets

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Gets: CFunctionPointer<((Tcl_Channel, UnsafePointer<Tcl_DString>) -> Int32)> ``` |
| To | ``` var tcl_Gets: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_DString>) -> Int32)> ``` |

Modified TclStubs.tcl_GetsObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetsObj: CFunctionPointer<((Tcl_Channel, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_GetsObj: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_GlobalEval

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GlobalEval: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_GlobalEval: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_GlobalEvalObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GlobalEvalObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_GlobalEvalObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_HashStats

|  | Declaration |
| --- | --- |
| From | ``` var tcl_HashStats: CFunctionPointer<((UnsafePointer<Tcl_HashTable>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_HashStats: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_HideCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_HideCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_HideCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_Import

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Import: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Namespace>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Import: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_Init

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Init: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_Init: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_InitBignumFromDouble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitBignumFromDouble: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Double, UnsafePointer<mp_int>) -> Int32)> ``` |
| To | ``` var tcl_InitBignumFromDouble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<mp_int>) -> Int32)> ``` |

Modified TclStubs.tcl_InitCustomHashTable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitCustomHashTable: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, Int32, UnsafePointer<Tcl_HashKeyType>) -> Void)> ``` |
| To | ``` var tcl_InitCustomHashTable: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, Int32, UnsafeMutablePointer<Tcl_HashKeyType>) -> Void)> ``` |

Modified TclStubs.tcl_InitHashTable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitHashTable: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, Int32) -> Void)> ``` |
| To | ``` var tcl_InitHashTable: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_InitMemory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitMemory: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_InitMemory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |

Modified TclStubs.tcl_InitObjHashTable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitObjHashTable: CFunctionPointer<((UnsafePointer<Tcl_HashTable>) -> Void)> ``` |
| To | ``` var tcl_InitObjHashTable: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>) -> Void)> ``` |

Modified TclStubs.tcl_InterpDeleted

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InterpDeleted: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_InterpDeleted: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_InvalidateStringRep

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InvalidateStringRep: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_InvalidateStringRep: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_IsChannelExisting

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsChannelExisting: CFunctionPointer<((ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_IsChannelExisting: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_IsChannelRegistered

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsChannelRegistered: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_IsChannelRegistered: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |

Modified TclStubs.tcl_IsSafe

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsSafe: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_IsSafe: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_JoinPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_JoinPath: CFunctionPointer<((Int32, ConstUnsafePointer<ConstUnsafePointer<Int8>>, UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_JoinPath: CFunctionPointer<((Int32, UnsafePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_JoinThread

|  | Declaration |
| --- | --- |
| From | ``` var tcl_JoinThread: CFunctionPointer<((Tcl_ThreadId, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_JoinThread: CFunctionPointer<((Tcl_ThreadId, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_LimitAddHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitAddHandler: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_LimitHandlerProc>, ClientData, CFunctionPointer<Tcl_LimitHandlerDeleteProc>) -> Void)> ``` |
| To | ``` var tcl_LimitAddHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_LimitHandlerProc>, ClientData, CFunctionPointer<Tcl_LimitHandlerDeleteProc>) -> Void)> ``` |

Modified TclStubs.tcl_LimitCheck

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitCheck: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_LimitCheck: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_LimitExceeded

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitExceeded: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_LimitExceeded: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_LimitGetCommands

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitGetCommands: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_LimitGetCommands: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_LimitGetGranularity

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitGetGranularity: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_LimitGetGranularity: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_LimitGetTime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitGetTime: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_LimitGetTime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |

Modified TclStubs.tcl_LimitReady

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitReady: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_LimitReady: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_LimitRemoveHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitRemoveHandler: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_LimitHandlerProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_LimitRemoveHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_LimitHandlerProc>, ClientData) -> Void)> ``` |

Modified TclStubs.tcl_LimitSetCommands

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitSetCommands: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Void)> ``` |
| To | ``` var tcl_LimitSetCommands: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_LimitSetGranularity

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitSetGranularity: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, Int32) -> Void)> ``` |
| To | ``` var tcl_LimitSetGranularity: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32) -> Void)> ``` |

Modified TclStubs.tcl_LimitSetTime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitSetTime: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_LimitSetTime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |

Modified TclStubs.tcl_LimitTypeEnabled

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitTypeEnabled: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_LimitTypeEnabled: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_LimitTypeExceeded

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitTypeExceeded: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_LimitTypeExceeded: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_LimitTypeReset

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitTypeReset: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Void)> ``` |
| To | ``` var tcl_LimitTypeReset: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_LimitTypeSet

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitTypeSet: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Void)> ``` |
| To | ``` var tcl_LimitTypeSet: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_LinkVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LinkVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_LinkVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_ListMathFuncs

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListMathFuncs: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_ListMathFuncs: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_ListObjAppendElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjAppendElement: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_ListObjAppendElement: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_ListObjAppendList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjAppendList: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_ListObjAppendList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_ListObjGetElements

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjGetElements: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>, UnsafePointer<UnsafePointer<UnsafePointer<Tcl_Obj>>>) -> Int32)> ``` |
| To | ``` var tcl_ListObjGetElements: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)> ``` |

Modified TclStubs.tcl_ListObjIndex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjIndex: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_ListObjIndex: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_ListObjLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjLength: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ListObjLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_ListObjReplace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjReplace: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32, Int32, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_ListObjReplace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_LogCommandInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LogCommandInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_LogCommandInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_MakeSafe

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MakeSafe: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_MakeSafe: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |

Modified TclStubs.tcl_Merge

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Merge: CFunctionPointer<((Int32, ConstUnsafePointer<ConstUnsafePointer<Int8>>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_Merge: CFunctionPointer<((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_MutexFinalize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MutexFinalize: CFunctionPointer<((UnsafePointer<Tcl_Mutex>) -> Void)> ``` |
| To | ``` var tcl_MutexFinalize: CFunctionPointer<((UnsafeMutablePointer<Tcl_Mutex>) -> Void)> ``` |

Modified TclStubs.tcl_MutexLock

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MutexLock: CFunctionPointer<((UnsafePointer<Tcl_Mutex>) -> Void)> ``` |
| To | ``` var tcl_MutexLock: CFunctionPointer<((UnsafeMutablePointer<Tcl_Mutex>) -> Void)> ``` |

Modified TclStubs.tcl_MutexUnlock

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MutexUnlock: CFunctionPointer<((UnsafePointer<Tcl_Mutex>) -> Void)> ``` |
| To | ``` var tcl_MutexUnlock: CFunctionPointer<((UnsafeMutablePointer<Tcl_Mutex>) -> Void)> ``` |

Modified TclStubs.tcl_NewBignumObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewBignumObj: CFunctionPointer<((UnsafePointer<mp_int>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewBignumObj: CFunctionPointer<((UnsafeMutablePointer<mp_int>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewBooleanObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewBooleanObj: CFunctionPointer<((Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewBooleanObj: CFunctionPointer<((Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewByteArrayObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewByteArrayObj: CFunctionPointer<((ConstUnsafePointer<UInt8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewByteArrayObj: CFunctionPointer<((UnsafePointer<UInt8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewDictObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewDictObj: CFunctionPointer<(() -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewDictObj: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewDoubleObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewDoubleObj: CFunctionPointer<((Double) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewDoubleObj: CFunctionPointer<((Double) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewIntObj: CFunctionPointer<((Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewIntObj: CFunctionPointer<((Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewListObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewListObj: CFunctionPointer<((Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewListObj: CFunctionPointer<((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewLongObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewLongObj: CFunctionPointer<((Int) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewLongObj: CFunctionPointer<((Int) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewObj: CFunctionPointer<(() -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewObj: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewStringObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewStringObj: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewStringObj: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewUnicodeObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewUnicodeObj: CFunctionPointer<((ConstUnsafePointer<Tcl_UniChar>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewUnicodeObj: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NewWideIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewWideIntObj: CFunctionPointer<((Tcl_WideInt) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewWideIntObj: CFunctionPointer<((Tcl_WideInt) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_NextHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NextHashEntry: CFunctionPointer<((UnsafePointer<Tcl_HashSearch>) -> UnsafePointer<Tcl_HashEntry>)> ``` |
| To | ``` var tcl_NextHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |

Modified TclStubs.tcl_NumUtfChars

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NumUtfChars: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_NumUtfChars: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_ObjGetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ObjGetVar2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_ObjGetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_ObjSetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ObjSetVar2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_ObjSetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_OpenCommandChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OpenCommandChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, UnsafePointer<ConstUnsafePointer<Int8>>, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_OpenCommandChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, Int32) -> Tcl_Channel)> ``` |

Modified TclStubs.tcl_OpenFileChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OpenFileChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_OpenFileChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)> ``` |

Modified TclStubs.tcl_OpenTcpClient

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OpenTcpClient: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_OpenTcpClient: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, Int32) -> Tcl_Channel)> ``` |

Modified TclStubs.tcl_OpenTcpServer

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OpenTcpServer: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, ConstUnsafePointer<Int8>, CFunctionPointer<Tcl_TcpAcceptProc>, ClientData) -> Tcl_Channel)> ``` |
| To | ``` var tcl_OpenTcpServer: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, CFunctionPointer<Tcl_TcpAcceptProc>, ClientData) -> Tcl_Channel)> ``` |

Modified TclStubs.tcl_PanicVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PanicVA: CFunctionPointer<((ConstUnsafePointer<Int8>, CVaListPointer) -> Void)> ``` |
| To | ``` var tcl_PanicVA: CFunctionPointer<((UnsafePointer<Int8>, CVaListPointer) -> Void)> ``` |

Modified TclStubs.tcl_ParseBraces

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseBraces: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Tcl_Parse>, Int32, UnsafePointer<ConstUnsafePointer<Int8>>) -> Int32)> ``` |
| To | ``` var tcl_ParseBraces: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)> ``` |

Modified TclStubs.tcl_ParseCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, Int32, UnsafePointer<Tcl_Parse>) -> Int32)> ``` |
| To | ``` var tcl_ParseCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)> ``` |

Modified TclStubs.tcl_ParseExpr

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseExpr: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Tcl_Parse>) -> Int32)> ``` |
| To | ``` var tcl_ParseExpr: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)> ``` |

Modified TclStubs.tcl_ParseQuotedString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseQuotedString: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Tcl_Parse>, Int32, UnsafePointer<ConstUnsafePointer<Int8>>) -> Int32)> ``` |
| To | ``` var tcl_ParseQuotedString: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)> ``` |

Modified TclStubs.tcl_ParseVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<ConstUnsafePointer<Int8>>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ParseVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_ParseVarName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseVarName: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Tcl_Parse>, Int32) -> Int32)> ``` |
| To | ``` var tcl_ParseVarName: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_PkgPresent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgPresent: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PkgPresent: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_PkgPresentEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgPresentEx: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32, UnsafePointer<ClientData>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PkgPresentEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_PkgProvide

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgProvide: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_PkgProvide: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_PkgProvideEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgProvideEx: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, ClientData) -> Int32)> ``` |
| To | ``` var tcl_PkgProvideEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, ClientData) -> Int32)> ``` |

Modified TclStubs.tcl_PkgRequire

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgRequire: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PkgRequire: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_PkgRequireEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgRequireEx: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32, UnsafePointer<ClientData>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PkgRequireEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_PkgRequireProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgRequireProc: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, UnsafePointer<ClientData>) -> Int32)> ``` |
| To | ``` var tcl_PkgRequireProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<ClientData>) -> Int32)> ``` |

Modified TclStubs.tcl_PosixError

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PosixError: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PosixError: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_PrintDouble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PrintDouble: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Double, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_PrintDouble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_ProcObjCmd

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ProcObjCmd: CFunctionPointer<((ClientData, UnsafePointer<Tcl_Interp>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_ProcObjCmd: CFunctionPointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |

Modified TclStubs.tcl_PutEnv

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PutEnv: CFunctionPointer<((ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_PutEnv: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_QueryTimeProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_QueryTimeProc: CFunctionPointer<((UnsafePointer<CFunctionPointer<Tcl_GetTimeProc>>, UnsafePointer<CFunctionPointer<Tcl_ScaleTimeProc>>, UnsafePointer<ClientData>) -> Void)> ``` |
| To | ``` var tcl_QueryTimeProc: CFunctionPointer<((UnsafeMutablePointer<CFunctionPointer<Tcl_GetTimeProc>>, UnsafeMutablePointer<CFunctionPointer<Tcl_ScaleTimeProc>>, UnsafeMutablePointer<ClientData>) -> Void)> ``` |

Modified TclStubs.tcl_QueueEvent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_QueueEvent: CFunctionPointer<((UnsafePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)> ``` |
| To | ``` var tcl_QueueEvent: CFunctionPointer<((UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)> ``` |

Modified TclStubs.tcl_Read

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Read: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Read: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_ReadChars

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ReadChars: CFunctionPointer<((Tcl_Channel, UnsafePointer<Tcl_Obj>, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_ReadChars: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_ReadRaw

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ReadRaw: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_ReadRaw: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_Realloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Realloc: CFunctionPointer<((UnsafePointer<Int8>, UInt32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_Realloc: CFunctionPointer<((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_RecordAndEval

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RecordAndEval: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_RecordAndEval: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_RecordAndEvalObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RecordAndEvalObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32) -> Int32)> ``` |
| To | ``` var tcl_RecordAndEvalObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_RegExpCompile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpCompile: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Tcl_RegExp)> ``` |
| To | ``` var tcl_RegExpCompile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_RegExp)> ``` |

Modified TclStubs.tcl_RegExpExec

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpExec: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_RegExp, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_RegExpExec: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_RegExpExecObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpExecObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_RegExp, UnsafePointer<Tcl_Obj>, Int32, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_RegExpExecObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_RegExpGetInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpGetInfo: CFunctionPointer<((Tcl_RegExp, UnsafePointer<Tcl_RegExpInfo>) -> Void)> ``` |
| To | ``` var tcl_RegExpGetInfo: CFunctionPointer<((Tcl_RegExp, UnsafeMutablePointer<Tcl_RegExpInfo>) -> Void)> ``` |

Modified TclStubs.tcl_RegExpMatch

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpMatch: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_RegExpMatch: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_RegExpMatchObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpMatchObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_RegExpMatchObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_RegExpRange

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpRange: CFunctionPointer<((Tcl_RegExp, Int32, UnsafePointer<ConstUnsafePointer<Int8>>, UnsafePointer<ConstUnsafePointer<Int8>>) -> Void)> ``` |
| To | ``` var tcl_RegExpRange: CFunctionPointer<((Tcl_RegExp, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)> ``` |

Modified TclStubs.tcl_RegisterChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegisterChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Channel) -> Void)> ``` |
| To | ``` var tcl_RegisterChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Void)> ``` |

Modified TclStubs.tcl_RegisterConfig

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegisterConfig: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_Config>, ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_RegisterConfig: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Config>, UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_RegisterObjType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegisterObjType: CFunctionPointer<((UnsafePointer<Tcl_ObjType>) -> Void)> ``` |
| To | ``` var tcl_RegisterObjType: CFunctionPointer<((UnsafeMutablePointer<Tcl_ObjType>) -> Void)> ``` |

Modified TclStubs.tcl_ResetResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ResetResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_ResetResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |

Modified TclStubs.tcl_RestoreInterpState

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RestoreInterpState: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_InterpState) -> Int32)> ``` |
| To | ``` var tcl_RestoreInterpState: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_InterpState) -> Int32)> ``` |

Modified TclStubs.tcl_RestoreResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RestoreResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_SavedResult>) -> Void)> ``` |
| To | ``` var tcl_RestoreResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)> ``` |

Modified TclStubs.tcl_SaveInterpState

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SaveInterpState: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Tcl_InterpState)> ``` |
| To | ``` var tcl_SaveInterpState: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Tcl_InterpState)> ``` |

Modified TclStubs.tcl_SaveResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SaveResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_SavedResult>) -> Void)> ``` |
| To | ``` var tcl_SaveResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)> ``` |

Modified TclStubs.tcl_ScanCountedElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ScanCountedElement: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ScanCountedElement: CFunctionPointer<((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_ScanElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ScanElement: CFunctionPointer<((ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ScanElement: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_SetAssocData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetAssocData: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_SetAssocData: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |

Modified TclStubs.tcl_SetBignumObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetBignumObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, UnsafePointer<mp_int>) -> Void)> ``` |
| To | ``` var tcl_SetBignumObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Void)> ``` |

Modified TclStubs.tcl_SetBooleanObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetBooleanObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetBooleanObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_SetByteArrayLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetByteArrayLength: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32) -> UnsafePointer<UInt8>)> ``` |
| To | ``` var tcl_SetByteArrayLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<UInt8>)> ``` |

Modified TclStubs.tcl_SetByteArrayObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetByteArrayObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<UInt8>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetByteArrayObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<UInt8>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_SetChannelError

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetChannelError: CFunctionPointer<((Tcl_Channel, UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_SetChannelError: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_SetChannelErrorInterp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetChannelErrorInterp: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_SetChannelErrorInterp: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_SetChannelOption

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetChannelOption: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Channel, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_SetChannelOption: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_SetCommandInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetCommandInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Tcl_CmdInfo>) -> Int32)> ``` |
| To | ``` var tcl_SetCommandInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Tcl_CmdInfo>) -> Int32)> ``` |

Modified TclStubs.tcl_SetCommandInfoFromToken

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetCommandInfoFromToken: CFunctionPointer<((Tcl_Command, ConstUnsafePointer<Tcl_CmdInfo>) -> Int32)> ``` |
| To | ``` var tcl_SetCommandInfoFromToken: CFunctionPointer<((Tcl_Command, UnsafePointer<Tcl_CmdInfo>) -> Int32)> ``` |

Modified TclStubs.tcl_SetDefaultEncodingDir

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetDefaultEncodingDir: CFunctionPointer<((ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_SetDefaultEncodingDir: CFunctionPointer<((UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_SetDoubleObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetDoubleObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Double) -> Void)> ``` |
| To | ``` var tcl_SetDoubleObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Double) -> Void)> ``` |

Modified TclStubs.tcl_SetEncodingSearchPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEncodingSearchPath: CFunctionPointer<((UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetEncodingSearchPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_SetEnsembleFlags

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEnsembleFlags: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, Int32) -> Int32)> ``` |
| To | ``` var tcl_SetEnsembleFlags: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_SetEnsembleMappingDict

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEnsembleMappingDict: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetEnsembleMappingDict: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_SetEnsembleSubcommandList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEnsembleSubcommandList: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetEnsembleSubcommandList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_SetEnsembleUnknownHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEnsembleUnknownHandler: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Command, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetEnsembleUnknownHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_SetErrorCodeVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetErrorCodeVA: CFunctionPointer<((UnsafePointer<Tcl_Interp>, CVaListPointer) -> Void)> ``` |
| To | ``` var tcl_SetErrorCodeVA: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)> ``` |

Modified TclStubs.tcl_SetIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetIntObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetIntObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_SetListObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetListObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Void)> ``` |
| To | ``` var tcl_SetListObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)> ``` |

Modified TclStubs.tcl_SetLongObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetLongObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int) -> Void)> ``` |
| To | ``` var tcl_SetLongObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int) -> Void)> ``` |

Modified TclStubs.tcl_SetMaxBlockTime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetMaxBlockTime: CFunctionPointer<((UnsafePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_SetMaxBlockTime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |

Modified TclStubs.tcl_SetNamespaceUnknownHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetNamespaceUnknownHandler: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Namespace>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetNamespaceUnknownHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_SetNotifier

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetNotifier: CFunctionPointer<((UnsafePointer<Tcl_NotifierProcs>) -> Void)> ``` |
| To | ``` var tcl_SetNotifier: CFunctionPointer<((UnsafeMutablePointer<Tcl_NotifierProcs>) -> Void)> ``` |

Modified TclStubs.tcl_SetObjErrorCode

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetObjErrorCode: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_SetObjErrorCode: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_SetObjLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetObjLength: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetObjLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_SetObjResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetObjResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_SetObjResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |

Modified TclStubs.tcl_SetRecursionLimit

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetRecursionLimit: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_SetRecursionLimit: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_SetResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetResult: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_FreeProc>) -> Void)> ``` |
| To | ``` var tcl_SetResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Int8>, CFunctionPointer<Tcl_FreeProc>) -> Void)> ``` |

Modified TclStubs.tcl_SetReturnOptions

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetReturnOptions: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetReturnOptions: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_SetStringObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetStringObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetStringObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_SetSystemEncoding

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetSystemEncoding: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_SetSystemEncoding: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_SetTimer

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetTimer: CFunctionPointer<((UnsafePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_SetTimer: CFunctionPointer<((UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |

Modified TclStubs.tcl_SetUnicodeObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetUnicodeObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Tcl_UniChar>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetUnicodeObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_SetVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_SetVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_SetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetVar2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_SetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_SetVar2Ex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetVar2Ex: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_Obj>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_SetVar2Ex: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_SetWideIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetWideIntObj: CFunctionPointer<((UnsafePointer<Tcl_Obj>, Tcl_WideInt) -> Void)> ``` |
| To | ``` var tcl_SetWideIntObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Tcl_WideInt) -> Void)> ``` |

Modified TclStubs.tcl_SignalId

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SignalId: CFunctionPointer<((Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_SignalId: CFunctionPointer<((Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_SignalMsg

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SignalMsg: CFunctionPointer<((Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_SignalMsg: CFunctionPointer<((Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_SourceRCFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SourceRCFile: CFunctionPointer<((UnsafePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_SourceRCFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |

Modified TclStubs.tcl_SplitList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SplitList: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>, UnsafePointer<UnsafePointer<ConstUnsafePointer<Int8>>>) -> Int32)> ``` |
| To | ``` var tcl_SplitList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)> ``` |

Modified TclStubs.tcl_SplitPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SplitPath: CFunctionPointer<((ConstUnsafePointer<Int8>, UnsafePointer<Int32>, UnsafePointer<UnsafePointer<ConstUnsafePointer<Int8>>>) -> Void)> ``` |
| To | ``` var tcl_SplitPath: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Void)> ``` |

Modified TclStubs.tcl_StackChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_StackChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_ChannelType>, ClientData, Int32, Tcl_Channel) -> Tcl_Channel)> ``` |
| To | ``` var tcl_StackChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_ChannelType>, ClientData, Int32, Tcl_Channel) -> Tcl_Channel)> ``` |

Modified TclStubs.tcl_Stat

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Stat: CFunctionPointer<((ConstUnsafePointer<Int8>, UnsafePointer<stat>) -> Int32)> ``` |
| To | ``` var tcl_Stat: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)> ``` |

Modified TclStubs.tcl_StaticPackage

|  | Declaration |
| --- | --- |
| From | ``` var tcl_StaticPackage: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, CFunctionPointer<Tcl_PackageInitProc>, CFunctionPointer<Tcl_PackageInitProc>) -> Void)> ``` |
| To | ``` var tcl_StaticPackage: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_PackageInitProc>, CFunctionPointer<Tcl_PackageInitProc>) -> Void)> ``` |

Modified TclStubs.tcl_StringCaseMatch

|  | Declaration |
| --- | --- |
| From | ``` var tcl_StringCaseMatch: CFunctionPointer<((ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_StringCaseMatch: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_StringMatch

|  | Declaration |
| --- | --- |
| From | ``` var tcl_StringMatch: CFunctionPointer<((ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_StringMatch: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_SubstObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SubstObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32) -> UnsafePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_SubstObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |

Modified TclStubs.tcl_TakeBignumFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TakeBignumFromObj: CFunctionPointer<((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<mp_int>) -> Int32)> ``` |
| To | ``` var tcl_TakeBignumFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)> ``` |

Modified TclStubs.tcl_ThreadQueueEvent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ThreadQueueEvent: CFunctionPointer<((Tcl_ThreadId, UnsafePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)> ``` |
| To | ``` var tcl_ThreadQueueEvent: CFunctionPointer<((Tcl_ThreadId, UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)> ``` |

Modified TclStubs.tcl_TraceCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TraceCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> Int32)> ``` |
| To | ``` var tcl_TraceCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> Int32)> ``` |

Modified TclStubs.tcl_TraceVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TraceVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Int32)> ``` |
| To | ``` var tcl_TraceVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Int32)> ``` |

Modified TclStubs.tcl_TraceVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TraceVar2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Int32)> ``` |
| To | ``` var tcl_TraceVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Int32)> ``` |

Modified TclStubs.tcl_TranslateFileName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TranslateFileName: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_TranslateFileName: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_Ungets

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Ungets: CFunctionPointer<((Tcl_Channel, ConstUnsafePointer<Int8>, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_Ungets: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_UniCharAtIndex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharAtIndex: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> Tcl_UniChar)> ``` |
| To | ``` var tcl_UniCharAtIndex: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Tcl_UniChar)> ``` |

Modified TclStubs.tcl_UniCharCaseMatch

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharCaseMatch: CFunctionPointer<((ConstUnsafePointer<Tcl_UniChar>, ConstUnsafePointer<Tcl_UniChar>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharCaseMatch: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_UniCharLen

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharLen: CFunctionPointer<((ConstUnsafePointer<Tcl_UniChar>) -> Int32)> ``` |
| To | ``` var tcl_UniCharLen: CFunctionPointer<((UnsafePointer<Tcl_UniChar>) -> Int32)> ``` |

Modified TclStubs.tcl_UniCharNcasecmp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharNcasecmp: CFunctionPointer<((ConstUnsafePointer<Tcl_UniChar>, ConstUnsafePointer<Tcl_UniChar>, UInt) -> Int32)> ``` |
| To | ``` var tcl_UniCharNcasecmp: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)> ``` |

Modified TclStubs.tcl_UniCharNcmp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharNcmp: CFunctionPointer<((ConstUnsafePointer<Tcl_UniChar>, ConstUnsafePointer<Tcl_UniChar>, UInt) -> Int32)> ``` |
| To | ``` var tcl_UniCharNcmp: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)> ``` |

Modified TclStubs.tcl_UniCharToUtf

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharToUtf: CFunctionPointer<((Int32, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UniCharToUtf: CFunctionPointer<((Int32, UnsafeMutablePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_UniCharToUtfDString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharToUtfDString: CFunctionPointer<((ConstUnsafePointer<Tcl_UniChar>, Int32, UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UniCharToUtfDString: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_UnlinkVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnlinkVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_UnlinkVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_UnregisterChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnregisterChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_UnregisterChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |

Modified TclStubs.tcl_UnsetVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnsetVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UnsetVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_UnsetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnsetVar2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UnsetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_UnstackChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnstackChannel: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_UnstackChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |

Modified TclStubs.tcl_UntraceCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UntraceCommand: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_UntraceCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> Void)> ``` |

Modified TclStubs.tcl_UntraceVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UntraceVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_UntraceVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Void)> ``` |

Modified TclStubs.tcl_UntraceVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UntraceVar2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_UntraceVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Void)> ``` |

Modified TclStubs.tcl_UpVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UpVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UpVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_UpVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UpVar2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UpVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_UpdateLinkedVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UpdateLinkedVar: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_UpdateLinkedVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |

Modified TclStubs.tcl_UtfAtIndex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfAtIndex: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfAtIndex: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_UtfBackslash

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfBackslash: CFunctionPointer<((ConstUnsafePointer<Int8>, UnsafePointer<Int32>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UtfBackslash: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_UtfCharComplete

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfCharComplete: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UtfCharComplete: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_UtfFindFirst

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfFindFirst: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfFindFirst: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_UtfFindLast

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfFindLast: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfFindLast: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_UtfNcasecmp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfNcasecmp: CFunctionPointer<((ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, UInt) -> Int32)> ``` |
| To | ``` var tcl_UtfNcasecmp: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)> ``` |

Modified TclStubs.tcl_UtfNcmp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfNcmp: CFunctionPointer<((ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, UInt) -> Int32)> ``` |
| To | ``` var tcl_UtfNcmp: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)> ``` |

Modified TclStubs.tcl_UtfNext

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfNext: CFunctionPointer<((ConstUnsafePointer<Int8>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfNext: CFunctionPointer<((UnsafePointer<Int8>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_UtfPrev

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfPrev: CFunctionPointer<((ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> ConstUnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfPrev: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafePointer<Int8>)> ``` |

Modified TclStubs.tcl_UtfToExternal

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToExternal: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Tcl_Encoding, ConstUnsafePointer<Int8>, Int32, Int32, UnsafePointer<Tcl_EncodingState>, UnsafePointer<Int8>, Int32, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_UtfToExternal: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified TclStubs.tcl_UtfToExternalDString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToExternalDString: CFunctionPointer<((Tcl_Encoding, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfToExternalDString: CFunctionPointer<((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified TclStubs.tcl_UtfToLower

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToLower: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UtfToLower: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_UtfToTitle

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToTitle: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UtfToTitle: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_UtfToUniChar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToUniChar: CFunctionPointer<((ConstUnsafePointer<Int8>, UnsafePointer<Tcl_UniChar>) -> Int32)> ``` |
| To | ``` var tcl_UtfToUniChar: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_UniChar>) -> Int32)> ``` |

Modified TclStubs.tcl_UtfToUniCharDString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToUniCharDString: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32, UnsafePointer<Tcl_DString>) -> UnsafePointer<Tcl_UniChar>)> ``` |
| To | ``` var tcl_UtfToUniCharDString: CFunctionPointer<((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Tcl_UniChar>)> ``` |

Modified TclStubs.tcl_UtfToUpper

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToUpper: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UtfToUpper: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Int32)> ``` |

Modified TclStubs.tcl_ValidateAllMemory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ValidateAllMemory: CFunctionPointer<((ConstUnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_ValidateAllMemory: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Void)> ``` |

Modified TclStubs.tcl_VarEvalVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_VarEvalVA: CFunctionPointer<((UnsafePointer<Tcl_Interp>, CVaListPointer) -> Int32)> ``` |
| To | ``` var tcl_VarEvalVA: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Int32)> ``` |

Modified TclStubs.tcl_VarTraceInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_VarTraceInfo: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> ClientData)> ``` |
| To | ``` var tcl_VarTraceInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> ClientData)> ``` |

Modified TclStubs.tcl_VarTraceInfo2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_VarTraceInfo2: CFunctionPointer<((UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> ClientData)> ``` |
| To | ``` var tcl_VarTraceInfo2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> ClientData)> ``` |

Modified TclStubs.tcl_WaitForEvent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WaitForEvent: CFunctionPointer<((UnsafePointer<Tcl_Time>) -> Int32)> ``` |
| To | ``` var tcl_WaitForEvent: CFunctionPointer<((UnsafeMutablePointer<Tcl_Time>) -> Int32)> ``` |

Modified TclStubs.tcl_WaitPid

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WaitPid: CFunctionPointer<((Tcl_Pid, UnsafePointer<Int32>, Int32) -> Tcl_Pid)> ``` |
| To | ``` var tcl_WaitPid: CFunctionPointer<((Tcl_Pid, UnsafeMutablePointer<Int32>, Int32) -> Tcl_Pid)> ``` |

Modified TclStubs.tcl_Write

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Write: CFunctionPointer<((Tcl_Channel, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Write: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_WriteChars

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WriteChars: CFunctionPointer<((Tcl_Channel, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_WriteChars: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_WriteObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WriteObj: CFunctionPointer<((Tcl_Channel, UnsafePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_WriteObj: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |

Modified TclStubs.tcl_WriteRaw

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WriteRaw: CFunctionPointer<((Tcl_Channel, ConstUnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_WriteRaw: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)> ``` |

Modified TclStubs.tcl_WrongNumArgs

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WrongNumArgs: CFunctionPointer<((UnsafePointer<Tcl_Interp>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, ConstUnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_WrongNumArgs: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>) -> Void)> ``` |

Modified Tcl_CallFrame [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_CallFrame {     var nsPtr: UnsafePointer<Tcl_Namespace>     var dummy1: Int32     var dummy2: Int32     var dummy3: UnsafePointer<()>     var dummy4: UnsafePointer<()>     var dummy5: UnsafePointer<()>     var dummy6: Int32     var dummy7: UnsafePointer<()>     var dummy8: UnsafePointer<()>     var dummy9: Int32     var dummy10: UnsafePointer<()>     var dummy11: UnsafePointer<()>     var dummy12: UnsafePointer<()>     var dummy13: UnsafePointer<()> } ``` |
| To | ``` struct Tcl_CallFrame {     var nsPtr: UnsafeMutablePointer<Tcl_Namespace>     var dummy1: Int32     var dummy2: Int32     var dummy3: UnsafeMutablePointer<Void>     var dummy4: UnsafeMutablePointer<Void>     var dummy5: UnsafeMutablePointer<Void>     var dummy6: Int32     var dummy7: UnsafeMutablePointer<Void>     var dummy8: UnsafeMutablePointer<Void>     var dummy9: Int32     var dummy10: UnsafeMutablePointer<Void>     var dummy11: UnsafeMutablePointer<Void>     var dummy12: UnsafeMutablePointer<Void>     var dummy13: UnsafeMutablePointer<Void>     init()     init(nsPtr nsPtr: UnsafeMutablePointer<Tcl_Namespace>, dummy1 dummy1: Int32, dummy2 dummy2: Int32, dummy3 dummy3: UnsafeMutablePointer<Void>, dummy4 dummy4: UnsafeMutablePointer<Void>, dummy5 dummy5: UnsafeMutablePointer<Void>, dummy6 dummy6: Int32, dummy7 dummy7: UnsafeMutablePointer<Void>, dummy8 dummy8: UnsafeMutablePointer<Void>, dummy9 dummy9: Int32, dummy10 dummy10: UnsafeMutablePointer<Void>, dummy11 dummy11: UnsafeMutablePointer<Void>, dummy12 dummy12: UnsafeMutablePointer<Void>, dummy13 dummy13: UnsafeMutablePointer<Void>) } ``` |

Modified Tcl_CallFrame.dummy10

|  | Declaration |
| --- | --- |
| From | ``` var dummy10: UnsafePointer<()> ``` |
| To | ``` var dummy10: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.dummy11

|  | Declaration |
| --- | --- |
| From | ``` var dummy11: UnsafePointer<()> ``` |
| To | ``` var dummy11: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.dummy12

|  | Declaration |
| --- | --- |
| From | ``` var dummy12: UnsafePointer<()> ``` |
| To | ``` var dummy12: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.dummy13

|  | Declaration |
| --- | --- |
| From | ``` var dummy13: UnsafePointer<()> ``` |
| To | ``` var dummy13: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.dummy3

|  | Declaration |
| --- | --- |
| From | ``` var dummy3: UnsafePointer<()> ``` |
| To | ``` var dummy3: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.dummy4

|  | Declaration |
| --- | --- |
| From | ``` var dummy4: UnsafePointer<()> ``` |
| To | ``` var dummy4: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.dummy5

|  | Declaration |
| --- | --- |
| From | ``` var dummy5: UnsafePointer<()> ``` |
| To | ``` var dummy5: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.dummy7

|  | Declaration |
| --- | --- |
| From | ``` var dummy7: UnsafePointer<()> ``` |
| To | ``` var dummy7: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.dummy8

|  | Declaration |
| --- | --- |
| From | ``` var dummy8: UnsafePointer<()> ``` |
| To | ``` var dummy8: UnsafeMutablePointer<Void> ``` |

Modified Tcl_CallFrame.nsPtr

|  | Declaration |
| --- | --- |
| From | ``` var nsPtr: UnsafePointer<Tcl_Namespace> ``` |
| To | ``` var nsPtr: UnsafeMutablePointer<Tcl_Namespace> ``` |

Modified Tcl_ChannelType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_ChannelType {     var typeName: UnsafePointer<Int8>     var version: Tcl_ChannelTypeVersion     var closeProc: CFunctionPointer<Tcl_DriverCloseProc>     var inputProc: CFunctionPointer<Tcl_DriverInputProc>     var outputProc: CFunctionPointer<Tcl_DriverOutputProc>     var seekProc: CFunctionPointer<Tcl_DriverSeekProc>     var setOptionProc: CFunctionPointer<Tcl_DriverSetOptionProc>     var getOptionProc: CFunctionPointer<Tcl_DriverGetOptionProc>     var watchProc: CFunctionPointer<Tcl_DriverWatchProc>     var getHandleProc: CFunctionPointer<Tcl_DriverGetHandleProc>     var close2Proc: CFunctionPointer<Tcl_DriverClose2Proc>     var blockModeProc: CFunctionPointer<Tcl_DriverBlockModeProc>     var flushProc: CFunctionPointer<Tcl_DriverFlushProc>     var handlerProc: CFunctionPointer<Tcl_DriverHandlerProc>     var wideSeekProc: CFunctionPointer<Tcl_DriverWideSeekProc>     var threadActionProc: CFunctionPointer<Tcl_DriverThreadActionProc>     var truncateProc: CFunctionPointer<Tcl_DriverTruncateProc> } ``` |
| To | ``` struct Tcl_ChannelType {     var typeName: UnsafeMutablePointer<Int8>     var version: Tcl_ChannelTypeVersion     var closeProc: CFunctionPointer<Tcl_DriverCloseProc>     var inputProc: CFunctionPointer<Tcl_DriverInputProc>     var outputProc: CFunctionPointer<Tcl_DriverOutputProc>     var seekProc: CFunctionPointer<Tcl_DriverSeekProc>     var setOptionProc: CFunctionPointer<Tcl_DriverSetOptionProc>     var getOptionProc: CFunctionPointer<Tcl_DriverGetOptionProc>     var watchProc: CFunctionPointer<Tcl_DriverWatchProc>     var getHandleProc: CFunctionPointer<Tcl_DriverGetHandleProc>     var close2Proc: CFunctionPointer<Tcl_DriverClose2Proc>     var blockModeProc: CFunctionPointer<Tcl_DriverBlockModeProc>     var flushProc: CFunctionPointer<Tcl_DriverFlushProc>     var handlerProc: CFunctionPointer<Tcl_DriverHandlerProc>     var wideSeekProc: CFunctionPointer<Tcl_DriverWideSeekProc>     var threadActionProc: CFunctionPointer<Tcl_DriverThreadActionProc>     var truncateProc: CFunctionPointer<Tcl_DriverTruncateProc>     init()     init(typeName typeName: UnsafeMutablePointer<Int8>, version version: Tcl_ChannelTypeVersion, closeProc closeProc: CFunctionPointer<Tcl_DriverCloseProc>, inputProc inputProc: CFunctionPointer<Tcl_DriverInputProc>, outputProc outputProc: CFunctionPointer<Tcl_DriverOutputProc>, seekProc seekProc: CFunctionPointer<Tcl_DriverSeekProc>, setOptionProc setOptionProc: CFunctionPointer<Tcl_DriverSetOptionProc>, getOptionProc getOptionProc: CFunctionPointer<Tcl_DriverGetOptionProc>, watchProc watchProc: CFunctionPointer<Tcl_DriverWatchProc>, getHandleProc getHandleProc: CFunctionPointer<Tcl_DriverGetHandleProc>, close2Proc close2Proc: CFunctionPointer<Tcl_DriverClose2Proc>, blockModeProc blockModeProc: CFunctionPointer<Tcl_DriverBlockModeProc>, flushProc flushProc: CFunctionPointer<Tcl_DriverFlushProc>, handlerProc handlerProc: CFunctionPointer<Tcl_DriverHandlerProc>, wideSeekProc wideSeekProc: CFunctionPointer<Tcl_DriverWideSeekProc>, threadActionProc threadActionProc: CFunctionPointer<Tcl_DriverThreadActionProc>, truncateProc truncateProc: CFunctionPointer<Tcl_DriverTruncateProc>) } ``` |

Modified Tcl_ChannelType.typeName

|  | Declaration |
| --- | --- |
| From | ``` var typeName: UnsafePointer<Int8> ``` |
| To | ``` var typeName: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_CmdInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_CmdInfo {     var isNativeObjectProc: Int32     var objProc: CFunctionPointer<Tcl_ObjCmdProc>     var objClientData: ClientData     var proc: CFunctionPointer<Tcl_CmdProc>     var clientData: ClientData     var deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>     var deleteData: ClientData     var namespacePtr: UnsafePointer<Tcl_Namespace> } ``` |
| To | ``` struct Tcl_CmdInfo {     var isNativeObjectProc: Int32     var objProc: CFunctionPointer<Tcl_ObjCmdProc>     var objClientData: ClientData     var proc: CFunctionPointer<Tcl_CmdProc>     var clientData: ClientData     var deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>     var deleteData: ClientData     var namespacePtr: UnsafeMutablePointer<Tcl_Namespace>     init()     init(isNativeObjectProc isNativeObjectProc: Int32, objProc objProc: CFunctionPointer<Tcl_ObjCmdProc>, objClientData objClientData: ClientData, proc proc: CFunctionPointer<Tcl_CmdProc>, clientData clientData: ClientData, deleteProc deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>, deleteData deleteData: ClientData, namespacePtr namespacePtr: UnsafeMutablePointer<Tcl_Namespace>) } ``` |

Modified Tcl_CmdInfo.namespacePtr

|  | Declaration |
| --- | --- |
| From | ``` var namespacePtr: UnsafePointer<Tcl_Namespace> ``` |
| To | ``` var namespacePtr: UnsafeMutablePointer<Tcl_Namespace> ``` |

Modified Tcl_Config [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Config {     var key: ConstUnsafePointer<Int8>     var value: ConstUnsafePointer<Int8> } ``` |
| To | ``` struct Tcl_Config {     var key: UnsafePointer<Int8>     var value: UnsafePointer<Int8>     init()     init(key key: UnsafePointer<Int8>, value value: UnsafePointer<Int8>) } ``` |

Modified Tcl_Config.key

|  | Declaration |
| --- | --- |
| From | ``` var key: ConstUnsafePointer<Int8> ``` |
| To | ``` var key: UnsafePointer<Int8> ``` |

Modified Tcl_Config.value

|  | Declaration |
| --- | --- |
| From | ``` var value: ConstUnsafePointer<Int8> ``` |
| To | ``` var value: UnsafePointer<Int8> ``` |

Modified Tcl_DString [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_DString {     var string: UnsafePointer<Int8>     var length: Int32     var spaceAvl: Int32     var staticSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct Tcl_DString {     var string: UnsafeMutablePointer<Int8>     var length: Int32     var spaceAvl: Int32     var staticSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(string string: UnsafeMutablePointer<Int8>, length length: Int32, spaceAvl spaceAvl: Int32, staticSpace staticSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified Tcl_DString.string

|  | Declaration |
| --- | --- |
| From | ``` var string: UnsafePointer<Int8> ``` |
| To | ``` var string: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_DictSearch [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_DictSearch {     var next: UnsafePointer<()>     var epoch: Int32     var dictionaryPtr: Tcl_Dict } ``` |
| To | ``` struct Tcl_DictSearch {     var next: UnsafeMutablePointer<Void>     var epoch: Int32     var dictionaryPtr: Tcl_Dict     init()     init(next next: UnsafeMutablePointer<Void>, epoch epoch: Int32, dictionaryPtr dictionaryPtr: Tcl_Dict) } ``` |

Modified Tcl_DictSearch.next

|  | Declaration |
| --- | --- |
| From | ``` var next: UnsafePointer<()> ``` |
| To | ``` var next: UnsafeMutablePointer<Void> ``` |

Modified Tcl_EncodingType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_EncodingType {     var encodingName: ConstUnsafePointer<Int8>     var toUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>     var fromUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>     var freeProc: CFunctionPointer<Tcl_EncodingFreeProc>     var clientData: ClientData     var nullSize: Int32 } ``` |
| To | ``` struct Tcl_EncodingType {     var encodingName: UnsafePointer<Int8>     var toUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>     var fromUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>     var freeProc: CFunctionPointer<Tcl_EncodingFreeProc>     var clientData: ClientData     var nullSize: Int32     init()     init(encodingName encodingName: UnsafePointer<Int8>, toUtfProc toUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>, fromUtfProc fromUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>, freeProc freeProc: CFunctionPointer<Tcl_EncodingFreeProc>, clientData clientData: ClientData, nullSize nullSize: Int32) } ``` |

Modified Tcl_EncodingType.encodingName

|  | Declaration |
| --- | --- |
| From | ``` var encodingName: ConstUnsafePointer<Int8> ``` |
| To | ``` var encodingName: UnsafePointer<Int8> ``` |

Modified Tcl_Event [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Event {     var proc: CFunctionPointer<Tcl_EventProc>     var nextPtr: UnsafePointer<Tcl_Event> } ``` |
| To | ``` struct Tcl_Event {     var proc: CFunctionPointer<Tcl_EventProc>     var nextPtr: UnsafeMutablePointer<Tcl_Event>     init()     init(proc proc: CFunctionPointer<Tcl_EventProc>, nextPtr nextPtr: UnsafeMutablePointer<Tcl_Event>) } ``` |

Modified Tcl_Event.nextPtr

|  | Declaration |
| --- | --- |
| From | ``` var nextPtr: UnsafePointer<Tcl_Event> ``` |
| To | ``` var nextPtr: UnsafeMutablePointer<Tcl_Event> ``` |

Modified Tcl_Filesystem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Filesystem {     var typeName: ConstUnsafePointer<Int8>     var structureLength: Int32     var version: Tcl_FSVersion     var pathInFilesystemProc: CFunctionPointer<Tcl_FSPathInFilesystemProc>     var dupInternalRepProc: CFunctionPointer<Tcl_FSDupInternalRepProc>     var freeInternalRepProc: CFunctionPointer<Tcl_FSFreeInternalRepProc>     var internalToNormalizedProc: CFunctionPointer<Tcl_FSInternalToNormalizedProc>     var createInternalRepProc: CFunctionPointer<Tcl_FSCreateInternalRepProc>     var normalizePathProc: CFunctionPointer<Tcl_FSNormalizePathProc>     var filesystemPathTypeProc: CFunctionPointer<Tcl_FSFilesystemPathTypeProc>     var filesystemSeparatorProc: CFunctionPointer<Tcl_FSFilesystemSeparatorProc>     var statProc: CFunctionPointer<Tcl_FSStatProc>     var accessProc: CFunctionPointer<Tcl_FSAccessProc>     var openFileChannelProc: CFunctionPointer<Tcl_FSOpenFileChannelProc>     var matchInDirectoryProc: CFunctionPointer<Tcl_FSMatchInDirectoryProc>     var utimeProc: CFunctionPointer<Tcl_FSUtimeProc>     var linkProc: CFunctionPointer<Tcl_FSLinkProc>     var listVolumesProc: CFunctionPointer<Tcl_FSListVolumesProc>     var fileAttrStringsProc: CFunctionPointer<Tcl_FSFileAttrStringsProc>     var fileAttrsGetProc: CFunctionPointer<Tcl_FSFileAttrsGetProc>     var fileAttrsSetProc: CFunctionPointer<Tcl_FSFileAttrsSetProc>     var createDirectoryProc: CFunctionPointer<Tcl_FSCreateDirectoryProc>     var removeDirectoryProc: CFunctionPointer<Tcl_FSRemoveDirectoryProc>     var deleteFileProc: CFunctionPointer<Tcl_FSDeleteFileProc>     var copyFileProc: CFunctionPointer<Tcl_FSCopyFileProc>     var renameFileProc: CFunctionPointer<Tcl_FSRenameFileProc>     var copyDirectoryProc: CFunctionPointer<Tcl_FSCopyDirectoryProc>     var lstatProc: CFunctionPointer<Tcl_FSLstatProc>     var loadFileProc: CFunctionPointer<Tcl_FSLoadFileProc>     var getCwdProc: CFunctionPointer<Tcl_FSGetCwdProc>     var chdirProc: CFunctionPointer<Tcl_FSChdirProc> } ``` |
| To | ``` struct Tcl_Filesystem {     var typeName: UnsafePointer<Int8>     var structureLength: Int32     var version: Tcl_FSVersion     var pathInFilesystemProc: CFunctionPointer<Tcl_FSPathInFilesystemProc>     var dupInternalRepProc: CFunctionPointer<Tcl_FSDupInternalRepProc>     var freeInternalRepProc: CFunctionPointer<Tcl_FSFreeInternalRepProc>     var internalToNormalizedProc: CFunctionPointer<Tcl_FSInternalToNormalizedProc>     var createInternalRepProc: CFunctionPointer<Tcl_FSCreateInternalRepProc>     var normalizePathProc: CFunctionPointer<Tcl_FSNormalizePathProc>     var filesystemPathTypeProc: CFunctionPointer<Tcl_FSFilesystemPathTypeProc>     var filesystemSeparatorProc: CFunctionPointer<Tcl_FSFilesystemSeparatorProc>     var statProc: CFunctionPointer<Tcl_FSStatProc>     var accessProc: CFunctionPointer<Tcl_FSAccessProc>     var openFileChannelProc: CFunctionPointer<Tcl_FSOpenFileChannelProc>     var matchInDirectoryProc: CFunctionPointer<Tcl_FSMatchInDirectoryProc>     var utimeProc: CFunctionPointer<Tcl_FSUtimeProc>     var linkProc: CFunctionPointer<Tcl_FSLinkProc>     var listVolumesProc: CFunctionPointer<Tcl_FSListVolumesProc>     var fileAttrStringsProc: CFunctionPointer<Tcl_FSFileAttrStringsProc>     var fileAttrsGetProc: CFunctionPointer<Tcl_FSFileAttrsGetProc>     var fileAttrsSetProc: CFunctionPointer<Tcl_FSFileAttrsSetProc>     var createDirectoryProc: CFunctionPointer<Tcl_FSCreateDirectoryProc>     var removeDirectoryProc: CFunctionPointer<Tcl_FSRemoveDirectoryProc>     var deleteFileProc: CFunctionPointer<Tcl_FSDeleteFileProc>     var copyFileProc: CFunctionPointer<Tcl_FSCopyFileProc>     var renameFileProc: CFunctionPointer<Tcl_FSRenameFileProc>     var copyDirectoryProc: CFunctionPointer<Tcl_FSCopyDirectoryProc>     var lstatProc: CFunctionPointer<Tcl_FSLstatProc>     var loadFileProc: CFunctionPointer<Tcl_FSLoadFileProc>     var getCwdProc: CFunctionPointer<Tcl_FSGetCwdProc>     var chdirProc: CFunctionPointer<Tcl_FSChdirProc>     init()     init(typeName typeName: UnsafePointer<Int8>, structureLength structureLength: Int32, version version: Tcl_FSVersion, pathInFilesystemProc pathInFilesystemProc: CFunctionPointer<Tcl_FSPathInFilesystemProc>, dupInternalRepProc dupInternalRepProc: CFunctionPointer<Tcl_FSDupInternalRepProc>, freeInternalRepProc freeInternalRepProc: CFunctionPointer<Tcl_FSFreeInternalRepProc>, internalToNormalizedProc internalToNormalizedProc: CFunctionPointer<Tcl_FSInternalToNormalizedProc>, createInternalRepProc createInternalRepProc: CFunctionPointer<Tcl_FSCreateInternalRepProc>, normalizePathProc normalizePathProc: CFunctionPointer<Tcl_FSNormalizePathProc>, filesystemPathTypeProc filesystemPathTypeProc: CFunctionPointer<Tcl_FSFilesystemPathTypeProc>, filesystemSeparatorProc filesystemSeparatorProc: CFunctionPointer<Tcl_FSFilesystemSeparatorProc>, statProc statProc: CFunctionPointer<Tcl_FSStatProc>, accessProc accessProc: CFunctionPointer<Tcl_FSAccessProc>, openFileChannelProc openFileChannelProc: CFunctionPointer<Tcl_FSOpenFileChannelProc>, matchInDirectoryProc matchInDirectoryProc: CFunctionPointer<Tcl_FSMatchInDirectoryProc>, utimeProc utimeProc: CFunctionPointer<Tcl_FSUtimeProc>, linkProc linkProc: CFunctionPointer<Tcl_FSLinkProc>, listVolumesProc listVolumesProc: CFunctionPointer<Tcl_FSListVolumesProc>, fileAttrStringsProc fileAttrStringsProc: CFunctionPointer<Tcl_FSFileAttrStringsProc>, fileAttrsGetProc fileAttrsGetProc: CFunctionPointer<Tcl_FSFileAttrsGetProc>, fileAttrsSetProc fileAttrsSetProc: CFunctionPointer<Tcl_FSFileAttrsSetProc>, createDirectoryProc createDirectoryProc: CFunctionPointer<Tcl_FSCreateDirectoryProc>, removeDirectoryProc removeDirectoryProc: CFunctionPointer<Tcl_FSRemoveDirectoryProc>, deleteFileProc deleteFileProc: CFunctionPointer<Tcl_FSDeleteFileProc>, copyFileProc copyFileProc: CFunctionPointer<Tcl_FSCopyFileProc>, renameFileProc renameFileProc: CFunctionPointer<Tcl_FSRenameFileProc>, copyDirectoryProc copyDirectoryProc: CFunctionPointer<Tcl_FSCopyDirectoryProc>, lstatProc lstatProc: CFunctionPointer<Tcl_FSLstatProc>, loadFileProc loadFileProc: CFunctionPointer<Tcl_FSLoadFileProc>, getCwdProc getCwdProc: CFunctionPointer<Tcl_FSGetCwdProc>, chdirProc chdirProc: CFunctionPointer<Tcl_FSChdirProc>) } ``` |

Modified Tcl_Filesystem.typeName

|  | Declaration |
| --- | --- |
| From | ``` var typeName: ConstUnsafePointer<Int8> ``` |
| To | ``` var typeName: UnsafePointer<Int8> ``` |

Modified Tcl_GlobTypeData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_GlobTypeData {     var type: Int32     var perm: Int32     var macType: UnsafePointer<Tcl_Obj>     var macCreator: UnsafePointer<Tcl_Obj> } ``` |
| To | ``` struct Tcl_GlobTypeData {     var type: Int32     var perm: Int32     var macType: UnsafeMutablePointer<Tcl_Obj>     var macCreator: UnsafeMutablePointer<Tcl_Obj>     init()     init(type type: Int32, perm perm: Int32, macType macType: UnsafeMutablePointer<Tcl_Obj>, macCreator macCreator: UnsafeMutablePointer<Tcl_Obj>) } ``` |

Modified Tcl_GlobTypeData.macCreator

|  | Declaration |
| --- | --- |
| From | ``` var macCreator: UnsafePointer<Tcl_Obj> ``` |
| To | ``` var macCreator: UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_GlobTypeData.macType

|  | Declaration |
| --- | --- |
| From | ``` var macType: UnsafePointer<Tcl_Obj> ``` |
| To | ``` var macType: UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_HashEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_HashEntry {     var nextPtr: UnsafePointer<Tcl_HashEntry>     var tablePtr: UnsafePointer<Tcl_HashTable>     var hash: UnsafePointer<()>     var clientData: ClientData } ``` |
| To | ``` struct Tcl_HashEntry {     var nextPtr: UnsafeMutablePointer<Tcl_HashEntry>     var tablePtr: UnsafeMutablePointer<Tcl_HashTable>     var hash: UnsafeMutablePointer<Void>     var clientData: ClientData     init() } ``` |

Modified Tcl_HashEntry.hash

|  | Declaration |
| --- | --- |
| From | ``` var hash: UnsafePointer<()> ``` |
| To | ``` var hash: UnsafeMutablePointer<Void> ``` |

Modified Tcl_HashEntry.nextPtr

|  | Declaration |
| --- | --- |
| From | ``` var nextPtr: UnsafePointer<Tcl_HashEntry> ``` |
| To | ``` var nextPtr: UnsafeMutablePointer<Tcl_HashEntry> ``` |

Modified Tcl_HashEntry.tablePtr

|  | Declaration |
| --- | --- |
| From | ``` var tablePtr: UnsafePointer<Tcl_HashTable> ``` |
| To | ``` var tablePtr: UnsafeMutablePointer<Tcl_HashTable> ``` |

Modified Tcl_HashKeyType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_HashKeyType {     var version: Int32     var flags: Int32     var hashKeyProc: CFunctionPointer<Tcl_HashKeyProc>     var compareKeysProc: CFunctionPointer<Tcl_CompareHashKeysProc>     var allocEntryProc: CFunctionPointer<Tcl_AllocHashEntryProc>     var freeEntryProc: CFunctionPointer<Tcl_FreeHashEntryProc> } ``` |
| To | ``` struct Tcl_HashKeyType {     var version: Int32     var flags: Int32     var hashKeyProc: CFunctionPointer<Tcl_HashKeyProc>     var compareKeysProc: CFunctionPointer<Tcl_CompareHashKeysProc>     var allocEntryProc: CFunctionPointer<Tcl_AllocHashEntryProc>     var freeEntryProc: CFunctionPointer<Tcl_FreeHashEntryProc>     init()     init(version version: Int32, flags flags: Int32, hashKeyProc hashKeyProc: CFunctionPointer<Tcl_HashKeyProc>, compareKeysProc compareKeysProc: CFunctionPointer<Tcl_CompareHashKeysProc>, allocEntryProc allocEntryProc: CFunctionPointer<Tcl_AllocHashEntryProc>, freeEntryProc freeEntryProc: CFunctionPointer<Tcl_FreeHashEntryProc>) } ``` |

Modified Tcl_HashSearch [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_HashSearch {     var tablePtr: UnsafePointer<Tcl_HashTable>     var nextIndex: Int32     var nextEntryPtr: UnsafePointer<Tcl_HashEntry> } ``` |
| To | ``` struct Tcl_HashSearch {     var tablePtr: UnsafeMutablePointer<Tcl_HashTable>     var nextIndex: Int32     var nextEntryPtr: UnsafeMutablePointer<Tcl_HashEntry>     init()     init(tablePtr tablePtr: UnsafeMutablePointer<Tcl_HashTable>, nextIndex nextIndex: Int32, nextEntryPtr nextEntryPtr: UnsafeMutablePointer<Tcl_HashEntry>) } ``` |

Modified Tcl_HashSearch.nextEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` var nextEntryPtr: UnsafePointer<Tcl_HashEntry> ``` |
| To | ``` var nextEntryPtr: UnsafeMutablePointer<Tcl_HashEntry> ``` |

Modified Tcl_HashSearch.tablePtr

|  | Declaration |
| --- | --- |
| From | ``` var tablePtr: UnsafePointer<Tcl_HashTable> ``` |
| To | ``` var tablePtr: UnsafeMutablePointer<Tcl_HashTable> ``` |

Modified Tcl_HashTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_HashTable {     var buckets: UnsafePointer<UnsafePointer<Tcl_HashEntry>>     var staticBuckets: (UnsafePointer<Tcl_HashEntry>, UnsafePointer<Tcl_HashEntry>, UnsafePointer<Tcl_HashEntry>, UnsafePointer<Tcl_HashEntry>)     var numBuckets: Int32     var numEntries: Int32     var rebuildSize: Int32     var downShift: Int32     var mask: Int32     var keyType: Int32     var findProc: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_HashEntry>)>     var createProc: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> UnsafePointer<Tcl_HashEntry>)>     var typePtr: UnsafePointer<Tcl_HashKeyType> } ``` |
| To | ``` struct Tcl_HashTable {     var buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>     var staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>)     var numBuckets: Int32     var numEntries: Int32     var rebuildSize: Int32     var downShift: Int32     var mask: Int32     var keyType: Int32     var findProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)>     var createProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)>     var typePtr: UnsafeMutablePointer<Tcl_HashKeyType>     init()     init(buckets buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>, staticBuckets staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>), numBuckets numBuckets: Int32, numEntries numEntries: Int32, rebuildSize rebuildSize: Int32, downShift downShift: Int32, mask mask: Int32, keyType keyType: Int32, findProc findProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)>, createProc createProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)>, typePtr typePtr: UnsafeMutablePointer<Tcl_HashKeyType>) } ``` |

Modified Tcl_HashTable.buckets

|  | Declaration |
| --- | --- |
| From | ``` var buckets: UnsafePointer<UnsafePointer<Tcl_HashEntry>> ``` |
| To | ``` var buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>> ``` |

Modified Tcl_HashTable.createProc

|  | Declaration |
| --- | --- |
| From | ``` var createProc: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, ConstUnsafePointer<Int8>, UnsafePointer<Int32>) -> UnsafePointer<Tcl_HashEntry>)> ``` |
| To | ``` var createProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |

Modified Tcl_HashTable.findProc

|  | Declaration |
| --- | --- |
| From | ``` var findProc: CFunctionPointer<((UnsafePointer<Tcl_HashTable>, ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_HashEntry>)> ``` |
| To | ``` var findProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |

Modified Tcl_HashTable.staticBuckets

|  | Declaration |
| --- | --- |
| From | ``` var staticBuckets: (UnsafePointer<Tcl_HashEntry>, UnsafePointer<Tcl_HashEntry>, UnsafePointer<Tcl_HashEntry>, UnsafePointer<Tcl_HashEntry>) ``` |
| To | ``` var staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>) ``` |

Modified Tcl_HashTable.typePtr

|  | Declaration |
| --- | --- |
| From | ``` var typePtr: UnsafePointer<Tcl_HashKeyType> ``` |
| To | ``` var typePtr: UnsafeMutablePointer<Tcl_HashKeyType> ``` |

Modified Tcl_Interp [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Interp {     var result: UnsafePointer<Int8>     var freeProc: CFunctionPointer<((UnsafePointer<Int8>) -> Void)>     var errorLine: Int32 } ``` |
| To | ``` struct Tcl_Interp {     var result: UnsafeMutablePointer<Int8>     var freeProc: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)>     var errorLine: Int32     init()     init(result result: UnsafeMutablePointer<Int8>, freeProc freeProc: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)>, errorLine errorLine: Int32) } ``` |

Modified Tcl_Interp.freeProc

|  | Declaration |
| --- | --- |
| From | ``` var freeProc: CFunctionPointer<((UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var freeProc: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)> ``` |

Modified Tcl_Interp.result

|  | Declaration |
| --- | --- |
| From | ``` var result: UnsafePointer<Int8> ``` |
| To | ``` var result: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_Namespace [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Namespace {     var name: UnsafePointer<Int8>     var fullName: UnsafePointer<Int8>     var clientData: ClientData     var deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>     var parentPtr: UnsafePointer<Tcl_Namespace> } ``` |
| To | ``` struct Tcl_Namespace {     var name: UnsafeMutablePointer<Int8>     var fullName: UnsafeMutablePointer<Int8>     var clientData: ClientData     var deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>     var parentPtr: UnsafeMutablePointer<Tcl_Namespace>     init()     init(name name: UnsafeMutablePointer<Int8>, fullName fullName: UnsafeMutablePointer<Int8>, clientData clientData: ClientData, deleteProc deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>, parentPtr parentPtr: UnsafeMutablePointer<Tcl_Namespace>) } ``` |

Modified Tcl_Namespace.fullName

|  | Declaration |
| --- | --- |
| From | ``` var fullName: UnsafePointer<Int8> ``` |
| To | ``` var fullName: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_Namespace.name

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_Namespace.parentPtr

|  | Declaration |
| --- | --- |
| From | ``` var parentPtr: UnsafePointer<Tcl_Namespace> ``` |
| To | ``` var parentPtr: UnsafeMutablePointer<Tcl_Namespace> ``` |

Modified Tcl_NotifierProcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_NotifierProcs {     var setTimerProc: CFunctionPointer<Tcl_SetTimerProc>     var waitForEventProc: CFunctionPointer<Tcl_WaitForEventProc>     var createFileHandlerProc: CFunctionPointer<Tcl_CreateFileHandlerProc>     var deleteFileHandlerProc: CFunctionPointer<Tcl_DeleteFileHandlerProc>     var initNotifierProc: CFunctionPointer<Tcl_InitNotifierProc>     var finalizeNotifierProc: CFunctionPointer<Tcl_FinalizeNotifierProc>     var alertNotifierProc: CFunctionPointer<Tcl_AlertNotifierProc>     var serviceModeHookProc: CFunctionPointer<Tcl_ServiceModeHookProc> } ``` |
| To | ``` struct Tcl_NotifierProcs {     var setTimerProc: CFunctionPointer<Tcl_SetTimerProc>     var waitForEventProc: CFunctionPointer<Tcl_WaitForEventProc>     var createFileHandlerProc: CFunctionPointer<Tcl_CreateFileHandlerProc>     var deleteFileHandlerProc: CFunctionPointer<Tcl_DeleteFileHandlerProc>     var initNotifierProc: CFunctionPointer<Tcl_InitNotifierProc>     var finalizeNotifierProc: CFunctionPointer<Tcl_FinalizeNotifierProc>     var alertNotifierProc: CFunctionPointer<Tcl_AlertNotifierProc>     var serviceModeHookProc: CFunctionPointer<Tcl_ServiceModeHookProc>     init()     init(setTimerProc setTimerProc: CFunctionPointer<Tcl_SetTimerProc>, waitForEventProc waitForEventProc: CFunctionPointer<Tcl_WaitForEventProc>, createFileHandlerProc createFileHandlerProc: CFunctionPointer<Tcl_CreateFileHandlerProc>, deleteFileHandlerProc deleteFileHandlerProc: CFunctionPointer<Tcl_DeleteFileHandlerProc>, initNotifierProc initNotifierProc: CFunctionPointer<Tcl_InitNotifierProc>, finalizeNotifierProc finalizeNotifierProc: CFunctionPointer<Tcl_FinalizeNotifierProc>, alertNotifierProc alertNotifierProc: CFunctionPointer<Tcl_AlertNotifierProc>, serviceModeHookProc serviceModeHookProc: CFunctionPointer<Tcl_ServiceModeHookProc>) } ``` |

Modified Tcl_Obj [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Obj {     var refCount: Int32     var bytes: UnsafePointer<Int8>     var length: Int32     var typePtr: UnsafePointer<Tcl_ObjType> } ``` |
| To | ``` struct Tcl_Obj {     var refCount: Int32     var bytes: UnsafeMutablePointer<Int8>     var length: Int32     var typePtr: UnsafeMutablePointer<Tcl_ObjType>     init() } ``` |

Modified Tcl_Obj.bytes

|  | Declaration |
| --- | --- |
| From | ``` var bytes: UnsafePointer<Int8> ``` |
| To | ``` var bytes: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_Obj.typePtr

|  | Declaration |
| --- | --- |
| From | ``` var typePtr: UnsafePointer<Tcl_ObjType> ``` |
| To | ``` var typePtr: UnsafeMutablePointer<Tcl_ObjType> ``` |

Modified Tcl_ObjType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_ObjType {     var name: UnsafePointer<Int8>     var freeIntRepProc: CFunctionPointer<Tcl_FreeInternalRepProc>     var dupIntRepProc: CFunctionPointer<Tcl_DupInternalRepProc>     var updateStringProc: CFunctionPointer<Tcl_UpdateStringProc>     var setFromAnyProc: CFunctionPointer<Tcl_SetFromAnyProc> } ``` |
| To | ``` struct Tcl_ObjType {     var name: UnsafeMutablePointer<Int8>     var freeIntRepProc: CFunctionPointer<Tcl_FreeInternalRepProc>     var dupIntRepProc: CFunctionPointer<Tcl_DupInternalRepProc>     var updateStringProc: CFunctionPointer<Tcl_UpdateStringProc>     var setFromAnyProc: CFunctionPointer<Tcl_SetFromAnyProc>     init()     init(name name: UnsafeMutablePointer<Int8>, freeIntRepProc freeIntRepProc: CFunctionPointer<Tcl_FreeInternalRepProc>, dupIntRepProc dupIntRepProc: CFunctionPointer<Tcl_DupInternalRepProc>, updateStringProc updateStringProc: CFunctionPointer<Tcl_UpdateStringProc>, setFromAnyProc setFromAnyProc: CFunctionPointer<Tcl_SetFromAnyProc>) } ``` |

Modified Tcl_ObjType.name

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_Parse [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Parse {     var commentStart: ConstUnsafePointer<Int8>     var commentSize: Int32     var commandStart: ConstUnsafePointer<Int8>     var commandSize: Int32     var numWords: Int32     var tokenPtr: UnsafePointer<Tcl_Token>     var numTokens: Int32     var tokensAvailable: Int32     var errorType: Int32     var string: ConstUnsafePointer<Int8>     var end: ConstUnsafePointer<Int8>     var interp: UnsafePointer<Tcl_Interp>     var term: ConstUnsafePointer<Int8>     var incomplete: Int32     var staticTokens: (Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token) } ``` |
| To | ``` struct Tcl_Parse {     var commentStart: UnsafePointer<Int8>     var commentSize: Int32     var commandStart: UnsafePointer<Int8>     var commandSize: Int32     var numWords: Int32     var tokenPtr: UnsafeMutablePointer<Tcl_Token>     var numTokens: Int32     var tokensAvailable: Int32     var errorType: Int32     var string: UnsafePointer<Int8>     var end: UnsafePointer<Int8>     var interp: UnsafeMutablePointer<Tcl_Interp>     var term: UnsafePointer<Int8>     var incomplete: Int32     var staticTokens: (Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token)     init()     init(commentStart commentStart: UnsafePointer<Int8>, commentSize commentSize: Int32, commandStart commandStart: UnsafePointer<Int8>, commandSize commandSize: Int32, numWords numWords: Int32, tokenPtr tokenPtr: UnsafeMutablePointer<Tcl_Token>, numTokens numTokens: Int32, tokensAvailable tokensAvailable: Int32, errorType errorType: Int32, string string: UnsafePointer<Int8>, end end: UnsafePointer<Int8>, interp interp: UnsafeMutablePointer<Tcl_Interp>, term term: UnsafePointer<Int8>, incomplete incomplete: Int32, staticTokens staticTokens: (Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token, Tcl_Token)) } ``` |

Modified Tcl_Parse.commandStart

|  | Declaration |
| --- | --- |
| From | ``` var commandStart: ConstUnsafePointer<Int8> ``` |
| To | ``` var commandStart: UnsafePointer<Int8> ``` |

Modified Tcl_Parse.commentStart

|  | Declaration |
| --- | --- |
| From | ``` var commentStart: ConstUnsafePointer<Int8> ``` |
| To | ``` var commentStart: UnsafePointer<Int8> ``` |

Modified Tcl_Parse.end

|  | Declaration |
| --- | --- |
| From | ``` var end: ConstUnsafePointer<Int8> ``` |
| To | ``` var end: UnsafePointer<Int8> ``` |

Modified Tcl_Parse.interp

|  | Declaration |
| --- | --- |
| From | ``` var interp: UnsafePointer<Tcl_Interp> ``` |
| To | ``` var interp: UnsafeMutablePointer<Tcl_Interp> ``` |

Modified Tcl_Parse.string

|  | Declaration |
| --- | --- |
| From | ``` var string: ConstUnsafePointer<Int8> ``` |
| To | ``` var string: UnsafePointer<Int8> ``` |

Modified Tcl_Parse.term

|  | Declaration |
| --- | --- |
| From | ``` var term: ConstUnsafePointer<Int8> ``` |
| To | ``` var term: UnsafePointer<Int8> ``` |

Modified Tcl_Parse.tokenPtr

|  | Declaration |
| --- | --- |
| From | ``` var tokenPtr: UnsafePointer<Tcl_Token> ``` |
| To | ``` var tokenPtr: UnsafeMutablePointer<Tcl_Token> ``` |

Modified Tcl_RegExpIndices [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_RegExpIndices {     var start: Int     var end: Int } ``` |
| To | ``` struct Tcl_RegExpIndices {     var start: Int     var end: Int     init()     init(start start: Int, end end: Int) } ``` |

Modified Tcl_RegExpInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_RegExpInfo {     var nsubs: Int32     var matches: UnsafePointer<Tcl_RegExpIndices>     var extendStart: Int     var reserved: Int } ``` |
| To | ``` struct Tcl_RegExpInfo {     var nsubs: Int32     var matches: UnsafeMutablePointer<Tcl_RegExpIndices>     var extendStart: Int     var reserved: Int     init()     init(nsubs nsubs: Int32, matches matches: UnsafeMutablePointer<Tcl_RegExpIndices>, extendStart extendStart: Int, reserved reserved: Int) } ``` |

Modified Tcl_RegExpInfo.matches

|  | Declaration |
| --- | --- |
| From | ``` var matches: UnsafePointer<Tcl_RegExpIndices> ``` |
| To | ``` var matches: UnsafeMutablePointer<Tcl_RegExpIndices> ``` |

Modified Tcl_SavedResult [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_SavedResult {     var result: UnsafePointer<Int8>     var freeProc: CFunctionPointer<Tcl_FreeProc>     var objResultPtr: UnsafePointer<Tcl_Obj>     var appendResult: UnsafePointer<Int8>     var appendAvl: Int32     var appendUsed: Int32     var resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct Tcl_SavedResult {     var result: UnsafeMutablePointer<Int8>     var freeProc: CFunctionPointer<Tcl_FreeProc>     var objResultPtr: UnsafeMutablePointer<Tcl_Obj>     var appendResult: UnsafeMutablePointer<Int8>     var appendAvl: Int32     var appendUsed: Int32     var resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(result result: UnsafeMutablePointer<Int8>, freeProc freeProc: CFunctionPointer<Tcl_FreeProc>, objResultPtr objResultPtr: UnsafeMutablePointer<Tcl_Obj>, appendResult appendResult: UnsafeMutablePointer<Int8>, appendAvl appendAvl: Int32, appendUsed appendUsed: Int32, resultSpace resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified Tcl_SavedResult.appendResult

|  | Declaration |
| --- | --- |
| From | ``` var appendResult: UnsafePointer<Int8> ``` |
| To | ``` var appendResult: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_SavedResult.objResultPtr

|  | Declaration |
| --- | --- |
| From | ``` var objResultPtr: UnsafePointer<Tcl_Obj> ``` |
| To | ``` var objResultPtr: UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_SavedResult.result

|  | Declaration |
| --- | --- |
| From | ``` var result: UnsafePointer<Int8> ``` |
| To | ``` var result: UnsafeMutablePointer<Int8> ``` |

Modified Tcl_Time [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Time {     var sec: Int     var usec: Int } ``` |
| To | ``` struct Tcl_Time {     var sec: Int     var usec: Int     init()     init(sec sec: Int, usec usec: Int) } ``` |

Modified Tcl_Token [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Token {     var type: Int32     var start: ConstUnsafePointer<Int8>     var size: Int32     var numComponents: Int32 } ``` |
| To | ``` struct Tcl_Token {     var type: Int32     var start: UnsafePointer<Int8>     var size: Int32     var numComponents: Int32     init()     init(type type: Int32, start start: UnsafePointer<Int8>, size size: Int32, numComponents numComponents: Int32) } ``` |

Modified Tcl_Token.start

|  | Declaration |
| --- | --- |
| From | ``` var start: ConstUnsafePointer<Int8> ``` |
| To | ``` var start: UnsafePointer<Int8> ``` |

Modified Tcl_Value [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Value {     var type: Tcl_ValueType     var intValue: Int     var doubleValue: Double     var wideValue: Tcl_WideInt } ``` |
| To | ``` struct Tcl_Value {     var type: Tcl_ValueType     var intValue: Int     var doubleValue: Double     var wideValue: Tcl_WideInt     init()     init(type type: Tcl_ValueType, intValue intValue: Int, doubleValue doubleValue: Double, wideValue wideValue: Tcl_WideInt) } ``` |

Modified mp_int [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mp_int {     var used: Int32     var alloc: Int32     var sign: Int32     var dp: UnsafePointer<mp_digit> } ``` |
| To | ``` struct mp_int {     var used: Int32     var alloc: Int32     var sign: Int32     var dp: UnsafeMutablePointer<mp_digit>     init()     init(used used: Int32, alloc alloc: Int32, sign sign: Int32, dp dp: UnsafeMutablePointer<mp_digit>) } ``` |

Modified mp_int.dp

|  | Declaration |
| --- | --- |
| From | ``` var dp: UnsafePointer<mp_digit> ``` |
| To | ``` var dp: UnsafeMutablePointer<mp_digit> ``` |

Modified ClientData

|  | Declaration |
| --- | --- |
| From | ``` typealias ClientData = UnsafePointer<()> ``` |
| To | ``` typealias ClientData = UnsafeMutablePointer<Void> ``` |

Modified TclFreeObj(UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func TclFreeObj(_ objPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func TclFreeObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified TclTomMathInitializeStubs(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func TclTomMathInitializeStubs(_ interp: UnsafePointer<Tcl_Interp>, _ version: ConstUnsafePointer<Int8>, _ epoch: Int32, _ revision: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func TclTomMathInitializeStubs(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ version: UnsafePointer<Int8>, _ epoch: Int32, _ revision: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_Access(UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Access(_ path: ConstUnsafePointer<Int8>, _ mode: Int32) -> Int32 ``` |
| To | ``` func Tcl_Access(_ path: UnsafePointer<Int8>, _ mode: Int32) -> Int32 ``` |

Modified Tcl_AddErrorInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AddErrorInfo(_ interp: UnsafePointer<Tcl_Interp>, _ message: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_AddErrorInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ message: UnsafePointer<Int8>) ``` |

Modified Tcl_AddObjErrorInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AddObjErrorInfo(_ interp: UnsafePointer<Tcl_Interp>, _ message: ConstUnsafePointer<Int8>, _ length: Int32) ``` |
| To | ``` func Tcl_AddObjErrorInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ message: UnsafePointer<Int8>, _ length: Int32) ``` |

Modified Tcl_Alloc(UInt32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Alloc(_ size: UInt32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_Alloc(_ size: UInt32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_AllocHashEntryProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_AllocHashEntryProc = ((UnsafePointer<Tcl_HashTable>, UnsafePointer<()>) -> UnsafePointer<Tcl_HashEntry>) ``` |
| To | ``` typealias Tcl_AllocHashEntryProc = ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Tcl_HashEntry>) ``` |

Modified Tcl_AllocStatBuf() -> UnsafeMutablePointer<Tcl_StatBuf>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AllocStatBuf() -> UnsafePointer<Tcl_StatBuf> ``` |
| To | ``` func Tcl_AllocStatBuf() -> UnsafeMutablePointer<Tcl_StatBuf> ``` |

Modified Tcl_AllowExceptions(UnsafeMutablePointer<Tcl_Interp>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AllowExceptions(_ interp: UnsafePointer<Tcl_Interp>) ``` |
| To | ``` func Tcl_AllowExceptions(_ interp: UnsafeMutablePointer<Tcl_Interp>) ``` |

Modified Tcl_AppInit(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppInit(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_AppInit(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_AppInitProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_AppInitProc = ((UnsafePointer<Tcl_Interp>) -> Int32) ``` |
| To | ``` typealias Tcl_AppInitProc = ((UnsafeMutablePointer<Tcl_Interp>) -> Int32) ``` |

Modified Tcl_AppendAllObjTypes(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendAllObjTypes(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_AppendAllObjTypes(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_AppendElement(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendElement(_ interp: UnsafePointer<Tcl_Interp>, _ element: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_AppendElement(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ element: UnsafePointer<Int8>) ``` |

Modified Tcl_AppendExportList(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendExportList(_ interp: UnsafePointer<Tcl_Interp>, _ nsPtr: UnsafePointer<Tcl_Namespace>, _ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_AppendExportList(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ nsPtr: UnsafeMutablePointer<Tcl_Namespace>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_AppendFormatToObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendFormatToObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ format: ConstUnsafePointer<Int8>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_AppendFormatToObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ format: UnsafePointer<Int8>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_AppendLimitedToObj(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, Int32, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendLimitedToObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ bytes: ConstUnsafePointer<Int8>, _ length: Int32, _ limit: Int32, _ ellipsis: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_AppendLimitedToObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ bytes: UnsafePointer<Int8>, _ length: Int32, _ limit: Int32, _ ellipsis: UnsafePointer<Int8>) ``` |

Modified Tcl_AppendObjToErrorInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendObjToErrorInfo(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_AppendObjToErrorInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_AppendObjToObj(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendObjToObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ appendObjPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_AppendObjToObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ appendObjPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_AppendResultVA(UnsafeMutablePointer<Tcl_Interp>, CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendResultVA(_ interp: UnsafePointer<Tcl_Interp>, _ argList: CVaListPointer) ``` |
| To | ``` func Tcl_AppendResultVA(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ argList: CVaListPointer) ``` |

Modified Tcl_AppendStringsToObjVA(UnsafeMutablePointer<Tcl_Obj>, CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendStringsToObjVA(_ objPtr: UnsafePointer<Tcl_Obj>, _ argList: CVaListPointer) ``` |
| To | ``` func Tcl_AppendStringsToObjVA(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ argList: CVaListPointer) ``` |

Modified Tcl_AppendToObj(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendToObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ bytes: ConstUnsafePointer<Int8>, _ length: Int32) ``` |
| To | ``` func Tcl_AppendToObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ bytes: UnsafePointer<Int8>, _ length: Int32) ``` |

Modified Tcl_AppendUnicodeToObj(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AppendUnicodeToObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ unicode: ConstUnsafePointer<Tcl_UniChar>, _ length: Int32) ``` |
| To | ``` func Tcl_AppendUnicodeToObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ unicode: UnsafePointer<Tcl_UniChar>, _ length: Int32) ``` |

Modified Tcl_AsyncInvoke(UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AsyncInvoke(_ interp: UnsafePointer<Tcl_Interp>, _ code: Int32) -> Int32 ``` |
| To | ``` func Tcl_AsyncInvoke(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ code: Int32) -> Int32 ``` |

Modified Tcl_AsyncProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_AsyncProc = ((ClientData, UnsafePointer<Tcl_Interp>, Int32) -> Int32) ``` |
| To | ``` typealias Tcl_AsyncProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32) ``` |

Modified Tcl_AttemptAlloc(UInt32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AttemptAlloc(_ size: UInt32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_AttemptAlloc(_ size: UInt32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_AttemptDbCkalloc(UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AttemptDbCkalloc(_ size: UInt32, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_AttemptDbCkalloc(_ size: UInt32, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_AttemptDbCkrealloc(UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AttemptDbCkrealloc(_ ptr: UnsafePointer<Int8>, _ size: UInt32, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_AttemptDbCkrealloc(_ ptr: UnsafeMutablePointer<Int8>, _ size: UInt32, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_AttemptRealloc(UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AttemptRealloc(_ ptr: UnsafePointer<Int8>, _ size: UInt32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_AttemptRealloc(_ ptr: UnsafeMutablePointer<Int8>, _ size: UInt32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_AttemptSetObjLength(UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AttemptSetObjLength(_ objPtr: UnsafePointer<Tcl_Obj>, _ length: Int32) -> Int32 ``` |
| To | ``` func Tcl_AttemptSetObjLength(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ length: Int32) -> Int32 ``` |

Modified Tcl_BackgroundError(UnsafeMutablePointer<Tcl_Interp>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_BackgroundError(_ interp: UnsafePointer<Tcl_Interp>) ``` |
| To | ``` func Tcl_BackgroundError(_ interp: UnsafeMutablePointer<Tcl_Interp>) ``` |

Modified Tcl_Backslash(UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int8

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Backslash(_ src: ConstUnsafePointer<Int8>, _ readPtr: UnsafePointer<Int32>) -> Int8 ``` |
| To | ``` func Tcl_Backslash(_ src: UnsafePointer<Int8>, _ readPtr: UnsafeMutablePointer<Int32>) -> Int8 ``` |

Modified Tcl_BadChannelOption(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_BadChannelOption(_ interp: UnsafePointer<Tcl_Interp>, _ optionName: ConstUnsafePointer<Int8>, _ optionList: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_BadChannelOption(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ optionName: UnsafePointer<Int8>, _ optionList: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_CallWhenDeleted(UnsafeMutablePointer<Tcl_Interp>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CallWhenDeleted(_ interp: UnsafePointer<Tcl_Interp>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CallWhenDeleted(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |

Modified Tcl_ChannelBlockModeProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverBlockModeProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelBlockModeProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverBlockModeProc> ``` |
| To | ``` func Tcl_ChannelBlockModeProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverBlockModeProc> ``` |

Modified Tcl_ChannelClose2Proc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverClose2Proc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelClose2Proc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverClose2Proc> ``` |
| To | ``` func Tcl_ChannelClose2Proc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverClose2Proc> ``` |

Modified Tcl_ChannelCloseProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverCloseProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelCloseProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverCloseProc> ``` |
| To | ``` func Tcl_ChannelCloseProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverCloseProc> ``` |

Modified Tcl_ChannelFlushProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverFlushProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelFlushProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverFlushProc> ``` |
| To | ``` func Tcl_ChannelFlushProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverFlushProc> ``` |

Modified Tcl_ChannelGetHandleProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetHandleProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelGetHandleProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetHandleProc> ``` |
| To | ``` func Tcl_ChannelGetHandleProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetHandleProc> ``` |

Modified Tcl_ChannelGetOptionProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetOptionProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelGetOptionProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetOptionProc> ``` |
| To | ``` func Tcl_ChannelGetOptionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetOptionProc> ``` |

Modified Tcl_ChannelHandlerProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverHandlerProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelHandlerProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverHandlerProc> ``` |
| To | ``` func Tcl_ChannelHandlerProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverHandlerProc> ``` |

Modified Tcl_ChannelInputProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverInputProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelInputProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverInputProc> ``` |
| To | ``` func Tcl_ChannelInputProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverInputProc> ``` |

Modified Tcl_ChannelName(UnsafePointer<Tcl_ChannelType>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelName(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_ChannelName(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> UnsafePointer<Int8> ``` |

Modified Tcl_ChannelOutputProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverOutputProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelOutputProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverOutputProc> ``` |
| To | ``` func Tcl_ChannelOutputProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverOutputProc> ``` |

Modified Tcl_ChannelSeekProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSeekProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelSeekProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSeekProc> ``` |
| To | ``` func Tcl_ChannelSeekProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSeekProc> ``` |

Modified Tcl_ChannelSetOptionProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSetOptionProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelSetOptionProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSetOptionProc> ``` |
| To | ``` func Tcl_ChannelSetOptionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSetOptionProc> ``` |

Modified Tcl_ChannelThreadActionProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverThreadActionProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelThreadActionProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverThreadActionProc> ``` |
| To | ``` func Tcl_ChannelThreadActionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverThreadActionProc> ``` |

Modified Tcl_ChannelTruncateProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverTruncateProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelTruncateProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverTruncateProc> ``` |
| To | ``` func Tcl_ChannelTruncateProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverTruncateProc> ``` |

Modified Tcl_ChannelVersion(UnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelVersion(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion ``` |
| To | ``` func Tcl_ChannelVersion(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion ``` |

Modified Tcl_ChannelWatchProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWatchProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelWatchProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWatchProc> ``` |
| To | ``` func Tcl_ChannelWatchProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWatchProc> ``` |

Modified Tcl_ChannelWideSeekProc(UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWideSeekProc>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelWideSeekProc(_ chanTypePtr: ConstUnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWideSeekProc> ``` |
| To | ``` func Tcl_ChannelWideSeekProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWideSeekProc> ``` |

Modified Tcl_Chdir(UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Chdir(_ dirName: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_Chdir(_ dirName: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_Close(UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Close(_ interp: UnsafePointer<Tcl_Interp>, _ chan: Tcl_Channel) -> Int32 ``` |
| To | ``` func Tcl_Close(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ chan: Tcl_Channel) -> Int32 ``` |

Modified Tcl_CmdObjTraceProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_CmdObjTraceProc = ((ClientData, UnsafePointer<Tcl_Interp>, Int32, ConstUnsafePointer<Int8>, Tcl_Command, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32) ``` |
| To | ``` typealias Tcl_CmdObjTraceProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, Tcl_Command, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32) ``` |

Modified Tcl_CmdProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_CmdProc = ((ClientData, UnsafePointer<Tcl_Interp>, Int32, UnsafePointer<ConstUnsafePointer<Int8>>) -> Int32) ``` |
| To | ``` typealias Tcl_CmdProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32) ``` |

Modified Tcl_CmdTraceProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_CmdTraceProc = ((ClientData, UnsafePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, CFunctionPointer<Tcl_CmdProc>, ClientData, Int32, UnsafePointer<ConstUnsafePointer<Int8>>) -> Void) ``` |
| To | ``` typealias Tcl_CmdTraceProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Int8>, CFunctionPointer<Tcl_CmdProc>, ClientData, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void) ``` |

Modified Tcl_CommandComplete(UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CommandComplete(_ cmd: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_CommandComplete(_ cmd: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_CommandTraceInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CommandTraceInfo(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_CommandTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |
| To | ``` func Tcl_CommandTraceInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_CommandTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |

Modified Tcl_CommandTraceProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_CommandTraceProc = ((ClientData, UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> Void) ``` |
| To | ``` typealias Tcl_CommandTraceProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void) ``` |

Modified Tcl_CompareHashKeysProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_CompareHashKeysProc = ((UnsafePointer<()>, UnsafePointer<Tcl_HashEntry>) -> Int32) ``` |
| To | ``` typealias Tcl_CompareHashKeysProc = ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Tcl_HashEntry>) -> Int32) ``` |

Modified Tcl_Concat(Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Concat(_ argc: Int32, _ argv: ConstUnsafePointer<ConstUnsafePointer<Int8>>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_Concat(_ argc: Int32, _ argv: UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_ConcatObj(Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ConcatObj(_ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_ConcatObj(_ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_ConditionFinalize(UnsafeMutablePointer<Tcl_Condition>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ConditionFinalize(_ condPtr: UnsafePointer<Tcl_Condition>) ``` |
| To | ``` func Tcl_ConditionFinalize(_ condPtr: UnsafeMutablePointer<Tcl_Condition>) ``` |

Modified Tcl_ConditionNotify(UnsafeMutablePointer<Tcl_Condition>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ConditionNotify(_ condPtr: UnsafePointer<Tcl_Condition>) ``` |
| To | ``` func Tcl_ConditionNotify(_ condPtr: UnsafeMutablePointer<Tcl_Condition>) ``` |

Modified Tcl_ConditionWait(UnsafeMutablePointer<Tcl_Condition>, UnsafeMutablePointer<Tcl_Mutex>, UnsafeMutablePointer<Tcl_Time>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ConditionWait(_ condPtr: UnsafePointer<Tcl_Condition>, _ mutexPtr: UnsafePointer<Tcl_Mutex>, _ timePtr: UnsafePointer<Tcl_Time>) ``` |
| To | ``` func Tcl_ConditionWait(_ condPtr: UnsafeMutablePointer<Tcl_Condition>, _ mutexPtr: UnsafeMutablePointer<Tcl_Mutex>, _ timePtr: UnsafeMutablePointer<Tcl_Time>) ``` |

Modified Tcl_ConvertCountedElement(UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ConvertCountedElement(_ src: ConstUnsafePointer<Int8>, _ length: Int32, _ dst: UnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_ConvertCountedElement(_ src: UnsafePointer<Int8>, _ length: Int32, _ dst: UnsafeMutablePointer<Int8>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_ConvertElement(UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ConvertElement(_ src: ConstUnsafePointer<Int8>, _ dst: UnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_ConvertElement(_ src: UnsafePointer<Int8>, _ dst: UnsafeMutablePointer<Int8>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_ConvertToType(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_ObjType>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ConvertToType(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ typePtr: UnsafePointer<Tcl_ObjType>) -> Int32 ``` |
| To | ``` func Tcl_ConvertToType(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ typePtr: UnsafeMutablePointer<Tcl_ObjType>) -> Int32 ``` |

Modified Tcl_CreateAlias(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafePointer<Int8>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateAlias(_ slave: UnsafePointer<Tcl_Interp>, _ slaveCmd: ConstUnsafePointer<Int8>, _ target: UnsafePointer<Tcl_Interp>, _ targetCmd: ConstUnsafePointer<Int8>, _ argc: Int32, _ argv: ConstUnsafePointer<ConstUnsafePointer<Int8>>) -> Int32 ``` |
| To | ``` func Tcl_CreateAlias(_ slave: UnsafeMutablePointer<Tcl_Interp>, _ slaveCmd: UnsafePointer<Int8>, _ target: UnsafeMutablePointer<Tcl_Interp>, _ targetCmd: UnsafePointer<Int8>, _ argc: Int32, _ argv: UnsafePointer<UnsafePointer<Int8>>) -> Int32 ``` |

Modified Tcl_CreateAliasObj(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateAliasObj(_ slave: UnsafePointer<Tcl_Interp>, _ slaveCmd: ConstUnsafePointer<Int8>, _ target: UnsafePointer<Tcl_Interp>, _ targetCmd: ConstUnsafePointer<Int8>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_CreateAliasObj(_ slave: UnsafeMutablePointer<Tcl_Interp>, _ slaveCmd: UnsafePointer<Int8>, _ target: UnsafeMutablePointer<Tcl_Interp>, _ targetCmd: UnsafePointer<Int8>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_CreateChannel(UnsafeMutablePointer<Tcl_ChannelType>, UnsafePointer<Int8>, ClientData, Int32) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateChannel(_ typePtr: UnsafePointer<Tcl_ChannelType>, _ chanName: ConstUnsafePointer<Int8>, _ instanceData: ClientData, _ mask: Int32) -> Tcl_Channel ``` |
| To | ``` func Tcl_CreateChannel(_ typePtr: UnsafeMutablePointer<Tcl_ChannelType>, _ chanName: UnsafePointer<Int8>, _ instanceData: ClientData, _ mask: Int32) -> Tcl_Channel ``` |

Modified Tcl_CreateCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_CmdProc>, ClientData, CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateCommand(_ interp: UnsafePointer<Tcl_Interp>, _ cmdName: ConstUnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_CmdProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command ``` |
| To | ``` func Tcl_CreateCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_CmdProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command ``` |

Modified Tcl_CreateEncoding(UnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateEncoding(_ typePtr: ConstUnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding ``` |
| To | ``` func Tcl_CreateEncoding(_ typePtr: UnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding ``` |

Modified Tcl_CreateEnsemble(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateEnsemble(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ namespacePtr: UnsafePointer<Tcl_Namespace>, _ flags: Int32) -> Tcl_Command ``` |
| To | ``` func Tcl_CreateEnsemble(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ namespacePtr: UnsafeMutablePointer<Tcl_Namespace>, _ flags: Int32) -> Tcl_Command ``` |

Modified Tcl_CreateHashEntry(UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateHashEntry(_ tablePtr: UnsafePointer<Tcl_HashTable>, _ key: ConstUnsafePointer<Int8>, _ newPtr: UnsafePointer<Int32>) -> UnsafePointer<Tcl_HashEntry> ``` |
| To | ``` func Tcl_CreateHashEntry(_ tablePtr: UnsafeMutablePointer<Tcl_HashTable>, _ key: UnsafePointer<Int8>, _ newPtr: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry> ``` |

Modified Tcl_CreateInterp() -> UnsafeMutablePointer<Tcl_Interp>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateInterp() -> UnsafePointer<Tcl_Interp> ``` |
| To | ``` func Tcl_CreateInterp() -> UnsafeMutablePointer<Tcl_Interp> ``` |

Modified Tcl_CreateMathFunc(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_ValueType>, CFunctionPointer<Tcl_MathProc>, ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateMathFunc(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ numArgs: Int32, _ argTypes: UnsafePointer<Tcl_ValueType>, _ proc: CFunctionPointer<Tcl_MathProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CreateMathFunc(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ numArgs: Int32, _ argTypes: UnsafeMutablePointer<Tcl_ValueType>, _ proc: CFunctionPointer<Tcl_MathProc>, _ clientData: ClientData) ``` |

Modified Tcl_CreateNamespace(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ClientData, CFunctionPointer<Tcl_NamespaceDeleteProc>) -> UnsafeMutablePointer<Tcl_Namespace>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateNamespace(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>) -> UnsafePointer<Tcl_Namespace> ``` |
| To | ``` func Tcl_CreateNamespace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>) -> UnsafeMutablePointer<Tcl_Namespace> ``` |

Modified Tcl_CreateObjCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_ObjCmdProc>, ClientData, CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateObjCommand(_ interp: UnsafePointer<Tcl_Interp>, _ cmdName: ConstUnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_ObjCmdProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command ``` |
| To | ``` func Tcl_CreateObjCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_ObjCmdProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command ``` |

Modified Tcl_CreateObjTrace(UnsafeMutablePointer<Tcl_Interp>, Int32, Int32, CFunctionPointer<Tcl_CmdObjTraceProc>, ClientData, CFunctionPointer<Tcl_CmdObjTraceDeleteProc>) -> Tcl_Trace

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateObjTrace(_ interp: UnsafePointer<Tcl_Interp>, _ level: Int32, _ flags: Int32, _ objProc: CFunctionPointer<Tcl_CmdObjTraceProc>, _ clientData: ClientData, _ delProc: CFunctionPointer<Tcl_CmdObjTraceDeleteProc>) -> Tcl_Trace ``` |
| To | ``` func Tcl_CreateObjTrace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ level: Int32, _ flags: Int32, _ objProc: CFunctionPointer<Tcl_CmdObjTraceProc>, _ clientData: ClientData, _ delProc: CFunctionPointer<Tcl_CmdObjTraceDeleteProc>) -> Tcl_Trace ``` |

Modified Tcl_CreateSlave(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Interp>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateSlave(_ interp: UnsafePointer<Tcl_Interp>, _ slaveName: ConstUnsafePointer<Int8>, _ isSafe: Int32) -> UnsafePointer<Tcl_Interp> ``` |
| To | ``` func Tcl_CreateSlave(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ slaveName: UnsafePointer<Int8>, _ isSafe: Int32) -> UnsafeMutablePointer<Tcl_Interp> ``` |

Modified Tcl_CreateThread(UnsafeMutablePointer<Tcl_ThreadId>, CFunctionPointer<Tcl_ThreadCreateProc>, ClientData, Int32, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateThread(_ idPtr: UnsafePointer<Tcl_ThreadId>, _ proc: CFunctionPointer<Tcl_ThreadCreateProc>, _ clientData: ClientData, _ stackSize: Int32, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_CreateThread(_ idPtr: UnsafeMutablePointer<Tcl_ThreadId>, _ proc: CFunctionPointer<Tcl_ThreadCreateProc>, _ clientData: ClientData, _ stackSize: Int32, _ flags: Int32) -> Int32 ``` |

Modified Tcl_CreateTrace(UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_CmdTraceProc>, ClientData) -> Tcl_Trace

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateTrace(_ interp: UnsafePointer<Tcl_Interp>, _ level: Int32, _ proc: CFunctionPointer<Tcl_CmdTraceProc>, _ clientData: ClientData) -> Tcl_Trace ``` |
| To | ``` func Tcl_CreateTrace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ level: Int32, _ proc: CFunctionPointer<Tcl_CmdTraceProc>, _ clientData: ClientData) -> Tcl_Trace ``` |

Modified Tcl_DStringAppend(UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringAppend(_ dsPtr: UnsafePointer<Tcl_DString>, _ bytes: ConstUnsafePointer<Int8>, _ length: Int32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_DStringAppend(_ dsPtr: UnsafeMutablePointer<Tcl_DString>, _ bytes: UnsafePointer<Int8>, _ length: Int32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_DStringAppendElement(UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringAppendElement(_ dsPtr: UnsafePointer<Tcl_DString>, _ element: ConstUnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_DStringAppendElement(_ dsPtr: UnsafeMutablePointer<Tcl_DString>, _ element: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_DStringEndSublist(UnsafeMutablePointer<Tcl_DString>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringEndSublist(_ dsPtr: UnsafePointer<Tcl_DString>) ``` |
| To | ``` func Tcl_DStringEndSublist(_ dsPtr: UnsafeMutablePointer<Tcl_DString>) ``` |

Modified Tcl_DStringFree(UnsafeMutablePointer<Tcl_DString>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringFree(_ dsPtr: UnsafePointer<Tcl_DString>) ``` |
| To | ``` func Tcl_DStringFree(_ dsPtr: UnsafeMutablePointer<Tcl_DString>) ``` |

Modified Tcl_DStringGetResult(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringGetResult(_ interp: UnsafePointer<Tcl_Interp>, _ dsPtr: UnsafePointer<Tcl_DString>) ``` |
| To | ``` func Tcl_DStringGetResult(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dsPtr: UnsafeMutablePointer<Tcl_DString>) ``` |

Modified Tcl_DStringInit(UnsafeMutablePointer<Tcl_DString>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringInit(_ dsPtr: UnsafePointer<Tcl_DString>) ``` |
| To | ``` func Tcl_DStringInit(_ dsPtr: UnsafeMutablePointer<Tcl_DString>) ``` |

Modified Tcl_DStringResult(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringResult(_ interp: UnsafePointer<Tcl_Interp>, _ dsPtr: UnsafePointer<Tcl_DString>) ``` |
| To | ``` func Tcl_DStringResult(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dsPtr: UnsafeMutablePointer<Tcl_DString>) ``` |

Modified Tcl_DStringSetLength(UnsafeMutablePointer<Tcl_DString>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringSetLength(_ dsPtr: UnsafePointer<Tcl_DString>, _ length: Int32) ``` |
| To | ``` func Tcl_DStringSetLength(_ dsPtr: UnsafeMutablePointer<Tcl_DString>, _ length: Int32) ``` |

Modified Tcl_DStringStartSublist(UnsafeMutablePointer<Tcl_DString>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DStringStartSublist(_ dsPtr: UnsafePointer<Tcl_DString>) ``` |
| To | ``` func Tcl_DStringStartSublist(_ dsPtr: UnsafeMutablePointer<Tcl_DString>) ``` |

Modified Tcl_DbCkalloc(UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbCkalloc(_ size: UInt32, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_DbCkalloc(_ size: UInt32, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_DbCkfree(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbCkfree(_ ptr: UnsafePointer<Int8>, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> Int32 ``` |
| To | ``` func Tcl_DbCkfree(_ ptr: UnsafeMutablePointer<Int8>, _ file: UnsafePointer<Int8>, _ line: Int32) -> Int32 ``` |

Modified Tcl_DbCkrealloc(UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbCkrealloc(_ ptr: UnsafePointer<Int8>, _ size: UInt32, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_DbCkrealloc(_ ptr: UnsafeMutablePointer<Int8>, _ size: UInt32, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_DbDecrRefCount(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbDecrRefCount(_ objPtr: UnsafePointer<Tcl_Obj>, _ file: ConstUnsafePointer<Int8>, _ line: Int32) ``` |
| To | ``` func Tcl_DbDecrRefCount(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ file: UnsafePointer<Int8>, _ line: Int32) ``` |

Modified Tcl_DbIncrRefCount(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbIncrRefCount(_ objPtr: UnsafePointer<Tcl_Obj>, _ file: ConstUnsafePointer<Int8>, _ line: Int32) ``` |
| To | ``` func Tcl_DbIncrRefCount(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ file: UnsafePointer<Int8>, _ line: Int32) ``` |

Modified Tcl_DbIsShared(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbIsShared(_ objPtr: UnsafePointer<Tcl_Obj>, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> Int32 ``` |
| To | ``` func Tcl_DbIsShared(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ file: UnsafePointer<Int8>, _ line: Int32) -> Int32 ``` |

Modified Tcl_DbNewBignumObj(UnsafeMutablePointer<mp_int>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewBignumObj(_ value: UnsafePointer<mp_int>, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewBignumObj(_ value: UnsafeMutablePointer<mp_int>, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewBooleanObj(Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewBooleanObj(_ boolValue: Int32, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewBooleanObj(_ boolValue: Int32, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewByteArrayObj(UnsafePointer<UInt8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewByteArrayObj(_ bytes: ConstUnsafePointer<UInt8>, _ length: Int32, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewByteArrayObj(_ bytes: UnsafePointer<UInt8>, _ length: Int32, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewDictObj(UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewDictObj(_ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewDictObj(_ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewDoubleObj(Double, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewDoubleObj(_ doubleValue: Double, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewDoubleObj(_ doubleValue: Double, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewListObj(Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewListObj(_ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewListObj(_ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewLongObj(Int, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewLongObj(_ longValue: Int, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewLongObj(_ longValue: Int, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewObj(UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewObj(_ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewObj(_ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewStringObj(UnsafePointer<Int8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewStringObj(_ bytes: ConstUnsafePointer<Int8>, _ length: Int32, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewStringObj(_ bytes: UnsafePointer<Int8>, _ length: Int32, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DbNewWideIntObj(Tcl_WideInt, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DbNewWideIntObj(_ wideValue: Tcl_WideInt, _ file: ConstUnsafePointer<Int8>, _ line: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DbNewWideIntObj(_ wideValue: Tcl_WideInt, _ file: UnsafePointer<Int8>, _ line: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_DecrRefCount(UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DecrRefCount(_ objPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_DecrRefCount(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_DeleteAssocData(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteAssocData(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_DeleteAssocData(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>) ``` |

Modified Tcl_DeleteCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteCommand(_ interp: UnsafePointer<Tcl_Interp>, _ cmdName: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_DeleteCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_DeleteCommandFromToken(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteCommandFromToken(_ interp: UnsafePointer<Tcl_Interp>, _ command: Tcl_Command) -> Int32 ``` |
| To | ``` func Tcl_DeleteCommandFromToken(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ command: Tcl_Command) -> Int32 ``` |

Modified Tcl_DeleteHashEntry(UnsafeMutablePointer<Tcl_HashEntry>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteHashEntry(_ entryPtr: UnsafePointer<Tcl_HashEntry>) ``` |
| To | ``` func Tcl_DeleteHashEntry(_ entryPtr: UnsafeMutablePointer<Tcl_HashEntry>) ``` |

Modified Tcl_DeleteHashTable(UnsafeMutablePointer<Tcl_HashTable>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteHashTable(_ tablePtr: UnsafePointer<Tcl_HashTable>) ``` |
| To | ``` func Tcl_DeleteHashTable(_ tablePtr: UnsafeMutablePointer<Tcl_HashTable>) ``` |

Modified Tcl_DeleteInterp(UnsafeMutablePointer<Tcl_Interp>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteInterp(_ interp: UnsafePointer<Tcl_Interp>) ``` |
| To | ``` func Tcl_DeleteInterp(_ interp: UnsafeMutablePointer<Tcl_Interp>) ``` |

Modified Tcl_DeleteNamespace(UnsafeMutablePointer<Tcl_Namespace>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteNamespace(_ nsPtr: UnsafePointer<Tcl_Namespace>) ``` |
| To | ``` func Tcl_DeleteNamespace(_ nsPtr: UnsafeMutablePointer<Tcl_Namespace>) ``` |

Modified Tcl_DeleteTrace(UnsafeMutablePointer<Tcl_Interp>, Tcl_Trace)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteTrace(_ interp: UnsafePointer<Tcl_Interp>, _ trace: Tcl_Trace) ``` |
| To | ``` func Tcl_DeleteTrace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ trace: Tcl_Trace) ``` |

Modified Tcl_DetachChannel(UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DetachChannel(_ interp: UnsafePointer<Tcl_Interp>, _ channel: Tcl_Channel) -> Int32 ``` |
| To | ``` func Tcl_DetachChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ channel: Tcl_Channel) -> Int32 ``` |

Modified Tcl_DetachPids(Int32, UnsafeMutablePointer<Tcl_Pid>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DetachPids(_ numPids: Int32, _ pidPtr: UnsafePointer<Tcl_Pid>) ``` |
| To | ``` func Tcl_DetachPids(_ numPids: Int32, _ pidPtr: UnsafeMutablePointer<Tcl_Pid>) ``` |

Modified Tcl_DictObjDone(UnsafeMutablePointer<Tcl_DictSearch>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjDone(_ searchPtr: UnsafePointer<Tcl_DictSearch>) ``` |
| To | ``` func Tcl_DictObjDone(_ searchPtr: UnsafeMutablePointer<Tcl_DictSearch>) ``` |

Modified Tcl_DictObjFirst(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjFirst(_ interp: UnsafePointer<Tcl_Interp>, _ dictPtr: UnsafePointer<Tcl_Obj>, _ searchPtr: UnsafePointer<Tcl_DictSearch>, _ keyPtrPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>, _ valuePtrPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>, _ donePtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_DictObjFirst(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dictPtr: UnsafeMutablePointer<Tcl_Obj>, _ searchPtr: UnsafeMutablePointer<Tcl_DictSearch>, _ keyPtrPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, _ valuePtrPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, _ donePtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_DictObjGet(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjGet(_ interp: UnsafePointer<Tcl_Interp>, _ dictPtr: UnsafePointer<Tcl_Obj>, _ keyPtr: UnsafePointer<Tcl_Obj>, _ valuePtrPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_DictObjGet(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dictPtr: UnsafeMutablePointer<Tcl_Obj>, _ keyPtr: UnsafeMutablePointer<Tcl_Obj>, _ valuePtrPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_DictObjNext(UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjNext(_ searchPtr: UnsafePointer<Tcl_DictSearch>, _ keyPtrPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>, _ valuePtrPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>, _ donePtr: UnsafePointer<Int32>) ``` |
| To | ``` func Tcl_DictObjNext(_ searchPtr: UnsafeMutablePointer<Tcl_DictSearch>, _ keyPtrPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, _ valuePtrPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, _ donePtr: UnsafeMutablePointer<Int32>) ``` |

Modified Tcl_DictObjPut(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjPut(_ interp: UnsafePointer<Tcl_Interp>, _ dictPtr: UnsafePointer<Tcl_Obj>, _ keyPtr: UnsafePointer<Tcl_Obj>, _ valuePtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_DictObjPut(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dictPtr: UnsafeMutablePointer<Tcl_Obj>, _ keyPtr: UnsafeMutablePointer<Tcl_Obj>, _ valuePtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_DictObjPutKeyList(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjPutKeyList(_ interp: UnsafePointer<Tcl_Interp>, _ dictPtr: UnsafePointer<Tcl_Obj>, _ keyc: Int32, _ keyv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, _ valuePtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_DictObjPutKeyList(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dictPtr: UnsafeMutablePointer<Tcl_Obj>, _ keyc: Int32, _ keyv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, _ valuePtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_DictObjRemove(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjRemove(_ interp: UnsafePointer<Tcl_Interp>, _ dictPtr: UnsafePointer<Tcl_Obj>, _ keyPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_DictObjRemove(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dictPtr: UnsafeMutablePointer<Tcl_Obj>, _ keyPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_DictObjRemoveKeyList(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjRemoveKeyList(_ interp: UnsafePointer<Tcl_Interp>, _ dictPtr: UnsafePointer<Tcl_Obj>, _ keyc: Int32, _ keyv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_DictObjRemoveKeyList(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dictPtr: UnsafeMutablePointer<Tcl_Obj>, _ keyc: Int32, _ keyv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_DictObjSize(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DictObjSize(_ interp: UnsafePointer<Tcl_Interp>, _ dictPtr: UnsafePointer<Tcl_Obj>, _ sizePtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_DictObjSize(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ dictPtr: UnsafeMutablePointer<Tcl_Obj>, _ sizePtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_DiscardResult(UnsafeMutablePointer<Tcl_SavedResult>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DiscardResult(_ statePtr: UnsafePointer<Tcl_SavedResult>) ``` |
| To | ``` func Tcl_DiscardResult(_ statePtr: UnsafeMutablePointer<Tcl_SavedResult>) ``` |

Modified Tcl_DontCallWhenDeleted(UnsafeMutablePointer<Tcl_Interp>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DontCallWhenDeleted(_ interp: UnsafePointer<Tcl_Interp>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DontCallWhenDeleted(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |

Modified Tcl_DriverClose2Proc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverClose2Proc = ((ClientData, UnsafePointer<Tcl_Interp>, Int32) -> Int32) ``` |
| To | ``` typealias Tcl_DriverClose2Proc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32) ``` |

Modified Tcl_DriverCloseProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverCloseProc = ((ClientData, UnsafePointer<Tcl_Interp>) -> Int32) ``` |
| To | ``` typealias Tcl_DriverCloseProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32) ``` |

Modified Tcl_DriverGetHandleProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverGetHandleProc = ((ClientData, Int32, UnsafePointer<ClientData>) -> Int32) ``` |
| To | ``` typealias Tcl_DriverGetHandleProc = ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32) ``` |

Modified Tcl_DriverGetOptionProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverGetOptionProc = ((ClientData, UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_DString>) -> Int32) ``` |
| To | ``` typealias Tcl_DriverGetOptionProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32) ``` |

Modified Tcl_DriverInputProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverInputProc = ((ClientData, UnsafePointer<Int8>, Int32, UnsafePointer<Int32>) -> Int32) ``` |
| To | ``` typealias Tcl_DriverInputProc = ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32) ``` |

Modified Tcl_DriverOutputProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverOutputProc = ((ClientData, ConstUnsafePointer<Int8>, Int32, UnsafePointer<Int32>) -> Int32) ``` |
| To | ``` typealias Tcl_DriverOutputProc = ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32) ``` |

Modified Tcl_DriverSeekProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverSeekProc = ((ClientData, Int, Int32, UnsafePointer<Int32>) -> Int32) ``` |
| To | ``` typealias Tcl_DriverSeekProc = ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32) ``` |

Modified Tcl_DriverSetOptionProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverSetOptionProc = ((ClientData, UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>) -> Int32) ``` |
| To | ``` typealias Tcl_DriverSetOptionProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32) ``` |

Modified Tcl_DriverWideSeekProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DriverWideSeekProc = ((ClientData, Tcl_WideInt, Int32, UnsafePointer<Int32>) -> Tcl_WideInt) ``` |
| To | ``` typealias Tcl_DriverWideSeekProc = ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt) ``` |

Modified Tcl_DumpActiveMemory(UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DumpActiveMemory(_ fileName: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_DumpActiveMemory(_ fileName: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_DupInternalRepProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_DupInternalRepProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Void) ``` |
| To | ``` typealias Tcl_DupInternalRepProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void) ``` |

Modified Tcl_DuplicateObj(UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DuplicateObj(_ objPtr: UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_DuplicateObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_EncodingConvertProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_EncodingConvertProc = ((ClientData, ConstUnsafePointer<Int8>, Int32, Int32, UnsafePointer<Tcl_EncodingState>, UnsafePointer<Int8>, Int32, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Int32>) -> Int32) ``` |
| To | ``` typealias Tcl_EncodingConvertProc = ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32) ``` |

Modified Tcl_ErrnoId() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ErrnoId() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_ErrnoId() -> UnsafePointer<Int8> ``` |

Modified Tcl_ErrnoMsg(Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ErrnoMsg(_ err: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_ErrnoMsg(_ err: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_Eval(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Eval(_ interp: UnsafePointer<Tcl_Interp>, _ script: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_Eval(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ script: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_EvalEx(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_EvalEx(_ interp: UnsafePointer<Tcl_Interp>, _ script: ConstUnsafePointer<Int8>, _ numBytes: Int32, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_EvalEx(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ script: UnsafePointer<Int8>, _ numBytes: Int32, _ flags: Int32) -> Int32 ``` |

Modified Tcl_EvalFile(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_EvalFile(_ interp: UnsafePointer<Tcl_Interp>, _ fileName: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_EvalFile(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ fileName: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_EvalObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_EvalObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_EvalObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_EvalObjEx(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_EvalObjEx(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_EvalObjEx(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_EvalObjv(UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_EvalObjv(_ interp: UnsafePointer<Tcl_Interp>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_EvalObjv(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_EvalTokens(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_EvalTokens(_ interp: UnsafePointer<Tcl_Interp>, _ tokenPtr: UnsafePointer<Tcl_Token>, _ count: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_EvalTokens(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ tokenPtr: UnsafeMutablePointer<Tcl_Token>, _ count: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_EvalTokensStandard(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_EvalTokensStandard(_ interp: UnsafePointer<Tcl_Interp>, _ tokenPtr: UnsafePointer<Tcl_Token>, _ count: Int32) -> Int32 ``` |
| To | ``` func Tcl_EvalTokensStandard(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ tokenPtr: UnsafeMutablePointer<Tcl_Token>, _ count: Int32) -> Int32 ``` |

Modified Tcl_EventDeleteProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_EventDeleteProc = ((UnsafePointer<Tcl_Event>, ClientData) -> Int32) ``` |
| To | ``` typealias Tcl_EventDeleteProc = ((UnsafeMutablePointer<Tcl_Event>, ClientData) -> Int32) ``` |

Modified Tcl_EventProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_EventProc = ((UnsafePointer<Tcl_Event>, Int32) -> Int32) ``` |
| To | ``` typealias Tcl_EventProc = ((UnsafeMutablePointer<Tcl_Event>, Int32) -> Int32) ``` |

Modified Tcl_Export(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Export(_ interp: UnsafePointer<Tcl_Interp>, _ nsPtr: UnsafePointer<Tcl_Namespace>, _ pattern: ConstUnsafePointer<Int8>, _ resetListFirst: Int32) -> Int32 ``` |
| To | ``` func Tcl_Export(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ nsPtr: UnsafeMutablePointer<Tcl_Namespace>, _ pattern: UnsafePointer<Int8>, _ resetListFirst: Int32) -> Int32 ``` |

Modified Tcl_ExposeCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExposeCommand(_ interp: UnsafePointer<Tcl_Interp>, _ hiddenCmdToken: ConstUnsafePointer<Int8>, _ cmdName: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_ExposeCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ hiddenCmdToken: UnsafePointer<Int8>, _ cmdName: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_ExprBoolean(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExprBoolean(_ interp: UnsafePointer<Tcl_Interp>, _ expr: ConstUnsafePointer<Int8>, _ ptr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_ExprBoolean(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ expr: UnsafePointer<Int8>, _ ptr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_ExprBooleanObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExprBooleanObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ ptr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_ExprBooleanObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ ptr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_ExprDouble(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExprDouble(_ interp: UnsafePointer<Tcl_Interp>, _ expr: ConstUnsafePointer<Int8>, _ ptr: UnsafePointer<Double>) -> Int32 ``` |
| To | ``` func Tcl_ExprDouble(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ expr: UnsafePointer<Int8>, _ ptr: UnsafeMutablePointer<Double>) -> Int32 ``` |

Modified Tcl_ExprDoubleObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExprDoubleObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ ptr: UnsafePointer<Double>) -> Int32 ``` |
| To | ``` func Tcl_ExprDoubleObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ ptr: UnsafeMutablePointer<Double>) -> Int32 ``` |

Modified Tcl_ExprLong(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExprLong(_ interp: UnsafePointer<Tcl_Interp>, _ expr: ConstUnsafePointer<Int8>, _ ptr: UnsafePointer<Int>) -> Int32 ``` |
| To | ``` func Tcl_ExprLong(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ expr: UnsafePointer<Int8>, _ ptr: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified Tcl_ExprLongObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExprLongObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ ptr: UnsafePointer<Int>) -> Int32 ``` |
| To | ``` func Tcl_ExprLongObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ ptr: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified Tcl_ExprObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExprObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ resultPtrPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_ExprObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ resultPtrPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_ExprString(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExprString(_ interp: UnsafePointer<Tcl_Interp>, _ expr: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_ExprString(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ expr: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_ExternalToUtf(UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExternalToUtf(_ interp: UnsafePointer<Tcl_Interp>, _ encoding: Tcl_Encoding, _ src: ConstUnsafePointer<Int8>, _ srcLen: Int32, _ flags: Int32, _ statePtr: UnsafePointer<Tcl_EncodingState>, _ dst: UnsafePointer<Int8>, _ dstLen: Int32, _ srcReadPtr: UnsafePointer<Int32>, _ dstWrotePtr: UnsafePointer<Int32>, _ dstCharsPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_ExternalToUtf(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ encoding: Tcl_Encoding, _ src: UnsafePointer<Int8>, _ srcLen: Int32, _ flags: Int32, _ statePtr: UnsafeMutablePointer<Tcl_EncodingState>, _ dst: UnsafeMutablePointer<Int8>, _ dstLen: Int32, _ srcReadPtr: UnsafeMutablePointer<Int32>, _ dstWrotePtr: UnsafeMutablePointer<Int32>, _ dstCharsPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_ExternalToUtfDString(Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ExternalToUtfDString(_ encoding: Tcl_Encoding, _ src: ConstUnsafePointer<Int8>, _ srcLen: Int32, _ dsPtr: UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_ExternalToUtfDString(_ encoding: Tcl_Encoding, _ src: UnsafePointer<Int8>, _ srcLen: Int32, _ dsPtr: UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_FSAccess(UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSAccess(_ pathPtr: UnsafePointer<Tcl_Obj>, _ mode: Int32) -> Int32 ``` |
| To | ``` func Tcl_FSAccess(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ mode: Int32) -> Int32 ``` |

Modified Tcl_FSAccessProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSAccessProc = ((UnsafePointer<Tcl_Obj>, Int32) -> Int32) ``` |
| To | ``` typealias Tcl_FSAccessProc = ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32) ``` |

Modified Tcl_FSChdir(UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSChdir(_ pathPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSChdir(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSChdirProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSChdirProc = ((UnsafePointer<Tcl_Obj>) -> Int32) ``` |
| To | ``` typealias Tcl_FSChdirProc = ((UnsafeMutablePointer<Tcl_Obj>) -> Int32) ``` |

Modified Tcl_FSConvertToPathType(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSConvertToPathType(_ interp: UnsafePointer<Tcl_Interp>, _ pathPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSConvertToPathType(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSCopyDirectory(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSCopyDirectory(_ srcPathPtr: UnsafePointer<Tcl_Obj>, _ destPathPtr: UnsafePointer<Tcl_Obj>, _ errorPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_FSCopyDirectory(_ srcPathPtr: UnsafeMutablePointer<Tcl_Obj>, _ destPathPtr: UnsafeMutablePointer<Tcl_Obj>, _ errorPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_FSCopyDirectoryProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSCopyDirectoryProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32) ``` |
| To | ``` typealias Tcl_FSCopyDirectoryProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32) ``` |

Modified Tcl_FSCopyFile(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSCopyFile(_ srcPathPtr: UnsafePointer<Tcl_Obj>, _ destPathPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSCopyFile(_ srcPathPtr: UnsafeMutablePointer<Tcl_Obj>, _ destPathPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSCopyFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSCopyFileProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32) ``` |
| To | ``` typealias Tcl_FSCopyFileProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32) ``` |

Modified Tcl_FSCreateDirectory(UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSCreateDirectory(_ pathPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSCreateDirectory(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSCreateDirectoryProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSCreateDirectoryProc = ((UnsafePointer<Tcl_Obj>) -> Int32) ``` |
| To | ``` typealias Tcl_FSCreateDirectoryProc = ((UnsafeMutablePointer<Tcl_Obj>) -> Int32) ``` |

Modified Tcl_FSCreateInternalRepProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSCreateInternalRepProc = ((UnsafePointer<Tcl_Obj>) -> ClientData) ``` |
| To | ``` typealias Tcl_FSCreateInternalRepProc = ((UnsafeMutablePointer<Tcl_Obj>) -> ClientData) ``` |

Modified Tcl_FSData(UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSData(_ fsPtr: UnsafePointer<Tcl_Filesystem>) -> ClientData ``` |
| To | ``` func Tcl_FSData(_ fsPtr: UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData ``` |

Modified Tcl_FSDeleteFile(UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSDeleteFile(_ pathPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSDeleteFile(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSDeleteFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSDeleteFileProc = ((UnsafePointer<Tcl_Obj>) -> Int32) ``` |
| To | ``` typealias Tcl_FSDeleteFileProc = ((UnsafeMutablePointer<Tcl_Obj>) -> Int32) ``` |

Modified Tcl_FSEqualPaths(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSEqualPaths(_ firstPtr: UnsafePointer<Tcl_Obj>, _ secondPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSEqualPaths(_ firstPtr: UnsafeMutablePointer<Tcl_Obj>, _ secondPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSEvalFile(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSEvalFile(_ interp: UnsafePointer<Tcl_Interp>, _ fileName: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSEvalFile(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ fileName: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSEvalFileEx(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSEvalFileEx(_ interp: UnsafePointer<Tcl_Interp>, _ fileName: UnsafePointer<Tcl_Obj>, _ encodingName: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_FSEvalFileEx(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ fileName: UnsafeMutablePointer<Tcl_Obj>, _ encodingName: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_FSFileAttrStrings(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSFileAttrStrings(_ pathPtr: UnsafePointer<Tcl_Obj>, _ objPtrRef: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<ConstUnsafePointer<Int8>> ``` |
| To | ``` func Tcl_FSFileAttrStrings(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ objPtrRef: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>> ``` |

Modified Tcl_FSFileAttrStringsProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSFileAttrStringsProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<ConstUnsafePointer<Int8>>) ``` |
| To | ``` typealias Tcl_FSFileAttrStringsProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>) ``` |

Modified Tcl_FSFileAttrsGet(UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSFileAttrsGet(_ interp: UnsafePointer<Tcl_Interp>, _ index: Int32, _ pathPtr: UnsafePointer<Tcl_Obj>, _ objPtrRef: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_FSFileAttrsGet(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ index: Int32, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ objPtrRef: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_FSFileAttrsGetProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSFileAttrsGetProc = ((UnsafePointer<Tcl_Interp>, Int32, UnsafePointer<Tcl_Obj>, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32) ``` |
| To | ``` typealias Tcl_FSFileAttrsGetProc = ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32) ``` |

Modified Tcl_FSFileAttrsSet(UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSFileAttrsSet(_ interp: UnsafePointer<Tcl_Interp>, _ index: Int32, _ pathPtr: UnsafePointer<Tcl_Obj>, _ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSFileAttrsSet(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ index: Int32, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSFileAttrsSetProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSFileAttrsSetProc = ((UnsafePointer<Tcl_Interp>, Int32, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32) ``` |
| To | ``` typealias Tcl_FSFileAttrsSetProc = ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32) ``` |

Modified Tcl_FSFileSystemInfo(UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSFileSystemInfo(_ pathPtr: UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSFileSystemInfo(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSFilesystemPathTypeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSFilesystemPathTypeProc = ((UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj>) ``` |
| To | ``` typealias Tcl_FSFilesystemPathTypeProc = ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_FSFilesystemSeparatorProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSFilesystemSeparatorProc = ((UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj>) ``` |
| To | ``` typealias Tcl_FSFilesystemSeparatorProc = ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_FSGetCwd(UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSGetCwd(_ interp: UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSGetCwd(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSGetCwdProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSGetCwdProc = ((UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Obj>) ``` |
| To | ``` typealias Tcl_FSGetCwdProc = ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_FSGetFileSystemForPath(UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Filesystem>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSGetFileSystemForPath(_ pathPtr: UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Filesystem> ``` |
| To | ``` func Tcl_FSGetFileSystemForPath(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Filesystem> ``` |

Modified Tcl_FSGetInternalRep(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSGetInternalRep(_ pathPtr: UnsafePointer<Tcl_Obj>, _ fsPtr: UnsafePointer<Tcl_Filesystem>) -> ClientData ``` |
| To | ``` func Tcl_FSGetInternalRep(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ fsPtr: UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData ``` |

Modified Tcl_FSGetNativePath(UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSGetNativePath(_ pathPtr: UnsafePointer<Tcl_Obj>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_FSGetNativePath(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8> ``` |

Modified Tcl_FSGetNormalizedPath(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSGetNormalizedPath(_ interp: UnsafePointer<Tcl_Interp>, _ pathPtr: UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSGetNormalizedPath(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSGetPathType(UnsafeMutablePointer<Tcl_Obj>) -> Tcl_PathType

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSGetPathType(_ pathPtr: UnsafePointer<Tcl_Obj>) -> Tcl_PathType ``` |
| To | ``` func Tcl_FSGetPathType(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> Tcl_PathType ``` |

Modified Tcl_FSGetTranslatedPath(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSGetTranslatedPath(_ interp: UnsafePointer<Tcl_Interp>, _ pathPtr: UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSGetTranslatedPath(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSGetTranslatedStringPath(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSGetTranslatedStringPath(_ interp: UnsafePointer<Tcl_Interp>, _ pathPtr: UnsafePointer<Tcl_Obj>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_FSGetTranslatedStringPath(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8> ``` |

Modified Tcl_FSInternalToNormalizedProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSInternalToNormalizedProc = ((ClientData) -> UnsafePointer<Tcl_Obj>) ``` |
| To | ``` typealias Tcl_FSInternalToNormalizedProc = ((ClientData) -> UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_FSJoinPath(UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSJoinPath(_ listObj: UnsafePointer<Tcl_Obj>, _ elements: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSJoinPath(_ listObj: UnsafeMutablePointer<Tcl_Obj>, _ elements: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSJoinToPath(UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSJoinToPath(_ pathPtr: UnsafePointer<Tcl_Obj>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSJoinToPath(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSLink(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSLink(_ pathPtr: UnsafePointer<Tcl_Obj>, _ toPtr: UnsafePointer<Tcl_Obj>, _ linkAction: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSLink(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ toPtr: UnsafeMutablePointer<Tcl_Obj>, _ linkAction: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSLinkProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSLinkProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, Int32) -> UnsafePointer<Tcl_Obj>) ``` |
| To | ``` typealias Tcl_FSLinkProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_FSListVolumes() -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSListVolumes() -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSListVolumes() -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSListVolumesProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSListVolumesProc = (() -> UnsafePointer<Tcl_Obj>) ``` |
| To | ``` typealias Tcl_FSListVolumesProc = (() -> UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_FSLoadFile(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSLoadFile(_ interp: UnsafePointer<Tcl_Interp>, _ pathPtr: UnsafePointer<Tcl_Obj>, _ sym1: ConstUnsafePointer<Int8>, _ sym2: ConstUnsafePointer<Int8>, _ proc1Ptr: UnsafePointer<CFunctionPointer<Tcl_PackageInitProc>>, _ proc2Ptr: UnsafePointer<CFunctionPointer<Tcl_PackageInitProc>>, _ handlePtr: UnsafePointer<Tcl_LoadHandle>, _ unloadProcPtr: UnsafePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32 ``` |
| To | ``` func Tcl_FSLoadFile(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ sym1: UnsafePointer<Int8>, _ sym2: UnsafePointer<Int8>, _ proc1Ptr: UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, _ proc2Ptr: UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, _ handlePtr: UnsafeMutablePointer<Tcl_LoadHandle>, _ unloadProcPtr: UnsafeMutablePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32 ``` |

Modified Tcl_FSLoadFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSLoadFileProc = ((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_LoadHandle>, UnsafePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32) ``` |
| To | ``` typealias Tcl_FSLoadFileProc = ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32) ``` |

Modified Tcl_FSLstat(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSLstat(_ pathPtr: UnsafePointer<Tcl_Obj>, _ buf: UnsafePointer<Tcl_StatBuf>) -> Int32 ``` |
| To | ``` func Tcl_FSLstat(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ buf: UnsafeMutablePointer<Tcl_StatBuf>) -> Int32 ``` |

Modified Tcl_FSLstatProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSLstatProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_StatBuf>) -> Int32) ``` |
| To | ``` typealias Tcl_FSLstatProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32) ``` |

Modified Tcl_FSMatchInDirectory(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSMatchInDirectory(_ interp: UnsafePointer<Tcl_Interp>, _ result: UnsafePointer<Tcl_Obj>, _ pathPtr: UnsafePointer<Tcl_Obj>, _ pattern: ConstUnsafePointer<Int8>, _ types: UnsafePointer<Tcl_GlobTypeData>) -> Int32 ``` |
| To | ``` func Tcl_FSMatchInDirectory(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ result: UnsafeMutablePointer<Tcl_Obj>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ pattern: UnsafePointer<Int8>, _ types: UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32 ``` |

Modified Tcl_FSMatchInDirectoryProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSMatchInDirectoryProc = ((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>, ConstUnsafePointer<Int8>, UnsafePointer<Tcl_GlobTypeData>) -> Int32) ``` |
| To | ``` typealias Tcl_FSMatchInDirectoryProc = ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32) ``` |

Modified Tcl_FSMountsChanged(UnsafeMutablePointer<Tcl_Filesystem>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSMountsChanged(_ fsPtr: UnsafePointer<Tcl_Filesystem>) ``` |
| To | ``` func Tcl_FSMountsChanged(_ fsPtr: UnsafeMutablePointer<Tcl_Filesystem>) ``` |

Modified Tcl_FSNewNativePath(UnsafeMutablePointer<Tcl_Filesystem>, ClientData) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSNewNativePath(_ fromFilesystem: UnsafePointer<Tcl_Filesystem>, _ clientData: ClientData) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSNewNativePath(_ fromFilesystem: UnsafeMutablePointer<Tcl_Filesystem>, _ clientData: ClientData) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSNormalizePathProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSNormalizePathProc = ((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32) -> Int32) ``` |
| To | ``` typealias Tcl_FSNormalizePathProc = ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32) ``` |

Modified Tcl_FSOpenFileChannel(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSOpenFileChannel(_ interp: UnsafePointer<Tcl_Interp>, _ pathPtr: UnsafePointer<Tcl_Obj>, _ modeString: ConstUnsafePointer<Int8>, _ permissions: Int32) -> Tcl_Channel ``` |
| To | ``` func Tcl_FSOpenFileChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ modeString: UnsafePointer<Int8>, _ permissions: Int32) -> Tcl_Channel ``` |

Modified Tcl_FSOpenFileChannelProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSOpenFileChannelProc = ((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>, Int32, Int32) -> Tcl_Channel) ``` |
| To | ``` typealias Tcl_FSOpenFileChannelProc = ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Tcl_Channel) ``` |

Modified Tcl_FSPathInFilesystemProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSPathInFilesystemProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<ClientData>) -> Int32) ``` |
| To | ``` typealias Tcl_FSPathInFilesystemProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<ClientData>) -> Int32) ``` |

Modified Tcl_FSPathSeparator(UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSPathSeparator(_ pathPtr: UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSPathSeparator(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSRegister(ClientData, UnsafeMutablePointer<Tcl_Filesystem>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSRegister(_ clientData: ClientData, _ fsPtr: UnsafePointer<Tcl_Filesystem>) -> Int32 ``` |
| To | ``` func Tcl_FSRegister(_ clientData: ClientData, _ fsPtr: UnsafeMutablePointer<Tcl_Filesystem>) -> Int32 ``` |

Modified Tcl_FSRemoveDirectory(UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSRemoveDirectory(_ pathPtr: UnsafePointer<Tcl_Obj>, _ recursive: Int32, _ errorPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_FSRemoveDirectory(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ recursive: Int32, _ errorPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_FSRemoveDirectoryProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSRemoveDirectoryProc = ((UnsafePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32) ``` |
| To | ``` typealias Tcl_FSRemoveDirectoryProc = ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32) ``` |

Modified Tcl_FSRenameFile(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSRenameFile(_ srcPathPtr: UnsafePointer<Tcl_Obj>, _ destPathPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_FSRenameFile(_ srcPathPtr: UnsafeMutablePointer<Tcl_Obj>, _ destPathPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_FSRenameFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSRenameFileProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_Obj>) -> Int32) ``` |
| To | ``` typealias Tcl_FSRenameFileProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32) ``` |

Modified Tcl_FSSplitPath(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSSplitPath(_ pathPtr: UnsafePointer<Tcl_Obj>, _ lenPtr: UnsafePointer<Int32>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_FSSplitPath(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ lenPtr: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_FSStat(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSStat(_ pathPtr: UnsafePointer<Tcl_Obj>, _ buf: UnsafePointer<Tcl_StatBuf>) -> Int32 ``` |
| To | ``` func Tcl_FSStat(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ buf: UnsafeMutablePointer<Tcl_StatBuf>) -> Int32 ``` |

Modified Tcl_FSStatProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSStatProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<Tcl_StatBuf>) -> Int32) ``` |
| To | ``` typealias Tcl_FSStatProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32) ``` |

Modified Tcl_FSUnregister(UnsafeMutablePointer<Tcl_Filesystem>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSUnregister(_ fsPtr: UnsafePointer<Tcl_Filesystem>) -> Int32 ``` |
| To | ``` func Tcl_FSUnregister(_ fsPtr: UnsafeMutablePointer<Tcl_Filesystem>) -> Int32 ``` |

Modified Tcl_FSUtime(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSUtime(_ pathPtr: UnsafePointer<Tcl_Obj>, _ tval: UnsafePointer<utimbuf>) -> Int32 ``` |
| To | ``` func Tcl_FSUtime(_ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ tval: UnsafeMutablePointer<utimbuf>) -> Int32 ``` |

Modified Tcl_FSUtimeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSUtimeProc = ((UnsafePointer<Tcl_Obj>, UnsafePointer<utimbuf>) -> Int32) ``` |
| To | ``` typealias Tcl_FSUtimeProc = ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32) ``` |

Modified Tcl_FindCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FindCommand(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ contextNsPtr: UnsafePointer<Tcl_Namespace>, _ flags: Int32) -> Tcl_Command ``` |
| To | ``` func Tcl_FindCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ contextNsPtr: UnsafeMutablePointer<Tcl_Namespace>, _ flags: Int32) -> Tcl_Command ``` |

Modified Tcl_FindEnsemble(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_Command

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FindEnsemble(_ interp: UnsafePointer<Tcl_Interp>, _ cmdNameObj: UnsafePointer<Tcl_Obj>, _ flags: Int32) -> Tcl_Command ``` |
| To | ``` func Tcl_FindEnsemble(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdNameObj: UnsafeMutablePointer<Tcl_Obj>, _ flags: Int32) -> Tcl_Command ``` |

Modified Tcl_FindExecutable(UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FindExecutable(_ argv0: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_FindExecutable(_ argv0: UnsafePointer<Int8>) ``` |

Modified Tcl_FindHashEntry(UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FindHashEntry(_ tablePtr: UnsafePointer<Tcl_HashTable>, _ key: ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_HashEntry> ``` |
| To | ``` func Tcl_FindHashEntry(_ tablePtr: UnsafeMutablePointer<Tcl_HashTable>, _ key: UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry> ``` |

Modified Tcl_FindNamespace(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> UnsafeMutablePointer<Tcl_Namespace>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FindNamespace(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ contextNsPtr: UnsafePointer<Tcl_Namespace>, _ flags: Int32) -> UnsafePointer<Tcl_Namespace> ``` |
| To | ``` func Tcl_FindNamespace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ contextNsPtr: UnsafeMutablePointer<Tcl_Namespace>, _ flags: Int32) -> UnsafeMutablePointer<Tcl_Namespace> ``` |

Modified Tcl_FirstHashEntry(UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FirstHashEntry(_ tablePtr: UnsafePointer<Tcl_HashTable>, _ searchPtr: UnsafePointer<Tcl_HashSearch>) -> UnsafePointer<Tcl_HashEntry> ``` |
| To | ``` func Tcl_FirstHashEntry(_ tablePtr: UnsafeMutablePointer<Tcl_HashTable>, _ searchPtr: UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry> ``` |

Modified Tcl_ForgetImport(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ForgetImport(_ interp: UnsafePointer<Tcl_Interp>, _ nsPtr: UnsafePointer<Tcl_Namespace>, _ pattern: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_ForgetImport(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ nsPtr: UnsafeMutablePointer<Tcl_Namespace>, _ pattern: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_Format(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Format(_ interp: UnsafePointer<Tcl_Interp>, _ format: ConstUnsafePointer<Int8>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_Format(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ format: UnsafePointer<Int8>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_Free(UnsafeMutablePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Free(_ ptr: UnsafePointer<Int8>) ``` |
| To | ``` func Tcl_Free(_ ptr: UnsafeMutablePointer<Int8>) ``` |

Modified Tcl_FreeHashEntryProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FreeHashEntryProc = ((UnsafePointer<Tcl_HashEntry>) -> Void) ``` |
| To | ``` typealias Tcl_FreeHashEntryProc = ((UnsafeMutablePointer<Tcl_HashEntry>) -> Void) ``` |

Modified Tcl_FreeInternalRepProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FreeInternalRepProc = ((UnsafePointer<Tcl_Obj>) -> Void) ``` |
| To | ``` typealias Tcl_FreeInternalRepProc = ((UnsafeMutablePointer<Tcl_Obj>) -> Void) ``` |

Modified Tcl_FreeParse(UnsafeMutablePointer<Tcl_Parse>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FreeParse(_ parsePtr: UnsafePointer<Tcl_Parse>) ``` |
| To | ``` func Tcl_FreeParse(_ parsePtr: UnsafeMutablePointer<Tcl_Parse>) ``` |

Modified Tcl_FreeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FreeProc = ((UnsafePointer<Int8>) -> Void) ``` |
| To | ``` typealias Tcl_FreeProc = ((UnsafeMutablePointer<Int8>) -> Void) ``` |

Modified Tcl_FreeResult(UnsafeMutablePointer<Tcl_Interp>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FreeResult(_ interp: UnsafePointer<Tcl_Interp>) ``` |
| To | ``` func Tcl_FreeResult(_ interp: UnsafeMutablePointer<Tcl_Interp>) ``` |

Modified Tcl_GetAlias(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetAlias(_ interp: UnsafePointer<Tcl_Interp>, _ slaveCmd: ConstUnsafePointer<Int8>, _ targetInterpPtr: UnsafePointer<UnsafePointer<Tcl_Interp>>, _ targetCmdPtr: UnsafePointer<ConstUnsafePointer<Int8>>, _ argcPtr: UnsafePointer<Int32>, _ argvPtr: UnsafePointer<UnsafePointer<ConstUnsafePointer<Int8>>>) -> Int32 ``` |
| To | ``` func Tcl_GetAlias(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ slaveCmd: UnsafePointer<Int8>, _ targetInterpPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, _ targetCmdPtr: UnsafeMutablePointer<UnsafePointer<Int8>>, _ argcPtr: UnsafeMutablePointer<Int32>, _ argvPtr: UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32 ``` |

Modified Tcl_GetAliasObj(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetAliasObj(_ interp: UnsafePointer<Tcl_Interp>, _ slaveCmd: ConstUnsafePointer<Int8>, _ targetInterpPtr: UnsafePointer<UnsafePointer<Tcl_Interp>>, _ targetCmdPtr: UnsafePointer<ConstUnsafePointer<Int8>>, _ objcPtr: UnsafePointer<Int32>, _ objv: UnsafePointer<UnsafePointer<UnsafePointer<Tcl_Obj>>>) -> Int32 ``` |
| To | ``` func Tcl_GetAliasObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ slaveCmd: UnsafePointer<Int8>, _ targetInterpPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, _ targetCmdPtr: UnsafeMutablePointer<UnsafePointer<Int8>>, _ objcPtr: UnsafeMutablePointer<Int32>, _ objv: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32 ``` |

Modified Tcl_GetAllocMutex() -> UnsafeMutablePointer<Tcl_Mutex>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetAllocMutex() -> UnsafePointer<Tcl_Mutex> ``` |
| To | ``` func Tcl_GetAllocMutex() -> UnsafeMutablePointer<Tcl_Mutex> ``` |

Modified Tcl_GetAssocData(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<CFunctionPointer<Tcl_InterpDeleteProc>>) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetAssocData(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ procPtr: UnsafePointer<CFunctionPointer<Tcl_InterpDeleteProc>>) -> ClientData ``` |
| To | ``` func Tcl_GetAssocData(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ procPtr: UnsafeMutablePointer<CFunctionPointer<Tcl_InterpDeleteProc>>) -> ClientData ``` |

Modified Tcl_GetBignumFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetBignumFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ obj: UnsafePointer<Tcl_Obj>, _ value: UnsafePointer<mp_int>) -> Int32 ``` |
| To | ``` func Tcl_GetBignumFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ obj: UnsafeMutablePointer<Tcl_Obj>, _ value: UnsafeMutablePointer<mp_int>) -> Int32 ``` |

Modified Tcl_GetBoolean(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetBoolean(_ interp: UnsafePointer<Tcl_Interp>, _ src: ConstUnsafePointer<Int8>, _ boolPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_GetBoolean(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ src: UnsafePointer<Int8>, _ boolPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_GetBooleanFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetBooleanFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ boolPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_GetBooleanFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ boolPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_GetByteArrayFromObj(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<UInt8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetByteArrayFromObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ lengthPtr: UnsafePointer<Int32>) -> UnsafePointer<UInt8> ``` |
| To | ``` func Tcl_GetByteArrayFromObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ lengthPtr: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<UInt8> ``` |

Modified Tcl_GetChannel(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannel(_ interp: UnsafePointer<Tcl_Interp>, _ chanName: ConstUnsafePointer<Int8>, _ modePtr: UnsafePointer<Int32>) -> Tcl_Channel ``` |
| To | ``` func Tcl_GetChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ chanName: UnsafePointer<Int8>, _ modePtr: UnsafeMutablePointer<Int32>) -> Tcl_Channel ``` |

Modified Tcl_GetChannelError(Tcl_Channel, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannelError(_ chan: Tcl_Channel, _ msg: UnsafePointer<UnsafePointer<Tcl_Obj>>) ``` |
| To | ``` func Tcl_GetChannelError(_ chan: Tcl_Channel, _ msg: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) ``` |

Modified Tcl_GetChannelErrorInterp(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannelErrorInterp(_ interp: UnsafePointer<Tcl_Interp>, _ msg: UnsafePointer<UnsafePointer<Tcl_Obj>>) ``` |
| To | ``` func Tcl_GetChannelErrorInterp(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ msg: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) ``` |

Modified Tcl_GetChannelHandle(Tcl_Channel, Int32, UnsafeMutablePointer<ClientData>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannelHandle(_ chan: Tcl_Channel, _ direction: Int32, _ handlePtr: UnsafePointer<ClientData>) -> Int32 ``` |
| To | ``` func Tcl_GetChannelHandle(_ chan: Tcl_Channel, _ direction: Int32, _ handlePtr: UnsafeMutablePointer<ClientData>) -> Int32 ``` |

Modified Tcl_GetChannelName(Tcl_Channel) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannelName(_ chan: Tcl_Channel) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetChannelName(_ chan: Tcl_Channel) -> UnsafePointer<Int8> ``` |

Modified Tcl_GetChannelNames(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannelNames(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_GetChannelNames(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_GetChannelNamesEx(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannelNamesEx(_ interp: UnsafePointer<Tcl_Interp>, _ pattern: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_GetChannelNamesEx(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pattern: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_GetChannelOption(UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannelOption(_ interp: UnsafePointer<Tcl_Interp>, _ chan: Tcl_Channel, _ optionName: ConstUnsafePointer<Int8>, _ dsPtr: UnsafePointer<Tcl_DString>) -> Int32 ``` |
| To | ``` func Tcl_GetChannelOption(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ chan: Tcl_Channel, _ optionName: UnsafePointer<Int8>, _ dsPtr: UnsafeMutablePointer<Tcl_DString>) -> Int32 ``` |

Modified Tcl_GetChannelType(Tcl_Channel) -> UnsafeMutablePointer<Tcl_ChannelType>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetChannelType(_ chan: Tcl_Channel) -> UnsafePointer<Tcl_ChannelType> ``` |
| To | ``` func Tcl_GetChannelType(_ chan: Tcl_Channel) -> UnsafeMutablePointer<Tcl_ChannelType> ``` |

Modified Tcl_GetCharLength(UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetCharLength(_ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_GetCharLength(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_GetCommandFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Tcl_Command

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetCommandFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>) -> Tcl_Command ``` |
| To | ``` func Tcl_GetCommandFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Tcl_Command ``` |

Modified Tcl_GetCommandFullName(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetCommandFullName(_ interp: UnsafePointer<Tcl_Interp>, _ command: Tcl_Command, _ objPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_GetCommandFullName(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ command: Tcl_Command, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_GetCommandInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetCommandInfo(_ interp: UnsafePointer<Tcl_Interp>, _ cmdName: ConstUnsafePointer<Int8>, _ infoPtr: UnsafePointer<Tcl_CmdInfo>) -> Int32 ``` |
| To | ``` func Tcl_GetCommandInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ infoPtr: UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32 ``` |

Modified Tcl_GetCommandInfoFromToken(Tcl_Command, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetCommandInfoFromToken(_ token: Tcl_Command, _ infoPtr: UnsafePointer<Tcl_CmdInfo>) -> Int32 ``` |
| To | ``` func Tcl_GetCommandInfoFromToken(_ token: Tcl_Command, _ infoPtr: UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32 ``` |

Modified Tcl_GetCommandName(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetCommandName(_ interp: UnsafePointer<Tcl_Interp>, _ command: Tcl_Command) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetCommandName(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ command: Tcl_Command) -> UnsafePointer<Int8> ``` |

Modified Tcl_GetCurrentNamespace(UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetCurrentNamespace(_ interp: UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Namespace> ``` |
| To | ``` func Tcl_GetCurrentNamespace(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace> ``` |

Modified Tcl_GetCwd(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetCwd(_ interp: UnsafePointer<Tcl_Interp>, _ cwdPtr: UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetCwd(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cwdPtr: UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_GetDefaultEncodingDir() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetDefaultEncodingDir() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetDefaultEncodingDir() -> UnsafePointer<Int8> ``` |

Modified Tcl_GetDouble(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetDouble(_ interp: UnsafePointer<Tcl_Interp>, _ src: ConstUnsafePointer<Int8>, _ doublePtr: UnsafePointer<Double>) -> Int32 ``` |
| To | ``` func Tcl_GetDouble(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ src: UnsafePointer<Int8>, _ doublePtr: UnsafeMutablePointer<Double>) -> Int32 ``` |

Modified Tcl_GetDoubleFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetDoubleFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ doublePtr: UnsafePointer<Double>) -> Int32 ``` |
| To | ``` func Tcl_GetDoubleFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ doublePtr: UnsafeMutablePointer<Double>) -> Int32 ``` |

Modified Tcl_GetEncoding(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_Encoding

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEncoding(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>) -> Tcl_Encoding ``` |
| To | ``` func Tcl_GetEncoding(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>) -> Tcl_Encoding ``` |

Modified Tcl_GetEncodingFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Encoding>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEncodingFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ encodingPtr: UnsafePointer<Tcl_Encoding>) -> Int32 ``` |
| To | ``` func Tcl_GetEncodingFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ encodingPtr: UnsafeMutablePointer<Tcl_Encoding>) -> Int32 ``` |

Modified Tcl_GetEncodingName(Tcl_Encoding) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEncodingName(_ encoding: Tcl_Encoding) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetEncodingName(_ encoding: Tcl_Encoding) -> UnsafePointer<Int8> ``` |

Modified Tcl_GetEncodingNameFromEnvironment(UnsafeMutablePointer<Tcl_DString>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEncodingNameFromEnvironment(_ bufPtr: UnsafePointer<Tcl_DString>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetEncodingNameFromEnvironment(_ bufPtr: UnsafeMutablePointer<Tcl_DString>) -> UnsafePointer<Int8> ``` |

Modified Tcl_GetEncodingNames(UnsafeMutablePointer<Tcl_Interp>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEncodingNames(_ interp: UnsafePointer<Tcl_Interp>) ``` |
| To | ``` func Tcl_GetEncodingNames(_ interp: UnsafeMutablePointer<Tcl_Interp>) ``` |

Modified Tcl_GetEncodingSearchPath() -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEncodingSearchPath() -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_GetEncodingSearchPath() -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_GetEnsembleFlags(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEnsembleFlags(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ flagsPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_GetEnsembleFlags(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ flagsPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_GetEnsembleMappingDict(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEnsembleMappingDict(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ mapDictPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_GetEnsembleMappingDict(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ mapDictPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_GetEnsembleNamespace(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Namespace>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEnsembleNamespace(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ namespacePtrPtr: UnsafePointer<UnsafePointer<Tcl_Namespace>>) -> Int32 ``` |
| To | ``` func Tcl_GetEnsembleNamespace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ namespacePtrPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Namespace>>) -> Int32 ``` |

Modified Tcl_GetEnsembleSubcommandList(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEnsembleSubcommandList(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ subcmdListPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_GetEnsembleSubcommandList(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ subcmdListPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_GetEnsembleUnknownHandler(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetEnsembleUnknownHandler(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ unknownListPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_GetEnsembleUnknownHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ unknownListPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_GetGlobalNamespace(UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetGlobalNamespace(_ interp: UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Namespace> ``` |
| To | ``` func Tcl_GetGlobalNamespace(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace> ``` |

Modified Tcl_GetHostName() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetHostName() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetHostName() -> UnsafePointer<Int8> ``` |

Modified Tcl_GetIndexFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetIndexFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ tablePtr: UnsafePointer<ConstUnsafePointer<Int8>>, _ msg: ConstUnsafePointer<Int8>, _ flags: Int32, _ indexPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_GetIndexFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ tablePtr: UnsafeMutablePointer<UnsafePointer<Int8>>, _ msg: UnsafePointer<Int8>, _ flags: Int32, _ indexPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_GetIndexFromObjStruct(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Void>, Int32, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetIndexFromObjStruct(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ tablePtr: ConstUnsafePointer<()>, _ offset: Int32, _ msg: ConstUnsafePointer<Int8>, _ flags: Int32, _ indexPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_GetIndexFromObjStruct(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ tablePtr: UnsafePointer<Void>, _ offset: Int32, _ msg: UnsafePointer<Int8>, _ flags: Int32, _ indexPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_GetInt(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetInt(_ interp: UnsafePointer<Tcl_Interp>, _ src: ConstUnsafePointer<Int8>, _ intPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_GetInt(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ src: UnsafePointer<Int8>, _ intPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_GetIntFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetIntFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ intPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_GetIntFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ intPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_GetInterpPath(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetInterpPath(_ askInterp: UnsafePointer<Tcl_Interp>, _ slaveInterp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_GetInterpPath(_ askInterp: UnsafeMutablePointer<Tcl_Interp>, _ slaveInterp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_GetLongFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetLongFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ longPtr: UnsafePointer<Int>) -> Int32 ``` |
| To | ``` func Tcl_GetLongFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ longPtr: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified Tcl_GetMaster(UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Interp>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetMaster(_ interp: UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Interp> ``` |
| To | ``` func Tcl_GetMaster(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Interp> ``` |

Modified Tcl_GetMathFuncInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, UnsafeMutablePointer<CFunctionPointer<Tcl_MathProc>>, UnsafeMutablePointer<ClientData>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetMathFuncInfo(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ numArgsPtr: UnsafePointer<Int32>, _ argTypesPtr: UnsafePointer<UnsafePointer<Tcl_ValueType>>, _ procPtr: UnsafePointer<CFunctionPointer<Tcl_MathProc>>, _ clientDataPtr: UnsafePointer<ClientData>) -> Int32 ``` |
| To | ``` func Tcl_GetMathFuncInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ numArgsPtr: UnsafeMutablePointer<Int32>, _ argTypesPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, _ procPtr: UnsafeMutablePointer<CFunctionPointer<Tcl_MathProc>>, _ clientDataPtr: UnsafeMutablePointer<ClientData>) -> Int32 ``` |

Modified Tcl_GetNameOfExecutable() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetNameOfExecutable() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetNameOfExecutable() -> UnsafePointer<Int8> ``` |

Modified Tcl_GetNamespaceUnknownHandler(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetNamespaceUnknownHandler(_ interp: UnsafePointer<Tcl_Interp>, _ nsPtr: UnsafePointer<Tcl_Namespace>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_GetNamespaceUnknownHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ nsPtr: UnsafeMutablePointer<Tcl_Namespace>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_GetObjResult(UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetObjResult(_ interp: UnsafePointer<Tcl_Interp>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_GetObjResult(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_GetObjType(UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_ObjType>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetObjType(_ typeName: ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_ObjType> ``` |
| To | ``` func Tcl_GetObjType(_ typeName: UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_ObjType> ``` |

Modified Tcl_GetOpenFile(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<ClientData>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetOpenFile(_ interp: UnsafePointer<Tcl_Interp>, _ chanID: ConstUnsafePointer<Int8>, _ forWriting: Int32, _ checkUsage: Int32, _ filePtr: UnsafePointer<ClientData>) -> Int32 ``` |
| To | ``` func Tcl_GetOpenFile(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ chanID: UnsafePointer<Int8>, _ forWriting: Int32, _ checkUsage: Int32, _ filePtr: UnsafeMutablePointer<ClientData>) -> Int32 ``` |

Modified Tcl_GetPathType(UnsafePointer<Int8>) -> Tcl_PathType

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetPathType(_ path: ConstUnsafePointer<Int8>) -> Tcl_PathType ``` |
| To | ``` func Tcl_GetPathType(_ path: UnsafePointer<Int8>) -> Tcl_PathType ``` |

Modified Tcl_GetRange(UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetRange(_ objPtr: UnsafePointer<Tcl_Obj>, _ first: Int32, _ last: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_GetRange(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ first: Int32, _ last: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_GetRegExpFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_RegExp

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetRegExpFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ patObj: UnsafePointer<Tcl_Obj>, _ flags: Int32) -> Tcl_RegExp ``` |
| To | ``` func Tcl_GetRegExpFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ patObj: UnsafeMutablePointer<Tcl_Obj>, _ flags: Int32) -> Tcl_RegExp ``` |

Modified Tcl_GetReturnOptions(UnsafeMutablePointer<Tcl_Interp>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetReturnOptions(_ interp: UnsafePointer<Tcl_Interp>, _ result: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_GetReturnOptions(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ result: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_GetSlave(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Interp>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetSlave(_ interp: UnsafePointer<Tcl_Interp>, _ slaveName: ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_Interp> ``` |
| To | ``` func Tcl_GetSlave(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ slaveName: UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Interp> ``` |

Modified Tcl_GetString(UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetString(_ objPtr: UnsafePointer<Tcl_Obj>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetString(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_GetStringFromObj(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetStringFromObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ lengthPtr: UnsafePointer<Int32>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetStringFromObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ lengthPtr: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_GetStringResult(UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetStringResult(_ interp: UnsafePointer<Tcl_Interp>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetStringResult(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8> ``` |

Modified Tcl_GetThreadData(UnsafeMutablePointer<Tcl_ThreadDataKey>, Int32) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetThreadData(_ keyPtr: UnsafePointer<Tcl_ThreadDataKey>, _ size: Int32) -> UnsafePointer<()> ``` |
| To | ``` func Tcl_GetThreadData(_ keyPtr: UnsafeMutablePointer<Tcl_ThreadDataKey>, _ size: Int32) -> UnsafeMutablePointer<Void> ``` |

Modified Tcl_GetTime(UnsafeMutablePointer<Tcl_Time>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetTime(_ timeBuf: UnsafePointer<Tcl_Time>) ``` |
| To | ``` func Tcl_GetTime(_ timeBuf: UnsafeMutablePointer<Tcl_Time>) ``` |

Modified Tcl_GetTimeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_GetTimeProc = ((UnsafePointer<Tcl_Time>, ClientData) -> Void) ``` |
| To | ``` typealias Tcl_GetTimeProc = ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void) ``` |

Modified Tcl_GetUniChar(UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_UniChar

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetUniChar(_ objPtr: UnsafePointer<Tcl_Obj>, _ index: Int32) -> Tcl_UniChar ``` |
| To | ``` func Tcl_GetUniChar(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ index: Int32) -> Tcl_UniChar ``` |

Modified Tcl_GetUnicode(UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_UniChar>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetUnicode(_ objPtr: UnsafePointer<Tcl_Obj>) -> UnsafePointer<Tcl_UniChar> ``` |
| To | ``` func Tcl_GetUnicode(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_UniChar> ``` |

Modified Tcl_GetUnicodeFromObj(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_UniChar>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetUnicodeFromObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ lengthPtr: UnsafePointer<Int32>) -> UnsafePointer<Tcl_UniChar> ``` |
| To | ``` func Tcl_GetUnicodeFromObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ lengthPtr: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_UniChar> ``` |

Modified Tcl_GetVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetVar(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ flags: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_GetVar2(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetVar2(_ interp: UnsafePointer<Tcl_Interp>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ flags: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_GetVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_GetVar2Ex(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetVar2Ex(_ interp: UnsafePointer<Tcl_Interp>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ flags: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_GetVar2Ex(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_GetVersion(UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetVersion(_ major: UnsafePointer<Int32>, _ minor: UnsafePointer<Int32>, _ patchLevel: UnsafePointer<Int32>, _ type: UnsafePointer<Int32>) ``` |
| To | ``` func Tcl_GetVersion(_ major: UnsafeMutablePointer<Int32>, _ minor: UnsafeMutablePointer<Int32>, _ patchLevel: UnsafeMutablePointer<Int32>, _ type: UnsafeMutablePointer<Int32>) ``` |

Modified Tcl_GetWideIntFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_WideInt>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetWideIntFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ widePtr: UnsafePointer<Tcl_WideInt>) -> Int32 ``` |
| To | ``` func Tcl_GetWideIntFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ widePtr: UnsafeMutablePointer<Tcl_WideInt>) -> Int32 ``` |

Modified Tcl_Gets(Tcl_Channel, UnsafeMutablePointer<Tcl_DString>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Gets(_ chan: Tcl_Channel, _ dsPtr: UnsafePointer<Tcl_DString>) -> Int32 ``` |
| To | ``` func Tcl_Gets(_ chan: Tcl_Channel, _ dsPtr: UnsafeMutablePointer<Tcl_DString>) -> Int32 ``` |

Modified Tcl_GetsObj(Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetsObj(_ chan: Tcl_Channel, _ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_GetsObj(_ chan: Tcl_Channel, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_GlobalEval(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GlobalEval(_ interp: UnsafePointer<Tcl_Interp>, _ command: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_GlobalEval(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ command: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_GlobalEvalObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GlobalEvalObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_GlobalEvalObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_HashKeyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_HashKeyProc = ((UnsafePointer<Tcl_HashTable>, UnsafePointer<()>) -> UInt32) ``` |
| To | ``` typealias Tcl_HashKeyProc = ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UInt32) ``` |

Modified Tcl_HashStats(UnsafeMutablePointer<Tcl_HashTable>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_HashStats(_ tablePtr: UnsafePointer<Tcl_HashTable>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_HashStats(_ tablePtr: UnsafeMutablePointer<Tcl_HashTable>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_HideCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_HideCommand(_ interp: UnsafePointer<Tcl_Interp>, _ cmdName: ConstUnsafePointer<Int8>, _ hiddenCmdToken: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_HideCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ hiddenCmdToken: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_Import(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Import(_ interp: UnsafePointer<Tcl_Interp>, _ nsPtr: UnsafePointer<Tcl_Namespace>, _ pattern: ConstUnsafePointer<Int8>, _ allowOverwrite: Int32) -> Int32 ``` |
| To | ``` func Tcl_Import(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ nsPtr: UnsafeMutablePointer<Tcl_Namespace>, _ pattern: UnsafePointer<Int8>, _ allowOverwrite: Int32) -> Int32 ``` |

Modified Tcl_IncrRefCount(UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_IncrRefCount(_ objPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_IncrRefCount(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_Init(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Init(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_Init(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_InitBignumFromDouble(UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<mp_int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_InitBignumFromDouble(_ interp: UnsafePointer<Tcl_Interp>, _ initval: Double, _ toInit: UnsafePointer<mp_int>) -> Int32 ``` |
| To | ``` func Tcl_InitBignumFromDouble(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ initval: Double, _ toInit: UnsafeMutablePointer<mp_int>) -> Int32 ``` |

Modified Tcl_InitCustomHashTable(UnsafeMutablePointer<Tcl_HashTable>, Int32, UnsafeMutablePointer<Tcl_HashKeyType>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_InitCustomHashTable(_ tablePtr: UnsafePointer<Tcl_HashTable>, _ keyType: Int32, _ typePtr: UnsafePointer<Tcl_HashKeyType>) ``` |
| To | ``` func Tcl_InitCustomHashTable(_ tablePtr: UnsafeMutablePointer<Tcl_HashTable>, _ keyType: Int32, _ typePtr: UnsafeMutablePointer<Tcl_HashKeyType>) ``` |

Modified Tcl_InitHashTable(UnsafeMutablePointer<Tcl_HashTable>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_InitHashTable(_ tablePtr: UnsafePointer<Tcl_HashTable>, _ keyType: Int32) ``` |
| To | ``` func Tcl_InitHashTable(_ tablePtr: UnsafeMutablePointer<Tcl_HashTable>, _ keyType: Int32) ``` |

Modified Tcl_InitMemory(UnsafeMutablePointer<Tcl_Interp>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_InitMemory(_ interp: UnsafePointer<Tcl_Interp>) ``` |
| To | ``` func Tcl_InitMemory(_ interp: UnsafeMutablePointer<Tcl_Interp>) ``` |

Modified Tcl_InitObjHashTable(UnsafeMutablePointer<Tcl_HashTable>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_InitObjHashTable(_ tablePtr: UnsafePointer<Tcl_HashTable>) ``` |
| To | ``` func Tcl_InitObjHashTable(_ tablePtr: UnsafeMutablePointer<Tcl_HashTable>) ``` |

Modified Tcl_InitStubs(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_InitStubs(_ interp: UnsafePointer<Tcl_Interp>, _ version: ConstUnsafePointer<Int8>, _ exact: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_InitStubs(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ version: UnsafePointer<Int8>, _ exact: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_InterpDeleteProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_InterpDeleteProc = ((ClientData, UnsafePointer<Tcl_Interp>) -> Void) ``` |
| To | ``` typealias Tcl_InterpDeleteProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void) ``` |

Modified Tcl_InterpDeleted(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_InterpDeleted(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_InterpDeleted(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_InvalidateStringRep(UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_InvalidateStringRep(_ objPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_InvalidateStringRep(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_IsChannelExisting(UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_IsChannelExisting(_ channelName: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_IsChannelExisting(_ channelName: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_IsChannelRegistered(UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_IsChannelRegistered(_ interp: UnsafePointer<Tcl_Interp>, _ channel: Tcl_Channel) -> Int32 ``` |
| To | ``` func Tcl_IsChannelRegistered(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ channel: Tcl_Channel) -> Int32 ``` |

Modified Tcl_IsSafe(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_IsSafe(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_IsSafe(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_IsShared(UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_IsShared(_ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_IsShared(_ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_JoinPath(Int32, UnsafePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_JoinPath(_ argc: Int32, _ argv: ConstUnsafePointer<ConstUnsafePointer<Int8>>, _ resultPtr: UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_JoinPath(_ argc: Int32, _ argv: UnsafePointer<UnsafePointer<Int8>>, _ resultPtr: UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_JoinThread(Tcl_ThreadId, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_JoinThread(_ threadId: Tcl_ThreadId, _ result: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_JoinThread(_ threadId: Tcl_ThreadId, _ result: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_LimitAddHandler(UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_LimitHandlerProc>, ClientData, CFunctionPointer<Tcl_LimitHandlerDeleteProc>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitAddHandler(_ interp: UnsafePointer<Tcl_Interp>, _ type: Int32, _ handlerProc: CFunctionPointer<Tcl_LimitHandlerProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_LimitHandlerDeleteProc>) ``` |
| To | ``` func Tcl_LimitAddHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32, _ handlerProc: CFunctionPointer<Tcl_LimitHandlerProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_LimitHandlerDeleteProc>) ``` |

Modified Tcl_LimitCheck(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitCheck(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_LimitCheck(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_LimitExceeded(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitExceeded(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_LimitExceeded(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_LimitGetCommands(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitGetCommands(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_LimitGetCommands(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_LimitGetGranularity(UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitGetGranularity(_ interp: UnsafePointer<Tcl_Interp>, _ type: Int32) -> Int32 ``` |
| To | ``` func Tcl_LimitGetGranularity(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32) -> Int32 ``` |

Modified Tcl_LimitGetTime(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitGetTime(_ interp: UnsafePointer<Tcl_Interp>, _ timeLimitPtr: UnsafePointer<Tcl_Time>) ``` |
| To | ``` func Tcl_LimitGetTime(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ timeLimitPtr: UnsafeMutablePointer<Tcl_Time>) ``` |

Modified Tcl_LimitHandlerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_LimitHandlerProc = ((ClientData, UnsafePointer<Tcl_Interp>) -> Void) ``` |
| To | ``` typealias Tcl_LimitHandlerProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void) ``` |

Modified Tcl_LimitReady(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitReady(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_LimitReady(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_LimitRemoveHandler(UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_LimitHandlerProc>, ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitRemoveHandler(_ interp: UnsafePointer<Tcl_Interp>, _ type: Int32, _ handlerProc: CFunctionPointer<Tcl_LimitHandlerProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_LimitRemoveHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32, _ handlerProc: CFunctionPointer<Tcl_LimitHandlerProc>, _ clientData: ClientData) ``` |

Modified Tcl_LimitSetCommands(UnsafeMutablePointer<Tcl_Interp>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitSetCommands(_ interp: UnsafePointer<Tcl_Interp>, _ commandLimit: Int32) ``` |
| To | ``` func Tcl_LimitSetCommands(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ commandLimit: Int32) ``` |

Modified Tcl_LimitSetGranularity(UnsafeMutablePointer<Tcl_Interp>, Int32, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitSetGranularity(_ interp: UnsafePointer<Tcl_Interp>, _ type: Int32, _ granularity: Int32) ``` |
| To | ``` func Tcl_LimitSetGranularity(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32, _ granularity: Int32) ``` |

Modified Tcl_LimitSetTime(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitSetTime(_ interp: UnsafePointer<Tcl_Interp>, _ timeLimitPtr: UnsafePointer<Tcl_Time>) ``` |
| To | ``` func Tcl_LimitSetTime(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ timeLimitPtr: UnsafeMutablePointer<Tcl_Time>) ``` |

Modified Tcl_LimitTypeEnabled(UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitTypeEnabled(_ interp: UnsafePointer<Tcl_Interp>, _ type: Int32) -> Int32 ``` |
| To | ``` func Tcl_LimitTypeEnabled(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32) -> Int32 ``` |

Modified Tcl_LimitTypeExceeded(UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitTypeExceeded(_ interp: UnsafePointer<Tcl_Interp>, _ type: Int32) -> Int32 ``` |
| To | ``` func Tcl_LimitTypeExceeded(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32) -> Int32 ``` |

Modified Tcl_LimitTypeReset(UnsafeMutablePointer<Tcl_Interp>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitTypeReset(_ interp: UnsafePointer<Tcl_Interp>, _ type: Int32) ``` |
| To | ``` func Tcl_LimitTypeReset(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32) ``` |

Modified Tcl_LimitTypeSet(UnsafeMutablePointer<Tcl_Interp>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitTypeSet(_ interp: UnsafePointer<Tcl_Interp>, _ type: Int32) ``` |
| To | ``` func Tcl_LimitTypeSet(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32) ``` |

Modified Tcl_LinkVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LinkVar(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ addr: UnsafePointer<Int8>, _ type: Int32) -> Int32 ``` |
| To | ``` func Tcl_LinkVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ addr: UnsafeMutablePointer<Int8>, _ type: Int32) -> Int32 ``` |

Modified Tcl_ListMathFuncs(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ListMathFuncs(_ interp: UnsafePointer<Tcl_Interp>, _ pattern: ConstUnsafePointer<Int8>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_ListMathFuncs(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pattern: UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_ListObjAppendElement(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ListObjAppendElement(_ interp: UnsafePointer<Tcl_Interp>, _ listPtr: UnsafePointer<Tcl_Obj>, _ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_ListObjAppendElement(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ listPtr: UnsafeMutablePointer<Tcl_Obj>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_ListObjAppendList(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ListObjAppendList(_ interp: UnsafePointer<Tcl_Interp>, _ listPtr: UnsafePointer<Tcl_Obj>, _ elemListPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_ListObjAppendList(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ listPtr: UnsafeMutablePointer<Tcl_Obj>, _ elemListPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_ListObjGetElements(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ListObjGetElements(_ interp: UnsafePointer<Tcl_Interp>, _ listPtr: UnsafePointer<Tcl_Obj>, _ objcPtr: UnsafePointer<Int32>, _ objvPtr: UnsafePointer<UnsafePointer<UnsafePointer<Tcl_Obj>>>) -> Int32 ``` |
| To | ``` func Tcl_ListObjGetElements(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ listPtr: UnsafeMutablePointer<Tcl_Obj>, _ objcPtr: UnsafeMutablePointer<Int32>, _ objvPtr: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32 ``` |

Modified Tcl_ListObjIndex(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ListObjIndex(_ interp: UnsafePointer<Tcl_Interp>, _ listPtr: UnsafePointer<Tcl_Obj>, _ index: Int32, _ objPtrPtr: UnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_ListObjIndex(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ listPtr: UnsafeMutablePointer<Tcl_Obj>, _ index: Int32, _ objPtrPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_ListObjLength(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ListObjLength(_ interp: UnsafePointer<Tcl_Interp>, _ listPtr: UnsafePointer<Tcl_Obj>, _ lengthPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_ListObjLength(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ listPtr: UnsafeMutablePointer<Tcl_Obj>, _ lengthPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_ListObjReplace(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ListObjReplace(_ interp: UnsafePointer<Tcl_Interp>, _ listPtr: UnsafePointer<Tcl_Obj>, _ first: Int32, _ count: Int32, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_ListObjReplace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ listPtr: UnsafeMutablePointer<Tcl_Obj>, _ first: Int32, _ count: Int32, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_LogCommandInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LogCommandInfo(_ interp: UnsafePointer<Tcl_Interp>, _ script: ConstUnsafePointer<Int8>, _ command: ConstUnsafePointer<Int8>, _ length: Int32) ``` |
| To | ``` func Tcl_LogCommandInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ script: UnsafePointer<Int8>, _ command: UnsafePointer<Int8>, _ length: Int32) ``` |

Modified Tcl_Main(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, CFunctionPointer<Tcl_AppInitProc>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Main(_ argc: Int32, _ argv: UnsafePointer<UnsafePointer<Int8>>, _ appInitProc: CFunctionPointer<Tcl_AppInitProc>) ``` |
| To | ``` func Tcl_Main(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ appInitProc: CFunctionPointer<Tcl_AppInitProc>) ``` |

Modified Tcl_MakeSafe(UnsafeMutablePointer<Tcl_Interp>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_MakeSafe(_ interp: UnsafePointer<Tcl_Interp>) -> Int32 ``` |
| To | ``` func Tcl_MakeSafe(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> Int32 ``` |

Modified Tcl_MathProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_MathProc = ((ClientData, UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Value>, UnsafePointer<Tcl_Value>) -> Int32) ``` |
| To | ``` typealias Tcl_MathProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32) ``` |

Modified Tcl_Merge(Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Merge(_ argc: Int32, _ argv: ConstUnsafePointer<ConstUnsafePointer<Int8>>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_Merge(_ argc: Int32, _ argv: UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_MutexFinalize(UnsafeMutablePointer<Tcl_Mutex>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_MutexFinalize(_ mutex: UnsafePointer<Tcl_Mutex>) ``` |
| To | ``` func Tcl_MutexFinalize(_ mutex: UnsafeMutablePointer<Tcl_Mutex>) ``` |

Modified Tcl_MutexLock(UnsafeMutablePointer<Tcl_Mutex>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_MutexLock(_ mutexPtr: UnsafePointer<Tcl_Mutex>) ``` |
| To | ``` func Tcl_MutexLock(_ mutexPtr: UnsafeMutablePointer<Tcl_Mutex>) ``` |

Modified Tcl_MutexUnlock(UnsafeMutablePointer<Tcl_Mutex>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_MutexUnlock(_ mutexPtr: UnsafePointer<Tcl_Mutex>) ``` |
| To | ``` func Tcl_MutexUnlock(_ mutexPtr: UnsafeMutablePointer<Tcl_Mutex>) ``` |

Modified Tcl_NewBignumObj(UnsafeMutablePointer<mp_int>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewBignumObj(_ value: UnsafePointer<mp_int>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewBignumObj(_ value: UnsafeMutablePointer<mp_int>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewBooleanObj(Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewBooleanObj(_ boolValue: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewBooleanObj(_ boolValue: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewByteArrayObj(UnsafePointer<UInt8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewByteArrayObj(_ bytes: ConstUnsafePointer<UInt8>, _ length: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewByteArrayObj(_ bytes: UnsafePointer<UInt8>, _ length: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewDictObj() -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewDictObj() -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewDictObj() -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewDoubleObj(Double) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewDoubleObj(_ doubleValue: Double) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewDoubleObj(_ doubleValue: Double) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewIntObj(Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewIntObj(_ intValue: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewIntObj(_ intValue: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewListObj(Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewListObj(_ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewListObj(_ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewLongObj(Int) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewLongObj(_ longValue: Int) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewLongObj(_ longValue: Int) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewObj() -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewObj() -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewObj() -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewStringObj(UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewStringObj(_ bytes: ConstUnsafePointer<Int8>, _ length: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewStringObj(_ bytes: UnsafePointer<Int8>, _ length: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewUnicodeObj(UnsafePointer<Tcl_UniChar>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewUnicodeObj(_ unicode: ConstUnsafePointer<Tcl_UniChar>, _ numChars: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewUnicodeObj(_ unicode: UnsafePointer<Tcl_UniChar>, _ numChars: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NewWideIntObj(Tcl_WideInt) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NewWideIntObj(_ wideValue: Tcl_WideInt) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_NewWideIntObj(_ wideValue: Tcl_WideInt) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_NextHashEntry(UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NextHashEntry(_ searchPtr: UnsafePointer<Tcl_HashSearch>) -> UnsafePointer<Tcl_HashEntry> ``` |
| To | ``` func Tcl_NextHashEntry(_ searchPtr: UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry> ``` |

Modified Tcl_NumUtfChars(UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_NumUtfChars(_ src: ConstUnsafePointer<Int8>, _ length: Int32) -> Int32 ``` |
| To | ``` func Tcl_NumUtfChars(_ src: UnsafePointer<Int8>, _ length: Int32) -> Int32 ``` |

Modified Tcl_ObjCmdProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_ObjCmdProc = ((ClientData, UnsafePointer<Tcl_Interp>, Int32, ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32) ``` |
| To | ``` typealias Tcl_ObjCmdProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32) ``` |

Modified Tcl_ObjGetVar2(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ObjGetVar2(_ interp: UnsafePointer<Tcl_Interp>, _ part1Ptr: UnsafePointer<Tcl_Obj>, _ part2Ptr: UnsafePointer<Tcl_Obj>, _ flags: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_ObjGetVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1Ptr: UnsafeMutablePointer<Tcl_Obj>, _ part2Ptr: UnsafeMutablePointer<Tcl_Obj>, _ flags: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_ObjSetVar2(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ObjSetVar2(_ interp: UnsafePointer<Tcl_Interp>, _ part1Ptr: UnsafePointer<Tcl_Obj>, _ part2Ptr: UnsafePointer<Tcl_Obj>, _ newValuePtr: UnsafePointer<Tcl_Obj>, _ flags: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_ObjSetVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1Ptr: UnsafeMutablePointer<Tcl_Obj>, _ part2Ptr: UnsafeMutablePointer<Tcl_Obj>, _ newValuePtr: UnsafeMutablePointer<Tcl_Obj>, _ flags: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_OldStat_

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_OldStat_ = UnsafePointer<stat> ``` |
| To | ``` typealias Tcl_OldStat_ = UnsafeMutablePointer<stat> ``` |

Modified Tcl_OpenCommandChannel(UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, Int32) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_OpenCommandChannel(_ interp: UnsafePointer<Tcl_Interp>, _ argc: Int32, _ argv: UnsafePointer<ConstUnsafePointer<Int8>>, _ flags: Int32) -> Tcl_Channel ``` |
| To | ``` func Tcl_OpenCommandChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ argc: Int32, _ argv: UnsafeMutablePointer<UnsafePointer<Int8>>, _ flags: Int32) -> Tcl_Channel ``` |

Modified Tcl_OpenFileChannel(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_OpenFileChannel(_ interp: UnsafePointer<Tcl_Interp>, _ fileName: ConstUnsafePointer<Int8>, _ modeString: ConstUnsafePointer<Int8>, _ permissions: Int32) -> Tcl_Channel ``` |
| To | ``` func Tcl_OpenFileChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ fileName: UnsafePointer<Int8>, _ modeString: UnsafePointer<Int8>, _ permissions: Int32) -> Tcl_Channel ``` |

Modified Tcl_OpenTcpClient(UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, Int32) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_OpenTcpClient(_ interp: UnsafePointer<Tcl_Interp>, _ port: Int32, _ address: ConstUnsafePointer<Int8>, _ myaddr: ConstUnsafePointer<Int8>, _ myport: Int32, _ async: Int32) -> Tcl_Channel ``` |
| To | ``` func Tcl_OpenTcpClient(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ port: Int32, _ address: UnsafePointer<Int8>, _ myaddr: UnsafePointer<Int8>, _ myport: Int32, _ async: Int32) -> Tcl_Channel ``` |

Modified Tcl_OpenTcpServer(UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, CFunctionPointer<Tcl_TcpAcceptProc>, ClientData) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_OpenTcpServer(_ interp: UnsafePointer<Tcl_Interp>, _ port: Int32, _ host: ConstUnsafePointer<Int8>, _ acceptProc: CFunctionPointer<Tcl_TcpAcceptProc>, _ callbackData: ClientData) -> Tcl_Channel ``` |
| To | ``` func Tcl_OpenTcpServer(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ port: Int32, _ host: UnsafePointer<Int8>, _ acceptProc: CFunctionPointer<Tcl_TcpAcceptProc>, _ callbackData: ClientData) -> Tcl_Channel ``` |

Modified Tcl_PackageInitProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_PackageInitProc = ((UnsafePointer<Tcl_Interp>) -> Int32) ``` |
| To | ``` typealias Tcl_PackageInitProc = ((UnsafeMutablePointer<Tcl_Interp>) -> Int32) ``` |

Modified Tcl_PackageUnloadProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_PackageUnloadProc = ((UnsafePointer<Tcl_Interp>, Int32) -> Int32) ``` |
| To | ``` typealias Tcl_PackageUnloadProc = ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32) ``` |

Modified Tcl_PanicVA(UnsafePointer<Int8>, CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PanicVA(_ format: ConstUnsafePointer<Int8>, _ argList: CVaListPointer) ``` |
| To | ``` func Tcl_PanicVA(_ format: UnsafePointer<Int8>, _ argList: CVaListPointer) ``` |

Modified Tcl_ParseBraces(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ParseBraces(_ interp: UnsafePointer<Tcl_Interp>, _ start: ConstUnsafePointer<Int8>, _ numBytes: Int32, _ parsePtr: UnsafePointer<Tcl_Parse>, _ append: Int32, _ termPtr: UnsafePointer<ConstUnsafePointer<Int8>>) -> Int32 ``` |
| To | ``` func Tcl_ParseBraces(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ start: UnsafePointer<Int8>, _ numBytes: Int32, _ parsePtr: UnsafeMutablePointer<Tcl_Parse>, _ append: Int32, _ termPtr: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32 ``` |

Modified Tcl_ParseCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ParseCommand(_ interp: UnsafePointer<Tcl_Interp>, _ start: ConstUnsafePointer<Int8>, _ numBytes: Int32, _ nested: Int32, _ parsePtr: UnsafePointer<Tcl_Parse>) -> Int32 ``` |
| To | ``` func Tcl_ParseCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ start: UnsafePointer<Int8>, _ numBytes: Int32, _ nested: Int32, _ parsePtr: UnsafeMutablePointer<Tcl_Parse>) -> Int32 ``` |

Modified Tcl_ParseExpr(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ParseExpr(_ interp: UnsafePointer<Tcl_Interp>, _ start: ConstUnsafePointer<Int8>, _ numBytes: Int32, _ parsePtr: UnsafePointer<Tcl_Parse>) -> Int32 ``` |
| To | ``` func Tcl_ParseExpr(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ start: UnsafePointer<Int8>, _ numBytes: Int32, _ parsePtr: UnsafeMutablePointer<Tcl_Parse>) -> Int32 ``` |

Modified Tcl_ParseQuotedString(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ParseQuotedString(_ interp: UnsafePointer<Tcl_Interp>, _ start: ConstUnsafePointer<Int8>, _ numBytes: Int32, _ parsePtr: UnsafePointer<Tcl_Parse>, _ append: Int32, _ termPtr: UnsafePointer<ConstUnsafePointer<Int8>>) -> Int32 ``` |
| To | ``` func Tcl_ParseQuotedString(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ start: UnsafePointer<Int8>, _ numBytes: Int32, _ parsePtr: UnsafeMutablePointer<Tcl_Parse>, _ append: Int32, _ termPtr: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32 ``` |

Modified Tcl_ParseVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ParseVar(_ interp: UnsafePointer<Tcl_Interp>, _ start: ConstUnsafePointer<Int8>, _ termPtr: UnsafePointer<ConstUnsafePointer<Int8>>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_ParseVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ start: UnsafePointer<Int8>, _ termPtr: UnsafeMutablePointer<UnsafePointer<Int8>>) -> UnsafePointer<Int8> ``` |

Modified Tcl_ParseVarName(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ParseVarName(_ interp: UnsafePointer<Tcl_Interp>, _ start: ConstUnsafePointer<Int8>, _ numBytes: Int32, _ parsePtr: UnsafePointer<Tcl_Parse>, _ append: Int32) -> Int32 ``` |
| To | ``` func Tcl_ParseVarName(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ start: UnsafePointer<Int8>, _ numBytes: Int32, _ parsePtr: UnsafeMutablePointer<Tcl_Parse>, _ append: Int32) -> Int32 ``` |

Modified Tcl_PkgInitStubsCheck(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PkgInitStubsCheck(_ interp: UnsafePointer<Tcl_Interp>, _ version: ConstUnsafePointer<Int8>, _ exact: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_PkgInitStubsCheck(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ version: UnsafePointer<Int8>, _ exact: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_PkgPresent(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PkgPresent(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ version: ConstUnsafePointer<Int8>, _ exact: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_PkgPresent(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ version: UnsafePointer<Int8>, _ exact: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_PkgPresentEx(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PkgPresentEx(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ version: ConstUnsafePointer<Int8>, _ exact: Int32, _ clientDataPtr: UnsafePointer<ClientData>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_PkgPresentEx(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ version: UnsafePointer<Int8>, _ exact: Int32, _ clientDataPtr: UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8> ``` |

Modified Tcl_PkgProvide(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PkgProvide(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ version: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_PkgProvide(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ version: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_PkgProvideEx(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, ClientData) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PkgProvideEx(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ version: ConstUnsafePointer<Int8>, _ clientData: ClientData) -> Int32 ``` |
| To | ``` func Tcl_PkgProvideEx(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ version: UnsafePointer<Int8>, _ clientData: ClientData) -> Int32 ``` |

Modified Tcl_PkgRequire(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PkgRequire(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ version: ConstUnsafePointer<Int8>, _ exact: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_PkgRequire(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ version: UnsafePointer<Int8>, _ exact: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_PkgRequireEx(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PkgRequireEx(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ version: ConstUnsafePointer<Int8>, _ exact: Int32, _ clientDataPtr: UnsafePointer<ClientData>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_PkgRequireEx(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ version: UnsafePointer<Int8>, _ exact: Int32, _ clientDataPtr: UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8> ``` |

Modified Tcl_PkgRequireProc(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<ClientData>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PkgRequireProc(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, _ clientDataPtr: UnsafePointer<ClientData>) -> Int32 ``` |
| To | ``` func Tcl_PkgRequireProc(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, _ clientDataPtr: UnsafeMutablePointer<ClientData>) -> Int32 ``` |

Modified Tcl_PosixError(UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PosixError(_ interp: UnsafePointer<Tcl_Interp>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_PosixError(_ interp: UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8> ``` |

Modified Tcl_PrintDouble(UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PrintDouble(_ interp: UnsafePointer<Tcl_Interp>, _ value: Double, _ dst: UnsafePointer<Int8>) ``` |
| To | ``` func Tcl_PrintDouble(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ value: Double, _ dst: UnsafeMutablePointer<Int8>) ``` |

Modified Tcl_ProcObjCmd(ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ProcObjCmd(_ clientData: ClientData, _ interp: UnsafePointer<Tcl_Interp>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) -> Int32 ``` |
| To | ``` func Tcl_ProcObjCmd(_ clientData: ClientData, _ interp: UnsafeMutablePointer<Tcl_Interp>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32 ``` |

Modified Tcl_PutEnv(UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_PutEnv(_ assignment: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_PutEnv(_ assignment: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_QueryTimeProc(UnsafeMutablePointer<CFunctionPointer<Tcl_GetTimeProc>>, UnsafeMutablePointer<CFunctionPointer<Tcl_ScaleTimeProc>>, UnsafeMutablePointer<ClientData>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_QueryTimeProc(_ getProc: UnsafePointer<CFunctionPointer<Tcl_GetTimeProc>>, _ scaleProc: UnsafePointer<CFunctionPointer<Tcl_ScaleTimeProc>>, _ clientData: UnsafePointer<ClientData>) ``` |
| To | ``` func Tcl_QueryTimeProc(_ getProc: UnsafeMutablePointer<CFunctionPointer<Tcl_GetTimeProc>>, _ scaleProc: UnsafeMutablePointer<CFunctionPointer<Tcl_ScaleTimeProc>>, _ clientData: UnsafeMutablePointer<ClientData>) ``` |

Modified Tcl_QueueEvent(UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_QueueEvent(_ evPtr: UnsafePointer<Tcl_Event>, _ position: Tcl_QueuePosition) ``` |
| To | ``` func Tcl_QueueEvent(_ evPtr: UnsafeMutablePointer<Tcl_Event>, _ position: Tcl_QueuePosition) ``` |

Modified Tcl_Read(Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Read(_ chan: Tcl_Channel, _ bufPtr: UnsafePointer<Int8>, _ toRead: Int32) -> Int32 ``` |
| To | ``` func Tcl_Read(_ chan: Tcl_Channel, _ bufPtr: UnsafeMutablePointer<Int8>, _ toRead: Int32) -> Int32 ``` |

Modified Tcl_ReadChars(Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ReadChars(_ channel: Tcl_Channel, _ objPtr: UnsafePointer<Tcl_Obj>, _ charsToRead: Int32, _ appendFlag: Int32) -> Int32 ``` |
| To | ``` func Tcl_ReadChars(_ channel: Tcl_Channel, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ charsToRead: Int32, _ appendFlag: Int32) -> Int32 ``` |

Modified Tcl_ReadRaw(Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ReadRaw(_ chan: Tcl_Channel, _ dst: UnsafePointer<Int8>, _ bytesToRead: Int32) -> Int32 ``` |
| To | ``` func Tcl_ReadRaw(_ chan: Tcl_Channel, _ dst: UnsafeMutablePointer<Int8>, _ bytesToRead: Int32) -> Int32 ``` |

Modified Tcl_Realloc(UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Realloc(_ ptr: UnsafePointer<Int8>, _ size: UInt32) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_Realloc(_ ptr: UnsafeMutablePointer<Int8>, _ size: UInt32) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_RecordAndEval(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RecordAndEval(_ interp: UnsafePointer<Tcl_Interp>, _ cmd: ConstUnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_RecordAndEval(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmd: UnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_RecordAndEvalObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RecordAndEvalObj(_ interp: UnsafePointer<Tcl_Interp>, _ cmdPtr: UnsafePointer<Tcl_Obj>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_RecordAndEvalObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdPtr: UnsafeMutablePointer<Tcl_Obj>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_RegExpCompile(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_RegExp

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegExpCompile(_ interp: UnsafePointer<Tcl_Interp>, _ pattern: ConstUnsafePointer<Int8>) -> Tcl_RegExp ``` |
| To | ``` func Tcl_RegExpCompile(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pattern: UnsafePointer<Int8>) -> Tcl_RegExp ``` |

Modified Tcl_RegExpExec(UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegExpExec(_ interp: UnsafePointer<Tcl_Interp>, _ regexp: Tcl_RegExp, _ text: ConstUnsafePointer<Int8>, _ start: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_RegExpExec(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ regexp: Tcl_RegExp, _ text: UnsafePointer<Int8>, _ start: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_RegExpExecObj(UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegExpExecObj(_ interp: UnsafePointer<Tcl_Interp>, _ regexp: Tcl_RegExp, _ textObj: UnsafePointer<Tcl_Obj>, _ offset: Int32, _ nmatches: Int32, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_RegExpExecObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ regexp: Tcl_RegExp, _ textObj: UnsafeMutablePointer<Tcl_Obj>, _ offset: Int32, _ nmatches: Int32, _ flags: Int32) -> Int32 ``` |

Modified Tcl_RegExpGetInfo(Tcl_RegExp, UnsafeMutablePointer<Tcl_RegExpInfo>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegExpGetInfo(_ regexp: Tcl_RegExp, _ infoPtr: UnsafePointer<Tcl_RegExpInfo>) ``` |
| To | ``` func Tcl_RegExpGetInfo(_ regexp: Tcl_RegExp, _ infoPtr: UnsafeMutablePointer<Tcl_RegExpInfo>) ``` |

Modified Tcl_RegExpMatch(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegExpMatch(_ interp: UnsafePointer<Tcl_Interp>, _ text: ConstUnsafePointer<Int8>, _ pattern: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_RegExpMatch(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ text: UnsafePointer<Int8>, _ pattern: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_RegExpMatchObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegExpMatchObj(_ interp: UnsafePointer<Tcl_Interp>, _ textObj: UnsafePointer<Tcl_Obj>, _ patternObj: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_RegExpMatchObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ textObj: UnsafeMutablePointer<Tcl_Obj>, _ patternObj: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_RegExpRange(Tcl_RegExp, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafePointer<Int8>>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegExpRange(_ regexp: Tcl_RegExp, _ index: Int32, _ startPtr: UnsafePointer<ConstUnsafePointer<Int8>>, _ endPtr: UnsafePointer<ConstUnsafePointer<Int8>>) ``` |
| To | ``` func Tcl_RegExpRange(_ regexp: Tcl_RegExp, _ index: Int32, _ startPtr: UnsafeMutablePointer<UnsafePointer<Int8>>, _ endPtr: UnsafeMutablePointer<UnsafePointer<Int8>>) ``` |

Modified Tcl_RegisterChannel(UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegisterChannel(_ interp: UnsafePointer<Tcl_Interp>, _ chan: Tcl_Channel) ``` |
| To | ``` func Tcl_RegisterChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ chan: Tcl_Channel) ``` |

Modified Tcl_RegisterConfig(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Config>, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegisterConfig(_ interp: UnsafePointer<Tcl_Interp>, _ pkgName: ConstUnsafePointer<Int8>, _ configuration: UnsafePointer<Tcl_Config>, _ valEncoding: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_RegisterConfig(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pkgName: UnsafePointer<Int8>, _ configuration: UnsafeMutablePointer<Tcl_Config>, _ valEncoding: UnsafePointer<Int8>) ``` |

Modified Tcl_RegisterObjType(UnsafeMutablePointer<Tcl_ObjType>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RegisterObjType(_ typePtr: UnsafePointer<Tcl_ObjType>) ``` |
| To | ``` func Tcl_RegisterObjType(_ typePtr: UnsafeMutablePointer<Tcl_ObjType>) ``` |

Modified Tcl_ResetResult(UnsafeMutablePointer<Tcl_Interp>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ResetResult(_ interp: UnsafePointer<Tcl_Interp>) ``` |
| To | ``` func Tcl_ResetResult(_ interp: UnsafeMutablePointer<Tcl_Interp>) ``` |

Modified Tcl_RestoreInterpState(UnsafeMutablePointer<Tcl_Interp>, Tcl_InterpState) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RestoreInterpState(_ interp: UnsafePointer<Tcl_Interp>, _ state: Tcl_InterpState) -> Int32 ``` |
| To | ``` func Tcl_RestoreInterpState(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ state: Tcl_InterpState) -> Int32 ``` |

Modified Tcl_RestoreResult(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_RestoreResult(_ interp: UnsafePointer<Tcl_Interp>, _ statePtr: UnsafePointer<Tcl_SavedResult>) ``` |
| To | ``` func Tcl_RestoreResult(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ statePtr: UnsafeMutablePointer<Tcl_SavedResult>) ``` |

Modified Tcl_SaveInterpState(UnsafeMutablePointer<Tcl_Interp>, Int32) -> Tcl_InterpState

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SaveInterpState(_ interp: UnsafePointer<Tcl_Interp>, _ status: Int32) -> Tcl_InterpState ``` |
| To | ``` func Tcl_SaveInterpState(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ status: Int32) -> Tcl_InterpState ``` |

Modified Tcl_SaveResult(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SaveResult(_ interp: UnsafePointer<Tcl_Interp>, _ statePtr: UnsafePointer<Tcl_SavedResult>) ``` |
| To | ``` func Tcl_SaveResult(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ statePtr: UnsafeMutablePointer<Tcl_SavedResult>) ``` |

Modified Tcl_ScaleTimeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_ScaleTimeProc = ((UnsafePointer<Tcl_Time>, ClientData) -> Void) ``` |
| To | ``` typealias Tcl_ScaleTimeProc = ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void) ``` |

Modified Tcl_ScanCountedElement(UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ScanCountedElement(_ str: ConstUnsafePointer<Int8>, _ length: Int32, _ flagPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_ScanCountedElement(_ str: UnsafePointer<Int8>, _ length: Int32, _ flagPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_ScanElement(UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ScanElement(_ str: ConstUnsafePointer<Int8>, _ flagPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_ScanElement(_ str: UnsafePointer<Int8>, _ flagPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_SetAssocData(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetAssocData(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_SetAssocData(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |

Modified Tcl_SetBignumObj(UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetBignumObj(_ obj: UnsafePointer<Tcl_Obj>, _ value: UnsafePointer<mp_int>) ``` |
| To | ``` func Tcl_SetBignumObj(_ obj: UnsafeMutablePointer<Tcl_Obj>, _ value: UnsafeMutablePointer<mp_int>) ``` |

Modified Tcl_SetBooleanObj(UnsafeMutablePointer<Tcl_Obj>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetBooleanObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ boolValue: Int32) ``` |
| To | ``` func Tcl_SetBooleanObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ boolValue: Int32) ``` |

Modified Tcl_SetByteArrayLength(UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<UInt8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetByteArrayLength(_ objPtr: UnsafePointer<Tcl_Obj>, _ length: Int32) -> UnsafePointer<UInt8> ``` |
| To | ``` func Tcl_SetByteArrayLength(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ length: Int32) -> UnsafeMutablePointer<UInt8> ``` |

Modified Tcl_SetByteArrayObj(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<UInt8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetByteArrayObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ bytes: ConstUnsafePointer<UInt8>, _ length: Int32) ``` |
| To | ``` func Tcl_SetByteArrayObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ bytes: UnsafePointer<UInt8>, _ length: Int32) ``` |

Modified Tcl_SetChannelError(Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetChannelError(_ chan: Tcl_Channel, _ msg: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_SetChannelError(_ chan: Tcl_Channel, _ msg: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_SetChannelErrorInterp(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetChannelErrorInterp(_ interp: UnsafePointer<Tcl_Interp>, _ msg: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_SetChannelErrorInterp(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ msg: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_SetChannelOption(UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetChannelOption(_ interp: UnsafePointer<Tcl_Interp>, _ chan: Tcl_Channel, _ optionName: ConstUnsafePointer<Int8>, _ newValue: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_SetChannelOption(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ chan: Tcl_Channel, _ optionName: UnsafePointer<Int8>, _ newValue: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_SetCommandInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Tcl_CmdInfo>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetCommandInfo(_ interp: UnsafePointer<Tcl_Interp>, _ cmdName: ConstUnsafePointer<Int8>, _ infoPtr: ConstUnsafePointer<Tcl_CmdInfo>) -> Int32 ``` |
| To | ``` func Tcl_SetCommandInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ infoPtr: UnsafePointer<Tcl_CmdInfo>) -> Int32 ``` |

Modified Tcl_SetCommandInfoFromToken(Tcl_Command, UnsafePointer<Tcl_CmdInfo>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetCommandInfoFromToken(_ token: Tcl_Command, _ infoPtr: ConstUnsafePointer<Tcl_CmdInfo>) -> Int32 ``` |
| To | ``` func Tcl_SetCommandInfoFromToken(_ token: Tcl_Command, _ infoPtr: UnsafePointer<Tcl_CmdInfo>) -> Int32 ``` |

Modified Tcl_SetDefaultEncodingDir(UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetDefaultEncodingDir(_ path: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_SetDefaultEncodingDir(_ path: UnsafePointer<Int8>) ``` |

Modified Tcl_SetDoubleObj(UnsafeMutablePointer<Tcl_Obj>, Double)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetDoubleObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ doubleValue: Double) ``` |
| To | ``` func Tcl_SetDoubleObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ doubleValue: Double) ``` |

Modified Tcl_SetEncodingSearchPath(UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetEncodingSearchPath(_ searchPath: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_SetEncodingSearchPath(_ searchPath: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_SetEnsembleFlags(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetEnsembleFlags(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_SetEnsembleFlags(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ flags: Int32) -> Int32 ``` |

Modified Tcl_SetEnsembleMappingDict(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetEnsembleMappingDict(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ mapDict: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_SetEnsembleMappingDict(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ mapDict: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_SetEnsembleSubcommandList(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetEnsembleSubcommandList(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ subcmdList: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_SetEnsembleSubcommandList(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ subcmdList: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_SetEnsembleUnknownHandler(UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetEnsembleUnknownHandler(_ interp: UnsafePointer<Tcl_Interp>, _ token: Tcl_Command, _ unknownList: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_SetEnsembleUnknownHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ token: Tcl_Command, _ unknownList: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_SetErrorCodeVA(UnsafeMutablePointer<Tcl_Interp>, CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetErrorCodeVA(_ interp: UnsafePointer<Tcl_Interp>, _ argList: CVaListPointer) ``` |
| To | ``` func Tcl_SetErrorCodeVA(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ argList: CVaListPointer) ``` |

Modified Tcl_SetFromAnyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_SetFromAnyProc = ((UnsafePointer<Tcl_Interp>, UnsafePointer<Tcl_Obj>) -> Int32) ``` |
| To | ``` typealias Tcl_SetFromAnyProc = ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32) ``` |

Modified Tcl_SetIntObj(UnsafeMutablePointer<Tcl_Obj>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetIntObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ intValue: Int32) ``` |
| To | ``` func Tcl_SetIntObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ intValue: Int32) ``` |

Modified Tcl_SetListObj(UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetListObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>) ``` |
| To | ``` func Tcl_SetListObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) ``` |

Modified Tcl_SetLongObj(UnsafeMutablePointer<Tcl_Obj>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetLongObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ longValue: Int) ``` |
| To | ``` func Tcl_SetLongObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ longValue: Int) ``` |

Modified Tcl_SetMaxBlockTime(UnsafeMutablePointer<Tcl_Time>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetMaxBlockTime(_ timePtr: UnsafePointer<Tcl_Time>) ``` |
| To | ``` func Tcl_SetMaxBlockTime(_ timePtr: UnsafeMutablePointer<Tcl_Time>) ``` |

Modified Tcl_SetNamespaceUnknownHandler(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetNamespaceUnknownHandler(_ interp: UnsafePointer<Tcl_Interp>, _ nsPtr: UnsafePointer<Tcl_Namespace>, _ handlerPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_SetNamespaceUnknownHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ nsPtr: UnsafeMutablePointer<Tcl_Namespace>, _ handlerPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_SetNotifier(UnsafeMutablePointer<Tcl_NotifierProcs>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetNotifier(_ notifierProcPtr: UnsafePointer<Tcl_NotifierProcs>) ``` |
| To | ``` func Tcl_SetNotifier(_ notifierProcPtr: UnsafeMutablePointer<Tcl_NotifierProcs>) ``` |

Modified Tcl_SetObjErrorCode(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetObjErrorCode(_ interp: UnsafePointer<Tcl_Interp>, _ errorObjPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_SetObjErrorCode(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ errorObjPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_SetObjLength(UnsafeMutablePointer<Tcl_Obj>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetObjLength(_ objPtr: UnsafePointer<Tcl_Obj>, _ length: Int32) ``` |
| To | ``` func Tcl_SetObjLength(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ length: Int32) ``` |

Modified Tcl_SetObjResult(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetObjResult(_ interp: UnsafePointer<Tcl_Interp>, _ resultObjPtr: UnsafePointer<Tcl_Obj>) ``` |
| To | ``` func Tcl_SetObjResult(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ resultObjPtr: UnsafeMutablePointer<Tcl_Obj>) ``` |

Modified Tcl_SetRecursionLimit(UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetRecursionLimit(_ interp: UnsafePointer<Tcl_Interp>, _ depth: Int32) -> Int32 ``` |
| To | ``` func Tcl_SetRecursionLimit(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ depth: Int32) -> Int32 ``` |

Modified Tcl_SetResult(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Int8>, CFunctionPointer<Tcl_FreeProc>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetResult(_ interp: UnsafePointer<Tcl_Interp>, _ result: UnsafePointer<Int8>, _ freeProc: CFunctionPointer<Tcl_FreeProc>) ``` |
| To | ``` func Tcl_SetResult(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ result: UnsafeMutablePointer<Int8>, _ freeProc: CFunctionPointer<Tcl_FreeProc>) ``` |

Modified Tcl_SetReturnOptions(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetReturnOptions(_ interp: UnsafePointer<Tcl_Interp>, _ options: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_SetReturnOptions(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ options: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_SetStringObj(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetStringObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ bytes: ConstUnsafePointer<Int8>, _ length: Int32) ``` |
| To | ``` func Tcl_SetStringObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ bytes: UnsafePointer<Int8>, _ length: Int32) ``` |

Modified Tcl_SetSystemEncoding(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetSystemEncoding(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_SetSystemEncoding(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_SetTimer(UnsafeMutablePointer<Tcl_Time>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetTimer(_ timePtr: UnsafePointer<Tcl_Time>) ``` |
| To | ``` func Tcl_SetTimer(_ timePtr: UnsafeMutablePointer<Tcl_Time>) ``` |

Modified Tcl_SetTimerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_SetTimerProc = ((UnsafePointer<Tcl_Time>) -> Void) ``` |
| To | ``` typealias Tcl_SetTimerProc = ((UnsafeMutablePointer<Tcl_Time>) -> Void) ``` |

Modified Tcl_SetUnicodeObj(UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetUnicodeObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ unicode: ConstUnsafePointer<Tcl_UniChar>, _ numChars: Int32) ``` |
| To | ``` func Tcl_SetUnicodeObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ unicode: UnsafePointer<Tcl_UniChar>, _ numChars: Int32) ``` |

Modified Tcl_SetVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetVar(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ newValue: ConstUnsafePointer<Int8>, _ flags: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_SetVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ newValue: UnsafePointer<Int8>, _ flags: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_SetVar2(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetVar2(_ interp: UnsafePointer<Tcl_Interp>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ newValue: ConstUnsafePointer<Int8>, _ flags: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_SetVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ newValue: UnsafePointer<Int8>, _ flags: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_SetVar2Ex(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetVar2Ex(_ interp: UnsafePointer<Tcl_Interp>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ newValuePtr: UnsafePointer<Tcl_Obj>, _ flags: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_SetVar2Ex(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ newValuePtr: UnsafeMutablePointer<Tcl_Obj>, _ flags: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_SetWideIntObj(UnsafeMutablePointer<Tcl_Obj>, Tcl_WideInt)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetWideIntObj(_ objPtr: UnsafePointer<Tcl_Obj>, _ wideValue: Tcl_WideInt) ``` |
| To | ``` func Tcl_SetWideIntObj(_ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ wideValue: Tcl_WideInt) ``` |

Modified Tcl_SignalId(Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SignalId(_ sig: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_SignalId(_ sig: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_SignalMsg(Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SignalMsg(_ sig: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_SignalMsg(_ sig: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_SourceRCFile(UnsafeMutablePointer<Tcl_Interp>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SourceRCFile(_ interp: UnsafePointer<Tcl_Interp>) ``` |
| To | ``` func Tcl_SourceRCFile(_ interp: UnsafeMutablePointer<Tcl_Interp>) ``` |

Modified Tcl_SplitList(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SplitList(_ interp: UnsafePointer<Tcl_Interp>, _ listStr: ConstUnsafePointer<Int8>, _ argcPtr: UnsafePointer<Int32>, _ argvPtr: UnsafePointer<UnsafePointer<ConstUnsafePointer<Int8>>>) -> Int32 ``` |
| To | ``` func Tcl_SplitList(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ listStr: UnsafePointer<Int8>, _ argcPtr: UnsafeMutablePointer<Int32>, _ argvPtr: UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32 ``` |

Modified Tcl_SplitPath(UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SplitPath(_ path: ConstUnsafePointer<Int8>, _ argcPtr: UnsafePointer<Int32>, _ argvPtr: UnsafePointer<UnsafePointer<ConstUnsafePointer<Int8>>>) ``` |
| To | ``` func Tcl_SplitPath(_ path: UnsafePointer<Int8>, _ argcPtr: UnsafeMutablePointer<Int32>, _ argvPtr: UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) ``` |

Modified Tcl_StackChannel(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_ChannelType>, ClientData, Int32, Tcl_Channel) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_StackChannel(_ interp: UnsafePointer<Tcl_Interp>, _ typePtr: UnsafePointer<Tcl_ChannelType>, _ instanceData: ClientData, _ mask: Int32, _ prevChan: Tcl_Channel) -> Tcl_Channel ``` |
| To | ``` func Tcl_StackChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ typePtr: UnsafeMutablePointer<Tcl_ChannelType>, _ instanceData: ClientData, _ mask: Int32, _ prevChan: Tcl_Channel) -> Tcl_Channel ``` |

Modified Tcl_Stat(UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Stat(_ path: ConstUnsafePointer<Int8>, _ bufPtr: UnsafePointer<stat>) -> Int32 ``` |
| To | ``` func Tcl_Stat(_ path: UnsafePointer<Int8>, _ bufPtr: UnsafeMutablePointer<stat>) -> Int32 ``` |

Modified Tcl_Stat_

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_Stat_ = UnsafePointer<Tcl_StatBuf> ``` |
| To | ``` typealias Tcl_Stat_ = UnsafeMutablePointer<Tcl_StatBuf> ``` |

Modified Tcl_StaticPackage(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_PackageInitProc>, CFunctionPointer<Tcl_PackageInitProc>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_StaticPackage(_ interp: UnsafePointer<Tcl_Interp>, _ pkgName: ConstUnsafePointer<Int8>, _ initProc: CFunctionPointer<Tcl_PackageInitProc>, _ safeInitProc: CFunctionPointer<Tcl_PackageInitProc>) ``` |
| To | ``` func Tcl_StaticPackage(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pkgName: UnsafePointer<Int8>, _ initProc: CFunctionPointer<Tcl_PackageInitProc>, _ safeInitProc: CFunctionPointer<Tcl_PackageInitProc>) ``` |

Modified Tcl_StringCaseMatch(UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_StringCaseMatch(_ str: ConstUnsafePointer<Int8>, _ pattern: ConstUnsafePointer<Int8>, _ nocase: Int32) -> Int32 ``` |
| To | ``` func Tcl_StringCaseMatch(_ str: UnsafePointer<Int8>, _ pattern: UnsafePointer<Int8>, _ nocase: Int32) -> Int32 ``` |

Modified Tcl_StringMatch(UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_StringMatch(_ str: ConstUnsafePointer<Int8>, _ pattern: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_StringMatch(_ str: UnsafePointer<Int8>, _ pattern: UnsafePointer<Int8>) -> Int32 ``` |

Modified Tcl_SubstObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SubstObj(_ interp: UnsafePointer<Tcl_Interp>, _ objPtr: UnsafePointer<Tcl_Obj>, _ flags: Int32) -> UnsafePointer<Tcl_Obj> ``` |
| To | ``` func Tcl_SubstObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objPtr: UnsafeMutablePointer<Tcl_Obj>, _ flags: Int32) -> UnsafeMutablePointer<Tcl_Obj> ``` |

Modified Tcl_TakeBignumFromObj(UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_TakeBignumFromObj(_ interp: UnsafePointer<Tcl_Interp>, _ obj: UnsafePointer<Tcl_Obj>, _ value: UnsafePointer<mp_int>) -> Int32 ``` |
| To | ``` func Tcl_TakeBignumFromObj(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ obj: UnsafeMutablePointer<Tcl_Obj>, _ value: UnsafeMutablePointer<mp_int>) -> Int32 ``` |

Modified Tcl_TcpAcceptProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_TcpAcceptProc = ((ClientData, Tcl_Channel, UnsafePointer<Int8>, Int32) -> Void) ``` |
| To | ``` typealias Tcl_TcpAcceptProc = ((ClientData, Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Void) ``` |

Modified Tcl_ThreadQueueEvent(Tcl_ThreadId, UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ThreadQueueEvent(_ threadId: Tcl_ThreadId, _ evPtr: UnsafePointer<Tcl_Event>, _ position: Tcl_QueuePosition) ``` |
| To | ``` func Tcl_ThreadQueueEvent(_ threadId: Tcl_ThreadId, _ evPtr: UnsafeMutablePointer<Tcl_Event>, _ position: Tcl_QueuePosition) ``` |

Modified Tcl_TraceCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_TraceCommand(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_CommandTraceProc>, _ clientData: ClientData) -> Int32 ``` |
| To | ``` func Tcl_TraceCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_CommandTraceProc>, _ clientData: ClientData) -> Int32 ``` |

Modified Tcl_TraceVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_TraceVar(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) -> Int32 ``` |
| To | ``` func Tcl_TraceVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) -> Int32 ``` |

Modified Tcl_TraceVar2(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_TraceVar2(_ interp: UnsafePointer<Tcl_Interp>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) -> Int32 ``` |
| To | ``` func Tcl_TraceVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) -> Int32 ``` |

Modified Tcl_TranslateFileName(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_TranslateFileName(_ interp: UnsafePointer<Tcl_Interp>, _ name: ConstUnsafePointer<Int8>, _ bufferPtr: UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_TranslateFileName(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ bufferPtr: UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_Ungets(Tcl_Channel, UnsafePointer<Int8>, Int32, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Ungets(_ chan: Tcl_Channel, _ str: ConstUnsafePointer<Int8>, _ len: Int32, _ atHead: Int32) -> Int32 ``` |
| To | ``` func Tcl_Ungets(_ chan: Tcl_Channel, _ str: UnsafePointer<Int8>, _ len: Int32, _ atHead: Int32) -> Int32 ``` |

Modified Tcl_UniCharAtIndex(UnsafePointer<Int8>, Int32) -> Tcl_UniChar

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UniCharAtIndex(_ src: ConstUnsafePointer<Int8>, _ index: Int32) -> Tcl_UniChar ``` |
| To | ``` func Tcl_UniCharAtIndex(_ src: UnsafePointer<Int8>, _ index: Int32) -> Tcl_UniChar ``` |

Modified Tcl_UniCharCaseMatch(UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UniCharCaseMatch(_ uniStr: ConstUnsafePointer<Tcl_UniChar>, _ uniPattern: ConstUnsafePointer<Tcl_UniChar>, _ nocase: Int32) -> Int32 ``` |
| To | ``` func Tcl_UniCharCaseMatch(_ uniStr: UnsafePointer<Tcl_UniChar>, _ uniPattern: UnsafePointer<Tcl_UniChar>, _ nocase: Int32) -> Int32 ``` |

Modified Tcl_UniCharLen(UnsafePointer<Tcl_UniChar>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UniCharLen(_ uniStr: ConstUnsafePointer<Tcl_UniChar>) -> Int32 ``` |
| To | ``` func Tcl_UniCharLen(_ uniStr: UnsafePointer<Tcl_UniChar>) -> Int32 ``` |

Modified Tcl_UniCharNcasecmp(UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UniCharNcasecmp(_ ucs: ConstUnsafePointer<Tcl_UniChar>, _ uct: ConstUnsafePointer<Tcl_UniChar>, _ numChars: UInt) -> Int32 ``` |
| To | ``` func Tcl_UniCharNcasecmp(_ ucs: UnsafePointer<Tcl_UniChar>, _ uct: UnsafePointer<Tcl_UniChar>, _ numChars: UInt) -> Int32 ``` |

Modified Tcl_UniCharNcmp(UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UniCharNcmp(_ ucs: ConstUnsafePointer<Tcl_UniChar>, _ uct: ConstUnsafePointer<Tcl_UniChar>, _ numChars: UInt) -> Int32 ``` |
| To | ``` func Tcl_UniCharNcmp(_ ucs: UnsafePointer<Tcl_UniChar>, _ uct: UnsafePointer<Tcl_UniChar>, _ numChars: UInt) -> Int32 ``` |

Modified Tcl_UniCharToUtf(Int32, UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UniCharToUtf(_ ch: Int32, _ buf: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_UniCharToUtf(_ ch: Int32, _ buf: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified Tcl_UniCharToUtfDString(UnsafePointer<Tcl_UniChar>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UniCharToUtfDString(_ uniStr: ConstUnsafePointer<Tcl_UniChar>, _ uniLength: Int32, _ dsPtr: UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_UniCharToUtfDString(_ uniStr: UnsafePointer<Tcl_UniChar>, _ uniLength: Int32, _ dsPtr: UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_UnlinkVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UnlinkVar(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_UnlinkVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>) ``` |

Modified Tcl_UnregisterChannel(UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UnregisterChannel(_ interp: UnsafePointer<Tcl_Interp>, _ chan: Tcl_Channel) -> Int32 ``` |
| To | ``` func Tcl_UnregisterChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ chan: Tcl_Channel) -> Int32 ``` |

Modified Tcl_UnsetVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UnsetVar(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_UnsetVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_UnsetVar2(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UnsetVar2(_ interp: UnsafePointer<Tcl_Interp>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_UnsetVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_UnstackChannel(UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UnstackChannel(_ interp: UnsafePointer<Tcl_Interp>, _ chan: Tcl_Channel) -> Int32 ``` |
| To | ``` func Tcl_UnstackChannel(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ chan: Tcl_Channel) -> Int32 ``` |

Modified Tcl_UntraceCommand(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UntraceCommand(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_CommandTraceProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_UntraceCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_CommandTraceProc>, _ clientData: ClientData) ``` |

Modified Tcl_UntraceVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UntraceVar(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_UntraceVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) ``` |

Modified Tcl_UntraceVar2(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UntraceVar2(_ interp: UnsafePointer<Tcl_Interp>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_UntraceVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) ``` |

Modified Tcl_UpVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UpVar(_ interp: UnsafePointer<Tcl_Interp>, _ frameName: ConstUnsafePointer<Int8>, _ varName: ConstUnsafePointer<Int8>, _ localName: ConstUnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_UpVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ frameName: UnsafePointer<Int8>, _ varName: UnsafePointer<Int8>, _ localName: UnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_UpVar2(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UpVar2(_ interp: UnsafePointer<Tcl_Interp>, _ frameName: ConstUnsafePointer<Int8>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ localName: ConstUnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_UpVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ frameName: UnsafePointer<Int8>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ localName: UnsafePointer<Int8>, _ flags: Int32) -> Int32 ``` |

Modified Tcl_UpdateLinkedVar(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UpdateLinkedVar(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_UpdateLinkedVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>) ``` |

Modified Tcl_UpdateStringProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_UpdateStringProc = ((UnsafePointer<Tcl_Obj>) -> Void) ``` |
| To | ``` typealias Tcl_UpdateStringProc = ((UnsafeMutablePointer<Tcl_Obj>) -> Void) ``` |

Modified Tcl_UtfAtIndex(UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfAtIndex(_ src: ConstUnsafePointer<Int8>, _ index: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_UtfAtIndex(_ src: UnsafePointer<Int8>, _ index: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_UtfBackslash(UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfBackslash(_ src: ConstUnsafePointer<Int8>, _ readPtr: UnsafePointer<Int32>, _ dst: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_UtfBackslash(_ src: UnsafePointer<Int8>, _ readPtr: UnsafeMutablePointer<Int32>, _ dst: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified Tcl_UtfCharComplete(UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfCharComplete(_ src: ConstUnsafePointer<Int8>, _ length: Int32) -> Int32 ``` |
| To | ``` func Tcl_UtfCharComplete(_ src: UnsafePointer<Int8>, _ length: Int32) -> Int32 ``` |

Modified Tcl_UtfFindFirst(UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfFindFirst(_ src: ConstUnsafePointer<Int8>, _ ch: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_UtfFindFirst(_ src: UnsafePointer<Int8>, _ ch: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_UtfFindLast(UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfFindLast(_ src: ConstUnsafePointer<Int8>, _ ch: Int32) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_UtfFindLast(_ src: UnsafePointer<Int8>, _ ch: Int32) -> UnsafePointer<Int8> ``` |

Modified Tcl_UtfNcasecmp(UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfNcasecmp(_ s1: ConstUnsafePointer<Int8>, _ s2: ConstUnsafePointer<Int8>, _ n: UInt) -> Int32 ``` |
| To | ``` func Tcl_UtfNcasecmp(_ s1: UnsafePointer<Int8>, _ s2: UnsafePointer<Int8>, _ n: UInt) -> Int32 ``` |

Modified Tcl_UtfNcmp(UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfNcmp(_ s1: ConstUnsafePointer<Int8>, _ s2: ConstUnsafePointer<Int8>, _ n: UInt) -> Int32 ``` |
| To | ``` func Tcl_UtfNcmp(_ s1: UnsafePointer<Int8>, _ s2: UnsafePointer<Int8>, _ n: UInt) -> Int32 ``` |

Modified Tcl_UtfNext(UnsafePointer<Int8>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfNext(_ src: ConstUnsafePointer<Int8>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_UtfNext(_ src: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |

Modified Tcl_UtfPrev(UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfPrev(_ src: ConstUnsafePointer<Int8>, _ start: ConstUnsafePointer<Int8>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Tcl_UtfPrev(_ src: UnsafePointer<Int8>, _ start: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |

Modified Tcl_UtfToExternal(UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfToExternal(_ interp: UnsafePointer<Tcl_Interp>, _ encoding: Tcl_Encoding, _ src: ConstUnsafePointer<Int8>, _ srcLen: Int32, _ flags: Int32, _ statePtr: UnsafePointer<Tcl_EncodingState>, _ dst: UnsafePointer<Int8>, _ dstLen: Int32, _ srcReadPtr: UnsafePointer<Int32>, _ dstWrotePtr: UnsafePointer<Int32>, _ dstCharsPtr: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func Tcl_UtfToExternal(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ encoding: Tcl_Encoding, _ src: UnsafePointer<Int8>, _ srcLen: Int32, _ flags: Int32, _ statePtr: UnsafeMutablePointer<Tcl_EncodingState>, _ dst: UnsafeMutablePointer<Int8>, _ dstLen: Int32, _ srcReadPtr: UnsafeMutablePointer<Int32>, _ dstWrotePtr: UnsafeMutablePointer<Int32>, _ dstCharsPtr: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified Tcl_UtfToExternalDString(Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfToExternalDString(_ encoding: Tcl_Encoding, _ src: ConstUnsafePointer<Int8>, _ srcLen: Int32, _ dsPtr: UnsafePointer<Tcl_DString>) -> UnsafePointer<Int8> ``` |
| To | ``` func Tcl_UtfToExternalDString(_ encoding: Tcl_Encoding, _ src: UnsafePointer<Int8>, _ srcLen: Int32, _ dsPtr: UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8> ``` |

Modified Tcl_UtfToLower(UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfToLower(_ src: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_UtfToLower(_ src: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified Tcl_UtfToTitle(UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfToTitle(_ src: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_UtfToTitle(_ src: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified Tcl_UtfToUniChar(UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_UniChar>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfToUniChar(_ src: ConstUnsafePointer<Int8>, _ chPtr: UnsafePointer<Tcl_UniChar>) -> Int32 ``` |
| To | ``` func Tcl_UtfToUniChar(_ src: UnsafePointer<Int8>, _ chPtr: UnsafeMutablePointer<Tcl_UniChar>) -> Int32 ``` |

Modified Tcl_UtfToUniCharDString(UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Tcl_UniChar>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfToUniCharDString(_ src: ConstUnsafePointer<Int8>, _ length: Int32, _ dsPtr: UnsafePointer<Tcl_DString>) -> UnsafePointer<Tcl_UniChar> ``` |
| To | ``` func Tcl_UtfToUniCharDString(_ src: UnsafePointer<Int8>, _ length: Int32, _ dsPtr: UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Tcl_UniChar> ``` |

Modified Tcl_UtfToUpper(UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UtfToUpper(_ src: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Tcl_UtfToUpper(_ src: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified Tcl_ValidateAllMemory(UnsafePointer<Int8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ValidateAllMemory(_ file: ConstUnsafePointer<Int8>, _ line: Int32) ``` |
| To | ``` func Tcl_ValidateAllMemory(_ file: UnsafePointer<Int8>, _ line: Int32) ``` |

Modified Tcl_VarEvalVA(UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_VarEvalVA(_ interp: UnsafePointer<Tcl_Interp>, _ argList: CVaListPointer) -> Int32 ``` |
| To | ``` func Tcl_VarEvalVA(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ argList: CVaListPointer) -> Int32 ``` |

Modified Tcl_VarTraceInfo(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_VarTraceInfo(_ interp: UnsafePointer<Tcl_Interp>, _ varName: ConstUnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_VarTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |
| To | ``` func Tcl_VarTraceInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_VarTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |

Modified Tcl_VarTraceInfo2(UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_VarTraceInfo2(_ interp: UnsafePointer<Tcl_Interp>, _ part1: ConstUnsafePointer<Int8>, _ part2: ConstUnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_VarTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |
| To | ``` func Tcl_VarTraceInfo2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_VarTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |

Modified Tcl_VarTraceProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_VarTraceProc = ((ClientData, UnsafePointer<Tcl_Interp>, ConstUnsafePointer<Int8>, ConstUnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>) ``` |
| To | ``` typealias Tcl_VarTraceProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>) ``` |

Modified Tcl_WaitForEvent(UnsafeMutablePointer<Tcl_Time>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_WaitForEvent(_ timePtr: UnsafePointer<Tcl_Time>) -> Int32 ``` |
| To | ``` func Tcl_WaitForEvent(_ timePtr: UnsafeMutablePointer<Tcl_Time>) -> Int32 ``` |

Modified Tcl_WaitForEventProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_WaitForEventProc = ((UnsafePointer<Tcl_Time>) -> Int32) ``` |
| To | ``` typealias Tcl_WaitForEventProc = ((UnsafeMutablePointer<Tcl_Time>) -> Int32) ``` |

Modified Tcl_WaitPid(Tcl_Pid, UnsafeMutablePointer<Int32>, Int32) -> Tcl_Pid

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_WaitPid(_ pid: Tcl_Pid, _ statPtr: UnsafePointer<Int32>, _ options: Int32) -> Tcl_Pid ``` |
| To | ``` func Tcl_WaitPid(_ pid: Tcl_Pid, _ statPtr: UnsafeMutablePointer<Int32>, _ options: Int32) -> Tcl_Pid ``` |

Modified Tcl_Write(Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Write(_ chan: Tcl_Channel, _ s: ConstUnsafePointer<Int8>, _ slen: Int32) -> Int32 ``` |
| To | ``` func Tcl_Write(_ chan: Tcl_Channel, _ s: UnsafePointer<Int8>, _ slen: Int32) -> Int32 ``` |

Modified Tcl_WriteChars(Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_WriteChars(_ chan: Tcl_Channel, _ src: ConstUnsafePointer<Int8>, _ srcLen: Int32) -> Int32 ``` |
| To | ``` func Tcl_WriteChars(_ chan: Tcl_Channel, _ src: UnsafePointer<Int8>, _ srcLen: Int32) -> Int32 ``` |

Modified Tcl_WriteObj(Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_WriteObj(_ chan: Tcl_Channel, _ objPtr: UnsafePointer<Tcl_Obj>) -> Int32 ``` |
| To | ``` func Tcl_WriteObj(_ chan: Tcl_Channel, _ objPtr: UnsafeMutablePointer<Tcl_Obj>) -> Int32 ``` |

Modified Tcl_WriteRaw(Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_WriteRaw(_ chan: Tcl_Channel, _ src: ConstUnsafePointer<Int8>, _ srcLen: Int32) -> Int32 ``` |
| To | ``` func Tcl_WriteRaw(_ chan: Tcl_Channel, _ src: UnsafePointer<Int8>, _ srcLen: Int32) -> Int32 ``` |

Modified Tcl_WrongNumArgs(UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_WrongNumArgs(_ interp: UnsafePointer<Tcl_Interp>, _ objc: Int32, _ objv: ConstUnsafePointer<UnsafePointer<Tcl_Obj>>, _ message: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Tcl_WrongNumArgs(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ objc: Int32, _ objv: UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, _ message: UnsafePointer<Int8>) ``` |

Modified tclPlatStubsPtr

|  | Declaration |
| --- | --- |
| From | ``` var tclPlatStubsPtr: UnsafePointer<TclPlatStubs> ``` |
| To | ``` var tclPlatStubsPtr: UnsafeMutablePointer<TclPlatStubs> ``` |

Modified tclStubsPtr

|  | Declaration |
| --- | --- |
| From | ``` var tclStubsPtr: UnsafePointer<TclStubs> ``` |
| To | ``` var tclStubsPtr: UnsafeMutablePointer<TclStubs> ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

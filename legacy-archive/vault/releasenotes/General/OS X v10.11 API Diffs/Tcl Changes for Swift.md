---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/Tcl.html
archived_at: '2026-07-18T02:53:46.479353Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Tcl Changes for Swift

### Tcl

Removed Tcl_ChannelType.init(typeName: UnsafeMutablePointer<Int8>, version: Tcl_ChannelTypeVersion, closeProc: CFunctionPointer<Tcl_DriverCloseProc>, inputProc: CFunctionPointer<Tcl_DriverInputProc>, outputProc: CFunctionPointer<Tcl_DriverOutputProc>, seekProc: CFunctionPointer<Tcl_DriverSeekProc>, setOptionProc: CFunctionPointer<Tcl_DriverSetOptionProc>, getOptionProc: CFunctionPointer<Tcl_DriverGetOptionProc>, watchProc: CFunctionPointer<Tcl_DriverWatchProc>, getHandleProc: CFunctionPointer<Tcl_DriverGetHandleProc>, close2Proc: CFunctionPointer<Tcl_DriverClose2Proc>, blockModeProc: CFunctionPointer<Tcl_DriverBlockModeProc>, flushProc: CFunctionPointer<Tcl_DriverFlushProc>, handlerProc: CFunctionPointer<Tcl_DriverHandlerProc>, wideSeekProc: CFunctionPointer<Tcl_DriverWideSeekProc>, threadActionProc: CFunctionPointer<Tcl_DriverThreadActionProc>, truncateProc: CFunctionPointer<Tcl_DriverTruncateProc>)Removed Tcl_CmdInfo.init(isNativeObjectProc: Int32, objProc: CFunctionPointer<Tcl_ObjCmdProc>, objClientData: ClientData, proc: CFunctionPointer<Tcl_CmdProc>, clientData: ClientData, deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>, deleteData: ClientData, namespacePtr: UnsafeMutablePointer<Tcl_Namespace>)Removed Tcl_EncodingType.init(encodingName: UnsafePointer<Int8>, toUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>, fromUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>, freeProc: CFunctionPointer<Tcl_EncodingFreeProc>, clientData: ClientData, nullSize: Int32)Removed Tcl_Event.init(proc: CFunctionPointer<Tcl_EventProc>, nextPtr: UnsafeMutablePointer<Tcl_Event>)Removed Tcl_Filesystem.init(typeName: UnsafePointer<Int8>, structureLength: Int32, version: Tcl_FSVersion, pathInFilesystemProc: CFunctionPointer<Tcl_FSPathInFilesystemProc>, dupInternalRepProc: CFunctionPointer<Tcl_FSDupInternalRepProc>, freeInternalRepProc: CFunctionPointer<Tcl_FSFreeInternalRepProc>, internalToNormalizedProc: CFunctionPointer<Tcl_FSInternalToNormalizedProc>, createInternalRepProc: CFunctionPointer<Tcl_FSCreateInternalRepProc>, normalizePathProc: CFunctionPointer<Tcl_FSNormalizePathProc>, filesystemPathTypeProc: CFunctionPointer<Tcl_FSFilesystemPathTypeProc>, filesystemSeparatorProc: CFunctionPointer<Tcl_FSFilesystemSeparatorProc>, statProc: CFunctionPointer<Tcl_FSStatProc>, accessProc: CFunctionPointer<Tcl_FSAccessProc>, openFileChannelProc: CFunctionPointer<Tcl_FSOpenFileChannelProc>, matchInDirectoryProc: CFunctionPointer<Tcl_FSMatchInDirectoryProc>, utimeProc: CFunctionPointer<Tcl_FSUtimeProc>, linkProc: CFunctionPointer<Tcl_FSLinkProc>, listVolumesProc: CFunctionPointer<Tcl_FSListVolumesProc>, fileAttrStringsProc: CFunctionPointer<Tcl_FSFileAttrStringsProc>, fileAttrsGetProc: CFunctionPointer<Tcl_FSFileAttrsGetProc>, fileAttrsSetProc: CFunctionPointer<Tcl_FSFileAttrsSetProc>, createDirectoryProc: CFunctionPointer<Tcl_FSCreateDirectoryProc>, removeDirectoryProc: CFunctionPointer<Tcl_FSRemoveDirectoryProc>, deleteFileProc: CFunctionPointer<Tcl_FSDeleteFileProc>, copyFileProc: CFunctionPointer<Tcl_FSCopyFileProc>, renameFileProc: CFunctionPointer<Tcl_FSRenameFileProc>, copyDirectoryProc: CFunctionPointer<Tcl_FSCopyDirectoryProc>, lstatProc: CFunctionPointer<Tcl_FSLstatProc>, loadFileProc: CFunctionPointer<Tcl_FSLoadFileProc>, getCwdProc: CFunctionPointer<Tcl_FSGetCwdProc>, chdirProc: CFunctionPointer<Tcl_FSChdirProc>)Removed Tcl_HashKeyType.init(version: Int32, flags: Int32, hashKeyProc: CFunctionPointer<Tcl_HashKeyProc>, compareKeysProc: CFunctionPointer<Tcl_CompareHashKeysProc>, allocEntryProc: CFunctionPointer<Tcl_AllocHashEntryProc>, freeEntryProc: CFunctionPointer<Tcl_FreeHashEntryProc>)Removed Tcl_HashTable.init(buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>, staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>), numBuckets: Int32, numEntries: Int32, rebuildSize: Int32, downShift: Int32, mask: Int32, keyType: Int32, findProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)>, createProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)>, typePtr: UnsafeMutablePointer<Tcl_HashKeyType>)Removed Tcl_Interp.init(result: UnsafeMutablePointer<Int8>, freeProc: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)>, errorLine: Int32)Removed Tcl_Namespace.init(name: UnsafeMutablePointer<Int8>, fullName: UnsafeMutablePointer<Int8>, clientData: ClientData, deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>, parentPtr: UnsafeMutablePointer<Tcl_Namespace>)Removed Tcl_NotifierProcs.init(setTimerProc: CFunctionPointer<Tcl_SetTimerProc>, waitForEventProc: CFunctionPointer<Tcl_WaitForEventProc>, createFileHandlerProc: CFunctionPointer<Tcl_CreateFileHandlerProc>, deleteFileHandlerProc: CFunctionPointer<Tcl_DeleteFileHandlerProc>, initNotifierProc: CFunctionPointer<Tcl_InitNotifierProc>, finalizeNotifierProc: CFunctionPointer<Tcl_FinalizeNotifierProc>, alertNotifierProc: CFunctionPointer<Tcl_AlertNotifierProc>, serviceModeHookProc: CFunctionPointer<Tcl_ServiceModeHookProc>)Removed Tcl_ObjType.init(name: UnsafeMutablePointer<Int8>, freeIntRepProc: CFunctionPointer<Tcl_FreeInternalRepProc>, dupIntRepProc: CFunctionPointer<Tcl_DupInternalRepProc>, updateStringProc: CFunctionPointer<Tcl_UpdateStringProc>, setFromAnyProc: CFunctionPointer<Tcl_SetFromAnyProc>)Removed Tcl_PathType.valueRemoved Tcl_QueuePosition.valueRemoved Tcl_SavedResult.init(result: UnsafeMutablePointer<Int8>, freeProc: CFunctionPointer<Tcl_FreeProc>, objResultPtr: UnsafeMutablePointer<Tcl_Obj>, appendResult: UnsafeMutablePointer<Int8>, appendAvl: Int32, appendUsed: Int32, resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Removed Tcl_ValueType.valueAdded Tcl_ChannelType.init(typeName: UnsafeMutablePointer<Int8>, version: Tcl_ChannelTypeVersion, closeProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, inputProc: ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, outputProc: ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, seekProc: ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, setOptionProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, getOptionProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!, watchProc: ((ClientData, Int32) -> Void)!, getHandleProc: ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!, close2Proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, blockModeProc: ((ClientData, Int32) -> Int32)!, flushProc: ((ClientData) -> Int32)!, handlerProc: ((ClientData, Int32) -> Int32)!, wideSeekProc: ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)!, threadActionProc: ((ClientData, Int32) -> Void)!, truncateProc: ((ClientData, Tcl_WideInt) -> Int32)!)Added Tcl_CmdInfo.init(isNativeObjectProc: Int32, objProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, objClientData: ClientData, proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, clientData: ClientData, deleteProc: ((ClientData) -> Void)!, deleteData: ClientData, namespacePtr: UnsafeMutablePointer<Tcl_Namespace>)Added Tcl_EncodingType.init(encodingName: UnsafePointer<Int8>, toUtfProc: ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!, fromUtfProc: ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!, freeProc: ((ClientData) -> Void)!, clientData: ClientData, nullSize: Int32)Added Tcl_Event.init(proc: ((UnsafeMutablePointer<Tcl_Event>, Int32) -> Int32)!, nextPtr: UnsafeMutablePointer<Tcl_Event>)Added Tcl_Filesystem.init(typeName: UnsafePointer<Int8>, structureLength: Int32, version: Tcl_FSVersion, pathInFilesystemProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<ClientData>) -> Int32)!, dupInternalRepProc: ((ClientData) -> ClientData)!, freeInternalRepProc: ((ClientData) -> Void)!, internalToNormalizedProc: ((ClientData) -> UnsafeMutablePointer<Tcl_Obj>)!, createInternalRepProc: ((UnsafeMutablePointer<Tcl_Obj>) -> ClientData)!, normalizePathProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!, filesystemPathTypeProc: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, filesystemSeparatorProc: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, statProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!, accessProc: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!, openFileChannelProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Tcl_Channel)!, matchInDirectoryProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)!, utimeProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)!, linkProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, listVolumesProc: (() -> UnsafeMutablePointer<Tcl_Obj>)!, fileAttrStringsProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)!, fileAttrsGetProc: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, fileAttrsSetProc: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, createDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, removeDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, deleteFileProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, copyFileProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, renameFileProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, copyDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, lstatProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!, loadFileProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32)!, getCwdProc: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)!, chdirProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!)Added Tcl_HashKeyType.init(version: Int32, flags: Int32, hashKeyProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UInt32)!, compareKeysProc: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Tcl_HashEntry>) -> Int32)!, allocEntryProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, freeEntryProc: ((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)!)Added Tcl_HashTable.init(buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>, staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>), numBuckets: Int32, numEntries: Int32, rebuildSize: Int32, downShift: Int32, mask: Int32, keyType: Int32, findProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, createProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, typePtr: UnsafeMutablePointer<Tcl_HashKeyType>)Added Tcl_Interp.init(result: UnsafeMutablePointer<Int8>, freeProc: ((UnsafeMutablePointer<Int8>) -> Void)!, errorLine: Int32)Added Tcl_Namespace.init(name: UnsafeMutablePointer<Int8>, fullName: UnsafeMutablePointer<Int8>, clientData: ClientData, deleteProc: ((ClientData) -> Void)!, parentPtr: UnsafeMutablePointer<Tcl_Namespace>)Added Tcl_NotifierProcs.init(setTimerProc: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!, waitForEventProc: ((UnsafeMutablePointer<Tcl_Time>) -> Int32)!, createFileHandlerProc: ((Int32, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!, deleteFileHandlerProc: ((Int32) -> Void)!, initNotifierProc: (() -> ClientData)!, finalizeNotifierProc: ((ClientData) -> Void)!, alertNotifierProc: ((ClientData) -> Void)!, serviceModeHookProc: ((Int32) -> Void)!)Added Tcl_ObjType.init(name: UnsafeMutablePointer<Int8>, freeIntRepProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!, dupIntRepProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, updateStringProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!, setFromAnyProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!)Added Tcl_PathType.init(rawValue: UInt32)Added Tcl_PathType.rawValueAdded Tcl_QueuePosition.init(rawValue: UInt32)Added Tcl_QueuePosition.rawValueAdded Tcl_SavedResult.init(result: UnsafeMutablePointer<Int8>, freeProc: ((UnsafeMutablePointer<Int8>) -> Void)!, objResultPtr: UnsafeMutablePointer<Tcl_Obj>, appendResult: UnsafeMutablePointer<Int8>, appendAvl: Int32, appendUsed: Int32, resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added Tcl_ValueType.init(rawValue: UInt32)Added Tcl_ValueType.rawValueModified Tcl_ChannelType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_ChannelType {     var typeName: UnsafeMutablePointer<Int8>     var version: Tcl_ChannelTypeVersion     var closeProc: CFunctionPointer<Tcl_DriverCloseProc>     var inputProc: CFunctionPointer<Tcl_DriverInputProc>     var outputProc: CFunctionPointer<Tcl_DriverOutputProc>     var seekProc: CFunctionPointer<Tcl_DriverSeekProc>     var setOptionProc: CFunctionPointer<Tcl_DriverSetOptionProc>     var getOptionProc: CFunctionPointer<Tcl_DriverGetOptionProc>     var watchProc: CFunctionPointer<Tcl_DriverWatchProc>     var getHandleProc: CFunctionPointer<Tcl_DriverGetHandleProc>     var close2Proc: CFunctionPointer<Tcl_DriverClose2Proc>     var blockModeProc: CFunctionPointer<Tcl_DriverBlockModeProc>     var flushProc: CFunctionPointer<Tcl_DriverFlushProc>     var handlerProc: CFunctionPointer<Tcl_DriverHandlerProc>     var wideSeekProc: CFunctionPointer<Tcl_DriverWideSeekProc>     var threadActionProc: CFunctionPointer<Tcl_DriverThreadActionProc>     var truncateProc: CFunctionPointer<Tcl_DriverTruncateProc>     init()     init(typeName typeName: UnsafeMutablePointer<Int8>, version version: Tcl_ChannelTypeVersion, closeProc closeProc: CFunctionPointer<Tcl_DriverCloseProc>, inputProc inputProc: CFunctionPointer<Tcl_DriverInputProc>, outputProc outputProc: CFunctionPointer<Tcl_DriverOutputProc>, seekProc seekProc: CFunctionPointer<Tcl_DriverSeekProc>, setOptionProc setOptionProc: CFunctionPointer<Tcl_DriverSetOptionProc>, getOptionProc getOptionProc: CFunctionPointer<Tcl_DriverGetOptionProc>, watchProc watchProc: CFunctionPointer<Tcl_DriverWatchProc>, getHandleProc getHandleProc: CFunctionPointer<Tcl_DriverGetHandleProc>, close2Proc close2Proc: CFunctionPointer<Tcl_DriverClose2Proc>, blockModeProc blockModeProc: CFunctionPointer<Tcl_DriverBlockModeProc>, flushProc flushProc: CFunctionPointer<Tcl_DriverFlushProc>, handlerProc handlerProc: CFunctionPointer<Tcl_DriverHandlerProc>, wideSeekProc wideSeekProc: CFunctionPointer<Tcl_DriverWideSeekProc>, threadActionProc threadActionProc: CFunctionPointer<Tcl_DriverThreadActionProc>, truncateProc truncateProc: CFunctionPointer<Tcl_DriverTruncateProc>) } ``` |
| To | ``` struct Tcl_ChannelType {     var typeName: UnsafeMutablePointer<Int8>     var version: Tcl_ChannelTypeVersion     var closeProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var inputProc: ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!     var outputProc: ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!     var seekProc: ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)!     var setOptionProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var getOptionProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!     var watchProc: ((ClientData, Int32) -> Void)!     var getHandleProc: ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!     var close2Proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!     var blockModeProc: ((ClientData, Int32) -> Int32)!     var flushProc: ((ClientData) -> Int32)!     var handlerProc: ((ClientData, Int32) -> Int32)!     var wideSeekProc: ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)!     var threadActionProc: ((ClientData, Int32) -> Void)!     var truncateProc: ((ClientData, Tcl_WideInt) -> Int32)!     init()     init(typeName typeName: UnsafeMutablePointer<Int8>, version version: Tcl_ChannelTypeVersion, closeProc closeProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, inputProc inputProc: ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, outputProc outputProc: ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, seekProc seekProc: ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, setOptionProc setOptionProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, getOptionProc getOptionProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!, watchProc watchProc: ((ClientData, Int32) -> Void)!, getHandleProc getHandleProc: ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!, close2Proc close2Proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, blockModeProc blockModeProc: ((ClientData, Int32) -> Int32)!, flushProc flushProc: ((ClientData) -> Int32)!, handlerProc handlerProc: ((ClientData, Int32) -> Int32)!, wideSeekProc wideSeekProc: ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)!, threadActionProc threadActionProc: ((ClientData, Int32) -> Void)!, truncateProc truncateProc: ((ClientData, Tcl_WideInt) -> Int32)!) } ``` |

Modified Tcl_ChannelType.blockModeProc

|  | Declaration |
| --- | --- |
| From | ``` var blockModeProc: CFunctionPointer<Tcl_DriverBlockModeProc> ``` |
| To | ``` var blockModeProc: ((ClientData, Int32) -> Int32)! ``` |

Modified Tcl_ChannelType.close2Proc

|  | Declaration |
| --- | --- |
| From | ``` var close2Proc: CFunctionPointer<Tcl_DriverClose2Proc> ``` |
| To | ``` var close2Proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)! ``` |

Modified Tcl_ChannelType.closeProc

|  | Declaration |
| --- | --- |
| From | ``` var closeProc: CFunctionPointer<Tcl_DriverCloseProc> ``` |
| To | ``` var closeProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified Tcl_ChannelType.flushProc

|  | Declaration |
| --- | --- |
| From | ``` var flushProc: CFunctionPointer<Tcl_DriverFlushProc> ``` |
| To | ``` var flushProc: ((ClientData) -> Int32)! ``` |

Modified Tcl_ChannelType.getHandleProc

|  | Declaration |
| --- | --- |
| From | ``` var getHandleProc: CFunctionPointer<Tcl_DriverGetHandleProc> ``` |
| To | ``` var getHandleProc: ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)! ``` |

Modified Tcl_ChannelType.getOptionProc

|  | Declaration |
| --- | --- |
| From | ``` var getOptionProc: CFunctionPointer<Tcl_DriverGetOptionProc> ``` |
| To | ``` var getOptionProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)! ``` |

Modified Tcl_ChannelType.handlerProc

|  | Declaration |
| --- | --- |
| From | ``` var handlerProc: CFunctionPointer<Tcl_DriverHandlerProc> ``` |
| To | ``` var handlerProc: ((ClientData, Int32) -> Int32)! ``` |

Modified Tcl_ChannelType.inputProc

|  | Declaration |
| --- | --- |
| From | ``` var inputProc: CFunctionPointer<Tcl_DriverInputProc> ``` |
| To | ``` var inputProc: ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified Tcl_ChannelType.outputProc

|  | Declaration |
| --- | --- |
| From | ``` var outputProc: CFunctionPointer<Tcl_DriverOutputProc> ``` |
| To | ``` var outputProc: ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified Tcl_ChannelType.seekProc

|  | Declaration |
| --- | --- |
| From | ``` var seekProc: CFunctionPointer<Tcl_DriverSeekProc> ``` |
| To | ``` var seekProc: ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified Tcl_ChannelType.setOptionProc

|  | Declaration |
| --- | --- |
| From | ``` var setOptionProc: CFunctionPointer<Tcl_DriverSetOptionProc> ``` |
| To | ``` var setOptionProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified Tcl_ChannelType.threadActionProc

|  | Declaration |
| --- | --- |
| From | ``` var threadActionProc: CFunctionPointer<Tcl_DriverThreadActionProc> ``` |
| To | ``` var threadActionProc: ((ClientData, Int32) -> Void)! ``` |

Modified Tcl_ChannelType.truncateProc

|  | Declaration |
| --- | --- |
| From | ``` var truncateProc: CFunctionPointer<Tcl_DriverTruncateProc> ``` |
| To | ``` var truncateProc: ((ClientData, Tcl_WideInt) -> Int32)! ``` |

Modified Tcl_ChannelType.watchProc

|  | Declaration |
| --- | --- |
| From | ``` var watchProc: CFunctionPointer<Tcl_DriverWatchProc> ``` |
| To | ``` var watchProc: ((ClientData, Int32) -> Void)! ``` |

Modified Tcl_ChannelType.wideSeekProc

|  | Declaration |
| --- | --- |
| From | ``` var wideSeekProc: CFunctionPointer<Tcl_DriverWideSeekProc> ``` |
| To | ``` var wideSeekProc: ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)! ``` |

Modified Tcl_CmdInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_CmdInfo {     var isNativeObjectProc: Int32     var objProc: CFunctionPointer<Tcl_ObjCmdProc>     var objClientData: ClientData     var proc: CFunctionPointer<Tcl_CmdProc>     var clientData: ClientData     var deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>     var deleteData: ClientData     var namespacePtr: UnsafeMutablePointer<Tcl_Namespace>     init()     init(isNativeObjectProc isNativeObjectProc: Int32, objProc objProc: CFunctionPointer<Tcl_ObjCmdProc>, objClientData objClientData: ClientData, proc proc: CFunctionPointer<Tcl_CmdProc>, clientData clientData: ClientData, deleteProc deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>, deleteData deleteData: ClientData, namespacePtr namespacePtr: UnsafeMutablePointer<Tcl_Namespace>) } ``` |
| To | ``` struct Tcl_CmdInfo {     var isNativeObjectProc: Int32     var objProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var objClientData: ClientData     var proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!     var clientData: ClientData     var deleteProc: ((ClientData) -> Void)!     var deleteData: ClientData     var namespacePtr: UnsafeMutablePointer<Tcl_Namespace>     init()     init(isNativeObjectProc isNativeObjectProc: Int32, objProc objProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, objClientData objClientData: ClientData, proc proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, clientData clientData: ClientData, deleteProc deleteProc: ((ClientData) -> Void)!, deleteData deleteData: ClientData, namespacePtr namespacePtr: UnsafeMutablePointer<Tcl_Namespace>) } ``` |

Modified Tcl_CmdInfo.deleteProc

|  | Declaration |
| --- | --- |
| From | ``` var deleteProc: CFunctionPointer<Tcl_CmdDeleteProc> ``` |
| To | ``` var deleteProc: ((ClientData) -> Void)! ``` |

Modified Tcl_CmdInfo.objProc

|  | Declaration |
| --- | --- |
| From | ``` var objProc: CFunctionPointer<Tcl_ObjCmdProc> ``` |
| To | ``` var objProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified Tcl_CmdInfo.proc

|  | Declaration |
| --- | --- |
| From | ``` var proc: CFunctionPointer<Tcl_CmdProc> ``` |
| To | ``` var proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)! ``` |

Modified Tcl_EncodingType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_EncodingType {     var encodingName: UnsafePointer<Int8>     var toUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>     var fromUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>     var freeProc: CFunctionPointer<Tcl_EncodingFreeProc>     var clientData: ClientData     var nullSize: Int32     init()     init(encodingName encodingName: UnsafePointer<Int8>, toUtfProc toUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>, fromUtfProc fromUtfProc: CFunctionPointer<Tcl_EncodingConvertProc>, freeProc freeProc: CFunctionPointer<Tcl_EncodingFreeProc>, clientData clientData: ClientData, nullSize nullSize: Int32) } ``` |
| To | ``` struct Tcl_EncodingType {     var encodingName: UnsafePointer<Int8>     var toUtfProc: ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!     var fromUtfProc: ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!     var freeProc: ((ClientData) -> Void)!     var clientData: ClientData     var nullSize: Int32     init()     init(encodingName encodingName: UnsafePointer<Int8>, toUtfProc toUtfProc: ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!, fromUtfProc fromUtfProc: ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!, freeProc freeProc: ((ClientData) -> Void)!, clientData clientData: ClientData, nullSize nullSize: Int32) } ``` |

Modified Tcl_EncodingType.freeProc

|  | Declaration |
| --- | --- |
| From | ``` var freeProc: CFunctionPointer<Tcl_EncodingFreeProc> ``` |
| To | ``` var freeProc: ((ClientData) -> Void)! ``` |

Modified Tcl_EncodingType.fromUtfProc

|  | Declaration |
| --- | --- |
| From | ``` var fromUtfProc: CFunctionPointer<Tcl_EncodingConvertProc> ``` |
| To | ``` var fromUtfProc: ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified Tcl_EncodingType.toUtfProc

|  | Declaration |
| --- | --- |
| From | ``` var toUtfProc: CFunctionPointer<Tcl_EncodingConvertProc> ``` |
| To | ``` var toUtfProc: ((ClientData, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified Tcl_Event [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Event {     var proc: CFunctionPointer<Tcl_EventProc>     var nextPtr: UnsafeMutablePointer<Tcl_Event>     init()     init(proc proc: CFunctionPointer<Tcl_EventProc>, nextPtr nextPtr: UnsafeMutablePointer<Tcl_Event>) } ``` |
| To | ``` struct Tcl_Event {     var proc: ((UnsafeMutablePointer<Tcl_Event>, Int32) -> Int32)!     var nextPtr: UnsafeMutablePointer<Tcl_Event>     init()     init(proc proc: ((UnsafeMutablePointer<Tcl_Event>, Int32) -> Int32)!, nextPtr nextPtr: UnsafeMutablePointer<Tcl_Event>) } ``` |

Modified Tcl_Event.proc

|  | Declaration |
| --- | --- |
| From | ``` var proc: CFunctionPointer<Tcl_EventProc> ``` |
| To | ``` var proc: ((UnsafeMutablePointer<Tcl_Event>, Int32) -> Int32)! ``` |

Modified Tcl_Filesystem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Filesystem {     var typeName: UnsafePointer<Int8>     var structureLength: Int32     var version: Tcl_FSVersion     var pathInFilesystemProc: CFunctionPointer<Tcl_FSPathInFilesystemProc>     var dupInternalRepProc: CFunctionPointer<Tcl_FSDupInternalRepProc>     var freeInternalRepProc: CFunctionPointer<Tcl_FSFreeInternalRepProc>     var internalToNormalizedProc: CFunctionPointer<Tcl_FSInternalToNormalizedProc>     var createInternalRepProc: CFunctionPointer<Tcl_FSCreateInternalRepProc>     var normalizePathProc: CFunctionPointer<Tcl_FSNormalizePathProc>     var filesystemPathTypeProc: CFunctionPointer<Tcl_FSFilesystemPathTypeProc>     var filesystemSeparatorProc: CFunctionPointer<Tcl_FSFilesystemSeparatorProc>     var statProc: CFunctionPointer<Tcl_FSStatProc>     var accessProc: CFunctionPointer<Tcl_FSAccessProc>     var openFileChannelProc: CFunctionPointer<Tcl_FSOpenFileChannelProc>     var matchInDirectoryProc: CFunctionPointer<Tcl_FSMatchInDirectoryProc>     var utimeProc: CFunctionPointer<Tcl_FSUtimeProc>     var linkProc: CFunctionPointer<Tcl_FSLinkProc>     var listVolumesProc: CFunctionPointer<Tcl_FSListVolumesProc>     var fileAttrStringsProc: CFunctionPointer<Tcl_FSFileAttrStringsProc>     var fileAttrsGetProc: CFunctionPointer<Tcl_FSFileAttrsGetProc>     var fileAttrsSetProc: CFunctionPointer<Tcl_FSFileAttrsSetProc>     var createDirectoryProc: CFunctionPointer<Tcl_FSCreateDirectoryProc>     var removeDirectoryProc: CFunctionPointer<Tcl_FSRemoveDirectoryProc>     var deleteFileProc: CFunctionPointer<Tcl_FSDeleteFileProc>     var copyFileProc: CFunctionPointer<Tcl_FSCopyFileProc>     var renameFileProc: CFunctionPointer<Tcl_FSRenameFileProc>     var copyDirectoryProc: CFunctionPointer<Tcl_FSCopyDirectoryProc>     var lstatProc: CFunctionPointer<Tcl_FSLstatProc>     var loadFileProc: CFunctionPointer<Tcl_FSLoadFileProc>     var getCwdProc: CFunctionPointer<Tcl_FSGetCwdProc>     var chdirProc: CFunctionPointer<Tcl_FSChdirProc>     init()     init(typeName typeName: UnsafePointer<Int8>, structureLength structureLength: Int32, version version: Tcl_FSVersion, pathInFilesystemProc pathInFilesystemProc: CFunctionPointer<Tcl_FSPathInFilesystemProc>, dupInternalRepProc dupInternalRepProc: CFunctionPointer<Tcl_FSDupInternalRepProc>, freeInternalRepProc freeInternalRepProc: CFunctionPointer<Tcl_FSFreeInternalRepProc>, internalToNormalizedProc internalToNormalizedProc: CFunctionPointer<Tcl_FSInternalToNormalizedProc>, createInternalRepProc createInternalRepProc: CFunctionPointer<Tcl_FSCreateInternalRepProc>, normalizePathProc normalizePathProc: CFunctionPointer<Tcl_FSNormalizePathProc>, filesystemPathTypeProc filesystemPathTypeProc: CFunctionPointer<Tcl_FSFilesystemPathTypeProc>, filesystemSeparatorProc filesystemSeparatorProc: CFunctionPointer<Tcl_FSFilesystemSeparatorProc>, statProc statProc: CFunctionPointer<Tcl_FSStatProc>, accessProc accessProc: CFunctionPointer<Tcl_FSAccessProc>, openFileChannelProc openFileChannelProc: CFunctionPointer<Tcl_FSOpenFileChannelProc>, matchInDirectoryProc matchInDirectoryProc: CFunctionPointer<Tcl_FSMatchInDirectoryProc>, utimeProc utimeProc: CFunctionPointer<Tcl_FSUtimeProc>, linkProc linkProc: CFunctionPointer<Tcl_FSLinkProc>, listVolumesProc listVolumesProc: CFunctionPointer<Tcl_FSListVolumesProc>, fileAttrStringsProc fileAttrStringsProc: CFunctionPointer<Tcl_FSFileAttrStringsProc>, fileAttrsGetProc fileAttrsGetProc: CFunctionPointer<Tcl_FSFileAttrsGetProc>, fileAttrsSetProc fileAttrsSetProc: CFunctionPointer<Tcl_FSFileAttrsSetProc>, createDirectoryProc createDirectoryProc: CFunctionPointer<Tcl_FSCreateDirectoryProc>, removeDirectoryProc removeDirectoryProc: CFunctionPointer<Tcl_FSRemoveDirectoryProc>, deleteFileProc deleteFileProc: CFunctionPointer<Tcl_FSDeleteFileProc>, copyFileProc copyFileProc: CFunctionPointer<Tcl_FSCopyFileProc>, renameFileProc renameFileProc: CFunctionPointer<Tcl_FSRenameFileProc>, copyDirectoryProc copyDirectoryProc: CFunctionPointer<Tcl_FSCopyDirectoryProc>, lstatProc lstatProc: CFunctionPointer<Tcl_FSLstatProc>, loadFileProc loadFileProc: CFunctionPointer<Tcl_FSLoadFileProc>, getCwdProc getCwdProc: CFunctionPointer<Tcl_FSGetCwdProc>, chdirProc chdirProc: CFunctionPointer<Tcl_FSChdirProc>) } ``` |
| To | ``` struct Tcl_Filesystem {     var typeName: UnsafePointer<Int8>     var structureLength: Int32     var version: Tcl_FSVersion     var pathInFilesystemProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<ClientData>) -> Int32)!     var dupInternalRepProc: ((ClientData) -> ClientData)!     var freeInternalRepProc: ((ClientData) -> Void)!     var internalToNormalizedProc: ((ClientData) -> UnsafeMutablePointer<Tcl_Obj>)!     var createInternalRepProc: ((UnsafeMutablePointer<Tcl_Obj>) -> ClientData)!     var normalizePathProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!     var filesystemPathTypeProc: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!     var filesystemSeparatorProc: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!     var statProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!     var accessProc: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!     var openFileChannelProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Tcl_Channel)!     var matchInDirectoryProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)!     var utimeProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)!     var linkProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var listVolumesProc: (() -> UnsafeMutablePointer<Tcl_Obj>)!     var fileAttrStringsProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)!     var fileAttrsGetProc: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var fileAttrsSetProc: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var createDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var removeDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var deleteFileProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var copyFileProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var renameFileProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var copyDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var lstatProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!     var loadFileProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32)!     var getCwdProc: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)!     var chdirProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     init()     init(typeName typeName: UnsafePointer<Int8>, structureLength structureLength: Int32, version version: Tcl_FSVersion, pathInFilesystemProc pathInFilesystemProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<ClientData>) -> Int32)!, dupInternalRepProc dupInternalRepProc: ((ClientData) -> ClientData)!, freeInternalRepProc freeInternalRepProc: ((ClientData) -> Void)!, internalToNormalizedProc internalToNormalizedProc: ((ClientData) -> UnsafeMutablePointer<Tcl_Obj>)!, createInternalRepProc createInternalRepProc: ((UnsafeMutablePointer<Tcl_Obj>) -> ClientData)!, normalizePathProc normalizePathProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!, filesystemPathTypeProc filesystemPathTypeProc: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, filesystemSeparatorProc filesystemSeparatorProc: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, statProc statProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!, accessProc accessProc: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!, openFileChannelProc openFileChannelProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Tcl_Channel)!, matchInDirectoryProc matchInDirectoryProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)!, utimeProc utimeProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)!, linkProc linkProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, listVolumesProc listVolumesProc: (() -> UnsafeMutablePointer<Tcl_Obj>)!, fileAttrStringsProc fileAttrStringsProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)!, fileAttrsGetProc fileAttrsGetProc: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, fileAttrsSetProc fileAttrsSetProc: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, createDirectoryProc createDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, removeDirectoryProc removeDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, deleteFileProc deleteFileProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, copyFileProc copyFileProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, renameFileProc renameFileProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, copyDirectoryProc copyDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, lstatProc lstatProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!, loadFileProc loadFileProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32)!, getCwdProc getCwdProc: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)!, chdirProc chdirProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!) } ``` |

Modified Tcl_Filesystem.accessProc

|  | Declaration |
| --- | --- |
| From | ``` var accessProc: CFunctionPointer<Tcl_FSAccessProc> ``` |
| To | ``` var accessProc: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)! ``` |

Modified Tcl_Filesystem.chdirProc

|  | Declaration |
| --- | --- |
| From | ``` var chdirProc: CFunctionPointer<Tcl_FSChdirProc> ``` |
| To | ``` var chdirProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified Tcl_Filesystem.copyDirectoryProc

|  | Declaration |
| --- | --- |
| From | ``` var copyDirectoryProc: CFunctionPointer<Tcl_FSCopyDirectoryProc> ``` |
| To | ``` var copyDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified Tcl_Filesystem.copyFileProc

|  | Declaration |
| --- | --- |
| From | ``` var copyFileProc: CFunctionPointer<Tcl_FSCopyFileProc> ``` |
| To | ``` var copyFileProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified Tcl_Filesystem.createDirectoryProc

|  | Declaration |
| --- | --- |
| From | ``` var createDirectoryProc: CFunctionPointer<Tcl_FSCreateDirectoryProc> ``` |
| To | ``` var createDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified Tcl_Filesystem.createInternalRepProc

|  | Declaration |
| --- | --- |
| From | ``` var createInternalRepProc: CFunctionPointer<Tcl_FSCreateInternalRepProc> ``` |
| To | ``` var createInternalRepProc: ((UnsafeMutablePointer<Tcl_Obj>) -> ClientData)! ``` |

Modified Tcl_Filesystem.deleteFileProc

|  | Declaration |
| --- | --- |
| From | ``` var deleteFileProc: CFunctionPointer<Tcl_FSDeleteFileProc> ``` |
| To | ``` var deleteFileProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified Tcl_Filesystem.dupInternalRepProc

|  | Declaration |
| --- | --- |
| From | ``` var dupInternalRepProc: CFunctionPointer<Tcl_FSDupInternalRepProc> ``` |
| To | ``` var dupInternalRepProc: ((ClientData) -> ClientData)! ``` |

Modified Tcl_Filesystem.fileAttrsGetProc

|  | Declaration |
| --- | --- |
| From | ``` var fileAttrsGetProc: CFunctionPointer<Tcl_FSFileAttrsGetProc> ``` |
| To | ``` var fileAttrsGetProc: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified Tcl_Filesystem.fileAttrsSetProc

|  | Declaration |
| --- | --- |
| From | ``` var fileAttrsSetProc: CFunctionPointer<Tcl_FSFileAttrsSetProc> ``` |
| To | ``` var fileAttrsSetProc: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified Tcl_Filesystem.fileAttrStringsProc

|  | Declaration |
| --- | --- |
| From | ``` var fileAttrStringsProc: CFunctionPointer<Tcl_FSFileAttrStringsProc> ``` |
| To | ``` var fileAttrStringsProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)! ``` |

Modified Tcl_Filesystem.filesystemPathTypeProc

|  | Declaration |
| --- | --- |
| From | ``` var filesystemPathTypeProc: CFunctionPointer<Tcl_FSFilesystemPathTypeProc> ``` |
| To | ``` var filesystemPathTypeProc: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified Tcl_Filesystem.filesystemSeparatorProc

|  | Declaration |
| --- | --- |
| From | ``` var filesystemSeparatorProc: CFunctionPointer<Tcl_FSFilesystemSeparatorProc> ``` |
| To | ``` var filesystemSeparatorProc: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified Tcl_Filesystem.freeInternalRepProc

|  | Declaration |
| --- | --- |
| From | ``` var freeInternalRepProc: CFunctionPointer<Tcl_FSFreeInternalRepProc> ``` |
| To | ``` var freeInternalRepProc: ((ClientData) -> Void)! ``` |

Modified Tcl_Filesystem.getCwdProc

|  | Declaration |
| --- | --- |
| From | ``` var getCwdProc: CFunctionPointer<Tcl_FSGetCwdProc> ``` |
| To | ``` var getCwdProc: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified Tcl_Filesystem.internalToNormalizedProc

|  | Declaration |
| --- | --- |
| From | ``` var internalToNormalizedProc: CFunctionPointer<Tcl_FSInternalToNormalizedProc> ``` |
| To | ``` var internalToNormalizedProc: ((ClientData) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified Tcl_Filesystem.linkProc

|  | Declaration |
| --- | --- |
| From | ``` var linkProc: CFunctionPointer<Tcl_FSLinkProc> ``` |
| To | ``` var linkProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified Tcl_Filesystem.listVolumesProc

|  | Declaration |
| --- | --- |
| From | ``` var listVolumesProc: CFunctionPointer<Tcl_FSListVolumesProc> ``` |
| To | ``` var listVolumesProc: (() -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified Tcl_Filesystem.loadFileProc

|  | Declaration |
| --- | --- |
| From | ``` var loadFileProc: CFunctionPointer<Tcl_FSLoadFileProc> ``` |
| To | ``` var loadFileProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32)! ``` |

Modified Tcl_Filesystem.lstatProc

|  | Declaration |
| --- | --- |
| From | ``` var lstatProc: CFunctionPointer<Tcl_FSLstatProc> ``` |
| To | ``` var lstatProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)! ``` |

Modified Tcl_Filesystem.matchInDirectoryProc

|  | Declaration |
| --- | --- |
| From | ``` var matchInDirectoryProc: CFunctionPointer<Tcl_FSMatchInDirectoryProc> ``` |
| To | ``` var matchInDirectoryProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)! ``` |

Modified Tcl_Filesystem.normalizePathProc

|  | Declaration |
| --- | --- |
| From | ``` var normalizePathProc: CFunctionPointer<Tcl_FSNormalizePathProc> ``` |
| To | ``` var normalizePathProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)! ``` |

Modified Tcl_Filesystem.openFileChannelProc

|  | Declaration |
| --- | --- |
| From | ``` var openFileChannelProc: CFunctionPointer<Tcl_FSOpenFileChannelProc> ``` |
| To | ``` var openFileChannelProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Tcl_Channel)! ``` |

Modified Tcl_Filesystem.pathInFilesystemProc

|  | Declaration |
| --- | --- |
| From | ``` var pathInFilesystemProc: CFunctionPointer<Tcl_FSPathInFilesystemProc> ``` |
| To | ``` var pathInFilesystemProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<ClientData>) -> Int32)! ``` |

Modified Tcl_Filesystem.removeDirectoryProc

|  | Declaration |
| --- | --- |
| From | ``` var removeDirectoryProc: CFunctionPointer<Tcl_FSRemoveDirectoryProc> ``` |
| To | ``` var removeDirectoryProc: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified Tcl_Filesystem.renameFileProc

|  | Declaration |
| --- | --- |
| From | ``` var renameFileProc: CFunctionPointer<Tcl_FSRenameFileProc> ``` |
| To | ``` var renameFileProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified Tcl_Filesystem.statProc

|  | Declaration |
| --- | --- |
| From | ``` var statProc: CFunctionPointer<Tcl_FSStatProc> ``` |
| To | ``` var statProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)! ``` |

Modified Tcl_Filesystem.utimeProc

|  | Declaration |
| --- | --- |
| From | ``` var utimeProc: CFunctionPointer<Tcl_FSUtimeProc> ``` |
| To | ``` var utimeProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)! ``` |

Modified Tcl_HashKeyType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_HashKeyType {     var version: Int32     var flags: Int32     var hashKeyProc: CFunctionPointer<Tcl_HashKeyProc>     var compareKeysProc: CFunctionPointer<Tcl_CompareHashKeysProc>     var allocEntryProc: CFunctionPointer<Tcl_AllocHashEntryProc>     var freeEntryProc: CFunctionPointer<Tcl_FreeHashEntryProc>     init()     init(version version: Int32, flags flags: Int32, hashKeyProc hashKeyProc: CFunctionPointer<Tcl_HashKeyProc>, compareKeysProc compareKeysProc: CFunctionPointer<Tcl_CompareHashKeysProc>, allocEntryProc allocEntryProc: CFunctionPointer<Tcl_AllocHashEntryProc>, freeEntryProc freeEntryProc: CFunctionPointer<Tcl_FreeHashEntryProc>) } ``` |
| To | ``` struct Tcl_HashKeyType {     var version: Int32     var flags: Int32     var hashKeyProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UInt32)!     var compareKeysProc: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Tcl_HashEntry>) -> Int32)!     var allocEntryProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Tcl_HashEntry>)!     var freeEntryProc: ((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)!     init()     init(version version: Int32, flags flags: Int32, hashKeyProc hashKeyProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UInt32)!, compareKeysProc compareKeysProc: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Tcl_HashEntry>) -> Int32)!, allocEntryProc allocEntryProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, freeEntryProc freeEntryProc: ((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)!) } ``` |

Modified Tcl_HashKeyType.allocEntryProc

|  | Declaration |
| --- | --- |
| From | ``` var allocEntryProc: CFunctionPointer<Tcl_AllocHashEntryProc> ``` |
| To | ``` var allocEntryProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Tcl_HashEntry>)! ``` |

Modified Tcl_HashKeyType.compareKeysProc

|  | Declaration |
| --- | --- |
| From | ``` var compareKeysProc: CFunctionPointer<Tcl_CompareHashKeysProc> ``` |
| To | ``` var compareKeysProc: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Tcl_HashEntry>) -> Int32)! ``` |

Modified Tcl_HashKeyType.freeEntryProc

|  | Declaration |
| --- | --- |
| From | ``` var freeEntryProc: CFunctionPointer<Tcl_FreeHashEntryProc> ``` |
| To | ``` var freeEntryProc: ((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)! ``` |

Modified Tcl_HashKeyType.hashKeyProc

|  | Declaration |
| --- | --- |
| From | ``` var hashKeyProc: CFunctionPointer<Tcl_HashKeyProc> ``` |
| To | ``` var hashKeyProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Void>) -> UInt32)! ``` |

Modified Tcl_HashTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_HashTable {     var buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>     var staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>)     var numBuckets: Int32     var numEntries: Int32     var rebuildSize: Int32     var downShift: Int32     var mask: Int32     var keyType: Int32     var findProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)>     var createProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)>     var typePtr: UnsafeMutablePointer<Tcl_HashKeyType>     init()     init(buckets buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>, staticBuckets staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>), numBuckets numBuckets: Int32, numEntries numEntries: Int32, rebuildSize rebuildSize: Int32, downShift downShift: Int32, mask mask: Int32, keyType keyType: Int32, findProc findProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)>, createProc createProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)>, typePtr typePtr: UnsafeMutablePointer<Tcl_HashKeyType>) } ``` |
| To | ``` struct Tcl_HashTable {     var buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>     var staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>)     var numBuckets: Int32     var numEntries: Int32     var rebuildSize: Int32     var downShift: Int32     var mask: Int32     var keyType: Int32     var findProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)!     var createProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)!     var typePtr: UnsafeMutablePointer<Tcl_HashKeyType>     init()     init(buckets buckets: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_HashEntry>>, staticBuckets staticBuckets: (UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>, UnsafeMutablePointer<Tcl_HashEntry>), numBuckets numBuckets: Int32, numEntries numEntries: Int32, rebuildSize rebuildSize: Int32, downShift downShift: Int32, mask mask: Int32, keyType keyType: Int32, findProc findProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, createProc createProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, typePtr typePtr: UnsafeMutablePointer<Tcl_HashKeyType>) } ``` |

Modified Tcl_HashTable.createProc

|  | Declaration |
| --- | --- |
| From | ``` var createProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |
| To | ``` var createProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)! ``` |

Modified Tcl_HashTable.findProc

|  | Declaration |
| --- | --- |
| From | ``` var findProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |
| To | ``` var findProc: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)! ``` |

Modified Tcl_Interp [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Interp {     var result: UnsafeMutablePointer<Int8>     var freeProc: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)>     var errorLine: Int32     init()     init(result result: UnsafeMutablePointer<Int8>, freeProc freeProc: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)>, errorLine errorLine: Int32) } ``` |
| To | ``` struct Tcl_Interp {     var result: UnsafeMutablePointer<Int8>     var freeProc: ((UnsafeMutablePointer<Int8>) -> Void)!     var errorLine: Int32     init()     init(result result: UnsafeMutablePointer<Int8>, freeProc freeProc: ((UnsafeMutablePointer<Int8>) -> Void)!, errorLine errorLine: Int32) } ``` |

Modified Tcl_Interp.freeProc

|  | Declaration |
| --- | --- |
| From | ``` var freeProc: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)> ``` |
| To | ``` var freeProc: ((UnsafeMutablePointer<Int8>) -> Void)! ``` |

Modified Tcl_Namespace [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_Namespace {     var name: UnsafeMutablePointer<Int8>     var fullName: UnsafeMutablePointer<Int8>     var clientData: ClientData     var deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>     var parentPtr: UnsafeMutablePointer<Tcl_Namespace>     init()     init(name name: UnsafeMutablePointer<Int8>, fullName fullName: UnsafeMutablePointer<Int8>, clientData clientData: ClientData, deleteProc deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>, parentPtr parentPtr: UnsafeMutablePointer<Tcl_Namespace>) } ``` |
| To | ``` struct Tcl_Namespace {     var name: UnsafeMutablePointer<Int8>     var fullName: UnsafeMutablePointer<Int8>     var clientData: ClientData     var deleteProc: ((ClientData) -> Void)!     var parentPtr: UnsafeMutablePointer<Tcl_Namespace>     init()     init(name name: UnsafeMutablePointer<Int8>, fullName fullName: UnsafeMutablePointer<Int8>, clientData clientData: ClientData, deleteProc deleteProc: ((ClientData) -> Void)!, parentPtr parentPtr: UnsafeMutablePointer<Tcl_Namespace>) } ``` |

Modified Tcl_Namespace.deleteProc

|  | Declaration |
| --- | --- |
| From | ``` var deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc> ``` |
| To | ``` var deleteProc: ((ClientData) -> Void)! ``` |

Modified Tcl_NotifierProcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_NotifierProcs {     var setTimerProc: CFunctionPointer<Tcl_SetTimerProc>     var waitForEventProc: CFunctionPointer<Tcl_WaitForEventProc>     var createFileHandlerProc: CFunctionPointer<Tcl_CreateFileHandlerProc>     var deleteFileHandlerProc: CFunctionPointer<Tcl_DeleteFileHandlerProc>     var initNotifierProc: CFunctionPointer<Tcl_InitNotifierProc>     var finalizeNotifierProc: CFunctionPointer<Tcl_FinalizeNotifierProc>     var alertNotifierProc: CFunctionPointer<Tcl_AlertNotifierProc>     var serviceModeHookProc: CFunctionPointer<Tcl_ServiceModeHookProc>     init()     init(setTimerProc setTimerProc: CFunctionPointer<Tcl_SetTimerProc>, waitForEventProc waitForEventProc: CFunctionPointer<Tcl_WaitForEventProc>, createFileHandlerProc createFileHandlerProc: CFunctionPointer<Tcl_CreateFileHandlerProc>, deleteFileHandlerProc deleteFileHandlerProc: CFunctionPointer<Tcl_DeleteFileHandlerProc>, initNotifierProc initNotifierProc: CFunctionPointer<Tcl_InitNotifierProc>, finalizeNotifierProc finalizeNotifierProc: CFunctionPointer<Tcl_FinalizeNotifierProc>, alertNotifierProc alertNotifierProc: CFunctionPointer<Tcl_AlertNotifierProc>, serviceModeHookProc serviceModeHookProc: CFunctionPointer<Tcl_ServiceModeHookProc>) } ``` |
| To | ``` struct Tcl_NotifierProcs {     var setTimerProc: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!     var waitForEventProc: ((UnsafeMutablePointer<Tcl_Time>) -> Int32)!     var createFileHandlerProc: ((Int32, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!     var deleteFileHandlerProc: ((Int32) -> Void)!     var initNotifierProc: (() -> ClientData)!     var finalizeNotifierProc: ((ClientData) -> Void)!     var alertNotifierProc: ((ClientData) -> Void)!     var serviceModeHookProc: ((Int32) -> Void)!     init()     init(setTimerProc setTimerProc: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!, waitForEventProc waitForEventProc: ((UnsafeMutablePointer<Tcl_Time>) -> Int32)!, createFileHandlerProc createFileHandlerProc: ((Int32, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!, deleteFileHandlerProc deleteFileHandlerProc: ((Int32) -> Void)!, initNotifierProc initNotifierProc: (() -> ClientData)!, finalizeNotifierProc finalizeNotifierProc: ((ClientData) -> Void)!, alertNotifierProc alertNotifierProc: ((ClientData) -> Void)!, serviceModeHookProc serviceModeHookProc: ((Int32) -> Void)!) } ``` |

Modified Tcl_NotifierProcs.alertNotifierProc

|  | Declaration |
| --- | --- |
| From | ``` var alertNotifierProc: CFunctionPointer<Tcl_AlertNotifierProc> ``` |
| To | ``` var alertNotifierProc: ((ClientData) -> Void)! ``` |

Modified Tcl_NotifierProcs.createFileHandlerProc

|  | Declaration |
| --- | --- |
| From | ``` var createFileHandlerProc: CFunctionPointer<Tcl_CreateFileHandlerProc> ``` |
| To | ``` var createFileHandlerProc: ((Int32, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)! ``` |

Modified Tcl_NotifierProcs.deleteFileHandlerProc

|  | Declaration |
| --- | --- |
| From | ``` var deleteFileHandlerProc: CFunctionPointer<Tcl_DeleteFileHandlerProc> ``` |
| To | ``` var deleteFileHandlerProc: ((Int32) -> Void)! ``` |

Modified Tcl_NotifierProcs.finalizeNotifierProc

|  | Declaration |
| --- | --- |
| From | ``` var finalizeNotifierProc: CFunctionPointer<Tcl_FinalizeNotifierProc> ``` |
| To | ``` var finalizeNotifierProc: ((ClientData) -> Void)! ``` |

Modified Tcl_NotifierProcs.initNotifierProc

|  | Declaration |
| --- | --- |
| From | ``` var initNotifierProc: CFunctionPointer<Tcl_InitNotifierProc> ``` |
| To | ``` var initNotifierProc: (() -> ClientData)! ``` |

Modified Tcl_NotifierProcs.serviceModeHookProc

|  | Declaration |
| --- | --- |
| From | ``` var serviceModeHookProc: CFunctionPointer<Tcl_ServiceModeHookProc> ``` |
| To | ``` var serviceModeHookProc: ((Int32) -> Void)! ``` |

Modified Tcl_NotifierProcs.setTimerProc

|  | Declaration |
| --- | --- |
| From | ``` var setTimerProc: CFunctionPointer<Tcl_SetTimerProc> ``` |
| To | ``` var setTimerProc: ((UnsafeMutablePointer<Tcl_Time>) -> Void)! ``` |

Modified Tcl_NotifierProcs.waitForEventProc

|  | Declaration |
| --- | --- |
| From | ``` var waitForEventProc: CFunctionPointer<Tcl_WaitForEventProc> ``` |
| To | ``` var waitForEventProc: ((UnsafeMutablePointer<Tcl_Time>) -> Int32)! ``` |

Modified Tcl_ObjType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_ObjType {     var name: UnsafeMutablePointer<Int8>     var freeIntRepProc: CFunctionPointer<Tcl_FreeInternalRepProc>     var dupIntRepProc: CFunctionPointer<Tcl_DupInternalRepProc>     var updateStringProc: CFunctionPointer<Tcl_UpdateStringProc>     var setFromAnyProc: CFunctionPointer<Tcl_SetFromAnyProc>     init()     init(name name: UnsafeMutablePointer<Int8>, freeIntRepProc freeIntRepProc: CFunctionPointer<Tcl_FreeInternalRepProc>, dupIntRepProc dupIntRepProc: CFunctionPointer<Tcl_DupInternalRepProc>, updateStringProc updateStringProc: CFunctionPointer<Tcl_UpdateStringProc>, setFromAnyProc setFromAnyProc: CFunctionPointer<Tcl_SetFromAnyProc>) } ``` |
| To | ``` struct Tcl_ObjType {     var name: UnsafeMutablePointer<Int8>     var freeIntRepProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var dupIntRepProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var updateStringProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var setFromAnyProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     init()     init(name name: UnsafeMutablePointer<Int8>, freeIntRepProc freeIntRepProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!, dupIntRepProc dupIntRepProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, updateStringProc updateStringProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!, setFromAnyProc setFromAnyProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!) } ``` |

Modified Tcl_ObjType.dupIntRepProc

|  | Declaration |
| --- | --- |
| From | ``` var dupIntRepProc: CFunctionPointer<Tcl_DupInternalRepProc> ``` |
| To | ``` var dupIntRepProc: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified Tcl_ObjType.freeIntRepProc

|  | Declaration |
| --- | --- |
| From | ``` var freeIntRepProc: CFunctionPointer<Tcl_FreeInternalRepProc> ``` |
| To | ``` var freeIntRepProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified Tcl_ObjType.setFromAnyProc

|  | Declaration |
| --- | --- |
| From | ``` var setFromAnyProc: CFunctionPointer<Tcl_SetFromAnyProc> ``` |
| To | ``` var setFromAnyProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified Tcl_ObjType.updateStringProc

|  | Declaration |
| --- | --- |
| From | ``` var updateStringProc: CFunctionPointer<Tcl_UpdateStringProc> ``` |
| To | ``` var updateStringProc: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified Tcl_PathType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Tcl_PathType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct Tcl_PathType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified Tcl_QueuePosition [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Tcl_QueuePosition {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct Tcl_QueuePosition : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified Tcl_SavedResult [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tcl_SavedResult {     var result: UnsafeMutablePointer<Int8>     var freeProc: CFunctionPointer<Tcl_FreeProc>     var objResultPtr: UnsafeMutablePointer<Tcl_Obj>     var appendResult: UnsafeMutablePointer<Int8>     var appendAvl: Int32     var appendUsed: Int32     var resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(result result: UnsafeMutablePointer<Int8>, freeProc freeProc: CFunctionPointer<Tcl_FreeProc>, objResultPtr objResultPtr: UnsafeMutablePointer<Tcl_Obj>, appendResult appendResult: UnsafeMutablePointer<Int8>, appendAvl appendAvl: Int32, appendUsed appendUsed: Int32, resultSpace resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |
| To | ``` struct Tcl_SavedResult {     var result: UnsafeMutablePointer<Int8>     var freeProc: ((UnsafeMutablePointer<Int8>) -> Void)!     var objResultPtr: UnsafeMutablePointer<Tcl_Obj>     var appendResult: UnsafeMutablePointer<Int8>     var appendAvl: Int32     var appendUsed: Int32     var resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(result result: UnsafeMutablePointer<Int8>, freeProc freeProc: ((UnsafeMutablePointer<Int8>) -> Void)!, objResultPtr objResultPtr: UnsafeMutablePointer<Tcl_Obj>, appendResult appendResult: UnsafeMutablePointer<Int8>, appendAvl appendAvl: Int32, appendUsed appendUsed: Int32, resultSpace resultSpace: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified Tcl_SavedResult.freeProc

|  | Declaration |
| --- | --- |
| From | ``` var freeProc: CFunctionPointer<Tcl_FreeProc> ``` |
| To | ``` var freeProc: ((UnsafeMutablePointer<Int8>) -> Void)! ``` |

Modified Tcl_ValueType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Tcl_ValueType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct Tcl_ValueType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified TclStubs [struct]

|  | Declaration |
| --- | --- |
| From | ```  ``` |
| To | ``` struct TclStubs {     var magic: Int32     var hooks: UnsafeMutablePointer<TclStubHooks>     var tcl_PkgProvideEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, ClientData) -> Int32)!     var tcl_PkgRequireEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)!     var tcl_Panic: COpaquePointer     var tcl_Alloc: ((UInt32) -> UnsafeMutablePointer<Int8>)!     var tcl_Free: ((UnsafeMutablePointer<Int8>) -> Void)!     var tcl_Realloc: ((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)!     var tcl_DbCkalloc: ((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!     var tcl_DbCkfree: ((UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_DbCkrealloc: ((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!     var tcl_CreateFileHandler: ((Int32, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!     var tcl_DeleteFileHandler: ((Int32) -> Void)!     var tcl_SetTimer: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!     var tcl_Sleep: ((Int32) -> Void)!     var tcl_WaitForEvent: ((UnsafeMutablePointer<Tcl_Time>) -> Int32)!     var tcl_AppendAllObjTypes: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_AppendStringsToObj: COpaquePointer     var tcl_AppendToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)!     var tcl_ConcatObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_ConvertToType: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_ObjType>) -> Int32)!     var tcl_DbDecrRefCount: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)!     var tcl_DbIncrRefCount: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)!     var tcl_DbIsShared: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_DbNewBooleanObj: ((Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DbNewByteArrayObj: ((UnsafePointer<UInt8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DbNewDoubleObj: ((Double, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DbNewListObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DbNewLongObj: ((Int, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DbNewObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DbNewStringObj: ((UnsafePointer<Int8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DuplicateObj: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tclFreeObj: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_GetBoolean: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_GetBooleanFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_GetByteArrayFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<UInt8>)!     var tcl_GetDouble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)!     var tcl_GetDoubleFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)!     var tcl_GetIndexFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_GetInt: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_GetIntFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_GetLongFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)!     var tcl_GetObjType: ((UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_ObjType>)!     var tcl_GetStringFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8>)!     var tcl_InvalidateStringRep: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_ListObjAppendList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_ListObjAppendElement: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_ListObjGetElements: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)!     var tcl_ListObjIndex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_ListObjLength: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_ListObjReplace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_NewBooleanObj: ((Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_NewByteArrayObj: ((UnsafePointer<UInt8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_NewDoubleObj: ((Double) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_NewIntObj: ((Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_NewListObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_NewLongObj: ((Int) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_NewObj: (() -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_NewStringObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_SetBooleanObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)!     var tcl_SetByteArrayLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<UInt8>)!     var tcl_SetByteArrayObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<UInt8>, Int32) -> Void)!     var tcl_SetDoubleObj: ((UnsafeMutablePointer<Tcl_Obj>, Double) -> Void)!     var tcl_SetIntObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)!     var tcl_SetListObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)!     var tcl_SetLongObj: ((UnsafeMutablePointer<Tcl_Obj>, Int) -> Void)!     var tcl_SetObjLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)!     var tcl_SetStringObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)!     var tcl_AddErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!     var tcl_AddObjErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Void)!     var tcl_AllowExceptions: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!     var tcl_AppendElement: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!     var tcl_AppendResult: COpaquePointer     var tcl_AsyncCreate: ((((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, ClientData) -> Tcl_AsyncHandler)!     var tcl_AsyncDelete: ((Tcl_AsyncHandler) -> Void)!     var tcl_AsyncInvoke: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!     var tcl_AsyncMark: ((Tcl_AsyncHandler) -> Void)!     var tcl_AsyncReady: (() -> Int32)!     var tcl_BackgroundError: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!     var tcl_Backslash: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int8)!     var tcl_BadChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var tcl_CallWhenDeleted: ((UnsafeMutablePointer<Tcl_Interp>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)!     var tcl_CancelIdleCall: ((((ClientData) -> Void)!, ClientData) -> Void)!     var tcl_Close: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!     var tcl_CommandComplete: ((UnsafePointer<Int8>) -> Int32)!     var tcl_Concat: ((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)!     var tcl_ConvertElement: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)!     var tcl_ConvertCountedElement: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int8>, Int32) -> Int32)!     var tcl_CreateAlias: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafePointer<Int8>>) -> Int32)!     var tcl_CreateAliasObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_CreateChannel: ((UnsafeMutablePointer<Tcl_ChannelType>, UnsafePointer<Int8>, ClientData, Int32) -> Tcl_Channel)!     var tcl_CreateChannelHandler: ((Tcl_Channel, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!     var tcl_CreateCloseHandler: ((Tcl_Channel, ((ClientData) -> Void)!, ClientData) -> Void)!     var tcl_CreateCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Command)!     var tcl_CreateEventSource: ((((ClientData, Int32) -> Void)!, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!     var tcl_CreateExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)!     var tcl_CreateInterp: (() -> UnsafeMutablePointer<Tcl_Interp>)!     var tcl_CreateMathFunc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_ValueType>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)!, ClientData) -> Void)!     var tcl_CreateObjCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Command)!     var tcl_CreateSlave: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Interp>)!     var tcl_CreateTimerHandler: ((Int32, ((ClientData) -> Void)!, ClientData) -> Tcl_TimerToken)!     var tcl_CreateTrace: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)!, ClientData) -> Tcl_Trace)!     var tcl_DeleteAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!     var tcl_DeleteChannelHandler: ((Tcl_Channel, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!     var tcl_DeleteCloseHandler: ((Tcl_Channel, ((ClientData) -> Void)!, ClientData) -> Void)!     var tcl_DeleteCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!     var tcl_DeleteCommandFromToken: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> Int32)!     var tcl_DeleteEvents: ((((UnsafeMutablePointer<Tcl_Event>, ClientData) -> Int32)!, ClientData) -> Void)!     var tcl_DeleteEventSource: ((((ClientData, Int32) -> Void)!, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!     var tcl_DeleteExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)!     var tcl_DeleteHashEntry: ((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)!     var tcl_DeleteHashTable: ((UnsafeMutablePointer<Tcl_HashTable>) -> Void)!     var tcl_DeleteInterp: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!     var tcl_DetachPids: ((Int32, UnsafeMutablePointer<Tcl_Pid>) -> Void)!     var tcl_DeleteTimerHandler: ((Tcl_TimerToken) -> Void)!     var tcl_DeleteTrace: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Trace) -> Void)!     var tcl_DontCallWhenDeleted: ((UnsafeMutablePointer<Tcl_Interp>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)!     var tcl_DoOneEvent: ((Int32) -> Int32)!     var tcl_DoWhenIdle: ((((ClientData) -> Void)!, ClientData) -> Void)!     var tcl_DStringAppend: ((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!     var tcl_DStringAppendElement: ((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>)!     var tcl_DStringEndSublist: ((UnsafeMutablePointer<Tcl_DString>) -> Void)!     var tcl_DStringFree: ((UnsafeMutablePointer<Tcl_DString>) -> Void)!     var tcl_DStringGetResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)!     var tcl_DStringInit: ((UnsafeMutablePointer<Tcl_DString>) -> Void)!     var tcl_DStringResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)!     var tcl_DStringSetLength: ((UnsafeMutablePointer<Tcl_DString>, Int32) -> Void)!     var tcl_DStringStartSublist: ((UnsafeMutablePointer<Tcl_DString>) -> Void)!     var tcl_Eof: ((Tcl_Channel) -> Int32)!     var tcl_ErrnoId: (() -> UnsafePointer<Int8>)!     var tcl_ErrnoMsg: ((Int32) -> UnsafePointer<Int8>)!     var tcl_Eval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!     var tcl_EvalFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!     var tcl_EvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_EventuallyFree: ((ClientData, ((UnsafeMutablePointer<Int8>) -> Void)!) -> Void)!     var tcl_Exit: ((Int32) -> Void)!     var tcl_ExposeCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var tcl_ExprBoolean: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_ExprBooleanObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_ExprDouble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)!     var tcl_ExprDoubleObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)!     var tcl_ExprLong: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int>) -> Int32)!     var tcl_ExprLongObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)!     var tcl_ExprObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_ExprString: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!     var tcl_Finalize: (() -> Void)!     var tcl_FindExecutable: ((UnsafePointer<Int8>) -> Void)!     var tcl_FirstHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)!     var tcl_Flush: ((Tcl_Channel) -> Int32)!     var tcl_FreeResult: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!     var tcl_GetAlias: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)!     var tcl_GetAliasObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)!     var tcl_GetAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)?>) -> ClientData)!     var tcl_GetChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Tcl_Channel)!     var tcl_GetChannelBufferSize: ((Tcl_Channel) -> Int32)!     var tcl_GetChannelHandle: ((Tcl_Channel, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!     var tcl_GetChannelInstanceData: ((Tcl_Channel) -> ClientData)!     var tcl_GetChannelMode: ((Tcl_Channel) -> Int32)!     var tcl_GetChannelName: ((Tcl_Channel) -> UnsafePointer<Int8>)!     var tcl_GetChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!     var tcl_GetChannelType: ((Tcl_Channel) -> UnsafeMutablePointer<Tcl_ChannelType>)!     var tcl_GetCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)!     var tcl_GetCommandName: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> UnsafePointer<Int8>)!     var tcl_GetErrno: (() -> Int32)!     var tcl_GetHostName: (() -> UnsafePointer<Int8>)!     var tcl_GetInterpPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_GetMaster: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Interp>)!     var tcl_GetNameOfExecutable: (() -> UnsafePointer<Int8>)!     var tcl_GetObjResult: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_GetOpenFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!     var tcl_GetPathType: ((UnsafePointer<Int8>) -> Tcl_PathType)!     var tcl_Gets: ((Tcl_Channel, UnsafeMutablePointer<Tcl_DString>) -> Int32)!     var tcl_GetsObj: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_GetServiceMode: (() -> Int32)!     var tcl_GetSlave: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Interp>)!     var tcl_GetStdChannel: ((Int32) -> Tcl_Channel)!     var tcl_GetStringResult: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)!     var tcl_GetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_GetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_GlobalEval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!     var tcl_GlobalEvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_HideCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var tcl_Init: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_InitHashTable: ((UnsafeMutablePointer<Tcl_HashTable>, Int32) -> Void)!     var tcl_InputBlocked: ((Tcl_Channel) -> Int32)!     var tcl_InputBuffered: ((Tcl_Channel) -> Int32)!     var tcl_InterpDeleted: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_IsSafe: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_JoinPath: ((Int32, UnsafePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!     var tcl_LinkVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)!     var reserved188: UnsafeMutablePointer<Void>     var tcl_MakeFileChannel: ((ClientData, Int32) -> Tcl_Channel)!     var tcl_MakeSafe: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_MakeTcpClientChannel: ((ClientData) -> Tcl_Channel)!     var tcl_Merge: ((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)!     var tcl_NextHashEntry: ((UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)!     var tcl_NotifyChannel: ((Tcl_Channel, Int32) -> Void)!     var tcl_ObjGetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_ObjSetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_OpenCommandChannel: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, Int32) -> Tcl_Channel)!     var tcl_OpenFileChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)!     var tcl_OpenTcpClient: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, Int32) -> Tcl_Channel)!     var tcl_OpenTcpServer: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, ((ClientData, Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Void)!, ClientData) -> Tcl_Channel)!     var tcl_Preserve: ((ClientData) -> Void)!     var tcl_PrintDouble: ((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<Int8>) -> Void)!     var tcl_PutEnv: ((UnsafePointer<Int8>) -> Int32)!     var tcl_PosixError: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)!     var tcl_QueueEvent: ((UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)!     var tcl_Read: ((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)!     var tcl_ReapDetachedProcs: (() -> Void)!     var tcl_RecordAndEval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_RecordAndEvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!     var tcl_RegisterChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Void)!     var tcl_RegisterObjType: ((UnsafeMutablePointer<Tcl_ObjType>) -> Void)!     var tcl_RegExpCompile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_RegExp)!     var tcl_RegExpExec: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var tcl_RegExpMatch: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var tcl_RegExpRange: ((Tcl_RegExp, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)!     var tcl_Release: ((ClientData) -> Void)!     var tcl_ResetResult: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!     var tcl_ScanElement: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_ScanCountedElement: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_SeekOld: ((Tcl_Channel, Int32, Int32) -> Int32)!     var tcl_ServiceAll: (() -> Int32)!     var tcl_ServiceEvent: ((Int32) -> Int32)!     var tcl_SetAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)!     var tcl_SetChannelBufferSize: ((Tcl_Channel, Int32) -> Void)!     var tcl_SetChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var tcl_SetCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Tcl_CmdInfo>) -> Int32)!     var tcl_SetErrno: ((Int32) -> Void)!     var tcl_SetErrorCode: COpaquePointer     var tcl_SetMaxBlockTime: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!     var tcl_SetPanicProc: ((COpaquePointer) -> Void)!     var tcl_SetRecursionLimit: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!     var tcl_SetResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Int8>, ((UnsafeMutablePointer<Int8>) -> Void)!) -> Void)!     var tcl_SetServiceMode: ((Int32) -> Int32)!     var tcl_SetObjErrorCode: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_SetObjResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_SetStdChannel: ((Tcl_Channel, Int32) -> Void)!     var tcl_SetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_SetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_SignalId: ((Int32) -> UnsafePointer<Int8>)!     var tcl_SignalMsg: ((Int32) -> UnsafePointer<Int8>)!     var tcl_SourceRCFile: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!     var tcl_SplitList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)!     var tcl_SplitPath: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Void)!     var tcl_StaticPackage: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!) -> Void)!     var tcl_StringMatch: ((UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var tcl_TellOld: ((Tcl_Channel) -> Int32)!     var tcl_TraceVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Int32)!     var tcl_TraceVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Int32)!     var tcl_TranslateFileName: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!     var tcl_Ungets: ((Tcl_Channel, UnsafePointer<Int8>, Int32, Int32) -> Int32)!     var tcl_UnlinkVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!     var tcl_UnregisterChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!     var tcl_UnsetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_UnsetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_UntraceVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Void)!     var tcl_UntraceVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Void)!     var tcl_UpdateLinkedVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!     var tcl_UpVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_UpVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_VarEval: COpaquePointer     var tcl_VarTraceInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> ClientData)!     var tcl_VarTraceInfo2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> ClientData)!     var tcl_Write: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_WrongNumArgs: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>) -> Void)!     var tcl_DumpActiveMemory: ((UnsafePointer<Int8>) -> Int32)!     var tcl_ValidateAllMemory: ((UnsafePointer<Int8>, Int32) -> Void)!     var tcl_AppendResultVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)!     var tcl_AppendStringsToObjVA: ((UnsafeMutablePointer<Tcl_Obj>, CVaListPointer) -> Void)!     var tcl_HashStats: ((UnsafeMutablePointer<Tcl_HashTable>) -> UnsafeMutablePointer<Int8>)!     var tcl_ParseVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> UnsafePointer<Int8>)!     var tcl_PkgPresent: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_PkgPresentEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)!     var tcl_PkgProvide: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!     var tcl_PkgRequire: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_SetErrorCodeVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)!     var tcl_VarEvalVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Int32)!     var tcl_WaitPid: ((Tcl_Pid, UnsafeMutablePointer<Int32>, Int32) -> Tcl_Pid)!     var tcl_PanicVA: ((UnsafePointer<Int8>, CVaListPointer) -> Void)!     var tcl_GetVersion: ((UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Void)!     var tcl_InitMemory: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!     var tcl_StackChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_ChannelType>, ClientData, Int32, Tcl_Channel) -> Tcl_Channel)!     var tcl_UnstackChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!     var tcl_GetStackedChannel: ((Tcl_Channel) -> Tcl_Channel)!     var tcl_SetMainLoop: (((() -> Void)!) -> Void)!     var reserved285: UnsafeMutablePointer<Void>     var tcl_AppendObjToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_CreateEncoding: ((UnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding)!     var tcl_CreateThreadExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)!     var tcl_DeleteThreadExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)!     var tcl_DiscardResult: ((UnsafeMutablePointer<Tcl_SavedResult>) -> Void)!     var tcl_EvalEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32) -> Int32)!     var tcl_EvalObjv: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, Int32) -> Int32)!     var tcl_EvalObjEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!     var tcl_ExitThread: ((Int32) -> Void)!     var tcl_ExternalToUtf: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_ExternalToUtfDString: ((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!     var tcl_FinalizeThread: (() -> Void)!     var tcl_FinalizeNotifier: ((ClientData) -> Void)!     var tcl_FreeEncoding: ((Tcl_Encoding) -> Void)!     var tcl_GetCurrentThread: (() -> Tcl_ThreadId)!     var tcl_GetEncoding: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_Encoding)!     var tcl_GetEncodingName: ((Tcl_Encoding) -> UnsafePointer<Int8>)!     var tcl_GetEncodingNames: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!     var tcl_GetIndexFromObjStruct: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Void>, Int32, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_GetThreadData: ((UnsafeMutablePointer<Tcl_ThreadDataKey>, Int32) -> UnsafeMutablePointer<Void>)!     var tcl_GetVar2Ex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_InitNotifier: (() -> ClientData)!     var tcl_MutexLock: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)!     var tcl_MutexUnlock: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)!     var tcl_ConditionNotify: ((UnsafeMutablePointer<Tcl_Condition>) -> Void)!     var tcl_ConditionWait: ((UnsafeMutablePointer<Tcl_Condition>, UnsafeMutablePointer<Tcl_Mutex>, UnsafeMutablePointer<Tcl_Time>) -> Void)!     var tcl_NumUtfChars: ((UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_ReadChars: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Int32)!     var tcl_RestoreResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)!     var tcl_SaveResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)!     var tcl_SetSystemEncoding: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!     var tcl_SetVar2Ex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_ThreadAlert: ((Tcl_ThreadId) -> Void)!     var tcl_ThreadQueueEvent: ((Tcl_ThreadId, UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)!     var tcl_UniCharAtIndex: ((UnsafePointer<Int8>, Int32) -> Tcl_UniChar)!     var tcl_UniCharToLower: ((Int32) -> Tcl_UniChar)!     var tcl_UniCharToTitle: ((Int32) -> Tcl_UniChar)!     var tcl_UniCharToUpper: ((Int32) -> Tcl_UniChar)!     var tcl_UniCharToUtf: ((Int32, UnsafeMutablePointer<Int8>) -> Int32)!     var tcl_UtfAtIndex: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_UtfCharComplete: ((UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_UtfBackslash: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int8>) -> Int32)!     var tcl_UtfFindFirst: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_UtfFindLast: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!     var tcl_UtfNext: ((UnsafePointer<Int8>) -> UnsafePointer<Int8>)!     var tcl_UtfPrev: ((UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafePointer<Int8>)!     var tcl_UtfToExternal: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_UtfToExternalDString: ((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!     var tcl_UtfToLower: ((UnsafeMutablePointer<Int8>) -> Int32)!     var tcl_UtfToTitle: ((UnsafeMutablePointer<Int8>) -> Int32)!     var tcl_UtfToUniChar: ((UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_UniChar>) -> Int32)!     var tcl_UtfToUpper: ((UnsafeMutablePointer<Int8>) -> Int32)!     var tcl_WriteChars: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_WriteObj: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_GetString: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Int8>)!     var tcl_GetDefaultEncodingDir: (() -> UnsafePointer<Int8>)!     var tcl_SetDefaultEncodingDir: ((UnsafePointer<Int8>) -> Void)!     var tcl_AlertNotifier: ((ClientData) -> Void)!     var tcl_ServiceModeHook: ((Int32) -> Void)!     var tcl_UniCharIsAlnum: ((Int32) -> Int32)!     var tcl_UniCharIsAlpha: ((Int32) -> Int32)!     var tcl_UniCharIsDigit: ((Int32) -> Int32)!     var tcl_UniCharIsLower: ((Int32) -> Int32)!     var tcl_UniCharIsSpace: ((Int32) -> Int32)!     var tcl_UniCharIsUpper: ((Int32) -> Int32)!     var tcl_UniCharIsWordChar: ((Int32) -> Int32)!     var tcl_UniCharLen: ((UnsafePointer<Tcl_UniChar>) -> Int32)!     var tcl_UniCharNcmp: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)!     var tcl_UniCharToUtfDString: ((UnsafePointer<Tcl_UniChar>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!     var tcl_UtfToUniCharDString: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Tcl_UniChar>)!     var tcl_GetRegExpFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_RegExp)!     var tcl_EvalTokens: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FreeParse: ((UnsafeMutablePointer<Tcl_Parse>) -> Void)!     var tcl_LogCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!     var tcl_ParseBraces: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!     var tcl_ParseCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)!     var tcl_ParseExpr: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)!     var tcl_ParseQuotedString: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!     var tcl_ParseVarName: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32) -> Int32)!     var tcl_GetCwd: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!     var tcl_Chdir: ((UnsafePointer<Int8>) -> Int32)!     var tcl_Access: ((UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_Stat: ((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)!     var tcl_UtfNcmp: ((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)!     var tcl_UtfNcasecmp: ((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)!     var tcl_StringCaseMatch: ((UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_UniCharIsControl: ((Int32) -> Int32)!     var tcl_UniCharIsGraph: ((Int32) -> Int32)!     var tcl_UniCharIsPrint: ((Int32) -> Int32)!     var tcl_UniCharIsPunct: ((Int32) -> Int32)!     var tcl_RegExpExecObj: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32) -> Int32)!     var tcl_RegExpGetInfo: ((Tcl_RegExp, UnsafeMutablePointer<Tcl_RegExpInfo>) -> Void)!     var tcl_NewUnicodeObj: ((UnsafePointer<Tcl_UniChar>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_SetUnicodeObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)!     var tcl_GetCharLength: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_GetUniChar: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_UniChar)!     var tcl_GetUnicode: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_UniChar>)!     var tcl_GetRange: ((UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_AppendUnicodeToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)!     var tcl_RegExpMatchObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_SetNotifier: ((UnsafeMutablePointer<Tcl_NotifierProcs>) -> Void)!     var tcl_GetAllocMutex: (() -> UnsafeMutablePointer<Tcl_Mutex>)!     var tcl_GetChannelNames: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_GetChannelNamesEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!     var tcl_ProcObjCmd: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_ConditionFinalize: ((UnsafeMutablePointer<Tcl_Condition>) -> Void)!     var tcl_MutexFinalize: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)!     var tcl_CreateThread: ((UnsafeMutablePointer<Tcl_ThreadId>, ((ClientData) -> Void)!, ClientData, Int32, Int32) -> Int32)!     var tcl_ReadRaw: ((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)!     var tcl_WriteRaw: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_GetTopChannel: ((Tcl_Channel) -> Tcl_Channel)!     var tcl_ChannelBuffered: ((Tcl_Channel) -> Int32)!     var tcl_ChannelName: ((UnsafePointer<Tcl_ChannelType>) -> UnsafePointer<Int8>)!     var tcl_ChannelVersion: ((UnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion)!     var tcl_ChannelBlockModeProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)!)!     var tcl_ChannelCloseProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!)!     var tcl_ChannelClose2Proc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!)!     var tcl_ChannelInputProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)!     var tcl_ChannelOutputProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)!     var tcl_ChannelSeekProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)!     var tcl_ChannelSetOptionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!)!     var tcl_ChannelGetOptionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!)!     var tcl_ChannelWatchProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)!)!     var tcl_ChannelGetHandleProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!)!     var tcl_ChannelFlushProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData) -> Int32)!)!     var tcl_ChannelHandlerProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)!)!     var tcl_JoinThread: ((Tcl_ThreadId, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_IsChannelShared: ((Tcl_Channel) -> Int32)!     var tcl_IsChannelRegistered: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!     var tcl_CutChannel: ((Tcl_Channel) -> Void)!     var tcl_SpliceChannel: ((Tcl_Channel) -> Void)!     var tcl_ClearChannelHandlers: ((Tcl_Channel) -> Void)!     var tcl_IsChannelExisting: ((UnsafePointer<Int8>) -> Int32)!     var tcl_UniCharNcasecmp: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)!     var tcl_UniCharCaseMatch: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, Int32) -> Int32)!     var tcl_FindHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)!     var tcl_CreateHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)!     var tcl_InitCustomHashTable: ((UnsafeMutablePointer<Tcl_HashTable>, Int32, UnsafeMutablePointer<Tcl_HashKeyType>) -> Void)!     var tcl_InitObjHashTable: ((UnsafeMutablePointer<Tcl_HashTable>) -> Void)!     var tcl_CommandTraceInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> ClientData)!     var tcl_TraceCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> Int32)!     var tcl_UntraceCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> Void)!     var tcl_AttemptAlloc: ((UInt32) -> UnsafeMutablePointer<Int8>)!     var tcl_AttemptDbCkalloc: ((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!     var tcl_AttemptRealloc: ((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)!     var tcl_AttemptDbCkrealloc: ((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!     var tcl_AttemptSetObjLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!     var tcl_GetChannelThread: ((Tcl_Channel) -> Tcl_ThreadId)!     var tcl_GetUnicodeFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_UniChar>)!     var tcl_GetMathFuncInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)?>, UnsafeMutablePointer<ClientData>) -> Int32)!     var tcl_ListMathFuncs: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_SubstObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DetachChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!     var tcl_IsStandardChannel: ((Tcl_Channel) -> Int32)!     var tcl_FSCopyFile: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSCopyDirectory: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_FSCreateDirectory: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSDeleteFile: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSLoadFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32)!     var tcl_FSMatchInDirectory: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)!     var tcl_FSLink: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSRemoveDirectory: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_FSRenameFile: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSLstat: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!     var tcl_FSUtime: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)!     var tcl_FSFileAttrsGet: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_FSFileAttrsSet: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSFileAttrStrings: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)!     var tcl_FSStat: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!     var tcl_FSAccess: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!     var tcl_FSOpenFileChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)!     var tcl_FSGetCwd: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSChdir: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSConvertToPathType: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSJoinPath: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSSplitPath: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSEqualPaths: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSGetNormalizedPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSJoinToPath: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSGetInternalRep: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)!     var tcl_FSGetTranslatedPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSEvalFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_FSNewNativePath: ((UnsafeMutablePointer<Tcl_Filesystem>, ClientData) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSGetNativePath: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)!     var tcl_FSFileSystemInfo: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSPathSeparator: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSListVolumes: (() -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_FSRegister: ((ClientData, UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)!     var tcl_FSUnregister: ((UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)!     var tcl_FSData: ((UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)!     var tcl_FSGetTranslatedStringPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)!     var tcl_FSGetFileSystemForPath: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Filesystem>)!     var tcl_FSGetPathType: ((UnsafeMutablePointer<Tcl_Obj>) -> Tcl_PathType)!     var tcl_OutputBuffered: ((Tcl_Channel) -> Int32)!     var tcl_FSMountsChanged: ((UnsafeMutablePointer<Tcl_Filesystem>) -> Void)!     var tcl_EvalTokensStandard: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> Int32)!     var tcl_GetTime: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!     var tcl_CreateObjTrace: ((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, Tcl_Command, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Trace)!     var tcl_GetCommandInfoFromToken: ((Tcl_Command, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)!     var tcl_SetCommandInfoFromToken: ((Tcl_Command, UnsafePointer<Tcl_CmdInfo>) -> Int32)!     var tcl_DbNewWideIntObj: ((Tcl_WideInt, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_GetWideIntFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_WideInt>) -> Int32)!     var tcl_NewWideIntObj: ((Tcl_WideInt) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_SetWideIntObj: ((UnsafeMutablePointer<Tcl_Obj>, Tcl_WideInt) -> Void)!     var tcl_AllocStatBuf: (() -> UnsafeMutablePointer<Tcl_StatBuf>)!     var tcl_Seek: ((Tcl_Channel, Tcl_WideInt, Int32) -> Tcl_WideInt)!     var tcl_Tell: ((Tcl_Channel) -> Tcl_WideInt)!     var tcl_ChannelWideSeekProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)!)!     var tcl_DictObjPut: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_DictObjGet: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_DictObjRemove: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_DictObjSize: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_DictObjFirst: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_DictObjNext: ((UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Void)!     var tcl_DictObjDone: ((UnsafeMutablePointer<Tcl_DictSearch>) -> Void)!     var tcl_DictObjPutKeyList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_DictObjRemoveKeyList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_NewDictObj: (() -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DbNewDictObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_RegisterConfig: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Config>, UnsafePointer<Int8>) -> Void)!     var tcl_CreateNamespace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ClientData, ((ClientData) -> Void)!) -> UnsafeMutablePointer<Tcl_Namespace>)!     var tcl_DeleteNamespace: ((UnsafeMutablePointer<Tcl_Namespace>) -> Void)!     var tcl_AppendExportList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_Export: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_Import: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)!     var tcl_ForgetImport: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>) -> Int32)!     var tcl_GetCurrentNamespace: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)!     var tcl_GetGlobalNamespace: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)!     var tcl_FindNamespace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> UnsafeMutablePointer<Tcl_Namespace>)!     var tcl_FindCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)!     var tcl_GetCommandFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Tcl_Command)!     var tcl_GetCommandFullName: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_FSEvalFileEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>) -> Int32)!     var tcl_SetExitProc: ((((ClientData) -> Void)!) -> ((ClientData) -> Void)!)!     var tcl_LimitAddHandler: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData, ((ClientData) -> Void)!) -> Void)!     var tcl_LimitRemoveHandler: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)!     var tcl_LimitReady: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_LimitCheck: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_LimitExceeded: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_LimitSetCommands: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)!     var tcl_LimitSetTime: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)!     var tcl_LimitSetGranularity: ((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32) -> Void)!     var tcl_LimitTypeEnabled: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!     var tcl_LimitTypeExceeded: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!     var tcl_LimitTypeSet: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)!     var tcl_LimitTypeReset: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)!     var tcl_LimitGetCommands: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!     var tcl_LimitGetTime: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)!     var tcl_LimitGetGranularity: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!     var tcl_SaveInterpState: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Tcl_InterpState)!     var tcl_RestoreInterpState: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_InterpState) -> Int32)!     var tcl_DiscardInterpState: ((Tcl_InterpState) -> Void)!     var tcl_SetReturnOptions: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_GetReturnOptions: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_IsEnsemble: ((Tcl_Command) -> Int32)!     var tcl_CreateEnsemble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)!     var tcl_FindEnsemble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_Command)!     var tcl_SetEnsembleSubcommandList: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_SetEnsembleMappingDict: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_SetEnsembleUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_SetEnsembleFlags: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, Int32) -> Int32)!     var tcl_GetEnsembleSubcommandList: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_GetEnsembleMappingDict: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_GetEnsembleUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_GetEnsembleFlags: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Int32>) -> Int32)!     var tcl_GetEnsembleNamespace: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Namespace>>) -> Int32)!     var tcl_SetTimeProc: ((((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, ClientData) -> Void)!     var tcl_QueryTimeProc: ((UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, UnsafeMutablePointer<ClientData>) -> Void)!     var tcl_ChannelThreadActionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)!)!     var tcl_NewBignumObj: ((UnsafeMutablePointer<mp_int>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_DbNewBignumObj: ((UnsafeMutablePointer<mp_int>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_SetBignumObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Void)!     var tcl_GetBignumFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)!     var tcl_TakeBignumFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)!     var tcl_TruncateChannel: ((Tcl_Channel, Tcl_WideInt) -> Int32)!     var tcl_ChannelTruncateProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt) -> Int32)!)!     var tcl_SetChannelErrorInterp: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_GetChannelErrorInterp: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)!     var tcl_SetChannelError: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_GetChannelError: ((Tcl_Channel, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)!     var tcl_InitBignumFromDouble: ((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<mp_int>) -> Int32)!     var tcl_GetNamespaceUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_SetNamespaceUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_GetEncodingFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Encoding>) -> Int32)!     var tcl_GetEncodingSearchPath: (() -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_SetEncodingSearchPath: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!     var tcl_GetEncodingNameFromEnvironment: ((UnsafeMutablePointer<Tcl_DString>) -> UnsafePointer<Int8>)!     var tcl_PkgRequireProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<ClientData>) -> Int32)!     var tcl_AppendObjToErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!     var tcl_AppendLimitedToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, Int32, UnsafePointer<Int8>) -> Void)!     var tcl_Format: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)!     var tcl_AppendFormatToObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!     var tcl_ObjPrintf: COpaquePointer     var tcl_AppendPrintfToObj: COpaquePointer     init()     init(magic magic: Int32, hooks hooks: UnsafeMutablePointer<TclStubHooks>, tcl_PkgProvideEx tcl_PkgProvideEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, ClientData) -> Int32)!, tcl_PkgRequireEx tcl_PkgRequireEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)!, tcl_Panic tcl_Panic: COpaquePointer, tcl_Alloc tcl_Alloc: ((UInt32) -> UnsafeMutablePointer<Int8>)!, tcl_Free tcl_Free: ((UnsafeMutablePointer<Int8>) -> Void)!, tcl_Realloc tcl_Realloc: ((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)!, tcl_DbCkalloc tcl_DbCkalloc: ((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, tcl_DbCkfree tcl_DbCkfree: ((UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_DbCkrealloc tcl_DbCkrealloc: ((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, tcl_CreateFileHandler tcl_CreateFileHandler: ((Int32, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!, tcl_DeleteFileHandler tcl_DeleteFileHandler: ((Int32) -> Void)!, tcl_SetTimer tcl_SetTimer: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!, tcl_Sleep tcl_Sleep: ((Int32) -> Void)!, tcl_WaitForEvent tcl_WaitForEvent: ((UnsafeMutablePointer<Tcl_Time>) -> Int32)!, tcl_AppendAllObjTypes tcl_AppendAllObjTypes: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_AppendStringsToObj tcl_AppendStringsToObj: COpaquePointer, tcl_AppendToObj tcl_AppendToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)!, tcl_ConcatObj tcl_ConcatObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_ConvertToType tcl_ConvertToType: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_ObjType>) -> Int32)!, tcl_DbDecrRefCount tcl_DbDecrRefCount: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)!, tcl_DbIncrRefCount tcl_DbIncrRefCount: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)!, tcl_DbIsShared tcl_DbIsShared: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_DbNewBooleanObj tcl_DbNewBooleanObj: ((Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DbNewByteArrayObj tcl_DbNewByteArrayObj: ((UnsafePointer<UInt8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DbNewDoubleObj tcl_DbNewDoubleObj: ((Double, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DbNewListObj tcl_DbNewListObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DbNewLongObj tcl_DbNewLongObj: ((Int, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DbNewObj tcl_DbNewObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DbNewStringObj tcl_DbNewStringObj: ((UnsafePointer<Int8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DuplicateObj tcl_DuplicateObj: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, tclFreeObj tclFreeObj: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_GetBoolean tcl_GetBoolean: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_GetBooleanFromObj tcl_GetBooleanFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_GetByteArrayFromObj tcl_GetByteArrayFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<UInt8>)!, tcl_GetDouble tcl_GetDouble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)!, tcl_GetDoubleFromObj tcl_GetDoubleFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)!, tcl_GetIndexFromObj tcl_GetIndexFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_GetInt tcl_GetInt: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_GetIntFromObj tcl_GetIntFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_GetLongFromObj tcl_GetLongFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)!, tcl_GetObjType tcl_GetObjType: ((UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_ObjType>)!, tcl_GetStringFromObj tcl_GetStringFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8>)!, tcl_InvalidateStringRep tcl_InvalidateStringRep: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_ListObjAppendList tcl_ListObjAppendList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_ListObjAppendElement tcl_ListObjAppendElement: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_ListObjGetElements tcl_ListObjGetElements: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)!, tcl_ListObjIndex tcl_ListObjIndex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_ListObjLength tcl_ListObjLength: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_ListObjReplace tcl_ListObjReplace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_NewBooleanObj tcl_NewBooleanObj: ((Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_NewByteArrayObj tcl_NewByteArrayObj: ((UnsafePointer<UInt8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_NewDoubleObj tcl_NewDoubleObj: ((Double) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_NewIntObj tcl_NewIntObj: ((Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_NewListObj tcl_NewListObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_NewLongObj tcl_NewLongObj: ((Int) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_NewObj tcl_NewObj: (() -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_NewStringObj tcl_NewStringObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_SetBooleanObj tcl_SetBooleanObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)!, tcl_SetByteArrayLength tcl_SetByteArrayLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<UInt8>)!, tcl_SetByteArrayObj tcl_SetByteArrayObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<UInt8>, Int32) -> Void)!, tcl_SetDoubleObj tcl_SetDoubleObj: ((UnsafeMutablePointer<Tcl_Obj>, Double) -> Void)!, tcl_SetIntObj tcl_SetIntObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)!, tcl_SetListObj tcl_SetListObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)!, tcl_SetLongObj tcl_SetLongObj: ((UnsafeMutablePointer<Tcl_Obj>, Int) -> Void)!, tcl_SetObjLength tcl_SetObjLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)!, tcl_SetStringObj tcl_SetStringObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)!, tcl_AddErrorInfo tcl_AddErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!, tcl_AddObjErrorInfo tcl_AddObjErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Void)!, tcl_AllowExceptions tcl_AllowExceptions: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!, tcl_AppendElement tcl_AppendElement: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!, tcl_AppendResult tcl_AppendResult: COpaquePointer, tcl_AsyncCreate tcl_AsyncCreate: ((((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, ClientData) -> Tcl_AsyncHandler)!, tcl_AsyncDelete tcl_AsyncDelete: ((Tcl_AsyncHandler) -> Void)!, tcl_AsyncInvoke tcl_AsyncInvoke: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, tcl_AsyncMark tcl_AsyncMark: ((Tcl_AsyncHandler) -> Void)!, tcl_AsyncReady tcl_AsyncReady: (() -> Int32)!, tcl_BackgroundError tcl_BackgroundError: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!, tcl_Backslash tcl_Backslash: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int8)!, tcl_BadChannelOption tcl_BadChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, tcl_CallWhenDeleted tcl_CallWhenDeleted: ((UnsafeMutablePointer<Tcl_Interp>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)!, tcl_CancelIdleCall tcl_CancelIdleCall: ((((ClientData) -> Void)!, ClientData) -> Void)!, tcl_Close tcl_Close: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!, tcl_CommandComplete tcl_CommandComplete: ((UnsafePointer<Int8>) -> Int32)!, tcl_Concat tcl_Concat: ((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)!, tcl_ConvertElement tcl_ConvertElement: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)!, tcl_ConvertCountedElement tcl_ConvertCountedElement: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int8>, Int32) -> Int32)!, tcl_CreateAlias tcl_CreateAlias: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafePointer<Int8>>) -> Int32)!, tcl_CreateAliasObj tcl_CreateAliasObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_CreateChannel tcl_CreateChannel: ((UnsafeMutablePointer<Tcl_ChannelType>, UnsafePointer<Int8>, ClientData, Int32) -> Tcl_Channel)!, tcl_CreateChannelHandler tcl_CreateChannelHandler: ((Tcl_Channel, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!, tcl_CreateCloseHandler tcl_CreateCloseHandler: ((Tcl_Channel, ((ClientData) -> Void)!, ClientData) -> Void)!, tcl_CreateCommand tcl_CreateCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Command)!, tcl_CreateEventSource tcl_CreateEventSource: ((((ClientData, Int32) -> Void)!, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!, tcl_CreateExitHandler tcl_CreateExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)!, tcl_CreateInterp tcl_CreateInterp: (() -> UnsafeMutablePointer<Tcl_Interp>)!, tcl_CreateMathFunc tcl_CreateMathFunc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_ValueType>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)!, ClientData) -> Void)!, tcl_CreateObjCommand tcl_CreateObjCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Command)!, tcl_CreateSlave tcl_CreateSlave: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Interp>)!, tcl_CreateTimerHandler tcl_CreateTimerHandler: ((Int32, ((ClientData) -> Void)!, ClientData) -> Tcl_TimerToken)!, tcl_CreateTrace tcl_CreateTrace: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)!, ClientData) -> Tcl_Trace)!, tcl_DeleteAssocData tcl_DeleteAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!, tcl_DeleteChannelHandler tcl_DeleteChannelHandler: ((Tcl_Channel, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!, tcl_DeleteCloseHandler tcl_DeleteCloseHandler: ((Tcl_Channel, ((ClientData) -> Void)!, ClientData) -> Void)!, tcl_DeleteCommand tcl_DeleteCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!, tcl_DeleteCommandFromToken tcl_DeleteCommandFromToken: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> Int32)!, tcl_DeleteEvents tcl_DeleteEvents: ((((UnsafeMutablePointer<Tcl_Event>, ClientData) -> Int32)!, ClientData) -> Void)!, tcl_DeleteEventSource tcl_DeleteEventSource: ((((ClientData, Int32) -> Void)!, ((ClientData, Int32) -> Void)!, ClientData) -> Void)!, tcl_DeleteExitHandler tcl_DeleteExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)!, tcl_DeleteHashEntry tcl_DeleteHashEntry: ((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)!, tcl_DeleteHashTable tcl_DeleteHashTable: ((UnsafeMutablePointer<Tcl_HashTable>) -> Void)!, tcl_DeleteInterp tcl_DeleteInterp: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!, tcl_DetachPids tcl_DetachPids: ((Int32, UnsafeMutablePointer<Tcl_Pid>) -> Void)!, tcl_DeleteTimerHandler tcl_DeleteTimerHandler: ((Tcl_TimerToken) -> Void)!, tcl_DeleteTrace tcl_DeleteTrace: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Trace) -> Void)!, tcl_DontCallWhenDeleted tcl_DontCallWhenDeleted: ((UnsafeMutablePointer<Tcl_Interp>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)!, tcl_DoOneEvent tcl_DoOneEvent: ((Int32) -> Int32)!, tcl_DoWhenIdle tcl_DoWhenIdle: ((((ClientData) -> Void)!, ClientData) -> Void)!, tcl_DStringAppend tcl_DStringAppend: ((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, tcl_DStringAppendElement tcl_DStringAppendElement: ((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>)!, tcl_DStringEndSublist tcl_DStringEndSublist: ((UnsafeMutablePointer<Tcl_DString>) -> Void)!, tcl_DStringFree tcl_DStringFree: ((UnsafeMutablePointer<Tcl_DString>) -> Void)!, tcl_DStringGetResult tcl_DStringGetResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)!, tcl_DStringInit tcl_DStringInit: ((UnsafeMutablePointer<Tcl_DString>) -> Void)!, tcl_DStringResult tcl_DStringResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)!, tcl_DStringSetLength tcl_DStringSetLength: ((UnsafeMutablePointer<Tcl_DString>, Int32) -> Void)!, tcl_DStringStartSublist tcl_DStringStartSublist: ((UnsafeMutablePointer<Tcl_DString>) -> Void)!, tcl_Eof tcl_Eof: ((Tcl_Channel) -> Int32)!, tcl_ErrnoId tcl_ErrnoId: (() -> UnsafePointer<Int8>)!, tcl_ErrnoMsg tcl_ErrnoMsg: ((Int32) -> UnsafePointer<Int8>)!, tcl_Eval tcl_Eval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!, tcl_EvalFile tcl_EvalFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!, tcl_EvalObj tcl_EvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_EventuallyFree tcl_EventuallyFree: ((ClientData, ((UnsafeMutablePointer<Int8>) -> Void)!) -> Void)!, tcl_Exit tcl_Exit: ((Int32) -> Void)!, tcl_ExposeCommand tcl_ExposeCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, tcl_ExprBoolean tcl_ExprBoolean: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_ExprBooleanObj tcl_ExprBooleanObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_ExprDouble tcl_ExprDouble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)!, tcl_ExprDoubleObj tcl_ExprDoubleObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)!, tcl_ExprLong tcl_ExprLong: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int>) -> Int32)!, tcl_ExprLongObj tcl_ExprLongObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)!, tcl_ExprObj tcl_ExprObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_ExprString tcl_ExprString: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!, tcl_Finalize tcl_Finalize: (() -> Void)!, tcl_FindExecutable tcl_FindExecutable: ((UnsafePointer<Int8>) -> Void)!, tcl_FirstHashEntry tcl_FirstHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, tcl_Flush tcl_Flush: ((Tcl_Channel) -> Int32)!, tcl_FreeResult tcl_FreeResult: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!, tcl_GetAlias tcl_GetAlias: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)!, tcl_GetAliasObj tcl_GetAliasObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)!, tcl_GetAssocData tcl_GetAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)?>) -> ClientData)!, tcl_GetChannel tcl_GetChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Tcl_Channel)!, tcl_GetChannelBufferSize tcl_GetChannelBufferSize: ((Tcl_Channel) -> Int32)!, tcl_GetChannelHandle tcl_GetChannelHandle: ((Tcl_Channel, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!, tcl_GetChannelInstanceData tcl_GetChannelInstanceData: ((Tcl_Channel) -> ClientData)!, tcl_GetChannelMode tcl_GetChannelMode: ((Tcl_Channel) -> Int32)!, tcl_GetChannelName tcl_GetChannelName: ((Tcl_Channel) -> UnsafePointer<Int8>)!, tcl_GetChannelOption tcl_GetChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!, tcl_GetChannelType tcl_GetChannelType: ((Tcl_Channel) -> UnsafeMutablePointer<Tcl_ChannelType>)!, tcl_GetCommandInfo tcl_GetCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)!, tcl_GetCommandName tcl_GetCommandName: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> UnsafePointer<Int8>)!, tcl_GetErrno tcl_GetErrno: (() -> Int32)!, tcl_GetHostName tcl_GetHostName: (() -> UnsafePointer<Int8>)!, tcl_GetInterpPath tcl_GetInterpPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_GetMaster tcl_GetMaster: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Interp>)!, tcl_GetNameOfExecutable tcl_GetNameOfExecutable: (() -> UnsafePointer<Int8>)!, tcl_GetObjResult tcl_GetObjResult: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_GetOpenFile tcl_GetOpenFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!, tcl_GetPathType tcl_GetPathType: ((UnsafePointer<Int8>) -> Tcl_PathType)!, tcl_Gets tcl_Gets: ((Tcl_Channel, UnsafeMutablePointer<Tcl_DString>) -> Int32)!, tcl_GetsObj tcl_GetsObj: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_GetServiceMode tcl_GetServiceMode: (() -> Int32)!, tcl_GetSlave tcl_GetSlave: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Interp>)!, tcl_GetStdChannel tcl_GetStdChannel: ((Int32) -> Tcl_Channel)!, tcl_GetStringResult tcl_GetStringResult: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)!, tcl_GetVar tcl_GetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_GetVar2 tcl_GetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_GlobalEval tcl_GlobalEval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!, tcl_GlobalEvalObj tcl_GlobalEvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_HideCommand tcl_HideCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, tcl_Init tcl_Init: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_InitHashTable tcl_InitHashTable: ((UnsafeMutablePointer<Tcl_HashTable>, Int32) -> Void)!, tcl_InputBlocked tcl_InputBlocked: ((Tcl_Channel) -> Int32)!, tcl_InputBuffered tcl_InputBuffered: ((Tcl_Channel) -> Int32)!, tcl_InterpDeleted tcl_InterpDeleted: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_IsSafe tcl_IsSafe: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_JoinPath tcl_JoinPath: ((Int32, UnsafePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!, tcl_LinkVar tcl_LinkVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)!, reserved188 reserved188: UnsafeMutablePointer<Void>, tcl_MakeFileChannel tcl_MakeFileChannel: ((ClientData, Int32) -> Tcl_Channel)!, tcl_MakeSafe tcl_MakeSafe: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_MakeTcpClientChannel tcl_MakeTcpClientChannel: ((ClientData) -> Tcl_Channel)!, tcl_Merge tcl_Merge: ((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)!, tcl_NextHashEntry tcl_NextHashEntry: ((UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, tcl_NotifyChannel tcl_NotifyChannel: ((Tcl_Channel, Int32) -> Void)!, tcl_ObjGetVar2 tcl_ObjGetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_ObjSetVar2 tcl_ObjSetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_OpenCommandChannel tcl_OpenCommandChannel: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, Int32) -> Tcl_Channel)!, tcl_OpenFileChannel tcl_OpenFileChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)!, tcl_OpenTcpClient tcl_OpenTcpClient: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, Int32) -> Tcl_Channel)!, tcl_OpenTcpServer tcl_OpenTcpServer: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, ((ClientData, Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Void)!, ClientData) -> Tcl_Channel)!, tcl_Preserve tcl_Preserve: ((ClientData) -> Void)!, tcl_PrintDouble tcl_PrintDouble: ((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<Int8>) -> Void)!, tcl_PutEnv tcl_PutEnv: ((UnsafePointer<Int8>) -> Int32)!, tcl_PosixError tcl_PosixError: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)!, tcl_QueueEvent tcl_QueueEvent: ((UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)!, tcl_Read tcl_Read: ((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)!, tcl_ReapDetachedProcs tcl_ReapDetachedProcs: (() -> Void)!, tcl_RecordAndEval tcl_RecordAndEval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_RecordAndEvalObj tcl_RecordAndEvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!, tcl_RegisterChannel tcl_RegisterChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Void)!, tcl_RegisterObjType tcl_RegisterObjType: ((UnsafeMutablePointer<Tcl_ObjType>) -> Void)!, tcl_RegExpCompile tcl_RegExpCompile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_RegExp)!, tcl_RegExpExec tcl_RegExpExec: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, tcl_RegExpMatch tcl_RegExpMatch: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, tcl_RegExpRange tcl_RegExpRange: ((Tcl_RegExp, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)!, tcl_Release tcl_Release: ((ClientData) -> Void)!, tcl_ResetResult tcl_ResetResult: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!, tcl_ScanElement tcl_ScanElement: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_ScanCountedElement tcl_ScanCountedElement: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_SeekOld tcl_SeekOld: ((Tcl_Channel, Int32, Int32) -> Int32)!, tcl_ServiceAll tcl_ServiceAll: (() -> Int32)!, tcl_ServiceEvent tcl_ServiceEvent: ((Int32) -> Int32)!, tcl_SetAssocData tcl_SetAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)!, tcl_SetChannelBufferSize tcl_SetChannelBufferSize: ((Tcl_Channel, Int32) -> Void)!, tcl_SetChannelOption tcl_SetChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, tcl_SetCommandInfo tcl_SetCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Tcl_CmdInfo>) -> Int32)!, tcl_SetErrno tcl_SetErrno: ((Int32) -> Void)!, tcl_SetErrorCode tcl_SetErrorCode: COpaquePointer, tcl_SetMaxBlockTime tcl_SetMaxBlockTime: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!, tcl_SetPanicProc tcl_SetPanicProc: ((COpaquePointer) -> Void)!, tcl_SetRecursionLimit tcl_SetRecursionLimit: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, tcl_SetResult tcl_SetResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Int8>, ((UnsafeMutablePointer<Int8>) -> Void)!) -> Void)!, tcl_SetServiceMode tcl_SetServiceMode: ((Int32) -> Int32)!, tcl_SetObjErrorCode tcl_SetObjErrorCode: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_SetObjResult tcl_SetObjResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_SetStdChannel tcl_SetStdChannel: ((Tcl_Channel, Int32) -> Void)!, tcl_SetVar tcl_SetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_SetVar2 tcl_SetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_SignalId tcl_SignalId: ((Int32) -> UnsafePointer<Int8>)!, tcl_SignalMsg tcl_SignalMsg: ((Int32) -> UnsafePointer<Int8>)!, tcl_SourceRCFile tcl_SourceRCFile: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!, tcl_SplitList tcl_SplitList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)!, tcl_SplitPath tcl_SplitPath: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Void)!, tcl_StaticPackage tcl_StaticPackage: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!) -> Void)!, tcl_StringMatch tcl_StringMatch: ((UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, tcl_TellOld tcl_TellOld: ((Tcl_Channel) -> Int32)!, tcl_TraceVar tcl_TraceVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Int32)!, tcl_TraceVar2 tcl_TraceVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Int32)!, tcl_TranslateFileName tcl_TranslateFileName: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!, tcl_Ungets tcl_Ungets: ((Tcl_Channel, UnsafePointer<Int8>, Int32, Int32) -> Int32)!, tcl_UnlinkVar tcl_UnlinkVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!, tcl_UnregisterChannel tcl_UnregisterChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!, tcl_UnsetVar tcl_UnsetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_UnsetVar2 tcl_UnsetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_UntraceVar tcl_UntraceVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Void)!, tcl_UntraceVar2 tcl_UntraceVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Void)!, tcl_UpdateLinkedVar tcl_UpdateLinkedVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)!, tcl_UpVar tcl_UpVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_UpVar2 tcl_UpVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_VarEval tcl_VarEval: COpaquePointer, tcl_VarTraceInfo tcl_VarTraceInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> ClientData)!, tcl_VarTraceInfo2 tcl_VarTraceInfo2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> ClientData)!, tcl_Write tcl_Write: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_WrongNumArgs tcl_WrongNumArgs: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>) -> Void)!, tcl_DumpActiveMemory tcl_DumpActiveMemory: ((UnsafePointer<Int8>) -> Int32)!, tcl_ValidateAllMemory tcl_ValidateAllMemory: ((UnsafePointer<Int8>, Int32) -> Void)!, tcl_AppendResultVA tcl_AppendResultVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)!, tcl_AppendStringsToObjVA tcl_AppendStringsToObjVA: ((UnsafeMutablePointer<Tcl_Obj>, CVaListPointer) -> Void)!, tcl_HashStats tcl_HashStats: ((UnsafeMutablePointer<Tcl_HashTable>) -> UnsafeMutablePointer<Int8>)!, tcl_ParseVar tcl_ParseVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> UnsafePointer<Int8>)!, tcl_PkgPresent tcl_PkgPresent: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_PkgPresentEx tcl_PkgPresentEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)!, tcl_PkgProvide tcl_PkgProvide: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!, tcl_PkgRequire tcl_PkgRequire: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_SetErrorCodeVA tcl_SetErrorCodeVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)!, tcl_VarEvalVA tcl_VarEvalVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Int32)!, tcl_WaitPid tcl_WaitPid: ((Tcl_Pid, UnsafeMutablePointer<Int32>, Int32) -> Tcl_Pid)!, tcl_PanicVA tcl_PanicVA: ((UnsafePointer<Int8>, CVaListPointer) -> Void)!, tcl_GetVersion tcl_GetVersion: ((UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Void)!, tcl_InitMemory tcl_InitMemory: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!, tcl_StackChannel tcl_StackChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_ChannelType>, ClientData, Int32, Tcl_Channel) -> Tcl_Channel)!, tcl_UnstackChannel tcl_UnstackChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!, tcl_GetStackedChannel tcl_GetStackedChannel: ((Tcl_Channel) -> Tcl_Channel)!, tcl_SetMainLoop tcl_SetMainLoop: (((() -> Void)!) -> Void)!, reserved285 reserved285: UnsafeMutablePointer<Void>, tcl_AppendObjToObj tcl_AppendObjToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_CreateEncoding tcl_CreateEncoding: ((UnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding)!, tcl_CreateThreadExitHandler tcl_CreateThreadExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)!, tcl_DeleteThreadExitHandler tcl_DeleteThreadExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)!, tcl_DiscardResult tcl_DiscardResult: ((UnsafeMutablePointer<Tcl_SavedResult>) -> Void)!, tcl_EvalEx tcl_EvalEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32) -> Int32)!, tcl_EvalObjv tcl_EvalObjv: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, Int32) -> Int32)!, tcl_EvalObjEx tcl_EvalObjEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!, tcl_ExitThread tcl_ExitThread: ((Int32) -> Void)!, tcl_ExternalToUtf tcl_ExternalToUtf: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_ExternalToUtfDString tcl_ExternalToUtfDString: ((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!, tcl_FinalizeThread tcl_FinalizeThread: (() -> Void)!, tcl_FinalizeNotifier tcl_FinalizeNotifier: ((ClientData) -> Void)!, tcl_FreeEncoding tcl_FreeEncoding: ((Tcl_Encoding) -> Void)!, tcl_GetCurrentThread tcl_GetCurrentThread: (() -> Tcl_ThreadId)!, tcl_GetEncoding tcl_GetEncoding: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_Encoding)!, tcl_GetEncodingName tcl_GetEncodingName: ((Tcl_Encoding) -> UnsafePointer<Int8>)!, tcl_GetEncodingNames tcl_GetEncodingNames: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)!, tcl_GetIndexFromObjStruct tcl_GetIndexFromObjStruct: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Void>, Int32, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_GetThreadData tcl_GetThreadData: ((UnsafeMutablePointer<Tcl_ThreadDataKey>, Int32) -> UnsafeMutablePointer<Void>)!, tcl_GetVar2Ex tcl_GetVar2Ex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_InitNotifier tcl_InitNotifier: (() -> ClientData)!, tcl_MutexLock tcl_MutexLock: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)!, tcl_MutexUnlock tcl_MutexUnlock: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)!, tcl_ConditionNotify tcl_ConditionNotify: ((UnsafeMutablePointer<Tcl_Condition>) -> Void)!, tcl_ConditionWait tcl_ConditionWait: ((UnsafeMutablePointer<Tcl_Condition>, UnsafeMutablePointer<Tcl_Mutex>, UnsafeMutablePointer<Tcl_Time>) -> Void)!, tcl_NumUtfChars tcl_NumUtfChars: ((UnsafePointer<Int8>, Int32) -> Int32)!, tcl_ReadChars tcl_ReadChars: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Int32)!, tcl_RestoreResult tcl_RestoreResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)!, tcl_SaveResult tcl_SaveResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)!, tcl_SetSystemEncoding tcl_SetSystemEncoding: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!, tcl_SetVar2Ex tcl_SetVar2Ex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_ThreadAlert tcl_ThreadAlert: ((Tcl_ThreadId) -> Void)!, tcl_ThreadQueueEvent tcl_ThreadQueueEvent: ((Tcl_ThreadId, UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)!, tcl_UniCharAtIndex tcl_UniCharAtIndex: ((UnsafePointer<Int8>, Int32) -> Tcl_UniChar)!, tcl_UniCharToLower tcl_UniCharToLower: ((Int32) -> Tcl_UniChar)!, tcl_UniCharToTitle tcl_UniCharToTitle: ((Int32) -> Tcl_UniChar)!, tcl_UniCharToUpper tcl_UniCharToUpper: ((Int32) -> Tcl_UniChar)!, tcl_UniCharToUtf tcl_UniCharToUtf: ((Int32, UnsafeMutablePointer<Int8>) -> Int32)!, tcl_UtfAtIndex tcl_UtfAtIndex: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_UtfCharComplete tcl_UtfCharComplete: ((UnsafePointer<Int8>, Int32) -> Int32)!, tcl_UtfBackslash tcl_UtfBackslash: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int8>) -> Int32)!, tcl_UtfFindFirst tcl_UtfFindFirst: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_UtfFindLast tcl_UtfFindLast: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)!, tcl_UtfNext tcl_UtfNext: ((UnsafePointer<Int8>) -> UnsafePointer<Int8>)!, tcl_UtfPrev tcl_UtfPrev: ((UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafePointer<Int8>)!, tcl_UtfToExternal tcl_UtfToExternal: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_UtfToExternalDString tcl_UtfToExternalDString: ((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!, tcl_UtfToLower tcl_UtfToLower: ((UnsafeMutablePointer<Int8>) -> Int32)!, tcl_UtfToTitle tcl_UtfToTitle: ((UnsafeMutablePointer<Int8>) -> Int32)!, tcl_UtfToUniChar tcl_UtfToUniChar: ((UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_UniChar>) -> Int32)!, tcl_UtfToUpper tcl_UtfToUpper: ((UnsafeMutablePointer<Int8>) -> Int32)!, tcl_WriteChars tcl_WriteChars: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_WriteObj tcl_WriteObj: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_GetString tcl_GetString: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Int8>)!, tcl_GetDefaultEncodingDir tcl_GetDefaultEncodingDir: (() -> UnsafePointer<Int8>)!, tcl_SetDefaultEncodingDir tcl_SetDefaultEncodingDir: ((UnsafePointer<Int8>) -> Void)!, tcl_AlertNotifier tcl_AlertNotifier: ((ClientData) -> Void)!, tcl_ServiceModeHook tcl_ServiceModeHook: ((Int32) -> Void)!, tcl_UniCharIsAlnum tcl_UniCharIsAlnum: ((Int32) -> Int32)!, tcl_UniCharIsAlpha tcl_UniCharIsAlpha: ((Int32) -> Int32)!, tcl_UniCharIsDigit tcl_UniCharIsDigit: ((Int32) -> Int32)!, tcl_UniCharIsLower tcl_UniCharIsLower: ((Int32) -> Int32)!, tcl_UniCharIsSpace tcl_UniCharIsSpace: ((Int32) -> Int32)!, tcl_UniCharIsUpper tcl_UniCharIsUpper: ((Int32) -> Int32)!, tcl_UniCharIsWordChar tcl_UniCharIsWordChar: ((Int32) -> Int32)!, tcl_UniCharLen tcl_UniCharLen: ((UnsafePointer<Tcl_UniChar>) -> Int32)!, tcl_UniCharNcmp tcl_UniCharNcmp: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)!, tcl_UniCharToUtfDString tcl_UniCharToUtfDString: ((UnsafePointer<Tcl_UniChar>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!, tcl_UtfToUniCharDString tcl_UtfToUniCharDString: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Tcl_UniChar>)!, tcl_GetRegExpFromObj tcl_GetRegExpFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_RegExp)!, tcl_EvalTokens tcl_EvalTokens: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FreeParse tcl_FreeParse: ((UnsafeMutablePointer<Tcl_Parse>) -> Void)!, tcl_LogCommandInfo tcl_LogCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, tcl_ParseBraces tcl_ParseBraces: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, tcl_ParseCommand tcl_ParseCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)!, tcl_ParseExpr tcl_ParseExpr: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)!, tcl_ParseQuotedString tcl_ParseQuotedString: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, tcl_ParseVarName tcl_ParseVarName: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32) -> Int32)!, tcl_GetCwd tcl_GetCwd: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)!, tcl_Chdir tcl_Chdir: ((UnsafePointer<Int8>) -> Int32)!, tcl_Access tcl_Access: ((UnsafePointer<Int8>, Int32) -> Int32)!, tcl_Stat tcl_Stat: ((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)!, tcl_UtfNcmp tcl_UtfNcmp: ((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)!, tcl_UtfNcasecmp tcl_UtfNcasecmp: ((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)!, tcl_StringCaseMatch tcl_StringCaseMatch: ((UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_UniCharIsControl tcl_UniCharIsControl: ((Int32) -> Int32)!, tcl_UniCharIsGraph tcl_UniCharIsGraph: ((Int32) -> Int32)!, tcl_UniCharIsPrint tcl_UniCharIsPrint: ((Int32) -> Int32)!, tcl_UniCharIsPunct tcl_UniCharIsPunct: ((Int32) -> Int32)!, tcl_RegExpExecObj tcl_RegExpExecObj: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32) -> Int32)!, tcl_RegExpGetInfo tcl_RegExpGetInfo: ((Tcl_RegExp, UnsafeMutablePointer<Tcl_RegExpInfo>) -> Void)!, tcl_NewUnicodeObj tcl_NewUnicodeObj: ((UnsafePointer<Tcl_UniChar>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_SetUnicodeObj tcl_SetUnicodeObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)!, tcl_GetCharLength tcl_GetCharLength: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_GetUniChar tcl_GetUniChar: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_UniChar)!, tcl_GetUnicode tcl_GetUnicode: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_UniChar>)!, tcl_GetRange tcl_GetRange: ((UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_AppendUnicodeToObj tcl_AppendUnicodeToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)!, tcl_RegExpMatchObj tcl_RegExpMatchObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_SetNotifier tcl_SetNotifier: ((UnsafeMutablePointer<Tcl_NotifierProcs>) -> Void)!, tcl_GetAllocMutex tcl_GetAllocMutex: (() -> UnsafeMutablePointer<Tcl_Mutex>)!, tcl_GetChannelNames tcl_GetChannelNames: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_GetChannelNamesEx tcl_GetChannelNamesEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)!, tcl_ProcObjCmd tcl_ProcObjCmd: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_ConditionFinalize tcl_ConditionFinalize: ((UnsafeMutablePointer<Tcl_Condition>) -> Void)!, tcl_MutexFinalize tcl_MutexFinalize: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)!, tcl_CreateThread tcl_CreateThread: ((UnsafeMutablePointer<Tcl_ThreadId>, ((ClientData) -> Void)!, ClientData, Int32, Int32) -> Int32)!, tcl_ReadRaw tcl_ReadRaw: ((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)!, tcl_WriteRaw tcl_WriteRaw: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_GetTopChannel tcl_GetTopChannel: ((Tcl_Channel) -> Tcl_Channel)!, tcl_ChannelBuffered tcl_ChannelBuffered: ((Tcl_Channel) -> Int32)!, tcl_ChannelName tcl_ChannelName: ((UnsafePointer<Tcl_ChannelType>) -> UnsafePointer<Int8>)!, tcl_ChannelVersion tcl_ChannelVersion: ((UnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion)!, tcl_ChannelBlockModeProc tcl_ChannelBlockModeProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)!)!, tcl_ChannelCloseProc tcl_ChannelCloseProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!)!, tcl_ChannelClose2Proc tcl_ChannelClose2Proc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!)!, tcl_ChannelInputProc tcl_ChannelInputProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)!, tcl_ChannelOutputProc tcl_ChannelOutputProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)!, tcl_ChannelSeekProc tcl_ChannelSeekProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)!, tcl_ChannelSetOptionProc tcl_ChannelSetOptionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!)!, tcl_ChannelGetOptionProc tcl_ChannelGetOptionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!)!, tcl_ChannelWatchProc tcl_ChannelWatchProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)!)!, tcl_ChannelGetHandleProc tcl_ChannelGetHandleProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!)!, tcl_ChannelFlushProc tcl_ChannelFlushProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData) -> Int32)!)!, tcl_ChannelHandlerProc tcl_ChannelHandlerProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)!)!, tcl_JoinThread tcl_JoinThread: ((Tcl_ThreadId, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_IsChannelShared tcl_IsChannelShared: ((Tcl_Channel) -> Int32)!, tcl_IsChannelRegistered tcl_IsChannelRegistered: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!, tcl_CutChannel tcl_CutChannel: ((Tcl_Channel) -> Void)!, tcl_SpliceChannel tcl_SpliceChannel: ((Tcl_Channel) -> Void)!, tcl_ClearChannelHandlers tcl_ClearChannelHandlers: ((Tcl_Channel) -> Void)!, tcl_IsChannelExisting tcl_IsChannelExisting: ((UnsafePointer<Int8>) -> Int32)!, tcl_UniCharNcasecmp tcl_UniCharNcasecmp: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)!, tcl_UniCharCaseMatch tcl_UniCharCaseMatch: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, Int32) -> Int32)!, tcl_FindHashEntry tcl_FindHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, tcl_CreateHashEntry tcl_CreateHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)!, tcl_InitCustomHashTable tcl_InitCustomHashTable: ((UnsafeMutablePointer<Tcl_HashTable>, Int32, UnsafeMutablePointer<Tcl_HashKeyType>) -> Void)!, tcl_InitObjHashTable tcl_InitObjHashTable: ((UnsafeMutablePointer<Tcl_HashTable>) -> Void)!, tcl_CommandTraceInfo tcl_CommandTraceInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> ClientData)!, tcl_TraceCommand tcl_TraceCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> Int32)!, tcl_UntraceCommand tcl_UntraceCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> Void)!, tcl_AttemptAlloc tcl_AttemptAlloc: ((UInt32) -> UnsafeMutablePointer<Int8>)!, tcl_AttemptDbCkalloc tcl_AttemptDbCkalloc: ((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, tcl_AttemptRealloc tcl_AttemptRealloc: ((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)!, tcl_AttemptDbCkrealloc tcl_AttemptDbCkrealloc: ((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, tcl_AttemptSetObjLength tcl_AttemptSetObjLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!, tcl_GetChannelThread tcl_GetChannelThread: ((Tcl_Channel) -> Tcl_ThreadId)!, tcl_GetUnicodeFromObj tcl_GetUnicodeFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_UniChar>)!, tcl_GetMathFuncInfo tcl_GetMathFuncInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)?>, UnsafeMutablePointer<ClientData>) -> Int32)!, tcl_ListMathFuncs tcl_ListMathFuncs: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_SubstObj tcl_SubstObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DetachChannel tcl_DetachChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)!, tcl_IsStandardChannel tcl_IsStandardChannel: ((Tcl_Channel) -> Int32)!, tcl_FSCopyFile tcl_FSCopyFile: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSCopyDirectory tcl_FSCopyDirectory: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_FSCreateDirectory tcl_FSCreateDirectory: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSDeleteFile tcl_FSDeleteFile: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSLoadFile tcl_FSLoadFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32)!, tcl_FSMatchInDirectory tcl_FSMatchInDirectory: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)!, tcl_FSLink tcl_FSLink: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSRemoveDirectory tcl_FSRemoveDirectory: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_FSRenameFile tcl_FSRenameFile: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSLstat tcl_FSLstat: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!, tcl_FSUtime tcl_FSUtime: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)!, tcl_FSFileAttrsGet tcl_FSFileAttrsGet: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_FSFileAttrsSet tcl_FSFileAttrsSet: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSFileAttrStrings tcl_FSFileAttrStrings: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)!, tcl_FSStat tcl_FSStat: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)!, tcl_FSAccess tcl_FSAccess: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)!, tcl_FSOpenFileChannel tcl_FSOpenFileChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)!, tcl_FSGetCwd tcl_FSGetCwd: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSChdir tcl_FSChdir: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSConvertToPathType tcl_FSConvertToPathType: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSJoinPath tcl_FSJoinPath: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSSplitPath tcl_FSSplitPath: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSEqualPaths tcl_FSEqualPaths: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSGetNormalizedPath tcl_FSGetNormalizedPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSJoinToPath tcl_FSJoinToPath: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSGetInternalRep tcl_FSGetInternalRep: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)!, tcl_FSGetTranslatedPath tcl_FSGetTranslatedPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSEvalFile tcl_FSEvalFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_FSNewNativePath tcl_FSNewNativePath: ((UnsafeMutablePointer<Tcl_Filesystem>, ClientData) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSGetNativePath tcl_FSGetNativePath: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)!, tcl_FSFileSystemInfo tcl_FSFileSystemInfo: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSPathSeparator tcl_FSPathSeparator: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSListVolumes tcl_FSListVolumes: (() -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_FSRegister tcl_FSRegister: ((ClientData, UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)!, tcl_FSUnregister tcl_FSUnregister: ((UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)!, tcl_FSData tcl_FSData: ((UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)!, tcl_FSGetTranslatedStringPath tcl_FSGetTranslatedStringPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)!, tcl_FSGetFileSystemForPath tcl_FSGetFileSystemForPath: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Filesystem>)!, tcl_FSGetPathType tcl_FSGetPathType: ((UnsafeMutablePointer<Tcl_Obj>) -> Tcl_PathType)!, tcl_OutputBuffered tcl_OutputBuffered: ((Tcl_Channel) -> Int32)!, tcl_FSMountsChanged tcl_FSMountsChanged: ((UnsafeMutablePointer<Tcl_Filesystem>) -> Void)!, tcl_EvalTokensStandard tcl_EvalTokensStandard: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> Int32)!, tcl_GetTime tcl_GetTime: ((UnsafeMutablePointer<Tcl_Time>) -> Void)!, tcl_CreateObjTrace tcl_CreateObjTrace: ((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, Tcl_Command, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Trace)!, tcl_GetCommandInfoFromToken tcl_GetCommandInfoFromToken: ((Tcl_Command, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)!, tcl_SetCommandInfoFromToken tcl_SetCommandInfoFromToken: ((Tcl_Command, UnsafePointer<Tcl_CmdInfo>) -> Int32)!, tcl_DbNewWideIntObj tcl_DbNewWideIntObj: ((Tcl_WideInt, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_GetWideIntFromObj tcl_GetWideIntFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_WideInt>) -> Int32)!, tcl_NewWideIntObj tcl_NewWideIntObj: ((Tcl_WideInt) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_SetWideIntObj tcl_SetWideIntObj: ((UnsafeMutablePointer<Tcl_Obj>, Tcl_WideInt) -> Void)!, tcl_AllocStatBuf tcl_AllocStatBuf: (() -> UnsafeMutablePointer<Tcl_StatBuf>)!, tcl_Seek tcl_Seek: ((Tcl_Channel, Tcl_WideInt, Int32) -> Tcl_WideInt)!, tcl_Tell tcl_Tell: ((Tcl_Channel) -> Tcl_WideInt)!, tcl_ChannelWideSeekProc tcl_ChannelWideSeekProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)!)!, tcl_DictObjPut tcl_DictObjPut: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_DictObjGet tcl_DictObjGet: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_DictObjRemove tcl_DictObjRemove: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_DictObjSize tcl_DictObjSize: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_DictObjFirst tcl_DictObjFirst: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_DictObjNext tcl_DictObjNext: ((UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Void)!, tcl_DictObjDone tcl_DictObjDone: ((UnsafeMutablePointer<Tcl_DictSearch>) -> Void)!, tcl_DictObjPutKeyList tcl_DictObjPutKeyList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_DictObjRemoveKeyList tcl_DictObjRemoveKeyList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_NewDictObj tcl_NewDictObj: (() -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DbNewDictObj tcl_DbNewDictObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_RegisterConfig tcl_RegisterConfig: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Config>, UnsafePointer<Int8>) -> Void)!, tcl_CreateNamespace tcl_CreateNamespace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ClientData, ((ClientData) -> Void)!) -> UnsafeMutablePointer<Tcl_Namespace>)!, tcl_DeleteNamespace tcl_DeleteNamespace: ((UnsafeMutablePointer<Tcl_Namespace>) -> Void)!, tcl_AppendExportList tcl_AppendExportList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_Export tcl_Export: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_Import tcl_Import: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)!, tcl_ForgetImport tcl_ForgetImport: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>) -> Int32)!, tcl_GetCurrentNamespace tcl_GetCurrentNamespace: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)!, tcl_GetGlobalNamespace tcl_GetGlobalNamespace: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)!, tcl_FindNamespace tcl_FindNamespace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> UnsafeMutablePointer<Tcl_Namespace>)!, tcl_FindCommand tcl_FindCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)!, tcl_GetCommandFromObj tcl_GetCommandFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Tcl_Command)!, tcl_GetCommandFullName tcl_GetCommandFullName: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_FSEvalFileEx tcl_FSEvalFileEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>) -> Int32)!, tcl_SetExitProc tcl_SetExitProc: ((((ClientData) -> Void)!) -> ((ClientData) -> Void)!)!, tcl_LimitAddHandler tcl_LimitAddHandler: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData, ((ClientData) -> Void)!) -> Void)!, tcl_LimitRemoveHandler tcl_LimitRemoveHandler: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)!, tcl_LimitReady tcl_LimitReady: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_LimitCheck tcl_LimitCheck: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_LimitExceeded tcl_LimitExceeded: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_LimitSetCommands tcl_LimitSetCommands: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)!, tcl_LimitSetTime tcl_LimitSetTime: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)!, tcl_LimitSetGranularity tcl_LimitSetGranularity: ((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32) -> Void)!, tcl_LimitTypeEnabled tcl_LimitTypeEnabled: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, tcl_LimitTypeExceeded tcl_LimitTypeExceeded: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, tcl_LimitTypeSet tcl_LimitTypeSet: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)!, tcl_LimitTypeReset tcl_LimitTypeReset: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)!, tcl_LimitGetCommands tcl_LimitGetCommands: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, tcl_LimitGetTime tcl_LimitGetTime: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)!, tcl_LimitGetGranularity tcl_LimitGetGranularity: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, tcl_SaveInterpState tcl_SaveInterpState: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Tcl_InterpState)!, tcl_RestoreInterpState tcl_RestoreInterpState: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_InterpState) -> Int32)!, tcl_DiscardInterpState tcl_DiscardInterpState: ((Tcl_InterpState) -> Void)!, tcl_SetReturnOptions tcl_SetReturnOptions: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_GetReturnOptions tcl_GetReturnOptions: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_IsEnsemble tcl_IsEnsemble: ((Tcl_Command) -> Int32)!, tcl_CreateEnsemble tcl_CreateEnsemble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)!, tcl_FindEnsemble tcl_FindEnsemble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_Command)!, tcl_SetEnsembleSubcommandList tcl_SetEnsembleSubcommandList: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_SetEnsembleMappingDict tcl_SetEnsembleMappingDict: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_SetEnsembleUnknownHandler tcl_SetEnsembleUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_SetEnsembleFlags tcl_SetEnsembleFlags: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, Int32) -> Int32)!, tcl_GetEnsembleSubcommandList tcl_GetEnsembleSubcommandList: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_GetEnsembleMappingDict tcl_GetEnsembleMappingDict: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_GetEnsembleUnknownHandler tcl_GetEnsembleUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_GetEnsembleFlags tcl_GetEnsembleFlags: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Int32>) -> Int32)!, tcl_GetEnsembleNamespace tcl_GetEnsembleNamespace: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Namespace>>) -> Int32)!, tcl_SetTimeProc tcl_SetTimeProc: ((((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, ClientData) -> Void)!, tcl_QueryTimeProc tcl_QueryTimeProc: ((UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, UnsafeMutablePointer<ClientData>) -> Void)!, tcl_ChannelThreadActionProc tcl_ChannelThreadActionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)!)!, tcl_NewBignumObj tcl_NewBignumObj: ((UnsafeMutablePointer<mp_int>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_DbNewBignumObj tcl_DbNewBignumObj: ((UnsafeMutablePointer<mp_int>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_SetBignumObj tcl_SetBignumObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Void)!, tcl_GetBignumFromObj tcl_GetBignumFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)!, tcl_TakeBignumFromObj tcl_TakeBignumFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)!, tcl_TruncateChannel tcl_TruncateChannel: ((Tcl_Channel, Tcl_WideInt) -> Int32)!, tcl_ChannelTruncateProc tcl_ChannelTruncateProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt) -> Int32)!)!, tcl_SetChannelErrorInterp tcl_SetChannelErrorInterp: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_GetChannelErrorInterp tcl_GetChannelErrorInterp: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)!, tcl_SetChannelError tcl_SetChannelError: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_GetChannelError tcl_GetChannelError: ((Tcl_Channel, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)!, tcl_InitBignumFromDouble tcl_InitBignumFromDouble: ((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<mp_int>) -> Int32)!, tcl_GetNamespaceUnknownHandler tcl_GetNamespaceUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_SetNamespaceUnknownHandler tcl_SetNamespaceUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_GetEncodingFromObj tcl_GetEncodingFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Encoding>) -> Int32)!, tcl_GetEncodingSearchPath tcl_GetEncodingSearchPath: (() -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_SetEncodingSearchPath tcl_SetEncodingSearchPath: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)!, tcl_GetEncodingNameFromEnvironment tcl_GetEncodingNameFromEnvironment: ((UnsafeMutablePointer<Tcl_DString>) -> UnsafePointer<Int8>)!, tcl_PkgRequireProc tcl_PkgRequireProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<ClientData>) -> Int32)!, tcl_AppendObjToErrorInfo tcl_AppendObjToErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)!, tcl_AppendLimitedToObj tcl_AppendLimitedToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, Int32, UnsafePointer<Int8>) -> Void)!, tcl_Format tcl_Format: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)!, tcl_AppendFormatToObj tcl_AppendFormatToObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, tcl_ObjPrintf tcl_ObjPrintf: COpaquePointer, tcl_AppendPrintfToObj tcl_AppendPrintfToObj: COpaquePointer) } ``` |

Modified TclStubs.tcl_Access

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Access: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Access: ((UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_AddErrorInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AddErrorInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_AddErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_AddObjErrorInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AddObjErrorInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_AddObjErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_AlertNotifier

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AlertNotifier: CFunctionPointer<((ClientData) -> Void)> ``` |
| To | ``` var tcl_AlertNotifier: ((ClientData) -> Void)! ``` |

Modified TclStubs.tcl_Alloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Alloc: CFunctionPointer<((UInt32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_Alloc: ((UInt32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_AllocStatBuf

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AllocStatBuf: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_StatBuf>)> ``` |
| To | ``` var tcl_AllocStatBuf: (() -> UnsafeMutablePointer<Tcl_StatBuf>)! ``` |

Modified TclStubs.tcl_AllowExceptions

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AllowExceptions: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_AllowExceptions: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)! ``` |

Modified TclStubs.tcl_AppendAllObjTypes

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendAllObjTypes: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_AppendAllObjTypes: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_AppendElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendElement: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_AppendElement: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_AppendExportList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendExportList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_AppendExportList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_AppendFormatToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendFormatToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_AppendFormatToObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_AppendLimitedToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendLimitedToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, Int32, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_AppendLimitedToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32, Int32, UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_AppendObjToErrorInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendObjToErrorInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_AppendObjToErrorInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified TclStubs.tcl_AppendObjToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendObjToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_AppendObjToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified TclStubs.tcl_AppendResultVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendResultVA: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)> ``` |
| To | ``` var tcl_AppendResultVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)! ``` |

Modified TclStubs.tcl_AppendStringsToObjVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendStringsToObjVA: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, CVaListPointer) -> Void)> ``` |
| To | ``` var tcl_AppendStringsToObjVA: ((UnsafeMutablePointer<Tcl_Obj>, CVaListPointer) -> Void)! ``` |

Modified TclStubs.tcl_AppendToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_AppendToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_AppendUnicodeToObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AppendUnicodeToObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)> ``` |
| To | ``` var tcl_AppendUnicodeToObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_AsyncCreate

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AsyncCreate: CFunctionPointer<((CFunctionPointer<Tcl_AsyncProc>, ClientData) -> Tcl_AsyncHandler)> ``` |
| To | ``` var tcl_AsyncCreate: ((((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, ClientData) -> Tcl_AsyncHandler)! ``` |

Modified TclStubs.tcl_AsyncDelete

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AsyncDelete: CFunctionPointer<((Tcl_AsyncHandler) -> Void)> ``` |
| To | ``` var tcl_AsyncDelete: ((Tcl_AsyncHandler) -> Void)! ``` |

Modified TclStubs.tcl_AsyncInvoke

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AsyncInvoke: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_AsyncInvoke: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_AsyncMark

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AsyncMark: CFunctionPointer<((Tcl_AsyncHandler) -> Void)> ``` |
| To | ``` var tcl_AsyncMark: ((Tcl_AsyncHandler) -> Void)! ``` |

Modified TclStubs.tcl_AsyncReady

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AsyncReady: CFunctionPointer<(() -> Int32)> ``` |
| To | ``` var tcl_AsyncReady: (() -> Int32)! ``` |

Modified TclStubs.tcl_AttemptAlloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptAlloc: CFunctionPointer<((UInt32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_AttemptAlloc: ((UInt32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_AttemptDbCkalloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptDbCkalloc: CFunctionPointer<((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_AttemptDbCkalloc: ((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_AttemptDbCkrealloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptDbCkrealloc: CFunctionPointer<((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_AttemptDbCkrealloc: ((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_AttemptRealloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptRealloc: CFunctionPointer<((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_AttemptRealloc: ((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_AttemptSetObjLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_AttemptSetObjLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)> ``` |
| To | ``` var tcl_AttemptSetObjLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_BackgroundError

|  | Declaration |
| --- | --- |
| From | ``` var tcl_BackgroundError: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_BackgroundError: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)! ``` |

Modified TclStubs.tcl_Backslash

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Backslash: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int8)> ``` |
| To | ``` var tcl_Backslash: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int8)! ``` |

Modified TclStubs.tcl_BadChannelOption

|  | Declaration |
| --- | --- |
| From | ``` var tcl_BadChannelOption: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_BadChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_CallWhenDeleted

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CallWhenDeleted: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CallWhenDeleted: ((UnsafeMutablePointer<Tcl_Interp>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_CancelIdleCall

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CancelIdleCall: CFunctionPointer<((CFunctionPointer<Tcl_IdleProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CancelIdleCall: ((((ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_ChannelBlockModeProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelBlockModeProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverBlockModeProc>)> ``` |
| To | ``` var tcl_ChannelBlockModeProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelBuffered

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelBuffered: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_ChannelBuffered: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_ChannelClose2Proc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelClose2Proc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverClose2Proc>)> ``` |
| To | ``` var tcl_ChannelClose2Proc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelCloseProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelCloseProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverCloseProc>)> ``` |
| To | ``` var tcl_ChannelCloseProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelFlushProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelFlushProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverFlushProc>)> ``` |
| To | ``` var tcl_ChannelFlushProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelGetHandleProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelGetHandleProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetHandleProc>)> ``` |
| To | ``` var tcl_ChannelGetHandleProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelGetOptionProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelGetOptionProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetOptionProc>)> ``` |
| To | ``` var tcl_ChannelGetOptionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelHandlerProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelHandlerProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverHandlerProc>)> ``` |
| To | ``` var tcl_ChannelHandlerProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelInputProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelInputProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverInputProc>)> ``` |
| To | ``` var tcl_ChannelInputProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelName: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ChannelName: ((UnsafePointer<Tcl_ChannelType>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_ChannelOutputProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelOutputProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverOutputProc>)> ``` |
| To | ``` var tcl_ChannelOutputProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelSeekProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelSeekProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSeekProc>)> ``` |
| To | ``` var tcl_ChannelSeekProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelSetOptionProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelSetOptionProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSetOptionProc>)> ``` |
| To | ``` var tcl_ChannelSetOptionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelThreadActionProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelThreadActionProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverThreadActionProc>)> ``` |
| To | ``` var tcl_ChannelThreadActionProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)!)! ``` |

Modified TclStubs.tcl_ChannelTruncateProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelTruncateProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverTruncateProc>)> ``` |
| To | ``` var tcl_ChannelTruncateProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt) -> Int32)!)! ``` |

Modified TclStubs.tcl_ChannelVersion

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelVersion: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion)> ``` |
| To | ``` var tcl_ChannelVersion: ((UnsafePointer<Tcl_ChannelType>) -> Tcl_ChannelTypeVersion)! ``` |

Modified TclStubs.tcl_ChannelWatchProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelWatchProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWatchProc>)> ``` |
| To | ``` var tcl_ChannelWatchProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)!)! ``` |

Modified TclStubs.tcl_ChannelWideSeekProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ChannelWideSeekProc: CFunctionPointer<((UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWideSeekProc>)> ``` |
| To | ``` var tcl_ChannelWideSeekProc: ((UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)!)! ``` |

Modified TclStubs.tcl_Chdir

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Chdir: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_Chdir: ((UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_ClearChannelHandlers

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ClearChannelHandlers: CFunctionPointer<((Tcl_Channel) -> Void)> ``` |
| To | ``` var tcl_ClearChannelHandlers: ((Tcl_Channel) -> Void)! ``` |

Modified TclStubs.tcl_Close

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Close: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_Close: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_CommandComplete

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CommandComplete: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_CommandComplete: ((UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_CommandTraceInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CommandTraceInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> ClientData)> ``` |
| To | ``` var tcl_CommandTraceInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> ClientData)! ``` |

Modified TclStubs.tcl_Concat

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Concat: CFunctionPointer<((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_Concat: ((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_ConcatObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConcatObj: CFunctionPointer<((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_ConcatObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_ConditionFinalize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConditionFinalize: CFunctionPointer<((UnsafeMutablePointer<Tcl_Condition>) -> Void)> ``` |
| To | ``` var tcl_ConditionFinalize: ((UnsafeMutablePointer<Tcl_Condition>) -> Void)! ``` |

Modified TclStubs.tcl_ConditionNotify

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConditionNotify: CFunctionPointer<((UnsafeMutablePointer<Tcl_Condition>) -> Void)> ``` |
| To | ``` var tcl_ConditionNotify: ((UnsafeMutablePointer<Tcl_Condition>) -> Void)! ``` |

Modified TclStubs.tcl_ConditionWait

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConditionWait: CFunctionPointer<((UnsafeMutablePointer<Tcl_Condition>, UnsafeMutablePointer<Tcl_Mutex>, UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_ConditionWait: ((UnsafeMutablePointer<Tcl_Condition>, UnsafeMutablePointer<Tcl_Mutex>, UnsafeMutablePointer<Tcl_Time>) -> Void)! ``` |

Modified TclStubs.tcl_ConvertCountedElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConvertCountedElement: CFunctionPointer<((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_ConvertCountedElement: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ConvertElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConvertElement: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_ConvertElement: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ConvertToType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ConvertToType: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_ObjType>) -> Int32)> ``` |
| To | ``` var tcl_ConvertToType: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_ObjType>) -> Int32)! ``` |

Modified TclStubs.tcl_CreateAlias

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateAlias: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafePointer<Int8>>) -> Int32)> ``` |
| To | ``` var tcl_CreateAlias: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafePointer<Int8>>) -> Int32)! ``` |

Modified TclStubs.tcl_CreateAliasObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateAliasObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_CreateAliasObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_CreateChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_ChannelType>, UnsafePointer<Int8>, ClientData, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_CreateChannel: ((UnsafeMutablePointer<Tcl_ChannelType>, UnsafePointer<Int8>, ClientData, Int32) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_CreateChannelHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateChannelHandler: CFunctionPointer<((Tcl_Channel, Int32, CFunctionPointer<Tcl_ChannelProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CreateChannelHandler: ((Tcl_Channel, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_CreateCloseHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateCloseHandler: CFunctionPointer<((Tcl_Channel, CFunctionPointer<Tcl_CloseProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CreateCloseHandler: ((Tcl_Channel, ((ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_CreateCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_CmdProc>, ClientData, CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command)> ``` |
| To | ``` var tcl_CreateCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Command)! ``` |

Modified TclStubs.tcl_CreateEncoding

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateEncoding: CFunctionPointer<((UnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding)> ``` |
| To | ``` var tcl_CreateEncoding: ((UnsafePointer<Tcl_EncodingType>) -> Tcl_Encoding)! ``` |

Modified TclStubs.tcl_CreateEnsemble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateEnsemble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)> ``` |
| To | ``` var tcl_CreateEnsemble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)! ``` |

Modified TclStubs.tcl_CreateEventSource

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateEventSource: CFunctionPointer<((CFunctionPointer<Tcl_EventSetupProc>, CFunctionPointer<Tcl_EventCheckProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CreateEventSource: ((((ClientData, Int32) -> Void)!, ((ClientData, Int32) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_CreateExitHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateExitHandler: CFunctionPointer<((CFunctionPointer<Tcl_ExitProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CreateExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_CreateFileHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateFileHandler: CFunctionPointer<((Int32, Int32, CFunctionPointer<Tcl_FileProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CreateFileHandler: ((Int32, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_CreateHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |
| To | ``` var tcl_CreateHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_HashEntry>)! ``` |

Modified TclStubs.tcl_CreateInterp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateInterp: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Interp>)> ``` |
| To | ``` var tcl_CreateInterp: (() -> UnsafeMutablePointer<Tcl_Interp>)! ``` |

Modified TclStubs.tcl_CreateMathFunc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateMathFunc: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_ValueType>, CFunctionPointer<Tcl_MathProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CreateMathFunc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_ValueType>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_CreateNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ClientData, CFunctionPointer<Tcl_NamespaceDeleteProc>) -> UnsafeMutablePointer<Tcl_Namespace>)> ``` |
| To | ``` var tcl_CreateNamespace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ClientData, ((ClientData) -> Void)!) -> UnsafeMutablePointer<Tcl_Namespace>)! ``` |

Modified TclStubs.tcl_CreateObjCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateObjCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_ObjCmdProc>, ClientData, CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command)> ``` |
| To | ``` var tcl_CreateObjCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Command)! ``` |

Modified TclStubs.tcl_CreateObjTrace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateObjTrace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32, CFunctionPointer<Tcl_CmdObjTraceProc>, ClientData, CFunctionPointer<Tcl_CmdObjTraceDeleteProc>) -> Tcl_Trace)> ``` |
| To | ``` var tcl_CreateObjTrace: ((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, Tcl_Command, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, ClientData, ((ClientData) -> Void)!) -> Tcl_Trace)! ``` |

Modified TclStubs.tcl_CreateSlave

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateSlave: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Interp>)> ``` |
| To | ``` var tcl_CreateSlave: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Interp>)! ``` |

Modified TclStubs.tcl_CreateThread

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateThread: CFunctionPointer<((UnsafeMutablePointer<Tcl_ThreadId>, CFunctionPointer<Tcl_ThreadCreateProc>, ClientData, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_CreateThread: ((UnsafeMutablePointer<Tcl_ThreadId>, ((ClientData) -> Void)!, ClientData, Int32, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_CreateThreadExitHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateThreadExitHandler: CFunctionPointer<((CFunctionPointer<Tcl_ExitProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_CreateThreadExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_CreateTimerHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateTimerHandler: CFunctionPointer<((Int32, CFunctionPointer<Tcl_TimerProc>, ClientData) -> Tcl_TimerToken)> ``` |
| To | ``` var tcl_CreateTimerHandler: ((Int32, ((ClientData) -> Void)!, ClientData) -> Tcl_TimerToken)! ``` |

Modified TclStubs.tcl_CreateTrace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CreateTrace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_CmdTraceProc>, ClientData) -> Tcl_Trace)> ``` |
| To | ``` var tcl_CreateTrace: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)!, ClientData) -> Tcl_Trace)! ``` |

Modified TclStubs.tcl_CutChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_CutChannel: CFunctionPointer<((Tcl_Channel) -> Void)> ``` |
| To | ``` var tcl_CutChannel: ((Tcl_Channel) -> Void)! ``` |

Modified TclStubs.tcl_DbCkalloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbCkalloc: CFunctionPointer<((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_DbCkalloc: ((UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_DbCkfree

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbCkfree: CFunctionPointer<((UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_DbCkfree: ((UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_DbCkrealloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbCkrealloc: CFunctionPointer<((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_DbCkrealloc: ((UnsafeMutablePointer<Int8>, UInt32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_DbDecrRefCount

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbDecrRefCount: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_DbDecrRefCount: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_DbIncrRefCount

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbIncrRefCount: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_DbIncrRefCount: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_DbIsShared

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbIsShared: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_DbIsShared: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_DbNewBignumObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewBignumObj: CFunctionPointer<((UnsafeMutablePointer<mp_int>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewBignumObj: ((UnsafeMutablePointer<mp_int>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewBooleanObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewBooleanObj: CFunctionPointer<((Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewBooleanObj: ((Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewByteArrayObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewByteArrayObj: CFunctionPointer<((UnsafePointer<UInt8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewByteArrayObj: ((UnsafePointer<UInt8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewDictObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewDictObj: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewDictObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewDoubleObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewDoubleObj: CFunctionPointer<((Double, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewDoubleObj: ((Double, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewListObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewListObj: CFunctionPointer<((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewListObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewLongObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewLongObj: CFunctionPointer<((Int, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewLongObj: ((Int, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewObj: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewStringObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewStringObj: CFunctionPointer<((UnsafePointer<Int8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewStringObj: ((UnsafePointer<Int8>, Int32, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DbNewWideIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DbNewWideIntObj: CFunctionPointer<((Tcl_WideInt, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DbNewWideIntObj: ((Tcl_WideInt, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_DeleteAssocData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteAssocData: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_DeleteAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_DeleteChannelHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteChannelHandler: CFunctionPointer<((Tcl_Channel, CFunctionPointer<Tcl_ChannelProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DeleteChannelHandler: ((Tcl_Channel, ((ClientData, Int32) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_DeleteCloseHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteCloseHandler: CFunctionPointer<((Tcl_Channel, CFunctionPointer<Tcl_CloseProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DeleteCloseHandler: ((Tcl_Channel, ((ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_DeleteCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_DeleteCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_DeleteCommandFromToken

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteCommandFromToken: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> Int32)> ``` |
| To | ``` var tcl_DeleteCommandFromToken: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> Int32)! ``` |

Modified TclStubs.tcl_DeleteEvents

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteEvents: CFunctionPointer<((CFunctionPointer<Tcl_EventDeleteProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DeleteEvents: ((((UnsafeMutablePointer<Tcl_Event>, ClientData) -> Int32)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_DeleteEventSource

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteEventSource: CFunctionPointer<((CFunctionPointer<Tcl_EventSetupProc>, CFunctionPointer<Tcl_EventCheckProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DeleteEventSource: ((((ClientData, Int32) -> Void)!, ((ClientData, Int32) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_DeleteExitHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteExitHandler: CFunctionPointer<((CFunctionPointer<Tcl_ExitProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DeleteExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_DeleteFileHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteFileHandler: CFunctionPointer<((Int32) -> Void)> ``` |
| To | ``` var tcl_DeleteFileHandler: ((Int32) -> Void)! ``` |

Modified TclStubs.tcl_DeleteHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)> ``` |
| To | ``` var tcl_DeleteHashEntry: ((UnsafeMutablePointer<Tcl_HashEntry>) -> Void)! ``` |

Modified TclStubs.tcl_DeleteHashTable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteHashTable: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>) -> Void)> ``` |
| To | ``` var tcl_DeleteHashTable: ((UnsafeMutablePointer<Tcl_HashTable>) -> Void)! ``` |

Modified TclStubs.tcl_DeleteInterp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteInterp: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_DeleteInterp: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)! ``` |

Modified TclStubs.tcl_DeleteNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Namespace>) -> Void)> ``` |
| To | ``` var tcl_DeleteNamespace: ((UnsafeMutablePointer<Tcl_Namespace>) -> Void)! ``` |

Modified TclStubs.tcl_DeleteThreadExitHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteThreadExitHandler: CFunctionPointer<((CFunctionPointer<Tcl_ExitProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DeleteThreadExitHandler: ((((ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_DeleteTimerHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteTimerHandler: CFunctionPointer<((Tcl_TimerToken) -> Void)> ``` |
| To | ``` var tcl_DeleteTimerHandler: ((Tcl_TimerToken) -> Void)! ``` |

Modified TclStubs.tcl_DeleteTrace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DeleteTrace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Trace) -> Void)> ``` |
| To | ``` var tcl_DeleteTrace: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Trace) -> Void)! ``` |

Modified TclStubs.tcl_DetachChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DetachChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_DetachChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_DetachPids

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DetachPids: CFunctionPointer<((Int32, UnsafeMutablePointer<Tcl_Pid>) -> Void)> ``` |
| To | ``` var tcl_DetachPids: ((Int32, UnsafeMutablePointer<Tcl_Pid>) -> Void)! ``` |

Modified TclStubs.tcl_DictObjDone

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjDone: CFunctionPointer<((UnsafeMutablePointer<Tcl_DictSearch>) -> Void)> ``` |
| To | ``` var tcl_DictObjDone: ((UnsafeMutablePointer<Tcl_DictSearch>) -> Void)! ``` |

Modified TclStubs.tcl_DictObjFirst

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjFirst: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_DictObjFirst: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_DictObjGet

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjGet: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_DictObjGet: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_DictObjNext

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjNext: CFunctionPointer<((UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Void)> ``` |
| To | ``` var tcl_DictObjNext: ((UnsafeMutablePointer<Tcl_DictSearch>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Int32>) -> Void)! ``` |

Modified TclStubs.tcl_DictObjPut

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjPut: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_DictObjPut: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_DictObjPutKeyList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjPutKeyList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_DictObjPutKeyList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_DictObjRemove

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjRemove: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_DictObjRemove: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_DictObjRemoveKeyList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjRemoveKeyList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_DictObjRemoveKeyList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_DictObjSize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DictObjSize: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_DictObjSize: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_DiscardInterpState

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DiscardInterpState: CFunctionPointer<((Tcl_InterpState) -> Void)> ``` |
| To | ``` var tcl_DiscardInterpState: ((Tcl_InterpState) -> Void)! ``` |

Modified TclStubs.tcl_DiscardResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DiscardResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_SavedResult>) -> Void)> ``` |
| To | ``` var tcl_DiscardResult: ((UnsafeMutablePointer<Tcl_SavedResult>) -> Void)! ``` |

Modified TclStubs.tcl_DontCallWhenDeleted

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DontCallWhenDeleted: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DontCallWhenDeleted: ((UnsafeMutablePointer<Tcl_Interp>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_DoOneEvent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DoOneEvent: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_DoOneEvent: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_DoWhenIdle

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DoWhenIdle: CFunctionPointer<((CFunctionPointer<Tcl_IdleProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_DoWhenIdle: ((((ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_DStringAppend

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringAppend: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_DStringAppend: ((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_DStringAppendElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringAppendElement: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_DStringAppendElement: ((UnsafeMutablePointer<Tcl_DString>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_DStringEndSublist

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringEndSublist: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringEndSublist: ((UnsafeMutablePointer<Tcl_DString>) -> Void)! ``` |

Modified TclStubs.tcl_DStringFree

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringFree: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringFree: ((UnsafeMutablePointer<Tcl_DString>) -> Void)! ``` |

Modified TclStubs.tcl_DStringGetResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringGetResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringGetResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)! ``` |

Modified TclStubs.tcl_DStringInit

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringInit: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringInit: ((UnsafeMutablePointer<Tcl_DString>) -> Void)! ``` |

Modified TclStubs.tcl_DStringResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> Void)! ``` |

Modified TclStubs.tcl_DStringSetLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringSetLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>, Int32) -> Void)> ``` |
| To | ``` var tcl_DStringSetLength: ((UnsafeMutablePointer<Tcl_DString>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_DStringStartSublist

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DStringStartSublist: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> Void)> ``` |
| To | ``` var tcl_DStringStartSublist: ((UnsafeMutablePointer<Tcl_DString>) -> Void)! ``` |

Modified TclStubs.tcl_DumpActiveMemory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DumpActiveMemory: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_DumpActiveMemory: ((UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_DuplicateObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_DuplicateObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_DuplicateObj: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_Eof

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Eof: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_Eof: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_ErrnoId

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ErrnoId: CFunctionPointer<(() -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ErrnoId: (() -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_ErrnoMsg

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ErrnoMsg: CFunctionPointer<((Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ErrnoMsg: ((Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_Eval

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Eval: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_Eval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_EvalEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_EvalEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_EvalFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_EvalFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_EvalObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_EvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_EvalObjEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalObjEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)> ``` |
| To | ``` var tcl_EvalObjEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_EvalObjv

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalObjv: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, Int32) -> Int32)> ``` |
| To | ``` var tcl_EvalObjv: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_EvalTokens

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalTokens: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_EvalTokens: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_EvalTokensStandard

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EvalTokensStandard: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> Int32)> ``` |
| To | ``` var tcl_EvalTokensStandard: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Token>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_EventuallyFree

|  | Declaration |
| --- | --- |
| From | ``` var tcl_EventuallyFree: CFunctionPointer<((ClientData, CFunctionPointer<Tcl_FreeProc>) -> Void)> ``` |
| To | ``` var tcl_EventuallyFree: ((ClientData, ((UnsafeMutablePointer<Int8>) -> Void)!) -> Void)! ``` |

Modified TclStubs.tcl_Exit

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Exit: CFunctionPointer<((Int32) -> Void)> ``` |
| To | ``` var tcl_Exit: ((Int32) -> Void)! ``` |

Modified TclStubs.tcl_ExitThread

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExitThread: CFunctionPointer<((Int32) -> Void)> ``` |
| To | ``` var tcl_ExitThread: ((Int32) -> Void)! ``` |

Modified TclStubs.tcl_Export

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Export: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Export: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ExposeCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExposeCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_ExposeCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_ExprBoolean

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprBoolean: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ExprBoolean: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_ExprBooleanObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprBooleanObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ExprBooleanObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_ExprDouble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprDouble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)> ``` |
| To | ``` var tcl_ExprDouble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)! ``` |

Modified TclStubs.tcl_ExprDoubleObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprDoubleObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)> ``` |
| To | ``` var tcl_ExprDoubleObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)! ``` |

Modified TclStubs.tcl_ExprLong

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprLong: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int>) -> Int32)> ``` |
| To | ``` var tcl_ExprLong: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int>) -> Int32)! ``` |

Modified TclStubs.tcl_ExprLongObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprLongObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)> ``` |
| To | ``` var tcl_ExprLongObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)! ``` |

Modified TclStubs.tcl_ExprObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_ExprObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_ExprString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExprString: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_ExprString: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_ExternalToUtf

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExternalToUtf: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ExternalToUtf: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_ExternalToUtfDString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ExternalToUtfDString: CFunctionPointer<((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_ExternalToUtfDString: ((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_Finalize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Finalize: CFunctionPointer<(() -> Void)> ``` |
| To | ``` var tcl_Finalize: (() -> Void)! ``` |

Modified TclStubs.tcl_FinalizeNotifier

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FinalizeNotifier: CFunctionPointer<((ClientData) -> Void)> ``` |
| To | ``` var tcl_FinalizeNotifier: ((ClientData) -> Void)! ``` |

Modified TclStubs.tcl_FinalizeThread

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FinalizeThread: CFunctionPointer<(() -> Void)> ``` |
| To | ``` var tcl_FinalizeThread: (() -> Void)! ``` |

Modified TclStubs.tcl_FindCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)> ``` |
| To | ``` var tcl_FindCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> Tcl_Command)! ``` |

Modified TclStubs.tcl_FindEnsemble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindEnsemble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_Command)> ``` |
| To | ``` var tcl_FindEnsemble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_Command)! ``` |

Modified TclStubs.tcl_FindExecutable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindExecutable: CFunctionPointer<((UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_FindExecutable: ((UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_FindHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |
| To | ``` var tcl_FindHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_HashEntry>)! ``` |

Modified TclStubs.tcl_FindNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FindNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> UnsafeMutablePointer<Tcl_Namespace>)> ``` |
| To | ``` var tcl_FindNamespace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Namespace>, Int32) -> UnsafeMutablePointer<Tcl_Namespace>)! ``` |

Modified TclStubs.tcl_FirstHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FirstHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |
| To | ``` var tcl_FirstHashEntry: ((UnsafeMutablePointer<Tcl_HashTable>, UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)! ``` |

Modified TclStubs.tcl_Flush

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Flush: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_Flush: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_ForgetImport

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ForgetImport: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_ForgetImport: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_Format

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Format: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_Format: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_Free

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Free: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_Free: ((UnsafeMutablePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_FreeEncoding

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FreeEncoding: CFunctionPointer<((Tcl_Encoding) -> Void)> ``` |
| To | ``` var tcl_FreeEncoding: ((Tcl_Encoding) -> Void)! ``` |

Modified TclStubs.tcl_FreeParse

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FreeParse: CFunctionPointer<((UnsafeMutablePointer<Tcl_Parse>) -> Void)> ``` |
| To | ``` var tcl_FreeParse: ((UnsafeMutablePointer<Tcl_Parse>) -> Void)! ``` |

Modified TclStubs.tcl_FreeResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FreeResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_FreeResult: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)! ``` |

Modified TclStubs.tcl_FSAccess

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSAccess: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)> ``` |
| To | ``` var tcl_FSAccess: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_FSChdir

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSChdir: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSChdir: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSConvertToPathType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSConvertToPathType: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSConvertToPathType: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSCopyDirectory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSCopyDirectory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_FSCopyDirectory: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_FSCopyFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSCopyFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSCopyFile: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSCreateDirectory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSCreateDirectory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSCreateDirectory: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSData: CFunctionPointer<((UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)> ``` |
| To | ``` var tcl_FSData: ((UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)! ``` |

Modified TclStubs.tcl_FSDeleteFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSDeleteFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSDeleteFile: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSEqualPaths

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSEqualPaths: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSEqualPaths: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSEvalFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSEvalFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSEvalFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSEvalFileEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSEvalFileEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_FSEvalFileEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_FSFileAttrsGet

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSFileAttrsGet: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_FSFileAttrsGet: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_FSFileAttrsSet

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSFileAttrsSet: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSFileAttrsSet: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSFileAttrStrings

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSFileAttrStrings: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)> ``` |
| To | ``` var tcl_FSFileAttrStrings: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<UnsafePointer<Int8>>)! ``` |

Modified TclStubs.tcl_FSFileSystemInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSFileSystemInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSFileSystemInfo: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSGetCwd

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetCwd: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSGetCwd: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSGetFileSystemForPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetFileSystemForPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Filesystem>)> ``` |
| To | ``` var tcl_FSGetFileSystemForPath: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Filesystem>)! ``` |

Modified TclStubs.tcl_FSGetInternalRep

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetInternalRep: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)> ``` |
| To | ``` var tcl_FSGetInternalRep: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Filesystem>) -> ClientData)! ``` |

Modified TclStubs.tcl_FSGetNativePath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetNativePath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_FSGetNativePath: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_FSGetNormalizedPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetNormalizedPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSGetNormalizedPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSGetPathType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetPathType: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Tcl_PathType)> ``` |
| To | ``` var tcl_FSGetPathType: ((UnsafeMutablePointer<Tcl_Obj>) -> Tcl_PathType)! ``` |

Modified TclStubs.tcl_FSGetTranslatedPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetTranslatedPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSGetTranslatedPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSGetTranslatedStringPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSGetTranslatedStringPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_FSGetTranslatedStringPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_FSJoinPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSJoinPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSJoinPath: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSJoinToPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSJoinToPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSJoinToPath: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSLink

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSLink: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSLink: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSListVolumes

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSListVolumes: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSListVolumes: (() -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSLoadFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSLoadFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32)> ``` |
| To | ``` var tcl_FSLoadFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32)! ``` |

Modified TclStubs.tcl_FSLstat

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSLstat: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)> ``` |
| To | ``` var tcl_FSLstat: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)! ``` |

Modified TclStubs.tcl_FSMatchInDirectory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSMatchInDirectory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)> ``` |
| To | ``` var tcl_FSMatchInDirectory: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_GlobTypeData>) -> Int32)! ``` |

Modified TclStubs.tcl_FSMountsChanged

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSMountsChanged: CFunctionPointer<((UnsafeMutablePointer<Tcl_Filesystem>) -> Void)> ``` |
| To | ``` var tcl_FSMountsChanged: ((UnsafeMutablePointer<Tcl_Filesystem>) -> Void)! ``` |

Modified TclStubs.tcl_FSNewNativePath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSNewNativePath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Filesystem>, ClientData) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSNewNativePath: ((UnsafeMutablePointer<Tcl_Filesystem>, ClientData) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSOpenFileChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSOpenFileChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_FSOpenFileChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_FSPathSeparator

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSPathSeparator: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSPathSeparator: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSRegister

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSRegister: CFunctionPointer<((ClientData, UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)> ``` |
| To | ``` var tcl_FSRegister: ((ClientData, UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)! ``` |

Modified TclStubs.tcl_FSRemoveDirectory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSRemoveDirectory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_FSRemoveDirectory: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_FSRenameFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSRenameFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_FSRenameFile: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_FSSplitPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSSplitPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_FSSplitPath: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_FSStat

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSStat: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)> ``` |
| To | ``` var tcl_FSStat: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_StatBuf>) -> Int32)! ``` |

Modified TclStubs.tcl_FSUnregister

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSUnregister: CFunctionPointer<((UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)> ``` |
| To | ``` var tcl_FSUnregister: ((UnsafeMutablePointer<Tcl_Filesystem>) -> Int32)! ``` |

Modified TclStubs.tcl_FSUtime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_FSUtime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)> ``` |
| To | ``` var tcl_FSUtime: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<utimbuf>) -> Int32)! ``` |

Modified TclStubs.tcl_GetAlias

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetAlias: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)> ``` |
| To | ``` var tcl_GetAlias: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)! ``` |

Modified TclStubs.tcl_GetAliasObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetAliasObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)> ``` |
| To | ``` var tcl_GetAliasObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Interp>>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)! ``` |

Modified TclStubs.tcl_GetAllocMutex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetAllocMutex: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Mutex>)> ``` |
| To | ``` var tcl_GetAllocMutex: (() -> UnsafeMutablePointer<Tcl_Mutex>)! ``` |

Modified TclStubs.tcl_GetAssocData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetAssocData: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<CFunctionPointer<Tcl_InterpDeleteProc>>) -> ClientData)> ``` |
| To | ``` var tcl_GetAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)?>) -> ClientData)! ``` |

Modified TclStubs.tcl_GetBignumFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetBignumFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)> ``` |
| To | ``` var tcl_GetBignumFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)! ``` |

Modified TclStubs.tcl_GetBoolean

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetBoolean: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetBoolean: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_GetBooleanFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetBooleanFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetBooleanFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_GetByteArrayFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetByteArrayFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<UInt8>)> ``` |
| To | ``` var tcl_GetByteArrayFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<UInt8>)! ``` |

Modified TclStubs.tcl_GetChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Tcl_Channel)> ``` |
| To | ``` var tcl_GetChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_GetChannelBufferSize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelBufferSize: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_GetChannelBufferSize: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_GetChannelError

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelError: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)> ``` |
| To | ``` var tcl_GetChannelError: ((Tcl_Channel, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)! ``` |

Modified TclStubs.tcl_GetChannelErrorInterp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelErrorInterp: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)> ``` |
| To | ``` var tcl_GetChannelErrorInterp: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)! ``` |

Modified TclStubs.tcl_GetChannelHandle

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelHandle: CFunctionPointer<((Tcl_Channel, Int32, UnsafeMutablePointer<ClientData>) -> Int32)> ``` |
| To | ``` var tcl_GetChannelHandle: ((Tcl_Channel, Int32, UnsafeMutablePointer<ClientData>) -> Int32)! ``` |

Modified TclStubs.tcl_GetChannelInstanceData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelInstanceData: CFunctionPointer<((Tcl_Channel) -> ClientData)> ``` |
| To | ``` var tcl_GetChannelInstanceData: ((Tcl_Channel) -> ClientData)! ``` |

Modified TclStubs.tcl_GetChannelMode

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelMode: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_GetChannelMode: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_GetChannelName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelName: CFunctionPointer<((Tcl_Channel) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetChannelName: ((Tcl_Channel) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetChannelNames

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelNames: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_GetChannelNames: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_GetChannelNamesEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelNamesEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_GetChannelNamesEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_GetChannelOption

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelOption: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)> ``` |
| To | ``` var tcl_GetChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)! ``` |

Modified TclStubs.tcl_GetChannelThread

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelThread: CFunctionPointer<((Tcl_Channel) -> Tcl_ThreadId)> ``` |
| To | ``` var tcl_GetChannelThread: ((Tcl_Channel) -> Tcl_ThreadId)! ``` |

Modified TclStubs.tcl_GetChannelType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetChannelType: CFunctionPointer<((Tcl_Channel) -> UnsafeMutablePointer<Tcl_ChannelType>)> ``` |
| To | ``` var tcl_GetChannelType: ((Tcl_Channel) -> UnsafeMutablePointer<Tcl_ChannelType>)! ``` |

Modified TclStubs.tcl_GetCharLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCharLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_GetCharLength: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_GetCommandFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Tcl_Command)> ``` |
| To | ``` var tcl_GetCommandFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Tcl_Command)! ``` |

Modified TclStubs.tcl_GetCommandFullName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandFullName: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_GetCommandFullName: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified TclStubs.tcl_GetCommandInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)> ``` |
| To | ``` var tcl_GetCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)! ``` |

Modified TclStubs.tcl_GetCommandInfoFromToken

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandInfoFromToken: CFunctionPointer<((Tcl_Command, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)> ``` |
| To | ``` var tcl_GetCommandInfoFromToken: ((Tcl_Command, UnsafeMutablePointer<Tcl_CmdInfo>) -> Int32)! ``` |

Modified TclStubs.tcl_GetCommandName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCommandName: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetCommandName: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetCurrentNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCurrentNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)> ``` |
| To | ``` var tcl_GetCurrentNamespace: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)! ``` |

Modified TclStubs.tcl_GetCurrentThread

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCurrentThread: CFunctionPointer<(() -> Tcl_ThreadId)> ``` |
| To | ``` var tcl_GetCurrentThread: (() -> Tcl_ThreadId)! ``` |

Modified TclStubs.tcl_GetCwd

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetCwd: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_GetCwd: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetDefaultEncodingDir

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetDefaultEncodingDir: CFunctionPointer<(() -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetDefaultEncodingDir: (() -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetDouble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetDouble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)> ``` |
| To | ``` var tcl_GetDouble: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Double>) -> Int32)! ``` |

Modified TclStubs.tcl_GetDoubleFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetDoubleFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)> ``` |
| To | ``` var tcl_GetDoubleFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Double>) -> Int32)! ``` |

Modified TclStubs.tcl_GetEncoding

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncoding: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_Encoding)> ``` |
| To | ``` var tcl_GetEncoding: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_Encoding)! ``` |

Modified TclStubs.tcl_GetEncodingFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Encoding>) -> Int32)> ``` |
| To | ``` var tcl_GetEncodingFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Encoding>) -> Int32)! ``` |

Modified TclStubs.tcl_GetEncodingName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingName: CFunctionPointer<((Tcl_Encoding) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetEncodingName: ((Tcl_Encoding) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetEncodingNameFromEnvironment

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingNameFromEnvironment: CFunctionPointer<((UnsafeMutablePointer<Tcl_DString>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetEncodingNameFromEnvironment: ((UnsafeMutablePointer<Tcl_DString>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetEncodingNames

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingNames: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_GetEncodingNames: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)! ``` |

Modified TclStubs.tcl_GetEncodingSearchPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEncodingSearchPath: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetEncodingSearchPath: (() -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_GetEnsembleFlags

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleFlags: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleFlags: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_GetEnsembleMappingDict

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleMappingDict: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleMappingDict: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_GetEnsembleNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Namespace>>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleNamespace: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Namespace>>) -> Int32)! ``` |

Modified TclStubs.tcl_GetEnsembleSubcommandList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleSubcommandList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleSubcommandList: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_GetEnsembleUnknownHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetEnsembleUnknownHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_GetEnsembleUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_GetErrno

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetErrno: CFunctionPointer<(() -> Int32)> ``` |
| To | ``` var tcl_GetErrno: (() -> Int32)! ``` |

Modified TclStubs.tcl_GetGlobalNamespace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetGlobalNamespace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)> ``` |
| To | ``` var tcl_GetGlobalNamespace: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Namespace>)! ``` |

Modified TclStubs.tcl_GetHostName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetHostName: CFunctionPointer<(() -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetHostName: (() -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetIndexFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetIndexFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetIndexFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_GetIndexFromObjStruct

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetIndexFromObjStruct: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Void>, Int32, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetIndexFromObjStruct: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Void>, Int32, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_GetInt

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetInt: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetInt: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_GetInterpPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetInterpPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_GetInterpPath: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_GetIntFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetIntFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_GetIntFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_GetLongFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetLongFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)> ``` |
| To | ``` var tcl_GetLongFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int>) -> Int32)! ``` |

Modified TclStubs.tcl_GetMaster

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetMaster: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Interp>)> ``` |
| To | ``` var tcl_GetMaster: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Interp>)! ``` |

Modified TclStubs.tcl_GetMathFuncInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetMathFuncInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, UnsafeMutablePointer<CFunctionPointer<Tcl_MathProc>>, UnsafeMutablePointer<ClientData>) -> Int32)> ``` |
| To | ``` var tcl_GetMathFuncInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)?>, UnsafeMutablePointer<ClientData>) -> Int32)! ``` |

Modified TclStubs.tcl_GetNameOfExecutable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetNameOfExecutable: CFunctionPointer<(() -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetNameOfExecutable: (() -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetNamespaceUnknownHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetNamespaceUnknownHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetNamespaceUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_GetObjResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetObjResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetObjResult: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_GetObjType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetObjType: CFunctionPointer<((UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_ObjType>)> ``` |
| To | ``` var tcl_GetObjType: ((UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_ObjType>)! ``` |

Modified TclStubs.tcl_GetOpenFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetOpenFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<ClientData>) -> Int32)> ``` |
| To | ``` var tcl_GetOpenFile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<ClientData>) -> Int32)! ``` |

Modified TclStubs.tcl_GetPathType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetPathType: CFunctionPointer<((UnsafePointer<Int8>) -> Tcl_PathType)> ``` |
| To | ``` var tcl_GetPathType: ((UnsafePointer<Int8>) -> Tcl_PathType)! ``` |

Modified TclStubs.tcl_GetRange

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetRange: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetRange: ((UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_GetRegExpFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetRegExpFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_RegExp)> ``` |
| To | ``` var tcl_GetRegExpFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_RegExp)! ``` |

Modified TclStubs.tcl_GetReturnOptions

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetReturnOptions: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetReturnOptions: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_Gets

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Gets: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_DString>) -> Int32)> ``` |
| To | ``` var tcl_Gets: ((Tcl_Channel, UnsafeMutablePointer<Tcl_DString>) -> Int32)! ``` |

Modified TclStubs.tcl_GetServiceMode

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetServiceMode: CFunctionPointer<(() -> Int32)> ``` |
| To | ``` var tcl_GetServiceMode: (() -> Int32)! ``` |

Modified TclStubs.tcl_GetSlave

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetSlave: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Interp>)> ``` |
| To | ``` var tcl_GetSlave: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Interp>)! ``` |

Modified TclStubs.tcl_GetsObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetsObj: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_GetsObj: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_GetStackedChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetStackedChannel: CFunctionPointer<((Tcl_Channel) -> Tcl_Channel)> ``` |
| To | ``` var tcl_GetStackedChannel: ((Tcl_Channel) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_GetStdChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetStdChannel: CFunctionPointer<((Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_GetStdChannel: ((Int32) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_GetString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetString: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_GetString: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetStringFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetStringFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_GetStringFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetStringResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetStringResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetStringResult: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetThreadData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetThreadData: CFunctionPointer<((UnsafeMutablePointer<Tcl_ThreadDataKey>, Int32) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` var tcl_GetThreadData: ((UnsafeMutablePointer<Tcl_ThreadDataKey>, Int32) -> UnsafeMutablePointer<Void>)! ``` |

Modified TclStubs.tcl_GetTime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetTime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_GetTime: ((UnsafeMutablePointer<Tcl_Time>) -> Void)! ``` |

Modified TclStubs.tcl_GetTopChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetTopChannel: CFunctionPointer<((Tcl_Channel) -> Tcl_Channel)> ``` |
| To | ``` var tcl_GetTopChannel: ((Tcl_Channel) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_GetUniChar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetUniChar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_UniChar)> ``` |
| To | ``` var tcl_GetUniChar: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Tcl_UniChar)! ``` |

Modified TclStubs.tcl_GetUnicode

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetUnicode: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_UniChar>)> ``` |
| To | ``` var tcl_GetUnicode: ((UnsafeMutablePointer<Tcl_Obj>) -> UnsafeMutablePointer<Tcl_UniChar>)! ``` |

Modified TclStubs.tcl_GetUnicodeFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetUnicodeFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_UniChar>)> ``` |
| To | ``` var tcl_GetUnicodeFromObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Tcl_UniChar>)! ``` |

Modified TclStubs.tcl_GetVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_GetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_GetVar2Ex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetVar2Ex: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_GetVar2Ex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_GetVersion

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetVersion: CFunctionPointer<((UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Void)> ``` |
| To | ``` var tcl_GetVersion: ((UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Void)! ``` |

Modified TclStubs.tcl_GetWideIntFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GetWideIntFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_WideInt>) -> Int32)> ``` |
| To | ``` var tcl_GetWideIntFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_WideInt>) -> Int32)! ``` |

Modified TclStubs.tcl_GlobalEval

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GlobalEval: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_GlobalEval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_GlobalEvalObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_GlobalEvalObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_GlobalEvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_HashStats

|  | Declaration |
| --- | --- |
| From | ``` var tcl_HashStats: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_HashStats: ((UnsafeMutablePointer<Tcl_HashTable>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_HideCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_HideCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_HideCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_Import

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Import: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Import: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_Init

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Init: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_Init: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_InitBignumFromDouble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitBignumFromDouble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<mp_int>) -> Int32)> ``` |
| To | ``` var tcl_InitBignumFromDouble: ((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<mp_int>) -> Int32)! ``` |

Modified TclStubs.tcl_InitCustomHashTable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitCustomHashTable: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, Int32, UnsafeMutablePointer<Tcl_HashKeyType>) -> Void)> ``` |
| To | ``` var tcl_InitCustomHashTable: ((UnsafeMutablePointer<Tcl_HashTable>, Int32, UnsafeMutablePointer<Tcl_HashKeyType>) -> Void)! ``` |

Modified TclStubs.tcl_InitHashTable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitHashTable: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>, Int32) -> Void)> ``` |
| To | ``` var tcl_InitHashTable: ((UnsafeMutablePointer<Tcl_HashTable>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_InitMemory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitMemory: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_InitMemory: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)! ``` |

Modified TclStubs.tcl_InitNotifier

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitNotifier: CFunctionPointer<(() -> ClientData)> ``` |
| To | ``` var tcl_InitNotifier: (() -> ClientData)! ``` |

Modified TclStubs.tcl_InitObjHashTable

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InitObjHashTable: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashTable>) -> Void)> ``` |
| To | ``` var tcl_InitObjHashTable: ((UnsafeMutablePointer<Tcl_HashTable>) -> Void)! ``` |

Modified TclStubs.tcl_InputBlocked

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InputBlocked: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_InputBlocked: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_InputBuffered

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InputBuffered: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_InputBuffered: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_InterpDeleted

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InterpDeleted: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_InterpDeleted: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_InvalidateStringRep

|  | Declaration |
| --- | --- |
| From | ``` var tcl_InvalidateStringRep: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_InvalidateStringRep: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified TclStubs.tcl_IsChannelExisting

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsChannelExisting: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_IsChannelExisting: ((UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_IsChannelRegistered

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsChannelRegistered: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_IsChannelRegistered: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_IsChannelShared

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsChannelShared: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_IsChannelShared: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_IsEnsemble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsEnsemble: CFunctionPointer<((Tcl_Command) -> Int32)> ``` |
| To | ``` var tcl_IsEnsemble: ((Tcl_Command) -> Int32)! ``` |

Modified TclStubs.tcl_IsSafe

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsSafe: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_IsSafe: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_IsStandardChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_IsStandardChannel: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_IsStandardChannel: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_JoinPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_JoinPath: CFunctionPointer<((Int32, UnsafePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_JoinPath: ((Int32, UnsafePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_JoinThread

|  | Declaration |
| --- | --- |
| From | ``` var tcl_JoinThread: CFunctionPointer<((Tcl_ThreadId, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_JoinThread: ((Tcl_ThreadId, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_LimitAddHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitAddHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_LimitHandlerProc>, ClientData, CFunctionPointer<Tcl_LimitHandlerDeleteProc>) -> Void)> ``` |
| To | ``` var tcl_LimitAddHandler: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData, ((ClientData) -> Void)!) -> Void)! ``` |

Modified TclStubs.tcl_LimitCheck

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitCheck: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_LimitCheck: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_LimitExceeded

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitExceeded: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_LimitExceeded: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_LimitGetCommands

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitGetCommands: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_LimitGetCommands: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_LimitGetGranularity

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitGetGranularity: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_LimitGetGranularity: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_LimitGetTime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitGetTime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_LimitGetTime: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)! ``` |

Modified TclStubs.tcl_LimitReady

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitReady: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_LimitReady: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_LimitRemoveHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitRemoveHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, CFunctionPointer<Tcl_LimitHandlerProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_LimitRemoveHandler: ((UnsafeMutablePointer<Tcl_Interp>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_LimitSetCommands

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitSetCommands: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)> ``` |
| To | ``` var tcl_LimitSetCommands: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_LimitSetGranularity

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitSetGranularity: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32) -> Void)> ``` |
| To | ``` var tcl_LimitSetGranularity: ((UnsafeMutablePointer<Tcl_Interp>, Int32, Int32) -> Void)! ``` |

Modified TclStubs.tcl_LimitSetTime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitSetTime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_LimitSetTime: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Time>) -> Void)! ``` |

Modified TclStubs.tcl_LimitTypeEnabled

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitTypeEnabled: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_LimitTypeEnabled: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_LimitTypeExceeded

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitTypeExceeded: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_LimitTypeExceeded: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_LimitTypeReset

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitTypeReset: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)> ``` |
| To | ``` var tcl_LimitTypeReset: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_LimitTypeSet

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LimitTypeSet: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)> ``` |
| To | ``` var tcl_LimitTypeSet: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_LinkVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LinkVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_LinkVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ListMathFuncs

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListMathFuncs: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_ListMathFuncs: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_ListObjAppendElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjAppendElement: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_ListObjAppendElement: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_ListObjAppendList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjAppendList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_ListObjAppendList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_ListObjGetElements

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjGetElements: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)> ``` |
| To | ``` var tcl_ListObjGetElements: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>>) -> Int32)! ``` |

Modified TclStubs.tcl_ListObjIndex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjIndex: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_ListObjIndex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_ListObjLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ListObjLength: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_ListObjReplace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ListObjReplace: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_ListObjReplace: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_LogCommandInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_LogCommandInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_LogCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_MakeFileChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MakeFileChannel: CFunctionPointer<((ClientData, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_MakeFileChannel: ((ClientData, Int32) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_MakeSafe

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MakeSafe: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)> ``` |
| To | ``` var tcl_MakeSafe: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified TclStubs.tcl_MakeTcpClientChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MakeTcpClientChannel: CFunctionPointer<((ClientData) -> Tcl_Channel)> ``` |
| To | ``` var tcl_MakeTcpClientChannel: ((ClientData) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_Merge

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Merge: CFunctionPointer<((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_Merge: ((Int32, UnsafePointer<UnsafePointer<Int8>>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_MutexFinalize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MutexFinalize: CFunctionPointer<((UnsafeMutablePointer<Tcl_Mutex>) -> Void)> ``` |
| To | ``` var tcl_MutexFinalize: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)! ``` |

Modified TclStubs.tcl_MutexLock

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MutexLock: CFunctionPointer<((UnsafeMutablePointer<Tcl_Mutex>) -> Void)> ``` |
| To | ``` var tcl_MutexLock: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)! ``` |

Modified TclStubs.tcl_MutexUnlock

|  | Declaration |
| --- | --- |
| From | ``` var tcl_MutexUnlock: CFunctionPointer<((UnsafeMutablePointer<Tcl_Mutex>) -> Void)> ``` |
| To | ``` var tcl_MutexUnlock: ((UnsafeMutablePointer<Tcl_Mutex>) -> Void)! ``` |

Modified TclStubs.tcl_NewBignumObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewBignumObj: CFunctionPointer<((UnsafeMutablePointer<mp_int>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewBignumObj: ((UnsafeMutablePointer<mp_int>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewBooleanObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewBooleanObj: CFunctionPointer<((Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewBooleanObj: ((Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewByteArrayObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewByteArrayObj: CFunctionPointer<((UnsafePointer<UInt8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewByteArrayObj: ((UnsafePointer<UInt8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewDictObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewDictObj: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewDictObj: (() -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewDoubleObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewDoubleObj: CFunctionPointer<((Double) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewDoubleObj: ((Double) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewIntObj: CFunctionPointer<((Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewIntObj: ((Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewListObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewListObj: CFunctionPointer<((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewListObj: ((Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewLongObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewLongObj: CFunctionPointer<((Int) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewLongObj: ((Int) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewObj: CFunctionPointer<(() -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewObj: (() -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewStringObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewStringObj: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewStringObj: ((UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewUnicodeObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewUnicodeObj: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewUnicodeObj: ((UnsafePointer<Tcl_UniChar>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NewWideIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NewWideIntObj: CFunctionPointer<((Tcl_WideInt) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_NewWideIntObj: ((Tcl_WideInt) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_NextHashEntry

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NextHashEntry: CFunctionPointer<((UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)> ``` |
| To | ``` var tcl_NextHashEntry: ((UnsafeMutablePointer<Tcl_HashSearch>) -> UnsafeMutablePointer<Tcl_HashEntry>)! ``` |

Modified TclStubs.tcl_NotifyChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NotifyChannel: CFunctionPointer<((Tcl_Channel, Int32) -> Void)> ``` |
| To | ``` var tcl_NotifyChannel: ((Tcl_Channel, Int32) -> Void)! ``` |

Modified TclStubs.tcl_NumUtfChars

|  | Declaration |
| --- | --- |
| From | ``` var tcl_NumUtfChars: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_NumUtfChars: ((UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ObjGetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ObjGetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_ObjGetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_ObjSetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ObjSetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_ObjSetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_OpenCommandChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OpenCommandChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_OpenCommandChannel: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, Int32) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_OpenFileChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OpenFileChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_OpenFileChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_OpenTcpClient

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OpenTcpClient: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, Int32) -> Tcl_Channel)> ``` |
| To | ``` var tcl_OpenTcpClient: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, Int32) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_OpenTcpServer

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OpenTcpServer: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, CFunctionPointer<Tcl_TcpAcceptProc>, ClientData) -> Tcl_Channel)> ``` |
| To | ``` var tcl_OpenTcpServer: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, ((ClientData, Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Void)!, ClientData) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_OutputBuffered

|  | Declaration |
| --- | --- |
| From | ``` var tcl_OutputBuffered: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_OutputBuffered: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_PanicVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PanicVA: CFunctionPointer<((UnsafePointer<Int8>, CVaListPointer) -> Void)> ``` |
| To | ``` var tcl_PanicVA: ((UnsafePointer<Int8>, CVaListPointer) -> Void)! ``` |

Modified TclStubs.tcl_ParseBraces

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseBraces: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)> ``` |
| To | ``` var tcl_ParseBraces: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)! ``` |

Modified TclStubs.tcl_ParseCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)> ``` |
| To | ``` var tcl_ParseCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)! ``` |

Modified TclStubs.tcl_ParseExpr

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseExpr: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)> ``` |
| To | ``` var tcl_ParseExpr: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>) -> Int32)! ``` |

Modified TclStubs.tcl_ParseQuotedString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseQuotedString: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)> ``` |
| To | ``` var tcl_ParseQuotedString: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)! ``` |

Modified TclStubs.tcl_ParseVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_ParseVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_ParseVarName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ParseVarName: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32) -> Int32)> ``` |
| To | ``` var tcl_ParseVarName: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_Parse>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_PkgPresent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgPresent: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PkgPresent: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_PkgPresentEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgPresentEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PkgPresentEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_PkgProvide

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgProvide: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_PkgProvide: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_PkgProvideEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgProvideEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, ClientData) -> Int32)> ``` |
| To | ``` var tcl_PkgProvideEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, ClientData) -> Int32)! ``` |

Modified TclStubs.tcl_PkgRequire

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgRequire: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PkgRequire: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_PkgRequireEx

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgRequireEx: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PkgRequireEx: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<ClientData>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_PkgRequireProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PkgRequireProc: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<ClientData>) -> Int32)> ``` |
| To | ``` var tcl_PkgRequireProc: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafeMutablePointer<ClientData>) -> Int32)! ``` |

Modified TclStubs.tcl_PosixError

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PosixError: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_PosixError: ((UnsafeMutablePointer<Tcl_Interp>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_Preserve

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Preserve: CFunctionPointer<((ClientData) -> Void)> ``` |
| To | ``` var tcl_Preserve: ((ClientData) -> Void)! ``` |

Modified TclStubs.tcl_PrintDouble

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PrintDouble: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_PrintDouble: ((UnsafeMutablePointer<Tcl_Interp>, Double, UnsafeMutablePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_ProcObjCmd

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ProcObjCmd: CFunctionPointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)> ``` |
| To | ``` var tcl_ProcObjCmd: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)! ``` |

Modified TclStubs.tcl_PutEnv

|  | Declaration |
| --- | --- |
| From | ``` var tcl_PutEnv: CFunctionPointer<((UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_PutEnv: ((UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_QueryTimeProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_QueryTimeProc: CFunctionPointer<((UnsafeMutablePointer<CFunctionPointer<Tcl_GetTimeProc>>, UnsafeMutablePointer<CFunctionPointer<Tcl_ScaleTimeProc>>, UnsafeMutablePointer<ClientData>) -> Void)> ``` |
| To | ``` var tcl_QueryTimeProc: ((UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, UnsafeMutablePointer<ClientData>) -> Void)! ``` |

Modified TclStubs.tcl_QueueEvent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_QueueEvent: CFunctionPointer<((UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)> ``` |
| To | ``` var tcl_QueueEvent: ((UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)! ``` |

Modified TclStubs.tcl_Read

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Read: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Read: ((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ReadChars

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ReadChars: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_ReadChars: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ReadRaw

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ReadRaw: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_ReadRaw: ((Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_Realloc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Realloc: CFunctionPointer<((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_Realloc: ((UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_ReapDetachedProcs

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ReapDetachedProcs: CFunctionPointer<(() -> Void)> ``` |
| To | ``` var tcl_ReapDetachedProcs: (() -> Void)! ``` |

Modified TclStubs.tcl_RecordAndEval

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RecordAndEval: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_RecordAndEval: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_RecordAndEvalObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RecordAndEvalObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)> ``` |
| To | ``` var tcl_RecordAndEvalObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_RegExpCompile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpCompile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_RegExp)> ``` |
| To | ``` var tcl_RegExpCompile: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Tcl_RegExp)! ``` |

Modified TclStubs.tcl_RegExpExec

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpExec: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_RegExpExec: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_RegExpExecObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpExecObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_RegExpExecObj: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_RegExp, UnsafeMutablePointer<Tcl_Obj>, Int32, Int32, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_RegExpGetInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpGetInfo: CFunctionPointer<((Tcl_RegExp, UnsafeMutablePointer<Tcl_RegExpInfo>) -> Void)> ``` |
| To | ``` var tcl_RegExpGetInfo: ((Tcl_RegExp, UnsafeMutablePointer<Tcl_RegExpInfo>) -> Void)! ``` |

Modified TclStubs.tcl_RegExpMatch

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpMatch: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_RegExpMatch: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_RegExpMatchObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpMatchObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_RegExpMatchObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_RegExpRange

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegExpRange: CFunctionPointer<((Tcl_RegExp, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)> ``` |
| To | ``` var tcl_RegExpRange: ((Tcl_RegExp, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)! ``` |

Modified TclStubs.tcl_RegisterChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegisterChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Void)> ``` |
| To | ``` var tcl_RegisterChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Void)! ``` |

Modified TclStubs.tcl_RegisterConfig

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegisterConfig: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Config>, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_RegisterConfig: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Config>, UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_RegisterObjType

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RegisterObjType: CFunctionPointer<((UnsafeMutablePointer<Tcl_ObjType>) -> Void)> ``` |
| To | ``` var tcl_RegisterObjType: ((UnsafeMutablePointer<Tcl_ObjType>) -> Void)! ``` |

Modified TclStubs.tcl_Release

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Release: CFunctionPointer<((ClientData) -> Void)> ``` |
| To | ``` var tcl_Release: ((ClientData) -> Void)! ``` |

Modified TclStubs.tcl_ResetResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ResetResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_ResetResult: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)! ``` |

Modified TclStubs.tcl_RestoreInterpState

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RestoreInterpState: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_InterpState) -> Int32)> ``` |
| To | ``` var tcl_RestoreInterpState: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_InterpState) -> Int32)! ``` |

Modified TclStubs.tcl_RestoreResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_RestoreResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)> ``` |
| To | ``` var tcl_RestoreResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)! ``` |

Modified TclStubs.tcl_SaveInterpState

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SaveInterpState: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Tcl_InterpState)> ``` |
| To | ``` var tcl_SaveInterpState: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Tcl_InterpState)! ``` |

Modified TclStubs.tcl_SaveResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SaveResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)> ``` |
| To | ``` var tcl_SaveResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_SavedResult>) -> Void)! ``` |

Modified TclStubs.tcl_ScanCountedElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ScanCountedElement: CFunctionPointer<((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ScanCountedElement: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_ScanElement

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ScanElement: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_ScanElement: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_Seek

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Seek: CFunctionPointer<((Tcl_Channel, Tcl_WideInt, Int32) -> Tcl_WideInt)> ``` |
| To | ``` var tcl_Seek: ((Tcl_Channel, Tcl_WideInt, Int32) -> Tcl_WideInt)! ``` |

Modified TclStubs.tcl_SeekOld

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SeekOld: CFunctionPointer<((Tcl_Channel, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_SeekOld: ((Tcl_Channel, Int32, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ServiceAll

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ServiceAll: CFunctionPointer<(() -> Int32)> ``` |
| To | ``` var tcl_ServiceAll: (() -> Int32)! ``` |

Modified TclStubs.tcl_ServiceEvent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ServiceEvent: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_ServiceEvent: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_ServiceModeHook

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ServiceModeHook: CFunctionPointer<((Int32) -> Void)> ``` |
| To | ``` var tcl_ServiceModeHook: ((Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetAssocData

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetAssocData: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_InterpDeleteProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_SetAssocData: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_SetBignumObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetBignumObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Void)> ``` |
| To | ``` var tcl_SetBignumObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Void)! ``` |

Modified TclStubs.tcl_SetBooleanObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetBooleanObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetBooleanObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetByteArrayLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetByteArrayLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<UInt8>)> ``` |
| To | ``` var tcl_SetByteArrayLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<UInt8>)! ``` |

Modified TclStubs.tcl_SetByteArrayObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetByteArrayObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<UInt8>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetByteArrayObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<UInt8>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetChannelBufferSize

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetChannelBufferSize: CFunctionPointer<((Tcl_Channel, Int32) -> Void)> ``` |
| To | ``` var tcl_SetChannelBufferSize: ((Tcl_Channel, Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetChannelError

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetChannelError: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_SetChannelError: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified TclStubs.tcl_SetChannelErrorInterp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetChannelErrorInterp: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_SetChannelErrorInterp: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified TclStubs.tcl_SetChannelOption

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetChannelOption: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_SetChannelOption: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_SetCommandInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetCommandInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Tcl_CmdInfo>) -> Int32)> ``` |
| To | ``` var tcl_SetCommandInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Tcl_CmdInfo>) -> Int32)! ``` |

Modified TclStubs.tcl_SetCommandInfoFromToken

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetCommandInfoFromToken: CFunctionPointer<((Tcl_Command, UnsafePointer<Tcl_CmdInfo>) -> Int32)> ``` |
| To | ``` var tcl_SetCommandInfoFromToken: ((Tcl_Command, UnsafePointer<Tcl_CmdInfo>) -> Int32)! ``` |

Modified TclStubs.tcl_SetDefaultEncodingDir

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetDefaultEncodingDir: CFunctionPointer<((UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_SetDefaultEncodingDir: ((UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_SetDoubleObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetDoubleObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Double) -> Void)> ``` |
| To | ``` var tcl_SetDoubleObj: ((UnsafeMutablePointer<Tcl_Obj>, Double) -> Void)! ``` |

Modified TclStubs.tcl_SetEncodingSearchPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEncodingSearchPath: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetEncodingSearchPath: ((UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_SetEnsembleFlags

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEnsembleFlags: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, Int32) -> Int32)> ``` |
| To | ``` var tcl_SetEnsembleFlags: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_SetEnsembleMappingDict

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEnsembleMappingDict: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetEnsembleMappingDict: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_SetEnsembleSubcommandList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEnsembleSubcommandList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetEnsembleSubcommandList: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_SetEnsembleUnknownHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetEnsembleUnknownHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetEnsembleUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Command, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_SetErrno

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetErrno: CFunctionPointer<((Int32) -> Void)> ``` |
| To | ``` var tcl_SetErrno: ((Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetErrorCodeVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetErrorCodeVA: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)> ``` |
| To | ``` var tcl_SetErrorCodeVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Void)! ``` |

Modified TclStubs.tcl_SetExitProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetExitProc: CFunctionPointer<((CFunctionPointer<Tcl_ExitProc>) -> CFunctionPointer<Tcl_ExitProc>)> ``` |
| To | ``` var tcl_SetExitProc: ((((ClientData) -> Void)!) -> ((ClientData) -> Void)!)! ``` |

Modified TclStubs.tcl_SetIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetIntObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetIntObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetListObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetListObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)> ``` |
| To | ``` var tcl_SetListObj: ((UnsafeMutablePointer<Tcl_Obj>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Void)! ``` |

Modified TclStubs.tcl_SetLongObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetLongObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int) -> Void)> ``` |
| To | ``` var tcl_SetLongObj: ((UnsafeMutablePointer<Tcl_Obj>, Int) -> Void)! ``` |

Modified TclStubs.tcl_SetMainLoop

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetMainLoop: CFunctionPointer<((CFunctionPointer<Tcl_MainLoopProc>) -> Void)> ``` |
| To | ``` var tcl_SetMainLoop: (((() -> Void)!) -> Void)! ``` |

Modified TclStubs.tcl_SetMaxBlockTime

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetMaxBlockTime: CFunctionPointer<((UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_SetMaxBlockTime: ((UnsafeMutablePointer<Tcl_Time>) -> Void)! ``` |

Modified TclStubs.tcl_SetNamespaceUnknownHandler

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetNamespaceUnknownHandler: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetNamespaceUnknownHandler: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Namespace>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_SetNotifier

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetNotifier: CFunctionPointer<((UnsafeMutablePointer<Tcl_NotifierProcs>) -> Void)> ``` |
| To | ``` var tcl_SetNotifier: ((UnsafeMutablePointer<Tcl_NotifierProcs>) -> Void)! ``` |

Modified TclStubs.tcl_SetObjErrorCode

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetObjErrorCode: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_SetObjErrorCode: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified TclStubs.tcl_SetObjLength

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetObjLength: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetObjLength: ((UnsafeMutablePointer<Tcl_Obj>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetObjResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetObjResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tcl_SetObjResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified TclStubs.tcl_SetPanicProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetPanicProc: CFunctionPointer<((COpaquePointer) -> Void)> ``` |
| To | ``` var tcl_SetPanicProc: ((COpaquePointer) -> Void)! ``` |

Modified TclStubs.tcl_SetRecursionLimit

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetRecursionLimit: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)> ``` |
| To | ``` var tcl_SetRecursionLimit: ((UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_SetResult

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetResult: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Int8>, CFunctionPointer<Tcl_FreeProc>) -> Void)> ``` |
| To | ``` var tcl_SetResult: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Int8>, ((UnsafeMutablePointer<Int8>) -> Void)!) -> Void)! ``` |

Modified TclStubs.tcl_SetReturnOptions

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetReturnOptions: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_SetReturnOptions: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_SetServiceMode

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetServiceMode: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_SetServiceMode: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_SetStdChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetStdChannel: CFunctionPointer<((Tcl_Channel, Int32) -> Void)> ``` |
| To | ``` var tcl_SetStdChannel: ((Tcl_Channel, Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetStringObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetStringObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetStringObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Int8>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetSystemEncoding

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetSystemEncoding: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_SetSystemEncoding: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_SetTimeProc

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetTimeProc: CFunctionPointer<((CFunctionPointer<Tcl_GetTimeProc>, CFunctionPointer<Tcl_ScaleTimeProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_SetTimeProc: ((((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_SetTimer

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetTimer: CFunctionPointer<((UnsafeMutablePointer<Tcl_Time>) -> Void)> ``` |
| To | ``` var tcl_SetTimer: ((UnsafeMutablePointer<Tcl_Time>) -> Void)! ``` |

Modified TclStubs.tcl_SetUnicodeObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetUnicodeObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)> ``` |
| To | ``` var tcl_SetUnicodeObj: ((UnsafeMutablePointer<Tcl_Obj>, UnsafePointer<Tcl_UniChar>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_SetVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_SetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_SetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_SetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_SetVar2Ex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetVar2Ex: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_SetVar2Ex: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_SetWideIntObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SetWideIntObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>, Tcl_WideInt) -> Void)> ``` |
| To | ``` var tcl_SetWideIntObj: ((UnsafeMutablePointer<Tcl_Obj>, Tcl_WideInt) -> Void)! ``` |

Modified TclStubs.tcl_SignalId

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SignalId: CFunctionPointer<((Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_SignalId: ((Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_SignalMsg

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SignalMsg: CFunctionPointer<((Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_SignalMsg: ((Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_Sleep

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Sleep: CFunctionPointer<((Int32) -> Void)> ``` |
| To | ``` var tcl_Sleep: ((Int32) -> Void)! ``` |

Modified TclStubs.tcl_SourceRCFile

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SourceRCFile: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>) -> Void)> ``` |
| To | ``` var tcl_SourceRCFile: ((UnsafeMutablePointer<Tcl_Interp>) -> Void)! ``` |

Modified TclStubs.tcl_SpliceChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SpliceChannel: CFunctionPointer<((Tcl_Channel) -> Void)> ``` |
| To | ``` var tcl_SpliceChannel: ((Tcl_Channel) -> Void)! ``` |

Modified TclStubs.tcl_SplitList

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SplitList: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)> ``` |
| To | ``` var tcl_SplitList: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Int32)! ``` |

Modified TclStubs.tcl_SplitPath

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SplitPath: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Void)> ``` |
| To | ``` var tcl_SplitPath: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafePointer<Int8>>>) -> Void)! ``` |

Modified TclStubs.tcl_StackChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_StackChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_ChannelType>, ClientData, Int32, Tcl_Channel) -> Tcl_Channel)> ``` |
| To | ``` var tcl_StackChannel: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_ChannelType>, ClientData, Int32, Tcl_Channel) -> Tcl_Channel)! ``` |

Modified TclStubs.tcl_Stat

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Stat: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)> ``` |
| To | ``` var tcl_Stat: ((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)! ``` |

Modified TclStubs.tcl_StaticPackage

|  | Declaration |
| --- | --- |
| From | ``` var tcl_StaticPackage: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, CFunctionPointer<Tcl_PackageInitProc>, CFunctionPointer<Tcl_PackageInitProc>) -> Void)> ``` |
| To | ``` var tcl_StaticPackage: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!) -> Void)! ``` |

Modified TclStubs.tcl_StringCaseMatch

|  | Declaration |
| --- | --- |
| From | ``` var tcl_StringCaseMatch: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_StringCaseMatch: ((UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_StringMatch

|  | Declaration |
| --- | --- |
| From | ``` var tcl_StringMatch: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_StringMatch: ((UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_SubstObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_SubstObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)> ``` |
| To | ``` var tcl_SubstObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, Int32) -> UnsafeMutablePointer<Tcl_Obj>)! ``` |

Modified TclStubs.tcl_TakeBignumFromObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TakeBignumFromObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)> ``` |
| To | ``` var tcl_TakeBignumFromObj: ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<mp_int>) -> Int32)! ``` |

Modified TclStubs.tcl_Tell

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Tell: CFunctionPointer<((Tcl_Channel) -> Tcl_WideInt)> ``` |
| To | ``` var tcl_Tell: ((Tcl_Channel) -> Tcl_WideInt)! ``` |

Modified TclStubs.tcl_TellOld

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TellOld: CFunctionPointer<((Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_TellOld: ((Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_ThreadAlert

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ThreadAlert: CFunctionPointer<((Tcl_ThreadId) -> Void)> ``` |
| To | ``` var tcl_ThreadAlert: ((Tcl_ThreadId) -> Void)! ``` |

Modified TclStubs.tcl_ThreadQueueEvent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ThreadQueueEvent: CFunctionPointer<((Tcl_ThreadId, UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)> ``` |
| To | ``` var tcl_ThreadQueueEvent: ((Tcl_ThreadId, UnsafeMutablePointer<Tcl_Event>, Tcl_QueuePosition) -> Void)! ``` |

Modified TclStubs.tcl_TraceCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TraceCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> Int32)> ``` |
| To | ``` var tcl_TraceCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> Int32)! ``` |

Modified TclStubs.tcl_TraceVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TraceVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Int32)> ``` |
| To | ``` var tcl_TraceVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Int32)! ``` |

Modified TclStubs.tcl_TraceVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TraceVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Int32)> ``` |
| To | ``` var tcl_TraceVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Int32)! ``` |

Modified TclStubs.tcl_TranslateFileName

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TranslateFileName: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_TranslateFileName: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_TruncateChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_TruncateChannel: CFunctionPointer<((Tcl_Channel, Tcl_WideInt) -> Int32)> ``` |
| To | ``` var tcl_TruncateChannel: ((Tcl_Channel, Tcl_WideInt) -> Int32)! ``` |

Modified TclStubs.tcl_Ungets

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Ungets: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32, Int32) -> Int32)> ``` |
| To | ``` var tcl_Ungets: ((Tcl_Channel, UnsafePointer<Int8>, Int32, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharAtIndex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharAtIndex: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Tcl_UniChar)> ``` |
| To | ``` var tcl_UniCharAtIndex: ((UnsafePointer<Int8>, Int32) -> Tcl_UniChar)! ``` |

Modified TclStubs.tcl_UniCharCaseMatch

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharCaseMatch: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharCaseMatch: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsAlnum

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsAlnum: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsAlnum: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsAlpha

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsAlpha: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsAlpha: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsControl

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsControl: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsControl: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsDigit

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsDigit: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsDigit: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsGraph

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsGraph: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsGraph: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsLower

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsLower: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsLower: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsPrint

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsPrint: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsPrint: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsPunct

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsPunct: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsPunct: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsSpace

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsSpace: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsSpace: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsUpper

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsUpper: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsUpper: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharIsWordChar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharIsWordChar: CFunctionPointer<((Int32) -> Int32)> ``` |
| To | ``` var tcl_UniCharIsWordChar: ((Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharLen

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharLen: CFunctionPointer<((UnsafePointer<Tcl_UniChar>) -> Int32)> ``` |
| To | ``` var tcl_UniCharLen: ((UnsafePointer<Tcl_UniChar>) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharNcasecmp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharNcasecmp: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)> ``` |
| To | ``` var tcl_UniCharNcasecmp: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharNcmp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharNcmp: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)> ``` |
| To | ``` var tcl_UniCharNcmp: ((UnsafePointer<Tcl_UniChar>, UnsafePointer<Tcl_UniChar>, UInt) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharToLower

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharToLower: CFunctionPointer<((Int32) -> Tcl_UniChar)> ``` |
| To | ``` var tcl_UniCharToLower: ((Int32) -> Tcl_UniChar)! ``` |

Modified TclStubs.tcl_UniCharToTitle

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharToTitle: CFunctionPointer<((Int32) -> Tcl_UniChar)> ``` |
| To | ``` var tcl_UniCharToTitle: ((Int32) -> Tcl_UniChar)! ``` |

Modified TclStubs.tcl_UniCharToUpper

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharToUpper: CFunctionPointer<((Int32) -> Tcl_UniChar)> ``` |
| To | ``` var tcl_UniCharToUpper: ((Int32) -> Tcl_UniChar)! ``` |

Modified TclStubs.tcl_UniCharToUtf

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharToUtf: CFunctionPointer<((Int32, UnsafeMutablePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UniCharToUtf: ((Int32, UnsafeMutablePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_UniCharToUtfDString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UniCharToUtfDString: CFunctionPointer<((UnsafePointer<Tcl_UniChar>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_UniCharToUtfDString: ((UnsafePointer<Tcl_UniChar>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_UnlinkVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnlinkVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_UnlinkVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_UnregisterChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnregisterChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_UnregisterChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_UnsetVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnsetVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UnsetVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UnsetVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnsetVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UnsetVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UnstackChannel

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UnstackChannel: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)> ``` |
| To | ``` var tcl_UnstackChannel: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Channel) -> Int32)! ``` |

Modified TclStubs.tcl_UntraceCommand

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UntraceCommand: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_CommandTraceProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_UntraceCommand: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_UntraceVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UntraceVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_UntraceVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_UntraceVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UntraceVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> Void)> ``` |
| To | ``` var tcl_UntraceVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> Void)! ``` |

Modified TclStubs.tcl_UpdateLinkedVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UpdateLinkedVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_UpdateLinkedVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tcl_UpVar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UpVar: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UpVar: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UpVar2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UpVar2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UpVar2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UtfAtIndex

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfAtIndex: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfAtIndex: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_UtfBackslash

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfBackslash: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UtfBackslash: ((UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_UtfCharComplete

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfCharComplete: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_UtfCharComplete: ((UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_UtfFindFirst

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfFindFirst: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfFindFirst: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_UtfFindLast

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfFindLast: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfFindLast: ((UnsafePointer<Int8>, Int32) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_UtfNcasecmp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfNcasecmp: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)> ``` |
| To | ``` var tcl_UtfNcasecmp: ((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)! ``` |

Modified TclStubs.tcl_UtfNcmp

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfNcmp: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)> ``` |
| To | ``` var tcl_UtfNcmp: ((UnsafePointer<Int8>, UnsafePointer<Int8>, UInt) -> Int32)! ``` |

Modified TclStubs.tcl_UtfNext

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfNext: CFunctionPointer<((UnsafePointer<Int8>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfNext: ((UnsafePointer<Int8>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_UtfPrev

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfPrev: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var tcl_UtfPrev: ((UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafePointer<Int8>)! ``` |

Modified TclStubs.tcl_UtfToExternal

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToExternal: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` var tcl_UtfToExternal: ((UnsafeMutablePointer<Tcl_Interp>, Tcl_Encoding, UnsafePointer<Int8>, Int32, Int32, UnsafeMutablePointer<Tcl_EncodingState>, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified TclStubs.tcl_UtfToExternalDString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToExternalDString: CFunctionPointer<((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var tcl_UtfToExternalDString: ((Tcl_Encoding, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified TclStubs.tcl_UtfToLower

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToLower: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UtfToLower: ((UnsafeMutablePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_UtfToTitle

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToTitle: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UtfToTitle: ((UnsafeMutablePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_UtfToUniChar

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToUniChar: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_UniChar>) -> Int32)> ``` |
| To | ``` var tcl_UtfToUniChar: ((UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_UniChar>) -> Int32)! ``` |

Modified TclStubs.tcl_UtfToUniCharDString

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToUniCharDString: CFunctionPointer<((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Tcl_UniChar>)> ``` |
| To | ``` var tcl_UtfToUniCharDString: ((UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Tcl_DString>) -> UnsafeMutablePointer<Tcl_UniChar>)! ``` |

Modified TclStubs.tcl_UtfToUpper

|  | Declaration |
| --- | --- |
| From | ``` var tcl_UtfToUpper: CFunctionPointer<((UnsafeMutablePointer<Int8>) -> Int32)> ``` |
| To | ``` var tcl_UtfToUpper: ((UnsafeMutablePointer<Int8>) -> Int32)! ``` |

Modified TclStubs.tcl_ValidateAllMemory

|  | Declaration |
| --- | --- |
| From | ``` var tcl_ValidateAllMemory: CFunctionPointer<((UnsafePointer<Int8>, Int32) -> Void)> ``` |
| To | ``` var tcl_ValidateAllMemory: ((UnsafePointer<Int8>, Int32) -> Void)! ``` |

Modified TclStubs.tcl_VarEvalVA

|  | Declaration |
| --- | --- |
| From | ``` var tcl_VarEvalVA: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Int32)> ``` |
| To | ``` var tcl_VarEvalVA: ((UnsafeMutablePointer<Tcl_Interp>, CVaListPointer) -> Int32)! ``` |

Modified TclStubs.tcl_VarTraceInfo

|  | Declaration |
| --- | --- |
| From | ``` var tcl_VarTraceInfo: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> ClientData)> ``` |
| To | ``` var tcl_VarTraceInfo: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> ClientData)! ``` |

Modified TclStubs.tcl_VarTraceInfo2

|  | Declaration |
| --- | --- |
| From | ``` var tcl_VarTraceInfo2: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, CFunctionPointer<Tcl_VarTraceProc>, ClientData) -> ClientData)> ``` |
| To | ``` var tcl_VarTraceInfo2: ((UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, ClientData) -> ClientData)! ``` |

Modified TclStubs.tcl_WaitForEvent

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WaitForEvent: CFunctionPointer<((UnsafeMutablePointer<Tcl_Time>) -> Int32)> ``` |
| To | ``` var tcl_WaitForEvent: ((UnsafeMutablePointer<Tcl_Time>) -> Int32)! ``` |

Modified TclStubs.tcl_WaitPid

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WaitPid: CFunctionPointer<((Tcl_Pid, UnsafeMutablePointer<Int32>, Int32) -> Tcl_Pid)> ``` |
| To | ``` var tcl_WaitPid: ((Tcl_Pid, UnsafeMutablePointer<Int32>, Int32) -> Tcl_Pid)! ``` |

Modified TclStubs.tcl_Write

|  | Declaration |
| --- | --- |
| From | ``` var tcl_Write: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_Write: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_WriteChars

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WriteChars: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_WriteChars: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_WriteObj

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WriteObj: CFunctionPointer<((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)> ``` |
| To | ``` var tcl_WriteObj: ((Tcl_Channel, UnsafeMutablePointer<Tcl_Obj>) -> Int32)! ``` |

Modified TclStubs.tcl_WriteRaw

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WriteRaw: CFunctionPointer<((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)> ``` |
| To | ``` var tcl_WriteRaw: ((Tcl_Channel, UnsafePointer<Int8>, Int32) -> Int32)! ``` |

Modified TclStubs.tcl_WrongNumArgs

|  | Declaration |
| --- | --- |
| From | ``` var tcl_WrongNumArgs: CFunctionPointer<((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var tcl_WrongNumArgs: ((UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>, UnsafePointer<Int8>) -> Void)! ``` |

Modified TclStubs.tclFreeObj

|  | Declaration |
| --- | --- |
| From | ``` var tclFreeObj: CFunctionPointer<((UnsafeMutablePointer<Tcl_Obj>) -> Void)> ``` |
| To | ``` var tclFreeObj: ((UnsafeMutablePointer<Tcl_Obj>) -> Void)! ``` |

Modified Tcl_AsyncCreate(_: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, _: ClientData) -> Tcl_AsyncHandler

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_AsyncCreate(_ proc: CFunctionPointer<Tcl_AsyncProc>, _ clientData: ClientData) -> Tcl_AsyncHandler ``` |
| To | ``` func Tcl_AsyncCreate(_ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!, _ clientData: ClientData) -> Tcl_AsyncHandler ``` |

Modified Tcl_CallWhenDeleted(_: UnsafeMutablePointer<Tcl_Interp>, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CallWhenDeleted(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CallWhenDeleted(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_CancelIdleCall(_: ((ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CancelIdleCall(_ idleProc: CFunctionPointer<Tcl_IdleProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CancelIdleCall(_ idleProc: ((ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_ChannelBlockModeProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelBlockModeProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverBlockModeProc> ``` |
| To | ``` func Tcl_ChannelBlockModeProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)! ``` |

Modified Tcl_ChannelClose2Proc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelClose2Proc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverClose2Proc> ``` |
| To | ``` func Tcl_ChannelClose2Proc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32) -> Int32)! ``` |

Modified Tcl_ChannelCloseProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelCloseProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverCloseProc> ``` |
| To | ``` func Tcl_ChannelCloseProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Int32)! ``` |

Modified Tcl_ChannelFlushProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelFlushProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverFlushProc> ``` |
| To | ``` func Tcl_ChannelFlushProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData) -> Int32)! ``` |

Modified Tcl_ChannelGetHandleProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelGetHandleProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetHandleProc> ``` |
| To | ``` func Tcl_ChannelGetHandleProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32, UnsafeMutablePointer<ClientData>) -> Int32)! ``` |

Modified Tcl_ChannelGetOptionProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelGetOptionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverGetOptionProc> ``` |
| To | ``` func Tcl_ChannelGetOptionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafeMutablePointer<Tcl_DString>) -> Int32)! ``` |

Modified Tcl_ChannelHandlerProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelHandlerProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverHandlerProc> ``` |
| To | ``` func Tcl_ChannelHandlerProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Int32)! ``` |

Modified Tcl_ChannelInputProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelInputProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverInputProc> ``` |
| To | ``` func Tcl_ChannelInputProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified Tcl_ChannelOutputProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelOutputProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverOutputProc> ``` |
| To | ``` func Tcl_ChannelOutputProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified Tcl_ChannelSeekProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelSeekProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSeekProc> ``` |
| To | ``` func Tcl_ChannelSeekProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int, Int32, UnsafeMutablePointer<Int32>) -> Int32)! ``` |

Modified Tcl_ChannelSetOptionProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelSetOptionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverSetOptionProc> ``` |
| To | ``` func Tcl_ChannelSetOptionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32)! ``` |

Modified Tcl_ChannelThreadActionProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelThreadActionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverThreadActionProc> ``` |
| To | ``` func Tcl_ChannelThreadActionProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)! ``` |

Modified Tcl_ChannelTruncateProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt) -> Int32)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelTruncateProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverTruncateProc> ``` |
| To | ``` func Tcl_ChannelTruncateProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt) -> Int32)! ``` |

Modified Tcl_ChannelWatchProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelWatchProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWatchProc> ``` |
| To | ``` func Tcl_ChannelWatchProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Int32) -> Void)! ``` |

Modified Tcl_ChannelWideSeekProc(_: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_ChannelWideSeekProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> CFunctionPointer<Tcl_DriverWideSeekProc> ``` |
| To | ``` func Tcl_ChannelWideSeekProc(_ chanTypePtr: UnsafePointer<Tcl_ChannelType>) -> ((ClientData, Tcl_WideInt, Int32, UnsafeMutablePointer<Int32>) -> Tcl_WideInt)! ``` |

Modified Tcl_CmdTraceProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_CmdTraceProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Int8>, CFunctionPointer<Tcl_CmdProc>, ClientData, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void) ``` |
| To | ``` typealias Tcl_CmdTraceProc = ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void) ``` |

Modified Tcl_CommandTraceInfo(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, _: ClientData) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CommandTraceInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_CommandTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |
| To | ``` func Tcl_CommandTraceInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, _ prevClientData: ClientData) -> ClientData ``` |

Modified Tcl_CreateChannelHandler(_: Tcl_Channel, _: Int32, _: ((ClientData, Int32) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateChannelHandler(_ chan: Tcl_Channel, _ mask: Int32, _ proc: CFunctionPointer<Tcl_ChannelProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CreateChannelHandler(_ chan: Tcl_Channel, _ mask: Int32, _ proc: ((ClientData, Int32) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_CreateCloseHandler(_: Tcl_Channel, _: ((ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateCloseHandler(_ chan: Tcl_Channel, _ proc: CFunctionPointer<Tcl_CloseProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CreateCloseHandler(_ chan: Tcl_Channel, _ proc: ((ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_CreateCommand(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, _: ClientData, _: ((ClientData) -> Void)!) -> Tcl_Command

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_CmdProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command ``` |
| To | ``` func Tcl_CreateCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, _ clientData: ClientData, _ deleteProc: ((ClientData) -> Void)!) -> Tcl_Command ``` |

Modified Tcl_CreateEventSource(_: ((ClientData, Int32) -> Void)!, _: ((ClientData, Int32) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateEventSource(_ setupProc: CFunctionPointer<Tcl_EventSetupProc>, _ checkProc: CFunctionPointer<Tcl_EventCheckProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CreateEventSource(_ setupProc: ((ClientData, Int32) -> Void)!, _ checkProc: ((ClientData, Int32) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_CreateExitHandler(_: ((ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateExitHandler(_ proc: CFunctionPointer<Tcl_ExitProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CreateExitHandler(_ proc: ((ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_CreateFileHandler(_: Int32, _: Int32, _: ((ClientData, Int32) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateFileHandler(_ fd: Int32, _ mask: Int32, _ proc: CFunctionPointer<Tcl_FileProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CreateFileHandler(_ fd: Int32, _ mask: Int32, _ proc: ((ClientData, Int32) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_CreateFileHandlerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_CreateFileHandlerProc = ((Int32, Int32, CFunctionPointer<Tcl_FileProc>, ClientData) -> Void) ``` |
| To | ``` typealias Tcl_CreateFileHandlerProc = ((Int32, Int32, ((ClientData, Int32) -> Void)!, ClientData) -> Void) ``` |

Modified Tcl_CreateMathFunc(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: Int32, _: UnsafeMutablePointer<Tcl_ValueType>, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateMathFunc(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ numArgs: Int32, _ argTypes: UnsafeMutablePointer<Tcl_ValueType>, _ proc: CFunctionPointer<Tcl_MathProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CreateMathFunc(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ numArgs: Int32, _ argTypes: UnsafeMutablePointer<Tcl_ValueType>, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)!, _ clientData: ClientData) ``` |

Modified Tcl_CreateNamespace(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: ClientData, _: ((ClientData) -> Void)!) -> UnsafeMutablePointer<Tcl_Namespace>

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateNamespace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_NamespaceDeleteProc>) -> UnsafeMutablePointer<Tcl_Namespace> ``` |
| To | ``` func Tcl_CreateNamespace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ clientData: ClientData, _ deleteProc: ((ClientData) -> Void)!) -> UnsafeMutablePointer<Tcl_Namespace> ``` |

Modified Tcl_CreateObjCommand(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, _: ClientData, _: ((ClientData) -> Void)!) -> Tcl_Command

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateObjCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_ObjCmdProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_CmdDeleteProc>) -> Tcl_Command ``` |
| To | ``` func Tcl_CreateObjCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ cmdName: UnsafePointer<Int8>, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, _ clientData: ClientData, _ deleteProc: ((ClientData) -> Void)!) -> Tcl_Command ``` |

Modified Tcl_CreateObjTrace(_: UnsafeMutablePointer<Tcl_Interp>, _: Int32, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, Tcl_Command, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, _: ClientData, _: ((ClientData) -> Void)!) -> Tcl_Trace

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateObjTrace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ level: Int32, _ flags: Int32, _ objProc: CFunctionPointer<Tcl_CmdObjTraceProc>, _ clientData: ClientData, _ delProc: CFunctionPointer<Tcl_CmdObjTraceDeleteProc>) -> Tcl_Trace ``` |
| To | ``` func Tcl_CreateObjTrace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ level: Int32, _ flags: Int32, _ objProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafePointer<Int8>, Tcl_Command, Int32, UnsafePointer<UnsafeMutablePointer<Tcl_Obj>>) -> Int32)!, _ clientData: ClientData, _ delProc: ((ClientData) -> Void)!) -> Tcl_Trace ``` |

Modified Tcl_CreateThread(_: UnsafeMutablePointer<Tcl_ThreadId>, _: ((ClientData) -> Void)!, _: ClientData, _: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateThread(_ idPtr: UnsafeMutablePointer<Tcl_ThreadId>, _ proc: CFunctionPointer<Tcl_ThreadCreateProc>, _ clientData: ClientData, _ stackSize: Int32, _ flags: Int32) -> Int32 ``` |
| To | ``` func Tcl_CreateThread(_ idPtr: UnsafeMutablePointer<Tcl_ThreadId>, _ proc: ((ClientData) -> Void)!, _ clientData: ClientData, _ stackSize: Int32, _ flags: Int32) -> Int32 ``` |

Modified Tcl_CreateThreadExitHandler(_: ((ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateThreadExitHandler(_ proc: CFunctionPointer<Tcl_ExitProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_CreateThreadExitHandler(_ proc: ((ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_CreateTimerHandler(_: Int32, _: ((ClientData) -> Void)!, _: ClientData) -> Tcl_TimerToken

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateTimerHandler(_ milliseconds: Int32, _ proc: CFunctionPointer<Tcl_TimerProc>, _ clientData: ClientData) -> Tcl_TimerToken ``` |
| To | ``` func Tcl_CreateTimerHandler(_ milliseconds: Int32, _ proc: ((ClientData) -> Void)!, _ clientData: ClientData) -> Tcl_TimerToken ``` |

Modified Tcl_CreateTrace(_: UnsafeMutablePointer<Tcl_Interp>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)!, _: ClientData) -> Tcl_Trace

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_CreateTrace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ level: Int32, _ proc: CFunctionPointer<Tcl_CmdTraceProc>, _ clientData: ClientData) -> Tcl_Trace ``` |
| To | ``` func Tcl_CreateTrace(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ level: Int32, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<Int8>, ((ClientData, UnsafeMutablePointer<Tcl_Interp>, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32)!, ClientData, Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Void)!, _ clientData: ClientData) -> Tcl_Trace ``` |

Modified Tcl_DeleteChannelHandler(_: Tcl_Channel, _: ((ClientData, Int32) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteChannelHandler(_ chan: Tcl_Channel, _ proc: CFunctionPointer<Tcl_ChannelProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DeleteChannelHandler(_ chan: Tcl_Channel, _ proc: ((ClientData, Int32) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_DeleteCloseHandler(_: Tcl_Channel, _: ((ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteCloseHandler(_ chan: Tcl_Channel, _ proc: CFunctionPointer<Tcl_CloseProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DeleteCloseHandler(_ chan: Tcl_Channel, _ proc: ((ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_DeleteEvents(_: ((UnsafeMutablePointer<Tcl_Event>, ClientData) -> Int32)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteEvents(_ proc: CFunctionPointer<Tcl_EventDeleteProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DeleteEvents(_ proc: ((UnsafeMutablePointer<Tcl_Event>, ClientData) -> Int32)!, _ clientData: ClientData) ``` |

Modified Tcl_DeleteEventSource(_: ((ClientData, Int32) -> Void)!, _: ((ClientData, Int32) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteEventSource(_ setupProc: CFunctionPointer<Tcl_EventSetupProc>, _ checkProc: CFunctionPointer<Tcl_EventCheckProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DeleteEventSource(_ setupProc: ((ClientData, Int32) -> Void)!, _ checkProc: ((ClientData, Int32) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_DeleteExitHandler(_: ((ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteExitHandler(_ proc: CFunctionPointer<Tcl_ExitProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DeleteExitHandler(_ proc: ((ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_DeleteThreadExitHandler(_: ((ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DeleteThreadExitHandler(_ proc: CFunctionPointer<Tcl_ExitProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DeleteThreadExitHandler(_ proc: ((ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_DontCallWhenDeleted(_: UnsafeMutablePointer<Tcl_Interp>, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DontCallWhenDeleted(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DontCallWhenDeleted(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_DoWhenIdle(_: ((ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_DoWhenIdle(_ proc: CFunctionPointer<Tcl_IdleProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_DoWhenIdle(_ proc: ((ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_EventuallyFree(_: ClientData, _: ((UnsafeMutablePointer<Int8>) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_EventuallyFree(_ clientData: ClientData, _ freeProc: CFunctionPointer<Tcl_FreeProc>) ``` |
| To | ``` func Tcl_EventuallyFree(_ clientData: ClientData, _ freeProc: ((UnsafeMutablePointer<Int8>) -> Void)!) ``` |

Modified Tcl_FSLoadFile(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafeMutablePointer<Tcl_Obj>, _: UnsafePointer<Int8>, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, _: UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, _: UnsafeMutablePointer<Tcl_LoadHandle>, _: UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_FSLoadFile(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ sym1: UnsafePointer<Int8>, _ sym2: UnsafePointer<Int8>, _ proc1Ptr: UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, _ proc2Ptr: UnsafeMutablePointer<CFunctionPointer<Tcl_PackageInitProc>>, _ handlePtr: UnsafeMutablePointer<Tcl_LoadHandle>, _ unloadProcPtr: UnsafeMutablePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32 ``` |
| To | ``` func Tcl_FSLoadFile(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pathPtr: UnsafeMutablePointer<Tcl_Obj>, _ sym1: UnsafePointer<Int8>, _ sym2: UnsafePointer<Int8>, _ proc1Ptr: UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, _ proc2Ptr: UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Interp>) -> Int32)?>, _ handlePtr: UnsafeMutablePointer<Tcl_LoadHandle>, _ unloadProcPtr: UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32 ``` |

Modified Tcl_FSLoadFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias Tcl_FSLoadFileProc = ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<CFunctionPointer<Tcl_FSUnloadFileProc>>) -> Int32) ``` |
| To | ``` typealias Tcl_FSLoadFileProc = ((UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Obj>, UnsafeMutablePointer<Tcl_LoadHandle>, UnsafeMutablePointer<((Tcl_LoadHandle) -> Void)?>) -> Int32) ``` |

Modified Tcl_GetAssocData(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)?>) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetAssocData(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ procPtr: UnsafeMutablePointer<CFunctionPointer<Tcl_InterpDeleteProc>>) -> ClientData ``` |
| To | ``` func Tcl_GetAssocData(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ procPtr: UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)?>) -> ClientData ``` |

Modified Tcl_GetMathFuncInfo(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<Int32>, _: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, _: UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)?>, _: UnsafeMutablePointer<ClientData>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_GetMathFuncInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ numArgsPtr: UnsafeMutablePointer<Int32>, _ argTypesPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, _ procPtr: UnsafeMutablePointer<CFunctionPointer<Tcl_MathProc>>, _ clientDataPtr: UnsafeMutablePointer<ClientData>) -> Int32 ``` |
| To | ``` func Tcl_GetMathFuncInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ numArgsPtr: UnsafeMutablePointer<Int32>, _ argTypesPtr: UnsafeMutablePointer<UnsafeMutablePointer<Tcl_ValueType>>, _ procPtr: UnsafeMutablePointer<((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafeMutablePointer<Tcl_Value>, UnsafeMutablePointer<Tcl_Value>) -> Int32)?>, _ clientDataPtr: UnsafeMutablePointer<ClientData>) -> Int32 ``` |

Modified Tcl_LimitAddHandler(_: UnsafeMutablePointer<Tcl_Interp>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _: ClientData, _: ((ClientData) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitAddHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32, _ handlerProc: CFunctionPointer<Tcl_LimitHandlerProc>, _ clientData: ClientData, _ deleteProc: CFunctionPointer<Tcl_LimitHandlerDeleteProc>) ``` |
| To | ``` func Tcl_LimitAddHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32, _ handlerProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _ clientData: ClientData, _ deleteProc: ((ClientData) -> Void)!) ``` |

Modified Tcl_LimitRemoveHandler(_: UnsafeMutablePointer<Tcl_Interp>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_LimitRemoveHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32, _ handlerProc: CFunctionPointer<Tcl_LimitHandlerProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_LimitRemoveHandler(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ type: Int32, _ handlerProc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_Main(_: Int32, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_Main(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ appInitProc: CFunctionPointer<Tcl_AppInitProc>) ``` |
| To | ``` func Tcl_Main(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ appInitProc: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!) ``` |

Modified Tcl_OpenTcpServer(_: UnsafeMutablePointer<Tcl_Interp>, _: Int32, _: UnsafePointer<Int8>, _: ((ClientData, Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Void)!, _: ClientData) -> Tcl_Channel

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_OpenTcpServer(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ port: Int32, _ host: UnsafePointer<Int8>, _ acceptProc: CFunctionPointer<Tcl_TcpAcceptProc>, _ callbackData: ClientData) -> Tcl_Channel ``` |
| To | ``` func Tcl_OpenTcpServer(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ port: Int32, _ host: UnsafePointer<Int8>, _ acceptProc: ((ClientData, Tcl_Channel, UnsafeMutablePointer<Int8>, Int32) -> Void)!, _ callbackData: ClientData) -> Tcl_Channel ``` |

Modified Tcl_QueryTimeProc(_: UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, _: UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, _: UnsafeMutablePointer<ClientData>)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_QueryTimeProc(_ getProc: UnsafeMutablePointer<CFunctionPointer<Tcl_GetTimeProc>>, _ scaleProc: UnsafeMutablePointer<CFunctionPointer<Tcl_ScaleTimeProc>>, _ clientData: UnsafeMutablePointer<ClientData>) ``` |
| To | ``` func Tcl_QueryTimeProc(_ getProc: UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, _ scaleProc: UnsafeMutablePointer<((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)?>, _ clientData: UnsafeMutablePointer<ClientData>) ``` |

Modified Tcl_SetAssocData(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetAssocData(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ proc: CFunctionPointer<Tcl_InterpDeleteProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_SetAssocData(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ name: UnsafePointer<Int8>, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_SetExitProc(_: ((ClientData) -> Void)!) -> ((ClientData) -> Void)!

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetExitProc(_ proc: CFunctionPointer<Tcl_ExitProc>) -> CFunctionPointer<Tcl_ExitProc> ``` |
| To | ``` func Tcl_SetExitProc(_ proc: ((ClientData) -> Void)!) -> ((ClientData) -> Void)! ``` |

Modified Tcl_SetMainLoop(_: (() -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetMainLoop(_ proc: CFunctionPointer<Tcl_MainLoopProc>) ``` |
| To | ``` func Tcl_SetMainLoop(_ proc: (() -> Void)!) ``` |

Modified Tcl_SetResult(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafeMutablePointer<Int8>, _: ((UnsafeMutablePointer<Int8>) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetResult(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ result: UnsafeMutablePointer<Int8>, _ freeProc: CFunctionPointer<Tcl_FreeProc>) ``` |
| To | ``` func Tcl_SetResult(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ result: UnsafeMutablePointer<Int8>, _ freeProc: ((UnsafeMutablePointer<Int8>) -> Void)!) ``` |

Modified Tcl_SetTimeProc(_: ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, _: ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_SetTimeProc(_ getProc: CFunctionPointer<Tcl_GetTimeProc>, _ scaleProc: CFunctionPointer<Tcl_ScaleTimeProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_SetTimeProc(_ getProc: ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, _ scaleProc: ((UnsafeMutablePointer<Tcl_Time>, ClientData) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_StaticPackage(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, _: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_StaticPackage(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pkgName: UnsafePointer<Int8>, _ initProc: CFunctionPointer<Tcl_PackageInitProc>, _ safeInitProc: CFunctionPointer<Tcl_PackageInitProc>) ``` |
| To | ``` func Tcl_StaticPackage(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ pkgName: UnsafePointer<Int8>, _ initProc: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!, _ safeInitProc: ((UnsafeMutablePointer<Tcl_Interp>) -> Int32)!) ``` |

Modified Tcl_TraceCommand(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, _: ClientData) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_TraceCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_CommandTraceProc>, _ clientData: ClientData) -> Int32 ``` |
| To | ``` func Tcl_TraceCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, _ clientData: ClientData) -> Int32 ``` |

Modified Tcl_TraceVar(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _: ClientData) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_TraceVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) -> Int32 ``` |
| To | ``` func Tcl_TraceVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _ clientData: ClientData) -> Int32 ``` |

Modified Tcl_TraceVar2(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _: ClientData) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_TraceVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) -> Int32 ``` |
| To | ``` func Tcl_TraceVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _ clientData: ClientData) -> Int32 ``` |

Modified Tcl_UntraceCommand(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UntraceCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_CommandTraceProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_UntraceCommand(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> Void)!, _ clientData: ClientData) ``` |

Modified Tcl_UntraceVar(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UntraceVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_UntraceVar(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _ clientData: ClientData) ``` |

Modified Tcl_UntraceVar2(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _: ClientData)

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_UntraceVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ proc: CFunctionPointer<Tcl_VarTraceProc>, _ clientData: ClientData) ``` |
| To | ``` func Tcl_UntraceVar2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ proc: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _ clientData: ClientData) ``` |

Modified Tcl_VarTraceInfo(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _: ClientData) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_VarTraceInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_VarTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |
| To | ``` func Tcl_VarTraceInfo(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ varName: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _ prevClientData: ClientData) -> ClientData ``` |

Modified Tcl_VarTraceInfo2(_: UnsafeMutablePointer<Tcl_Interp>, _: UnsafePointer<Int8>, _: UnsafePointer<Int8>, _: Int32, _: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _: ClientData) -> ClientData

|  | Declaration |
| --- | --- |
| From | ``` func Tcl_VarTraceInfo2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: CFunctionPointer<Tcl_VarTraceProc>, _ prevClientData: ClientData) -> ClientData ``` |
| To | ``` func Tcl_VarTraceInfo2(_ interp: UnsafeMutablePointer<Tcl_Interp>, _ part1: UnsafePointer<Int8>, _ part2: UnsafePointer<Int8>, _ flags: Int32, _ procPtr: ((ClientData, UnsafeMutablePointer<Tcl_Interp>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Int8>)!, _ prevClientData: ClientData) -> ClientData ``` |

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

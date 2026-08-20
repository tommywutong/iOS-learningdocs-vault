---
title: Carbon Core Release Notes
apple_id: TP40000988
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-CarbonCore/index.html
archived_at: '2026-07-18T02:50:21.698234Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# CarbonCore Framework Release Notes for Mac OS X v10.5

> [!IMPORTANT]
> 

CarbonCore is accessible within the CoreServices umbrella framework and is pulled into your application by linking against CoreServices or one of the higher level umbrellas such as Cocoa or Carbon which bring in CoreServices.

This document describes the changes in CarbonCore since Mac OS X release 10.4, Tiger. Note that you may be able to find more information on many of these changes in Apple's developer documentation.

#### Contents:

- [64-bit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Alias Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Backup (Time Machine)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [File Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Folder Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [FSEvents](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)
- [Resource Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ny)

### 64-bit

Mac OS X Leopard contains 64-bit versions of many system frameworks, enabling building and running Cocoa apps as 64-bit.

A few new API calls have been added to support 64-bit applications. Many of the API calls which were deprecated for Mac OS X 10.4 and a few other APIs are unavailable for 64-bit applications. These functions are marked [32-bit only] in their descriptions in the header files. Routines which operate on the FSSpec data type (and the parameter block based variants) are not available for 64-bit applications. New types have been introduced to allow the same code to be used by both 32-bit and 64-bit applications.

### Alias Manager

The Alias Manager adds two new API:

```
OSStatus FSNewAliasFromPath( const char *fromFilePath, const char *targetPath, OptionBits flags, AliasHandle *inAlias, Boolean *isDirectory);
OSStatus FSMatchAliasBulk( const FSRef *fromFile, unsigned long rulesMask, AliasHandle inAlias, short *aliasCount, FSRef *aliasList, Boolean *needsUpdate, FSAliasFilterProcPtr aliasFilter, void *yourDataPtr);
```

[FSNewAliasFromPath](https://developer.apple.com/documentation/coreservices/1444431-fsnewaliasfrompath) creates a new alias record using UTF-8 POSIX style paths. [FSMatchAliasBulk](https://developer.apple.com/documentation/coreservices/1444389-fsmatchaliasbulk) is the same as `FSMatchAlias` except it takes a 64-bit friendly [FSAliasFilterProcPtr](https://developer.apple.com/documentation/coreservices/fsaliasfilterprocptr) instead of the now deprecated `AliasFilterUPP`. See Aliases.h for more information.

### Backup (Time Machine)

Two API calls have been added for managing items that should be skipped by Time Machine:

```
OSStatus CSBackupSetItemExcluded(CFURLRef item, Boolean exclude, Boolean excludeByPath);
Boolean CSBackupIsItemExcluded(CFURLRef item, Boolean *excludeByPath);
```

See BackupCore.h for more information.

### File Manager

The File Manager has added several API calls to support safe save operations. FSReplaceObject and FSPathReplaceObject have been provided to assist in properly preserving metadata during safe save operations. Supporting routines will return the temporary directory which ReplaceObject uses by default:

```
OSStatus FSReplaceObject(const FSRef *originalObject, const FSRef *replacementObject, CFStringRef newName, CFStringRef temporaryName, const FSRef *temporaryDirectory, OptionBits flags, FSRef *resultObject);
OSStatus FSPathReplaceObject(const char *originalObjectPath, const char *replacementObjectPath, CFStringRef newName, CFStringRef temporaryName, const char *temporaryDirectoryPath, OptionBits flags);
OSStatus FSGetTemporaryDirectoryForReplaceObject(const FSRef *originalObject, FSRef *temporaryDirectory, OptionBits flags);
OSStatus FSPathGetTemporaryDirectoryForReplaceObject(const char *originalObjectPath, char *temporaryDirectoryPath, UInt32 maxPathSize, OptionBits flags);
```

MoveToTrash has been added as a new FSFileOperation. These calls are similar to the Move FSFileOperation with the Trash as the implied destination and an optional output parameter to return the new location (since the operation will place the item in the proper trash location based on its current location):

```
OSStatus FSMoveObjectToTrashSync(const FSRef *source, FSRef *target, OptionBits options);
OSStatus FSPathMoveObjectToTrashSync(const char *sourcePath, char **targetPath, OptionBits options);
OSStatus FSMoveObjectToTrashAsync(FSFileOperationRef fileOp, const FSRef *source, OptionBits flags, FSFileOperationStatusProcPtr callback <null>, CFTimeInterval statusChangeInterval, FSFileOperationClientContext *clientContext);
OSStatus FSPathMoveObjectToTrashAsync(FSFileOperationRef fileOp, const char *sourcePath, OptionBits flags, FSPathFileOperationStatusProcPtr callback, CFTimeInterval statusChangeInterval, FSFileOperationClientContext *clientContext);
```

A new set of API calls have been provided for the deletion of file system objects:

```
OSErr FSUnlinkObject(const FSRef *ref);
OSErr PBUnlinkObjectSync(FSRefParam *paramBlock);
void PBUnlinkObjectAsync(FSRefParam *paramBlock);
```

These calls behave very similar to their DeleteObject counterparts, except that they will succeed on open objects and understand how properly handle archive directory links (aka directory hard links). The UnlinkObject calls behave more like the [unlink(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/unlink.2.html#//apple_ref/doc/man/2/unlink) system call.

As part of the 64-bit cleanup two new types have been introduced. [FSVolumeRefNum](https://developer.apple.com/documentation/coreservices/fsvolumerefnum) (typed as SInt16) is used to represent volume reference numbers and FSIORefNum (typed int for 64-bit, SInt16 for 32-bit) is used for fork reference numbers. Several new API calls were added to provide replacements for functions that needed to be deprecated due to dependencies on types that have been deprecated. These functions mostly replace similar variants which used parameter blocks that are not present for 64-bit:

```
OSStatus FSGetVolumeParms(FSVolumeRefNum volume, GetVolParmsInfoBuffer *buffer, ByteCount bufferSize);
OSStatus FSGetVolumeMountInfoSize(FSVolumeRefNum volume, ByteCount *size);
OSStatus FSGetVolumeMountInfo(FSVolumeRefNum volume, BytePtr buffer, ByteCount bufferSize, ByteCount *actualSize <out, NULL>);
OSStatus FSVolumeMount(BytePtr buffer, FSVolumeRefNum *mountedVolume);
OSStatus FSFlushVolume(FSVolumeRefNum vRefNum);
OSStatus PBFlushVolumeSync(FSRefParamPtr paramBlock);
OSStatus PBFlushVolumeAsync(FSRefParamPtr paramBlock);
OSStatus PBFSCopyFileSync(FSRefParamPtr paramBlock);
OSStatus PBFSCopyFileAsync(FSRefParamPtr paramBlock);
OSStatus FSResolveNodeID(FSVolumeRefNum volume, UInt32 nodeID, FSRefPtr newRef);
OSStatus PBFSResolveNodeIDSync(FSRefParamPtr paramBlock);
OSStatus PBFSResolveNodeIDAsync(FSRefParamPtr paramBlock);
```

See Files.h for more information.

### Folder Manager

Several folders have had a "deny everyone delete" ACL added to them in Leopard. This was done to help prevent accidental deletion of important system and user folders.

One new API call has been added to the Folder Manager to aid in the transition from FSSpec style names to Unicode names:

```
OSStatus GetFolderNameUnicode(FSVolumeRefNum vRefNum, OSType foldType, FSVolumeRefNum *foundVRefNum, HFSUniStr255 *name);
```

The older `GetFolderName` call has been deprecated (and is unavailable for 64-bit).

Several new folder selectors have been added:

```
    kSpotlightImportersFolderType       = 'simp',    // Folder for Spotlight importers, usually /Library/Spotlight/ or ~/Library/Spotlight, etc.
    kSpotlightMetadataCacheFolderType   = 'scch',    // Folder for Spotlight metadata caches, for example: ~/Library/Caches/Metadata/
    kInputManagersFolderType            = 'inpt',    // InputManagers
    kInputMethodsFolderType             = 'inpf',    // ../Library/Input Methods/
    kLibraryAssistantsFolderType        = 'astl',    // Refers to the [domain]/Library/Assistants folder
    kAudioDigidesignFolderType          = 'adig',    // Refers to the Digidesign subfolder of the Audio Plug-ins folder
    kAudioVSTFolderType                 = 'avst',    // Refers to the VST subfolder of the Audio Plug-ins folder
    kColorPickersFolderType             = 'cpkr',    // Refers to the ColorPickers folder
    kCompositionsFolderType             = 'cmps',    // Refers to the Compositions folder
    kFontCollectionsFolderType          = 'fncl',    // Refers to the FontCollections folder
    kiMovieFolderType                   = 'imov',    // Refers to the iMovie folder
    kiMoviePlugInsFolderType            = 'impi',    // Refers to the Plug-ins subfolder of the iMovie Folder
    kiMovieSoundEffectsFolderType       = 'imse',    // Refers to the Sound Effects subfolder of the iMovie Folder
    kDownloadsFolderType                = 'down',    // Refers to the ~/Downloads folder
```

See Folders.h for more information.

### FSEvents

Leopard introduces a new API for monitoring file system changes. FSEvents provides a runloop based mechanism for receiving notifications of directory level file system changes. FSEvents allows for monitoring of directory hierarchies (the existing kqueue mechanism only reporting changes made at the root level of the directory being monitored). FSEvents supports batch notifications (many changes in a single callback) and tunable latency (allow the client to adjust how long after an event has occurred before a callback would be sent). See FSEvents.h for more information.

### Resource Manager

The Resource Manager introduces several new types and deprecates its `FSSpec` (and older) based API as part of the changes for 64-bit support:

```
typedef SInt16 ResID;
typedef SInt16 ResAttributes;
typedef SInt16 ResFileAttributes;
typedef SInt16 ResourceCount;
typedef SInt16 ResourceIndex;
typedef FSIORefNum ResFileRefNum;
```

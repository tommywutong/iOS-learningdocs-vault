---
title: Storing file references in CFPreferences
apple_id: DTS10003323
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreFoundation
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1350/_index.html
archived_at: '2026-07-18T02:30:25.721598Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1350

# Storing file references in CFPreferences

## Q:  What is the most robust way to store a file reference into a CFPreference?

A: What is the most robust way to store a file reference into a CFPreference?

Convert your file reference into an Alias handle; create a CFData with the contents of that Alias handle and then use CFPreferencesSetAppValue and CFPreferencesAppSynchronize to store it into your preferences file.

The first listing shows how to save a File Reference to a Preference file, and the second how to reload the File Reference from the Preference File.

__Listing 1__  Saving a file reference into a CFPreference:

```
/***************************************************** * * SaveFSRefToPref(inFSRef, inKey) * * Purpose: Saves a file reference in an application preference * * Inputs: inFSRef - The file reference *           inKey - the preference key * * Returns: none */ void SaveFSRefToPref(const FSRef* inFSRef,                       const CFStringRef inKey) {     AliasHandle tAliasHdl;     OSErr err = FSNewAlias(NULL, inFSRef, &tAliasHdl);     require_noerr(err, CantCreateAlias);      CFDataRef tCFDataRef;     tCFDataRef = CFDataCreate(kCFAllocatorDefault,                               (UInt8*) *tAliasHdl,                               GetHandleSize((Handle) tAliasHdl));     require(NULL != tCFDataRef, CantCreateCFData);      // set the preferences     CFPreferencesSetAppValue( inKey,                                tCFDataRef,                               kCFPreferencesCurrentApplication);     // sync to disk     CFPreferencesAppSynchronize(kCFPreferencesCurrentApplication);      CFRelease(tCFDataRef); CantCreateCFData:         DisposeHandle((Handle) tAliasHdl); CantCreateAlias:         return; }
```

To restore your file reference from the preference:

__Listing 2__  Restoring the file reference:

```
/***************************************************** * * LoadFSRefFromPref(inFSRef, inKey) * * Purpose: Loads a file reference from an application preference * * Inputs: outFSRef - Address where to store the file reference *           inKey - the preference key * * Returns: Boolean - true if the load was successful */ Boolean LoadFSRefFromPref(FSRef* outFSRef, CFStringRef inKey) {     Boolean result = false; // assume failure (pessimist!)      CFDataRef tCFDataRef;     tCFDataRef = (CFDataRef) CFPreferencesCopyAppValue(                        inKey,                         kCFPreferencesCurrentApplication);     require(NULL != tCFDataRef, CantGetPreference);      CFIndex dataSize = CFDataGetLength(tCFDataRef);     AliasHandle tAliasHdl = (AliasHandle) NewHandle(dataSize);     require(NULL != tAliasHdl, CantAllocateAlias);      CFDataGetBytes(tCFDataRef,                    CFRangeMake(0, dataSize),                     (UInt8*) *tAliasHdl);       FSRef tFSRef;     Boolean wasChanged;     OSErr err = FSResolveAlias(NULL,                                 tAliasHdl,                                 outFSRef,                                 &wasChanged);     if (noErr == err) result = true;      DisposeHandle((Handle) tAliasHdl);  CantAllocateAlias:     CFRelease(tCFDataRef); CantGetPreference:     return result; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2005-02-23 | The third parameter to "FSResolveAlias(NULL, tAliasHdl, &outFSRef, &wasChanged);" doesn't require the "&": "FSResolveAlias(NULL, tAliasHdl, outFSRef, &wasChanged);" |
|  | New document that describes storing file references in CFPreferences |


---
title: Launch Services Release Notes
apple_id: TP40001369
resource_type: Release Note
platform: macOS
topic: Data Management
technology: ApplicationServices
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-LaunchServices/index.html
archived_at: '2026-07-18T02:50:22.342995Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Launch Services Framework Release Notes for OS X v10.5

This document summarizes changes in Launch Services for OS X v10.5 (Leopard) that are of particular interest to software developers. Note that you may be able to find more information on these changes in Apple's developer documentation.

Launch Services in OS X v10.5 (Leopard) is available as a component of the Core Services umbrella framework. This is a binary-compatible change from Mac OS 10.4, where Launch Services was part of the Application Services umbrella framework. Clients of the Launch Services API may link with the Core Services framework or a higher-level umbrella framework (Application Services, Cocoa, or Carbon).

#### Contents:

- [64-Bit Application Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [File Quarantine](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Shared File Lists](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Opening Applications with Arguments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [New Info.plist Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrzfvbuqmjnknltc)

### 64-Bit Application Support

OS X Leopard contains 64-bit versions of many system frameworks, including Launch Services, enabling building and running Cocoa applications in a 64-bit address space. The 64-bit version of the Launch Services API differs from the 32-bit API in just one minor detail: two fields in the LSItemInfoRecord structure (iconFileName and kindID) have been eliminated. They are unused and undocumented in the 32-bit API, and so have not been carried forward to the 64-bit API.

### File Quarantine

File Quarantine is a new feature in Leopard designed to protect users from trojan horse attacks. It allows applications which download file content from the Internet to place files in “quarantine” to indicate that the file could be from an untrustworthy source. An application quarantines a file simply by assigning values to one or more quarantine properties which preserve information about when and where the file come from.

When the Launch Services API is used to open a quarantined file and the file appears to be an application, script, or other executable file type, Launch Services will display an alert to confirm the user understands the file is some kind of application. If the file is opened, the quarantine properties are automatically cleared by Launch Services if the user has write access to the file.

The quarantine properties dictionary is a new named attribute accessible with the [LSCopyItemAttribute](https://developer.apple.com/documentation/coreservices/1445023-lscopyitemattribute) or [LSCopyItemAttributes](https://developer.apple.com/documentation/coreservices/1446078-lscopyitemattributes) functions. A new string constant defines the name of the quarantine properties attribute:

```
const CFStringRef kLSItemQuarantineProperties;
```

The quarantine properties dictionary is modified using a new function for setting named attributes. In Leopard, the quarantine properties dictionary is the only settable named attribute.

```
    OSStatus LSSetItemAttribute(
        const FSRef *  inItem,
        LSRolesMask    inRoles,
        CFStringRef    inAttributeName,
        CFTypeRef      inValue);
```

The value of the quarantine properties attribute is a [CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref). The dictionary may contain values for the following quarantine properties:

```
    const CFStringRef kLSQuarantineAgentNameKey;
    const CFStringRef kLSQuarantineAgentBundleIdentifierKey;
    const CFStringRef kLSQuarantineTimeStampKey;
    const CFStringRef kLSQuarantineTypeKey;
    const CFStringRef kLSQuarantineOriginURLKey;
    const CFStringRef kLSQuarantineDataURLKey;
```

For more information about accessing named attributes, see interface LSInfo.h. For specific information about quarantine properties, see the new interface file LSQuarantine.h. Automatic file quarantining may also be enabled as a process-wide setting using an application Info.plist key (see [New Info.plist Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrzfvbuqmjnknltc)).

### Shared File Lists

The Shared File List API is new to Launch Services in OS X Leopard. This API provides access to several kinds of system-global and per-user persistent lists of file system objects, such as recent documents and applications, favorites, and login items. For details, see the new interface file LSSharedFileList.h.

### Opening Applications with Arguments

The [LSApplicationParameters](https://developer.apple.com/documentation/coreservices/lsapplicationparameters) structure introduced in OS X v10.4 contains an `argv` field designed for passing arguments to an application's `main` function. This API feature was disabled in the 10.4 release but is implemented in Leopard. If a new application process is created as a result of calling to [LSOpenApplication](https://developer.apple.com/documentation/coreservices/1447930-lsopenapplication), [LSOpenItemsWithRole](https://developer.apple.com/documentation/coreservices/1449783-lsopenitemswithrole) or [LSOpenURLsWithRole](https://developer.apple.com/documentation/coreservices/1448184-lsopenurlswithrole) , the elements of the argv field are passed to the application's main function.

### New Info.plist Keys

Launch Services in Leopard supports several new Info.plist keys for configuring various application settings, including automatic file quarantine mode, CPU architecture configuration for universal applications, and document type handler ranking. The table below summarizes the meaning and usage of each new key:

| Key: | `LSArchitecturePriority` |
| Value type: | Array of strings |
| Valid values: | ppc, ppc64, i386, x86_64 |
| Notes: | This key specifies the valid set and preferred selection order of the available executable architectures in a universal application bundle. For example, if i386 appears before x86_64 in the array, then on 64-bit Intel CPUs, the 32-bit architecture will be selected unless the user changes the setting in the application Info window in the Finder. If ppc appears in the array before i386, then on Intel CPUs _Rosetta execution will be preferred over native execution_. Use the `LSRequiresNativeExecution` key to prevent an app from executing in the Rosetta environment. |

| Key: | `LSMinimumSystemVersionByArchitecture` |
| Value type: | Dictionary |
| Valid keys: | ppc, ppc64, i386, x86_64 |
| Valid values: | An OS X release version string, such as "10.5" or "10.4.2" |
| Notes: | This key controls the minimum system version number that is permitted to execute each architecture in a universal application bundle. For example, if the value of the ppc64 key is "10.5.2," then releases prior to 10.5.2 will not allow the application to launch in 64-bit mode on PowerPC CPUs. |

| Key: | `LSFileQuarantineEnabled` |
| Value type: | Boolean |
| Notes: | When the value of this key is `true`, all files _created_ by the application process will be quarantined by OS X. Three quarantine properties can be assigned automatically: the timestamp (current time), and the application name and bundle identifier (`kLSQuarantineTimeStampKey`, `kLSQuarantineAgentNameKey`, `kLSQuarantineAgentBundleIdentifierKey`). OS X does not have sufficient information to assign several important quarantine properties, such as the source URL; use the API to set additional properties. Automatic quarantine is useful when an application does not have complete control over the files it creates, for example, if it hosts externally-developed plugins. |

| Key: | `LSHandlerRank` |
| Value type: | String |
| Valid values: | Owner, Default, Alternate, None |
| Notes: | Handler ranking is a mechanism for fine-tuning the document binding selection rules in Launch Services. The `LSHandlerRank` key appears document type dictionaries under the `CFBundleDocumentTypes` Info.plist key. If the key is not present, the document type claim has rank `Default`. Specify rank `Owner` when your application is the primary handler for a custom document type. Launch Services will prefer a document type `Owner` over `Default` document type claims. Rank `Alternate` is used when the application is a so-called “secondary” editor or viewer of the document type. For example, TextEdit in Leopard is an Alternate editor of Microsoft Word documents because it does not support all formatting options provided in Word. If Microsoft Word is installed, Launch Services will prefer it as the default handler when opening Word documents. Finally, use rank None if your application should never be selected when opening the associated document type, but wants to accept drops of this document type onto your application icon. |

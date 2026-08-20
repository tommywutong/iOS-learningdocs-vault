---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreServices.html
archived_at: '2026-07-18T02:53:00.494495Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreServices Changes for Objective-C

### CoreServices

#### DictionaryServices.h

Modified [DCSCopyTextDefinition()](https://developer.apple.com/documentation/coreservices/1446842-dcscopytextdefinition)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef DCSCopyTextDefinition (     DCSDictionaryRef dictionary,     CFStringRef textString,     CFRange range ); ``` |
| To | ``` CFStringRef _Nullable DCSCopyTextDefinition (     DCSDictionaryRef _Nullable dictionary,     CFStringRef _Nonnull textString,     CFRange range ); ``` |

Modified [DCSGetTermRangeInString()](https://developer.apple.com/documentation/coreservices/1450556-dcsgettermrangeinstring)

|  | Declaration |
| --- | --- |
| From | ``` CFRange DCSGetTermRangeInString (     DCSDictionaryRef dictionary,     CFStringRef textString,     CFIndex offset ); ``` |
| To | ``` CFRange DCSGetTermRangeInString (     DCSDictionaryRef _Nullable dictionary,     CFStringRef _Nonnull textString,     CFIndex offset ); ``` |

#### FSEvents.h

Modified [FSEventsCopyUUIDForDevice()](https://developer.apple.com/documentation/coreservices/1444453-fseventscopyuuidfordevice)

|  | Declaration |
| --- | --- |
| From | ``` CFUUIDRef FSEventsCopyUUIDForDevice (     dev_t dev ); ``` |
| To | ``` CFUUIDRef _Nullable FSEventsCopyUUIDForDevice (     dev_t dev ); ``` |

Modified [FSEventStreamCopyDescription()](https://developer.apple.com/documentation/coreservices/1442676-fseventstreamcopydescription)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef FSEventStreamCopyDescription (     ConstFSEventStreamRef streamRef ); ``` |
| To | ``` CFStringRef _Nonnull FSEventStreamCopyDescription (     ConstFSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamCopyPathsBeingWatched()](https://developer.apple.com/documentation/coreservices/1447917-fseventstreamcopypathsbeingwatch)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef FSEventStreamCopyPathsBeingWatched (     ConstFSEventStreamRef streamRef ); ``` |
| To | ``` CFArrayRef _Nonnull FSEventStreamCopyPathsBeingWatched (     ConstFSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamCreate()](https://developer.apple.com/documentation/coreservices/1443980-fseventstreamcreate)

|  | Declaration |
| --- | --- |
| From | ``` FSEventStreamRef FSEventStreamCreate (     CFAllocatorRef allocator,     FSEventStreamCallback callback,     FSEventStreamContext *context,     CFArrayRef pathsToWatch,     FSEventStreamEventId sinceWhen,     CFTimeInterval latency,     FSEventStreamCreateFlags flags ); ``` |
| To | ``` FSEventStreamRef _Nullable FSEventStreamCreate (     CFAllocatorRef _Nullable allocator,     FSEventStreamCallback _Nonnull callback,     FSEventStreamContext * _Nullable context,     CFArrayRef _Nonnull pathsToWatch,     FSEventStreamEventId sinceWhen,     CFTimeInterval latency,     FSEventStreamCreateFlags flags ); ``` |

Modified [FSEventStreamCreateRelativeToDevice()](https://developer.apple.com/documentation/coreservices/1447341-fseventstreamcreaterelativetodev)

|  | Declaration |
| --- | --- |
| From | ``` FSEventStreamRef FSEventStreamCreateRelativeToDevice (     CFAllocatorRef allocator,     FSEventStreamCallback callback,     FSEventStreamContext *context,     dev_t deviceToWatch,     CFArrayRef pathsToWatchRelativeToDevice,     FSEventStreamEventId sinceWhen,     CFTimeInterval latency,     FSEventStreamCreateFlags flags ); ``` |
| To | ``` FSEventStreamRef _Nullable FSEventStreamCreateRelativeToDevice (     CFAllocatorRef _Nullable allocator,     FSEventStreamCallback _Nonnull callback,     FSEventStreamContext * _Nullable context,     dev_t deviceToWatch,     CFArrayRef _Nonnull pathsToWatchRelativeToDevice,     FSEventStreamEventId sinceWhen,     CFTimeInterval latency,     FSEventStreamCreateFlags flags ); ``` |

Modified [FSEventStreamFlushAsync()](https://developer.apple.com/documentation/coreservices/1441727-fseventstreamflushasync)

|  | Declaration |
| --- | --- |
| From | ``` FSEventStreamEventId FSEventStreamFlushAsync (     FSEventStreamRef streamRef ); ``` |
| To | ``` FSEventStreamEventId FSEventStreamFlushAsync (     FSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamFlushSync()](https://developer.apple.com/documentation/coreservices/1445629-fseventstreamflushsync)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamFlushSync (     FSEventStreamRef streamRef ); ``` |
| To | ``` void FSEventStreamFlushSync (     FSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamGetDeviceBeingWatched()](https://developer.apple.com/documentation/coreservices/1449675-fseventstreamgetdevicebeingwatch)

|  | Declaration |
| --- | --- |
| From | ``` dev_t FSEventStreamGetDeviceBeingWatched (     ConstFSEventStreamRef streamRef ); ``` |
| To | ``` dev_t FSEventStreamGetDeviceBeingWatched (     ConstFSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamGetLatestEventId()](https://developer.apple.com/documentation/coreservices/1446030-fseventstreamgetlatesteventid)

|  | Declaration |
| --- | --- |
| From | ``` FSEventStreamEventId FSEventStreamGetLatestEventId (     ConstFSEventStreamRef streamRef ); ``` |
| To | ``` FSEventStreamEventId FSEventStreamGetLatestEventId (     ConstFSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamInvalidate()](https://developer.apple.com/documentation/coreservices/1446990-fseventstreaminvalidate)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamInvalidate (     FSEventStreamRef streamRef ); ``` |
| To | ``` void FSEventStreamInvalidate (     FSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamRelease()](https://developer.apple.com/documentation/coreservices/1445989-fseventstreamrelease)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamRelease (     FSEventStreamRef streamRef ); ``` |
| To | ``` void FSEventStreamRelease (     FSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamRetain()](https://developer.apple.com/documentation/coreservices/1444986-fseventstreamretain)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamRetain (     FSEventStreamRef streamRef ); ``` |
| To | ``` void FSEventStreamRetain (     FSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamScheduleWithRunLoop()](https://developer.apple.com/documentation/coreservices/1447824-fseventstreamschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamScheduleWithRunLoop (     FSEventStreamRef streamRef,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void FSEventStreamScheduleWithRunLoop (     FSEventStreamRef _Nonnull streamRef,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [FSEventStreamSetDispatchQueue()](https://developer.apple.com/documentation/coreservices/1444164-fseventstreamsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamSetDispatchQueue (     FSEventStreamRef streamRef,     dispatch_queue_t q ); ``` |
| To | ``` void FSEventStreamSetDispatchQueue (     FSEventStreamRef _Nonnull streamRef,     dispatch_queue_t _Nullable q ); ``` |

Modified [FSEventStreamSetExclusionPaths()](https://developer.apple.com/documentation/coreservices/1444666-fseventstreamsetexclusionpaths)

|  | Declaration |
| --- | --- |
| From | ``` Boolean FSEventStreamSetExclusionPaths (     FSEventStreamRef streamRef,     CFArrayRef pathsToExclude ); ``` |
| To | ``` Boolean FSEventStreamSetExclusionPaths (     FSEventStreamRef _Nonnull streamRef,     CFArrayRef _Nonnull pathsToExclude ); ``` |

Modified [FSEventStreamShow()](https://developer.apple.com/documentation/coreservices/1444302-fseventstreamshow)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamShow (     ConstFSEventStreamRef streamRef ); ``` |
| To | ``` void FSEventStreamShow (     ConstFSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamStart()](https://developer.apple.com/documentation/coreservices/1448000-fseventstreamstart)

|  | Declaration |
| --- | --- |
| From | ``` Boolean FSEventStreamStart (     FSEventStreamRef streamRef ); ``` |
| To | ``` Boolean FSEventStreamStart (     FSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamStop()](https://developer.apple.com/documentation/coreservices/1447673-fseventstreamstop)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamStop (     FSEventStreamRef streamRef ); ``` |
| To | ``` void FSEventStreamStop (     FSEventStreamRef _Nonnull streamRef ); ``` |

Modified [FSEventStreamUnscheduleFromRunLoop()](https://developer.apple.com/documentation/coreservices/1441982-fseventstreamunschedulefromrunlo)

|  | Declaration |
| --- | --- |
| From | ``` void FSEventStreamUnscheduleFromRunLoop (     FSEventStreamRef streamRef,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void FSEventStreamUnscheduleFromRunLoop (     FSEventStreamRef _Nonnull streamRef,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

#### LSInfo.h

Removed [kLSInitializeDefaults](https://developer.apple.com/documentation/coreservices/launch_services/constants_no_longer_used/klsinitializedefaults)Removed [kLSMinCatInfoBitmap](https://developer.apple.com/documentation/coreservices/launch_services/constants_no_longer_used/klsmincatinfobitmap)Removed [LSInit()](https://developer.apple.com/documentation/coreservices/launch_services/1809325-lsinit)Removed [LSInitializeFlags](https://developer.apple.com/documentation/coreservices/launch_services/constants_no_longer_used)Removed [LSTerm()](https://developer.apple.com/documentation/coreservices/launch_services/1809329-lsterm)Modified [kLSHandlerOptionsDefault](https://developer.apple.com/documentation/coreservices/lshandleroptions/klshandleroptionsdefault)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSHandlerOptionsIgnoreCreator](https://developer.apple.com/documentation/coreservices/lshandleroptions/klshandleroptionsignorecreator)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified #def kLSInvalidExtensionIndex

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemContentType](https://developer.apple.com/documentation/coreservices/klsitemcontenttype)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemDisplayKind](https://developer.apple.com/documentation/coreservices/klsitemdisplaykind)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemDisplayName](https://developer.apple.com/documentation/coreservices/klsitemdisplayname)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemExtension](https://developer.apple.com/documentation/coreservices/klsitemextension)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemExtensionIsHidden](https://developer.apple.com/documentation/coreservices/klsitemextensionishidden)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemFileCreator](https://developer.apple.com/documentation/coreservices/klsitemfilecreator)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemFileType](https://developer.apple.com/documentation/coreservices/klsitemfiletype)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoAppIsScriptable](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoappisscriptable)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoAppPrefersClassic](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoappprefersclassic)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoAppPrefersNative](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1446535-appprefersnative)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoExtensionIsHidden](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoextensionishidden)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsAliasFile](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1444478-isaliasfile)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsApplication](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisapplication)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsClassicApp](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1449915-isclassicapp)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsContainer](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoiscontainer)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsInvisible](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1449065-isinvisible)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsNativeApp](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1443624-isnativeapp)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsPackage](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoispackage)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsPlainFile](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1444223-isplainfile)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsSymlink](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoissymlink)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsVolume](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisvolume)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemIsInvisible](https://developer.apple.com/documentation/coreservices/klsitemisinvisible)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemQuarantineProperties](https://developer.apple.com/documentation/coreservices/klsitemquarantineproperties)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemRoleHandlerDisplayName](https://developer.apple.com/documentation/coreservices/klsitemrolehandlerdisplayname)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestAllFlags](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestallflags)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestAllInfo](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestallinfo)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestAppTypeFlags](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestapptypeflags)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestBasicFlagsOnly](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestbasicflagsonly)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestExtension](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1448601-requestextension)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestExtensionFlagsOnly](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestextensionflagsonly)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestIconAndKind](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1447945-requesticonandkind)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestTypeCreator](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequesttypecreator)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified kLSUnknownKindID

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSCanRefAcceptItem()](https://developer.apple.com/documentation/coreservices/1442183-lscanrefacceptitem)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCanURLAcceptURL()](https://developer.apple.com/documentation/coreservices/1441854-lscanurlaccepturl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus LSCanURLAcceptURL (     CFURLRef inItemURL,     CFURLRef inTargetURL,     LSRolesMask inRoleMask,     LSAcceptanceFlags inFlags,     Boolean *outAcceptsItem ); ``` |
| To | ``` OSStatus LSCanURLAcceptURL (     CFURLRef _Nonnull inItemURL,     CFURLRef _Nonnull inTargetURL,     LSRolesMask inRoleMask,     LSAcceptanceFlags inFlags,     Boolean * _Nonnull outAcceptsItem ); ``` |

Modified [LSCopyAllHandlersForURLScheme()](https://developer.apple.com/documentation/coreservices/1443240-lscopyallhandlersforurlscheme)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef LSCopyAllHandlersForURLScheme (     CFStringRef inURLScheme ); ``` |
| To | ``` CFArrayRef _Nullable LSCopyAllHandlersForURLScheme (     CFStringRef _Nonnull inURLScheme ); ``` |

Modified [LSCopyAllRoleHandlersForContentType()](https://developer.apple.com/documentation/coreservices/1448020-lscopyallrolehandlersforcontentt)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef LSCopyAllRoleHandlersForContentType (     CFStringRef inContentType,     LSRolesMask inRole ); ``` |
| To | ``` CFArrayRef _Nullable LSCopyAllRoleHandlersForContentType (     CFStringRef _Nonnull inContentType,     LSRolesMask inRole ); ``` |

Modified [LSCopyApplicationForMIMEType()](https://developer.apple.com/documentation/coreservices/1448586-lscopyapplicationformimetype)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyApplicationURLsForBundleIdentifier()](https://developer.apple.com/documentation/coreservices/1449290-lscopyapplicationurlsforbundleid)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef LSCopyApplicationURLsForBundleIdentifier (     CFStringRef inBundleIdentifier,     CFErrorRef *outError ); ``` |
| To | ``` CFArrayRef _Nullable LSCopyApplicationURLsForBundleIdentifier (     CFStringRef _Nonnull inBundleIdentifier,     CFErrorRef  _Nullable * _Nullable outError ); ``` |

Modified [LSCopyApplicationURLsForURL()](https://developer.apple.com/documentation/coreservices/1445148-lscopyapplicationurlsforurl)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef LSCopyApplicationURLsForURL (     CFURLRef inURL,     LSRolesMask inRoleMask ); ``` |
| To | ``` CFArrayRef _Nullable LSCopyApplicationURLsForURL (     CFURLRef _Nonnull inURL,     LSRolesMask inRoleMask ); ``` |

Modified [LSCopyDefaultApplicationURLForContentType()](https://developer.apple.com/documentation/coreservices/1447734-lscopydefaultapplicationurlforco)

|  | Declaration |
| --- | --- |
| From | ``` CFURLRef LSCopyDefaultApplicationURLForContentType (     CFStringRef inContentType,     LSRolesMask inRoleMask,     CFErrorRef *outError ); ``` |
| To | ``` CFURLRef _Nullable LSCopyDefaultApplicationURLForContentType (     CFStringRef _Nonnull inContentType,     LSRolesMask inRoleMask,     CFErrorRef  _Nullable * _Nullable outError ); ``` |

Modified [LSCopyDefaultApplicationURLForURL()](https://developer.apple.com/documentation/coreservices/1448824-lscopydefaultapplicationurlforur)

|  | Declaration |
| --- | --- |
| From | ``` CFURLRef LSCopyDefaultApplicationURLForURL (     CFURLRef inURL,     LSRolesMask inRoleMask,     CFErrorRef *outError ); ``` |
| To | ``` CFURLRef _Nullable LSCopyDefaultApplicationURLForURL (     CFURLRef _Nonnull inURL,     LSRolesMask inRoleMask,     CFErrorRef  _Nullable * _Nullable outError ); ``` |

Modified [LSCopyDefaultHandlerForURLScheme()](https://developer.apple.com/documentation/coreservices/1441725-lscopydefaulthandlerforurlscheme)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef LSCopyDefaultHandlerForURLScheme (     CFStringRef inURLScheme ); ``` |
| To | ``` CFStringRef _Nullable LSCopyDefaultHandlerForURLScheme (     CFStringRef _Nonnull inURLScheme ); ``` |

Modified [LSCopyDefaultRoleHandlerForContentType()](https://developer.apple.com/documentation/coreservices/1449868-lscopydefaultrolehandlerforconte)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef LSCopyDefaultRoleHandlerForContentType (     CFStringRef inContentType,     LSRolesMask inRole ); ``` |
| To | ``` CFStringRef _Nullable LSCopyDefaultRoleHandlerForContentType (     CFStringRef _Nonnull inContentType,     LSRolesMask inRole ); ``` |

Modified [LSCopyDisplayNameForRef()](https://developer.apple.com/documentation/coreservices/1442576-lscopydisplaynameforref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyDisplayNameForURL()](https://developer.apple.com/documentation/coreservices/1446850-lscopydisplaynameforurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyItemAttribute()](https://developer.apple.com/documentation/coreservices/1445023-lscopyitemattribute)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyItemAttributes()](https://developer.apple.com/documentation/coreservices/1446078-lscopyitemattributes)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyItemInfoForRef()](https://developer.apple.com/documentation/coreservices/1445227-lscopyiteminfoforref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyItemInfoForURL()](https://developer.apple.com/documentation/coreservices/1445685-lscopyiteminfoforurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyKindStringForMIMEType()](https://developer.apple.com/documentation/coreservices/1442446-lscopykindstringformimetype)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyKindStringForRef()](https://developer.apple.com/documentation/coreservices/1448593-lscopykindstringforref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyKindStringForTypeInfo()](https://developer.apple.com/documentation/coreservices/1446207-lscopykindstringfortypeinfo)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyKindStringForURL()](https://developer.apple.com/documentation/coreservices/1447481-lscopykindstringforurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSFindApplicationForInfo()](https://developer.apple.com/documentation/coreservices/1449588-lsfindapplicationforinfo)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetApplicationForInfo()](https://developer.apple.com/documentation/coreservices/1449928-lsgetapplicationforinfo)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetApplicationForItem()](https://developer.apple.com/documentation/coreservices/1446185-lsgetapplicationforitem)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetApplicationForURL()](https://developer.apple.com/documentation/coreservices/1445210-lsgetapplicationforurl)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetExtensionInfo()](https://developer.apple.com/documentation/coreservices/1446043-lsgetextensioninfo)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetHandlerOptionsForContentType()](https://developer.apple.com/documentation/coreservices/1445296-lsgethandleroptionsforcontenttyp)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSHandlerOptions](https://developer.apple.com/documentation/coreservices/lshandleroptions)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSItemInfoFlags](https://developer.apple.com/documentation/coreservices/lsiteminfoflags)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSItemInfoRecord](https://developer.apple.com/documentation/coreservices/lsiteminforecord)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified LSKindID

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSRegisterFSRef()](https://developer.apple.com/documentation/coreservices/1444582-lsregisterfsref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSRegisterURL()](https://developer.apple.com/documentation/coreservices/1446350-lsregisterurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus LSRegisterURL (     CFURLRef inURL,     Boolean inUpdate ); ``` |
| To | ``` OSStatus LSRegisterURL (     CFURLRef _Nonnull inURL,     Boolean inUpdate ); ``` |

Modified [LSRequestedInfo](https://developer.apple.com/documentation/coreservices/lsrequestedinfo)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSSetDefaultHandlerForURLScheme()](https://developer.apple.com/documentation/coreservices/1447760-lssetdefaulthandlerforurlscheme)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus LSSetDefaultHandlerForURLScheme (     CFStringRef inURLScheme,     CFStringRef inHandlerBundleID ); ``` |
| To | ``` OSStatus LSSetDefaultHandlerForURLScheme (     CFStringRef _Nonnull inURLScheme,     CFStringRef _Nonnull inHandlerBundleID ); ``` |

Modified [LSSetDefaultRoleHandlerForContentType()](https://developer.apple.com/documentation/coreservices/1444955-lssetdefaultrolehandlerforconten)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus LSSetDefaultRoleHandlerForContentType (     CFStringRef inContentType,     LSRolesMask inRole,     CFStringRef inHandlerBundleID ); ``` |
| To | ``` OSStatus LSSetDefaultRoleHandlerForContentType (     CFStringRef _Nonnull inContentType,     LSRolesMask inRole,     CFStringRef _Nonnull inHandlerBundleID ); ``` |

Modified [LSSetExtensionHiddenForRef()](https://developer.apple.com/documentation/coreservices/1442766-lssetextensionhiddenforref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSSetExtensionHiddenForURL()](https://developer.apple.com/documentation/coreservices/1443948-lssetextensionhiddenforurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSSetHandlerOptionsForContentType()](https://developer.apple.com/documentation/coreservices/1447588-lssethandleroptionsforcontenttyp)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSSetItemAttribute()](https://developer.apple.com/documentation/coreservices/1446733-lssetitemattribute)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

#### LSInfoDeprecated.h (Added)

Modified [kLSHandlerOptionsDefault](https://developer.apple.com/documentation/coreservices/lshandleroptions/klshandleroptionsdefault)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSHandlerOptionsIgnoreCreator](https://developer.apple.com/documentation/coreservices/lshandleroptions/klshandleroptionsignorecreator)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified #def kLSInvalidExtensionIndex

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemContentType](https://developer.apple.com/documentation/coreservices/klsitemcontenttype)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemDisplayKind](https://developer.apple.com/documentation/coreservices/klsitemdisplaykind)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemDisplayName](https://developer.apple.com/documentation/coreservices/klsitemdisplayname)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemExtension](https://developer.apple.com/documentation/coreservices/klsitemextension)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemExtensionIsHidden](https://developer.apple.com/documentation/coreservices/klsitemextensionishidden)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemFileCreator](https://developer.apple.com/documentation/coreservices/klsitemfilecreator)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemFileType](https://developer.apple.com/documentation/coreservices/klsitemfiletype)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoAppIsScriptable](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoappisscriptable)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoAppPrefersClassic](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoappprefersclassic)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoAppPrefersNative](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1446535-appprefersnative)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoExtensionIsHidden](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoextensionishidden)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsAliasFile](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1444478-isaliasfile)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsApplication](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisapplication)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsClassicApp](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1449915-isclassicapp)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsContainer](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoiscontainer)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsInvisible](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1449065-isinvisible)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsNativeApp](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1443624-isnativeapp)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsPackage](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoispackage)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsPlainFile](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/1444223-isplainfile)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsSymlink](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoissymlink)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemInfoIsVolume](https://developer.apple.com/documentation/coreservices/lsiteminfoflags/klsiteminfoisvolume)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemIsInvisible](https://developer.apple.com/documentation/coreservices/klsitemisinvisible)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemQuarantineProperties](https://developer.apple.com/documentation/coreservices/klsitemquarantineproperties)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSItemRoleHandlerDisplayName](https://developer.apple.com/documentation/coreservices/klsitemrolehandlerdisplayname)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestAllFlags](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestallflags)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestAllInfo](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestallinfo)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestAppTypeFlags](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestapptypeflags)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestBasicFlagsOnly](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestbasicflagsonly)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestExtension](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1448601-requestextension)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestExtensionFlagsOnly](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequestextensionflagsonly)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestIconAndKind](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/1447945-requesticonandkind)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [kLSRequestTypeCreator](https://developer.apple.com/documentation/coreservices/lsrequestedinfo/klsrequesttypecreator)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified kLSUnknownKindID

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSCanRefAcceptItem()](https://developer.apple.com/documentation/coreservices/1442183-lscanrefacceptitem)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyApplicationForMIMEType()](https://developer.apple.com/documentation/coreservices/1448586-lscopyapplicationformimetype)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyDisplayNameForRef()](https://developer.apple.com/documentation/coreservices/1442576-lscopydisplaynameforref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyDisplayNameForURL()](https://developer.apple.com/documentation/coreservices/1446850-lscopydisplaynameforurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyItemAttribute()](https://developer.apple.com/documentation/coreservices/1445023-lscopyitemattribute)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyItemAttributes()](https://developer.apple.com/documentation/coreservices/1446078-lscopyitemattributes)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyItemInfoForRef()](https://developer.apple.com/documentation/coreservices/1445227-lscopyiteminfoforref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyItemInfoForURL()](https://developer.apple.com/documentation/coreservices/1445685-lscopyiteminfoforurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyKindStringForMIMEType()](https://developer.apple.com/documentation/coreservices/1442446-lscopykindstringformimetype)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyKindStringForRef()](https://developer.apple.com/documentation/coreservices/1448593-lscopykindstringforref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyKindStringForTypeInfo()](https://developer.apple.com/documentation/coreservices/1446207-lscopykindstringfortypeinfo)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSCopyKindStringForURL()](https://developer.apple.com/documentation/coreservices/1447481-lscopykindstringforurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSFindApplicationForInfo()](https://developer.apple.com/documentation/coreservices/1449588-lsfindapplicationforinfo)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetApplicationForInfo()](https://developer.apple.com/documentation/coreservices/1449928-lsgetapplicationforinfo)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetApplicationForItem()](https://developer.apple.com/documentation/coreservices/1446185-lsgetapplicationforitem)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetApplicationForURL()](https://developer.apple.com/documentation/coreservices/1445210-lsgetapplicationforurl)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetExtensionInfo()](https://developer.apple.com/documentation/coreservices/1446043-lsgetextensioninfo)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSGetHandlerOptionsForContentType()](https://developer.apple.com/documentation/coreservices/1445296-lsgethandleroptionsforcontenttyp)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSHandlerOptions](https://developer.apple.com/documentation/coreservices/lshandleroptions)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSItemInfoFlags](https://developer.apple.com/documentation/coreservices/lsiteminfoflags)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSItemInfoRecord](https://developer.apple.com/documentation/coreservices/lsiteminforecord)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified LSKindID

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSRegisterFSRef()](https://developer.apple.com/documentation/coreservices/1444582-lsregisterfsref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSRequestedInfo](https://developer.apple.com/documentation/coreservices/lsrequestedinfo)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSSetExtensionHiddenForRef()](https://developer.apple.com/documentation/coreservices/1442766-lssetextensionhiddenforref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

Modified [LSSetExtensionHiddenForURL()](https://developer.apple.com/documentation/coreservices/1443948-lssetextensionhiddenforurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSSetHandlerOptionsForContentType()](https://developer.apple.com/documentation/coreservices/1447588-lssethandleroptionsforcontenttyp)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSInfo.h |
| To | OS X 10.11 | LaunchServices/LSInfoDeprecated.h |

Modified [LSSetItemAttribute()](https://developer.apple.com/documentation/coreservices/1446733-lssetitemattribute)

|  | Header |
| --- | --- |
| From | LaunchServices/LSInfo.h |
| To | LaunchServices/LSInfoDeprecated.h |

#### LSOpen.h

Modified [kLSLaunchInClassic](https://developer.apple.com/documentation/coreservices/klslaunchinclassic)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSOpen.h |
| To | OS X 10.11 | LaunchServices/LSOpenDeprecated.h |

Modified [kLSLaunchStartClassic](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchstartclassic)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSOpen.h |
| To | OS X 10.11 | LaunchServices/LSOpenDeprecated.h |

Modified [LSApplicationParameters](https://developer.apple.com/documentation/coreservices/lsapplicationparameters)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSLaunchFSRefSpec](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenApplication()](https://developer.apple.com/documentation/coreservices/1447930-lsopenapplication)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenCFURLRef()](https://developer.apple.com/documentation/coreservices/1442850-lsopencfurlref)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus LSOpenCFURLRef (     CFURLRef inURL,     CFURLRef *outLaunchedURL ); ``` |
| To | ``` OSStatus LSOpenCFURLRef (     CFURLRef _Nonnull inURL,     CFURLRef  _Nullable * _Nullable outLaunchedURL ); ``` |

Modified [LSOpenFromRefSpec()](https://developer.apple.com/documentation/coreservices/1444466-lsopenfromrefspec)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenFromURLSpec()](https://developer.apple.com/documentation/coreservices/1441986-lsopenfromurlspec)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus LSOpenFromURLSpec (     const LSLaunchURLSpec *inLaunchSpec,     CFURLRef *outLaunchedURL ); ``` |
| To | ``` OSStatus LSOpenFromURLSpec (     const LSLaunchURLSpec * _Nonnull inLaunchSpec,     CFURLRef  _Nullable * _Nullable outLaunchedURL ); ``` |

Modified [LSOpenFSRef()](https://developer.apple.com/documentation/coreservices/1445663-lsopenfsref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenItemsWithRole()](https://developer.apple.com/documentation/coreservices/1449783-lsopenitemswithrole)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenURLsWithRole()](https://developer.apple.com/documentation/coreservices/1448184-lsopenurlswithrole)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

#### LSOpenDeprecated.h (Added)

Modified [kLSLaunchInClassic](https://developer.apple.com/documentation/coreservices/klslaunchinclassic)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSOpen.h |
| To | OS X 10.11 | LaunchServices/LSOpenDeprecated.h |

Modified [kLSLaunchStartClassic](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchstartclassic)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSOpen.h |
| To | OS X 10.11 | LaunchServices/LSOpenDeprecated.h |

Modified [LSApplicationParameters](https://developer.apple.com/documentation/coreservices/lsapplicationparameters)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSLaunchFSRefSpec](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenApplication()](https://developer.apple.com/documentation/coreservices/1447930-lsopenapplication)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenFromRefSpec()](https://developer.apple.com/documentation/coreservices/1444466-lsopenfromrefspec)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenFSRef()](https://developer.apple.com/documentation/coreservices/1445663-lsopenfsref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenItemsWithRole()](https://developer.apple.com/documentation/coreservices/1449783-lsopenitemswithrole)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

Modified [LSOpenURLsWithRole()](https://developer.apple.com/documentation/coreservices/1448184-lsopenurlswithrole)

|  | Header |
| --- | --- |
| From | LaunchServices/LSOpen.h |
| To | LaunchServices/LSOpenDeprecated.h |

#### LSSharedFileList.h (Added)

Modified [kLSSharedFileListDoNotMountVolumes](https://developer.apple.com/documentation/coreservices/klssharedfilelistdonotmountvolumes)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListFavoriteItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistfavoriteitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListFavoriteVolumes](https://developer.apple.com/documentation/coreservices/klssharedfilelistfavoritevolumes)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListGlobalLoginItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistgloballoginitems)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListItemBeforeFirst](https://developer.apple.com/documentation/coreservices/klssharedfilelistitembeforefirst)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListItemHidden](https://developer.apple.com/documentation/coreservices/klssharedfilelistitemhidden)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListItemLast](https://developer.apple.com/documentation/coreservices/klssharedfilelistitemlast)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListLoginItemHidden](https://developer.apple.com/documentation/coreservices/klssharedfilelistloginitemhidden)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListNoUserInteraction](https://developer.apple.com/documentation/coreservices/1581401-anonymous/klssharedfilelistnouserinteraction)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListRecentApplicationItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentapplicationitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListRecentDocumentItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentdocumentitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListRecentItemsMaxAmount](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentitemsmaxamount)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListRecentServerItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentserveritems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListSessionLoginItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistsessionloginitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListVolumesComputerVisible](https://developer.apple.com/documentation/coreservices/klssharedfilelistvolumescomputervisible)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListVolumesIDiskVisible](https://developer.apple.com/documentation/coreservices/klssharedfilelistvolumesidiskvisible)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListVolumesNetworkVisible](https://developer.apple.com/documentation/coreservices/klssharedfilelistvolumesnetworkvisible)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListAddObserver()](https://developer.apple.com/documentation/coreservices/1445770-lssharedfilelistaddobserver)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListChangedProcPtr](https://developer.apple.com/documentation/coreservices/lssharedfilelistchangedprocptr)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListCopyProperty()](https://developer.apple.com/documentation/coreservices/1444588-lssharedfilelistcopyproperty)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListCopySnapshot()](https://developer.apple.com/documentation/coreservices/1448112-lssharedfilelistcopysnapshot)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListCreate()](https://developer.apple.com/documentation/coreservices/1443926-lssharedfilelistcreate)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListGetSeedValue()](https://developer.apple.com/documentation/coreservices/1444885-lssharedfilelistgetseedvalue)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListGetTypeID()](https://developer.apple.com/documentation/coreservices/1450618-lssharedfilelistgettypeid)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListInsertItemFSRef()](https://developer.apple.com/documentation/coreservices/1449884-lssharedfilelistinsertitemfsref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListInsertItemURL()](https://developer.apple.com/documentation/coreservices/1444471-lssharedfilelistinsertitemurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemCopyDisplayName()](https://developer.apple.com/documentation/coreservices/1449716-lssharedfilelistitemcopydisplayn)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemCopyIconRef()](https://developer.apple.com/documentation/coreservices/1442889-lssharedfilelistitemcopyiconref)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemCopyProperty()](https://developer.apple.com/documentation/coreservices/1445074-lssharedfilelistitemcopyproperty)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemCopyResolvedURL()](https://developer.apple.com/documentation/coreservices/1449882-lssharedfilelistitemcopyresolved)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemGetID()](https://developer.apple.com/documentation/coreservices/1443305-lssharedfilelistitemgetid)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemGetTypeID()](https://developer.apple.com/documentation/coreservices/1447138-lssharedfilelistitemgettypeid)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemMove()](https://developer.apple.com/documentation/coreservices/1444348-lssharedfilelistitemmove)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemRef](https://developer.apple.com/documentation/coreservices/lssharedfilelistitemref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemRemove()](https://developer.apple.com/documentation/coreservices/1442025-lssharedfilelistitemremove)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemResolve()](https://developer.apple.com/documentation/coreservices/1447347-lssharedfilelistitemresolve)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemSetProperty()](https://developer.apple.com/documentation/coreservices/1445766-lssharedfilelistitemsetproperty)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListRef](https://developer.apple.com/documentation/coreservices/lssharedfilelistref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListRemoveAllItems()](https://developer.apple.com/documentation/coreservices/1446389-lssharedfilelistremoveallitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListRemoveObserver()](https://developer.apple.com/documentation/coreservices/1443404-lssharedfilelistremoveobserver)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListResolutionFlags](https://developer.apple.com/documentation/coreservices/lssharedfilelistresolutionflags)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListSetAuthorization()](https://developer.apple.com/documentation/coreservices/1446834-lssharedfilelistsetauthorization)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListSetProperty()](https://developer.apple.com/documentation/coreservices/1448857-lssharedfilelistsetproperty)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

#### LSSharedFileList.h (Removed)

Modified [kLSSharedFileListDoNotMountVolumes](https://developer.apple.com/documentation/coreservices/klssharedfilelistdonotmountvolumes)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListFavoriteItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistfavoriteitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListFavoriteVolumes](https://developer.apple.com/documentation/coreservices/klssharedfilelistfavoritevolumes)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListGlobalLoginItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistgloballoginitems)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListItemBeforeFirst](https://developer.apple.com/documentation/coreservices/klssharedfilelistitembeforefirst)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListItemHidden](https://developer.apple.com/documentation/coreservices/klssharedfilelistitemhidden)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListItemLast](https://developer.apple.com/documentation/coreservices/klssharedfilelistitemlast)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListLoginItemHidden](https://developer.apple.com/documentation/coreservices/klssharedfilelistloginitemhidden)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListNoUserInteraction](https://developer.apple.com/documentation/coreservices/1581401-anonymous/klssharedfilelistnouserinteraction)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListRecentApplicationItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentapplicationitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListRecentDocumentItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentdocumentitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListRecentItemsMaxAmount](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentitemsmaxamount)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListRecentServerItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistrecentserveritems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListSessionLoginItems](https://developer.apple.com/documentation/coreservices/klssharedfilelistsessionloginitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListVolumesComputerVisible](https://developer.apple.com/documentation/coreservices/klssharedfilelistvolumescomputervisible)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListVolumesIDiskVisible](https://developer.apple.com/documentation/coreservices/klssharedfilelistvolumesidiskvisible)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [kLSSharedFileListVolumesNetworkVisible](https://developer.apple.com/documentation/coreservices/klssharedfilelistvolumesnetworkvisible)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListAddObserver()](https://developer.apple.com/documentation/coreservices/1445770-lssharedfilelistaddobserver)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListChangedProcPtr](https://developer.apple.com/documentation/coreservices/lssharedfilelistchangedprocptr)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListCopyProperty()](https://developer.apple.com/documentation/coreservices/1444588-lssharedfilelistcopyproperty)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListCopySnapshot()](https://developer.apple.com/documentation/coreservices/1448112-lssharedfilelistcopysnapshot)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListCreate()](https://developer.apple.com/documentation/coreservices/1443926-lssharedfilelistcreate)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListGetSeedValue()](https://developer.apple.com/documentation/coreservices/1444885-lssharedfilelistgetseedvalue)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListGetTypeID()](https://developer.apple.com/documentation/coreservices/1450618-lssharedfilelistgettypeid)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListInsertItemFSRef()](https://developer.apple.com/documentation/coreservices/1449884-lssharedfilelistinsertitemfsref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListInsertItemURL()](https://developer.apple.com/documentation/coreservices/1444471-lssharedfilelistinsertitemurl)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemCopyDisplayName()](https://developer.apple.com/documentation/coreservices/1449716-lssharedfilelistitemcopydisplayn)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemCopyIconRef()](https://developer.apple.com/documentation/coreservices/1442889-lssharedfilelistitemcopyiconref)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemCopyProperty()](https://developer.apple.com/documentation/coreservices/1445074-lssharedfilelistitemcopyproperty)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemCopyResolvedURL()](https://developer.apple.com/documentation/coreservices/1449882-lssharedfilelistitemcopyresolved)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemGetID()](https://developer.apple.com/documentation/coreservices/1443305-lssharedfilelistitemgetid)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemGetTypeID()](https://developer.apple.com/documentation/coreservices/1447138-lssharedfilelistitemgettypeid)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemMove()](https://developer.apple.com/documentation/coreservices/1444348-lssharedfilelistitemmove)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemRef](https://developer.apple.com/documentation/coreservices/lssharedfilelistitemref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemRemove()](https://developer.apple.com/documentation/coreservices/1442025-lssharedfilelistitemremove)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemResolve()](https://developer.apple.com/documentation/coreservices/1447347-lssharedfilelistitemresolve)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListItemSetProperty()](https://developer.apple.com/documentation/coreservices/1445766-lssharedfilelistitemsetproperty)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListRef](https://developer.apple.com/documentation/coreservices/lssharedfilelistref)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListRemoveAllItems()](https://developer.apple.com/documentation/coreservices/1446389-lssharedfilelistremoveallitems)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListRemoveObserver()](https://developer.apple.com/documentation/coreservices/1443404-lssharedfilelistremoveobserver)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListResolutionFlags](https://developer.apple.com/documentation/coreservices/lssharedfilelistresolutionflags)

|  | Header |
| --- | --- |
| From | LaunchServices/LSSharedFileList.h |
| To | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListSetAuthorization()](https://developer.apple.com/documentation/coreservices/1446834-lssharedfilelistsetauthorization)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

Modified [LSSharedFileListSetProperty()](https://developer.apple.com/documentation/coreservices/1448857-lssharedfilelistsetproperty)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | LaunchServices/LSSharedFileList.h |
| To | OS X 10.11 | SharedFileList/LSSharedFileList.h |

#### MDItem.h

Added [kMDItemHTMLContent](https://developer.apple.com/documentation/coreservices/kmditemhtmlcontent)

#### SystemSound.h (Removed)

Removed AlertSoundPlay()Removed AlertSoundPlayCustomSound()Removed DisposeSystemSoundCompletionUPP()Removed #def DisposeSystemSoundCompletionUPPRemoved InvokeSystemSoundCompletionUPP()Removed #def InvokeSystemSoundCompletionUPPRemoved kSystemSoundClientTimedOutErrorRemoved kSystemSoundNoErrorRemoved kSystemSoundUnspecifiedErrorRemoved NewSystemSoundCompletionUPP()Removed #def NewSystemSoundCompletionUPPRemoved SystemSoundActionIDRemoved SystemSoundCompletionProcPtrRemoved SystemSoundCompletionUPPRemoved SystemSoundGetActionID()Removed SystemSoundPlay()Removed SystemSoundRemoveActionID()Removed SystemSoundRemoveCompletionRoutine()Removed SystemSoundSetCompletionRoutine()

#### TextCommon.h

Added [kTextEncodingUnicodeV7_0](https://developer.apple.com/documentation/coreservices/1400188-unicode_and_iso_ucs_text_encodin/ktextencodingunicodev7_0)

#### UTCoreTypes.h

Added [kUTTypeSwiftSource](https://developer.apple.com/documentation/coreservices/kuttypeswiftsource)

#### UTType.h

Modified [UTCreateStringForOSType()](https://developer.apple.com/documentation/coreservices/1442804-utcreatestringforostype)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef UTCreateStringForOSType (     OSType inOSType ); ``` |
| To | ``` CFStringRef _Nonnull UTCreateStringForOSType (     OSType inOSType ); ``` |

Modified [UTGetOSTypeFromString()](https://developer.apple.com/documentation/coreservices/1450472-utgetostypefromstring)

|  | Declaration |
| --- | --- |
| From | ``` OSType UTGetOSTypeFromString (     CFStringRef inString ); ``` |
| To | ``` OSType UTGetOSTypeFromString (     CFStringRef _Nonnull inString ); ``` |

Modified [UTTypeConformsTo()](https://developer.apple.com/documentation/coreservices/1444079-uttypeconformsto)

|  | Declaration |
| --- | --- |
| From | ``` Boolean UTTypeConformsTo (     CFStringRef inUTI,     CFStringRef inConformsToUTI ); ``` |
| To | ``` Boolean UTTypeConformsTo (     CFStringRef _Nonnull inUTI,     CFStringRef _Nonnull inConformsToUTI ); ``` |

Modified [UTTypeCopyAllTagsWithClass()](https://developer.apple.com/documentation/coreservices/1448473-uttypecopyalltagswithclass)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef UTTypeCopyAllTagsWithClass (     CFStringRef inUTI,     CFStringRef inTagClass ); ``` |
| To | ``` CFArrayRef _Nullable UTTypeCopyAllTagsWithClass (     CFStringRef _Nonnull inUTI,     CFStringRef _Nonnull inTagClass ); ``` |

Modified [UTTypeCopyDeclaration()](https://developer.apple.com/documentation/coreservices/1442505-uttypecopydeclaration)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef UTTypeCopyDeclaration (     CFStringRef inUTI ); ``` |
| To | ``` CFDictionaryRef _Nullable UTTypeCopyDeclaration (     CFStringRef _Nonnull inUTI ); ``` |

Modified [UTTypeCopyDeclaringBundleURL()](https://developer.apple.com/documentation/coreservices/1447781-uttypecopydeclaringbundleurl)

|  | Declaration |
| --- | --- |
| From | ``` CFURLRef UTTypeCopyDeclaringBundleURL (     CFStringRef inUTI ); ``` |
| To | ``` CFURLRef _Nullable UTTypeCopyDeclaringBundleURL (     CFStringRef _Nonnull inUTI ); ``` |

Modified [UTTypeCopyDescription()](https://developer.apple.com/documentation/coreservices/1448514-uttypecopydescription)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef UTTypeCopyDescription (     CFStringRef inUTI ); ``` |
| To | ``` CFStringRef _Nullable UTTypeCopyDescription (     CFStringRef _Nonnull inUTI ); ``` |

Modified [UTTypeCopyPreferredTagWithClass()](https://developer.apple.com/documentation/coreservices/1442744-uttypecopypreferredtagwithclass)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef UTTypeCopyPreferredTagWithClass (     CFStringRef inUTI,     CFStringRef inTagClass ); ``` |
| To | ``` CFStringRef _Nullable UTTypeCopyPreferredTagWithClass (     CFStringRef _Nonnull inUTI,     CFStringRef _Nonnull inTagClass ); ``` |

Modified [UTTypeCreateAllIdentifiersForTag()](https://developer.apple.com/documentation/coreservices/1447261-uttypecreateallidentifiersfortag)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef UTTypeCreateAllIdentifiersForTag (     CFStringRef inTagClass,     CFStringRef inTag,     CFStringRef inConformingToUTI ); ``` |
| To | ``` CFArrayRef _Nullable UTTypeCreateAllIdentifiersForTag (     CFStringRef _Nonnull inTagClass,     CFStringRef _Nonnull inTag,     CFStringRef _Nullable inConformingToUTI ); ``` |

Modified [UTTypeCreatePreferredIdentifierForTag()](https://developer.apple.com/documentation/coreservices/1448939-uttypecreatepreferredidentifierf)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef UTTypeCreatePreferredIdentifierForTag (     CFStringRef inTagClass,     CFStringRef inTag,     CFStringRef inConformingToUTI ); ``` |
| To | ``` CFStringRef _Nullable UTTypeCreatePreferredIdentifierForTag (     CFStringRef _Nonnull inTagClass,     CFStringRef _Nonnull inTag,     CFStringRef _Nullable inConformingToUTI ); ``` |

Modified [UTTypeEqual()](https://developer.apple.com/documentation/coreservices/1447783-uttypeequal)

|  | Declaration |
| --- | --- |
| From | ``` Boolean UTTypeEqual (     CFStringRef inUTI1,     CFStringRef inUTI2 ); ``` |
| To | ``` Boolean UTTypeEqual (     CFStringRef _Nonnull inUTI1,     CFStringRef _Nonnull inUTI2 ); ``` |

Modified [UTTypeIsDeclared()](https://developer.apple.com/documentation/coreservices/1450352-uttypeisdeclared)

|  | Declaration |
| --- | --- |
| From | ``` Boolean UTTypeIsDeclared (     CFStringRef inUTI ); ``` |
| To | ``` Boolean UTTypeIsDeclared (     CFStringRef _Nonnull inUTI ); ``` |

Modified [UTTypeIsDynamic()](https://developer.apple.com/documentation/coreservices/1442980-uttypeisdynamic)

|  | Declaration |
| --- | --- |
| From | ``` Boolean UTTypeIsDynamic (     CFStringRef inUTI ); ``` |
| To | ``` Boolean UTTypeIsDynamic (     CFStringRef _Nonnull inUTI ); ``` |

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

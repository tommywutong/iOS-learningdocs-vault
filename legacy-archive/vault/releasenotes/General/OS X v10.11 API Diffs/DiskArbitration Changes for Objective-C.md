---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/DiskArbitration.html
archived_at: '2026-07-18T02:53:01.888162Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# DiskArbitration Changes for Objective-C

### DiskArbitration

#### DADisk.h

Added [kDADiskDescriptionVolumeTypeKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionvolumetypekey)Modified [DADiskCopyDescription()](https://developer.apple.com/documentation/diskarbitration/1401854-dadiskcopydescription)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef DADiskCopyDescription (     DADiskRef disk ); ``` |
| To | ``` CFDictionaryRef _Nullable DADiskCopyDescription (     DADiskRef _Nonnull disk ); ``` |

Modified [DADiskCopyIOMedia()](https://developer.apple.com/documentation/diskarbitration/1401888-dadiskcopyiomedia)

|  | Declaration |
| --- | --- |
| From | ``` io_service_t DADiskCopyIOMedia (     DADiskRef disk ); ``` |
| To | ``` io_service_t DADiskCopyIOMedia (     DADiskRef _Nonnull disk ); ``` |

Modified [DADiskCopyWholeDisk()](https://developer.apple.com/documentation/diskarbitration/1401828-dadiskcopywholedisk)

|  | Declaration |
| --- | --- |
| From | ``` DADiskRef DADiskCopyWholeDisk (     DADiskRef disk ); ``` |
| To | ``` DADiskRef _Nullable DADiskCopyWholeDisk (     DADiskRef _Nonnull disk ); ``` |

Modified [DADiskCreateFromBSDName()](https://developer.apple.com/documentation/diskarbitration/1401870-dadiskcreatefrombsdname)

|  | Declaration |
| --- | --- |
| From | ``` DADiskRef DADiskCreateFromBSDName (     CFAllocatorRef allocator,     DASessionRef session,     const char *name ); ``` |
| To | ``` DADiskRef _Nullable DADiskCreateFromBSDName (     CFAllocatorRef _Nullable allocator,     DASessionRef _Nonnull session,     const char * _Nonnull name ); ``` |

Modified [DADiskCreateFromIOMedia()](https://developer.apple.com/documentation/diskarbitration/1401862-dadiskcreatefromiomedia)

|  | Declaration |
| --- | --- |
| From | ``` DADiskRef DADiskCreateFromIOMedia (     CFAllocatorRef allocator,     DASessionRef session,     io_service_t media ); ``` |
| To | ``` DADiskRef _Nullable DADiskCreateFromIOMedia (     CFAllocatorRef _Nullable allocator,     DASessionRef _Nonnull session,     io_service_t media ); ``` |

Modified [DADiskCreateFromVolumePath()](https://developer.apple.com/documentation/diskarbitration/1401858-dadiskcreatefromvolumepath)

|  | Declaration |
| --- | --- |
| From | ``` DADiskRef DADiskCreateFromVolumePath (     CFAllocatorRef allocator,     DASessionRef session,     CFURLRef path ); ``` |
| To | ``` DADiskRef _Nullable DADiskCreateFromVolumePath (     CFAllocatorRef _Nullable allocator,     DASessionRef _Nonnull session,     CFURLRef _Nonnull path ); ``` |

Modified [DADiskGetBSDName()](https://developer.apple.com/documentation/diskarbitration/1401880-dadiskgetbsdname)

|  | Declaration |
| --- | --- |
| From | ``` const char * DADiskGetBSDName (     DADiskRef disk ); ``` |
| To | ``` const char * _Nullable DADiskGetBSDName (     DADiskRef _Nonnull disk ); ``` |

#### DADissenter.h

Modified [DADissenterCreate()](https://developer.apple.com/documentation/diskarbitration/1501551-dadissentercreate)

|  | Declaration |
| --- | --- |
| From | ``` DADissenterRef DADissenterCreate (     CFAllocatorRef allocator,     DAReturn status,     CFStringRef string ); ``` |
| To | ``` DADissenterRef _Nonnull DADissenterCreate (     CFAllocatorRef _Nullable allocator,     DAReturn status,     CFStringRef _Nullable string ); ``` |

Modified [DADissenterGetStatus()](https://developer.apple.com/documentation/diskarbitration/1501539-dadissentergetstatus)

|  | Declaration |
| --- | --- |
| From | ``` DAReturn DADissenterGetStatus (     DADissenterRef dissenter ); ``` |
| To | ``` DAReturn DADissenterGetStatus (     DADissenterRef _Nonnull dissenter ); ``` |

Modified [DADissenterGetStatusString()](https://developer.apple.com/documentation/diskarbitration/1501531-dadissentergetstatusstring)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef DADissenterGetStatusString (     DADissenterRef dissenter ); ``` |
| To | ``` CFStringRef _Nullable DADissenterGetStatusString (     DADissenterRef _Nonnull dissenter ); ``` |

#### DASession.h

Modified [DAApprovalSessionCreate()](https://developer.apple.com/documentation/diskarbitration/1515337-daapprovalsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` DAApprovalSessionRef DAApprovalSessionCreate (     CFAllocatorRef allocator ); ``` |
| To | ``` DAApprovalSessionRef _Nullable DAApprovalSessionCreate (     CFAllocatorRef _Nullable allocator ); ``` |

Modified [DAApprovalSessionScheduleWithRunLoop()](https://developer.apple.com/documentation/diskarbitration/1515338-daapprovalsessionschedulewithrun)

|  | Declaration |
| --- | --- |
| From | ``` void DAApprovalSessionScheduleWithRunLoop (     DAApprovalSessionRef session,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void DAApprovalSessionScheduleWithRunLoop (     DAApprovalSessionRef _Nonnull session,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [DAApprovalSessionUnscheduleFromRunLoop()](https://developer.apple.com/documentation/diskarbitration/1515340-daapprovalsessionunschedulefromr)

|  | Declaration |
| --- | --- |
| From | ``` void DAApprovalSessionUnscheduleFromRunLoop (     DAApprovalSessionRef session,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void DAApprovalSessionUnscheduleFromRunLoop (     DAApprovalSessionRef _Nonnull session,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [DASessionCreate()](https://developer.apple.com/documentation/diskarbitration/1501530-dasessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` DASessionRef DASessionCreate (     CFAllocatorRef allocator ); ``` |
| To | ``` DASessionRef _Nullable DASessionCreate (     CFAllocatorRef _Nullable allocator ); ``` |

Modified [DASessionScheduleWithRunLoop()](https://developer.apple.com/documentation/diskarbitration/1501544-dasessionschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` void DASessionScheduleWithRunLoop (     DASessionRef session,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void DASessionScheduleWithRunLoop (     DASessionRef _Nonnull session,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [DASessionSetDispatchQueue()](https://developer.apple.com/documentation/diskarbitration/1501542-dasessionsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` void DASessionSetDispatchQueue (     DASessionRef session,     dispatch_queue_t queue ); ``` |
| To | ``` void DASessionSetDispatchQueue (     DASessionRef _Nonnull session,     dispatch_queue_t _Nullable queue ); ``` |

Modified [DASessionUnscheduleFromRunLoop()](https://developer.apple.com/documentation/diskarbitration/1501550-dasessionunschedulefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` void DASessionUnscheduleFromRunLoop (     DASessionRef session,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void DASessionUnscheduleFromRunLoop (     DASessionRef _Nonnull session,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

#### DiskArbitration.h

Removed [kDADiskOptionEjectUponLogout](https://developer.apple.com/documentation/diskarbitration/diskarbitration.h/dadiskoptions/kdadiskoptionejectuponlogout)Removed [kDADiskOptionMountAutomatic](https://developer.apple.com/documentation/diskarbitration/diskarbitration.h/dadiskoptions/kdadiskoptionmountautomatic)Removed [kDADiskOptionMountAutomaticNoDefer](https://developer.apple.com/documentation/diskarbitration/diskarbitration.h/dadiskoptions/kdadiskoptionmountautomaticnodefer)Removed [kDADiskOptionPrivate](https://developer.apple.com/documentation/diskarbitration/diskarbitration.h/dadiskoptions/kdadiskoptionprivate)Modified [DADiskClaim()](https://developer.apple.com/documentation/diskarbitration/1492694-dadiskclaim)

|  | Declaration |
| --- | --- |
| From | ``` void DADiskClaim (     DADiskRef disk,     DADiskClaimOptions options,     DADiskClaimReleaseCallback release,     void *releaseContext,     DADiskClaimCallback callback,     void *callbackContext ); ``` |
| To | ``` void DADiskClaim (     DADiskRef _Nonnull disk,     DADiskClaimOptions options,     DADiskClaimReleaseCallback _Nullable release,     void * _Nullable releaseContext,     DADiskClaimCallback _Nullable callback,     void * _Nullable callbackContext ); ``` |

Modified [DADiskEject()](https://developer.apple.com/documentation/diskarbitration/1492701-dadiskeject)

|  | Declaration |
| --- | --- |
| From | ``` void DADiskEject (     DADiskRef disk,     DADiskEjectOptions options,     DADiskEjectCallback callback,     void *context ); ``` |
| To | ``` void DADiskEject (     DADiskRef _Nonnull disk,     DADiskEjectOptions options,     DADiskEjectCallback _Nullable callback,     void * _Nullable context ); ``` |

Modified [DADiskGetOptions()](https://developer.apple.com/documentation/diskarbitration/1492711-dadiskgetoptions)

|  | Declaration |
| --- | --- |
| From | ``` DADiskOptions DADiskGetOptions (     DADiskRef disk ); ``` |
| To | ``` DADiskOptions DADiskGetOptions (     DADiskRef _Nonnull disk ); ``` |

Modified [DADiskIsClaimed()](https://developer.apple.com/documentation/diskarbitration/1492734-dadiskisclaimed)

|  | Declaration |
| --- | --- |
| From | ``` Boolean DADiskIsClaimed (     DADiskRef disk ); ``` |
| To | ``` Boolean DADiskIsClaimed (     DADiskRef _Nonnull disk ); ``` |

Modified [DADiskMount()](https://developer.apple.com/documentation/diskarbitration/1492772-dadiskmount)

|  | Declaration |
| --- | --- |
| From | ``` void DADiskMount (     DADiskRef disk,     CFURLRef path,     DADiskMountOptions options,     DADiskMountCallback callback,     void *context ); ``` |
| To | ``` void DADiskMount (     DADiskRef _Nonnull disk,     CFURLRef _Nullable path,     DADiskMountOptions options,     DADiskMountCallback _Nullable callback,     void * _Nullable context ); ``` |

Modified [DADiskMountWithArguments()](https://developer.apple.com/documentation/diskarbitration/1492714-dadiskmountwitharguments)

|  | Declaration |
| --- | --- |
| From | ``` void DADiskMountWithArguments (     DADiskRef disk,     CFURLRef path,     DADiskMountOptions options,     DADiskMountCallback callback,     void *context,     CFStringRef arguments[] ); ``` |
| To | ``` void DADiskMountWithArguments (     DADiskRef _Nonnull disk,     CFURLRef _Nullable path,     DADiskMountOptions options,     DADiskMountCallback _Nullable callback,     void * _Nullable context,     CFStringRef  _Nonnull arguments[] ); ``` |

Modified [DADiskRename()](https://developer.apple.com/documentation/diskarbitration/1492760-dadiskrename)

|  | Declaration |
| --- | --- |
| From | ``` void DADiskRename (     DADiskRef disk,     CFStringRef name,     DADiskRenameOptions options,     DADiskRenameCallback callback,     void *context ); ``` |
| To | ``` void DADiskRename (     DADiskRef _Nonnull disk,     CFStringRef _Nonnull name,     DADiskRenameOptions options,     DADiskRenameCallback _Nullable callback,     void * _Nullable context ); ``` |

Modified [DADiskSetOptions()](https://developer.apple.com/documentation/diskarbitration/1492759-dadisksetoptions)

|  | Declaration |
| --- | --- |
| From | ``` DAReturn DADiskSetOptions (     DADiskRef disk,     DADiskOptions options,     Boolean value ); ``` |
| To | ``` DAReturn DADiskSetOptions (     DADiskRef _Nonnull disk,     DADiskOptions options,     Boolean value ); ``` |

Modified [DADiskUnclaim()](https://developer.apple.com/documentation/diskarbitration/1492726-dadiskunclaim)

|  | Declaration |
| --- | --- |
| From | ``` void DADiskUnclaim (     DADiskRef disk ); ``` |
| To | ``` void DADiskUnclaim (     DADiskRef _Nonnull disk ); ``` |

Modified [DADiskUnmount()](https://developer.apple.com/documentation/diskarbitration/1492758-dadiskunmount)

|  | Declaration |
| --- | --- |
| From | ``` void DADiskUnmount (     DADiskRef disk,     DADiskUnmountOptions options,     DADiskUnmountCallback callback,     void *context ); ``` |
| To | ``` void DADiskUnmount (     DADiskRef _Nonnull disk,     DADiskUnmountOptions options,     DADiskUnmountCallback _Nullable callback,     void * _Nullable context ); ``` |

Modified [DARegisterDiskAppearedCallback()](https://developer.apple.com/documentation/diskarbitration/1492707-daregisterdiskappearedcallback)

|  | Declaration |
| --- | --- |
| From | ``` void DARegisterDiskAppearedCallback (     DASessionRef session,     CFDictionaryRef match,     DADiskAppearedCallback callback,     void *context ); ``` |
| To | ``` void DARegisterDiskAppearedCallback (     DASessionRef _Nonnull session,     CFDictionaryRef _Nullable match,     DADiskAppearedCallback _Nonnull callback,     void * _Nullable context ); ``` |

Modified [DARegisterDiskDescriptionChangedCallback()](https://developer.apple.com/documentation/diskarbitration/1492705-daregisterdiskdescriptionchanged)

|  | Declaration |
| --- | --- |
| From | ``` void DARegisterDiskDescriptionChangedCallback (     DASessionRef session,     CFDictionaryRef match,     CFArrayRef watch,     DADiskDescriptionChangedCallback callback,     void *context ); ``` |
| To | ``` void DARegisterDiskDescriptionChangedCallback (     DASessionRef _Nonnull session,     CFDictionaryRef _Nullable match,     CFArrayRef _Nullable watch,     DADiskDescriptionChangedCallback _Nonnull callback,     void * _Nullable context ); ``` |

Modified [DARegisterDiskDisappearedCallback()](https://developer.apple.com/documentation/diskarbitration/1492696-daregisterdiskdisappearedcallbac)

|  | Declaration |
| --- | --- |
| From | ``` void DARegisterDiskDisappearedCallback (     DASessionRef session,     CFDictionaryRef match,     DADiskDisappearedCallback callback,     void *context ); ``` |
| To | ``` void DARegisterDiskDisappearedCallback (     DASessionRef _Nonnull session,     CFDictionaryRef _Nullable match,     DADiskDisappearedCallback _Nonnull callback,     void * _Nullable context ); ``` |

Modified [DARegisterDiskEjectApprovalCallback()](https://developer.apple.com/documentation/diskarbitration/1492715-daregisterdiskejectapprovalcallb)

|  | Declaration |
| --- | --- |
| From | ``` void DARegisterDiskEjectApprovalCallback (     DASessionRef session,     CFDictionaryRef match,     DADiskEjectApprovalCallback callback,     void *context ); ``` |
| To | ``` void DARegisterDiskEjectApprovalCallback (     DASessionRef _Nonnull session,     CFDictionaryRef _Nullable match,     DADiskEjectApprovalCallback _Nonnull callback,     void * _Nullable context ); ``` |

Modified [DARegisterDiskMountApprovalCallback()](https://developer.apple.com/documentation/diskarbitration/1492762-daregisterdiskmountapprovalcallb)

|  | Declaration |
| --- | --- |
| From | ``` void DARegisterDiskMountApprovalCallback (     DASessionRef session,     CFDictionaryRef match,     DADiskMountApprovalCallback callback,     void *context ); ``` |
| To | ``` void DARegisterDiskMountApprovalCallback (     DASessionRef _Nonnull session,     CFDictionaryRef _Nullable match,     DADiskMountApprovalCallback _Nonnull callback,     void * _Nullable context ); ``` |

Modified [DARegisterDiskPeekCallback()](https://developer.apple.com/documentation/diskarbitration/1492728-daregisterdiskpeekcallback)

|  | Declaration |
| --- | --- |
| From | ``` void DARegisterDiskPeekCallback (     DASessionRef session,     CFDictionaryRef match,     CFIndex order,     DADiskPeekCallback callback,     void *context ); ``` |
| To | ``` void DARegisterDiskPeekCallback (     DASessionRef _Nonnull session,     CFDictionaryRef _Nullable match,     CFIndex order,     DADiskPeekCallback _Nonnull callback,     void * _Nullable context ); ``` |

Modified [DARegisterDiskUnmountApprovalCallback()](https://developer.apple.com/documentation/diskarbitration/1492698-daregisterdiskunmountapprovalcal)

|  | Declaration |
| --- | --- |
| From | ``` void DARegisterDiskUnmountApprovalCallback (     DASessionRef session,     CFDictionaryRef match,     DADiskUnmountApprovalCallback callback,     void *context ); ``` |
| To | ``` void DARegisterDiskUnmountApprovalCallback (     DASessionRef _Nonnull session,     CFDictionaryRef _Nullable match,     DADiskUnmountApprovalCallback _Nonnull callback,     void * _Nullable context ); ``` |

Modified [DAUnregisterApprovalCallback()](https://developer.apple.com/documentation/diskarbitration/1492750-daunregisterapprovalcallback)

|  | Declaration |
| --- | --- |
| From | ``` void DAUnregisterApprovalCallback (     DASessionRef session,     void *callback,     void *context ); ``` |
| To | ``` void DAUnregisterApprovalCallback (     DASessionRef _Nonnull session,     void * _Nonnull callback,     void * _Nullable context ); ``` |

Modified [DAUnregisterCallback()](https://developer.apple.com/documentation/diskarbitration/1492712-daunregistercallback)

|  | Declaration |
| --- | --- |
| From | ``` void DAUnregisterCallback (     DASessionRef session,     void *callback,     void *context ); ``` |
| To | ``` void DAUnregisterCallback (     DASessionRef _Nonnull session,     void * _Nonnull callback,     void * _Nullable context ); ``` |

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

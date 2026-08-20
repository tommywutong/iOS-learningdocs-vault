---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/DiskArbitration.html
archived_at: '2026-07-18T02:53:31.602457Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# DiskArbitration Changes for Swift

### DiskArbitration

Removed DAApprovalSessionCreate(_: CFAllocator!) -> Unmanaged<DAApprovalSession>!Removed DAApprovalSessionGetTypeID() -> CFTypeIDRemoved DAApprovalSessionRefRemoved DAApprovalSessionScheduleWithRunLoop(_: DAApprovalSession!, _: CFRunLoop!, _: CFString!)Removed DAApprovalSessionUnscheduleFromRunLoop(_: DAApprovalSession!, _: CFRunLoop!, _: CFString!)Removed DAUnregisterApprovalCallback(_: DASession!, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<Void>)Added [kDADiskDescriptionVolumeTypeKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionvolumetypekey)Modified [DADiskAppearedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskappearedcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskAppearedCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskAppearedCallback = (DADisk, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADiskClaim(_: DADisk, _: DADiskClaimOptions, _: DADiskClaimReleaseCallback?, _: UnsafeMutablePointer<Void>, _: DADiskClaimCallback?, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492694-dadiskclaim)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskClaim(_ disk: DADisk!, _ options: DADiskClaimOptions, _ release: DADiskClaimReleaseCallback, _ releaseContext: UnsafeMutablePointer<Void>, _ callback: DADiskClaimCallback, _ callbackContext: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskClaim(_ disk: DADisk, _ options: DADiskClaimOptions, _ release: DADiskClaimReleaseCallback?, _ releaseContext: UnsafeMutablePointer<Void>, _ callback: DADiskClaimCallback?, _ callbackContext: UnsafeMutablePointer<Void>) ``` |

Modified [DADiskClaimCallback](https://developer.apple.com/documentation/diskarbitration/dadiskclaimcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskClaimCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskClaimCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADiskClaimReleaseCallback](https://developer.apple.com/documentation/diskarbitration/dadiskclaimreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskClaimReleaseCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>!)> ``` |
| To | ``` typealias DADiskClaimReleaseCallback = (DADisk, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>? ``` |

Modified [DADiskCopyDescription(_: DADisk) -> CFDictionary?](https://developer.apple.com/documentation/diskarbitration/1401854-dadiskcopydescription)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskCopyDescription(_ disk: DADisk!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func DADiskCopyDescription(_ disk: DADisk) -> CFDictionary? ``` |

Modified [DADiskCopyIOMedia(_: DADisk) -> io_service_t](https://developer.apple.com/documentation/diskarbitration/1401888-dadiskcopyiomedia)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskCopyIOMedia(_ disk: DADisk!) -> io_service_t ``` |
| To | ``` func DADiskCopyIOMedia(_ disk: DADisk) -> io_service_t ``` |

Modified [DADiskCopyWholeDisk(_: DADisk) -> DADisk?](https://developer.apple.com/documentation/diskarbitration/1401828-dadiskcopywholedisk)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskCopyWholeDisk(_ disk: DADisk!) -> Unmanaged<DADisk>! ``` |
| To | ``` func DADiskCopyWholeDisk(_ disk: DADisk) -> DADisk? ``` |

Modified [DADiskCreateFromBSDName(_: CFAllocator?, _: DASession, _: UnsafePointer<Int8>) -> DADisk?](https://developer.apple.com/documentation/diskarbitration/1401870-dadiskcreatefrombsdname)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskCreateFromBSDName(_ allocator: CFAllocator!, _ session: DASession!, _ name: UnsafePointer<Int8>) -> Unmanaged<DADisk>! ``` |
| To | ``` func DADiskCreateFromBSDName(_ allocator: CFAllocator?, _ session: DASession, _ name: UnsafePointer<Int8>) -> DADisk? ``` |

Modified [DADiskCreateFromIOMedia(_: CFAllocator?, _: DASession, _: io_service_t) -> DADisk?](https://developer.apple.com/documentation/diskarbitration/1401862-dadiskcreatefromiomedia)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskCreateFromIOMedia(_ allocator: CFAllocator!, _ session: DASession!, _ media: io_service_t) -> Unmanaged<DADisk>! ``` |
| To | ``` func DADiskCreateFromIOMedia(_ allocator: CFAllocator?, _ session: DASession, _ media: io_service_t) -> DADisk? ``` |

Modified [DADiskCreateFromVolumePath(_: CFAllocator?, _: DASession, _: CFURL) -> DADisk?](https://developer.apple.com/documentation/diskarbitration/1401858-dadiskcreatefromvolumepath)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskCreateFromVolumePath(_ allocator: CFAllocator!, _ session: DASession!, _ path: CFURL!) -> Unmanaged<DADisk>! ``` |
| To | ``` func DADiskCreateFromVolumePath(_ allocator: CFAllocator?, _ session: DASession, _ path: CFURL) -> DADisk? ``` |

Modified [DADiskDescriptionChangedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskdescriptionchangedcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskDescriptionChangedCallback = CFunctionPointer<((DADisk!, CFArray!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskDescriptionChangedCallback = (DADisk, CFArray, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADiskDisappearedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskdisappearedcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskDisappearedCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskDisappearedCallback = (DADisk, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADiskEject(_: DADisk, _: DADiskEjectOptions, _: DADiskEjectCallback?, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492701-dadiskeject)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskEject(_ disk: DADisk!, _ options: DADiskEjectOptions, _ callback: DADiskEjectCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskEject(_ disk: DADisk, _ options: DADiskEjectOptions, _ callback: DADiskEjectCallback?, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DADiskEjectApprovalCallback](https://developer.apple.com/documentation/diskarbitration/dadiskejectapprovalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskEjectApprovalCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>!)> ``` |
| To | ``` typealias DADiskEjectApprovalCallback = (DADisk, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>? ``` |

Modified [DADiskEjectCallback](https://developer.apple.com/documentation/diskarbitration/dadiskejectcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskEjectCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskEjectCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADiskGetBSDName(_: DADisk) -> UnsafePointer<Int8>](https://developer.apple.com/documentation/diskarbitration/1401880-dadiskgetbsdname)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskGetBSDName(_ disk: DADisk!) -> UnsafePointer<Int8> ``` |
| To | ``` func DADiskGetBSDName(_ disk: DADisk) -> UnsafePointer<Int8> ``` |

Modified [DADiskGetOptions(_: DADisk) -> DADiskOptions](https://developer.apple.com/documentation/diskarbitration/1492711-dadiskgetoptions)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskGetOptions(_ disk: DADisk!) -> DADiskOptions ``` |
| To | ``` func DADiskGetOptions(_ disk: DADisk) -> DADiskOptions ``` |

Modified [DADiskIsClaimed(_: DADisk) -> Bool](https://developer.apple.com/documentation/diskarbitration/1492734-dadiskisclaimed)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskIsClaimed(_ disk: DADisk!) -> Boolean ``` |
| To | ``` func DADiskIsClaimed(_ disk: DADisk) -> Bool ``` |

Modified [DADiskMount(_: DADisk, _: CFURL?, _: DADiskMountOptions, _: DADiskMountCallback?, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492772-dadiskmount)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskMount(_ disk: DADisk!, _ path: CFURL!, _ options: DADiskMountOptions, _ callback: DADiskMountCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskMount(_ disk: DADisk, _ path: CFURL?, _ options: DADiskMountOptions, _ callback: DADiskMountCallback?, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DADiskMountApprovalCallback](https://developer.apple.com/documentation/diskarbitration/dadiskmountapprovalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskMountApprovalCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>!)> ``` |
| To | ``` typealias DADiskMountApprovalCallback = (DADisk, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>? ``` |

Modified [DADiskMountCallback](https://developer.apple.com/documentation/diskarbitration/dadiskmountcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskMountCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskMountCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADiskMountWithArguments(_: DADisk, _: CFURL?, _: DADiskMountOptions, _: DADiskMountCallback?, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<Unmanaged<CFString>?>)](https://developer.apple.com/documentation/diskarbitration/1492714-dadiskmountwitharguments)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskMountWithArguments(_ disk: DADisk!, _ path: CFURL!, _ options: DADiskMountOptions, _ callback: DADiskMountCallback, _ context: UnsafeMutablePointer<Void>, _ arguments: UnsafeMutablePointer<Unmanaged<CFString>?>) ``` |
| To | ``` func DADiskMountWithArguments(_ disk: DADisk, _ path: CFURL?, _ options: DADiskMountOptions, _ callback: DADiskMountCallback?, _ context: UnsafeMutablePointer<Void>, _ arguments: UnsafeMutablePointer<Unmanaged<CFString>?>) ``` |

Modified [DADiskPeekCallback](https://developer.apple.com/documentation/diskarbitration/dadiskpeekcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskPeekCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskPeekCallback = (DADisk, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADiskRename(_: DADisk, _: CFString, _: DADiskRenameOptions, _: DADiskRenameCallback?, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492760-dadiskrename)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskRename(_ disk: DADisk!, _ name: CFString!, _ options: DADiskRenameOptions, _ callback: DADiskRenameCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskRename(_ disk: DADisk, _ name: CFString, _ options: DADiskRenameOptions, _ callback: DADiskRenameCallback?, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DADiskRenameCallback](https://developer.apple.com/documentation/diskarbitration/dadiskrenamecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskRenameCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskRenameCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADiskSetOptions(_: DADisk, _: DADiskOptions, _: Bool) -> DAReturn](https://developer.apple.com/documentation/diskarbitration/1492759-dadisksetoptions)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskSetOptions(_ disk: DADisk!, _ options: DADiskOptions, _ value: Boolean) -> DAReturn ``` |
| To | ``` func DADiskSetOptions(_ disk: DADisk, _ options: DADiskOptions, _ value: Bool) -> DAReturn ``` |

Modified [DADiskUnclaim(_: DADisk)](https://developer.apple.com/documentation/diskarbitration/1492726-dadiskunclaim)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskUnclaim(_ disk: DADisk!) ``` |
| To | ``` func DADiskUnclaim(_ disk: DADisk) ``` |

Modified [DADiskUnmount(_: DADisk, _: DADiskUnmountOptions, _: DADiskUnmountCallback?, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492758-dadiskunmount)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskUnmount(_ disk: DADisk!, _ options: DADiskUnmountOptions, _ callback: DADiskUnmountCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskUnmount(_ disk: DADisk, _ options: DADiskUnmountOptions, _ callback: DADiskUnmountCallback?, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DADiskUnmountApprovalCallback](https://developer.apple.com/documentation/diskarbitration/dadiskunmountapprovalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskUnmountApprovalCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>!)> ``` |
| To | ``` typealias DADiskUnmountApprovalCallback = (DADisk, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>? ``` |

Modified [DADiskUnmountCallback](https://developer.apple.com/documentation/diskarbitration/dadiskunmountcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskUnmountCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DADiskUnmountCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [DADissenterCreate(_: CFAllocator?, _: DAReturn, _: CFString?) -> DADissenter](https://developer.apple.com/documentation/diskarbitration/1501551-dadissentercreate)

|  | Declaration |
| --- | --- |
| From | ``` func DADissenterCreate(_ allocator: CFAllocator!, _ status: DAReturn, _ string: CFString!) -> Unmanaged<DADissenter>! ``` |
| To | ``` func DADissenterCreate(_ allocator: CFAllocator?, _ status: DAReturn, _ string: CFString?) -> DADissenter ``` |

Modified [DADissenterGetStatus(_: DADissenter) -> DAReturn](https://developer.apple.com/documentation/diskarbitration/1501539-dadissentergetstatus)

|  | Declaration |
| --- | --- |
| From | ``` func DADissenterGetStatus(_ dissenter: DADissenter!) -> DAReturn ``` |
| To | ``` func DADissenterGetStatus(_ dissenter: DADissenter) -> DAReturn ``` |

Modified [DADissenterGetStatusString(_: DADissenter) -> CFString?](https://developer.apple.com/documentation/diskarbitration/1501531-dadissentergetstatusstring)

|  | Declaration |
| --- | --- |
| From | ``` func DADissenterGetStatusString(_ dissenter: DADissenter!) -> Unmanaged<CFString>! ``` |
| To | ``` func DADissenterGetStatusString(_ dissenter: DADissenter) -> CFString? ``` |

Modified [DARegisterDiskAppearedCallback(_: DASession, _: CFDictionary?, _: DADiskAppearedCallback, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492707-daregisterdiskappearedcallback)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskAppearedCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskAppearedCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskAppearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskAppearedCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DARegisterDiskDescriptionChangedCallback(_: DASession, _: CFDictionary?, _: CFArray?, _: DADiskDescriptionChangedCallback, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492705-daregisterdiskdescriptionchanged)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskDescriptionChangedCallback(_ session: DASession!, _ match: CFDictionary!, _ watch: CFArray!, _ callback: DADiskDescriptionChangedCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskDescriptionChangedCallback(_ session: DASession, _ match: CFDictionary?, _ watch: CFArray?, _ callback: DADiskDescriptionChangedCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DARegisterDiskDisappearedCallback(_: DASession, _: CFDictionary?, _: DADiskDisappearedCallback, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492696-daregisterdiskdisappearedcallbac)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskDisappearedCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskDisappearedCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskDisappearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskDisappearedCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DARegisterDiskEjectApprovalCallback(_: DASession, _: CFDictionary?, _: DADiskEjectApprovalCallback, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492715-daregisterdiskejectapprovalcallb)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskEjectApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskEjectApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskEjectApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskEjectApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DARegisterDiskMountApprovalCallback(_: DASession, _: CFDictionary?, _: DADiskMountApprovalCallback, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492762-daregisterdiskmountapprovalcallb)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskMountApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskMountApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskMountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskMountApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DARegisterDiskPeekCallback(_: DASession, _: CFDictionary?, _: CFIndex, _: DADiskPeekCallback, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492728-daregisterdiskpeekcallback)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskPeekCallback(_ session: DASession!, _ match: CFDictionary!, _ order: CFIndex, _ callback: DADiskPeekCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskPeekCallback(_ session: DASession, _ match: CFDictionary?, _ order: CFIndex, _ callback: DADiskPeekCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DARegisterDiskUnmountApprovalCallback(_: DASession, _: CFDictionary?, _: DADiskUnmountApprovalCallback, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492698-daregisterdiskunmountapprovalcal)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskUnmountApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskUnmountApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskUnmountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskUnmountApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [DASessionCreate(_: CFAllocator?) -> DASession?](https://developer.apple.com/documentation/diskarbitration/1501530-dasessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func DASessionCreate(_ allocator: CFAllocator!) -> Unmanaged<DASession>! ``` |
| To | ``` func DASessionCreate(_ allocator: CFAllocator?) -> DASession? ``` |

Modified [DASessionScheduleWithRunLoop(_: DASession, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/diskarbitration/1501544-dasessionschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func DASessionScheduleWithRunLoop(_ session: DASession!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func DASessionScheduleWithRunLoop(_ session: DASession, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [DASessionSetDispatchQueue(_: DASession, _: dispatch_queue_t?)](https://developer.apple.com/documentation/diskarbitration/1501542-dasessionsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func DASessionSetDispatchQueue(_ session: DASession!, _ queue: dispatch_queue_t!) ``` |
| To | ``` func DASessionSetDispatchQueue(_ session: DASession, _ queue: dispatch_queue_t?) ``` |

Modified [DASessionUnscheduleFromRunLoop(_: DASession, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/diskarbitration/1501550-dasessionunschedulefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func DASessionUnscheduleFromRunLoop(_ session: DASession!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func DASessionUnscheduleFromRunLoop(_ session: DASession, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [DAUnregisterCallback(_: DASession, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/diskarbitration/1492712-daunregistercallback)

|  | Declaration |
| --- | --- |
| From | ``` func DAUnregisterCallback(_ session: DASession!, _ callback: UnsafeMutablePointer<Void>, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DAUnregisterCallback(_ session: DASession, _ callback: UnsafeMutablePointer<Void>, _ context: UnsafeMutablePointer<Void>) ``` |

Modified [kDADiskDescriptionBusNameKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionbusnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionBusNameKey: CFString! ``` |
| To | ``` let kDADiskDescriptionBusNameKey: CFString ``` |

Modified [kDADiskDescriptionBusPathKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionbuspathkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionBusPathKey: CFString! ``` |
| To | ``` let kDADiskDescriptionBusPathKey: CFString ``` |

Modified [kDADiskDescriptionDeviceGUIDKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptiondeviceguidkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionDeviceGUIDKey: CFString! ``` |
| To | ``` let kDADiskDescriptionDeviceGUIDKey: CFString ``` |

Modified [kDADiskDescriptionDeviceInternalKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptiondeviceinternalkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionDeviceInternalKey: CFString! ``` |
| To | ``` let kDADiskDescriptionDeviceInternalKey: CFString ``` |

Modified [kDADiskDescriptionDeviceModelKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptiondevicemodelkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionDeviceModelKey: CFString! ``` |
| To | ``` let kDADiskDescriptionDeviceModelKey: CFString ``` |

Modified [kDADiskDescriptionDevicePathKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptiondevicepathkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionDevicePathKey: CFString! ``` |
| To | ``` let kDADiskDescriptionDevicePathKey: CFString ``` |

Modified [kDADiskDescriptionDeviceProtocolKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptiondeviceprotocolkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionDeviceProtocolKey: CFString! ``` |
| To | ``` let kDADiskDescriptionDeviceProtocolKey: CFString ``` |

Modified [kDADiskDescriptionDeviceRevisionKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptiondevicerevisionkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionDeviceRevisionKey: CFString! ``` |
| To | ``` let kDADiskDescriptionDeviceRevisionKey: CFString ``` |

Modified [kDADiskDescriptionDeviceUnitKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptiondeviceunitkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionDeviceUnitKey: CFString! ``` |
| To | ``` let kDADiskDescriptionDeviceUnitKey: CFString ``` |

Modified [kDADiskDescriptionDeviceVendorKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptiondevicevendorkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionDeviceVendorKey: CFString! ``` |
| To | ``` let kDADiskDescriptionDeviceVendorKey: CFString ``` |

Modified [kDADiskDescriptionMatchMediaUnformatted](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchmediaunformatted)

|  | Declaration |
| --- | --- |
| From | ``` var kDADiskDescriptionMatchMediaUnformatted: Unmanaged<CFDictionary>! ``` |
| To | ``` var kDADiskDescriptionMatchMediaUnformatted: Unmanaged<CFDictionary> ``` |

Modified [kDADiskDescriptionMatchMediaWhole](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchmediawhole)

|  | Declaration |
| --- | --- |
| From | ``` var kDADiskDescriptionMatchMediaWhole: Unmanaged<CFDictionary>! ``` |
| To | ``` var kDADiskDescriptionMatchMediaWhole: Unmanaged<CFDictionary> ``` |

Modified [kDADiskDescriptionMatchVolumeMountable](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchvolumemountable)

|  | Declaration |
| --- | --- |
| From | ``` var kDADiskDescriptionMatchVolumeMountable: Unmanaged<CFDictionary>! ``` |
| To | ``` var kDADiskDescriptionMatchVolumeMountable: Unmanaged<CFDictionary> ``` |

Modified [kDADiskDescriptionMatchVolumeUnrecognized](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchvolumeunrecognized)

|  | Declaration |
| --- | --- |
| From | ``` var kDADiskDescriptionMatchVolumeUnrecognized: Unmanaged<CFDictionary>! ``` |
| To | ``` var kDADiskDescriptionMatchVolumeUnrecognized: Unmanaged<CFDictionary> ``` |

Modified [kDADiskDescriptionMediaBlockSizeKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediablocksizekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaBlockSizeKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaBlockSizeKey: CFString ``` |

Modified [kDADiskDescriptionMediaBSDMajorKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediabsdmajorkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaBSDMajorKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaBSDMajorKey: CFString ``` |

Modified [kDADiskDescriptionMediaBSDMinorKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediabsdminorkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaBSDMinorKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaBSDMinorKey: CFString ``` |

Modified [kDADiskDescriptionMediaBSDNameKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediabsdnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaBSDNameKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaBSDNameKey: CFString ``` |

Modified [kDADiskDescriptionMediaBSDUnitKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediabsdunitkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaBSDUnitKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaBSDUnitKey: CFString ``` |

Modified [kDADiskDescriptionMediaContentKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediacontentkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaContentKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaContentKey: CFString ``` |

Modified [kDADiskDescriptionMediaEjectableKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediaejectablekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaEjectableKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaEjectableKey: CFString ``` |

Modified [kDADiskDescriptionMediaIconKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediaiconkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaIconKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaIconKey: CFString ``` |

Modified [kDADiskDescriptionMediaKindKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediakindkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaKindKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaKindKey: CFString ``` |

Modified [kDADiskDescriptionMediaLeafKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmedialeafkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaLeafKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaLeafKey: CFString ``` |

Modified [kDADiskDescriptionMediaNameKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmedianamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaNameKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaNameKey: CFString ``` |

Modified [kDADiskDescriptionMediaPathKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediapathkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaPathKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaPathKey: CFString ``` |

Modified [kDADiskDescriptionMediaRemovableKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediaremovablekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaRemovableKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaRemovableKey: CFString ``` |

Modified [kDADiskDescriptionMediaSizeKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediasizekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaSizeKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaSizeKey: CFString ``` |

Modified [kDADiskDescriptionMediaTypeKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediatypekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaTypeKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaTypeKey: CFString ``` |

Modified [kDADiskDescriptionMediaUUIDKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediauuidkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaUUIDKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaUUIDKey: CFString ``` |

Modified [kDADiskDescriptionMediaWholeKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediawholekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaWholeKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaWholeKey: CFString ``` |

Modified [kDADiskDescriptionMediaWritableKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmediawritablekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionMediaWritableKey: CFString! ``` |
| To | ``` let kDADiskDescriptionMediaWritableKey: CFString ``` |

Modified [kDADiskDescriptionVolumeKindKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionvolumekindkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionVolumeKindKey: CFString! ``` |
| To | ``` let kDADiskDescriptionVolumeKindKey: CFString ``` |

Modified [kDADiskDescriptionVolumeMountableKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionvolumemountablekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionVolumeMountableKey: CFString! ``` |
| To | ``` let kDADiskDescriptionVolumeMountableKey: CFString ``` |

Modified [kDADiskDescriptionVolumeNameKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionvolumenamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionVolumeNameKey: CFString! ``` |
| To | ``` let kDADiskDescriptionVolumeNameKey: CFString ``` |

Modified [kDADiskDescriptionVolumeNetworkKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionvolumenetworkkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionVolumeNetworkKey: CFString! ``` |
| To | ``` let kDADiskDescriptionVolumeNetworkKey: CFString ``` |

Modified [kDADiskDescriptionVolumePathKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionvolumepathkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionVolumePathKey: CFString! ``` |
| To | ``` let kDADiskDescriptionVolumePathKey: CFString ``` |

Modified [kDADiskDescriptionVolumeUUIDKey](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionvolumeuuidkey)

|  | Declaration |
| --- | --- |
| From | ``` let kDADiskDescriptionVolumeUUIDKey: CFString! ``` |
| To | ``` let kDADiskDescriptionVolumeUUIDKey: CFString ``` |

Modified [kDADiskDescriptionWatchVolumeName](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionwatchvolumename)

|  | Declaration |
| --- | --- |
| From | ``` var kDADiskDescriptionWatchVolumeName: Unmanaged<CFArray>! ``` |
| To | ``` var kDADiskDescriptionWatchVolumeName: Unmanaged<CFArray> ``` |

Modified [kDADiskDescriptionWatchVolumePath](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionwatchvolumepath)

|  | Declaration |
| --- | --- |
| From | ``` var kDADiskDescriptionWatchVolumePath: Unmanaged<CFArray>! ``` |
| To | ``` var kDADiskDescriptionWatchVolumePath: Unmanaged<CFArray> ``` |

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

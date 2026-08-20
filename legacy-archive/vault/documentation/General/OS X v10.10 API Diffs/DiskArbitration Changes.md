---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/DiskArbitration.html
archived_at: '2026-07-15T07:34:54.210354Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# DiskArbitration Changes

## DiskArbitration (Added)

Added DAApprovalSessionCreate(CFAllocator!) -> Unmanaged<DAApprovalSession>!Added DAApprovalSessionGetTypeID() -> CFTypeIDAdded DAApprovalSessionRefAdded DAApprovalSessionScheduleWithRunLoop(DAApprovalSession!, CFRunLoop!, CFString!)Added DAApprovalSessionUnscheduleFromRunLoop(DAApprovalSession!, CFRunLoop!, CFString!)Added DADiskAppearedCallbackAdded DADiskClaim(DADisk!, DADiskClaimOptions, DADiskClaimReleaseCallback, UnsafeMutablePointer<Void>, DADiskClaimCallback, UnsafeMutablePointer<Void>)Added DADiskClaimCallbackAdded DADiskClaimOptionsAdded DADiskClaimReleaseCallbackAdded DADiskCopyDescription(DADisk!) -> Unmanaged<CFDictionary>!Added DADiskCopyIOMedia(DADisk!) -> io_service_tAdded DADiskCopyWholeDisk(DADisk!) -> Unmanaged<DADisk>!Added DADiskCreateFromBSDName(CFAllocator!, DASession!, UnsafePointer<Int8>) -> Unmanaged<DADisk>!Added DADiskCreateFromIOMedia(CFAllocator!, DASession!, io_service_t) -> Unmanaged<DADisk>!Added DADiskCreateFromVolumePath(CFAllocator!, DASession!, CFURL!) -> Unmanaged<DADisk>!Added DADiskDescriptionChangedCallbackAdded DADiskDisappearedCallbackAdded DADiskEject(DADisk!, DADiskEjectOptions, DADiskEjectCallback, UnsafeMutablePointer<Void>)Added DADiskEjectApprovalCallbackAdded DADiskEjectCallbackAdded DADiskEjectOptionsAdded DADiskGetBSDName(DADisk!) -> UnsafePointer<Int8>Added DADiskGetOptions(DADisk!) -> DADiskOptionsAdded DADiskGetTypeID() -> CFTypeIDAdded DADiskIsClaimed(DADisk!) -> BooleanAdded DADiskMount(DADisk!, CFURL!, DADiskMountOptions, DADiskMountCallback, UnsafeMutablePointer<Void>)Added DADiskMountApprovalCallbackAdded DADiskMountCallbackAdded DADiskMountOptionsAdded DADiskMountWithArguments(DADisk!, CFURL!, DADiskMountOptions, DADiskMountCallback, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<CFString>?>)Added DADiskOptionsAdded DADiskPeekCallbackAdded DADiskRefAdded DADiskRename(DADisk!, CFString!, DADiskRenameOptions, DADiskRenameCallback, UnsafeMutablePointer<Void>)Added DADiskRenameCallbackAdded DADiskRenameOptionsAdded DADiskSetOptions(DADisk!, DADiskOptions, Boolean) -> DAReturnAdded DADiskUnclaim(DADisk!)Added DADiskUnmount(DADisk!, DADiskUnmountOptions, DADiskUnmountCallback, UnsafeMutablePointer<Void>)Added DADiskUnmountApprovalCallbackAdded DADiskUnmountCallbackAdded DADiskUnmountOptionsAdded DADissenterCreate(CFAllocator!, DAReturn, CFString!) -> Unmanaged<DADissenter>!Added DADissenterGetStatus(DADissenter!) -> DAReturnAdded DADissenterGetStatusString(DADissenter!) -> Unmanaged<CFString>!Added DADissenterRefAdded DARegisterDiskAppearedCallback(DASession!, CFDictionary!, DADiskAppearedCallback, UnsafeMutablePointer<Void>)Added DARegisterDiskDescriptionChangedCallback(DASession!, CFDictionary!, CFArray!, DADiskDescriptionChangedCallback, UnsafeMutablePointer<Void>)Added DARegisterDiskDisappearedCallback(DASession!, CFDictionary!, DADiskDisappearedCallback, UnsafeMutablePointer<Void>)Added DARegisterDiskEjectApprovalCallback(DASession!, CFDictionary!, DADiskEjectApprovalCallback, UnsafeMutablePointer<Void>)Added DARegisterDiskMountApprovalCallback(DASession!, CFDictionary!, DADiskMountApprovalCallback, UnsafeMutablePointer<Void>)Added DARegisterDiskPeekCallback(DASession!, CFDictionary!, CFIndex, DADiskPeekCallback, UnsafeMutablePointer<Void>)Added DARegisterDiskUnmountApprovalCallback(DASession!, CFDictionary!, DADiskUnmountApprovalCallback, UnsafeMutablePointer<Void>)Added DAReturnAdded DASessionCreate(CFAllocator!) -> Unmanaged<DASession>!Added DASessionGetTypeID() -> CFTypeIDAdded DASessionRefAdded DASessionScheduleWithRunLoop(DASession!, CFRunLoop!, CFString!)Added DASessionSetDispatchQueue(DASession!, dispatch_queue_t!)Added DASessionUnscheduleFromRunLoop(DASession!, CFRunLoop!, CFString!)Added DAUnregisterApprovalCallback(DASession!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)Added DAUnregisterCallback(DASession!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)Added kDADiskClaimOptionDefaultAdded kDADiskDescriptionBusNameKeyAdded kDADiskDescriptionBusPathKeyAdded kDADiskDescriptionDeviceGUIDKeyAdded kDADiskDescriptionDeviceInternalKeyAdded kDADiskDescriptionDeviceModelKeyAdded kDADiskDescriptionDevicePathKeyAdded kDADiskDescriptionDeviceProtocolKeyAdded kDADiskDescriptionDeviceRevisionKeyAdded kDADiskDescriptionDeviceUnitKeyAdded kDADiskDescriptionDeviceVendorKeyAdded kDADiskDescriptionMatchMediaUnformattedAdded kDADiskDescriptionMatchMediaWholeAdded kDADiskDescriptionMatchVolumeMountableAdded kDADiskDescriptionMatchVolumeUnrecognizedAdded kDADiskDescriptionMediaBSDMajorKeyAdded kDADiskDescriptionMediaBSDMinorKeyAdded kDADiskDescriptionMediaBSDNameKeyAdded kDADiskDescriptionMediaBSDUnitKeyAdded kDADiskDescriptionMediaBlockSizeKeyAdded kDADiskDescriptionMediaContentKeyAdded kDADiskDescriptionMediaEjectableKeyAdded kDADiskDescriptionMediaIconKeyAdded kDADiskDescriptionMediaKindKeyAdded kDADiskDescriptionMediaLeafKeyAdded kDADiskDescriptionMediaNameKeyAdded kDADiskDescriptionMediaPathKeyAdded kDADiskDescriptionMediaRemovableKeyAdded kDADiskDescriptionMediaSizeKeyAdded kDADiskDescriptionMediaTypeKeyAdded kDADiskDescriptionMediaUUIDKeyAdded kDADiskDescriptionMediaWholeKeyAdded kDADiskDescriptionMediaWritableKeyAdded kDADiskDescriptionVolumeKindKeyAdded kDADiskDescriptionVolumeMountableKeyAdded kDADiskDescriptionVolumeNameKeyAdded kDADiskDescriptionVolumeNetworkKeyAdded kDADiskDescriptionVolumePathKeyAdded kDADiskDescriptionVolumeUUIDKeyAdded kDADiskDescriptionWatchVolumeNameAdded kDADiskDescriptionWatchVolumePathAdded kDADiskEjectOptionDefaultAdded kDADiskMountOptionDefaultAdded kDADiskMountOptionWholeAdded kDADiskOptionDefaultAdded kDADiskRenameOptionDefaultAdded kDADiskUnmountOptionDefaultAdded kDADiskUnmountOptionForceAdded kDADiskUnmountOptionWholeAdded kDAReturnBadArgumentAdded kDAReturnBusyAdded kDAReturnErrorAdded kDAReturnExclusiveAccessAdded kDAReturnNoResourcesAdded kDAReturnNotFoundAdded kDAReturnNotMountedAdded kDAReturnNotPermittedAdded kDAReturnNotPrivilegedAdded kDAReturnNotReadyAdded kDAReturnNotWritableAdded kDAReturnSuccessAdded kDAReturnUnsupported

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

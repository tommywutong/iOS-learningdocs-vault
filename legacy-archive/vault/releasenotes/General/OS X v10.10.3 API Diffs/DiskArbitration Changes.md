---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/DiskArbitration.html
archived_at: '2026-07-18T02:52:23.813576Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# DiskArbitration Changes

## DiskArbitration

Modified DADiskAppearedCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskAppearedCallback = CFunctionPointer<((DADisk!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskAppearedCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DADiskClaim(DADisk!, DADiskClaimOptions, DADiskClaimReleaseCallback, UnsafeMutablePointer<Void>, DADiskClaimCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskClaim(_ disk: DADisk!, _ options: DADiskClaimOptions, _ release: DADiskClaimReleaseCallback, _ releaseContext: UnsafePointer<()>, _ callback: DADiskClaimCallback, _ callbackContext: UnsafePointer<()>) ``` |
| To | ``` func DADiskClaim(_ disk: DADisk!, _ options: DADiskClaimOptions, _ release: DADiskClaimReleaseCallback, _ releaseContext: UnsafeMutablePointer<Void>, _ callback: DADiskClaimCallback, _ callbackContext: UnsafeMutablePointer<Void>) ``` |

Modified DADiskClaimCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskClaimCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskClaimCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DADiskClaimReleaseCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskClaimReleaseCallback = CFunctionPointer<((DADisk!, UnsafePointer<()>) -> Unmanaged<DADissenter>!)> ``` |
| To | ``` typealias DADiskClaimReleaseCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>!)> ``` |

Modified DADiskCreateFromBSDName(CFAllocator!, DASession!, UnsafePointer<Int8>) -> Unmanaged<DADisk>!

|  | Declaration |
| --- | --- |
| From | ``` func DADiskCreateFromBSDName(_ allocator: CFAllocator!, _ session: DASession!, _ name: ConstUnsafePointer<Int8>) -> Unmanaged<DADisk>! ``` |
| To | ``` func DADiskCreateFromBSDName(_ allocator: CFAllocator!, _ session: DASession!, _ name: UnsafePointer<Int8>) -> Unmanaged<DADisk>! ``` |

Modified DADiskDescriptionChangedCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskDescriptionChangedCallback = CFunctionPointer<((DADisk!, CFArray!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskDescriptionChangedCallback = CFunctionPointer<((DADisk!, CFArray!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DADiskDisappearedCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskDisappearedCallback = CFunctionPointer<((DADisk!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskDisappearedCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DADiskEject(DADisk!, DADiskEjectOptions, DADiskEjectCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskEject(_ disk: DADisk!, _ options: DADiskEjectOptions, _ callback: DADiskEjectCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DADiskEject(_ disk: DADisk!, _ options: DADiskEjectOptions, _ callback: DADiskEjectCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DADiskEjectApprovalCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskEjectApprovalCallback = CFunctionPointer<((DADisk!, UnsafePointer<()>) -> Unmanaged<DADissenter>!)> ``` |
| To | ``` typealias DADiskEjectApprovalCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>!)> ``` |

Modified DADiskEjectCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskEjectCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskEjectCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DADiskGetBSDName(DADisk!) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func DADiskGetBSDName(_ disk: DADisk!) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func DADiskGetBSDName(_ disk: DADisk!) -> UnsafePointer<Int8> ``` |

Modified DADiskMount(DADisk!, CFURL!, DADiskMountOptions, DADiskMountCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskMount(_ disk: DADisk!, _ path: CFURL!, _ options: DADiskMountOptions, _ callback: DADiskMountCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DADiskMount(_ disk: DADisk!, _ path: CFURL!, _ options: DADiskMountOptions, _ callback: DADiskMountCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DADiskMountApprovalCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskMountApprovalCallback = CFunctionPointer<((DADisk!, UnsafePointer<()>) -> Unmanaged<DADissenter>!)> ``` |
| To | ``` typealias DADiskMountApprovalCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>!)> ``` |

Modified DADiskMountCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskMountCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskMountCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DADiskMountWithArguments(DADisk!, CFURL!, DADiskMountOptions, DADiskMountCallback, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<CFString>?>)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskMountWithArguments(_ disk: DADisk!, _ path: CFURL!, _ options: DADiskMountOptions, _ callback: DADiskMountCallback, _ context: UnsafePointer<()>, _ arguments: UnsafePointer<Unmanaged<CFString>?>) ``` |
| To | ``` func DADiskMountWithArguments(_ disk: DADisk!, _ path: CFURL!, _ options: DADiskMountOptions, _ callback: DADiskMountCallback, _ context: UnsafeMutablePointer<Void>, _ arguments: UnsafeMutablePointer<Unmanaged<CFString>?>) ``` |

Modified DADiskPeekCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskPeekCallback = CFunctionPointer<((DADisk!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskPeekCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DADiskRename(DADisk!, CFString!, DADiskRenameOptions, DADiskRenameCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskRename(_ disk: DADisk!, _ name: CFString!, _ options: DADiskRenameOptions, _ callback: DADiskRenameCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DADiskRename(_ disk: DADisk!, _ name: CFString!, _ options: DADiskRenameOptions, _ callback: DADiskRenameCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DADiskRenameCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskRenameCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskRenameCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DADiskUnmount(DADisk!, DADiskUnmountOptions, DADiskUnmountCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskUnmount(_ disk: DADisk!, _ options: DADiskUnmountOptions, _ callback: DADiskUnmountCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DADiskUnmount(_ disk: DADisk!, _ options: DADiskUnmountOptions, _ callback: DADiskUnmountCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DADiskUnmountApprovalCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskUnmountApprovalCallback = CFunctionPointer<((DADisk!, UnsafePointer<()>) -> Unmanaged<DADissenter>!)> ``` |
| To | ``` typealias DADiskUnmountApprovalCallback = CFunctionPointer<((DADisk!, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>!)> ``` |

Modified DADiskUnmountCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskUnmountCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DADiskUnmountCallback = CFunctionPointer<((DADisk!, DADissenter!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DARegisterDiskAppearedCallback(DASession!, CFDictionary!, DADiskAppearedCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskAppearedCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskAppearedCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DARegisterDiskAppearedCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskAppearedCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DARegisterDiskDescriptionChangedCallback(DASession!, CFDictionary!, CFArray!, DADiskDescriptionChangedCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskDescriptionChangedCallback(_ session: DASession!, _ match: CFDictionary!, _ watch: CFArray!, _ callback: DADiskDescriptionChangedCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DARegisterDiskDescriptionChangedCallback(_ session: DASession!, _ match: CFDictionary!, _ watch: CFArray!, _ callback: DADiskDescriptionChangedCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DARegisterDiskDisappearedCallback(DASession!, CFDictionary!, DADiskDisappearedCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskDisappearedCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskDisappearedCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DARegisterDiskDisappearedCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskDisappearedCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DARegisterDiskEjectApprovalCallback(DASession!, CFDictionary!, DADiskEjectApprovalCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskEjectApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskEjectApprovalCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DARegisterDiskEjectApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskEjectApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DARegisterDiskMountApprovalCallback(DASession!, CFDictionary!, DADiskMountApprovalCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskMountApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskMountApprovalCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DARegisterDiskMountApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskMountApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DARegisterDiskPeekCallback(DASession!, CFDictionary!, CFIndex, DADiskPeekCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskPeekCallback(_ session: DASession!, _ match: CFDictionary!, _ order: CFIndex, _ callback: DADiskPeekCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DARegisterDiskPeekCallback(_ session: DASession!, _ match: CFDictionary!, _ order: CFIndex, _ callback: DADiskPeekCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DARegisterDiskUnmountApprovalCallback(DASession!, CFDictionary!, DADiskUnmountApprovalCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskUnmountApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskUnmountApprovalCallback, _ context: UnsafePointer<()>) ``` |
| To | ``` func DARegisterDiskUnmountApprovalCallback(_ session: DASession!, _ match: CFDictionary!, _ callback: DADiskUnmountApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DAUnregisterApprovalCallback(DASession!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DAUnregisterApprovalCallback(_ session: DASession!, _ callback: UnsafePointer<()>, _ context: UnsafePointer<()>) ``` |
| To | ``` func DAUnregisterApprovalCallback(_ session: DASession!, _ callback: UnsafeMutablePointer<Void>, _ context: UnsafeMutablePointer<Void>) ``` |

Modified DAUnregisterCallback(DASession!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func DAUnregisterCallback(_ session: DASession!, _ callback: UnsafePointer<()>, _ context: UnsafePointer<()>) ``` |
| To | ``` func DAUnregisterCallback(_ session: DASession!, _ callback: UnsafeMutablePointer<Void>, _ context: UnsafeMutablePointer<Void>) ``` |

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

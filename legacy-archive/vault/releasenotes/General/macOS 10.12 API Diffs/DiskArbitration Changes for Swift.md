---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/DiskArbitration.html
archived_at: '2026-07-18T02:51:16.581018Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# DiskArbitration Changes for Swift

### DiskArbitration

Modified [DADiskAppearedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskappearedcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskAppearedCallback = (DADisk, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskAppearedCallback = (DADisk, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DADiskClaim(_: DADisk, _: DADiskClaimOptions, _: DiskArbitration.DADiskClaimReleaseCallback?, _: UnsafeMutableRawPointer?, _: DiskArbitration.DADiskClaimCallback?, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492694-dadiskclaim)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskClaim(_ disk: DADisk, _ options: DADiskClaimOptions, _ release: DADiskClaimReleaseCallback?, _ releaseContext: UnsafeMutablePointer<Void>, _ callback: DADiskClaimCallback?, _ callbackContext: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskClaim(_ disk: DADisk, _ options: DADiskClaimOptions, _ release: DiskArbitration.DADiskClaimReleaseCallback?, _ releaseContext: UnsafeMutableRawPointer?, _ callback: DiskArbitration.DADiskClaimCallback?, _ callbackContext: UnsafeMutableRawPointer?) ``` |

Modified [DADiskClaimCallback](https://developer.apple.com/documentation/diskarbitration/dadiskclaimcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskClaimCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskClaimCallback = (DADisk, DADissenter?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DADiskClaimReleaseCallback](https://developer.apple.com/documentation/diskarbitration/dadiskclaimreleasecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskClaimReleaseCallback = (DADisk, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>? ``` |
| To | ``` typealias DADiskClaimReleaseCallback = (DADisk, UnsafeMutableRawPointer?) -> Unmanaged<DADissenter>? ``` |

Modified [DADiskDescriptionChangedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskdescriptionchangedcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskDescriptionChangedCallback = (DADisk, CFArray, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskDescriptionChangedCallback = (DADisk, CFArray, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DADiskDisappearedCallback](https://developer.apple.com/documentation/diskarbitration/dadiskdisappearedcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskDisappearedCallback = (DADisk, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskDisappearedCallback = (DADisk, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DADiskEject(_: DADisk, _: DADiskEjectOptions, _: DiskArbitration.DADiskEjectCallback?, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492701-dadiskeject)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskEject(_ disk: DADisk, _ options: DADiskEjectOptions, _ callback: DADiskEjectCallback?, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskEject(_ disk: DADisk, _ options: DADiskEjectOptions, _ callback: DiskArbitration.DADiskEjectCallback?, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DADiskEjectApprovalCallback](https://developer.apple.com/documentation/diskarbitration/dadiskejectapprovalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskEjectApprovalCallback = (DADisk, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>? ``` |
| To | ``` typealias DADiskEjectApprovalCallback = (DADisk, UnsafeMutableRawPointer?) -> Unmanaged<DADissenter>? ``` |

Modified [DADiskEjectCallback](https://developer.apple.com/documentation/diskarbitration/dadiskejectcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskEjectCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskEjectCallback = (DADisk, DADissenter?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DADiskGetBSDName(_: DADisk) -> UnsafePointer<Int8>?](https://developer.apple.com/documentation/diskarbitration/1401880-dadiskgetbsdname)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskGetBSDName(_ disk: DADisk) -> UnsafePointer<Int8> ``` |
| To | ``` func DADiskGetBSDName(_ disk: DADisk) -> UnsafePointer<Int8>? ``` |

Modified [DADiskMount(_: DADisk, _: CFURL?, _: DADiskMountOptions, _: DiskArbitration.DADiskMountCallback?, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492772-dadiskmount)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskMount(_ disk: DADisk, _ path: CFURL?, _ options: DADiskMountOptions, _ callback: DADiskMountCallback?, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskMount(_ disk: DADisk, _ path: CFURL?, _ options: DADiskMountOptions, _ callback: DiskArbitration.DADiskMountCallback?, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DADiskMountApprovalCallback](https://developer.apple.com/documentation/diskarbitration/dadiskmountapprovalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskMountApprovalCallback = (DADisk, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>? ``` |
| To | ``` typealias DADiskMountApprovalCallback = (DADisk, UnsafeMutableRawPointer?) -> Unmanaged<DADissenter>? ``` |

Modified [DADiskMountCallback](https://developer.apple.com/documentation/diskarbitration/dadiskmountcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskMountCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskMountCallback = (DADisk, DADissenter?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DADiskMountWithArguments(_: DADisk, _: CFURL?, _: DADiskMountOptions, _: DiskArbitration.DADiskMountCallback?, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<Unmanaged<CFString>>!)](https://developer.apple.com/documentation/diskarbitration/1492714-dadiskmountwitharguments)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskMountWithArguments(_ disk: DADisk, _ path: CFURL?, _ options: DADiskMountOptions, _ callback: DADiskMountCallback?, _ context: UnsafeMutablePointer<Void>, _ arguments: UnsafeMutablePointer<Unmanaged<CFString>?>) ``` |
| To | ``` func DADiskMountWithArguments(_ disk: DADisk, _ path: CFURL?, _ options: DADiskMountOptions, _ callback: DiskArbitration.DADiskMountCallback?, _ context: UnsafeMutableRawPointer?, _ arguments: UnsafeMutablePointer<Unmanaged<CFString>>!) ``` |

Modified [DADiskPeekCallback](https://developer.apple.com/documentation/diskarbitration/dadiskpeekcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskPeekCallback = (DADisk, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskPeekCallback = (DADisk, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DADiskRename(_: DADisk, _: CFString, _: DADiskRenameOptions, _: DiskArbitration.DADiskRenameCallback?, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492760-dadiskrename)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskRename(_ disk: DADisk, _ name: CFString, _ options: DADiskRenameOptions, _ callback: DADiskRenameCallback?, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskRename(_ disk: DADisk, _ name: CFString, _ options: DADiskRenameOptions, _ callback: DiskArbitration.DADiskRenameCallback?, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DADiskRenameCallback](https://developer.apple.com/documentation/diskarbitration/dadiskrenamecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskRenameCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskRenameCallback = (DADisk, DADissenter?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DADiskUnmount(_: DADisk, _: DADiskUnmountOptions, _: DiskArbitration.DADiskUnmountCallback?, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492758-dadiskunmount)

|  | Declaration |
| --- | --- |
| From | ``` func DADiskUnmount(_ disk: DADisk, _ options: DADiskUnmountOptions, _ callback: DADiskUnmountCallback?, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DADiskUnmount(_ disk: DADisk, _ options: DADiskUnmountOptions, _ callback: DiskArbitration.DADiskUnmountCallback?, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DADiskUnmountApprovalCallback](https://developer.apple.com/documentation/diskarbitration/dadiskunmountapprovalcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskUnmountApprovalCallback = (DADisk, UnsafeMutablePointer<Void>) -> Unmanaged<DADissenter>? ``` |
| To | ``` typealias DADiskUnmountApprovalCallback = (DADisk, UnsafeMutableRawPointer?) -> Unmanaged<DADissenter>? ``` |

Modified [DADiskUnmountCallback](https://developer.apple.com/documentation/diskarbitration/dadiskunmountcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias DADiskUnmountCallback = (DADisk, DADissenter?, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DADiskUnmountCallback = (DADisk, DADissenter?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [DARegisterDiskAppearedCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskAppearedCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492707-daregisterdiskappearedcallback)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskAppearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskAppearedCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskAppearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskAppearedCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskDescriptionChangedCallback(_: DASession, _: CFDictionary?, _: CFArray?, _: DiskArbitration.DADiskDescriptionChangedCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492705-daregisterdiskdescriptionchanged)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskDescriptionChangedCallback(_ session: DASession, _ match: CFDictionary?, _ watch: CFArray?, _ callback: DADiskDescriptionChangedCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskDescriptionChangedCallback(_ session: DASession, _ match: CFDictionary?, _ watch: CFArray?, _ callback: DiskArbitration.DADiskDescriptionChangedCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskDisappearedCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskDisappearedCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492696-daregisterdiskdisappearedcallbac)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskDisappearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskDisappearedCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskDisappearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskDisappearedCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskEjectApprovalCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskEjectApprovalCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492715-daregisterdiskejectapprovalcallb)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskEjectApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskEjectApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskEjectApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskEjectApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskMountApprovalCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskMountApprovalCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492762-daregisterdiskmountapprovalcallb)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskMountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskMountApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskMountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskMountApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskPeekCallback(_: DASession, _: CFDictionary?, _: CFIndex, _: DiskArbitration.DADiskPeekCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492728-daregisterdiskpeekcallback)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskPeekCallback(_ session: DASession, _ match: CFDictionary?, _ order: CFIndex, _ callback: DADiskPeekCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskPeekCallback(_ session: DASession, _ match: CFDictionary?, _ order: CFIndex, _ callback: DiskArbitration.DADiskPeekCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskUnmountApprovalCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskUnmountApprovalCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492698-daregisterdiskunmountapprovalcal)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskUnmountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DADiskUnmountApprovalCallback, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DARegisterDiskUnmountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskUnmountApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DASessionSetDispatchQueue(_: DASession, _: DispatchQueue?)](https://developer.apple.com/documentation/diskarbitration/1501542-dasessionsetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func DASessionSetDispatchQueue(_ session: DASession, _ queue: dispatch_queue_t?) ``` |
| To | ``` func DASessionSetDispatchQueue(_ session: DASession, _ queue: DispatchQueue?) ``` |

Modified [DAUnregisterCallback(_: DASession, _: UnsafeMutableRawPointer, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492712-daunregistercallback)

|  | Declaration |
| --- | --- |
| From | ``` func DAUnregisterCallback(_ session: DASession, _ callback: UnsafeMutablePointer<Void>, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func DAUnregisterCallback(_ session: DASession, _ callback: UnsafeMutableRawPointer, _ context: UnsafeMutableRawPointer?) ``` |

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

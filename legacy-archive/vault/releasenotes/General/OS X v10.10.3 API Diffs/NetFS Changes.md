---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/NetFS.html
archived_at: '2026-07-18T02:52:34.111807Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# NetFS Changes

## NetFS

Added kNAUIOptionAllowUIAdded kNAUIOptionForceUIAdded kNAUIOptionKeyAdded kNAUIOptionNoUIAdded kNetFSAccessRightsKeyAdded kNetFSAllowLoopbackKeyAdded kNetFSAllowSubMountsKeyAdded kNetFSAlreadyMountedKeyAdded kNetFSAlternatePortKeyAdded kNetFSAuthenticationInfoKeyAdded kNetFSAuthorityParamsKeyAdded kNetFSChangePasswordKeyAdded kNetFSConnectedAsGuestKeyAdded kNetFSConnectedAsUserKeyAdded kNetFSConnectedMultiUserKeyAdded kNetFSConnectedWithAuthenticationInfoKeyAdded kNetFSDisplayNameKeyAdded kNetFSForceNewSessionKeyAdded kNetFSGetAccessRightsKeyAdded kNetFSGuestOnlyKeyAdded kNetFSHasPasswordKeyAdded kNetFSHostKeyAdded kNetFSIsHiddenKeyAdded kNetFSMechTypesSupportedKeyAdded kNetFSMountAtMountDirKeyAdded kNetFSMountFlagsKeyAdded kNetFSMountPathKeyAdded kNetFSMountedByGuestKeyAdded kNetFSMountedByKerberosKeyAdded kNetFSMountedByUserKeyAdded kNetFSMountedMultiUserKeyAdded kNetFSMountedURLKeyAdded kNetFSMountedWithAuthenticationInfoKeyAdded kNetFSNoMountAuthenticationKeyAdded kNetFSNoUserPreferencesKeyAdded kNetFSPasswordKeyAdded kNetFSPathKeyAdded kNetFSPrinterShareKeyAdded kNetFSSchemeKeyAdded kNetFSServerDisplayNameKeyAdded kNetFSSoftMountKeyAdded kNetFSSupportsChangePasswordKeyAdded kNetFSSupportsGuestKeyAdded kNetFSSupportsKerberosKeyAdded kNetFSUseAuthenticationInfoKeyAdded kNetFSUseGuestKeyAdded kNetFSUseKerberosKeyAdded kNetFSUserNameKeyModified AsyncRequestID

|  | Declaration |
| --- | --- |
| From | ``` typealias AsyncRequestID = UnsafePointer<()> ``` |
| To | ``` typealias AsyncRequestID = UnsafeMutablePointer<Void> ``` |

Modified NetFSMountURLAsync(CFURL!, CFURL!, CFString!, CFString!, CFMutableDictionary!, CFMutableDictionary!, UnsafeMutablePointer<AsyncRequestID>, dispatch_queue_t!, NetFSMountURLBlock!) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NetFSMountURLAsync(_ url: CFURL!, _ mountpath: CFURL!, _ user: CFString!, _ passwd: CFString!, _ open_options: CFMutableDictionary!, _ mount_options: CFMutableDictionary!, _ requestID: UnsafePointer<AsyncRequestID>, _ dispatchq: dispatch_queue_t!, _ mount_report: NetFSMountURLBlock!) -> Int32 ``` | OS X 10.10 |
| To | ``` func NetFSMountURLAsync(_ url: CFURL!, _ mountpath: CFURL!, _ user: CFString!, _ passwd: CFString!, _ open_options: CFMutableDictionary!, _ mount_options: CFMutableDictionary!, _ requestID: UnsafeMutablePointer<AsyncRequestID>, _ dispatchq: dispatch_queue_t!, _ mount_report: NetFSMountURLBlock!) -> Int32 ``` | OS X 10.8 |

Modified NetFSMountURLCancel(AsyncRequestID) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified NetFSMountURLSync(CFURL!, CFURL!, CFString!, CFString!, CFMutableDictionary!, CFMutableDictionary!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NetFSMountURLSync(_ url: CFURL!, _ mountpath: CFURL!, _ user: CFString!, _ passwd: CFString!, _ open_options: CFMutableDictionary!, _ mount_options: CFMutableDictionary!, _ mountpoints: UnsafePointer<Unmanaged<CFArray>?>) -> Int32 ``` | OS X 10.10 |
| To | ``` func NetFSMountURLSync(_ url: CFURL!, _ mountpath: CFURL!, _ user: CFString!, _ passwd: CFString!, _ open_options: CFMutableDictionary!, _ mount_options: CFMutableDictionary!, _ mountpoints: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Int32 ``` | OS X 10.8 |

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

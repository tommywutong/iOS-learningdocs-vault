---
title: Runtime Configuration Guidelines
apple_id: 10000170i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPRuntimeConfig/Revision-5.2/history.html
archived_at: '2026-07-15T08:16:27.246852Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Runtime Configuration Guidelines](Introduction.md)


[Previous](Additional%20Configuration%20Tips.md)

# Document Revision History

This table describes the changes to _Runtime Configuration Guidelines_.

| __Date__ | __Notes__ |
| 2009-10-19 | Removed deprecated information from the document. |
|  | Moved the reference information for `Info.plist` keys to _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_. |
| 2009-09-09 | Clarified that while a CFBundleIdentifier is similar to a UTI, it is not actually a UTI, as the allowed character set is more restricted. |
| 2009-08-14 | Added links to Cocoa Core Competencies. |
| 2009-05-15 | Added information about keys introduced in OS X v10.6. |
|  | Documented `QuartzGLEnable` key. |
|  | Updated information on version strings to specify that the full three-digit string is required, e.g. 10.4.0. |
| 2008-07-08 | Updated multiplatform information. |
|  | Added `LSRequiresIPhoneOS`, `UIRequiresPersistentWiFi`, `UIStatusBarStyle`, `UIStatusBarHidden`, `UIInterfaceOrientation`, `LSFileQuarantineEnabled`, `LSHandlerRankkeys`. |
| 2007-04-18 | Updated property list keys to include UTI-based keys. Updated configuration guidelines to include Intel-based keys. |
| 2006-11-07 | Reintroduced the CFBundleGetInfoString key and clarified details about the NSAppleScriptEnabled key. |
|  | Added details on the new purpose of the `CFBundleGetInfoString` key. |
|  | Clarified the possible types of the `NSAppleScriptEnabled` key. |
| 2006-09-05 | Added definition of NSPersistentStoreTypeKey. |
| 2006-07-24 | Updated description of the CFBundleVersion and CFBundleShortVersionString keys. |
|  | Undocumented the `CFBundleGetInfoString` key. |
|  | Made minor editorial changes. |
| 2006-04-04 | Updated description of CFBundleIdentifier key. |
| 2005-11-09 | Modified example for LSMinimumSystemVersion key. |
| 2005-08-11 | Updated description of NSPrincipalClass key. Added information about how to put Info.plist data into flat executables. Added environment.plist illustration. |
| 2005-04-29 | Updated for OS X v10.4. |
| 2005-02-03 | Added CFBundleAllowMixedLocalizations key. Removed CFBundleGetInfoHTML key, which was included erroneously and is not supported. |
| 2004-08-31 | Added notes about the correct capitalization of files and directories in a bundle. |
| 2004-04-15 | Minor bug fixes. |
| 2004-01-08 | Minor bug fixes. |
| 2003-12-02 | Minor bug fixes. |
| 2003-08-07 | First version of _Runtime Configuration_. Some of the information in this topic previously appeared in _System Overview_. |

[Previous](Additional%20Configuration%20Tips.md)


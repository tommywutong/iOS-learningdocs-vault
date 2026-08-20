---
title: Fixing the "Audio Unit with Cocoa View" Xcode 3.1.x Template on Mac OS X 10.5.x
  Leopard
apple_id: DTS40009938
resource_type: QA
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: AudioUnit
published: '2010-04-19'
source_url: https://developer.apple.com/library/archive/qa/qa1602/_index.html
archived_at: '2026-07-18T02:32:24.265697Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1602

# Fixing the "Audio Unit with Cocoa View" Xcode 3.1.x Template on Mac OS X 10.5.x Leopard

## Q:  The "Release" build of Audio Units created using the Xcode "Audio Unit Effect with Cocoa View" template does not work. The project builds and runs, but the view displayed is the generic view, not the custom cocoa view. How can I fix this?

A: Important

The fix described __ONLY__ applies to Xcode 3.1.x. Xcode 3.0 users will need to first upgrade to Xcode 3.1.x before continuing with the template update.

If you have already upgraded to Mac OS X 10.6.x and Xcode 3.2.x, this template update is not required and can be ignored.

The problem with the template is that the 'Product Name' setting for the __Release__ build is incorrect.

To fix any __Project__ created with the Audio Unit Effect with Cocoa View template:

1. Select the CocoaUI target residing under the "Targets" tag.
2. Get Info (Cmd+i) on the CocoaUI in the project.
3. Select the Build Tab.
4. Select Debug Configuration.
5. Double click the entry for the 'Product Name' setting (Packaging Section) and copy the string.
6. Choose the Release configuration.
7. Double click the entry for the 'Product Name' setting (Packaging Section) and paste the new string.

The 'Product Name' string for both Debug and Release builds should now look like: `«ORGANIZATIONNAME»«PROJECTNAMEASIDENTIFIER»_CocoaViewFactory`.

To fix the Audio Unit Effect with Cocoa View __Template__ itself, apply the above changes to the following files:

__Xcode 3.1.x:__ `/Developer/Library/Xcode/Project\ Templates/Audio Units/Audio Unit Effect with Cocoa View/StarterAU.xcodeproj`

For convenience, we have included an updated version of the Audio Unit Effect with Cocoa View Template with the fix already applied for download. Simply replace the older template with the one included in the download.

- [Updated version of the Audio Unit Effect with Cocoa View Template for Xcode 3.1.x](https://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/getSoftware?bundleID=20597)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-04-19 | New document that discusses how to fix a bug with the release target of the Audio Unit Effect with Cocoa View Xcode Template on Leopard |


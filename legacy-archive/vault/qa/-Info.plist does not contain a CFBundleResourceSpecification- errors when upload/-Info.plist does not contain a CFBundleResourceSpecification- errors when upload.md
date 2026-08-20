---
title: '"Info.plist does not contain a CFBundleResourceSpecification" errors when
  uploading to iTunes Connect'
apple_id: DTS40009398
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2009-11-23'
source_url: https://developer.apple.com/library/archive/qa/qa1524/_index.html
archived_at: '2026-07-18T02:32:09.779077Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1524

# "Info.plist does not contain a CFBundleResourceSpecification" errors when uploading to iTunes Connect

## Q:  Why does uploading to iTunes Connect give an "Info.plist does not contain a CFBundleResourceSpecification" error?

A: Why does uploading to iTunes Connect give an "Info.plist does not contain a CFBundleResourceSpecification" error?

If you're getting the error message "Info.plist does not contain a CFBundleResourceSpecification" when uploading your application to iTunes Connect for App Store distribution, you may be uploading a Simulator-built version of your application.

Only Device-built applications are allowed in iTunes Connect. Confirm that your project's Active SDK is set to "Device" and not "Simulator" (see Figure 1).

__Figure 1__  Select a 'Device' option for iTunes Connect uploads.

!

The steps for preparing and building your application for App Store distribution are detailed under the "Distribution" section of the [iPhone Developer Program User Guide](https://developer.apple.com/iphone/download.action?path=/iphone/iphone_developer_program_user_guide/iphone_developer_program_user_guide__standard_program_v2.4.pdf).

Be sure to fully test your application on a device prior to uploading to iTunes Connect, as behavior in the Simulator can be dramatically different from on a device.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-11-23 | New document that describes the requirement for uploading "Device"-built versions instead of a "Simulator"-built versions of applications. |


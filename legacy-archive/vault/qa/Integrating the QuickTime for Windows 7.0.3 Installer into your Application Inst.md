---
title: Integrating the QuickTime for Windows 7.0.3 Installer into your Application
  Installer
apple_id: DTS10003875
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-02-07'
source_url: https://developer.apple.com/library/archive/qa/qa1463/_index.html
archived_at: '2026-07-18T02:30:52.698823Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1463

# Integrating the QuickTime for Windows 7.0.3 Installer into your Application Installer

## Q:  How do I integrate the QuickTime for Windows 7.0.3 installer into my application's installer?

A: The new QuickTime 7.0.3 installer is now packaged as a single compressed file. When launched, it will uncompress itself and create a separate process to perform the actual installation, then return control while the installation continues in the background.

Previous versions of the installer were packaged as an uncompressed file. When launched, they would perform the installation and then only return control once the installation was complete.

If your installer relies on the old logic (for example, if you use the InstallShield `LaunchAppAndWait` function to launch the QuickTime installer) we now provide a version of the installer that is packaged as an uncompressed file and behaves exactly as before (by not creating a separate process to perform the installation). You can now download the uncompressed version of the QuickTime for Windows installer [here](http://17.254.17.129/QuickTimeInstaller.exe.zip) (未归档：ZIP 按安全策略跳过).

As before, remember you first need to license QuickTime before you can distribute it with your application, and all QuickTime licensing terms and conditions remain in effect with this version of the installer.

If you have any questions about QuickTime licensing, visit the [Software Licensing](https://developer.apple.com/softwarelicensing/agreements/quicktime.html) web page for complete details. If you have additional licensing questions, please contact Software Licensing at <sw.license@apple.com>.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-02-07 | New document that describes new behavior for the QuickTime for Windows 7.0.3 Installer |


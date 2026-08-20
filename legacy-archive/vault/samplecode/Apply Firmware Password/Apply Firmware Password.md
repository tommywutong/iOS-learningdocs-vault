---
title: Apply Firmware Password
apple_id: DTS10004360
resource_type: Sample Code
platform: macOS
topic: System Administration
technology: null
published: '2007-06-12'
source_url: https://developer.apple.com/library/archive/samplecode/ApplyFirmwarePassword/Introduction/Intro.html
archived_at: '2026-07-18T03:01:11.047258Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AStoObjC-AStoObjC.h.md)

# Apply Firmware Password

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-06-12 First Version |
| __Build Requirements:__ | Xcode Tools 3.0 and Mac OS X version 10.5. |
| __Runtime Requirements:__ | Mac OS X version 10.5 and System Image Utility version 10.5 |

System Administrators can use package installers to customize the deployment workflow created by System Image Utility. While package installers are typically leveraged for software installation, they also function well as shell script containers. Shell scripts have been used for deployments for years, but they tend to make managed mass deployment daunting for less experienced system administrators. This example demonstrates how to build an AppleScript-based, System Image Utility Automator Action that conceals the complexities of a shell-based post-restore task.

This Automator Action includes a shell payload-free package installer. When run, the action will copy the package to /tmp and modify parameters in the postflight script to match user choices. System Image Utility passes an image information dictionary as input to each Automator Action in the workflow. By adding the package's path to the packageList array within this imageInfo dictionary, System Image Utility's Create Image action will copy the referenced package installer into the NetInstall set, and the client will install that package at restore time. The package installer won't actually install anything, but will then run the modified postflight script.

[Next](AStoObjC-AStoObjC.h.md)


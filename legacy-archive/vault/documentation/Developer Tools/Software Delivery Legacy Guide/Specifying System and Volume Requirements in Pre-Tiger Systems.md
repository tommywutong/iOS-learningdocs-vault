---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Legacy_Requirements/Legacy_Requirements.html
archived_at: '2026-07-15T07:26:54.725772Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Prebinding%20Applications.md)[Previous](Performing%20Remote%20Installs.md)

# Specifying System and Volume Requirements in Pre-Tiger Systems

JavaScript-based system and volume requirements are not supported on Pre-Tiger systems. To check installation requirements in computers running Mac OS X v10.2 or v10.3, you must use executable-based installation requirements. These installation requirements rely on two executable files that you create and include in an installation package.

You specify system and volume requirements using executables named `InstallationCheck` and `VolumeCheck`, respectively. These executables can be binary files or text-based scripts.

This chapter shows how to define executable-based installation requirements.

During the installation process, the Installer application invokes `InstallationCheck` and `VolumeCheck` when it needs to check system and volume requirements, respectively. See [The Installation Process](Managed%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnrnknltcma) for details.

The `InstallationCheck` executable can use any criteria to allow or disallow an install. It returns a value that tells Installer whether to continue the installation process.

Similarly, `VolumeCheck` can use any criteria to accept or reject a volume as a potential installation volume. The return value of `VolumeCheck` tells Installer whether to allow the user to choose a particular volume as an installation destination.

In addition to stopping the installation process and disallowing volumes to be chosen as installation volumes, the return values of these executables tell Installer which informational message to display to the user. You use strings files to define these informational messages.

When `InstallationCheck` cancels an install or when `VolumeCheck` disallows a volume to be chosen as the installation volume, the Installer application displays a default message or the message specified by the executable’s return value. To specify your own messages, place the files `InstallationCheck.strings` and `VolumeCheck.strings` (for system requirement and volume requirement failure messages, respectively) in a localized directory inside the package’s scripts directory. Table A-1 shows the directory names for the languages Installer recognizes.

__Table A-1__  Localized directories

| `Dutch.lproj` |
| `English.lproj` |
| `French.lproj` |
| `German.lproj` |
| `Italian.lproj` |
| `Japanese.lproj` |
| `Spanish.lproj` |
| `da.lproj` |
| `fi.lproj` |
| `ko.lproj` |
| `no.lproj` |
| `pt.lproj` |
| `sv.lproj` |
| `zh_CN.lproj` |
| `zn_TW.lproj` |

A strings file defines messages in the following format:

```
"<message_ID>" = "<message_string>";
```

- `<message_ID>`: Integer between 16 and 31.
- `<message_string>`: Informational message string.

Listing A-1 and Listing A-2 show sample `InstallationCheck.strings` and `VolumeCheck.strings` files, respectively.

__Listing A-1__  A sample `InstallationCheck.strings` file

```
"16" = "Can't install unless you have a Super Drive.";
"17" = "Can’t install unless you have more than 128MB of RAM.";
```


__Listing A-2__  A sample `VolumeCheck.strings` file

```
"16" = "Can't install on volumes named Panther.";
"17" = "Can’t install on volumes named Jaguar.";
```


The `InstallationCheck` executable returns an integer that the Installer application uses to determine whether to proceed with the installation process or which informational message to display as the reason for canceling the install. To allow the install, return `0`. To cancel the process, return an integer that specifies the message ID of the localized message to display. This integer, however, must also have bits 5 and 6 set to `1`.

For example, to instruct Installer to display message 16, return `112`. You can use the Calculator application to determine the correct return value for a specific message ID, or compute it in your executable.

Table A-2 lists the message IDs of the default messages for `InstallationCheck` failures. If you use these messages, you don’t need to create an `InstallationCheck.strings` file.

__Table A-2__  Installer default messages for `InstallationCheck` failures

| Message ID | Message string |
| `1` | This software cannot be installed on this computer. |
| `2` | The software <package_name> cannot be installed on this computer. |
| `3` | <package_name> cannot be installed on this computer. |
| `4` | An error was encountered while running the InstallationCheck tool for package <package_name>. |

The `VolumeCheck` executable returns an integer that the Installer application uses to determine whether to allow the user to choose a volume as the installation volume and which informational message to display when the user selects a disallowed volume. Returning `0` allows the user to identify a volume as the installation volume. When a volume doesn’t meet the volume requirements, the `VolumeCheck` return value specifies the message ID of the localized message to display when the user selects the volume. This integer, however, must also have bit 5 set to `1`.

For example, to disallow a volume and set the message ID of the appropriate message to `17`, return `49`. You can use the Calculator application to determine the correct return value for a specific message ID, or compute it in your executable.

Table A-3 lists the message IDs of the default messages for volumes that fail `VolumeCheck`. If you use these messages, you don’t need to create a `VolumeCheck.strings` file.

__Table A-3__  Installer default messages for `VolumeCheck` failures

| Message ID | Message string |
| `0` | You cannot install this software on this disk. You are not allowed to install the software on this disk for an unknown reason. |
| `1` | You cannot install this software on this disk. Could not find specified message for index 1. |
| `2` | You cannot install this software on this disk. An error was encountered while running the VolumeCheck tool for package <package_name>. |

[Next](Prebinding%20Applications.md)[Previous](Performing%20Remote%20Installs.md)


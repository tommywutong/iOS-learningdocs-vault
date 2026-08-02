---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Install_Operations/Install_Operations.html
archived_at: '2026-07-15T07:26:54.711879Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Performing%20Remote%20Installs.md)[Previous](Defining%20a%20Managed%20Install.md)

# Specifying Install Operations

In managed installs, install operations allow you to configure the destination environment before the payload is copied to the file system and to perform additional processing afterward. To specify install operations, you use executable files (known as _install operation executables_) that Installer invokes at specific stages during an install, as described in [The Installation Process](Managed%20Installs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqnrnknltcma).

Install operation executables must be named according to the install operation you want to define. The files can be binary files or text files containing shell scripts. All install operations are optional. You define only the operations required by a packaged product.

This chapter shows how you use install operation executables to define the install operations the Installer application performs in a managed install.

After the Installer application finishes checking installation requirements, it performs an install through distinct operations, known as _install operations_. You can define all but one of these operations, which copy payloads to their installation destinations. You should not use install operations to fix install problems, such as incorrect ownership and access permissions. You should use install operations only when other managed-install features, such as installation requirements, are not adequate for the chore you need to perform as part of installing a package or metapackage.

Table 7-1 lists the install operations in the order Installer performs them.

__Table 7-1__  Install operations and executables

| Install operation | Operation executable | Description |
| Preflight | `preflight` | Prepares the target system for the install; for example, quitting or stopping specific applications or processes. |
| Preinstall | `preinstall` | Prepares the target system for a payload for which no receipt is found. |
| Preupgrade | `preupgrade` | Prepares the target system for a payload for which a receipt is found. |
| Payload Drop | None | Copies the payload to the installation destination. This operation is not modifiable. |
| Postinstall | `postinstall` | Cleanup or system setup for an installed payload. |
| Postupgrade | `postupgrade` | Cleanup or system setup for an upgraded payload. |
| Postflight | `postflight` | Install postprocessing; for example, setting up `cron(8)` jobs or launching the installed application. |

The first three install operations, Preflight, Preinstall, and Preupgrade, can stop an install. When one of the corresponding executables returns anything other than `0`, Installer cancels the install.

The following list describes the arguments and environment variables available to install operation executables. Note that not all environment variables are available to all executables (see [Table 7-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmjvfvbuqmjufvjvomy)).

- `$1`: Full path to the installation package the Installer application is processing. For example:

```
/Volumes/Users/michelle/Desktop/Levon.mpkg
```
- `$2`: Full path to the installation destination. For example:

```
/Applications
```
- `$3`: Installation volume (or mountpoint) to receive the payload. For example:

```
/
/Volumes/Tools
```
- `$4`: The root directory for the system:

```
/
```
- `$SCRIPT_NAME`: Filename of the operation executable. For example:

```
preflight
```
- `$PACKAGE_PATH`: Full path to the installation package. Same as `$1`.
- `$INSTALLER_TEMP`: Scratch directory used by Installer to place its temporary work files. Install operations may use this area for their temporary work, too, but must not overwrite any Installer files. The Installer application erases this directory at the end of the install. For example:

```
/private/tmp/.Levon.pkg.897.install
```
- `$RECEIPT_PATH`: Full path to a temporary directory containing the operation executable. This is a subdirectory of `$INSTALLER_TEMP`. This location may vary between installs. The executable can use this path to locate other files in the package. For example:

```
/private/tmp/.Levon.pkg.897.install/Receipts/Levon.pkg/Contents/Resources
```

The four arguments described earlier are available to all install operations. Table 7-2 shows the availability of the environment variables.

__Table 7-2__  Environment variables in operation executables

| Operation executable | Available environment variables |
| `preflight` | None. |
| `preinstall`, `preupgrade` | `$SCRIPT_NAME`, `$PACKAGE_PATH`, `$INSTALLER_TEMP`. |
| `postinstall`, `postupgrade`, `postflight` | `$SCRIPT_NAME`, `$INSTALLER_TEMP`, `$PACKAGE_PATH`, `$RECEIPT_PATH`. |

Listing 7-1 shows a postflight operation implemented as a shell script that launches an installed application.

__Listing 7-1__  Sample install operation script

```
#!/bin/sh
echo $SCRIPT_NAME: launching Levon.app
open -b com.mycompany.Levon
exit 0
```

After Installer executes this install operation script, its log shows an entry similar to the one in Listing 7-2.

__Listing 7-2__  Sample Installer log entry

```
Jun 20 13:30:03 Athene : postflight[2274]: postflight: launching Levon.app
```

[Next](Performing%20Remote%20Installs.md)[Previous](Defining%20a%20Managed%20Install.md)


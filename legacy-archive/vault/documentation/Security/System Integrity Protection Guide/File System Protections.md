---
title: System Integrity Protection Guide
apple_id: TP40016462
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: Security
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/System_Integrity_Protection_Guide/FileSystemProtections/FileSystemProtections.html
archived_at: '2026-07-18T02:06:31.629107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [System Integrity Protection Guide](Introduction.md)


[Next](Runtime%20Protections.md)[Previous](Introduction.md)

# File System Protections

When system files are installed, they are marked with a special flag to protect against modification. Any attempts to modify protected files or directories are denied by the kernel unless that attempt is made by a system process signed with Apple’s code signing identity. This includes any attempts to write to a block device that backs protected content or mount a device over a protected directory.

The following directories can only be written to by the system:

__System-Only Locations__

- `/bin`
- `/sbin`
- `/usr`
- `/System`

In contrast, the following directories are available to any process:

__Locations Available to Developers__

- `/usr/local`
- `/Applications`
- `[~]/Library`

All directories in `/usr` except for `/usr/local` are restricted to the system. Apple app directories in `/Applications` are restricted to the system.

When upgrading to a version of macOS that supports System Integrity Protection, the system migrates any existing third-party content as part of its installation process. The installer takes the existing system, moves it to a temporary location, and writes the new system to the root volume.

As soon as the new system is written, the installer traverses the existing system locations for third-party files and, for each path, determines whether they can be written to the new system. If so, the path is moved to the new system. If not, the path is moved to `/Library/SystemMigration/History/Migration-<UUID>/QuarantineRoot/`.

Developers using Perl, Python, Ruby, or any other scripting languages that ship with macOS, are encouraged to manage their own installations of the language and dependencies in `/usr/local/`. When distributing programs written with a scripting language, developers are encouraged to bundle the language runtime and any required components into a self-contained binary.

[Next](Runtime%20Protections.md)[Previous](Introduction.md)


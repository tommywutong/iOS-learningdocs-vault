---
title: System Integrity Protection Guide
apple_id: TP40016462
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: Security
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/System_Integrity_Protection_Guide/ConfiguringSystemIntegrityProtection/ConfiguringSystemIntegrityProtection.html
archived_at: '2026-07-18T02:06:31.593582Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [System Integrity Protection Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Kernel%20Extensions.md)

# Configuring System Integrity Protection

Security configuration is stored in NVRAM rather than in the file system itself. As a result, this configuration applies to all installations of macOS across the entire machine and persists across macOS installations that support System Integrity Protection.

System Integrity Protection can be configured using the `csrutil(1)` command.

You can check whether System Integrity Protection is currently enabled on your system by running the following command in the Terminal:

```
$ csrutil status
System Integrity Protection status: enabled.
```

To enable or disable System Integrity Protection, you must boot to Recovery OS and run the `csrutil(1)` command from the Terminal.

1. Boot to Recovery OS by restarting your machine and holding down the Command and R keys at startup.
2. Launch Terminal from the Utilities menu.
3. Enter the following command:

   `$ csrutil enable`

After enabling or disabling System Integrity Protection on a machine, a reboot is required.

[Next](Document%20Revision%20History.md)[Previous](Kernel%20Extensions.md)


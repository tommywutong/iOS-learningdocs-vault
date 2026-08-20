---
title: System Integrity Protection Guide
apple_id: TP40016462
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: Security
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/System_Integrity_Protection_Guide/KernelExtensions/KernelExtensions.html
archived_at: '2026-07-18T02:06:31.718646Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [System Integrity Protection Guide](Introduction.md)


[Next](Configuring%20System%20Integrity%20Protection.md)[Previous](Runtime%20Protections.md)

# Kernel Extensions

A kernel extension, or _kext_, is a bundle that extends the kernel. With System Integrity Protection, kernel extensions must be signed with a Developer ID for Signing Kexts certificate, and installed into the `/Library/Extensions` directory.

As of macOS El Capitan, the `kext-dev-mode` boot-arg is now obsolete.

```
$ sudo nvram boot-args="kext-dev-mode=1" # Has No Effect
```

You can build unsigned kexts for internal testing, and disable System Integrity Protection on your test systems to allow unsigned kexts to load. See [Configuring System Integrity Protection](Configuring%20System%20Integrity%20Protection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinrsfvbuqnjnknltc) for more information.

You should sign a kernel extension using a Developer ID certificate only when it reaches its final stages of testing and is being evaluated for release to customers. You can request a Developer ID Certificate for signing kexts by visiting [https://developer.apple.com/contact/kext](https://developer.apple.com/contact/kext) and filling out the required details.

For more information, see [Kernel Extension Overview](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Extend/Extend.html#//apple_ref/doc/uid/TP30000905-CH220) in _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_.

[Next](Configuring%20System%20Integrity%20Protection.md)[Previous](Runtime%20Protections.md)


---
title: Kernel Extensions Release Notes
apple_id: TP40001023
resource_type: Release Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-04-28'
source_url: https://developer.apple.com/library/archive/releasenotes/Darwin/RN-KernelExtensions/index.html
archived_at: '2026-07-18T02:50:23.151183Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Kernel, Kernel Extensions, and I/O Kit Release Notes for OS X Snow Leopard

OS X Snow Leopard features a 64-bit kernel and a rewritten infrastructure for kernel extensions (kexts), with enhancements covering many aspects of kext development, from the linker up to the command-line tools. The underlying kext architecture has been thoroughly redesigned for better performance and flexibility, as well as support for 64-bit kexts. In the process of updating the kernel and kext environment, however, changes had to be made to the kernel programming interfaces, which may require some porting work for 32-bit kexts as well as 64-bit kexts.

__Important:__ There are no guarantees of binary or run-time compatibility between seeds. Be sure to rebuild all of your Snow Leopard kexts on this seed before loading them.

#### Contents:

- [Release Notes for Late April 2009](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamrtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Release Notes for April 2009](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamrtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Release Notes for March 2009](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamrtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Release Notes for November 2008](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamrtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjr)

### Release Notes for Late April 2009

This seed corrects an issue with the prelinked kernel, in which attaching a new device would significantly delay or stall startup.

Kernel extensions with binary `Info.plist` files are not recognized for loading from user space on OS X Snow Leopard; all kext plists must now be XML. On prior releases, kexts with binary plists have never been recognized by the booter or kernel, but happened to be loadable from user space due to the use of the Core Foundation plist parser. This caused some loading and debugging issues with XML that the kernel/IOKit XML parser couldn’t handle, so now all kext plists are processed with the same parser in both kernel and user space.

Kext authentication now ignores `.DS_Store` files. `.DS_Store` files are not available for resource download via `OSKextRequestResource()`.

### Release Notes for April 2009

On OS X Snow Leopard, kernel logging output is saved to the file `/var/log/kernel.log` rather than `/var/log/system.log`. Be sure to check both log files for relevant messages when debugging kernel extensions and kernel extension loading.

`kauth_cred_self()` was incorrectly listed in the new KPI tables. The correct name is `kauth_cred_get()`. The KPI tables have been updated to reflect this.

### Release Notes for March 2009

### Loading Kexts from C Code; Non-Root Loading

`kextload(8)` now sends an RPC load request to `kextd(8)`. You can load kexts from C code using these RPCs as well. Check out `<IOKit/kext/KextManager.h>` for `KextManagerLoadKextWithIdentifier()` and `KextManagerLoadKextWithURL()`.

Further, `kextload(8)` and these RPCs can be invoked as a non-root user for kexts:

- That define a boolean `OSBundleAllowUserLoad` property with a `true` value. (Note that there's a typo in the man page naming `OSKextAllowUserLoad`.)
- That are installed anywhere under `/System/`.
- Whose dependencies, direct and indirect, also do both of the above. `System.kext` and its plugins already define `OSBundleAllowUserLoad`, but no families do yet—and since I/O Kit drivers are loaded by `kextd(8)` on demand from the kernel, it’s unlikely they will add `OSBundleAllowUserLoad`.

Please enable non-root load for your kexts with some care and only if necessary for addressing security issues (such as avoiding a setuid binary on the system).

`kextunload(8)` and `kextutil(8)` still have to be run as root, for security concerns and because they communicate directly with the kernel.

### Autounload for BSD Kexts

BSD kexts can now enable and manage autounload for themselves via reference counting; see the Kernel framework’s `<libkern/OSKextLib.h>` for the functions `OSKextRetainKextWithLoadTag()` and `OSKextReleaseKextWithLoadTag()`. For example, if you have a filesystem kext, it can retain itself on each mount, and release itself on each unmount.

As noted elsewhere, BSD kexts can now safely use Libkern C++ classes without inadvertently triggering autounload (as has been the case on every prior release of OS X). Autounload used to be enabled on load for any kext that defined a subclass of OSObject; it is now enabled only when a kext defines a subclass of IOService. If you do define any IOService subclasses, your kext is still subject to autounload; you should either make sure an instance of one of those subclasses exists, or use the kext retain/release mechanism, as appropriate.

### Resource File Downloads

Brand new in this seed is a built-in facility for kexts to get resource files from their bundles while running in the kernel. See <libkern/OSKextLib.h> for `OSKextRequestResource()` and related functions. The intent is to allow I/O Kit drivers to get firmware blobs out of their personalities, so they don't sit around consuming wired kernel memory all the time. Note that resource downloads are performed by `kextd(8)`, so any requests made during early boot won't be fulfulled until `kextd(8)` starts.

### Developer Loading with kextutil

As detailed below `kextload(8)` no longer accepts development options. Use `kextutil(8)` for all development loading, symbol generation, and other testing.

### Final Classes

The Snow Leopard kext linker now supports final classes—classes that can't be subclassed by another kext (you can still subclass them within the same kext). To declare a class final, use the macros `OSDeclareFinalStructors()` and `OSDefineMetaClassAndFinalStructors()` from the Kernel framework’s `<libkern/c++/OSMetaClass.h>`.

Changing a class to use a final declaration breaks binary compatibility, so don't make a currently shipping library kext’s classes final if you expect other shipping kexts to link against it.

### Kext-Related Mach Error Codes

The Mach error codes for the new in-kernel kext system now have `mach_error_string` values set.

### Verbose Logging in User and Kernel Space

The kext logging engine has been completey redone, so kext tool output is hopefully less crammed with irrelevant message, but they do print to the terminal information that was normally only logged from the kernel direct to the console. This, combined with the new `mach_error_string` values, should make failure causes within the kernel more apparent.

The kext tools now don't log anything by default if the operation succeeds. Using `-v` turns on additional logging, but log messages about particular kexts are only printed if the kext itself has an `OSBundleEnableKextLogging` property (see below on overriding). The `-v` levels have been adjusted somewhat, but each still includes every previous level:

- 0: Errors only (= 0xff1 below)
- - (`-v` not specified): The default level includes warnings and errors (= 0xff2 below)
- 1: Basic outcome (= 0xff3 below)
- 2: Operation progress (= 0xff4 below)
- 3: Individual steps (typically each kext) (= 0xff5 below)
- 4: Details (= 0xff6 below)
- 5: Debug info (= 0xff7 below)
- 6: Debug info for all kexts (regardless of OSBundleEnableKextLogging) (= 0xfff below)

You can also specify logging to very fine detail using a 32-bit hexadecimal logging specification. In short, the bottom nibble, the last hex digit from 0–7, is the (internal) log level, which is generally 2 greater than the equivalent nonzero `-v` level from the list above. Setting the high bit of this nibble causes messages for all kexts to be logged as appropriate for the level, regardless of `OSBundleEnableKextLogging`. All bits above the bottom nibble are flags for various kinds of activity. The bottom 2 nibbles of the flags are for typical developer-relevant things like load operations, IPC, and archive creation/processing. The higher-order nibbles are for operations more relevent to the internals of the kext library. To see completely verbose logging, try `-v 0xffffffff`.

You can set logging for the kernel as well using the kextlog boot-arg/sysctl and the hexadecimal spec. These commands turn on kernel kext logging for the next restart, or immediately:

```
sudo nvram boot-args="-v kextlog=0xff4"
sudo sysctl -w debug.kextlog=0xff4
```


### Release Notes for November 2008

### 64-Bit Kernel and Kernel Extensions

The early 2008 models of the Mac Pro, 20" and 24" iMac, 15" and 17" MacBook Pro, and Xserve can be used for 64-bit kernel development. Audio and AirPort are now enabled on these testing conﬁgurations. In Snow Leopard, the 64-bit kernel is used by default on Xserve. Mac Pro and MacBook Pro systems can be booted into the 64-bit kernel in one of two ways:

- Temporarily boot into the 64-bit kernel by holding down "6" and "4" while powering on the machine.
- Run `sudo nvram boot-args="arch=x86_64"` to set the 64-bit kernel as your default kernel, and append any other debugging ﬂags you may need, such as `debug=0x144`. To revert back to the 32-bit kernel as the default, you can run `sudo nvram -d boot-args` to clear the boot args, or set `boot-args` without `arch=x86_64`.

This seed contains the necessary support for porting kexts to 64-bit, and developers are strongly encouraged to do so.

Known Limitations in the 64-bit kernel:

- Shark does not work on the 64-bit kernel.
- Sleep/wake and power management are not currently supported. It is recommend that you disable sleep in System Preferences.
- Graphics acceleration is not yet supported which may cause programs which require graphics acceleration to run incorrectly.
- Some behavior which was previously unsupported, such as modifying an OSCollection while enumerating it, and attempting to modify a kext's __TEXT segment, now results in diagnostic kernel panics.

### Changes to Kernel Extensions & Tools

### Changes to Kext Tools

Most kext tools have been rewritten on OS X Snow Leopard with support for long options, improved logging, and various other enhancements. The major changes to the tools are the deprecation of `kextload(8)` as a developer tool and support for cross-architecture work on kexts.

The `kextload(8)` tool has been reduced to the essential functionality required for production loading of kernel extensions. A new tool, `kextutil(8)`, now handles developer functionality. As of this seed, `kextload` no longer accepts developer options and supports only `-b`, `-d`, `-h`, `-q`, `-r`, `-v`, and their long equivalents; `-c`, `-D`, and `-t` will be accepted but ignored. See the man pages for details.

`kextutil(8)` features a `-arch` flag to generate symbols for an architecture other than that of the running kernel, enabling cross-architecture debugging of kexts. Mach-O layout should automatically work when generating symbols for Leopard and earlier releases.

Snow Leopard uses new versions of the mkext and prelinked kernel files, which are not recognized by earlier releases of OS X. Earlier releases will not be able to update Boot≠Root volumes with Snow Leopard installed, but Snow Leopard can update Boot≠Root volumes with earlier releases. `kextcache` includes new options to generate mkext files in both old and new formats, and like `kextutil` now features a `-arch` flag; it no longer generates old-format prelinked kernels.

### Debugging Kernel Extensions

The general procedure for debugging kernel extensions remains the same as on OS X Leopard. Here are the notable differences:

- Use the Snow Leopard version of `gdb` to debug Snow Leopard kexts.
- Use `kextutil(8)` to generate debug symbols.
- Always specify the architecture explicitly via the `-arch` flag when generating symbols or starting the debugger. This is particularly important for `gdb`, as it uses the `x86_64` architecture by default.

For example, if you want to generate 64-bit symbols for AppleFWOHCI.kext, and have installed the Kernel Debug Kit, you might use this command (all one line):

```
kextutil -n -z -e -r /Volumes/KernelDebugKit -k /Volumes/KernelDebugKit/mach_kernel -arch x86_64 \
    -a com.apple.driver.AppleFWOHCI@0xffffff7f80830000 -a com.apple.iokit.IOPCIFamily@0xffffff7f80604000 \
    -a com.apple.iokit.IOFireWireFamily@0xffffff7f807e6000 -s /tmp/syms -- /tmp/syms/AppleFWOHCI.kext
```

The options used are:

- `-n` — Don’t load into the kernel.
- `-z` — Don’t authenticate extensions (no longer needed on Snow Leopard when using `-n`, but necessary on older releases)
- `-e` — Don’t look in `/System/Library/Extensions` for dependencies or bundle identifiers
- `-r` — Look in `/Volumes/KernelDebugKit` for dependencies and bundle identifiers
- `-arch` — Use executables for the named architecture
- `-a` — Link as if the kext with the named identifier is loaded at the given address
- `-s` — Save symbol files to this directory
- `---` — End of options; everything after this is a kext name

In your `gdb` session, you use the add-kext command like so:

```
(gdb) add-kext /tmp/syms/AppleFWOHCI.kext
```

In addition, FireWire debugging is now built in to the system. To use FireWire debugging:

1. Enable FireWire kdp on the target machine in `boot-args`. For example: `sudo nvram boot-args="debug=0x146 kdp_match_name=firewire"`.
2. Restart the machine.
3. On the host machine, run the `fwkdp` command.
4. In a second terminal window, run gdb on the appropriate kernel file and attach; for example:

```
gdb -arch x86_64 /Volumes/KernelDebugKit/mach_kernel
source /Volumes/KernelDebugKit/kgmacros
kdp-reattach localhost
```

Note that with kdp you always attach to `localhost` and not the actual hostname of the target; `fwkdp` forwards the `gdb` packets between the host and the target.

For more information on FireWire debugging, consult the `fwkpfv` and `fwkdp(1)` man pages.

### 64-Bit Kernel Extensions

OS X Snow Leopard introduces a 64-bit kernel and support for writing 64-bit kernel extensions. The major change that affects 64-bit kexts is that the `com.apple.kernel*` libraries are not available; 64-bit kexts must use `com.apple.kpi.*`. Private KPI has been moved from the `com.apple.kpi.unsupported` kext to `com.apple.kpi.private`; third-party kexts should not use this KPI, as it will become unavailable for linkage by the final release of Snow Leopard.

64-bit kexts have a new Mach-O filetype (KEXTBUNDLE rather than OBJECT, as reported by `otool`).

See later in this document for information on porting kexts the 64-bit kernel environment.

### Installing Kernel Extensions

OS X Snow Leopard requires all directories and files within a kext bundle, except for the contents of the PlugIns folder (which technically contains distinct bundles that need not be kexts), to be owned by root:wheel and not to be writable by group or other. On prior releases this is the documented behavior, but the actual behavior has been to check only the bundle’s Info.plist and executable file and the directory nodes between them and the kext bundle itself. Installers that include resources or other files with different ownership or permissions should be updated to ensure correct protections on all component directories and files of kext bundles.

The recommended way to update kext caches following installation or update is still to update the modification time of `/System/Library/Extensions/` and then send a SIGHUP to kextd (both as the superuser):

```
touch /System/Library/Extensions
/bin/kill -1 `ps -ax | awk '{print $1" "$5}' | grep kextd | awk '{print $1}'`
```

On Leopard and Snow Leopard, the SIGHUP is optional. When `/System/Library/Extensions/` is touched, all kext caches except for the prelinked kernel are updated automatically after a short delay; the prelinked kernel is updated after the next restart. For more information, particularly with regard to installing on older releases of OS X, see [Technical Q&A QA1319: Installing an I/O Kit KEXT Without Rebooting](https://developer.apple.com/qa/qa2001/qa1319.html).

### Architecture-Specific Properties

On OS X Snow Leopard, when the kext management stack looks up a top-level kext bundle property, it checks first for the property name corresponding to the current architecture. Such a property name adds to the basic name an underscore followed by the architecture name; architecture-specific values for `OSBundleLibraries`, for example, can be set as `OSBundleLibraries_i386` and `OSBundleLibraries_x86_64`. (Note that the architecture name corresponds to the cputype only and never the cpusubtype.) By defining architecture-specific properties you can specify different sets of libraries to use when loading on different architectures, with different versions if necessary, via `OSBundleLibraries`; different I/O Kit personalities to use for matching via `IOKitPersonalities`; and different requirements for early loading with `OSBundleRequired`.

If your driver is not built fully universal, it's highly recommended that you use architecture-specific personalities to prevent spurious load requests.

The architecture used is by default that of the running kernel, but many of the kext tools allow you to specify the architecture with the `-arch` flag, as when generating debug symbols.

Note that architecture-specific properties are a feature of the kext management stack, and not of CFBundle. Only properties defined by the kext system and I/O Kit—specifically those beginning with `OSBundle…`, `OSKernel…`, and `IO…`—use architecture-specific variants.

### Mixed C/C++ Kexts

OS X Snow Leopard features support for kexts that use both C and C++ code. On prior releases of OS X, making use of Libkern C++ classes in a generic (C-based) kext was a risky proposition, since the I/O Kit auto-unloading mechanism destroyed any kext referencing such classes if there were no instances of them. Apart from that, even if non-Libkern C++ was used, the stub routine invoked at unload called the kext’s static C++ destructors before the kext’s stop routine, and when the kext was auto-unloaded the stop routine wasn’t invoked at all.

Snow Leopard corrects these issues by:

- Marking only kexts that define subclasses of IOService for auto-unload. Non-I/O Kit kexts loaded on Snow Leopard can safely use and subclass Libkern C++ classes.
- Altering the stub unload routine to call the kext’s stop routine first, then the kext’s static C++ destructors. __Important:__ To gain this behavior you must build your kext to be targeted against Snow Leopard, as the stub routine is built into the kext.
- Always unloading a kext by calling both the stop routine and then the C++ static destructors, regardless of kext type (generic or I/O Kit).

### Internal Changes

### Kext Caches on Snow Leopard

Kext caches on OS X Snow Leopard—including the prelinked kernel, mkext, and kext property caches—now all reside within the `/System/Library/Caches/com.apple.kext.caches/` folder. As mentioned above, installers and updaters need only update the modification time of `/System/Library/Extensions/` to ensure that the caches are rebuilt, and should make no assumptions about the locations of kext caches.

### Deprecation of kmod_… Interfaces

Due to significant changes to the kext loading and bookkeeping systems in the kernel, OS X Snow Leopard has removed nearly all `kmod_…` functions (MIG routines remain for user-space binary compatibility but most now return `KERN_UNSUPPORTED`). The linked list of `kmod_info` structs is also no longer exported. Kext start and stop routines are still passed a pointer to the kext’s `kmod_info` struct, but kexts should consider only the `name`, `version`, `id` (also known as the load tag or index), `address`, `size`, and `info_version` fields as valid. The remaining fields of the`kmod_info` struct may cease to be used by the final release of Snow Leopard or by a later release of OS X.

Please contact Developer Technical Support with any questions regarding this matter.

### Changes to Kernel Programming Interfaces (KPIs)

### Deprecated and New KPIs

This seed removes many symbols from the headers and KPIs for both 32- and 64-bit kernel extensions. In the 64-bit KPIs, we have consolidated the interfaces, removing functions with duplicate functionality and retaining the more sustainable of them. Some KPIs have minor alterations to make them more sustainable. A handful have been removed that were never in use and did not belong to the model of their subsystems.

Note that the compatible versions of 32-bit KPIs have not changed; removal of unsupported symbols is sufficient to prevent kexts referencing them from loading. If your kext fails to build because of symbols removed from headers, or fails to link because of symbols removed from symbol sets, please consult the Supported KPI documents in `/System/Library/Frameworks/Kernel.framework/Resources/` and the headers in `Kernel.framework` for replacements and update your kext accordingly. If no replacement is available for a symbol your kext has been linking against, please file a bug and contact Developer Technical Support.

PC Card support (the IOPCCardFamily.kext and headers) has been removed from OS X Snow Leopard.

A large number of new KPIs are available, particularly in 64-bit I/O Kit. Consult the rest of these release notes, the supported KPI documents in `/System/Library/Frameworks/Kernel.framework/Resources/` for full lists of symbols on all architectures, and the headers in `Kernel.framework` relevant to your kext for headerdoc comments.

Two symbols deserve special note here:

```
ucred_t     // legacy type removed, use kauth_cred_t instead
vfs_context // opaque and this time it is mandatory for K64; there is no private header exported
```


### KPI Changes for 64-Bit Kexts

All Apple-provided I/O Kit families, except for IOPCCardFamily.kext, are available for 64-bit kernel extensions in this Seed.

### I/O Kit KPI Changes

In general, using deprecated I/O Kit KPIs will result in a build warning, and you can consult the class documentation to see what has changed. The two major changes summarized here are to `IOCreateThread`, and `IOMemoryDescriptor`; otherwise, most changes are to internal KPIs.

`IOCreateThread` is deprecated for 64-bit kexts. `kernel_thread_start` should be used instead. Make sure to release the reference to the `thread_t` by calling `thread_deallocate`. `IOExitThread` can be replaced by a call to `thread_terminate(current_thread())`.

Changes to IOMemoryDescriptor and related classes are summarized here:

| Not supported in 64-Bit | Recommended |
| --- | --- |
| `IOMemoryDescriptor::getPhysicalSegment64()` | `IOMemoryDescriptor::getPhysicalSegment(kIOMemoryMapperNone)` |
| `IOMemoryDescriptor::getVirtualSegment()` | `IOMemoryDescriptor::map()->getVirtualAddress()` |
| - `IOMemoryDescriptor::initWithAddress(void *)` - `IOMemoryDescriptor::initWithAddress(task_t)` - `IOMemoryDescriptor::initWithPhysicalAddress()` - `IOMemoryDescriptor::initWithPhysicalRanges()` - `IOMemoryDescriptor::initWithRanges()` | `IOMemoryDescriptor::initWithOptions()` |
| `IOMemoryDescriptor::map(task_t)` | `IOMemoryDescriptor::createMappingInTask()` |
| `IOMemoryDescriptor::withAddress(task_t)` | `IOMemoryDescriptor::withAddressRange()` |
| `IOMemoryDescriptor::withPhysicalRanges()` | `IOMemoryDescriptor::withOptions(kIOMemoryTypePhysical)` |
| `IOMemoryDescriptor::withRanges()` | `IOMemoryDescriptor::withOptions(kIOMemoryTypeVirtual)` |
| `IOMemoryDescriptor::withSubRange()` | `IOSubMemoryDescriptor::withSubRange([kIOMemoryThreadSafe])` |
| `IOBufferMemoryDescriptor::initWithBytes()` | `IOBufferMemoryDescriptor::initWithPhysicalMask()` |
| `IOBufferMemoryDescriptor::initWithOptions(void *)` | `IOBufferMemoryDescriptor::initWithPhysicalMask()` |
| `IOBufferMemoryDescriptor::initWithOptions(task_t)` | `IOBufferMemoryDescriptor::initWithPhysicalMask()` |

Subclasses of `IOMemoryDescriptor` further have these changes:

| Not supported in 64-Bit | Recommended |
| --- | --- |
| `IOMemoryDescriptor::getPhysicalSegment()` | `IOMemoryDescriptor::getPhysicalSegment(IOOptionBits)` |
| - `IOMemoryDescriptor::getPhysicalSegment64()` - `IOMemoryDescriptor::initWithAddress(void *)` - `IOMemoryDescriptor::initWithAddress(task_t)` - `IOMemoryDescriptor::initWithPhysicalAddress()` - `IOMemoryDescriptor::initWithPhysicalRanges()` - `IOMemoryDescriptor::initWithRanges()` | — |

### Mach KPI Changes

All KPIs that utilize struct `mach_timespec` or `mach_timespec_t` are deprecated, and support for them is not expected in K64.

The following calls return values using new dedicated types, and the seconds returned is `unsigned long` (64 bits) in K64 (K32 is unchanged). Note these are the Mach primitives; most kexts will use the BSD equivalents instead.

```
extern void clock_get_system_microtime(
    clock_sec_t  * secs,
    clock_usec_t * microsecs);

extern void clock_get_system_nanotime(
    clock_sec_t  * secs,
    clock_nsec_t * nanosecs);

extern void clock_get_calendar_microtime(
    clock_sec_t  * secs,
    clock_usec_t * microsecs);

extern void clock_get_calendar_nanotime(
    clock_sec_t  * secs,
    clock_nsec_t * nanosecs);
```


### Thread Call KPI Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| - `thread_call_func` - `thread_call_func_cancel` - `thread_call_func_delayed` - `thread_call_is_delayed` | - `thread_call_allocate` - `thread_call_enter` - `thread_call_enter_delayed` - `thread_call_cancel` - `thread_call_free` |

### Thread Timer KPI Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| - `thread_set_timer` - `thread_set_timer_deadline` - `thread_cancel_timer` | - `assert_wait_deadline` - `assert_wait_timeout` |

### Kernel Thread KPI Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| `kernel_thread` | `kernel_thread_start` (Make sure to release the reference to the `thread_t` by calling `thread_deallocate`.) |

### Clock Time KPI Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| `clock_get_uptime` | `mach_absolute_time` |

### BSD and VFS KPI Changes

__Important:__ There is __no support__ for unthreaded filesystems in the 64-bit kernel. All Filesystems need to be threaded to work in K64. Do not rely on the funnel for any locking.

### KAuth User KPI Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| - `suser` - `is_suser` - `is_suser1` | - `kauth_cred_issuser`  `vfs_context_suser`  `proc_suser` |

### KAuth Credentials Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| `proc_ucred` | `kauth_cred_get` (or get cred out of passed in `vfs_context`) |
| `kauth_cred_rele` | `kauth_cred_unref` |

### UBC Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| - `ubc_setcred` - `ubc_sync_range` | - `ubc_setthreadcred` - `ubc_msync` |
| - `ubc_getobject` - `ubc_info_deallocate` - `ubc_info_init` - `ubc_info_zone` - `ubc_isinuse` | — |

### VFS Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| `file_vnode` | - `file_vnode_withvid` (provides `vnode` and `vid`) - `vnode_getwithvid` (for `ioref` without being under `fileref` scope) |
| `rootvnode` | - `vfs_rootvnode` (returns a pointer with `ioreference`, need to drop the ref with `vnode_put()`) |
| - `vslock` - `vsunlock` - `vnode_target` | — |

### Other Changes

| Not supported in 64-Bit | Recommended |
| --- | --- |
| - `ldisc_deregister` - `ldisc_register` - `lightning_bolt` - `postevent` | - — |

### Known Bugs in November 2008

- If you touch the Extensions folder on a Leopard volume while running Snow Leopard, it will be updated with the wrong format mkext and the Leopard volume will panic on startup.
- Not all Apple-provided kernel extensions are available when using the 64-bit kernel on this seed. In particular, accelerated graphics are not supported. Additionally, sleep and hibernate are not supported. These features should be available in the release version of OS X Snow Leopard
- The “himemory_mode” boot option used to debug large physical memory configurations is not supported in this seed.
- The `showuserstack` `gdb` macro in `kgmacros` doesn’t work on 64 bit processes.
- Using the `-v` flag with kext tools disables error logging.
- `kextunload` and `mkextunpack` do not recognize long options such as `-bundle-id`, and some long options that take optional arguments require an equals sign for the argument to be recognized.

---
title: Installing an IOKit KEXT Without Rebooting
apple_id: DTS10002355
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2011-07-22'
source_url: https://developer.apple.com/library/archive/qa/qa1319/_index.html
archived_at: '2026-07-18T02:30:22.720215Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1319

# Installing an I/O Kit KEXT Without Rebooting

## Q:  Is it possible to install an I/O Kit KEXT without requiring a restart?

A: There is no easy solution to this problem. Currently, even Apple's own installers require restarting after a KEXT installation. Here's why this is more complicated than it may seem.

If another driver is currently matched to your device, that driver has to be unloaded first. This in turn means that the device can't be in use. Plus, the preferred mechanism for updating the system's list of known KEXTs does not exist in early releases of Mac OS X.

Given those considerations, here is the logic you should use:

After installing your KEXT, run the `touch` command on `/System/Library/Extensions`. Then,

- if the release is 10.5 or newer, there's nothing more to do. All KEXT caches except for the prelinked kernel are updated automatically after a short delay; the prelinked kernel is updated after the next restart.
- If the release is either 10.3.x or 10.4.x and `kextd` is NOT running, require a restart. A shell script can determine whether `kextd` is running using the code in Listing 1. This code will return the PID of `kextd` if it is running, or return nothing if it isn't.
- If the release is either 10.3.x or 10.4.x AND `kextd` is running, send `kextd` a `SIGHUP` signal as shown in Listing 2.
- If the release is 10.2.x or older (Jaguar or before), require a restart.

__Listing 1__  Determining whether kextd is running.

```
/bin/ps -ax | /usr/bin/awk '{print $1" "$4}' | grep kextd | /usr/bin/awk '{print $1}'
```


__Listing 2__  Sending a SIGHUP to kextd.

```
/bin/kill -1 `/bin/ps -ax | /usr/bin/awk '{print $1" "$4}' | grep kextd | /usr/bin/awk '{print $1}'`
```

It is important that your install script cope with the case where `kextd` is not running.

You might wonder if you can just `posix_spawn kextload` to load your KEXT. This approach has its own pitfalls. If you run `kextload` but the user waits longer than about a minute to plug in the device, your driver will be unloaded and another matching driver will be loaded for your device instead. And, even if the user plugs in the device promptly, if they unplug the device later, your driver will still be unloaded after a minute. You're now back to the first situation because `kextd` isn't aware of your KEXT if you've loaded it by hand using `kextload`. `kextd` enumerates available KEXTs only according to the logic presented earlier.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-22 | Reformatted and made minor editorial changes. Added information about Mac OS X 10.5 and later. |
| 2003-10-28 | New document that describes the state of the art of installing I/O Kit kernel extensions (KEXTs) without requiring a restart. |


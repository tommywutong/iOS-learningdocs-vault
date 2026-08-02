---
title: IOKit Power Management Release Notes
apple_id: TP40006501
resource_type: Release Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Darwin/RN-IOKitPowerManagment/index.html
archived_at: '2026-07-18T02:50:23.112232Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# I/O Kit Power Management Release Notes

#### Contents:

- [Managing Power Chapter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Kernel Functional Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [New Driver API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [New Application API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)

### Managing Power Chapter

Please see the newly re-written _Managing Power_ chapter in _[IOKit Fundamentals](../../documentation/Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ - it documents many previously undocumented IOService power management API’s and behaviors.

### Kernel Functional Changes

In Leopard, the kernel implementation of driver power management has been revised and re-written. Threading, locking, and timing semantics have been changed for more robust, stable, and predictable behavior.

This means that your power managed I/O Kit device driver will have different threading and locking interactions with power management. Although the changes make for a more consistent and usable power management system, driver code that worked fine in Tiger may behave unexpectedly in Leopard.

- Calls into kernel Power Management are now asynchronous

  All IOService PM API calls simply enqueue the work to be done for later processing, and immediately return.

  For example, upon calling `IOService::changePowerStateTo`, a driver must wait for the call’s completion before taking any action (like trying to access device registers or communicate with the device before it has powered on). Drivers must wait for the following `IOService::setPowerState` call that indicates power management has actually changed the device’s state.
- Calls from kernel PM into drivers are now “clean”

  Any place power management will call into a driver, namely `IOService::setPowerState`, `IOService::powerStateWillChangeTo`, or `IOService::powerStateDidChangeTo`, is now performed on a newly created thread.
- Do not access IOService member variable _pm_vars_

  The `pm_vars` variable is deprecated in Leopard. The most common reason to use it was to check your driver’s current power state - please call `IOService::getPowerState` instead.

### New Driver API

- __IOService::systemWillShutdown__

  Any power managed IOService driver may receive a `kIOMessageSystemWillRestart` or `kIOMessageSystemWillShutdown` notification that the system is shutting down or restarting and take appropriate action.

  Shutdown notifications are delivered in child-first _IOPower_ plane order. Shutdowns are delivered after all user processes have been terminated and after all filesystems have been unmounted. If your hardware does not have any physical state to save (like a disk driver flushing caches to disk), you probably do not need to run at shutdown time.

  Please use discretion, as any unnecessary use of this API can cause slowdowns in shutdown or restart. For debugging, OS X reports per-driver time measurements via _FireWire kprintf_ with `boot-args="debug=0x14e io=0x880"`. See _FireWire SDK 24_ for details on kprintf logging.
- __IOService::getPowerState__

  Returns a device’s current power state (i.e. returns the integer index into the device’s power state array. A device's "current power state" is updated at the end of each power state transition.

### New Application API

- __Actively prevent System Sleep and Display Sleep__

  `IOPMAssertionCreate` and `IOPMAssertionRelease` allow a process to assert `kIOPMAssertionTypeNoDisplaySleep` or `kIOPMAssertionTypeNoIdleSleep`. As long as a sleep prevention or display sleep prevention assertion is active, the system will not idle sleep or display sleep, accordingly.

  Preventing idle sleep with an IOPMAssertion is far simpler than the existing technique of using `IORegisterForSystemPower`.

  Creating an assertion only requires one call at the beginning of any activities that should prevent sleep (making a backup, beginning a long computation) or that should prevent display sleep (playing a movie or slideshow).

  Assertions should be released with `IOPMAssertionRelease`. However, even if not properly released, assertions will be automatically released when the process exits, dies, or crashes. A crashed process will not prevent idle sleep indefinitely.

  The command-line tool `pmset -g` provides accountability by listing all outstanding assertions affecting _System Sleep_ or _Display Sleep_.

  Neither this API nor any other API allow an application to prevent _forced system sleep_ (e.g. lid close sleep, Apple Menu sleep, thermal emergency sleep, or low battery sleep).

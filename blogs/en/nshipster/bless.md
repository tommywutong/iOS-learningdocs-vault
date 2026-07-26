---
title: bless
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/bless/'
original_language: en
published: 2019-11-25
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:924e06ffff0a03b5'
translated: false
---

> 原文：[bless](https://nshipster.com/bless/)　·　NSHipster (Mattt)

# [bless](https://nshipster.com/bless/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  November 25^th, 2019

This Thursday is [Thanksgiving](https://en.wikipedia.org/wiki/Thanksgiving_%28United_States%29) in the United States, a holiday in which we’ll gather together to cultivate and express gratitude against a backdrop of turkey, mashed potatoes, and origin-myths of European colonialism in the Americas.

As the year — _and indeed the decade_ — draws to a close, we’re invited to reflect on the blessings in our lives: The individuals who fill them with joy, the circumstances that bring them comfort and security, the pursuits that endow them with meaning.

…of course, it’s also a time of ritualized, over-indulgent consumption. And for the PC gamers among us, that means shutting down our Macs, booting into our [Windows](https://support.apple.com/boot-camp) partitions, and settling into our long-neglected back catalogs on Steam.

---

So while you wait for your AAA titles to download and your Windows software updates to apply _(let’s assume you’re reading this on your iPhone)_, we invite you to count your blessings.

---

This week on NSHipster: a quick look at the `bless` command and the macOS boot process.

But first, a quick disclaimer:

---

The process of booting a computer is a small miracle. Starting with nothing — _“tabula rasa”_ — a computer incrementally runs smaller, simpler programs to load larger, more capable programs into memory, until it finally has everything it needs to run the operating system itself.

In a previous era of computers, operating systems were initialized using [BIOS](https://en.wikipedia.org/wiki/BIOS) firmware, which came pre-installed in system ROM. When a machine powered up, that firmware would be the first thing that the computer encountered, and it’d proceed to load machine code from the [boot sector](https://en.wikipedia.org/wiki/Boot_sector).

Nowadays, Macs and most other computers boot according to the [Extensible Firmware Interface](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#Booting) (EFI), which introduces a few levels of indirection for greater flexibility. When a machine powers on under this regime, it loads a boot manager, which is responsible for loading configuration from non-volatile RAM (NVRAM), including the file system paths of the loaders and kernels for the operating system. This additional step allows computers to boot into different partitions on disk and even network volumes.

The process of making a volume bootable is called blessing, and the operative command to accomplish this has been, historically, [`bless`](x-man-page://8/bless).

To get an overview of the blessed volumes on your machine, run `bless --info`:

```
$ sudo bless --info
… => Blessed System File is {Preboot}/…/System/Library/CoreServices/boot.efi
… => Blessed System Folder is {Preboot}/…/System/Library/CoreServices
The blessed volume in this APFS container is "/".
No blessed APFS snapshot for this volume.
```

Blessing a volume on the latest Mac hardware running the latest version of macOS is an involved process, which includes (among other things):

- Copying `boot.efi` to the correct file system path on the volume
- Writing information to the volume header to designate it as being bootable
- Setting the `efi-boot-device` and `efi-boot-device-data` variables to designate the volume as the next startup disk

To illustrate how much complexity is baked into blessing a volume, let’s focus on the first of these tasks:

> Copy `boot.efi`? Easy: `cp boot.efi "/Volumes/Macintosh HD"`.   
>  (It’s a UNIX system! I know this!)

_Well, not quite._

On a Mac booted from an APFS disk, `boot.efi` is in a special preboot volume (`/dev/disk1s2`), at a path containing a generated UUID. HFS+ is rather simpler by comparison, since the boot loader has a hard-coded located at `/System/Library/CoreServices/boot.efi`. That is, unless, the disk is encrypted with [FileVault full-disk encryption](https://support.apple.com/en-us/HT204837) or is part of a RAID array that requires additional drivers. And all of this is to say nothing of [Secure Boot](https://support.apple.com/en-us/HT208330) and the [Apple T2 Security Chip](https://support.apple.com/en-us/HT208862), which comes standard on the iMac Pro as well as Mac Mini, MacBook Air, and MacBook Pro computers since 2018.

But in case you remain undeterred, and _really_ want to avoid the inconvenience of opening up System Preferences, here’s the invocation you seek:

```
$ sudo bless -mount /Volumes/BOOTCAMP -setBoot --nextonly
Could not set boot device property: 0xe00002e2
```

However, that hasn’t worked since the advent of [System Integrity Protection](https://support.apple.com/en-us/HT204899) (SIP) in macOS 10.11.

A suggested workaround invokes `systemsetup` as a replacement for `bless`.

The [`systemsetup`](x-man-page://8/systemsetup) command is similar to System Preferences, in that it can be used to set machine-wide preferences, including: date and time settings, remote login and Apple Events and the behavior of the physical power button, as well as when a computer should go to sleep and what should happen after a power failure.

The `systemsetup` invocation to set the startup disk goes a little something like this:

```
$ sudo systemsetup -setstartupdisk /Volume/BOOTCAMP/Windows
Setting startup disk not allowed while System Integrity Protection is enabled.
```

But that, too, doesn’t seem to work on recent versions of macOS without disabling SIP _(and for the vast majority of folks, there’s never a good reason to do this)_.

---

So by now, Windows has finished updating itself _(maybe)_, the game is 100% downloaded and ready to launch, and you’re left wondering _“What’s the point of this article?”_

To that, dear reader, I’d first say that there are far, _far_ worse things than being pointless _(or [Point-Free](https://www.pointfree.co), as it were)_. But if you’re still searching for a takeaway, here it is:

> You probably won’t ever have an occasion to use the `bless` command _(or `systemsetup`, for that matter)_.

With every design decision, software vendors perform a balancing act between security and convenience. For most people, the new security features in recent versions of macOS and new Apple hardware make them undeniably safer, usually without any perceivable downside. Yet we, as developers, especially those of us with a hacker mentality, may see the Mac’s trajectory towards a closed, iOS-like security model as a mixed blessing — a curse, even.

If that’s the case for you _(and even if it isn’t)_, then please allow us to offer another helping of article-concluding takeaway:

> Take time to be thankful for all that you have, and seek to be present for those around you this holiday season.

---
title: Disabling Processor Cores on a Multi-Core System
apple_id: DTS10001686
resource_type: QA
platform: macOS
topic: Performance
technology: null
published: '2008-09-16'
source_url: https://developer.apple.com/library/archive/qa/qa1141/_index.html
archived_at: '2026-07-18T02:29:56.084693Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1141

# Disabling Processor Cores on a Multi-Core System

## Q:  These days, all Macintosh computers have multiple processor cores. I'd like to temporarily turn off some of the cores to test how my Mac OS X product behaves when fewer cores are available. How can I do that?

A: You have a couple of options for changing the number of active processor cores. The first option takes effect immediately and provides a convenient user interface. The second method requires a reboot but its effect is persistent until changed.

The simplest way to change the number of active processor cores is to use the Processor preference pane that is part of the CHUD (Computer Hardware Understanding Developer) tools. CHUD is normally installed as part of installing Xcode.

The Processor preference pane is located in `/Developer/Extras/Preference Panes`. Install it by just double-clicking it in Finder. System Preferences will launch and you'll have the option to install the preference pane for either the current user or for all users.

__Figure 1__  Processor preference pane icon.

!

Once the preference pane has been installed, you can use it to set the maximum number of processor cores available to the system and to start or stop any particular core on the fly.

__Figure 2__  Processor preference pane window.

!!

Click "Show control in menu bar" to install a shortcut to Processor functions in the menu bar.

__Figure 3__  Processor menu.

!

Select "Show Processor Palette" from the Processor menu to display a graphical representation of the available processors and their activity levels.

__Figure 4__  Processor palette.

!

Click the plus or minus buttons at the lower right to start or stop cores sequentially, or click the picture of each processor to stop or start that particular core.

Click the toolbar button at the upper right to show and hide the controls for customizing the processor palette.

__Figure 5__  Controls for customizing the processor palette.

!

The number of active cores can also be set from the command line using the `nvram` command to set the `boot-args` firmware variable.

Firmware variables are written to non-volatile memory (NVRAM) when the system is shut down or restarted. The kernel only reads `boot-args` at boot time. This means that, unlike using the Processor preference pane, a reboot is required to change the number of active processor cores from the command line. This also means that this setting is persistent across sleep/wake and system restarts, a useful feature for automated testing.

Follow these steps to set the number of active processor cores from the command line:

1. Note the current setting of `boot-args` using the following command:


```
$ nvram boot-args
```
2. Enter the following command to set the number of cores to use to 1:


```
$ sudo nvram boot-args="cpus=1"
```

   The `cpus` boot argument can range from 1 up to the total number of processor cores on your system.

   You will need to reenter the current value of `boot-args` if you want to preserve it. For example, if the result of step 1 was:


```
 boot-args       debug=0x4
```

   the `nvram` command would be:


```
$ sudo nvram boot-args="debug=0x4 cpus=1"
```
3. Enter the administrator password when prompted.
4. Restart the system.

If you decide to change the setting before restarting, just run `nvram` again with the desired settings which will then overwrite the previous setting. If you misspell any of the arguments such as `boot-args` or `cpus`, there is no warning, a (probably useless) new entry into NVRAM is made, and the number of active cores will be unchanged after restart.

The `cpus` boot argument will remain in effect across all system restarts until it is changed or cleared. There are two ways to clear the `cpus` setting:

1. Use the `nvram` command to clear the `boot-args` firmware variable as follows:


```
$ sudo nvram boot-args=""
```
2. You can clear `boot-args` by resetting your Mac's NVRAM as described in this [support article](http://support.apple.com/kb/HT1379). Keep in mind that this will also clear all other custom NVRAM settings.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-16 | Added CHUD Processor preference pane. Removed obsolete content. Made editorial changes. |
| 2002-05-22 | New document that describes how to disable processor cores on a multi-core system for testing purposes. |


---
title: CCL Modem Scripting Release Notes
apple_id: TP40006500
resource_type: Release Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/HardwareDrivers/RN-CCLModemScripting/index.html
archived_at: '2026-07-18T02:58:39.467426Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# CCL Modem Scripting Release Notes

#### Contents:

- [Changes to Leopard Modem CCLs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [If you have an existing script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Superseding an older script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Net User Impact](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)

### Changes to Leopard Modem CCLs

Modem scripts have changed for Leopard. The CCL language used to write the scripts is the same, but has been enhanced to support new pre-defined variables for GPRS-era devices. For example, Access Point Name (APN) and Context ID (CID) are now supported in `varString ^22` and `varString ^23`, respectively. Other new varString parameters are Connect Speed (`^20`), Init (`^21`), and four script-defined strings (`^27`-`^30`). The latter can be defined by the script author as useful parameters for supporting multiple devices with the same script. The CCL language changes have been documented in an updated _[CCL Modem Scripting Guide](../../documentation/Hardware%20Drivers/CCL%20Modem%20Scripting%20Guide/Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinru)_.

The other major change is to the packaging of CCL Scripts. Rather than a flat file with a name describing the device supported, CCL scripts are now packaged in `.ccl` bundles. These bundles specify "personalities" that specify a script, arguments to that script, and the name or names of devices that are supported by the personality. Parameters such as "Init String," "Preferred APN," and "varString 27" can be stored in a personality and then a single script can support multiple devices or configurations. Additionally, the names that appear in the Modem Preferences and Bluetooth Setup UIs are now independent of the name of the script on disk. Developer examples are in `/Developer/Extras/Modem Scripts` and `/Developer/Applications/Utilities/iSync Plug-in Maker.app` can create "Modem Script Bundles" starting from your script or a new template script. The shipping `Apple Modems.ccl` and `Generic GPRS.ccl` take advantage of some of these new features.

### If you have an existing script

If you have an old script and want to bundle it so that it appears under the proper vendor name in the UI, you can use _iSync Plug-in Maker_ (its help discusses Modem Scripts) to import your old flat script into the Modem Script pane. The Vendor and Device panes provide the associated meta-data and there is an option to create a Modem Script bundle (without creating an iSync Plug-in).

### Superseding an older script

If you give the `.ccl` bundle the same name as the script it is replacing, the new script will implicitly “supersede” the old script: the flat one will disappear from the UIs if both the bundle and the flat script are installed. If you want to give the bundled version a different name, you can add a `Supersedes` array to the relevant personality, naming flat scripts superseded by a that personality. See `/Developer/Extras/Modem Scripts/Replacement Example.ccl`. Additionally, if an old network configuration is migrated, any superseded flat scripts will be upgraded to the bundle and personality that replaces it when the user uses Modem Preferences.

### Net User Impact

Dialup networking support has changed and explicit support for very old modems was removed. If you have an older modem, you may need to select a new script for it. Vendor 'Generic', model 'Dialup' may work well. Otherwise, you may need to copy a script from an older OS X system or download a script from the manufacturer of your modem.

Similarly, if your ISP uses its own dialing program (e.g. AOL Connect) and you had a non-Apple modem, you may need to copy your old script from another system or download a script from the modem manufacturer.

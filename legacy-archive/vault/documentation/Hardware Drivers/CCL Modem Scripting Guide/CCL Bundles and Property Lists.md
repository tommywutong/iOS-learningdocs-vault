---
title: CCL Modem Scripting Guide
apple_id: TP40005464
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-06-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Reference/CCLScriptingRef/ExternalVariableStorage/ExternalVariableStorage.html
archived_at: '2026-07-15T07:41:16.383109Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CCL Modem Scripting Guide](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md)


[Next](CCL%20Command%20Reference.md)[Previous](CCL%20Script%20Syntax.md)

# CCL Bundles and Property Lists

OS X v.10.5 and later supports storage of strings and other data outside of the modem script itself in an easily modified property list file. Classic Mac OS (System 7 through Mac OS 9) and OS X prior to v.10.5 provided similar support with data stored in the resource fork of each script. This appendix explains both mechanisms for external storage to allow ease of conversion into the more modern property list format.

A modem script from Mac OS 9 and earlier may contain an optional `mlts` resource that tells the CCL interpreter the characteristics of the modem. Byte 1 indicated support for at least one type of _standard_ error correction (1=supported). Byte 2 was reserved. Byte 3 indicated contained the maximum length (in characters) for variable string 7, byte 4 for variable string 8, and byte 5 for variable string 9.

These legacy `mlts` options are not supported in OS X. OS X assumes that all modems can support dial strings of at least 40 characters per dial string and that all modems support built-in error correction.

Beginning in OS X v. 10.5, the preferred format for external storage is as a property list. When using this mechanism, the CCL script must be enclosed in a package. The structure of such a package is shown below:

```
MyModem.ccl
|
|-Contents
      |
      |- Info.plist        <- The property list
      |- Resources
             |-MyModem     <- The script itself
```

For general information about property lists, see _[Property List Programming Topics for Core Foundation](../../Core%20Foundation/Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i)_ and _[Property List Programming Guide](../../Cocoa/Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)_. The details of what should you should put in the property list are covered in the following sections.

This dictionary (`dict` element) contains parameters that are made available to your CCL script through variable strings. (See [Variable Strings (varStrings)](CCL%20Script%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqojnknltc) for more information on how to use these variables in your script.)

| Key in CCLParameters Dictionary | Variable String in CCL Script | Description |
| --- | --- | --- |
| `Connect Speed` | `^20` | The serial port speed desired.  You may use `-1` if your device has no notion of multiple connection speeds. |
| `Init String` | `^21` | The device initialization string. |
| `Preferred APN` | `^22` | Preferred access point name. Used mainly for cellular phone connections. |
| `Preferred CID` | `^23` | Preferred connection identifier. Used mainly for cellular phone connections. |
| `varString 27` | `^27` | One of four device-specific strings that you can pass in. By using these variable strings, you can share a single script across multiple similar modems or for using the same modem-like device with (for example) multiple cellular services. |
| `varString 28` | `^28` | One of four device-specific strings that you can pass in. By using these variable strings, you can share a single script across multiple similar modems or for using the same modem-like device with (for example) multiple cellular services. |
| `varString 29` | `^29` | One of four device-specific strings that you can pass in. By using these variable strings, you can share a single script across multiple similar modems or for using the same modem-like device with (for example) multiple cellular services. |
| `varString 30` | `^30` | One of four device-specific strings that you can pass in. By using these variable strings, you can share a single script across multiple similar modems or for using the same modem-like device with (for example) multiple cellular services. |

This `string` element describes the connection type. Valid values are `Dialup` and `GPRS`

This `dict` element should contain the following key/value pairs:

- `DeviceModel`—A `string` element representing the device model number or name.
- `DeviceVendor`—A `string` element describing the vendor name.

These strings are presented to the user when choosing a device model and manufacturer.

This `dict` element supports the following keys:

- `CID Query`—A boolean value that tells whether a device allows OS X to query it for valid connection IDs. OS X uses this information outside the scope of your script.

  Legal values are `<true/>` and `<false/>`.
- `Data Mode`—A boolean value that indicates whether a device supports initiating a connection by requesting data mode (`AT+CGDATA`). Your script should respect this value when making a connection and use data mode only on communication hardware that supports it.

  Legal values are `<true/>` and `<false/>`.
- `Dial Mode`—A boolean value that indicates whether a device supports initiating a connection by dialing a fictitious number (`ATD *99`). If true, OS X will fill in the phone number automatically.

  Legal values are `<true/>` and `<false/>`
- `Independent CIDs`—A boolean value that indicates whether or not a device supports independent CIDs for computer use versus internal (cellular phone feature) use.

  When you issue an AT command that sets the CID (`AT+CGDCONT=...`, devices with independent CID support treat the AT command as a temporary change from the default value. Devices that lack this feature "forget” their previous CID value and must be reconfigured upon disconnect to avoid service loss, diminished service, or unexpected billing charges.

  Legal values are `<true/>` and `<false/>`.
- `Maximum CID`—A value of type `integer` that represents the maximum allowable connection identifier (CID) value supported by the device. OS X uses this information outside the scope of your script.

This `string` element tells the name of the script within the `Resources` directory inside your script bundle.

This `integer` key should currently always be `1`.

The following `CFBundle` keys should be provided:

- `CFBundleDevelopmentRegion`
- `CFBundleGetInfoString`
- `CFBundleIdentifier`
- `CFBundleInfoDictionaryVersion`
- `CFBundleName`
- `CFBundlePackageType`
- `CFBundleShortVersionString`
- `CFBundleSignature`
- `CFBundleVersion`

For more information about these keys, see _[CFBundle Reference](https://developer.apple.com/documentation/corefoundation/cfbundle-s0a)_.

This section shows two example property lists. Listing 3-1 shows an example of a property list for a GPRS device. [Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnznknltg) shows a property list for a traditional dialup modem device.

__Listing 3-1__  A GPRS device property list example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CCL Personalities</key>
    <dict>
        <key>Default Personality</key>
        <dict>
            <key>Device Names</key>
            <array>
                <dict>
                    <key>DeviceModel</key>
                    <string>GPRS Device</string>
                    <key>DeviceVendor</key>
                    <string>Example</string>
                </dict>
            </array>
            <key>Connect Type</key>
            <string>GPRS</string>
            <key>Script Name</key>
            <string>GPRS Example</string>
            <key>GPRS Capabilities</key>
            <dict>
                <key>Data Mode</key>
                <false/>
                <key>Dial Mode</key>
                <true/>
                <key>Independent CIDs</key>
                <false/>
                <key>CID Query</key>
                <false/>
                <key>Maximum CID</key>
                <integer>10</integer>
            </dict>

            <!-- SystemConfiguration values can replace CCLParameters -->
            <key>CCLParameters</key>
            <dict>
                <key>Init String</key>
                <string>E0V1&amp;F&amp;D2&amp;C1&amp;C2S0=0</string>
                <key>Preferred APN</key>
                <string>network</string>
                <key>varString 27</key>
                <string></string>
                <key>varString 28</key>
                <string></string>
                <key>varString 29</key>
                <string></string>
                <key>varString 30</key>
                <string></string>
            </dict>
        </dict>
    </dict>
    <key>CFBundleIdentifier</key>
    <string>com.apple.ccl.GPRS_Example</string>
    <key>CFBundleName</key>
    <string>GPRS Example</string>
    <key>CCL Version</key>
    <integer>1</integer>
    <key>CFBundleDevelopmentRegion</key>
    <string>English</string>
    <key>CFBundlePackageType</key>
    <string>CCLB</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleSignature</key>
    <string>iSPM?</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
</dict>
</plist>
```


__Listing 3-2__  A dialup modem property list example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CCL Personalities</key>
    <dict>

        <key>Default Personality</key>
        <dict>
            <key>Device Names</key>
            <array>
                <dict>
                    <key>DeviceModel</key>
                    <string>Dialup Device</string>
                    <key>DeviceVendor</key>
                    <string>Example</string>
                </dict>
            </array>
            <key>Connect Type</key>
            <string>Dialup</string>
            <key>Script Name</key>
            <string>Dialup Example</string>
            <key>CCLParameters</key>
            <dict>
                <key>Connect Speed</key>
                <string>115200</string>
                <key>Init String</key>
                <string>&amp;FE0V1</string>
                <key>varString 27</key>
                <string></string>
                <key>varString 28</key>
                <string></string>
                <key>varString 29</key>
                <string></string>
                <key>varString 30</key>
                <string></string>
            </dict>
        </dict>

    </dict>

    <key>CFBundleIdentifier</key>
    <string>com.apple.ccl.Dialup_Example</string>
    <key>CFBundleName</key>
    <string>Dialup Example</string>
    <key>CCL Version</key>
    <integer>1</integer>
    <key>CFBundleDevelopmentRegion</key>
    <string>English</string>
    <key>CFBundlePackageType</key>
    <string>CCLB</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleSignature</key>
    <string>iSPM?</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
</dict>
</plist>
```

[Next](CCL%20Command%20Reference.md)[Previous](CCL%20Script%20Syntax.md)


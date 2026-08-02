---
title: Detecting low printer ink levels
apple_id: DTS10003734
resource_type: Technical Note
platform: macOS
topic: Graphics & Animation
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/technotes/tn2144/_index.html
archived_at: '2026-07-26T19:54:08.472249Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
Retired Document: This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2144

# Detecting low printer ink levels

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgqwugsbrfvjukq2ujfhu4mi)[Custom Supply Tools](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgqwugsbrfvjukq2ujfhu4mq)[Required Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgqwugsbrfvjukq2ujfhu4my)[Optional Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgqwugsbrfvjukq2ujfhu4na)[Testing your tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgqwugsbrfvjukq2ujfhu4ni)[Sample SNMP Query](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgqwugsbrfvjukq2ujfhu4nq)[Communication with your printer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgqwugsbrfvjukq2ujfhu4ny)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgqwvezlwnfzws33ojbuxg5dpoj4s2u2xge)

## Introduction

Starting with Mac OS X 10.4, IP printers can detect printer supply levels by using the built-in command line tool `snmpInk`. This tool is run by default to determine printer ink levels. The tool is located in `/System/Library/Printers/Libraries/` and can be run on the command line with a single argument, the printer queue ID.

```
/System/Library/Printers/Libraries/snmpInk <queue_id>
```

This tool will return XML formatted data obtained using SNMP which is then used to create a supply level Print Dialog Extension (PDE), which can be displayed to the user to indicate ink levels. Here is an example of a "Supply Levels" pane in the Print Dialog:

[Back to Top](#)

## Custom Supply Tools

A printer driver can provide a custom tool that can detect printer supply levels. This tool will override the default `snmpInk` tool used for IP printers. The driver specifies the appropriate tool via a line in the printer's PPD or an entry in the printer's info ticket. When the print system wishes to query the printer for supply levels, it will execute the tool passing in the queue id (the name of the printer queue) as the first argument.

If you have a CUPS driver and you would like to override the default tool with your custom tool, you must add the \*`APPrinterLowInkTool` key to your PPD file with the full path to your tool.

```
*APPrinterLowInkTool: "/Library/Printers/Foo/Utility/MySupplyTool"
```

If you have a Tioga driver (10.0 -10.1 based driver), you must include the `APPrinterLowInkTool` in your Info.plist file as the child of the root node.

When executed, the tool should write to stdout the XML form of a CF or `NSDictionary`. The dictionary describes each consumable in the printer and provides information about its current state.

Your tool should also be able to end gracefully when receiving the TERM signal. The TERM signal is sent to your tool if a user were to switch printers in the print dialog. Therefore, your tool may need a signal handler to gracefully shutdown its dialog with the printer.

[Back to Top](#)

## Required Keys

Currently, there is a single defined key for the top-level dictionary. This key is `prtMarkerSuppliesTable`. The value for the `prtMarkerSuppliesTable` key is an array of dictionaries. Each element in the array describes a consumable through a series of key-value pairs. The defined keys and their values are listed below. See [RFC 3805](http://www.ietf.org/rfc/rfc3805.txt) for additional information about these keys.

When creating your custom tool, you must support four keys.

__Table 1__  Required Keys

| Required Keys | Type | Value |
| prtMarkerSuppliesClass | CFNumber representing an integer | 1 = other 3 = supplyThatIsConsumed 4 = supplyThatIsFilled |
| prtMarkerSuppliesDescription | CFString | A localized description of the supply.This description should be as generic as possible. For example "Black ink". The prtMarkerPartNumber dictionary entry can be used to supply more precise information about the supply. |
| prtMarkerSuppliesMaxCapacity | CFNumber representing an integer | The maximum capacity of this supply container/receptacle expressed in prtMarkerSuppliesSupplyUnit. A value of (-1) means other and specifically indicates that the sub-unit places no restrictions on this parameter. A value of (-2) means unknown. |
| prtMarkerSuppliesLevel | CFNumber representing an integer | The current level if this supply is a container; the remaining space if this supply is a receptacle. A value of (-2) means unknown. A value of (-3) means that the printer knows that the maximum capacity has not been reached but the precise level is unknown. If the device can only signal if the supplies level is "low" then set this value to 5% of 'prtMarkerSuppliesMaxCapacity'. |

__Important:__ It is important to note that your custom tool should return localized CFStrings for the prtMarkerSuppliesDescription key. Therefore, your tool would most likely be contained in an application bundle with localized resources.

[Back to Top](#)

## Optional Keys

__Table 2__  Optional Keys

| Optional Keys | Type | Value |
| prtMarkerSuppliesType | CFNumber representing an integer | 1 = other 2 = unknown 3 - toner 4 = wasteToner 5 = ink 6 = inkCartridge 7 = inkRibbon 8 = wasteInk 9 = opc 10 = developer 11 = fuserOil 12 = solidWax 13 = ribbonWax 14 = wasteWax 15 = fuser 16 = coronaWire 17 = fuserOilWick 18 = cleanerUnit 19 = fuserCleaningPad 20 = transferUnit 21 = tonerCartridge 22 = fuserOiler 23 = water 24 = wasteWater 25 = glueWaterAdditive 26 = wastePaper 27 = bindingSupply 28 = bandingSupply 29 = stitchingWire 30 = shrinkWrap 31 = paperWrap 32 = staples 33 = inserts 34 = covers |
| prtMarkerSuppliesSupplyUnit | CFString representing an integer | 1 = other 2 = unknown 3 = tenThousandthsOfInches 4 = micrometers 7 = impressions 8 = sheets 11 = hours 12 = thousandthsOfOunces 13 = tenthsOfGrams 14 = hundrethsOfFluidOunces 15 = tenthsOfMilliliters 16 = feet 17 = meters 18 = items 19 = percent |
| prtMarkerSRGBRepresentation | CFArray containing three CFNumbers | The red, green, and blue sRGB values to represent on the display the color of this supply. |
| prtMarkerPartNumber | CFString holding the part number of the supply. | Vendor specific |

[Back to Top](#)

## Testing your tool

When you are testing your custom supply tool, you can run your tool on the command line and retrieve output in the console.

```
<tool> <queue_id>
```

__Note:__ When developing a custom tool you must enable verbose output by modifying your printing preferences to get the output returned by your tool. Enable verbose output with the following command:

defaults write com.apple.print verboseInk 'YES'

[Back to Top](#)

## Sample SNMP Query

Here is sample output for a color laser printer. This sample was generated via SNMP queries of the printer.

__Listing 1__  Sample SNMP Query

```xml
<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"                               "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> <plist version="1.0"> <dict>         <key>prtMarkerSuppliesTable</key>         <array>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Black Print Cartridge</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>20500</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>25000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>3</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8550A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Cyan Print Cartridge</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>11750</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>25000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>3</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8551A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Magenta Print Cartridge</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>12500</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>25000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>3</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8553A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Yellow Print Cartridge</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>11500</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>25000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>3</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8552A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Black Image Drum</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>38800</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>40000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>9</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8560A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Cyan Image Drum</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>14400</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>40000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>9</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8561A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Magenta Image Drum</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>14800</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>40000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>9</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8563A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Yellow Image Drum</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>14800</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>40000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>9</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8562A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Image Transfer Kit</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>162822</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>200000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>20</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8555A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Image Cleaning Kit</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>45388</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>50000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>18</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8554A</string>                 </dict>                 <dict>                         <key>prtMarkerSuppliesClass</key>                         <integer>3</integer>                         <key>prtMarkerSuppliesDescription</key>                         <string>Image Fuser Kit</string>                         <key>prtMarkerSuppliesLevel</key>                         <integer>62819</integer>                         <key>prtMarkerSuppliesMaxCapacity</key>                         <integer>100000</integer>                         <key>prtMarkerSuppliesSupplyUnit</key>                         <integer>7</integer>                         <key>prtMarkerSuppliesType</key>                         <integer>15</integer>                         <key>prtMarkerPartNumber</key>                         <string>HP C8556A </string>                 </dict>         </array> </dict> </plist>
```

[Back to Top](#)

## Communication with your printer

To communicate with your printer, you will need to determine your printers connection type. You can use the `PMPrinter` APIs to determine the connection type from the queue ID.

__Listing 2__  Determine your printers connection type from the queue ID

```
 //argv[1] = Queue name      CFStringRef queueID = CFStringCreateWithCString(kCFAllocatorDefault,argv[1],kCFStringEncodingUTF8);     PMPrinter printer = PMPrinterCreateFromPrinterID(queueID);      CFURLRef deviceURI;     PMPrinterCopyDeviceURI(printer, (CFURLRef *)&deviceURI);          //connection type : ipp, lpd ...     CFURLRef scheme = CFURLCopyScheme(deviceURI);
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2005-06-29 | Updates. |
|  | New document explaining how to detect printer supply levels using a low ink tool. |


---
title: New PPD keywords available in Mac OS X version 10.3
apple_id: DTS10003325
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: null
published: '2004-05-26'
source_url: https://developer.apple.com/library/archive/qa/qa1352/_index.html
archived_at: '2026-07-18T02:30:25.814630Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1352

# New PPD keywords available in Mac OS X version 10.3

## Q:  What new PPD keywords are available for CUPS filters to use in Mac OS X version 10.3?

A: Starting with Mac OS X version 10.3 (Panther), the printing system supports four new PostScript Printer Description (PPD) keywords that printer vendors can use to specify several new options.

- `APDialogExtension` - specifies a PDE (Printing Dialog Extension) to load
- `APPrinterUtilityPath` - specifies a printer configuration utility for the user
- `APPrinterIconPath` - specifies a custom icon
- `cupsICCProfile` - specifies a ColorSync profile(s) for the printer

The new keys provide a way for developers to specify Printing Dialog Extensions (PDEs), a configuration utility, a custom icon, and ColorSync profiles for use with their PPD.

A PPD can specify one or more PDEs to load in the Print dialog by adding the following key, one per PDE:


```
*APDialogExtension: "Library/Printers/Foo/PDEs/FinishingOptions.plugin"
```


A PPD can specify an appropriate printer utility by adding a line specifying the full path to the utility as follows:


```
*APPrinterUtilityPath: "/Library/Printers/Foo/Printer Utility/Utility.app"
```


A PPD can specify the location of a printer icon in a PPD file as follows:


```
*APPrinterIconPath: "/Library/Printers/Foo/Printer Icons/modelA.icns"
```


A PPD can specify ColorSync profiles to be associated to the PPD. The system will load and register the profiles when the printer queue is created. The profiles would then be used by the system at various times including PDF document spooling, during the printing of remotely queued print jobs, and so forth. Each profile is specified by a line in the PPD in the following form:


```
*cupsICCProfile ColorModel.MediaType.Resolution/Mode: "profile_location"
```

where the qualifier `ColorModel` is one of your PPD's `ColorModel` option values, the `MediaType` qualifier is one of the available `MediaType` option values and the `Resolution` qualifier is one of the available resolutions. If any of the qualifiers are missing, the PPD file will treat the missing qualifier as a wildcard value and will match the profile for ALL possible values of the missing qualifier. `Mode` is a human-readable string that will appear in the ColorSync Utility. The `profile_location` is either an absolute or relative path to the icc file. If a relative path is used, the path will be relative to `/usr/share/cups/profiles/`. The ColorSync Utility is the best tool to verify that your printer profiles have been correctly registered.

Here are a few examples:

(1)


```
*cupsICCProfile CMYK.Photo.600x600dpi/LoResPhoto CMYK Profile: "Foo/LoResPhotoCMYK.icc"
```

specifies a CMYK profile to use when the selected `ColorModel` is CMYK, printing to a `MediaType` called "Photo" and at "600x600dpi" `Resolution` mode. A relative path was given for the profile location, therefore the profile is located at `/usr/share/cups/profiles/Foo/`.

(2)


```
*cupsICCProfile CMYK..600x600dpi/LoRes CMYK Profile: "Foo/LoRes CMYK Profile.icc"
```

specifies a CMYK profile to use when the selected `ColorModel` is CMYK, printing to ALL possible `MediaType` values and at "600x600dpi" `Resolution` mode.

(3)

If you would like to match color profiles only by `ColorModel` values, your PPD file may have the following:


```
*cupsICCProfile Gray../Gray Profile: "/Library/Printers/Foo/Profiles/Test Gray Pro.icc"
*cupsICCProfile CMYK../CMYK Profile: "/Library/Printers/Foo/Profiles/TestCMYKPro.icc"
```

specifies a CMYK profile for when the selected `ColorModel` is CMYK, printing to a `MediaType` called "Photo" and at "600x600dpi" `Resolution` mode.

(4)

Profile matching in the PPD file is done by matching the following qualifiers :`ColorModel`, `MediaType`, and `Resolution` from the most specific to the least. Therefore, if examples 1-3 were the ONLY `cupsICCProfile` lines included in the same PPD file, the PPD file will match profiles in the following manner:

- 1. (LoResPhotoCMYK.icc) is the profile used if the print job options are CMYK, Photo, and 600x600dpi.
- 2. (LoRes CMYK Profile.icc) is used if the print job options are CMYK, any other media type, and 600x600dpi.
- 3. (TestCMYKPro.icc ) is used if the print job options are any other CMYK color model print job.
- 4. (Test Gray Pro.icc) is used if the print job option has Gray as the color model, regardless of the other options.

(5)

The default qualifiers are `ColorModel`, `MediaType`, and `Resolution`, in that order. Developers have the option of changing the second and third qualifiers that would replace the default values. To indicate an alternative to `MediaType`, a PPD needs to use the `cupsICCQualifier2` keyword. To indicate an alternative to `Resolution`, the `cupsICCQualifier3` keyword is used. For example, if you would like to use the `OutputMode` keyword instead of `Resolution` to change the third qualifier, you would set the value of the `cupsICCQualifier3` keyword to `OutputMode`. For example:


```
*cupsICCQualifier3: OutputMode
```

If the `cupsICCQualifier3` keyword did not exist, the result in the PPD file would have been equivalent to:


```
*cupsICCQualifier3: Resolution
```


As a reminder, Mac OS X 10.3 also supports the CUPS filter PPD keyword that allows the specification of a CUPS filter to run when the PPD is used.

To specify a CUPS filter use for PostScript, the vendor 'Foo' might use the following line:


```
*cupsFilter: "application/vnd.cups-postscript 0 /Library/Printers/Foo/filter/foopstops"
```


- [Technical Note TN2035, 'ColorSync on Mac OS X'](https://developer.apple.com/technotes/tn/tn2035.html)
- [PPD Files Tasks](https://developer.apple.com/documentation/Printing/Conceptual/UsingPPDFiles/ppd_tasks/chapter_3_section_1.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-05-26 | New document that describes the new PPD keywords available for CUPS filters in Mac OS X 10.3. |


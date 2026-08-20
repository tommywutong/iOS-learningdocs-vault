---
title: Supporting Printing in Your Carbon Application
apple_id: TP30000978
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-08-31'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/CPM_Concepts/cpm_chap4/cpm_adopt.html
archived_at: '2026-07-15T05:22:31.383947Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Supporting Printing in Your Carbon Application](Introduction%20to%20Supporting%20Printing%20in%20Your%20Carbon%20Application.md)


[Next](Document%20Revision%20History.md)[Previous](Printing%20Tasks.md)

# Adopting the Carbon Printing Manager

This chapter provides information that will help you convert printing code that uses the old Printing Manager so that your code uses the Carbon Printing Manager. The Carbon Printing Manager was designed to let Carbon applications take advantage of new features in Mac OS X, while still working correctly in previous versions of the Mac OS.

If you want to port an application that runs in Mac OS 9 and earlier versions of the Mac OS to one that runs in Mac OS X, you should read _Inside Carbon: Carbon Porting Guide_. The guide covers all porting topics, except for porting printing code, which is covered in this chapter.

Updating your application to use the Carbon Printing Manager is a straightforward process. These are the basic steps:

1. Remove all references to the `Printing.h` header file from your project.
2. If you are building your application so that is runs only in Mac OS X, make sure you link against the Application Services and Carbon frameworks. If you are building your application so that it can run in Mac OS 9 as well as in Mac OS X, you also need to add the `CarbonLib` library to your project.
3. Convert your code to use the new printing functions and opaque data types, as described in the following sections.

Because the Carbon Printing Manager replaces all of the functions in the old Printing Manager, the first step in converting your code is to locate and replace your old Printing Manager function calls with their equivalents from the Carbon Printing Manager. In most cases there is a one-to-one mapping between the new functions and the original functions they replace. [Table 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambug4wueqkki5buer2j) lists the Carbon equivalents for old Printing Manager functions.

__Table 3-1__  Carbon replacements for functions in the old Printing Manager

| Classic function | Carbon Printing Manager function |
| `PrOpen` | `PMCreateSession` |
| `PrClose` | `PMRelease` |
| `PrOpenDoc` | `PMSessionBeginDocument` |
| `PrCloseDoc` | `PMSessionEndDocument` |
| `PrOpenPage` | `PMSessionBeginPage` |
| `PrClosePage` | `PMSessionEndPage` |
| `PrintDefault` | `PMSessionDefaultPrintSettings` |
|  | `PMSessionDefaultPageFormat` |
| `PrValidate` | `PMSessionValidatePrintSettings` |
|  | `PMSessionValidatePageFormat` |
| `PrJobInit` | `PMSessionPrintDialogInit` |
| `PrJobDialog` | `PMSessionPrintDialog` |
| `PrStlInit` | `PMSessionPageSetupDialogInit` |
| `PrStlDialog` | `PMSessionPageSetupDialog` |
| `PrDlgMain` | `PMSessionPrintDialogMain` |
|  | `PMSessionPageSetupDialogMain` |
| `PrGeneral` | `PMSessionGeneral` Specific accessors replace common calls, see the Carbon Manager Reference documentation. |
| `PrSetError` | `PMSessionSetError` |
| `PrError` | `PMSessionError` |
| `MyDoPrintIdle` | `PMIdleProcPtr` |
| `MyPrDialogAppend` | `PMPageSetupDialogInitProcPtr` |
|  | `PMPrintDialogInitProcPtr` |

Some of the functionality provided by the old Printing Manager is no longer supported. [Table 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambug4wuerkjizbeuqsj) lists the old functions that are not supported by the Carbon Printing Manager.

__Table 3-2__  Old Printing Manager functions that are not supported in Carbon

| `PrPicFile` |
| `PrPurge` |
| `PrNoPurge` |
| `PrLoadDriver` |
| `PrDrvrDCE` |
| `PrDrvrOpen` |
| `PrDrvrClose` |
| `PrDrvrVers` |
| `PrCtlCall` |
| `PrJobMerge` |

The `PrPicFile` function was removed because the “deferred” printing style is no longer supported. All print records must use “draft” style, and printer drivers must perform their own despooling or, in Mac OS 8 and 9, use the Desktop Printer Spooler. Refer to the old Printing Manager documentation for information about draft and deferred printing styles. The Desktop Printer Spooler is described in Tech Note 1097.

A direct replacement for the `PrJobMerge` function is unnecessary because the `PMPageFormat` and `PMPrintSettings` objects can be used independently. You can print multiple documents, each with their own saved page format, using a single `PMPrintSettings` object.

The Carbon Printing Manager replaces the old Print Manager print record (`TPrint`) with two opaque data types, the `PMPrintSettings` object and the `PMPageFormat` object. All references to elements of the `TPrint` record in your code must be updated to refer to one of these objects, using the new accessor functions provided.

Because the `PMPrintSettings` and `PMPageFormat` objects are opaque, your application must not make assumptions about their size or internal structure. You will need to update any code that loads, stores, or directly manipulates the `TPrint` record.

[Table 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambug4wuerkjjfdusr2e) lists the accessor functions you can use to examine elements of the `PMPrintSettings` and `PMPageFormat` objects.

__Table 3-3__  Carbon accessor functions for the old Print Manager print record (TPrint) fields

| Data structure | Element | Accessor function |
| `TPrint` | `iPrVersion` | Not supported (Use `PMPrinterGetDriverReleaseInfo` to obtain a driver’s version strings. The version strings are not normally needed.) |
|  | `prInfo` | See `TPrInfo` |
|  | `rPaper` | `PMGetAdjustedPaperRect` |
|  | `prStl` | See `TPrStl` |
|  | `prInfoPT` | Not supported |
|  | `prXInfo` | not supported |
|  | `prJob` | See `TPrJob` |
|  | `printX[19]` | Not supported |
|  |  |  |
| `TPrInfo` | `iDev` | Not supported |
|  | `iVRes` | `PMGetResolution` |
|  | `iHRes` | `PMGetResolution` |
|  | `rPage` | `PMGetAdjustedPageRect` |
|  |  |  |
| `TPrStl` | `wDev` | `PMGetOrientation` |
|  | `iPageV` | `PMGetUnadjustedPaperRect` |
|  | `iPageH` | `PMGetUnadjustedPaperRect` |
|  | `bPort` | Not supported |
|  | `feed` | Not supported |
|  |  |  |
| `TPrJob` | `iFstPage` | `PMGetFirstPage` |
|  | `iLstPage` | `PMGetLastPage` |
|  | `iCopies` | `PMGetCopies` |
|  | `bJDocLoop` | Not supported |
|  | `fFromUsr` | Not supported |
|  | `pIdleProc` | `PMSessionSetIdleProc` This does nothing in Mac OS X; only used for Mac OS 8 and 9. |
|  | `pFileName` | Not supported |
|  | `iFileVol` | Not supported |
|  | `bFileVers` | Not supported |
|  | `bJobX` | Not supported |

When you use these accessor functions, be sure to pass the appropriate constant for any parameters you do not want to pass to the function or receive from it. For example, pass the `kPMDontWantData` constant in place of a parameter that returns data you’re not interested in.

Your application must dispose of any structures, references, or other data returned by Carbon Printing Manager functions. Your application should also release the `PMPrintSettings` and `PMPageFormat` objects it creates when they are no longer needed.

The Carbon Printing Manager provides the `PMSessionGeneral` function as a replacement for the old Printing Manager function `PrGeneral`. However, Apple suggests that you reduce your reliance on these functions because they are not currently supported by all printer drivers, and because they are not likely to be supported in future versions of the Mac OS.

[Table 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambug4wuerkjjfbusske) lists `PrGeneral` opcodes that are supported in Carbon in Mac OS 8 and 9, but not in Mac OS X. For opcodes that have an associated accessor function, you use that function instead of passing the opcode to `PMSessionGeneral`. For example, use `PMGetOrientation` instead of passing the `getRotnOp` constant to `PMSessionGeneral`. The `PMSessionGeneral` function returns the result code `kPMNotImplemented` for any unsupported opcodes, and for opcodes that have Carbon accessor functions.

__Table 3-4__  Carbon support for PrGeneral opcodes

| Opcode | Value | Accessor function |
| `GetRslDataOp` | 4 | `PMPrinterGetIndexedPrinterResolution` |
| `SetRslOp` | 5 | `PMSetResolution` |
| `DraftBitsOp` | 6 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `NoDraftBitsOp` | 7 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `getRotnOp` | 8 | `PMGetOrientation` |
| `NoGrayScl` | 9 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `GetPSInfoOp` | 10 | `PMSessionGeneral` supports this opcode in Mac OS 8/9; `PMPrinterGetLanguageInfo` supported in Mac OS 8/9 and Mac OS X |
| `PSIntentionsOp` | 11 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `EnableColorMatchingOp` | 12 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `PSAdobeOp` | 14 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `PSPrimaryPPDOp` | 15 | `PMPrinterGetDescriptionURL` |
| `kLoadCommProcsOp` | 16 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `kUnloadCommProcsOp` | 17 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `kPrinterDirectOpCode` | 20 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `kPrVersionOp` | 22 | `PMPrinterGetDriverCreator` |
| `kGetPrinterInfo` | 23 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `kIsSamePrinterInfo` | 24 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `kSetDefaultPrinterInfo` | 25 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |
| `kPrEnablePartialFonts` | 26 | `PMSessionGeneral` supports this opcode in Mac OS 8/9 |

[Table 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambug4wuerkjjfduqqkj) lists picture comments supported by the Carbon Printing Manager. Except where noted, these have the same behavior in Mac OS X as they do with LaserWriter 8 in Mac OS 8 and 9. Note that by default PostScript picture comments are ignored in Mac OS X; they are supported only when printing with LaserWriter 8 compatibility mode.

__Table 3-5__  Picture comments supported by the Carbon Printing Manager

| Name | Value | Data size | Data handle | Description |
| Text picture comments |  |  |  |
| `TextBegin` | 150 | 6 | `TTxtPicRec` | Begin text function |
| `TextEnd` | 151 | 0 | NULL | End text function |
| `StringBegin` | 152 | 0 | NULL | Begin string delimitation |
| `StringEnd` | 153 | 0 | NULL | End string delimitation |
| `TextCenter` | 154 | 8 | `TCenterRec` | Offset to center of rotation for text |
| `LineLayoutOff` | 155 | 0 | NULL | Turn printer driver’s line layout off |
| `LineLayoutOn` | 156 | 0 | NULL | Turn printer driver’s line layout on |
| `ClientLineLayout` | 157 | 16 | `TClientLLRec` | Customize line layout error distribution; not supported in Mac OS X |
|  |  |  |  |  |
| Graphics picture comments |  |  |
| `PolyBegin` | 160 | 0 | NULL | Begin special polygon |
| `PolyEnd` | 161 | 0 | NULL | End special polygon |
| `PolyIgnore` | 163 | 0 | NULL | Ignore following polygon data |
| `PolySmooth` | 164 | 1 | `TPolyVerbRec` | Mark that the polygon should be smoothed and indicate whether to frame, fill, and/or close |
| `PolyClose` | 165 | 0 | NULL | Mark the polygon as closed |
| `RotateBegin` | 200 | 8 | `TRotationRec` | Begin rotated port |
| `RotateEnd` | 201 | 0 | `NULL` | End rotation |
| `RotateCenter` | 202 | 8 | `TCenterRec` | Offset to center of rotation |
|  |  |  |  |  |
| Line-drawing picture comments |  |  |
| `DashedLine` | 180 | Size of a `TDashedLineRec` record | `TDashedLineRec` | Draw following line as dashed |
| `DashedStop` | 181 | 0 | `NULL` | End dashed lines |
| `SetLineWidth` | 182 | 4 | `TLineWidthHdl` | Set fractional line widths |
|  |  |  |  |  |
| PostScript picture comments are provided only for LaserWriter 8 compatibility. |
| `PostScriptBegin` | 190 | 0 | `NULL` | Set driver state to PostScript |
| `PostScriptEnd` | 191 | 0 | `NULL` | Restore QuickDraw state |
| `PostScriptHandle` | 192 | Size of the PostScript data in handle | a handle | PostScript data referenced by handle |
| `PostScriptFile` | 193 | Size of the PostScript data in handle | a handle | Filename referenced by handle |
| `TextIsPostScript` | 194 | 0 | `NULL` | If compatible with LaserWriter8, QuickDraw text is sent as PostScript |
| `PSBeginNoSave` | 196 | 0 | `NULL` | Set driver state to PostScript |
|  |  |  |  |  |
| ColorSync picture comments |  |  |
| `cmBeginProfile` | 220 | variable | version 1 profile data | Begin ColorSync profile; not supported in Mac OS X |
| `cmEndProfile` | 221 | 0 | `NULL` | End ColorSync profile; not supported in Mac OS X |
| `cmEnableMatching` | 222 | 0 | `NULL` | Begin ColorSync color matching |
| `cmDisableMatching` | 223 | 0 | `NULL` | End ColorSync color matching |
| `cmComment` | 224 | variable | a handle | Contents are a selector with data following |

[Next](Document%20Revision%20History.md)[Previous](Printing%20Tasks.md)


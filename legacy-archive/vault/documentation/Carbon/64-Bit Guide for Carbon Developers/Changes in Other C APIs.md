---
title: 64-Bit Guide for Carbon Developers
apple_id: TP40004381
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon64BitGuide/OtherAPIChanges/OtherAPIChanges.html
archived_at: '2026-07-15T05:22:31.471878Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Guide for Carbon Developers](Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md)


[Next](Document%20Revision%20History.md)[Previous](Changes%20in%20the%20Human%20Interface%20Toolbox.md)

# Changes in Other C APIs

This chapter discusses 64-bit changes in other C APIs commonly used by Carbon applications. The APIs are listed in alphabetical order.

__CoreServices: Aliases.h__

Alias Manager functions that use the `FSSpec` type or other deprecated types such as `CInfoPBPtr` are not available to 64-bit applications. Refer to _[Alias Manager Reference](https://developer.apple.com/documentation/coreservices/carbon_core/alias_manager)_ for detailed information about function availability.

__ApplicationServices: AppleEvents.h and related headers__

__Carbon: AEInteraction.h__

If your 64-bit application uses the Apple Event Manager:

- For custom event types, you need to make sure that the data types they use have explicit sizes.
- You must use the preferred numeric Apple event descriptor types. For example, you need to use `typeSInt32` instead of `typeLongInteger`. For more information, see `ApplicationServices/AE/AEDataModel.h`.
- The use of the `FSSpec` type in Apple events is discouraged; you should change your code to use `FSRef`. Type coercions into `typeFSS` by Apple events are not supported.
- The amount of data passed in an Apple event is still restricted to 4 gigabytes.

__AGL: agl.h and related headers__

Apple Graphics Library is a windowing system interface for OpenGL, specifically designed for the Carbon environment. AGL is not supported for use in 64-bit applications. For information about setting up an OpenGL drawing environment in Cocoa, see _[Cocoa Drawing Guide](../../Cocoa/Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_. For comprehensive information about OpenGL support in OS X, and for detailed examples of how to integrate OpenGL into a Cocoa application, see _[OpenGL Programming Guide for Mac](../../Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_.

__ApplicationServices: ATSFont.h, ATSTypes.h__

Apple Type Services for Fonts functions that use the `FSSpec` type are deprecated and are not available to 64-bit applications. The `ATSPoint` data type is defined as `CGPoint` in 64-bit applications.

__ApplicationServices: ATSUnicode.h and related headers__

Most functions in ATSUI are not available to 64-bit applications. Refer to _ATSUI Reference_ for detailed information about function availability. You should use Core Text or, if possible, the Cocoa text system. To learn about these technologies, see _[Core Text Programming Guide](../../Strings%20Text%20Fonts/Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_ and _[Text Layout Programming Guide](../../Cocoa/Text%20Layout%20Programming%20Guide/Introduction%20to%20Text%20Layout%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tq2i)_.

__CoreServices: CFNetwork.h and related headers__

Several CFNetwork functions now return the standard `CFIndex` type. The `CFNetDiagnosticStatus` type has changed to use the `CFIndex` type.

__CoreServices: CodeFragments.h__

The Code Fragment Manager is not available to 64-bit applications. You should use the Mach-O executable format instead. For more information, see _[Mach-O Programming Topics](../../Developer%20Tools/Mach-O%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjz)_.

__CoreServices: Collections.h__

Unlike most other managers, the Collection Manager is not being expanded to 64-bit byte counts; it continues to take and return 32-bit byte counts. Function parameters that are pointers are, of course, expanded to 64 bits.

If you’re currently using the Collection Manager, consider updating your software to use Core Foundation collection types such as CFMutableArray. For more information, see _[Collections Programming Topics for Core Foundation](../../Core%20Foundation/Collections%20Programming%20Topics%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdi2i)_.

__Carbon: ColorPicker.h__

Carbon applications use the Color Picker Manager to display a color selection window. The Color Picker Manager is not supported for use in 64-bit applications. You should use Cocoa to display the standard color selection window. For more information, see _[Color Programming Topics](../../Cocoa/Color%20Programming%20Topics/Introduction%20to%20Color%20Programming%20Topics%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4de2i)_.

__ApplicationServices: ColorSync.h and related headers__

__Carbon: CMCalibrator.h__

Many ColorSync Manager functions, data types, and constants that are rarely used, no longer recommended, or dependent on deprecated data types such as `FSSpec` are not available to 64-bit applications. For example, the following are no longer available:

- Older versions of profile search and profile-identifier search functions. Use the profile iteration function [CMIterateColorSyncFolder](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804904-cmiteratecolorsyncfolder) instead.
- Older versions of functions that convert from one color model to another. Use the conversion functions in `CMFloatBitmap.h` instead.
- Several functions that set default profiles.
- The function [CMGetCWInfo](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805097-cmgetcwinfo), because the data structure it returns is obsolete.
- The entire color management scripting plug-in API. You should use Image I/O and Quartz 2D instead. For more information, see _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
- The CMCalibrator API to make custom display color calibration plug-ins available in Displays Preferences. There is no replacement.

__CoreServices: Components.h__

Component Manager functions that use the `FSSpec` type, as well as four other obsolete functions, are not available to 64-bit applications. The following table lists these functions and their replacements:

| Removed Function | Replacement Function |
| --- | --- |
| `RegisterComponentFile` | `RegisterComponentFileRef` |
| `RegisterComponentFileEntries` | `RegisterComponentFileRefEntries` |
| `ComponentFunctionImplemented` | `CallComponentCanDo` |
| `GetComponentVersion` | `CallComponentVersion` |
| `ComponentSetTarget` | `CallComponentTarget` |
| `GetComponentIconSuite` | `GetIconRefFromComponent` |

On 64-bit architectures, the packing mechanism for the parameters described by the `ComponentParameters` structure has changed. The `params` array is a true array with 64-bit arguments. The number of arguments is computed by dividing the value in the `paramSize` field by `sizeof(long)`, which is 8 bytes in a 64-bit component. If you’re writing a 64-bit component and you supply a glue function that’s used to build the `ComponentParameters` structure, you need to update your glue code.

__CoreAudio: CoreAudio.h and related headers__

__AudioToolbox: AudioToolbox.h and related headers__

__AudioUnit: AudioUnit.h and related headers__

In the Core Audio framework, the Apple-supplied Carbon views (the generic Carbon view, and the EQ and DLS Synth custom views) are not available to 64-bit applications. In general, functions that use the `FSSpec` type are not available.

In the Audio Toolbox framework, the following are not available:

- The API declared in `AUMIDIController.h`
- The API declared in `DefaultAudioOutput.h`
- Three functions in `MusicPlayer.h`:

  - `MusicSequenceLoadSMF`
  - `MusicSequenceLoadSMFData`
  - `MusicSequenceSaveSMF`
- Two functions in `AUGraph.h`:

  - [AUGraphSetRenderNotification](https://developer.apple.com/documentation/audiotoolbox/audio_unit_processing_graph_services/1805624-augraphsetrendernotification)
  - [AUGraphRemoveRenderNotification](https://developer.apple.com/documentation/audiotoolbox/audio_unit_processing_graph_services/1805618-augraphremoverendernotification)

In the Audio Unit framework, the following are not available:

- The API declared in `AUNTComponent.h` (Version 1 audio units created for OS X v10.0 will not work in 64-bit applications)
- The function `AudioUnitRemovePropertyListener` in `AUComponent.h`

__CoreFoundation: CoreFoundation.h and related headers__

Four Core Foundation scalar types are changing from 32 bits to 64 bits on 64-bit architectures: `CFTypeID`, `CFOptionFlags`, `CFHashCode`, and `CFIndex`. Although the `CFOptionFlags` type is growing, the high 32 bits may not be used for several years, because flag parameters defined in the upper range will not be usable by 32-bit programs.

__CoreServices: DateTimeUtils.h, UTCUtils.h__

Most of the functions in Date, Time, and Measurement Utilities have been superseded by Core Foundation functions and are not available to 64-bit applications. For information about replacements, see _Date, Time, and Measurement Utilities Reference_.

__CoreServices: Files.h__

The Desktop Manager is not available to 64-bit applications. You should use Icon Services and Launch Services instead. For more information, see _[Obtaining and Using Icons With Icon Services](../Obtaining%20and%20Using%20Icons%20With%20Icon%20Services/Introduction%20to%20Obtaining%20and%20Using%20Icons%20With%20Icon%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjw)_ and _[Launch Services Programming Guide](../Launch%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojz)_.

__CoreServices: Files.h__

The Device Manager is not available in OS X v10.5 and later. The functions formerly declared in `Devices.h` have been moved into the 32-bit File Manager and deprecated. You should use the File Manager instead.

__ApplicationServices: Dictionary.h__

The Dictionary Manager is deprecated in OS X v10.5 and is not available to 64-bit applications. For related information, see [Language Analysis Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltcmy).

Dictionary Services lets you create your own custom dictionaries that users can access through the Dictionary application. You also use these services to access dictionaries programatically and to support user access to dictionary look-up through a contextual menu. To learn more about Dictionary Services, see _[Dictionary Services Programming Guide](../../User%20Experience/Dictionary%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcnjs)_.

__ApplicationServices: Displays.h__

The Display Manager is deprecated and is not available to 64-bit applications. The `GDHandle` data type, and functions that use this type, are no longer available. You must use the `CGDirectDisplayID` data type and Quartz Display Services instead. For more information, see _[Quartz Display Services Reference](https://developer.apple.com/documentation/coregraphics/quartz_display_services)_.

__CoreServices: Files.h__

In the File Manager, deprecated functions as well as a number of data types and constants are not available to 64-bit applications. Refer to _File Manager Reference_ for detailed information about function availability.

The `FSSpec` data type is replaced by the opaque `FSRef` type. (The `FSSpec` type continues to exist so that functions that merely pass along an `FSSpec` object don't have to change.) Functions that actually use or provide `FSSpec` information are deprecated. Functions that operate on Pascal strings are also deprecated. The File Manager provides replacement functions that use the `FSRef` type and Unicode strings to facilitate the 64-bit transition.

Many functions that return reference numbers now return a standard data type called `FSIORefNum`, which is defined as a 16-bit value on 32-bit architectures and a 32-bit value on 64-bit architectures. Another new standard type, `FSVolumeRefNum`, is defined as a 16-bit value on all architectures. You should start using the `FSIORefNum` and `FSVolumeRefNum` types to store reference numbers in your applications.

__CoreServices: Folders.h__

The deprecated functions in the Folder Manager are not available to 64-bit applications. Refer to _Folder Manager Reference_ to learn which functions are deprecated.

A new function named `GetFolderNameUnicode` replaces `GetFolderName`.

__ApplicationServices: Fonts.h__

The Font Manager is not available to 64-bit applications. You should use Core Text instead. For more information, see _[Core Text Programming Guide](../../Strings%20Text%20Fonts/Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_.

__Carbon: FontPanel.h__

Carbon applications use Fonts Window Services to display a font selection window. Fonts Window Services is not supported for use in 64-bit applications. You should use Cocoa to display the standard Fonts window. For more information, see _[Font Panel Programming Topics](../../Cocoa/Font%20Panel%20Programming%20Topics/Introduction%20to%20Font%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeytm2i)_.

__ApplicationServices: Icons.h__

__CoreServices: IconsCore.h, IconStorage.h__

Icon Utilities functions and data types, which are based on QuickDraw, are not available to 64-bit applications. These include data types that support classic icon formats such as `'ICON'`, `'cicn'`, and icon suites, and functions that use these data types. You must use the `IconRef` data type or a CGImage to represent an icon.

Deprecated functions in Icon Services are not available to 64-bit applications. Refer to _Icon Services and Utilities Reference_ to learn which functions are deprecated.

__Carbon: ImageCapture.h and related headers__

In `ICAApplication.h`, the following opaque types are defined as `UInt32` instead of as pointers:

```
ICAConnectionID
ICAEventDataCookie
ICAObject
ICAProperty
ICAScannerSessionID
ICASessionID
```


__Carbon: KeychainHI.h__

__CoreServices: KeychainCore.h__

The Keychain Manager function `KCMakeKCRefFromFSSpec` is not available to 64-bit applications. Note that the Keychain Manager has been superseded by Keychain Services. For more information, see _Keychain Services Programming Guide_.

__ApplicationServices: LanguageAnalysis.h__

The Language Analysis Manager is not available to 64-bit applications. You should use CFStringTokenizer in the Core Foundation framework instead. For more information, see _[CFStringTokenizer Reference](https://developer.apple.com/documentation/corefoundation/cfstringtokenizer)_.

CFStringTokenizer was introduced in OS X v10.5 to support typical tasks of internationalized applications. CFStringTokenizer let you tokenize a string of text into words, sentences or paragraphs in a language-neutral way (that is, you can tokenize a string without knowing the language.) It supports languages such as Japanese and Chinese that do not delimit words by spaces, and it can de-compound German compounds. You can obtain a Latin transcription for tokens. CFStringTokenizer also provides language identification.

__CoreServices: LaunchServices.h and related headers__

In Launch Services, two obsolete fields in the `LSItemInfoRecord` data structure are not available to 64-bit applications.

__CoreServices: FixMath.h, Math64.h, fp.h, ToolUtils.h__

Several existing functions in Mathematical and Logical Utilities have been changed to take arguments of type `SInt32` instead of type `long`, or to return a value of type `SInt32` instead of type `long`. For example, see the functions `Fix2Long` and `Long2Fix` in `CoreServices/CarbonCore/FixMath.h`.

__CoreServices: OSUtils.h__

The deprecated functions in Memory Management Utilities are not available to 64-bit applications. Refer to _Memory Management Utilities Reference_ to learn which functions are deprecated.

The function `MakeDataExecutable` is not available. You should use the BSD function [mprotect](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mprotect.2.html#//apple_ref/doc/man/2/mprotect) instead.

__CoreServices: MacMemory.h__

The deprecated Memory Manager functions are not available to 64-bit applications. Refer to _Memory Manager Reference_ to learn which functions are deprecated. Several obsolete data structures such as `Zone` are also not available.

The `BlockMove`, `BlockMoveData`, and `BlockZero` family of functions are not available; use the BSD functions [memmove](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/memmove.3.html#//apple_ref/doc/man/3/memmove) and [bzero](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/bzero.3.html#//apple_ref/doc/man/3/bzero) instead.

Pointer-based data types such as `Ptr` and `Handle` are now 64-bit types.

__CoreServices: Multiprocessing.h, MultiprocessingInfo.h__

Two Multiprocessing Services data types formerly defined as `UInt32` have changed:

```
typedef ItemCount TaskStorageIndex;
typedef LogicalAddress TaskStorageValue;
```

The function `MPDataToCode` is not available to 64-bit applications. You should use the BSD function [mprotect](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mprotect.2.html#//apple_ref/doc/man/2/mprotect) instead.

In OS X v10.5, the Carbon Printing Manager has been divided into two C APIs called Carbon Printing and Core Printing.

Carbon Printing is used by Carbon applications to present a user interface for printing. Carbon Printing includes functions to display the Page Setup and Print dialogs, and to execute a print loop that displays a print status dialog.

Core Printing is used for printing tasks that do not display a user interface. Any application can use this API, although Cocoa applications rarely need to use it.

Printing API changes that affect 64-bit applications are described below.

__Carbon: PMApplication.h, PMApplicationDeprecated.h__

Carbon Printing is not available to 64-bit applications. A 64-bit application with a Cocoa user interface should use Cocoa to display and customize printing dialogs, and to execute print jobs. For information on printing in Cocoa, see _[Printing Programming Guide for Mac](../../Cocoa/Printing%20Programming%20Guide%20for%20Mac/About%20Printing%20on%20the%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4dg2i)_.

__ApplicationServices: PMCore.h, PMCoreDeprecated.h, PMDefinitions.h, PMDefinitionsDeprecated.h__

Core Printing is available to 64-bit applications. However, most deprecated functions, data types, and constants are not available. Refer to _[Core Printing Reference](https://developer.apple.com/documentation/applicationservices/core_printing)_ for detailed information about function availability.

Deprecated functions include:

- Functions that use or assume the availability of QuickDraw
- Functions used to interleave PostScript and QuickDraw commands (the so-called “PICT with PostScript” document format)
- Functions that act on a current session rather than an explicit `PMPrintSession` object
- Functions that act on a current printer rather than an explicit `PMPrinter` object
- Functions that use or return Mac OS 9–style print records
- Functions that use or return handles
- A number of functions relevant only in Mac OS 9 and earlier

Some additional changes have been made in the OS X printing system that are related to 64-bit software development:

- You cannot build a 64-bit version of a printing dialog extension based on the CFPlugIn architecture described in _[Extending Printing Dialogs](../../Printing/Extending%20Printing%20Dialogs/Introduction%20to%20Extending%20Printing%20Dialogs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzz)_. If you’re a printer vendor and you want to build a 64-bit version of a plug-in that adds custom panes to the Print dialog, you need to use the newer Cocoa-based printing dialog extension API. For more information, see the header file `Carbon/Print/PDEPluginInterface.h` and the sample project _OutputBinsPDE_, which is located in `/Developer/Examples/Printing/Printer`.
- To get information from PostScript printer description (PPD) files in a 64-bit application, you must use CUPS instead of PPDLib. See the functions, data types, and constants declared in `/usr/include/cups/ppd.h`.
- If you plan to write a 64-bit printer driver, you must write a CUPS filter instead of a traditional printer module. Note that there is no specific need to have a 64-bit driver unless you think you will get better performance or need access to larger amounts of memory.
- You cannot build a 64-bit version of a printer browser. You can use the function [PMServerLaunchPrinterBrowser](https://developer.apple.com/documentation/applicationservices/1460175-pmserverlaunchprinterbrowser) to display the standard printer browser.

__ApplicationServices: Processes.h__

Several Process Manager data structures with fields that refer to the `FSSpec` type are not available to 64-bit applications. The Process Manager provides 64-bit versions of these data structures with fields that refer to the `FSRef` type.

__ApplicationServices: QuickDraw.h and related headers__

QuickDraw graphics ports are not supported. Consequently, the entire drawing API has been removed from 64-bit QuickDraw. Functions that manipulate regions and simple data structures (`Point` and `Rect`) are still available, but you cannot use QuickDraw to draw in a 64-bit application. To learn about other drawing APIs, see _[Quartz Programming Guide for QuickDraw Developers](../Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers/Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojy)_ and _[Cocoa Drawing Guide](../../Cocoa/Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_.

PICT files cannot be rendered any more, not even with the function `QDPictDrawToCGContext`. They need to be converted to PDF or other image formats supported by Image I/O.

The Picture Utilities API is deprecated and is not available to 64-bit applications.

__QuickTime: QuickTime.h and related headers__

The QuickTime C APIs are not available to 64-bit applications. For these applications, the QuickTime Kit Objective-C classes are the primary interface into QuickTime. For example, if you use the QuickTime C API to play movies and you want to build a 64-bit version of your application, use the QuickTime Kit and display the movie in a Cocoa window. The QuickTime Kit is described in detail in _[QuickTime Kit Programming Guide](../../Quick%20Time/QuickTime%20Kit%20Programming%20Guide/Introduction%20to%20QuickTime%20Kit%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbv)_.

Almost all of the QuickTime Kit classes, methods, and functions are supported, with one major exception: methods that take or return native QuickTime identifiers (in particular, `Movie`, `MovieController`, `Track`, and `Media`). For example, you cannot use the `quickTimeMovie` method in the `QTMovie` class to “dip down” into the QuickTime C APIs.

The following is a complete list of the QuickTime Kit methods that are not available to 64-bit applications.

In the `QTMovie` class:

```objc
+ (id)movieWithQuickTimeMovie:(Movie)movie
    disposeWhenDone:(BOOL)dispose
    error:(NSError **)errorPtr;
- (id)initWithQuickTimeMovie:(Movie)movie
    disposeWhenDone:(BOOL)dispose
    error:(NSError **)errorPtr;
- (Movie)quickTimeMovie;
- (MovieController)quickTimeMovieController;
```

In the `QTTrack` class:

```objc
+ (id)trackWithQuickTimeTrack:(Track)track
    error:(NSError **)errorPtr;
- (id)initWithQuickTimeTrack:(Track)track
    error:(NSError **)errorPtr;
- (Track)quickTimeTrack;
```

In the `QTMedia` class:

```objc
+ (id)mediaWithQuickTimeMedia:(Media)media
    error:(NSError **)errorPtr;
- (id)initWithQuickTimeMedia:(Media)media
    error:(NSError **)errorPtr;
- (Media)quickTimeMedia;
```

The QuickTime Music Architecture (QTMA) is not available to 64-bit applications. As an alternative, you should use Core Audio for audio and MIDI application development.

__CoreServices: Resources.h__

Resource Manager functions that use the `FSSpec` type for creating and opening resource files are not available to 64-bit applications.

The Resource Manager introduces several new standard types:

- `ResFileRefNum` is an alias for `FSIORefNum` (see [File Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknlte).) `ResFileRefNum` is used to return resource file reference numbers.
- `ResID` is used to represent resource IDs.
- `ResAttributes` is used to represent a resource attribute such as `resChangedBit`.
- `ResFileAttributes` is used to represent a resource file attribute such as `mapReadOnlyBit`.
- `ResCount` is used to represent a resource count.
- `ResourceIndex` is used to specify an item in a list of resources.

No code changes are necessary in order for your application to call functions that use these new types. You should adapt the `ResFileRefNum` type to declare local instances of resource reference numbers.

__CoreServices: Script.h__

The Script Manager is deprecated, and most Script Manager functions are not available to 64-bit applications. Refer to _Script Manager Reference_ for detailed information about function availability.

__Carbon: Sound.h__

The Sound Manager is deprecated in OS X v10.5 and is not available to 64-bit applications. You should use Core Audio instead. For general information about Core Audio, see _[Core Audio Overview](../../Music%20Audio/Core%20Audio%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzx)_. For information about writing audio units, see _[Audio Unit Programming Guide](../../Music%20Audio/Audio%20Unit%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzy)_.

__Carbon: SpeechRecognition.h__

Some function parameter types have changed; for example, parameters of type `Size` are now of type `SInt32`. User-supplied callback data is now of type `SRefCon`.

__ApplicationServices: SpeechSynthesis.h__

A number of parameters and fields of type `long` are now of type `SInt32`. User-supplied callback data is now of type `SRefCon`.

__Carbon: TypeSelect.h__

__CoreServices: TextUtils.h, StringCompare.h, NumberFormatting.h__

Most of the functions in Text Utilities are deprecated and are not available to 64-bit applications. (The only exception is the [Munger](https://developer.apple.com/documentation/coreservices/1588638-munger) utility function.) Refer to _Text Utilities Reference_ to learn about replacements for deprecated functions.

__CoreServices: Threads.h__

The underlying data type of `ThreadID` has changed from `UInt32` to `long`:

```
typedef unsigned long ThreadID;
```

As a result, the `ThreadID` type is still mapped directly to the `pthread_t` type in 64-bit applications.

__Carbon: Translation.h, TranslationExtensions.h__

The Translation Manager and Translation Extensions are not available to 64-bit applications. You should use Translation Services instead. For more information, see the header file `ApplicationServices/HIServices/TranslationServices.h`.

__Accelerate: vImage.h and related headers__

The vImage framework declares the data type [vImage_AffineTransform](https://developer.apple.com/documentation/accelerate/vimage_affinetransform) to serve the same purpose as the Quartz data type [CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgaffinetransform). The intent is that applications could use these types interchangeably. For example, you might use Quartz functions to operate on values of type `vImage_AffineTransform`.

In 64-bit applications, these data types are no longer interchangeable. Values of type `vImage_AffineTransform` contain single-precision quantities while values of type `CGAffineTransform` contain double-precision quantities. As a result, 64-bit applications that assume these types are interchangeable may fail.

[Next](Document%20Revision%20History.md)[Previous](Changes%20in%20the%20Human%20Interface%20Toolbox.md)


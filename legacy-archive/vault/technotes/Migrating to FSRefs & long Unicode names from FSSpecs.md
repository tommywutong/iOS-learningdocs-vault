---
title: Migrating to FSRefs & long Unicode names from FSSpecs
apple_id: DTS10003097
resource_type: Technical Note
platform: macOS
topic: null
technology: null
published: '2003-05-06'
source_url: https://developer.apple.com/library/archive/technotes/tn2078/_index.html
archived_at: '2026-07-26T19:53:50.004149Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2078

# Migrating to FSRefs & long Unicode names from FSSpecs

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Long Unicode name support, large file access, and better performance are a few of the reasons you should consider migrating your legacy `FSSpec` based File Manager code to take advantage of `FSRef` based APIs.

There are some things you should know about file paths, Unicode and interoperability before you make the transition.

The first two sections of this document cover many of the issues you will face during the transition, offer code examples, and detailed descriptions of the options you have, as well as tips and tricks to easing the transition. The last section delves a deeper into Unicode.

[FSSpecs and FSRefs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjukq2ujfhu4mi)[Differences between FSSpecs and FSRefs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyyq)[Converting FSSpecs to FSRefs and back](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyza)[How can I tell if an FSRef is valid?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyzq)[How can I tell if they reference the same item?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjy2a)[Getting the parent directory of an FSRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjy2q)[How do I specify non-existent items, such as files you plan to create?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjy3a)[Apple events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjy3q)[Persistent storage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjy4a)[Can I continue to use FSSpecs?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjy4q)[How do I get an FSRef to my application?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyyta)[LaunchServices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyytc)[Getting a file path](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyyte)[Additional Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyytg)[FSRefs and long Unicode file names](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjukq2ujfhu4mjv)[How do I get the name of an item from an FSRef?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyytk)[Notes about Unicode strings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyytm)[Truncating Unicode strings by width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyyto)[Truncating Unicode strings by length](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyytq)[Concatenation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyyts)[Determining the width of strings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyzda)[Encoding file names in other formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyzdc)[How file names are encoded](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyzde)[Notes About Using Unicode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjukq2ujfhu4mru)[What is Unicode?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyzdi)[Unicode terminology](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyzdk)[Truncating and other manipulations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyzdm)[Final Unicode comments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjvkqstivbviskpjyzdo)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wugsbrfvjukq2ujfhu4mrz)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## FSSpecs and FSRefs

Contains information and coding techniques useful in migrating your source from FSSpecs to using FSRefs.

### Differences between FSSpecs and FSRefs

__Listing 1__  Definitions in Files.h.

```swift
struct FSSpec {   short         vRefNum;   long          parID;   StrFileName   name; /* a Str63 */ };  struct FSRef {   UInt8         hidden[80]; /* private to File Manager*/ };
```

The differences which will probably have the biggest impact on your code are that FSRefs cannot represent items which do not exist, and an `FSRef` is an opaque data structure defined as an array of 80 bytes, the content of which is not documented. In particular, an `FSRef` does not contain the name of the item to which it refers. This comes as no surprise when you consider that Mac OS X allows the use of file names containing Unicode characters, with a maximum length of 255 UniChars (see FSRefs and long Unicode file names for more on this).

### Converting FSSpecs to FSRefs and back

To convert an `FSSpec` to an `FSRef`:

`err = FSpMakeFSRef( &fsSpec, &fsRef );`

To obtain an `FSSpec` from an `FSRef`:

`err = FSGetCatalogInfo( &fsRef, kFSCatInfoNone, NULL, NULL, &fsSpec, NULL );`

### How can I tell if an FSRef is valid?

```
 Boolean FSRefIsValid( const FSRef &fsRef ) {       return ( FSGetCatalogInfo( &fsRef, kFSCatInfoNone, NULL, NULL, NULL, NULL ) == noErr );  }
```

### How can I tell if they reference the same item?

```
if ( FSCompareFSRefs( &fsRef1, &fsRef2 ) == noErr )
```

### Getting the parent directory of an FSRef

```
err = FSGetCatalogInfo( &fsRef, kFSCatInfoNone, NULL, NULL,            NULL, &parentFSRef );
```

### How do I specify non-existent items, such as files you plan to create?

__Listing 2__  Common technique adopted by many developers is to create a pseudo `FSSpec` like structure or class.

```swift
struct ExtFSRef {   FSRef           parentFSRef;   HFSUniStr255    name; };  class CExtFSRef {   FSRef           parentFSRef;   HFSUniStr255    name;   // ... Some useful member functions };
```

This technique is especially useful when storing data returned by `NavCreatePutFileDialog()`. The Unicode-savvy file creation APIs take a parent `FSRef` and a `HFSUniStr255` name, so just store the information that way right up front instead of converting to a `CFURLRef` and then converting to parent `FSRef` and `HFSUniStr255` later. You could equally well save the name as a `CFStringRef` since that's how it's stored in the NavReplyRecord, and then create a `HFSUniStr255` when you need it:

__Listing 3__  Storing file names as CFStringRefs instead of `HFSUniStr255`

```swift
struct ExtFSRef2 {   FSRef            parentFSRef;   CFStringRef      name; };  class CExtFSRef2 {   FSRef            parentFSRef;   CFStringRef      name;   // ... Some useful member functions };
```

### Apple events

Don't pass FSRefs in AppleEvents. Because FSRefs are not guaranteed to be valid across processes in Mac OS X you shouldn't send them in AppleEvents. [MoreFinderEvents](https://developer.apple.com/samplecode/Sample_Code/Archive/Interapplication_Comm/Finder/MoreFinderEvents.htm) contains code demonstrating how to pass aliases to the Finder through AppleEvents.

### Persistent storage

Like FSSpecs, FSRefs are not guaranteed to be valid across boots in Mac OS 9 or Mac OS X, across processes in Mac OS X, or even across separate launches of the same application in Mac OS X, so don't use them when you need persistent storage. For persistent storage, aliases are still the recommended approach. ([Alias Manager](https://developer.apple.com/documentation/Carbon/Files/AliasManager/aliasmanager.html))

### Can I continue to use FSSpecs?

Yes, they continue to be valid file references. An `FSSpec`'s name can be mangled, though, so don't use them to get file names for either storage or display. The names are mangled when the real name can't be stored in a Pascal string, or if the name is longer than 31 characters. In the latter case you get names like "A really, really long file#23A4". The `FSSpec` still works, it just doesn't contain the item's real name.

It depends on your application.

The QuickTime and Drag Manager APIs still require FSSpecs, but creating temporary FSSpecs from FSRefs is an easy operation.

You have to use the new `NavCreateXXX` APIs introduced in Navigation Services 3.0. ([Navigation Services](https://developer.apple.com/documentation/Carbon/Files/NavigationServices/navigationservices.html)) You also have to use these if you want to implement open and save dialogs as sheets (though they don't need to be sheets)

__Note:__ If you use kWindowModalityAppModal for any of the new `NavCreateXXX` APIs, `NavDialogRun()` will not return until the user dismisses the dialog. If you use kWindowModalityWindowModal to get sheet behavior, `NavDialogRun()` will return immediately in Mac OS X. That is, NavDialogRun gets it going, but then it runs like a normal window. This behavior is often overlooked when transitioning from application modal behavior to window modal (sheet) behavior.

### How do I get an FSRef to my application?

__Listing 4__  If it's a single CFM binary, you can get an `FSSpec` and convert it to an `FSRef`.

```
OSErr GetCurrentProcessFSSpec( FSSpec *outFSSpec ) {   ProcessSerialNumber  currentProcess = { 0, kCurrentProcess };   ProcessInfoRec       processInfo;   processInfo.processInfoLength = sizeof(ProcessInfoRec);   processInfo.processName       = NULL; /* don't need the process name */   processInfo.processAppSpec    = outFSSpec;   return GetProcessInformation( &currentProcess, &processInfo ); }
```

If your application is bundled, this will get an `FSRef` for your executable, not the bundle folder.

__Listing 5__  How to get the `FSRef` to your application bundle, CFM or Mach-O.

```
OSErr GetMyBundleFSRef( FSRef *outFSRef )  {   ProcessSerialNumber  currentProcess = { 0, kCurrentProcess };    return( GetProcessBundleLocation( &currentProcess, outFSRef ) );  }
```

### LaunchServices

LaunchServices is a set of Mac OS X-only APIs for working with files. Read through <LaunchServices.h> if you want to be up-to-date on files in Mac OS X, where there are some new issues like bundled applications, display names, new rules for application binding, and so on. [Technical Note TN2017, 'Using Launch Services for discovering document binding and launching applications'](https://developer.apple.com/technotes/tn/tn2017.html), also contains a wealth of information.

__Listing 6__  Packages are kind of a cross between files and folders. Use `LSCopyItemInfoForRef()` to determine if a folder is a package/bundled application in Mac OS X.

```
OSStatus LSIsApplication( const FSRef *inRef, Boolean *outIsApplication,                           Boolean *outIsBundled ) {   LSItemInfoRecord  info;   OSStatus  err = LSCopyItemInfoForRef( inRef, kLSRequestBasicFlagsOnly,                                         &info );    if ( err == noErr )   {     *outIsApplication = ( kLSItemInfoIsApplication &info.flags ) != 0;     *outIsBundled = ( kLSItemInfoIsPackage &info.flags ) != 0;   }   return( err ); }
```

Use `LSCopyItemInfoForRef()` with the `kLSRequestTypeCreator` mask to get the type and creator of a bundled application. `FSGetCatalogInfo()` treats bundled applications as ordinary folders and hence can't be used to access the file type or creator of a bundled application.

Use `LSGetApplicationForItem()` to determine what application would be used by the Finder to open a file.

Use `LSGetApplicationForInfo()` to locate the application which would be used to open files with a certain extension, type, or creator. This is necessary in OS X because of the complex rules for binding files to applications, and the fact that users can specify an application for opening all files with a given creator, type, and/or extension, thereby overriding the default behavior you might expect.

Use `LSCopyDisplayNameForRef()` to get the name the Finder displays. i.e., if the 'Always show file extensions' option is off in Finder Preferences, the name returned by `LSCopyDisplayNameForRef()` will not contain the extension if it's not displayed in the Finder. For example, TextEdit's full name is "TextEdit.cpp", but `LSCopyDisplayNameForRef()` will return "TextEdit". As with all Launch Services APIs, `LSCopyDisplayNameForRef()` is not available in Mac OS 9, but the Mac OS 9 Finder always displays the file system name, so it's not a issue there.

### Getting a file path

The most straightforward approach to getting a files path is with the API:

```
OSStatus FSRefMakePath( const FSRef * ref, UInt8 * path, UInt32            maxPathSize);
```

This will return back a UTF8 encoded path to the object specified by the `FSRef`. The drawback to using this routine is that you must pass in a fixed size buffer, and therefore will return an error if the path to be returned will not fit in the buffer. Be sure to read the comments in Files.h for this API, as they imply it can return mangled names in Mac OS 9. Files.h also describes when `FSRefMakePath()` returns an HFS file path (Mac OS 9), and when it returns a POSIX path in UTF-8 format (Mac OS X).

__Listing 7__  Another way get to a file's path is to create a `CFURLRef` and use that to obtain the path

```
CFURLRef url = CFURLCreateFromFSRef( kCFAllocatorDefault, &fsRef ); CFStringRef cfString = NULL; if ( url != NULL ) {   cfString = CFURLCopyFileSystemPath( url, inPathStyle );   CFRelease( url ); }
```

__Listing 8__   If you want an HFS-style path in Mac OS X, or you find `FSRefMakePath()` doesn't work all the time, you can use something like the this code to build the path yourself.

```
Boolean GetPathManually( const FSRef *inFSRef, CFMutableStringRef ioPath,                          UniChar inSepChar ) {   //ioPath should already be created with CFStringCreateMutablexxx.   FSCatalogInfo catalogInfo;   int           n;   int           i;   HFSUniStr255 names[100];   FSRef         localRef  = *inFSRef;   OSStatus      err       = noErr;    CFStringDelete( ioPath, CFRangeMake( 0, CFStringGetLength( ioPath ) ) );   for ( n=0 ; err==noErr && catalogInfo.nodeID != fsRtDirID && n<100 ; n++ )   {     err = FSGetCatalogInfo( &localRef, kFSCatInfoNodeID, &catalogInfo,                            &names[n], nil, &localRef );   }   for ( i = n - 1; i >= 0; --i )   {     CFStringAppendCharacters( ioPath, names[i].unicode, names[i].length );     if ( i > 0 )       CFStringAppendCharacters( ioPath, &inSepChar, 1 );   }   return( err == noErr ); }
```

### Additional Notes

Because the contents of an `FSRef` are undocumented, those contents may vary depending on the format of the volume containing the item to which the `FSRef` refers. Currently, an `FSRef` for an item on a HFS or HFS+ volume continues to remain valid even if the item is moved or renamed, presumably because such an `FSRef` contains a file or directory ID for the item and a volume reference number. In this regard an `FSRef` is more robust than an `FSSpec`. Note that this is the current state of affairs, and as with any opaque data structure, any of this could change at any time and should not be relied upon. If you need robust file tracking, use aliases. ([Alias Manager](https://developer.apple.com/documentation/Carbon/Files/AliasManager/Alias_Manager/alias_manager/index.html))

__CarbonLib__ If you're contemplating a CarbonLib project, be aware that FSRefs were introduced with the new HFS+ APIs in Mac OS 9 and hence require Mac OS 9 or later. CarbonLib provides a wrapper around `FSRef` APIs, but does not actually implement them, so you can't use CarbonLib to get `FSRef` functionality in any version of Mac OS 8.

[Back to Top](#)

## FSRefs and long Unicode file names

### How do I get the name of an item from an FSRef?

__Listing 9__  Getting a Unicode name

```
OSErr FSRefGetName( const FSRef *fsRef, HFSUniStr255 *name ) {   return( FSGetCatalogInfo(fsRef, kFSCatInfoNone, NULL, name, NULL, NULL) ); }  An HFSUniStr255 is defined as:  struct HFSUniStr255 {   UInt16 length; /* number of unicode characters */   UniChar unicode[255]; /* unicode characters */ };
```

Since HFSUniStr255s occupy 512 bytes you may want to store names as CFStringRefs:

```
strRef = CFStringCreateWithCharacters( kCFAllocatorDefault, name.unicode,            name.length );
```

In addition to conserving memory, Core Foundation provides a wealth of APIs for testing and manipulating CFStrings. There are no such APIs for working with `HFSUniStr255` file names. The assumption is that you will do such testing and manipulation with a `CFStringRef` or `CFMutableStringRef` obtained from an `HFSUniStr255`.

Note that `FSGetCatalogInfo()` returns the __file system name__. The Mac OS X Finder doesn't always display file name extensions. The name the Finder displays is called the __display name__. If you want the display name in Mac OS X see the LaunchServices section.

Note: While technically correct, he definition of `HFSUniStr255` is somewhat misleading. HFS+ disks store file names as UTF-16 in an Apple-modified form of Normalization Form D (decomposed). This means a single Unicode code point value can occupy more than one UniChar in an `HFSUniStr255`, which in turn means a file name may be limited to fewer than 255 characters as perceived by normal readers. (see read more about Unicode character terminology)

### Notes about Unicode strings

Strictly speaking, the issue here is independent of the source of the CFString, but they are often encountered when deal with Unicode file names.

Many of us need to display the name of a file or folder in our applications. Since Mac OS X supports long Unicode file names, there are some related issues. Unicode has a number of things going on under the hood which you wouldn't expect if you are unfamiliar with Unicode and how it works. The following are some basic points to remember when working with Unicode file names.

A Unicode string (speaking from the viewpoint of Mac OS X) is a string of UniChars. Such a string can be converted to and from a `CFStringRef` or a `CFMutableStringRef`.

A single Unicode code point may require multiple UniChars, so never modify a Unicode string by simply removing a range of UniChars or inserting UniChars at an arbitrary offset. Doing so can produce a string which is not what you expect, incorrect, or even leave you with a string which is no longer a legal Unicode string.

### Truncating Unicode strings by width

__Listing 10__  To truncate a file name to a desired width prior to drawing it or other use, convert the name to a `CFMutableStringRef` and use `TruncateThemeText()` to truncate it.

```
Boolean TruncateWidth( CFMutableStringRef ioString, SInt16 inMaxWidth,                        TruncCode inTruncCode, ThemeFontID inThemeFontID,                        ThemeDrawState inState ) {   Boolean  wasTruncated = false;   OSStatus err = TruncateThemeText( ioString, inThemeFontID, inState,           inMaxWidth, inTruncCode, &wasTruncated );   return( (err == noErr) && wasTruncated ); }
```

### Truncating Unicode strings by length

Unfortunately, there is no simple API available which you can use to correctly truncate a Unicode string to a certain number of characters. To truncate a file name based on length, you'll need to convert the name to a UniChar string and use `UCFindTextBreak()` with `kUCTextBreakClusterMask`. (this actually requires a bit of code, but this is a summary) Using `UCFindTextBreak()` ensures you won't truncate the string in the middle of a cluster, the smallest group of UniChars which have semantic meaning. Any time you remove one or more characters from a cluster, at best you change its meaning, and at worst you end up with something which isn't legal in Unicode. (see grapheme clusters)

### Concatenation

You can concatenate Unicode strings at will. The individual pieces will retain their original meaning. For example, you can append ".txt" to a Unicode string without changing the meaning of the existing string. Or, you could concatenate English and Arabic (a right-to-left script) and get the desired result.

### Determining the width of strings

Don't try to estimate the width of a Unicode string based on the number of UniChars in the string. In addition to the issues of combining characters and surrogate pairs, Unicode text can contain invisible characters which are not rendered. Unicode goes beyond the simple encoding of characters and scripts. There are are several code point values which can be used to provide hints or instructions to rendering software, but are never rendered themselves.

__Listing 11__  How to determine the width of a Unicode string stored as a CFString.

```
SInt16 GetWidth( const CFStringRef inString, ThemeFontID inFontID,                  ThemeDrawState inState ) {   Point  pt;   SInt16 baseline;   GetThemeTextDimensions( inString, inFontID, inState, false, &pt,                           &baseline );   return( pt.h ); }
```

### Encoding file names in other formats

Again, this is not an issue limited to file names, but is included because people often make the mistake of assuming that the size of the buffer needed when converting a CFString to a C string is `CFStringGetSize( cfString )`. Because a single UniChar can (and will for all but the simplest Latin characters) require multiple characters when encoded with `kCFStringEncodingUTF8`.

__Listing 12__  The correct way to determine the required buffer size using `CFStringGetMaximumSizeForEncoding()`.

```
char* CreateUTF8CStringFromCFString( const CFStringRef inString ) {   // DisposePtr(cStr) must be called when with the result if successful.   CFIndex  max;   char     *cStr;   CFIndex  len   = CFStringGetLength( inString );    max = CFStringGetMaximumSizeForEncoding( len, kCFStringEncodingUTF8 );   cStr = NewPtr( 1 + max );   if ( cStr != NULL )   {     if ( !CFStringGetCString(inString, cStr, len, kCFStringEncodingUTF8) )     {       DisposePtr( cStr );       cStr = NULL;     }     if ( cStr != NULL )       SetPtrSize( cStr, strlen( cStr ) + 1 );       // SetPtrSize has no effect in Mac OS X if the new size is less than       // the old size. If you really want to shrink the pointer to the       // amount actually used, inMac OS X, you'll need to allocate a new       // pointer whose size is strlen(cStr) + 1 and copy the contents of       // cStr to the new pointer.   }   return( cStr ); }
```

### How file names are encoded

HFS+ disks store file names as UTF-16 in an Apple-modified form of Normalization Form D (decomposed). This form excludes certain compatibility decompositions and parts of the symbol blocks, in order to assure round-trip of file names to Mac OS encodings (applications using the HFS APIs assume they get the same bytes out that they put in).

In Mac OS X 10.2, the decomposition rules used were changed from Unicode 2.0.x (based on an intermediate draft) plus the above-mentioned Apple modifications, to Unicode 3.2 plus the above-mentioned Apple modifications. The Unicode Consortium has committed to not changing the decomposition rules after Unicode 3.2, so we shouldn't have to do this again. The change from 2.0.x to 3.2 was necessary because A) lots of new decompositions had been added, and B) the 2.0.x data was full of errors.

Other file systems use different storage formats. UFS disks use UTF-8, HFS disks use Mac OS encodings. AFP (AppleShare) uses Mac OS encodings prior to 3.0, and UTF-16 for 3.0 or later.

[Back to Top](#)

## Notes About Using Unicode

This could also be called "Unicode for File Names," as there are many aspects of Unicode which won't be discussed here because they aren't needed if all you're doing with Unicode is working with file names in Mac OS X. The reason for focusing on this particular area is that it's an area which every Mac OS X application should be prepared to support. If you're writing a Unicode-savvy word processor, you're going to need a lot more understanding than any glossary notes. Most of the information presented here is from the book, Unicode Demystified by Richard Gillam. However, its 800 pages and may be overkill if all you want to do is handle file names properly in Mac OS X.

### What is Unicode?

Unicode is a universal text encoding standard for representing written language in a format suitable for use and storage by computers. It's goal is to allow the encoding of all, or at least all significant forms of writing in use in the world today, as well as many which are no longer used, but are of historical or scholarly interest.

### Unicode terminology

There are two major challenges for those new to Unicode. First is getting a handle on the terminology. Second, and directly related to the first, is understanding what constitutes a character in a written language, in Unicode, and how the two are related (i.e., how characters are encoded in Unicode). English is one of the simplest—if not the simplest—of all the world's languages to write and encode for use by computers. Understandably, people whose native language is English tend to make incorrect assumptions about how other languages are written and encoded into Unicode. When code is written based on those false assumptions, it will not work correctly for all languages. Following are a some terms often used in Unicode discussions.

A __character__ is an abstract linguistic concept such as "the Latin letter A" or "the Chinese character for 'sun.'"

Every character defined in the Unicode standard is assigned a single 21-bit abstract __code point value__. Apple refers to a code point value in Unicode as a Unicode Scalar Value.

MacTypes.h has the following to say:

__Table 1__  MacTypes.h definitions

| typedef UInt32 | UnicodeScalarValue |
| typedef UInt16 | UniChar |
| typedef UInt16 | UTF16Char |
| UniChar | A 16-bit Unicode code value in the default UTF-16 format. |
| UTF16Char | UnicodeScalarValues 0-0xFFFF are expressed in UTF-16 format using a single UTF16Char with the same value. UnicodeScalarValues 0x10000-0x10FFFF are expressed in UTF-16 format using a pair of UTF16Chars - one in the high surrogate range (0xD800-0xDBFF) followed by one in the low surrogate range (0xDC00-0xDFFF). All of the characters defined in Unicode versions through 3.0 are in the range 0-0xFFFF and can be expressed using a single UTF16Char, thus the term "Unicode character" generally refers to a UniChar = UTF16Char. |

In Unicode terms: The __Basic Multilingual Plane__ or __BMP__ refers to the code point values from U+0000 to U+FFFF, and was the original Unicode encoding space. Later, when it was realized additional space was needed, 16 __supplementary planes__ were added to the encoding space and code point values were extended from 16 bits to 21 bits. Hence the BMP contains the code point values which can be converted to corresponding UniChars by simply lopping off the upper five zero bits. The nth supplementary plane contains code point values in the range U+n0000 to U+nFFFF, where n ranges from 0x01 - 0x10. Thus the full range of Unicode code point values is 0x0000 to 0x10FFFF. Planes 3 - 13 (U+30000 to U+EFFFF) are currently unused and available for future use.

__Surrogate pairs__ - Unicode sets aside 2,048 code point values (U+8000 - U+DFFF) in the BMP which will never be assigned to actual characters. They are reserved for defining paired combinations to represent characters outside the BMP. These values are called __surrogates__. The first 1,024 surrogate values (U+D800-U+DBFF) are called __high-surrogates__, and the remaining 1,024 surrogate values (U+DC00-U+DFFF) are called __low-surrogates__. A supplementary-plane character (a character not in the BMP) is represented by high-surrogate followed by a low-surrogate. Note that surrogates are only legal when they occur in high-low pairs. An unpaired surrogate is considered an error in Unicode.

In case you're just dying to know how a 21–bit code point value is mapped to a surrogate pair, it goes like this: First, subtract 0x10000 from the original code point value to get a 20–bit value. Split those 20 bits down the middle to get two 10–bit sequences. The first 10–bit sequence becomes the lower 10 bits of the high-surrogate value and the second 10–bit sequence becomes the lower 10 bits of the low-surrogate value.

__Combining marks__ are code point values which do not represent characters themselves, but apply a mark to a base character which precedes them. Diacritical marks are one kind of combining mark. For example:

é = e + ´ (U+0065 LATIN SMALL LETTER E) + (U+0301 COMBINING ACUTE ACCENT)

A __grapheme__ is a minimal writing unit is some written language; a mark that is considered a single "character" by an average reader or writer of a particular written language.

A __grapheme cluster__ is a sequence of one or more Unicode code points (UniChars) that should be treated as an indivisible unit by most processes operating on Unicode text, such as searching and sorting, hit testing, arrow key movement, and so on. References to the term "cluster" in documentation, or in the headers, such as `kUCTextBreakClusterMask`, refer to grapheme clusters.

A __glyph__ is a concrete visual representation of a character. It's what you see on screen or in print.

### Truncating and other manipulations

The original intention was for Unicode to represent every character with a single UniChar, but it quickly became obvious that it isn't possible to do this. More than 95,000 characters are now defined in the Unicode standard, far more than can be represented by a single 16-bit value. Only code point values in the Basic Multilingual Plane can be represented with a single UniChar. Furthermore, a significant number of characters are represented as a base character plus one or more diacritical or other combining marks. Assuming that there's a one-to-one relationship between characters and the Unicode characters which represent them leads to one of the most common errors in code which manipulates Unicode strings, which is to truncate a Unicode string at an inappropriate offset. Always use appropriate Unicode-aware APIs to truncate a Unicode string or determine where to insert or remove characters. (See truncation comments.)

(Encoded into Unicode as is done by the File Manager in Mac OS X, the string "résumé" contains eight UniChars. Lop off the last one and you'll have a Unicode string for "résume".)

### Final Unicode comments

A 32-bit encoding would allow Unicode to provide a direct 1-1 correspondence between code point values and their encoded values, which in turn would eliminate most of those issues about where you can safely insert or truncate characters. 21 bits provides support for about a million characters, roughly 10 times the number currently encoded. But the smallest data type used by computers that's easily manipulated and will contain 21 bits is 32 bits. The downside is that an encoding scheme based on a 32-bit data type would waste a lot of space. If Unicode used a 32-bit encoding scheme—which would allow encoding every code point value in a single code value—it would waste at least 11 bits for every character, and at least 16 bits/character for the vast majority of characters in common use. For example, a 32-bit based `HFSUniStr255` (used for file names in Mac OS X) would occupy 1022 bytes, even though most file names consist of less than 40-50 characters in the BMP.

[Back to Top](#)

## References

- [Laurence Harris, SkyTag Software](http://www.skytag.com/)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2003-05-06 | New document that answers and coding techniques to commonly asked questions about adopting FSRefs and long file names. |


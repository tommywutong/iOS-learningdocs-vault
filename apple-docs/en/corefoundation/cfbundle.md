---
title: CFBundle
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbundle
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundle.json'
content_hash: 'sha256:bb9009d3dd82830e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundle

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFBundle
```

## Overview

CFBundle allows you to use a folder hierarchy called a bundle to organize and locate many types of application resources including images, sounds, localized strings, and executable code. In macOS, bundles can also be used by CFM applications to load and execute functions from Mach-O frameworks. You can use bundles to support multiple languages or execute your application on multiple operating environments.

You create a bundle object using one of the `CFBundleCreate...` functions. CFBundle provides several functions for finding resources within a bundle. The [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>) function returns the location of a resource of the specified name and type, and in the specified subdirectory. Use [CFBundleCopyResourceURLForLocalization](<cfbundlecopyresourceurlforlocalization(__________).md>) to restrict the search to a specific localization name. Use [CFBundleCopyResourceURLsOfType](<cfbundlecopyresourceurlsoftype(______).md>) to get the locations of all resources of a specified type.

CFBundle provides functions for getting bundle information, such as its identifier and information dictionary. Use the [CFBundleGetIdentifier](<cfbundlegetidentifier(__).md>) function to get the identifier of a bundle, and the [CFBundleGetInfoDictionary](<cfbundlegetinfodictionary(__).md>) function to get its information dictionary. The principal intended purpose for locating bundles by identifier is so that code (in frameworks, plugins, etc.) can find its own bundle.

You can also obtain locations of subdirectories in a bundle represented as CFURL objects. The [CFBundleCopyExecutableURL](<cfbundlecopyexecutableurl(__).md>) function returns the location of the application’s executable. The functions [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>), [CFBundleCopySharedFrameworksURL](<cfbundlecopysharedframeworksurl(__).md>), [CFBundleCopyPrivateFrameworksURL](<cfbundlecopyprivateframeworksurl(__).md>), [CFBundleCopySharedSupportURL](<cfbundlecopysharedsupporturl(__).md>), and [CFBundleCopyBuiltInPlugInsURL](<cfbundlecopybuiltinpluginsurl(__).md>) return the location of a bundle’s subdirectory containing resources, shared frameworks, private frameworks, shared support files, and plug-ins respectively.

Other functions are used to manage localizations. The [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) and [CFBundleCopyLocalizationsForURL](<cfbundlecopylocalizationsforurl(__).md>) functions return a localized string from a bundle’s strings file. The [CFBundleCopyLocalizationsForPreferences](<cfbundlecopylocalizationsforpreferences(____).md>) function returns the localizations that CFBundle would prefer, given the specified bundle and user preference localizations.

Unlike some other Core Foundation opaque types with similar Cocoa Foundation names (such as CFString and `NSString`), [Bundle](../foundation/bundle.md) objects cannot be cast (“toll-free bridged”) to CFBundle objects.

Unlike `NSBundle`, which does not support unloading (because the Objective C runtime does not support the unloading of Objective C code), you can unload CFBundle objects.

[CFBundleGetFunctionPointerForName](<cfbundlegetfunctionpointerforname(____).md>) and related calls automatically load a bundle if it is not already loaded. When the last reference to the CFBundle object is released and it is finally deallocated, then the code will be unloaded if it is still loaded and if the executable is of a type that supports unloading. If you keep this in mind, and if you make sure that everything that uses the bundle keeps a retain on the CFBundle object, then you can just use the bundle naturally and never have to worry about when it is loaded and unloaded.

On the other hand, if you want to manually manage when the bundle is loaded and unloaded, then you can use [CFBundleLoadExecutable](<cfbundleloadexecutable(__).md>) and [CFBundleUnloadExecutable](<cfbundleunloadexecutable(__).md>)—although this technique is not recommended. These functions force immediate loading and unloading of the executable (if it has not already been loaded/unloaded, and in the case of unloading if the executable is of a type that supports unloading). If you do this, then the code calling `CFBundleUnloadExecutable` is responsible for making sure that there are no remaining references to anything in the bundle’s code before it is unloaded. In the previous approach, by contrast, this responsibility can be distributed to the individual code sections that use the bundle, by making sure that each one keeps its own retain on the CFBundle object.

One further point about CFBundle reference counting: if you are taking the first approach, but do not actually wish the bundle’s code to be unloaded (as is often the case), or if you are taking the second approach of manually managing the unloading yourself, then in many cases you do not actually have to worry about releasing a CFBundle object. CFBundle instances are uniqued, so there is only one CFBundle object for a given bundle, and rarely are there so many bundles being considered at once that the memory usage for CFBundle objects would be significant. There are cases in which a process could create CFBundle objects for potentially an unlimited number of bundles, and such processes would wish to balance retains and releases carefully, but such cases are likely to be rare.

Note that it is best to compile any unloadable bundles with the flag `-fno-constant-cfstrings`—see [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i) for more details.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating and Accessing Bundles

- [CFBundleCreate](<cfbundlecreate(____).md>) — Creates a CFBundle object.
- [CFBundleCreateBundlesFromDirectory](<cfbundlecreatebundlesfromdirectory(______).md>) — Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [CFBundleGetAllBundles](<cfbundlegetallbundles().md>) — Returns an array containing all of the bundles currently open in the application.
- [CFBundleGetBundleWithIdentifier](<cfbundlegetbundlewithidentifier(__).md>) — Locate a bundle given its program-defined identifier.
- [CFBundleGetMainBundle](<cfbundlegetmainbundle().md>) — Returns an application’s main bundle.

### Loading and Unloading a Bundle

- [CFBundleIsExecutableLoaded](<cfbundleisexecutableloaded(__).md>) — Obtains information about the load status for a bundle’s main executable.
- [CFBundlePreflightExecutable](<cfbundlepreflightexecutable(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [CFBundleLoadExecutable](<cfbundleloadexecutable(__).md>) — Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [CFBundleLoadExecutableAndReturnError](<cfbundleloadexecutableandreturnerror(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
- [CFBundleUnloadExecutable](<cfbundleunloadexecutable(__).md>) — Unloads the main executable for the specified bundle.

### Finding Locations in a Bundle

- [CFBundleCopyAuxiliaryExecutableURL](<cfbundlecopyauxiliaryexecutableurl(____).md>) — Returns the location of a bundle’s auxiliary executable code.
- [CFBundleCopyBuiltInPlugInsURL](<cfbundlecopybuiltinpluginsurl(__).md>) — Returns the location of a bundle’s built in plug-in.
- [CFBundleCopyExecutableURL](<cfbundlecopyexecutableurl(__).md>) — Returns the location of a bundle’s main executable code.
- [CFBundleCopyPrivateFrameworksURL](<cfbundlecopyprivateframeworksurl(__).md>) — Returns the location of a bundle’s private Frameworks directory.
- [CFBundleCopyResourcesDirectoryURL](<cfbundlecopyresourcesdirectoryurl(__).md>) — Returns the location of a bundle’s Resources directory.
- [CFBundleCopySharedFrameworksURL](<cfbundlecopysharedframeworksurl(__).md>) — Returns the location of a bundle’s shared frameworks directory.
- [CFBundleCopySharedSupportURL](<cfbundlecopysharedsupporturl(__).md>) — Returns the location of a bundle’s shared support files directory.
- [CFBundleCopySupportFilesDirectoryURL](<cfbundlecopysupportfilesdirectoryurl(__).md>) — Returns the location of the bundle’s support files directory.

### Locating Bundle Resources

- [CFBundleCloseBundleResourceMap](<cfbundleclosebundleresourcemap(____).md>) — Closes an open resource map for a bundle. _(deprecated)_
- [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>) — Returns the location of a resource contained in the specified bundle.
- [CFBundleCopyResourceURLInDirectory](<cfbundlecopyresourceurlindirectory(________).md>) — Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [CFBundleCopyResourceURLsOfType](<cfbundlecopyresourceurlsoftype(______).md>) — Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [CFBundleCopyResourceURLsOfTypeInDirectory](<cfbundlecopyresourceurlsoftypeindirectory(______).md>) — Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.
- [CFBundleCopyResourceURLForLocalization](<cfbundlecopyresourceurlforlocalization(__________).md>) — Returns the location of a localized resource in a bundle.
- [CFBundleCopyResourceURLsOfTypeForLocalization](<cfbundlecopyresourceurlsoftypeforlocalization(________).md>) — Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [CFBundleOpenBundleResourceFiles](<cfbundleopenbundleresourcefiles(______).md>) — Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps. _(deprecated)_
- [CFBundleOpenBundleResourceMap](<cfbundleopenbundleresourcemap(__).md>) — Opens the non-localized and localized resource files (if any) for a bundle in a single resource map. _(deprecated)_

### Managing Localizations

- [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) — Returns an array containing a bundle’s localizations.
- [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) — Returns a localized string from a bundle’s strings file.
- [CFBundleCopyLocalizationsForPreferences](<cfbundlecopylocalizationsforpreferences(____).md>) — Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [CFBundleCopyLocalizationsForURL](<cfbundlecopylocalizationsforurl(__).md>) — Returns an array containing the localizations for a bundle or executable at a particular location.
- [CFBundleCopyPreferredLocalizationsFromArray](<cfbundlecopypreferredlocalizationsfromarray(__).md>) — Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.

### Managing Executable Code

- [CFBundleGetDataPointerForName](<cfbundlegetdatapointerforname(____).md>) — Returns a data pointer to a symbol of the given name.
- [CFBundleGetDataPointersForNames](<cfbundlegetdatapointersfornames(______).md>) — Returns a C array of data pointer to symbols of the given names.
- [CFBundleGetFunctionPointerForName](<cfbundlegetfunctionpointerforname(____).md>) — Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [CFBundleGetFunctionPointersForNames](<cfbundlegetfunctionpointersfornames(______).md>) — Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [CFBundleGetPlugIn](<cfbundlegetplugin(__).md>) — Returns a bundle’s plug-in.

### Getting Bundle Properties

- [CFBundleCopyBundleURL](<cfbundlecopybundleurl(__).md>) — Returns the location of a bundle.
- [CFBundleGetDevelopmentRegion](<cfbundlegetdevelopmentregion(__).md>) — Returns the bundle’s development region from the bundle’s information property list.
- [CFBundleGetIdentifier](<cfbundlegetidentifier(__).md>) — Returns the bundle identifier from a bundle’s information property list.
- [CFBundleGetInfoDictionary](<cfbundlegetinfodictionary(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleGetLocalInfoDictionary](<cfbundlegetlocalinfodictionary(__).md>) — Returns a bundle’s localized information dictionary.
- [CFBundleGetValueForInfoDictionaryKey](<cfbundlegetvalueforinfodictionarykey(____).md>) — Returns a value (localized if possible) from a bundle’s information dictionary.
- [CFBundleCopyInfoDictionaryInDirectory](<cfbundlecopyinfodictionaryindirectory(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleCopyInfoDictionaryForURL](<cfbundlecopyinfodictionaryforurl(__).md>) — Returns the information dictionary for a given URL location.
- [CFBundleGetPackageInfo](<cfbundlegetpackageinfo(______).md>) — Returns a bundle’s package type and creator.
- [CFBundleGetPackageInfoInDirectory](<cfbundlegetpackageinfoindirectory(______).md>) — Returns a bundle’s package type and creator without having to create a CFBundle object.
- [CFBundleCopyExecutableArchitectures](<cfbundlecopyexecutablearchitectures(__).md>) — Returns an array of CFNumbers representing the architectures a given bundle provides.
- [CFBundleCopyExecutableArchitecturesForURL](<cfbundlecopyexecutablearchitecturesforurl(__).md>) — Returns an array of CFNumbers representing the architectures a given URL provides.
- [CFBundleGetVersionNumber](<cfbundlegetversionnumber(__).md>) — Returns a bundle’s version number.

### Getting the CFBundle Type ID

- [CFBundleGetTypeID](<cfbundlegettypeid().md>) — Returns the type identifier for the CFBundle opaque type.

### Data Types

- [CFBundleRefNum](cfbundlerefnum.md) — Type that identifies a distinct reference number for a resource map.

### Constants

- [Information Property List Keys](information-property-list-keys.md) — Standard keys found in a bundle’s information property list file.
- [Architecture Types](1537096-architecture-types.md) — Constants that identify executable architecture types.

## See Also

### Related Documentation

- [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
- [CFFileDescriptor](cffiledescriptor.md)

---
title: Creating color spaces that ensure color matching.
apple_id: DTS10003466
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2005-10-04'
source_url: https://developer.apple.com/library/archive/qa/qa1396/_index.html
archived_at: '2026-07-18T02:30:31.429505Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1396

# Creating color spaces that ensure color matching.

## Q:  How do I create color spaces so that I can make sure my colors are matched?

A: How do I create color spaces so that I can make sure my colors are matched?

To work with color effectively and to understand the Quartz 2D functions for using color spaces and color, you should be familiar with the terminology discussed in the [Color Management Overview](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/csintro/index.html). That document discusses color perception, color values, device-independent and device color spaces, the color-matching problem, rendering intent, color management modules, and ColorSync.

Devices (displays, printers, scanners, cameras) don't treat color the same way; each has its own range of colors that the device can produce faithfully. A color produced on one device might not be able to be produced on another device. The best way to avoid these kinds of problems is to use a color space with a "calibration profile" ? for example, an ICCBased color space which uses an ICC profile for calibration. In such a case the system will be able to translate color from this color space to any destination (e.g. display) in the best possible way. Unless there is already a profile for the destination, the best solution is to use a generic color space. Generic color spaces, for example Generic RGB or Generic CYMK, are color spaces that will always be calibrated when copied to a destination device.

New in Mac OS X 10.4, the constants `kCGColorSpaceGenericRGB`, `kCGColorSpaceGenericCMYK` and `kCGColorSpaceGenericGray` can be used to easily create generic RGB, CYMK, and Gray color spaces using the `CGColorSpaceCreateWithName` function. These constants are not available in 10.3.9 or earlier; if backwards compatibility is needed for systems before 10.4 use the code from Listing 2 to create color spaces from the generic ICC color profiles.

__Listing 1__  Creating a generic RGB color space using the kCGColorSpaceGenericRGB avalible in 10.4 and later

```
CGColorSpaceRef genericRGBColorSpace = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB);
```

Device color spaces are device-dependent and assume all colors are already calibrated for the destination device. The following APIs create device-dependent color spaces and should be avoided: `CGColorSpaceCreateDeviceRGB()`, `CGColorSpaceCreateDeviceCYMK()`, and `CGColorSpaceCreateDeviceGray()`.

Mac OS X provides the following ICC profile files in the directory `'/System/Library/ColorSync/Profiles/'`:

- Generic CMYK Profile.icc
- Generic Gray Profile.icc
- Generic Lab Profile.icc
- Generic RGB Profile.icc
- Generic XYZ Profile.icc
- sRGB Profile.icc

While there isn't a simple API for creating ICC color space from an ICC color profile, Listing 2 provides an example of how to create one.

__Listing 2__  Creating a color space from an ICC profile, and examples for creating a Generic RGB Color Space and an sRGB Color Space.

```
CGColorSpaceRef CreateICCColorSpaceFromPathToProfile (const char * iccProfilePath) {      CMProfileRef    iccProfile = (CMProfileRef) 0;     CGColorSpaceRef iccColorSpace = NULL;     CMProfileLocation loc;      // Specify that the location of the profile will be a POSIX path to the profile.     loc.locType = cmPathBasedProfile;      // Make sure the path is not larger then the buffer     if(strlen(iccProfilePath) > sizeof(loc.u.pathLoc.path))         return NULL;      // Copy the path the profile into the CMProfileLocation structure     strcpy (loc.u.pathLoc.path, iccProfilePath);      // Open the profile     if (CMOpenProfile(&iccProfile, &loc) != noErr)     {         iccProfile = (CMProfileRef) 0;                 return NULL;     }      // Create the ColorSpace with the open profile.     iccColorSpace = CGColorSpaceCreateWithPlatformColorSpace( iccProfile );      // Close the profile now that we have what we need from it.     CMCloseProfile(iccProfile);      return iccColorSpace; }  CGColorSpaceRef CreateColorSpaceFromSystemICCProfileName(CFStringRef profileName) {     FSRef pathToProfilesFolder;     FSRef pathToProfile;      // Find the Systems Color Sync Profiles folder     if(FSFindFolder(kOnSystemDisk, kColorSyncProfilesFolderType,              kDontCreateFolder, &pathToProfilesFolder) == noErr) {          // Make a UniChar string of the profile name         UniChar uniBuffer[sizeof(CMPathLocation)];         CFStringGetCharacters (profileName,CFRangeMake(0,CFStringGetLength(profileName)),uniBuffer);          // Create a FSRef to the profile in the Systems Color Sync Profile folder         if(FSMakeFSRefUnicode (&pathToProfilesFolder,CFStringGetLength(profileName),uniBuffer,             kUnicodeUTF8Format,&pathToProfile) == noErr) {                 char path[sizeof(CMPathLocation)];              // Write the posix path to the profile into our path buffer from the FSRef             if(FSRefMakePath (&pathToProfile,path,sizeof(CMPathLocation)) == noErr)                 return CreateICCColorSpaceFromPathToProfile(path);         }     }      return NULL; }  CGColorSpaceRef CreateICCGenericRGBColorSpace() {     return CreateColorSpaceFromSystemICCProfileName(CFSTR("Generic RGB Profile.icc")); }  CGColorSpaceRef CreateICCsRGBColorSpace() {      return CreateColorSpaceFromSystemICCProfileName(CFSTR("sRGB Profile.icc")); }
```

Offscreen caches are generally used to enhance performance, but if a color space is used to create an offscreen cache that doesn't match the display device, then every time the data is copied to the display device it must go though a color calibration process. Since every display device maps colors differently to the same color values, the optimum method is to ask the system for the display devices profile. Once the display devices profile is obtained, it can then be used to create a display color space which can be used to create a CGBitmapContext to be used as an offscreen cache. Listing 2 shows how to create a color space based on the current display profile.

__Listing 3__  Creating a color space that represents the main display

```
CGColorSpaceRef CreateSystemColorSpace () {     CMProfileRef sysprof = NULL;     CGColorSpaceRef dispColorSpace = NULL;      // Get the Systems Profile for the main display     if (CMGetSystemProfile(&sysprof) == noErr)     {         // Create a colorspace with the systems profile         dispColorSpace = CGColorSpaceCreateWithPlatformColorSpace(sysprof);          // Close the profile         CMCloseProfile(sysprof);     }      return dispColorSpace; }
```

Using "display color space", based on the current display profile, is telling the system that you don't want the color to be matched when it is copied to the screen, but you do want color matching when drawing to the offscreen cache. Since this "display color space" is based on the current display, if the cached data is going to be repeated on another system with a different display, the color appearance will be different because each device reacts differently to the same color values.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-10-04 | Added the new constants for creating generic RGB, CYMK, and Grey color spaces in 10.4 and later. |
| 2005-01-13 | New document that how to create color spaces that ensure color matching. |


---
title: GetProcAdress and OpenGL Entry Points
apple_id: DTS10001717
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2002-11-25'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1188.html
archived_at: '2026-07-18T02:38:17.448436Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > OpenGL](https://developer.apple.com/referencelibrary/GraphicsImaging/idxOpenGL-date.html)

|  |
| --- |
| Technical Q&A QA1188GetProcAdress and OpenGL Entry Points |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: __How can I get function pointers to OpenGL entry points?__  A: Getting function pointers to OpenGL entry points is a simple procedure from either Cocoa or Carbon. In the Cocoa or Carbon Mach-O you can use the existing NSLookupAndBindSymbol to get the address of an OpenGL entry point. Things are just slightly more complicated in Carbon CFM where you need to find the OpenGL Framework bundle and use the CFBundleGetFunctionPointerForName function to retrieve the actual function. The Carbon procedure works for both Mach-O and CFM binary formats without modification.  OpenGL has an expanding set of entry points, all of which are not exported by every version of Mac OS X. This technique of using function pointers, when combined with proper extension string and OpenGL version checking, allows developers to deploy across multiple Mac OS X versions whether or not the entry point is supported at link and/or runtime. Additionally, many developers coming from Windows or Linux have code which is designed to use functions like wglGetProcAddress to get function pointers to OpenGL entry points. This Q&A provides a solution to both these problems which makes using functions pointers on Mac OS X simple. Cocoa and Carbon versions of GetProcAddress for both Mach-O and CFM applications are shown in the listings below.  NSGLGetProcAddress is detailed in listing 1. The code first modifies the requested symbol name for standard name mangling conventions, then ensures the symbol is defined, and finally looks up the symbol and returns the appropriate pointer. Developers should ensure the pointer is valid (non-zero) prior to using it. Note, since the NSSymbol functions are part of the system framework and not part of Cocoa, NSGLGetProcAddress can be used for Mach-O Carbon applications as well as Cocoa ones.     |  | | --- | | ```  #import <mach-o/dyld.h>  #import <stdlib.h>  #import <string.h> void *NSGLGetProcAddress(const char *name) {     NSSymbol symbol;     char *symbolName;     // Prepend a '_' for the Unix C symbol mangling convention     symbolName = malloc (strlen (name) + 2);     strcpy(symbolName + 1, name);     symbolName[0] = '_';     symbol = NULL;     if (NSIsSymbolNameDefined (symbolName))         symbol = NSLookupAndBindSymbol (symbolName);     free (symbolName);     return symbol ? NSAddressOfSymbol (symbol) : NULL; } ``` | | __Listing 1__. NSGLGetProcAddress |     aglGetProcAddress, shown in listing 2, has three functions. The first, aglInitEntryPoints, sets up the bundle reference, the second, aglDellocEntryPoints, cleans up the bundle by releasing the reference and the third is the actual aglGetProcAddress function. Looking at aglInitEntryPoints, we see an initial setup, followed by a look up and work to find the Frameworks folder and to turn it into a CFURL, and finally creating the bundle and loading the executable. Once this is complete one can call aglGetProcAddress for any entry existing in the OpenGL Framework. On exit, the application should always de-allocate the bundle by calling aglDellocEntryPoints which unloads the bundle and releases the reference to it. This code requires Carbon and is designed for use with Mach-O and CFM Carbon applications.     |  | | --- | | ```  #include <Carbon/Carbon.h> CFBundleRef gBundleRefOpenGL = NULL;  // -------------------------  OSStatus aglInitEntryPoints (void) {     OSStatus err = noErr;     const Str255 frameworkName = "\pOpenGL.framework";     FSRefParam fileRefParam;     FSRef fileRef;     CFURLRef bundleURLOpenGL;      memset(&fileRefParam, 0, sizeof(fileRefParam));     memset(&fileRef, 0, sizeof(fileRef));      fileRefParam.ioNamePtr  = frameworkName;     fileRefParam.newRef = &fileRef;      // Frameworks directory/folder     err = FindFolder (kSystemDomain, kFrameworksFolderType, false,                       &fileRefParam.ioVRefNum, &fileRefParam.ioDirID);     if (noErr != err) {         DebugStr ("\pCould not find frameworks folder");         return err;     }     err = PBMakeFSRefSync (&fileRefParam); // make FSRef for folder     if (noErr != err) {         DebugStr ("\pCould make FSref to frameworks folder");         return err;     }     // create URL to folder     bundleURLOpenGL = CFURLCreateFromFSRef (kCFAllocatorDefault,                                             &fileRef);     if (!bundleURLOpenGL) {         DebugStr ("\pCould create OpenGL Framework bundle URL");         return paramErr;     }     // create ref to GL's bundle     gBundleRefOpenGL = CFBundleCreate (kCFAllocatorDefault,                                        bundleURLOpenGL);     if (!gBundleRefOpenGL) {         DebugStr ("\pCould not create OpenGL Framework bundle");         return paramErr;     }     CFRelease (bundleURLOpenGL); // release created bundle     // if the code was successfully loaded, look for our function.     if (!CFBundleLoadExecutable (gBundleRefOpenGL)) {         DebugStr ("\pCould not load MachO executable");         return paramErr;     }     return err; }  // -------------------------  void aglDellocEntryPoints (void) {     if (gBundleRefOpenGL != NULL) {         // unload the bundle's code.         CFBundleUnloadExecutable (gBundleRefOpenGL);         CFRelease (gBundleRefOpenGL);         gBundleRefOpenGL = NULL;     } }  // -------------------------  void * aglGetProcAddress (char * pszProc) {     return CFBundleGetFunctionPointerForName (gBundleRefOpenGL,                 CFStringCreateWithCStringNoCopy (NULL,                      pszProc, CFStringGetSystemEncoding (), NULL)); } ``` | | __Listing 2__. aglGetProcAddress |     Listings 3 and 4 show two code snippets which demonstrate the use of aglGetProcAddress and NSGLGetProcAddress for a few OpenGL entry points. Note both snippets are very similar, with aglGetProcAddress requiring the call to aglInitEntryPoints, to load the bundle, prior to retrieving a function pointer and then the call to aglDellocEntryPoints, to unload the bundle, prior to exiting the application. Otherwise these code examples are almost identical.     |  | | --- | | ``` #import "NSGLGetProcAddress.h" // header for get proc addr func in listing 1  static void InitEntryPoints (void); static void DeallocEntryPoints (void);  // function pointer typedefs     typedef void (*glBlendColorProcPtr)(GLclampf red,                                         GLclampf green,                                         GLclampf blue,                                         GLclampf alpha);     typedef void (*glBlendEquationProcPtr)(GLenum mode);     typedef void (*glDrawRangeElementsProcPtr)(GLenum mode,                                                GLuint start,                                                GLuint end,                                                GLsizei count,                                                GLenum type,                                                const GLvoid *indices);  // function pointer declarations // Note: One should not use the exact function names //       pfXXX is chosen to represent 'pointer to function'     glBlendColorProcPtr pfglBlendColor = NULL;     glBlendEquationProcPtr pfglBlendEquation = NULL;     glDrawRangeElementsProcPtr pfglDrawRangeElements  = NULL;  // ==========================  static void InitEntryPoints (void) {     pfglBlendColor = (glBlendColorProcPtr)                          NSGLGetProcAddress ("glBlendColor");     pfglBlendEquation = (glBlendEquationProcPtr)                             NSGLGetProcAddress ("glBlendEquation");     pfglDrawRangeElements = (glDrawRangeElementsProcPtr)                                 NSGLGetProcAddress ("glDrawRangeElements"); }  // -------------------------  static void DeallocEntryPoints (void) {     pfglBlendColor = NULL;     pfglBlendEquation = NULL;     pfglDrawRangeElements = NULL;; } ``` | | __Listing 3__. NSGLGetProcAddress Sample Usage |         |  | | --- | | ``` #include "aglGetProcAddress.h" // header for get proc addr funcs in listing 2  static OSStatus InitEntryPoints (void); static void DeallocEntryPoints (void);  // function pointer typedefs     typedef void (*glBlendColorProcPtr)(GLclampf red,                                         GLclampf green,                                         GLclampf blue,                                         GLclampf alpha);     typedef void (*glBlendEquationProcPtr)(GLenum mode);     typedef void (*glDrawRangeElementsProcPtr)(GLenum mode,                                                GLuint start,                                                GLuint end,                                                GLsizei count,                                                GLenum type,                                                const GLvoid *indices);  // function pointer declarations // Note: One should not use the exact function names //       pfXXX is chosen to represent 'pointer to function'     glBlendColorProcPtr pfglBlendColor = NULL;     glBlendEquationProcPtr pfglBlendEquation = NULL;     glDrawRangeElementsProcPtr pfglDrawRangeElements  = NULL;  // ==========================  static OSStatus InitEntryPoints (void) {     OSStatus err = aglInitEntryPoints (); //init bundle     if (noErr == err) {         pfglBlendColor = (glBlendColorProcPtr)                             aglGetProcAddress ("glBlendColor");         pfglBlendEquation = (glBlendEquationProcPtr)                                 aglGetProcAddress ("glBlendEquation");         pfglDrawRangeElements = (glDrawRangeElementsProcPtr)                                     aglGetProcAddress ("glDrawRangeElements");     }     return err; }  // -------------------------  static void DeallocEntryPoints (void) {     pfglBlendColor = NULL;     pfglBlendEquation = NULL;     pfglDrawRangeElements = NULL;;     aglDellocEntryPoints (); // dump bundle } ``` | | __Listing 4__. aglGetProcAddress Sample Usage |     One additional note on the use of function pointers for OpenGL entry points is worth understanding. Having a valid function pointer just means the entry point is exported by the OpenGL Framework, it has no bearing on whether that particular routine is supported and valid to call within an application. OpenGL applications should always check the current renderer extension string and/or OpenGL version number to confirm whether a particular feature is supported or not, prior to calling any OpenGL entry point (whether dynamically loaded or not). In summary, existence of the link time or runtime entry point is not an indication of specific feature support within a specific renderer  In summary, when deploying across multiple OS versions it is recommended CFM applications either weak link against the OpenGL stub libraries or use function pointers and MachO applications use function pointers for entry points that may not exist on all targeted OS versions to avoid launch time failures for undefined entry points.   ---  [Nov 25 2002] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

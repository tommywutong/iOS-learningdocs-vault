---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_entrypts/opengl_entrypts.html
archived_at: '2026-07-15T07:36:34.816370Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Document%20Revision%20History.md)[Previous](Updating%20an%20Application%20to%20Support%20the%20OpenGL%203.2%20Core%20Specification.md)

# Setting Up Function Pointers to OpenGL Routines

Function pointers to OpenGL routines allow you to deploy your application across multiple versions of OS X regardless of whether the entry point is supported at link time or runtime. This practice also provides support for code that needs to run cross-platform—in both OS X and Windows.

This appendix discusses the tasks needed to set up and use function pointers as entry points to OpenGL routines:

- [Obtaining a Function Pointer to an Arbitrary OpenGL Entry Point](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgiwvgvzs) shows how to write a generic routine that you can reuse for any OpenGL application on the Macintosh platform.
- [Initializing Entry Points](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgiwvgvzt) describes how to declare function pointer type definitions and initialize them with the appropriate OpenGL command entry points for your application.

Getting a pointer to an OpenGL entry point function is fairly straightforward from Cocoa. You can use the Dynamic Loader function `NSLookupAndBindSymbol` to get the address of an OpenGL entry point.

Keep in mind that getting a valid function pointer means that the entry point is exported by the OpenGL framework; it does not guarantee that a particular routine is supported and valid to call from within your application. You still need to check for OpenGL functionality on a per-renderer basis as described in [Detecting Functionality](Determining%20the%20OpenGL%20Capabilities%20Supported%20by%20the%20Renderer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgewvgvzr).

Listing C-1 shows how to use `NSLookupAndBindSymbol` from within the function `MyNSGLGetProcAddress`. When provided a symbol name, this application-defined function returns the appropriate function pointer from the global symbol table. A detailed explanation for each numbered line of code appears following the listing.

__Listing C-1__  Using `NSLookupAndBindSymbol` to obtain a symbol for a symbol name

```objc
#import <mach-o/dyld.h>
#import <stdlib.h>
#import <string.h>
void * MyNSGLGetProcAddress (const char *name)
{
    NSSymbol symbol;
    char *symbolName;
    symbolName = malloc (strlen (name) + 2); // 1
    strcpy(symbolName + 1, name); // 2
    symbolName[0] = '_'; // 3
    symbol = NULL;
    if (NSIsSymbolNameDefined (symbolName)) // 4
        symbol = NSLookupAndBindSymbol (symbolName);
    free (symbolName); // 5
    return symbol ? NSAddressOfSymbol (symbol) : NULL; // 6
}
```

Here's what the code does:

1. Allocates storage for the symbol name plus an underscore character (`'_'`). The underscore character is part of the UNIX C symbol-mangling convention, so make sure that you provide storage for it.
2. Copies the symbol name into the string variable, starting at the second character, to leave room for prefixing the underscore character.
3. Copies the underscore character into the first character of the symbol name string.
4. Checks to make sure that the symbol name is defined, and if it is, looks up the symbol.
5. Frees the symbol name string because it is no longer needed.
6. Returns the appropriate pointer if successful, or `NULL` if not successful. Before using this pointer, you should make sure that is it valid.

Listing C-2 shows how to use the `MyNSGLGetProcAddress` function from [Listing C-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgiwvgvzu) to obtain a few OpenGL entry points. A detailed explanation for each numbered line of code appears following the listing.

__Listing C-2__  Using `NSGLGetProcAddress` to obtain an OpenGL entry point

```objc
#import "MyNSGLGetProcAddress.h" // 1
static void InitEntryPoints (void);
static void DeallocEntryPoints (void);

// Function pointer type definitions
typedef void (*glBlendColorProcPtr)(GLclampf red,GLclampf green,
                        GLclampf blue,GLclampf alpha);
typedef void (*glBlendEquationProcPtr)(GLenum mode);
 typedef void (*glDrawRangeElementsProcPtr)(GLenum mode, GLuint start,
                GLuint end,GLsizei count,GLenum type,const GLvoid *indices);

glBlendColorProcPtr pfglBlendColor = NULL; // 2
glBlendEquationProcPtr pfglBlendEquation = NULL;
glDrawRangeElementsProcPtr pfglDrawRangeElements = NULL;

static void InitEntryPoints (void) // 3
{
    pfglBlendColor = (glBlendColorProcPtr) MyNSGLGetProcAddress
                                    ("glBlendColor");
    pfglBlendEquation = (glBlendEquationProcPtr)MyNSGLGetProcAddress
                                ("glBlendEquation");
    pfglDrawRangeElements = (glDrawRangeElementsProcPtr)MyNSGLGetProcAddress
                                ("glDrawRangeElements");
}
// -------------------------
static void DeallocEntryPoints (void) // 4
{
    pfglBlendColor = NULL;
    pfglBlendEquation = NULL;
    pfglDrawRangeElements = NULL;;
}
```

Here's what the code does:

1. Imports the header file that contains the `MyNSGLProcAddress` function from [Listing C-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgiwvgvzu).
2. Declares function pointers for the functions of interest. Note that each function pointer uses the prefix `pf` to distinguish it from the function it points to. Although using this prefix is not a requirement, it's best to avoid using the exact function names.
3. Initializes the entry points. This function repeatedly calls the `MyNSGLProcAddress` function to obtain function pointers for each of the functions of interest—`glBlendColor`, `glBlendEquation`, and `glDrawRangeElements`.
4. Sets each of the function pointers to `NULL` when they are no longer needed.

[Next](Document%20Revision%20History.md)[Previous](Updating%20an%20Application%20to%20Support%20the%20OpenGL%203.2%20Core%20Specification.md)


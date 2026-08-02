---
title: Uniform Type Identifiers Overview
apple_id: TP40001319
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreServices
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis.tasks/understand_utis_tasks.html
archived_at: '2026-07-15T07:32:26.905485Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Uniform Type Identifiers Overview](Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md)


[Next](Declaring%20New%20Uniform%20Type%20Identifiers.md)[Previous](Uniform%20Type%20Identifier%20Concepts.md)

# Adopting Uniform Type Identifiers

This chapter gives some guidelines for adopting uniform type identifiers in your application, and gives an overview of the utility functions used to manipulate UTIs.

Adopting UTIs in your application is a two-part process. You should use UTIs whenever you need to identify or exchange data, and you should declare specific UTIs for any proprietary types your application uses.

Apple uses UTIs throughout OS X. For example: building in UTI support for most data-interchange needs. For example, the following technologies all support UTIs:

- The Pasteboard Manager and Translation Services use UTIs to identify data types.
- Navigation Services allows you to specify UTIs for file filtering.
- Launch Services supports UTI-based document claims.
- NSView and NSWindow support UTI-based drag-and-drop promises.
- NSDocument, NSOpenPanel, NSSavePanel, and NSWorkspace all support UTIs.
- NSSound, NSImage and NSImageRep use UTIs to return supported data formats.

Further, Apple has deprecated most older mechanisms for identifying data in favor of UTIs.

If you have specific needs that are not addressed by the above, you can match types to UTIs in your own code. Typically this requires you to find a type with an alternate identifier (such as an `OSType`), create a UTI from that identifier, then check for conformance with UTIs defining the types your application can handle. For an example of how to do this, see [Navigation Services Tasks](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/NavServicesConcepts/ns_using/ns_using.html#//apple_ref/doc/uid/TP40000930-CH202) in _[Navigation Services Programming Guide](../../Carbon/Navigation%20Services%20Programming%20Guide/Introduction%20to%20Navigation%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbx)_.

iOS applications use UTIs to represent pasteboard types. For more information, see _[UIPasteboard Class Reference](https://developer.apple.com/documentation/uikit/uipasteboard)_.

You can find the functions used to manipulate UTIs in `UTType.h` in the Launch Services framework on OS X and the MobileCoreServices framework on iOS.

When testing to see if two UTIs are identical, you should always use the `UTTypeEqual` function rather than direct string comparison:

```
Boolean UTTypeEqual (
        CFStringRef inUTI1,
        CFStringRef inUTI2
    );
```

The two UTIs are equal if

- the UTI strings are identical
- a dynamic identifier’s tag specification is a subset of the other UTI’s tag specification.

However, in many cases you want to determine whether one UTI is compatible with another, in which case you should check for conformance rather than equality:

```
Boolean UTTypeConformsTo (
        CFStringRef inUTI1,
        CFStringRef inUTI2
    );
```

The `UTTypeConformsTo` function returns `true` if `inUTI1` conforms to `inUTI2`. Conformance relationships are transitive: if A conforms to B, and B conforms to C, then A conforms to C.

Often to use UTIs effectively, you must be able to convert various other type identifiers (OSType, MIME, and so on) to UTIs and vice versa.

To convert an identifier to a UTI, you can use the `UTTypeCreatePreferredIdentifierForTag` function:

```
CFStringRef UTTypeCreatePreferredIdentifierForTag(
        CFStringRef inTagClass,
        CFStringRef inTag,
        CFStringRef inConformingToUTI
    );
```

For the tag class, you pass one of the following tag class constants that define the alternate identifiers:

```
const CFStringRef kUTTagClassFilenameExtension;
const CFStringRef kUTTagClassMIMEType;
const CFStringRef kUTTagClassNSPboardType;
const CFStringRef kUTTagClassOSType;
```

You can pass a UTI in the `inConformingToUTI` parameter as a hint, in case the given tag appears in more than one UTI declaration. For example, if you know that the filename extension tag is associated with a file, not a directory, you can pass `public.data` here, which causes the function to ignore any types with the same extension that conform to `public.directory`. Pass `NULL` for this parameter if you have no hints.

In the rare case that two or more types exist that have the same identifier, this function prefers public UTIs over others. If no declared UTI exists for the identifier, `UTTypeCreatePreferredIdentifierForTag` creates and returns a dynamic identifier.

If you want to obtain all the UTIs that correspond to a given identifier, you can call `UTTypeCreateAllIdentifiersForTag`:

```
CFArrayRef UTTypeCreateAllIdentifiersForTag(
    CFStringRef inTagClass,
    CFStringRef inTag,
    CFStringRef inConformingToUTI );
```

This function returns an array of UTIs that you can examine to determine which one to use.

If you want to create an alternate identifier from a UTI, you call the `UTTypeCopyPreferredTagWithClass` function:

```
CFStringRef UTTypeCopyPreferredTagWithClass(
    CFStringRef inUTI,
    CFStringRef inTagClass );
```

The preferred tag is the first one listed in the tag specification array for a given tag class.

The UTI utility functions assume that all alternate identifier tags can be represented as Core Foundation strings. However, because type `OSType` is integer-based rather than string-based, it may not be immediately obvious how to correctly translate between type `CFStringRef` and type `OSType`. To ensure error-free encoding and decoding of OSType identifiers, use the following conversion functions:

```
CFStringRef UTCreateStringForOSType( OSType inOSType );

OSType UTGetOSTypeFromString( CFStringRef inTag );
```


To obtain a copy of a UTI’s declaration, use the `UTTCopyDeclaration` function:

```
CFDictionaryRef UTTypeCopyDeclaration(
    CFStringRef inUTI );
```

To obtain a URL to the bundle that contains the declaration for a given UTI, use the `UTTypeCopyDeclaringBundleURL` function:

```
CFURLRef UTTypeCopyDeclaringBundleURL(
    CFStringRef inUTI );
```

To obtain the localized description of a given UTI, call the `UTTypeCopyDescription` function:

```
CFStringRef UTTypeCopyDescription(
    CFStringRef inUTI );
```

[Next](Declaring%20New%20Uniform%20Type%20Identifiers.md)[Previous](Uniform%20Type%20Identifier%20Concepts.md)


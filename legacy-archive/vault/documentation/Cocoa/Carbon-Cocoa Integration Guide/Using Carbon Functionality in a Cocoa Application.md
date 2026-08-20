---
title: Carbon-Cocoa Integration Guide
apple_id: TP30000893
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CarbonCocoaDoc/Articles/CarbonInCocoa.html
archived_at: '2026-07-15T07:11:49.285177Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon-Cocoa Integration Guide](Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md)


[Next](Using%20a%20Cocoa%20User%20Interface%20in%20a%20Carbon%20Application.md)[Previous](Using%20Cocoa%20Functionality%20in%20a%20Carbon%20Application.md)

# Using Carbon Functionality in a Cocoa Application

Objective-C is a superset of ANSI C, so calling Carbon functions from a Cocoa application is easy as long as they are not user interface functions. A Cocoa application can always call low-level Carbon functions because Cocoa already links against the Application Services framework. To use high-level Carbon functions, a Cocoa application must import `Carbon.h` and link against the Carbon framework.

The following sections describe some of the situations in which you can use Carbon functions (other than user interface ones) in a Cocoa application:

- [Working With QuickTime Movies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydgljxhe3dmojs)
- [Accessing a Resource Fork From Cocoa](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydgljygyydkojx)
- [Using the FSRef Data Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydgljygyydmojy)
- [Managing Core Foundation Objects in Cocoa](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydgljygyydsmjt)

The situations in which you can call Carbon functions in a Cocoa application are not limited to the examples in this article. The examples illustrate the variety of ways that you can use non-UI Carbon functions in a Cocoa application. If you want to use a Carbon interface in a Cocoa application, read [Using a Carbon User Interface in a Cocoa Application](Using%20a%20Carbon%20User%20Interface%20in%20a%20Cocoa%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydklkukayq).

The Cocoa NSMovieView class displays an NSMovie (a wrapper for a QuickTime movie) in a frame and provides methods to play and edit the movie. Although there are methods for editing, setting the view size, setting the controller, setting play modes, and handling sound, the methods in the NSMovieView class do not access all the functionality available for working with QuickTime movies. For example, there are no methods to set the language of a QuickTime movie if alternate language tracks are available. However, you can call any QuickTime function from your Cocoa application, such as the function `SetMovieLanguage`. All you need to do is to initialize the Movie Toolbox by calling the QuickTime function `EnterMovies`.

See _QuickTime Framework Reference_ for information on the QuickTime functions you can call from your application.

Listing 1 shows one example of calling QuickTime functions from a Cocoa method. The code in the listing builds an array of track media types for a QuickTime movie. The track media types are displayed in the NSTableView control in the movie’s properties window. An explanation of each numbered line of code appears following the listing.

__Listing 1__  Building an array of track media types for a QuickTime movie

```objc
// Before you call QuickTime functions you must initialize the
// Movie Toolbox by calling the function EnterMovies();

- (void) myBuildTrackMediaTypesArray:(NSMovie *) movie
{
    short i;
    Movie qtmovie = [movie QTMovie];

    for (i = 0; i < GetMovieTrackCount (qtmovie); ++i)                  // 1
    {
        Str255  mediaName;
        OSErr   myErr;
        Track   movieTrack = GetMovieIndTrack (qtmovie, i+1);           // 2
        Media   trackMedia = GetTrackMedia (movieTrack);                // 3
        MediaHandler trackMediaHandler = GetMediaHandler(trackMedia);

        myErr = MediaGetName (trackMediaHandler, mediaName, 0, NULL);   // 4
        [myMovieTrackMediaTypesArray insertObject:[
                        NSString stringWithCString:&mediaName[1]
                        length:mediaName[0]]
                    atIndex:i];                                        // 5
    }
}
```

Here’s what the code does:

1. Calls the QuickTime function `GetMovieTrackCount` to obtain the number of tracks in the movie.
2. Calls the QuickTime function `GetMovieIndTrack` to determine the track identifier for a track. Note that tracks start at an index value of 1.
3. Calls the QuickTime function `GetTrackMedia` to obtain the media structure that contains sample data for the track.
4. Calls the QuickTime function `MediaGetName` to obtain the name (`Str255`) of the media type.
5. Adds the media name to the NSArray as an NSString.

For more information, see _NSMovieView Class Reference_.

A Cocoa application that works with legacy files may need to read the resource fork of a Mac OS 9 file and then parse the resource data. The Resource Manager is a Carbon API, so you can call the appropriate functions from within your Cocoa code, as shown in Listing 2. Once you read the data you can call the Cocoa method `stringWithCString:length:` to obtain an NSString that you can then parse.

__Listing 2__  Calling Resource Manager functions from a Cocoa application

```
    FSRef ref;
    NSString* theFilePath;    // the full path of the resources file
    if (FSPathMakeRef ([theFilePath fileSystemRepresentation], &ref, NULL)
        == noErr)
    {
        short res = FSOpenResFile (&ref, fsRdPerm);
        if (ResError() == noErr)
        {
            // Code that calls Resource Manager functions to read resources
            // goes here.
            CloseResFile(res);
        }
    }
```


The File Manager in Carbon uses the `FSRef` data type for specifying the name and location of a file or directory. When you call Carbon functions from a Cocoa application, you may need to pass an `FSRef` as a parameter to one of the functions, or you may receive an `FSRef` as a return value. For example, if you call the Alias Manager function `FSResolveAliasFile`, you must supply an `FSRef` that identifies the alias. An `FSRef` is an opaque 80-byte structure, so typically a pointer is used to pass an `FSRef` as a parameter.

Given a path to a file that already exists, you can use the code in Listing 3 to obtain an `FSRef` that identifies the file. An explanation for each numbered line of code appears following the listing.

__Listing 3__  A Cocoa method to convert a path into an FSRef

```objc
- (BOOL) myMakeFSRef:(FSRef *) outFSRef fromPath:(NSString *)inPath
{
    OSStatus status = noErr;
    status = FSPathMakeRef ([inPath fileSystemRepresentation],
                               outFSRef,
                               NULL); // 1
    return status == noErr; // 2
}
```

Here’s what the code does:

1. Calls the File Manager function `FSPathMakeRef` to convert a path into an `FSRef`. The `outFSRef` parameter must point to an actual `FSRef` structure.
2. Returns `YES` if the conversion was successful.

Given an `FSRef` to a file that already exists, you can use the code in Listing 4 to obtain a URL. An explanation for each numbered line of code appears following the listing.

__Listing 4__  A Cocoa method to convert an FSRef into a URL

```objc
- (NSURL *) myCreateURLFromFSRef:(FSRef *)inFSRef
{
    NSURL* url = nil;
    UInt8 path[PATH_MAX];
    OSStatus status = noErr;

    status = FSRefMakePath (inFSRef, (UInt8*)path, sizeof(path)); // 1
    if (status == noErr) {
        url = [NSURL fileURLWithPath: [NSString stringWithUTF8String:path]]; // 2
    }
    return url; // 3
}
```

Here’s what the code does:

1. Calls the File Manager function `FSRefMakePath` to convert the `FSRef` into a path.
2. Uses the path to create a new `NSURL` object.
3. Returns an `NSURL` object if the conversion was successful.

For complete documentation of the File Manager, see _File Manager Reference_.

Cocoa and Core Foundation use similar memory allocation conventions to allocate, retain, and release objects. In general, Core Foundation functions that have Copy or Create in their name return values the caller must release, while other functions return values the caller should not release. Cocoa objects created with `alloc`, `copy`, or `new` methods must be released by the caller, while all other return values should not be released by the caller. In addition, there is a set of data types that can be used interchangeably; these are referred to as toll-free bridged data types. (See [Interchangeable Data Types](Interchangeable%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgqydclkukayq) for a list.) As a result, you can use functions and methods from both environments in the same application.

The following code calls the Cocoa method `initWithCharacters` to initialize a newly allocated NSString. After the code that uses the string is executed, you need to release the string.

```
NSString *str = [[NSString alloc] initWithCharacters: ...];
// Your code that uses the string goes here.
[str release];
```

You can achieve the same result by calling the following Carbon code. This code uses the Core Foundation function `CFStringCreateWithCharacters`.

```
CFStringRef str = CFStringCreateWithCharacters(...);
// Your code that uses the string goes here.
CFRelease (str);
```

The following code calls the Core Foundation function `CFStringCreateWithCharacters`, casts the returned string to a Cocoa NSString, and releases the string using the Cocoa method `release`.

```
NSString *str = (NSString *) CFStringCreateWithCharacters(...);
// Your code that uses the string goes here.
[str release];
```

Similarly, the following code intermixes Core Foundation and Cocoa but calls the Cocoa method `autorelease` to dispose of the string.

```
NSString *str = (NSString *) CFStringCreateWithCharacters(...);
// Your code that uses the string goes here.
[str autorelease];
```

For a more information, see either the Cocoa programming topic _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_ or the Core Foundation programming topic _[Memory Management Programming Guide for Core Foundation](../../Core%20Foundation/Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdo2i)_.

[Next](Using%20a%20Cocoa%20User%20Interface%20in%20a%20Carbon%20Application.md)[Previous](Using%20Cocoa%20Functionality%20in%20a%20Carbon%20Application.md)


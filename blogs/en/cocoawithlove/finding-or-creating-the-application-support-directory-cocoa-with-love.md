---
title: 'Finding or creating the application support directory | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/05/finding-or-creating-application-support.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:909be3e5969bc09d'
translated: false
---

> 原文：[Finding or creating the application support directory | Cocoa with Love](https://www.cocoawithlove.com/2010/05/finding-or-creating-application-support.html)　·　Cocoa with Love (Matt Gallagher)

A simple post this week but one which optimizes a common task: locating the application support directory for the current application, creating it if it doesn't exist. The result makes accessing the current application's support directory a single line and provides a structure for locating and creating folders at other standard locations with similar ease.

[TOC]

## The Application Support Directory

On the Mac, the correct location to store persistent user-related files for your application is in a directory with the same name as your application in the Application Support directory for the current user.

As an example, if the current user "person" runs an application named "ExampleApp" it would store such files in the following location:

```objc
/Users/person/Library/Application Support/ExampleApp/
```

On iPhone OS devices, the running application gets its own copy of the Library directory, so you could write files wherever you choose within this. However, I use the same code on both platforms for consistency and there is no real penalty in doing this. For an iPhone OS device then, the path to the application support directory would look like this:

```objc
/User/Applications/12345678-AAAA-BBBB-CCCC-0123456789AB/Library/Application Support/ExampleApp/
```

where `12345678-AAAA-BBBB-CCCC-0123456789AB` is whatever UUID has been assigned to your application.

> . If you want to store user-related preferences, it is generally better to can store them in the
> 
> NSUserDefaults
> 
> .

## Getting paths correctly

The correct way to get the path to the Application Support directory is to use the `NSSearchPathForDirectoriesInDomains` function passing `NSApplicationSupportDirectory` for the search path and `NSUserDomainMask` for the domain.

This can be done in one line but on its own, it is only ever part of the solution.

While `NSSearchPathForDirectoriesInDomains` can return a path to the Application Support directory, it does not guarantee that the application support directory exists. For an iPhone OS device, it almost certainly won't exist the first time you run the application.

Further, we need to append the name of the current application to this path and create this application-specific subdirectory if needed.

Finally, we need to handle all of this in a way that is tolerant of errors including failure to create the directory or existence of files where we need a directory to go.

A simple idea — get the application support directory — turns out to be a multi-step operation.

## Design of the solution

The solution that I use in many of my applications is based around a method with the following declaration:

```objc
- (NSString *)findOrCreateDirectory:(NSSearchPathDirectory)searchPathDirectory
    inDomain:(NSSearchPathDomainMask)domainMask
    appendPathComponent:(NSString *)appendComponent
    error:(NSError **)errorOut
```

This is a flexible method that can be used for resolving/creating a directory/subdirectory at any standard location searchable by `NSSearchPathForDirectoriesInDomains`.

The first two parameters are the parameters passed to `NSSearchPathForDirectoriesInDomains`, the third parameter is a subpath to append to the result from `NSSearchPathForDirectoriesInDomains` (which we can use to append the current application's name to get our application specific subdirectory). The final parameter is used to return information about any of the three errors that can occur (no path found, file exists at directory location or unable to create directories).

I further supplement this with a convenience method to invoke this with all the appropriate parameters for creating the application support directory:

```objc
- (NSString *)applicationSupportDirectory
```

On error, this method simply logs any error result using `NSLog`.

In my solution, both of these methods are part of a category on `NSFileManager`. There is no technical requirement that it be a category on `NSFileManager` but these methods do use `NSFileManager` internally and do share the same goals of providing access to directories within the filesystem. Further refinements could also add a URL version based on the NSFileManager method `-URLsForDirectory:inDomains:` which would make the association less arbitrary.

## Implementation

I've omitted the creation of the error objects for space but otherwise the implementation is as follows:

```objc
- (NSString *)findOrCreateDirectory:(NSSearchPathDirectory)searchPathDirectory
    inDomain:(NSSearchPathDomainMask)domainMask
    appendPathComponent:(NSString *)appendComponent
    error:(NSError **)errorOut
{
    // Search for the path
    NSArray* paths = NSSearchPathForDirectoriesInDomains(
        searchPathDirectory,
        domainMask,
        YES);
    if ([paths count] == 0)
    {
        // *** creation and return of error object omitted for space
        return nil;
    }

    // Normally only need the first path
    NSString *resolvedPath = [paths objectAtIndex:0];
    
    if (appendComponent)
    {
        resolvedPath = [resolvedPath
            stringByAppendingPathComponent:appendComponent];
    }
    
    // Create the path if it doesn't exist
    NSError *error;
    BOOL success = [self
        createDirectoryAtPath:resolvedPath
        withIntermediateDirectories:YES
        attributes:nil
        error:&error];
    if (!success) 
    {
        if (errorOut)
        {
            *errorOut = error;
        }
        return nil;
    }
    
    // If we've made it this far, we have a success
    if (errorOut)
    {
        *errorOut = nil;
    }
    return resolvedPath;
}
```

I've noted that we "`Normally only need the first path`". If you pass multiple values ORed together for the domain mask (e.g. `NSUserDomainMask | NSLocalDomainMask`) then this assumption will not be true. If your program needs to handle multiple directories in this way, you'll need to add appropriate handling of multiple results.

Finally, we have the implementation of the `applicationSupportDirectory` method:

```objc
- (NSString *)applicationSupportDirectory
{
    NSString *executableName =
        [[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleExecutable"];
    NSError *error;
    NSString *result =
        [self
            findOrCreateDirectory:NSApplicationSupportDirectory
            inDomain:NSUserDomainMask
            appendPathComponent:executableName
            error:&error];
    if (error)
    {
        NSLog(@"Unable to find or create application support directory:\n%@", error);
    }
    return result;
}
```

As you can see, it pulls the application name out of the main bundle's `infoDictionary` and uses this to create the Application Support directory.

The end result is that you can get the path to the application support directory with the following line:

```objc
NSString *path = [[NSFileManager defaultManager] applicationSupportDirectory];
```

## Conclusion

> NSFileManager_DirectoryLocations.zip
> 
> (6kb)

I like it when a task that can be unambiguously described in a simple sentence ("Get the path to the application support directory.") is correspondingly achieved in a single line.

The code presented in this post implements a simple set of steps but since I need to do this in most applications, it is one of my most commonly used categories.

---
title: 'Resolving a path containing a mixture of aliases and symlinks | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/02/resolving-path-containing-mixture-of.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2826d4730a26d0ef'
translated: false
---

> 原文：[Resolving a path containing a mixture of aliases and symlinks | Cocoa with Love](https://www.cocoawithlove.com/2010/02/resolving-path-containing-mixture-of.html)　·　Cocoa with Love (Matt Gallagher)

Resolving symlinks in a path is very easy in Cocoa (it can be done in a single statement) but aliases require more work. Additionally the commands for resolving symlinks and aliases are incompatible with each other — meaning that you can resolve a path containing symlinks or aliases but not a mixture of the two. In this post, I present a category on `NSString` that will allow you to resolve a path containing any combination of symlinks or aliases as simply as resolving symlinks alone.

## Introduction

When Apple introduced [alias files](http://en.wikipedia.org/wiki/Alias_(Mac_OS)) in [System 7](http://en.wikipedia.org/wiki/System_7_(Macintosh)), they were the only way of referencing another file in the filesystem. Sure, other operating systems already had [symlinks](http://en.wikipedia.org/wiki/Symbolic_link) but there was little likelihood of the two needing to interact since System 7 had almost no interoperability with Unix filesystems (despite the existence of [A/UX](http://en.wikipedia.org/wiki/A/UX)).

Alias files are a great way of referencing other files because they can continue to track their target if it moves. Aliases store both the path of their target and the [inode](http://en.wikipedia.org/wiki/Inode) plus volume identifier of their target. This means that they won't break if the file at their target path moves, unlike a symlink which will break if the target moves (since a symlink is just a path). In fact, symlinks will often break if the symlink file itself moves since symlinks are normally relative paths.

Aliases do have some annoying traits. In their current incarnation, they insist on storing the thumbnail and metadata of data of their target, resulting in a file which may be hundreds of kilobytes (or more) of entirely redundant data — especially annoying if you have thousands of aliases. Despite this, they are normally a good, general-purpose way of linking files in the filesystem.

As a "user-exposed" feature (unlike symlinks which are largely hidden from novice users) they are also common. It's unfortunate then that they're so annoying to deal with in Cocoa.

## Resolving aliases

Resolving a symlink is easy:

```objc
NSString *resolvedPath = [path stringByResolvingSymlinksInPath];
```

Theoretically, you only need one command to resolve an alias:

```objc
OSErr err = FSResolveAliasFile(
    &fsRef, resolveAliasChains, &targetIsFolder, &wasAliased);
```

Unfortunately, the `FSRef` here is a campy 1990's throwback (the 90's are now two decades ago) and in Cocoa programming, you rarely have or want an `FSRef` for a file. This means that you need to convert your `NSString` to an `FSRef` and then convert the result back to an `NSString` when you're done.

Apple's Low Level File Management Topics include [an approach for resolving an alias from an `NSString` path](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/ResolvingAliases.html) which demonstrates this procedure. While I use an implementation derived from this in my solution, Apple's original implementation suffers from the following problems:

- The `CFURLGetFSRef` function used to convert a `CFURL` into an `FSRef` will fail if the path contains an alias at anywhere other than the last path component.
- While `CFURLGetFSRef` will follow symlinks in the URL to create the `FSRef`, no part of this code will actually return a resolved symlink, so that part will require a separate step.
- The function `FSResolveAliasFile` will present a user dialog if the alias points to a volume which is not mounted. While potentially desirable in a user application, this is undesirable in all other cases.

This final point is not too difficult — we'll replace `FSResolveAliasFile` with `FSResolveAliasFileWithMountFlags` which allows us to disable the user dialog using the flags. But the remaining two points will require a little more work to address.

As a further comment about usage of `FSResolveAliasFileWithMountFlags`: aliases that point to other aliases are exceedingly rare (if you try to create an alias to an alias in the Finder, the Finder will make the second alias point directly to the target) so I pass `false` for `resolveAliasChains` to optimize for the unchained case and handle the unusual case of chained aliases at a different level in the code.

## Breaking it down into solvable components

We can resolve paths that contain any number of symlinks and we can resolve a path that contains an alias but we can't do both at once.

The solution is therefore straightforward:

1. break the path down into components
2. build the components together, iteratively resolving aliases or symlinks at each level
3. implement code for resolving the symlink or alias as efficiently as possible for the bottom level of this scenario

Each of these points will then be a different tier in a three level solution.

My solution will contain two requirements:

- The initial path must be resolvable to an absolute path using `-[NSString stringByStandardizingPath]`
- The path contained within a symlink file will not include any aliases or symlinks except as the final string component (no recursive parsing)

This second point is mostly a theoretical limitation since it is nearly impossible to generate a symlink with an alias or other symlink as a non-final path component (you'd have to create the symlink file manually).

## Top level

The top level of the solution is simply an iteration over path components which then invokes the iterative link resolution.

```objc
// Break into components.
NSArray *pathComponents = [path pathComponents];

// First component ("/") needs no resolution; we only need to handle subsequent
// components.
NSString *resolvedPath = [pathComponents objectAtIndex:0];
pathComponents =
    [pathComponents subarrayWithRange:NSMakeRange(1, [pathComponents count] - 1)];

// Process all remaining components.
for (NSString *component in pathComponents)
{
    resolvedPath = [resolvedPath stringByAppendingPathComponent:component];
    resolvedPath = [resolvedPath stringByIterativelyResolvingSymlinkOrAlias];
    if (!resolvedPath)
    {
        return nil;
    }
}
```

I haven't shown the code which resolves the path to an absolute path or fails but the assumption that it begins with a "/" is valid.

## Middle level

The middle level of the solution iterates over a path where only the final component could be a symlink or alias and resolves it until the result is neither an alias nor symlink.

For efficiency, this does two things in an unusual way:

- I use `lstat` instead of `-[NSFileManager attributesOfItemAtPath:error]` since I only need the `st_mode` field, and `NSFileManager` invokes `lstat` internally anyway.
- I use my own `-[NSString stringByConditionallyResolvingSymlink]` method instead of `- [NSString stringByResolvingSymlinksInPath]` since I know that only the final component requires resolution (I've already done the work for earlier components).

```objc
- (NSString *)stringByIterativelyResolvingSymlinkOrAlias
{
    NSString *path = self;
    NSString *aliasTarget = nil;
    struct stat fileInfo;
    
    // Use lstat to determine if the file is a directory or symlink
    if (lstat([[NSFileManager defaultManager]
        fileSystemRepresentationWithPath:path], &fileInfo) < 0)
    {
        return nil;
    }
    
    // While the file is a symlink or resolves as an alias, keep iterating.
    while (S_ISLNK(fileInfo.st_mode) ||
        (!S_ISDIR(fileInfo.st_mode) &&
            (aliasTarget = [path stringByConditionallyResolvingAlias]) != nil))
    {
        if (S_ISLNK(fileInfo.st_mode))
        {
            // Resolve the symlink component in the path
            NSString *symlinkPath = [path stringByConditionallyResolvingSymlink];
            if (!symlinkPath)
            {
                return nil;
            }
            path = symlinkPath;
        }
        else
        {
            // Or use the resolved alias result
            path = aliasTarget;
        }

        // Use lstat again to prepare for the next iteration
        if (lstat([[NSFileManager defaultManager]
            fileSystemRepresentationWithPath:path], &fileInfo) < 0)
        {
            path = nil;
            continue;
        }
    }
    
    return path;
}
```

The `stringByConditionallyResolvingAlias` method returns `nil` if the path exists but isn't an alias, allowing this function to double as both a test for whether the path is an alias as well as the resolution of that alias. I could use a similar approach to test and resolve symlinks (since I have also implemented a `stringByConditionallyResolvingSymlink` method) but I don't do this for aforementioned efficiency reasons: it would cause an extra fetch of the filesystem metadata which is the main bottleneck of the whole procedure.

## Bottom level

The bottom level is then just the implementation of the `stringByConditionallyResolvingAlias` and `stringByCondictionallyResolvingSymlink`. The first is just a modification of Apple's code to address the issues I've already discussed — you can see the final product by downloading the code. The second method looks like this:

```objc
- (NSString *)stringByConditionallyResolvingSymlink
{
    // Get the path that the symlink points to
    NSString *symlinkPath =
        [[NSFileManager defaultManager]
            destinationOfSymbolicLinkAtPath:self
            error:NULL];
    if (!symlinkPath)
    {
        return nil;
    }
    if (![symlinkPath hasPrefix:@"/"])
    {
        // For relative path symlinks (common case), resolve the relative
        // components
        symlinkPath =
            [[self stringByDeletingLastPathComponent]
                stringByAppendingPathComponent:symlinkPath];
        symlinkPath = [symlinkPath stringByStandardizingPath];
    }
    return symlinkPath;
}
```

Hooray, I finally used `NSFileManager` in a post about files! Yes, once again it's probably just a wrapper around the C function `readlink` that I could invoke for myself but the fact that the `NSFileManager` method handles the nasty business of buffer allocation, sizing and string conversion is more than enough reason to forego the lower level function.

## Conclusion

> You can download [NSString+SymLinksAndAliases.zip](https://www.cocoawithlove.com/assets/objc-era/NSString+SymlinksAndAliases.zip) (3kb) which contains all the code discussed in this post (plus a few other related methods) as a category on `NSString`.

Usage of the category is as simple as importing the header and writing:

```objc
NSString *fullyResolvedPath = [somePath stringByResolvingSymlinksAndAliases];
```

The `fullyResolvedPath` will either contain the destination (as an absolute and fully resolved path) or it will be `nil` (if the path can't be fully resolved because it doesn't exist or can't be read for some reason).

I've tried to keep this code efficient by keeping the number of filesystem calls low. The code will certainly handle at least a few thousand alias resolutions per second on my computer but I haven't pushed it much harder than that.

Of course, if you're an iPhone programmer, all of this is a waste of time since the iPhone doesn't publicly expose `FSRef` (although `CFURLGetFSRef` exists to generate a pointer which is totally unusable). In fact, I'm not sure aliases are possible on the iPhone anyway.

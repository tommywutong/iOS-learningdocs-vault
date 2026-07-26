---
title: Temporary Files
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/temporary-files/'
original_language: en
published: 2014-03-03
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:1c2b709455df93ad'
translated: false
---

> 原文：[Temporary Files](https://nshipster.com/temporary-files/)　·　NSHipster (Mattt)

# [Temporary Files](https://nshipster.com/temporary-files/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  March 9^th, 2019 ([revised](https://github.com/nshipster/articles/commits/master/2014-03-03-temporary-files.md))

Volumes have been written about persisting data, but when it comes to short-lived, temporary files, there is very little to go on for Cocoa. (Or if there has, perhaps it was poetically ephemeral itself).

---

Temporary files are used to write data to disk before either moving it to a permanent location or discarding it. For example, when a movie editor app exports a project, it may write each frame to a temporary file until it reaches the end and moves the completed file to the `~/Movies` directory. Using a temporary file for these kinds of situations ensures that tasks are completed atomically (either you get a finished product or nothing at all; nothing half-way), and without creating excessive memory pressure on the system (on most computers, disk space is plentiful whereas memory is limited).

There are four distinct steps to working with a temporary file:

1. Creating a temporary directory in the filesystem
2. Creating a temporary file in that directory with a unique filename
3. Writing data to the temporary file
4. Moving or deleting the temporary file once you’re finished with it

## Creating a Temporary Directory

The first step to creating a temporary file is to find a reasonable, out-of-the-way location to which you can write — somewhere inconspicuous that doesn’t get in the way of the user or get picked up by a system process like Spotlight indexing, Time Machine backups, or iCloud sync.

On Unix systems, the `/tmp` directory is the de facto scratch space. However, today’s macOS and iOS apps run in a container and don’t have access to system directories; a hard-coded path like that isn’t going to cut it.

If you don’t intend to keep the temporary file around, you can use the `NSTemporaryDirectory()` function to get a path to a temporary directory for the current user.

```
let temporaryDirectoryURL = URL(fileURLWithPath: NSTemporaryDirectory(),
                                    isDirectory: true)
```

```
NSURL *temporaryDirectoryURL = [NSURL fileURLWithPath: NSTemporaryDirectory()
                                          isDirectory: YES];
```

Alternatively, if you intend to move your temporary file to a destination URL, the preferred (albeit more complicated) approach is to call the `FileManager` method `uri(for:in:appropriateFor:create:)`.

```
let destinationURL: URL = /path/to/destination
let temporaryDirectoryURL =
    try FileManager.default.url(for: .itemReplacementDirectory,
                                in: .userDomainMask,
                                appropriateFor: destinationURL,
                                create: true)
```

```
NSURL *destinationURL = <#/path/to/destination#>;

NSFileManager *fileManager = [NSFileManager defaultManager];
NSError *error = nil;
NSURL *temporaryDirectoryURL =
    [fileManager URLForDirectory:NSItemReplacementDirectory
                        inDomain:NSUserDomainMask
               appropriateForURL:destinationURL
                          create:YES
                           error:&error];
```

The parameters of this method are frequently misunderstood, so let’s go through each to understand what this method actually does:

- We pass the item replacement search path (`.itemReplacementDirectory`) to say that we’re interested in a temporary directory.
- We pass the user domain mask (`.userDomainMask`) to get a directory that’s accessible to the user.
- For the `appropriateForURL` parameter, we specify our `destinationURL`, so that the system returns a temporary directory from which a file can be quickly moved to the destination (and not, say across different volumes).
- Finally, we pass `true` to the `create` parameter to save us the additional step of creating it ourselves.

The resulting directory will have a path that looks something like this: file:///var/folders/l3/kyksr35977d8nfl1mhw6l_c00000gn/T/TemporaryItems/(A%20Document%20Being%20Saved%20By%20NSHipster%208)/

## Creating a Temporary File

With a place to call home (at least temporarily), the next step is to figure out what to call our temporary file. We’re not picky about what it’s named — just so long as it’s unique, and doesn’t interfere with any other temporary files in the directory.

The best way to generate a unique identifier is the `ProcessInfo` property `globallyUniqueString`:

```
ProcessInfo().globallyUniqueString
```

```
[[NSProcessInfo processInfo] globallyUniqueString];
```

The resulting filename will look something like this: 42BC63F7-E79E-4E41-8E0D-B72B049E9254-25121-000144AB9F08C9C1

Alternatively, [`UUID`](https://nshipster.com/uuid-udid-unique-identifier) also produces workably unique identifiers:

```
UUID().uuidString
```

```
[[NSUUID UUID] UUIDString]
```

A generated UUID string has the following format: B49C292E-573D-4F5B-A362-3F2291A786E7

Now that we have an appropriate directory and a unique filename, let’s put them together to create our temporary file:

```
let destinationURL: URL = /path/to/destination

let temporaryDirectoryURL =
    try FileManager.default.url(for: .itemReplacementDirectory,
                                in: .userDomainMask,
                                appropriateFor: destinationURL,
                                create: true)

let temporaryFilename = ProcessInfo().globallyUniqueString

let temporaryFileURL =
    temporaryDirectoryURL.appendingPathComponent(temporaryFilename)
```

```
NSURL *destinationURL = <#/path/to/destination#>;

NSFileManager *fileManager = [NSFileManager defaultManager];
NSError *error = nil;
NSURL *temporaryDirectoryURL =
    [fileManager URLForDirectory:NSItemReplacementDirectory
                        inDomain:NSUserDomainMask
               appropriateForURL:destinationURL
                          create:YES
                           error:&error];

NSString *temporaryFilename =
    [[NSProcessInfo processInfo] globallyUniqueString];
NSURL *temporaryFileURL =
    [temporaryDirectoryURL
        URLByAppendingPathComponent:temporaryFilename];
```

## Writing to a Temporary File

The sole act of creating a file URL is of no consequence to the file system; a file is created only when the file path is written to. So let’s talk about our options for doing that:

### Writing Data to a URL

The simplest way to write data to a file is to call the `Data` method `write(to:options)`:

```
let data: Data = some data
try data.write(to: temporaryFileURL,
               options: .atomic)
```

```
NSData *data = <#some data#>;
NSError *error = nil;
[data writeToURL:temporaryFileURL
         options:NSDataWritingAtomic
           error:&error];
```

By passing the `atomic` option, we ensure that either all of the data is written or the method returns an error.

### Writing Data to a File Handle

If you’re doing anything more complicated than writing a single `Data` object to a file, you might instead create an empty file and use a `FileHandle` to write data incrementally.

```
fileManager.createFile(atPath: temporaryFileURL.path, contents: Data())

let fileHandle = try FileHandle(forWritingTo: temporaryFileURL)
defer { fileHandle.closeFile() }

fileHandle.write(data)

// ...
```

```
[fileManager createFileAtPath: [temporaryFileURL path]
                     contents: [NSData data]
                   attributes: @{}];

NSError *error = nil;
NSFileHandle *fileHandle =
    [NSFileHandle fileHandleForWritingToURL:temporaryFileURL
                                      error:&error];
[fileHandle writeData:data];

// ...

[fileHandle closeFile];
```

### Writing Data to an Output Stream

For more advanced APIs, it’s not uncommon to use `OutputStream` to direct the flow of data. Creating an output stream to a temporary file is no different than any other kind of file:

```
let outputStream =
    OutputStream(url: temporaryFileURL, append: true)!
defer { outputStream.close() }

data.withUnsafeBytes { bytes in
    outputStream.write(bytes, maxLength: bytes.count)
}
```

```
NSOutputStream *outputStream =
    [NSOutputStream outputStreamWithURL:temporaryFileURL
                                 append:YES];

[outputStream write:data.bytes
          maxLength:data.length];

[outputStream close];
```

## Moving or Deleting the Temporary File

Files in system-designated temporary directories are periodically deleted by the operating system. So if you intend to hold onto the file that you’ve been writing to, you need to move it somewhere outside the line of fire.

If you already know where the file’s going to live, you can use `FileManager` to move it to its permanent home:

```
let fileURL: URL = /path/to/file
try FileManager.default.moveItem(at: temporaryFileURL,
                                 to: fileURL)
```

```
NSFileManager *fileManager = [NSFileManager defaultManager];

NSURL *fileURL = <#/path/to/file#>;
NSError *error = nil;
[fileManager moveItemAtURL:temporaryFileURL
                     toURL:fileURL
                     error:&error];
```

Although the system eventually takes care of files in temporary directories, it’s not a bad idea to be a responsible citizen and follow the guidance of _“take only pictures; leave only footprints.”_

`FileManager` can help us out here as well, with the `removeItem(at:)` method:

```
try FileManager.default.removeItem(at: temporaryFileURL)
```

```
NSFileManager *fileManager = [NSFileManager defaultManager];

NSError *error = nil;
[fileManager removeItemAtURL:temporaryFileURL
                       error:&error];
```

---

_“This too shall pass”_ is a mantra that acknowledges that all things are indeed temporary.

Within the context of the application lifecycle, some things are more temporary than others, and it’s with that knowledge that we choose to act appropriately: seeking to find the right place, make a unique impact, and leave without a trace.

Perhaps we can learn something from this cycle in our own, brief and glorious lifecycle.

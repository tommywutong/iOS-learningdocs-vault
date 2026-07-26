---
title: 'Optimizing the loading of a very large table on the iPhone | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/09/optimizing-loading-of-very-large-table.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:f29d90d0bbbfe1a5'
translated: false
---

> 原文：[Optimizing the loading of a very large table on the iPhone | Cocoa with Love](https://www.cocoawithlove.com/2009/09/optimizing-loading-of-very-large-table.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I look at a `UITableView` on the iPhone which loads its data from a server and look at how its performance scales from single rows to tens of thousands of rows. I'll examine which aspects of the iPhone scale well and which become a burden as a displayed dataset moves from trivially sized to large sizes.

## Introduction

Last week, I received an email asking if [StreamToMe](http://zqueue.com/streamtome/index.html) would be able to handle 20,000 files in a media collection. This person probably meant "20,000 files categorized into subfolders" but the performance geek in me immediately thought that 20,000 files in a single directory was a far more interesting question.

It's easy to find programs on the iPhone that become slower and less responsive when dealing with tables that only contain a few hundred rows. In my own experience, I've rarely tested with more than a couple hundred items in a `UITableView`. I had no idea what a `UITableView` would do with 20,000 items.

Purely looking at data sizes, it seems like it should work: the 128MB versions of the iPhone (all devices prior to the 3Gs) allow applications to use between 24MB and 64MB of RAM before they are killed for excess memory use. This should allow for between 1-3kB per row within available memory — far more than I need.

Of course, this won't be a synthetic test with efficient but trivial rows: this is a program with real data, transferred from a server, parsed, constructed and displayed, which must remain capable of media playback after everything else is loaded into memory.

## Generating test data

I wanted real test data so I decided to replicate a small MP3 file on the server. I used a 1 kilobyte file containing a single tone that plays for 4 seconds. I used UUID strings appended with ".mp3" for filenames so that file sorting algorithms would still have some real work to do.

```objc
for (NSInteger i = 0; i < MAX_FILES; i++)
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    CFUUIDRef uuid = CFUUIDCreate(NULL);
    NSString *uuidString = (NSString *)CFUUIDCreateString(NULL, uuid);
    CFRelease(uuid);
    [uuidString autorelease];

    NSString *filePath =
        [directoryPath stringByAppendingPathComponent:
            [NSString stringWithFormat:@"%@.mp3", uuidString]];
    [[NSFileManager defaultManager]
        createFileAtPath:filePath
        contents:mp3Data
        attributes:nil];
    
    if ((i % 1000) == 0)
    {
        NSLog(@"%ld files remaining.", MAX_FILES - i);
    }
    
    [pool drain];
}
```

Using this code, I created directories with 1, 10, 100, 1000, 10,000, 20,000, 100,000 and 1,000,000 files to see how far I would get with the application.

A few interesting points came out of this work, unrelated to the iPhone itself:

- Yes, you can now create more than 65536 files in a directory. I remember when Macs couldn't create more than 65536 files on the entire disk.
- Curiously, when you select files and use the "Copy" menu item in the Finder, the maximum number of items is still 65536.
- Don't try to drag 10,000 (or more) items from one window to another — I gave up watching the beachball on this action and hard-booted.
- is a little slower than other approaches because it creates the file in a temporary location and moves it to the target location (a single create at the target location would have been faster).
- if you try to create a million MP3s on your computer, be prepared to wait 3 hours while it churns away and then have the Spotlight metadata indexer slow your computer down for a further few hours.

## Initial results

Which data sets will load and how long will they take? With no preparation of StreamToMe in anticipation of this test, I immediately pointed it at the test directories.

| Number of files | Total time from touch event to display of directory |
|---|---|
| 1 | 131ms |
| 10 | 128ms |
| 100 | 424ms |
| 1,000 | 3,108ms |
| 10,000 | 30,587ms |
| 20,000 | 64,191ms***** |
| 100,000 | N/A |
| 1,000,000 | N/A |

_The asterisk here indicates that the 20,000 row run was not able to reliably play the audio files after loading (it would sometimes quit due to low memory). The one hundred thousand and million row tests both failed to load at all._

## Initial analysis

### Scaling

Looking first at the way the results scale, this table shows the expected behavior with the iPhone's memory arrangement:

1. The iPhone has a 16k data cache so tests that operate within this limit (fewer than a couple hundred rows) are more bound by the network latency and fixed-duration setup costs than any row-specific work performed. This leads to better than linear (less than O(n)) scaling for the 1, 10 and 100 tests.
2. Tests that exceed the 16k data limit (one thousand through twenty thousand) scale almost perfectly linearly as they push a consistent amount of data through main memory.
3. There is no virtual memory on the iPhone, so you don't see a greater than linear increase in time as memory runs out (thrashing) — instead, there's an abrupt point at which things simply fail. More memory will not make a iPhone faster in the same way that it will make a memory constrained Mac faster.

### Speed

Looking at performance, it's a little disappointing — no one would want to wait over a minute for their file list to load. Where is that time taken? Looking at timing results for the 20,000 row test:

- 6,563ms on the server, loading the directory listing and formatting the response.
- 3,111ms transferring data.
- 12,771ms on the client parsing the response from the server.
- 32,098ms on the client converting the parsed response into row-ready classes
- 9,453ms in autorelease pool cleanup

### Memory use

The memory footprint with 20,000 files loaded is around 6.8MB with peak memory use of 38.2MB. This leads to two questions:

1. With final memory so low, why is the program behaving as though its memory is constrained?
2. What is causing the peak memory to be so high? If it were much lower, 100,000 rows might be possible.

## Code changes and improvements

### stat is the biggest constraint on filesystem lookups

The first change I made was on the server. 6.5 seconds to load 20,000 files is too slow. The key constraining factor here is reading the basic metadata for tens of thousands of small files. The low level file function `stat` (or in this case, `lstat`) is the limiting factor.

Technically, I wasn't using `lstat` but `-[NSFileManager contentsOfDirectoryAtPath:error:]` was invoking it for every file and then `-[NSFileManager fileExistsAtPath:isDirectory:]` was invoking it again to see if each file was a directory.

In 10.6, you can replace `-[NSFileManager contentsOfDirectoryAtPath:error:]` with `-[NSFileManager contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:]` so that these two commands can be rolled into one (halving the number of calls to `lstat`). I want to keep 10.5 compatibility, so instead, I wrote my own traversal using `readdir` and `lstat` directly.

This change doubled the directory reading speed of the server.

### Lowering memory footprint

In Cocoa, peak memory is often caused by autoreleased memory that accumulates during loops. You can address this by inserting `NSAutoreleasePool` allocations and drains into your loops but this is slow. The best approach is to eliminate autoreleased memory in memory constrained areas. I did this throughout the parsing and conversion code on the iPhone.

There was also some unnecessary copying of memory (from the network data buffer to an NSString and back to a UTF8 string) that I removed (by passing the network data buffer directly as the UTF8 string).

More than simply lowering the memory footprint, these changed almost doubled the speed of parsing on the iPhone.

### Memory fragmentation

Even after lowering peak memory usage, I still encountered out of memory errors when trying to allocate larger objects, even though my memory usage was only 16MB.

After some investigation, I realized that my parser was fragmenting memory by allocating smaller and larger string fragments in a leapfrogging effect so that consecutive strings in the final data structure were not actually adjacent in memory. Even though memory usage was only around 50%, there was not a single, contiguous 2MB space within this for media loading and playback due to the scattered pattern of string, array and dictionary allocations following parsing.

The simplest solution (one that didn't involve rewriting the parser) was to copy the parsed data every few rows into properly contiguous locations, releasing the old non-contiguous locations. After this, memory allocation issues went away.

Of course, this did result in a minor increase in parsing time but the improved memory performance was worth the minor performance cost.

### Moving work out of critical loops

Finally, I looked at the conversion of parsed data into classes representing each row. This work was primarily assigning strings to properties of an object and couldn't be easily avoided.

During this process, I also created an `NSInvocation` for each object to handle its user-interface action when tapped in the table (media rows play the file, folder rows open the folder) and assigned a named `UIImage` (either the file or the folder icon) to the object.

Since there are only two images and two possible actions, these objects could be created outside the loop and either minimally modified for each row (with different parameters in the case of the `NSInvocation`) or assigned as-is (in the case of the `UIImage`).

These seemingly tiny changes (in addition to the memory changes mentioned above) resulted in a better than tenfold performance increase for the converting stage (which had been the most time consuming stage).

## Results revisited

With these changes, the results became.

| Number of files | New time taken | Old time taken |
|---|---|---|
| 1 | 135ms | 131ms |
| 10 | 137ms | 128ms |
| 100 | 250ms | 424ms |
| 1,000 | 845ms | 3,108ms |
| 10,000 | 7,998ms | 30,587ms |
| 20,000 | 14,606ms | 64,191ms***** |
| 100,000 | 84,594ms | N/A |
| 1,000,000 | N/A | N/A |

The 20,000 row test case now runs more than 4 times faster and the 100,000 test case completes successfully and can play the audio files once loaded.

## Running one million rows in the simulator

The million row test set involved 121MB of data sent over the network — it was never going to work on a 128MB iPhone.

Without the memory constraints of the iPhone, I ran a million rows in the simulator. It took 7.5 minutes to load (almost entirely bound by `lstat`).

After around 800,000 rows (40 pixels high each), `UITableView` can no longer address each pixel accurately with single precision `CGFloat`s used on the iPhone, so every second row was misplaced by 16 pixels or so making the result almost unreadable beyond that point. In short: `UITableView` isn't really meant to handle a million rows.

## Conclusion

The iPhone _can_ handle tables with 100,000 rows — and it continues to scroll as smoothly as though it were only 100 rows.

Optimization doesn't mean writing assembly code and bleeding from your fingernails. A couple hours work resulted in a 4 times performance increase and dramatically better memory usage from very simple code rearrangement.

The biggest improvements to the performance came from three points:

- replacing autoreleased objects with tight alloc and release pairs in just two loops (in some cases removing the allocation entirely)
- generation and

  lookup work from the key construction loop
- optimization per se)

And increasing available productive memory actually involved performing _more_ allocations — reallocating discontiguous collections of objects to contiguous memory locations. There was also the typical elimination of unnecessary copying.

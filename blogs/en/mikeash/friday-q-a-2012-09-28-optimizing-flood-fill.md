---
title: 'Friday Q&A 2012-09-28: Optimizing Flood Fill'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-09-28-optimizing-flood-fill.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5c27fc8f4d57235b'
translated: false
---

> 原文：[Friday Q&A 2012-09-28: Optimizing Flood Fill](https://www.mikeash.com/pyblog/friday-qa-2012-09-28-optimizing-flood-fill.html)　·　mikeash.com Friday Q&A

Posted at 2012-09-28 13:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-10-12: Obtaining and Interpreting Audio Data](https://www.mikeash.com/pyblog/friday-qa-2012-10-12-obtaining-and-interpreting-audio-data.html)  
Previous article: [Friday Q&A 2012-09-14: Implementing a Flood Fill](https://www.mikeash.com/pyblog/friday-qa-2012-09-14-implementing-a-flood-fill.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa) [image](https://www.mikeash.com/pyblog/?tag=image)

Friday Q&A 2012-09-28: Optimizing Flood Fill

by [Mike Ash](https://www.mikeash.com/)

**Measurement**  
A prerequisite for any optimization work is the ability to measure the code in question. In this case, we're optimizing for speed, so we have to measure how fast the code is. If you can't measure it, it's nearly impossible to make it faster, because you have only a vague idea how much difference any given change makes, or whether it's even an improvement at all. Lots of seemingly-obvious optimizations can end up making code slower, so it's important to have real data.

If at all possible, it's best to have a consistent scenario that you can run in an automated fashion. If you can simply push a button and get a number out that says how fast the code is, that's ideal. Anything that requires manual setup will add a lot of work. Anything that requires manual _inputs_ to the process is begging for trouble: if your inputs vary from one run to the next, you can't tell what changes are due to your code and what changes are due to your changing inputs! This can be important for UI-heavy code where the user's specific actions can heavily influence how much code runs and when it runs. Whenever possible, isolate the code in question away from the user and pass it pre-baked input.

For the flood fill, we need an image to fill. I wrote a quick method that creates a `NSBitmapImageRep` using `NSGraphicsContext` to draw into it, building a square covering most of the image, with some diagonal lines to ensure that the flood fill has something interesting to work on. Here's the code for that:

```
    NSBitmapImageRep *TestImageRep(int width, int height)
    {
        NSBitmapImageRep *rep = [[NSBitmapImageRep alloc]
                                 initWithBitmapDataPlanes: NULL
                                 pixelsWide: width
                                 pixelsHigh: height
                                 bitsPerSample: 8
                                 samplesPerPixel: 4
                                 hasAlpha: YES
                                 isPlanar: NO
                                 colorSpaceName: NSCalibratedRGBColorSpace
                                 bytesPerRow: width * 4
                                 bitsPerPixel: 32];

        NSGraphicsContext *ctx = [NSGraphicsContext graphicsContextWithBitmapImageRep: rep];

        [NSGraphicsContext saveGraphicsState];
        [NSGraphicsContext setCurrentContext: ctx];

        NSRect r;

        [[NSColor whiteColor] setFill];
        r = NSMakeRect(0, 0, width, height);
        NSRectFill(r);

        [[NSColor blackColor] setFill];
        r = NSMakeRect(width / 8, height / 8, width * 3 / 4, height * 3 / 4);
        NSRectFill(r);

        [[NSColor greenColor] setStroke];
        for(int i = 0; i < 4; i++)
        {
            NSPoint p1 = NSMakePoint(width * (i + 1) / 5, height / 5);
            NSPoint p2 = NSMakePoint(width / 5, height * (i + 1) / 5);
            [NSBezierPath strokeLineFromPoint: p1 toPoint: p2];
        }

        [ctx flushGraphics];
        [NSGraphicsContext restoreGraphicsState];

        return rep;
    }
```

This function can then be used to create the image that each flood fill test will operate on, to make each test totally consistent. The dimensions are left up to the caller here, and I decided to test on images of `10000` pixels square, which is hefty enough for the operation to take a substantial amount of time, but still fast enough to make for a decent testing cycle.

For the measurement itself, I wrote a function that takes a block, runs it several times, and measures how fast it runs. It's not generally a good idea to only run the code once, because transient events can strongly influence how long a particular run takes. For example, a background process might suddenly allocate a bunch of memory, causing your process's memory to be swapped out to disk, then back in again, making it run much slower than usual. Running several times helps even out these transients.

The next question is, how do you distill the results from all of the runs into a single number you can compare? The most obvious way is to simply take an average, but this isn't necessarily appropriate. For computation-heavy code like this, there are a lot of random events that could pop up to make it run slower than usual, but essentially nothing could happen to make it run _faster_ than usual.

Given that, the obvious choice is to use the fastest run out of all the trials. However, having an ingrained distrust of outliers, I opeted for the second-fastest run instead. It should provide essentially the same result.

Here's the function I wrote to do the test. It takes a name and a block and runs the block ten times. It measures each invocation's running time, and tracks all of the running times. Once all of the runs are complete, it grabs the second-best time out of the array and returns it to the caller:

```
    NSArray *Time(NSString *name, void (^block)(void))
    {
        NSMutableArray *times = [NSMutableArray array];
        int trials = 10;
        for(int i = 0; i < trials; i++)
        {
            @autoreleasepool
            {
                NSLog(@"Running trial %d of %d", i + 1, trials);
                NSTimeInterval start = [[NSProcessInfo processInfo] systemUptime];
                block();
                NSTimeInterval end = [[NSProcessInfo processInfo] systemUptime];
                NSLog(@"Done, total elapsed time is %f seconds", end - start);
                [times addObject: @(end - start)];
            }
        }
        NSArray *sortedTimes = [times sortedArrayUsingSelector: @selector(compare:)];
        NSTimeInterval secondBest = [sortedTimes[1] doubleValue];
        NSLog(@"%@: Second best time is %f, times are %@", name, secondBest, sortedTimes);

        return @[name, @(secondBest)];
    }
```

It also returns the name to the caller, purely to make it easier on the caller when aggregating the results.

With the testing infrastructure in place, we can measure the performance of the original `FloodFill` function. The result on my computer is roughly 26.2 seconds. Tolerable, for such a gigantic image, but not great.

**Setting a Lower Bound**  
I decided to write a simple fill routine to set a bound on the speed of the flood fill function. It simply scans _every_ pixel of the image and fills the pixel if it's within the threshold from the starting pixel. It will fill areas that are not contiguous with the starting pixel, so it's not useful as a flood fill. However, it's fast, and since it touches every pixel in the image, it gives a pretty decent lower bound. Since the flood fill area in the test image covers most of it, it's unlikely that any flood fill could ever surpass the speed of this dumb whole-image scan:

```
    void CheckAll(struct Pixel *image, int width, int height, int startx, int starty, struct Pixel fillValue, int threshold)
    {
        struct Pixel startPixel = PIXEL(startx, starty);

        for(int i = 0; i < width * height; i++)
        {
            int diff = PixelDiff(startPixel, image[i]);
            if(diff <= threshold)
                image[i] = fillValue;
        }
    }
```

Running this through the tester gives a run time of 0.5 seconds. Clearly, there's substantial room for improvement over the 26.2 second running time of the original flood fill.

**Profiling**  
Measuring the running time of the function is important to optimization, but to actually perform useful optimizations we need more specific data. We need to profile the code to see where the time is being spent. Although the much-beloved [Shark](https://www.mikeash.com/pyblog/friday-qa-2009-02-06-profiling-with-shark.html) is dead, Instruments is a decent substitute. In particular, the Time Profiler instrument provides far and away the best view of just where code is spending its time.

The Time Profiler instrument produces a call tree. Expanding it out, it shows each function under the "Symbol Name" column, and the amount and percentage of time spent in that function under the "Running Time" column.

To get more detail, you can double-click any function, and it will display that function's code and a percentage of time spent on each line. This is extremely useful when you have a slow function that's complex enough that you don't know exactly which part is slow.

**Pixels Visited Bitmap**  
Profiling the original flood fill function, the main source of slowness is immediately obvious. A huge amount of time is spent checking for membership in `NSIndexSet` and adding new indexes to the set. There are two `NSIndexSet`s in play here, but it seems fairly clear that the worst offender is the `pixelsSeen` set, which tracks the pixels that have already been seen and shouldn't be checked again. Over a quarter of the function's running time is spent in `containsIndex:`, which is only sent to `pixelsSeen`. The first order of business is to replace `pixelsSeen` with something faster.

This variable basically stores a single bit of information per pixel, namely whether that pixel has been visited or not. A natural way to store this information is with a bitmap. Essentially, make a new image with one bit per pixel that corresponds exactly to the image being filled. To mark a pixel as visited, set the bit to `1`. To test a pixel, just grab the corresponding bit.

C doesn't offerd bit-addressed arrays, but no matter. We can use an array of bytes, and do some bit twiddling to get at the individual bits. For a given index, the byte to access is just `index / 8`, and the bit is just `index % 8`. I used the `CHAR_BIT` macro to be clean, even though the odds of running this code on a system where `CHAR_BIT != 8` are only marginally better than the odds of winning the lottery while being simultaneously struck by lightning and being eaten by a shark.

With the byte and bit index, a bit of bitshifting and a bitwise `or` allows setting a bit within the bitmap:

```
    static inline void AddToBitmap(int x, int y, uint8_t *bitmap, int width)
    {
        int index = x + y * width;
        int bytes = index / CHAR_BIT;
        int bits = index % CHAR_BIT;
        uint8_t bit = 1 << bits;
        bitmap[bytes] |= bit;
    }
```

Similarly, a bitwise `and` allows checking whether the bit is set:

```
    static inline BOOL CheckBitmap(int x, int y, uint8_t *bitmap, int width)
    {
        int index = x + y * width;
        int bytes = index / CHAR_BIT;
        int bits = index % CHAR_BIT;
        uint8_t bit = 1 << bits;
        return bitmap[bytes] & bit ? YES : NO;
    }
```

The flood fill function must then allocate the bitmap when it starts up. It has to allocate a chunk of memory whose size is equal to the number of pixels in the image divided by eight, rounded up. This bit of code handles that:

```
    int length = width * height;
    int bytes = (length + CHAR_BIT - 1) / CHAR_BIT;
    uint8_t *pixelsSeen = calloc(1, bytes);
```

The uses of `pixelsSeen` then get replaced with calls to `AddToBitmap` and `CheckBitmap`. Finally, we free the bitmap at the end of the function:

```
    free(pixelsSeen);
```

Running the new version, the running time for the flood fill is down to 12.6 seconds. This one change made things over twice as fast!

**Pixel Queue**  
Profiling the new code shows that `NSIndexSet` is once again taking up most of the time. The `pixelsToExamine` variable is the only `NSIndexSet` remaining, so it clearly must be the culprit. `NSIndexSet` is fast enough to be acceptable here, but it's clearly not optimized for this particular use. This is only to be expected, since this is definitely not the use it was built for.

I'll replace the `NSIndexSet` with a simple stack of coordinates. This will be a big array and an index indicating the top of the array. Adding a coordinate will mean simply setting the element at the top of the array and incrementing the index. Retrieving the next coordinate to examine is simply a matter of decrementing the index and grabbing the value at the top of the array. Allocating enough memory to hold a coordinate for every pixel is impractical, so instead I'll dynamically increase the size of the array when required.

First, I make a variable to hold the current array length. This lets the code know when it hits the end of the array and needs to reallocate:

```
    int pixelsToExamineLength = 128;
```

I chose `128` simply because it's a decent middle size, and the number sounded nice. The exact number is probably not too important, as long as it's not `0` and not so large that it consumes an excessive amount of memory for no reason.

Next, I make a simple `Coordinate` structure, a variable to point to the array of coordinates, and allocate memory for it:

```
    struct Coordinate { int x, y; };
    struct Coordinate *pixelsToExamine = malloc(sizeof(*pixelsToExamine) * pixelsToExamineLength);
```

Then, there's a variable to hold the index of the current top of the stack:

```
    int pixelsToExamineIndex = 0;
```

Finally, the starting pixel is added to the stack:

```
    pixelsToExamine[pixelsToExamineIndex++] = (struct Coordinate){ startx, starty };
```

The top of the loop now examines and pulls from the array:

```
    while(pixelsToExamineIndex > 0)
    {
        struct Coordinate coordinate = pixelsToExamine[--pixelsToExamineIndex];

        int x = coordinate.x;
        int y = coordinate.y;
```

When adding a new coordinate to the array, it first checks the index to see if the array is full and needs to be reallocated. If it's full, it just doubles the length and calls `realloc` to allocate more memory:

```
    if(pixelsToExamineIndex >= pixelsToExamineLength)
    {
        pixelsToExamineLength *= 2;
        pixelsToExamine = realloc(pixelsToExamine, sizeof(*pixelsToExamine) * pixelsToExamineLength);
    }
```

Once enough memory is available, it simply stores the desired coordinate into the top of the array and increments the index:

```
    pixelsToExamine[pixelsToExamineIndex++] = (struct Coordinate){ nextX, nextY };
```

Don't forget to deallocate the memory at the end of the function:

```
    free(pixelsToExamine);
```

How did we do? Running this new flood fill function takes about 4.8 seconds, once again more than doubling the performance of the code. We're doing very well compared to the original time of 26.2 seconds, but more performance can be extracted.

**Linear Memory Access**  
Profiling this latest version now shows basically all of the run time is spent within the flood fill function itself. This is only to be expected, as it hardly makes any external calls at this point. Aside from very occasionally allocating or deallocating memory, it spends all of its time working internally. At this point, it's time to take advantage of Time Profiler's ability to examine the code within a function and see what the remaining bottlenecks are.

Double-clicking on the flood fill function in Instruments pulls up the source code and shows the time spent on each line. The line taking up the most time by far is the body of `ComponentDiff`, which is just:

```
    return MAX(a, b) - MIN(a, b);
```

Clearly there isn't much that can be done to speed this up. This is already as fast as it can get. The only other way to speed this up would be to simply call it less, but `ComponentDiff` has to run at least three times on every pixel examined (once per component), and the current code only runs it three times per pixel. This code is now as fast as it can possibly go, right?

Right?

Obviously the answer is "no", otherwise you'd be at the end of the article now. However, the way forward from here is deeply non-obvious and took me a long time to figure out.

I had some false starts trying to make the `ComponentDiff` function faster. Was there a way to make `MIN` and `MAX` faster? Could the subtraction be vectorized, so that all three components run at once?

It turned out that this was all completely wrong-headed, and the answer lies in a completely different direction.

RAM, despite being officially "random access", isn't truly random access these days. Modern computer memory is a complex hierarchical system which is optimized for common access patterns. Truly random access is quite slow compared to linearly reading or writing a long, contiguous chunk of memory.

When it comes to manipulating an image, this means that you always want to write code that iterates over `x` in the inner loop, like so:

```
    for(int y = 0; y < height; y++)
        for(int x = 0; x < width; x++)
            // Do something with pixel (x, y)
```

Since images are normally laid out in memory by rows, this code iterates over memory in a completely linear fashion, which is really fast. Writing the loops in a more conventional order ends up being substantially slower:

```
    for(int x = 0; x < width; x++)
        for(int y = 0; y < height; y++)
            // Do something with pixel (x, y)
```

This code jumps around a lot. For a 32-bit image that's 1024 pixels wide, this code will read the first pixel, then read a second pixel that's 4kB away in memory. The third pixel will be another 4kB down, etc. This scattered memory access is really slow.

Flood fill is not quite the simple systematic iteration of the above for loops, but it's ultimately similar. It iterates over a potentially large number of contiguous pixels, and the order in which it iterates will affect just how quickly the computer's memory is able to return pixels.

The massive amount of time spent in `ComponentDiff` is suspicious. It's a pretty simple operation, and there's a lot of other code running, so why is this one operation taking up half of the total run time? With the performance characteristics of modern RAM in mind, maybe the calculations themselves aren't taking up all of this time. Instead, it might just be that the calculations are spending a lot of time waiting for the data to be loaded from RAM.

Let's look at the access patterns of the flood fill function to see if this is really it, and whether it can be improved. The latest flood fill function uses a stack to store which pixels to examine. A stack operates in a last-in, first-out manner, where things come off the stack in the opposite order that they were put in. The last thing placed on the stack is the first thing to be retrieved. When a pixel adds adjacent pixels to the stack, those adjacent pixels will be the next ones to be examined. This contiguous access is what we want.

The big question is then: does it access rows before columns, or columns before rows? Here's the code that enqueues the new pixels to examine:

```
    int nextXs[4] = { x + 1, x - 1, x, x };
    int nextYs[4] = { y, y, y + 1, y - 1 };
    for(int i = 0; i < 4; i++)
    {
        int nextX = nextXs[i];
        int nextY = nextYs[i];
        // enqueue...
```

Remember, these pixels are popped off the stack in last-in, first-out order. The first pixel examined will be `(x, y - 1)`, which is the pixel above the current pixel. That pixel will do its own thing and enqueue the one above _it_, and so on until the entire column is filled above. After the flood fill runs in that direction, it'll run downward, then finally go left and lastly right. This is pretty much the opposite of what we need for good performance.

This is really easy to fix, though: just reverse the arrays!

```
    int nextXs[4] = { x, x, x - 1, x + 1 };
    int nextYs[4] = { y - 1, y + 1, y, y };
```

With only this change, the flood fill function drops from 4.8 seconds to 2.9 seconds. This really shows the value of good memory access patterns!

**Linear Memory Access, Part Two**  
Although the last optimization almost looked impossible, it's still worth running the profiler again to see if the change exposed any new bottlenecks. `ComponentDiff` is under 10% in the new profile, showing just how much of a difference the memory access pattern makes to memory-intensive code like this.

There are two noticeable hotspots with the latest flood fill function. One is the `pixelsSeen` bitmap, which manifests in a lot of time spent in `AddToBitmap` and `CheckBitmap`.

The access pattern for `pixelsSeen` is different from the access pattern for the image's pixels itself. Because it gets checked and set when enqueueing rather than when dequeueing, all four of a pixel's neighbors get checked, and potentially set, immediately. The pixels on the same row are fine, but the pixels above and below are far away in memory. It's exactly the sort of non-local memory access that the previous optimization tries to avoid in the image, although on a much smaller scale, since the pixels in `pixelsSeen` are only one bit instead of 32 bits.

Still, it appears to be worth attacking. My strategy is to change the `Coordinate` `struct` into a `Command` `struct` which will hold not only an `(x, y)` pair, but also a command to execute on that pair. There will be two commands. The `EXAMINE` command will do the same thing that the flood fill algorithm currently does: test the pixel's color and fill it and enqueue new pixels if it matches. The `ENQUEUE_VERTICALS` will point at the original pixel, and will enqueue the pixels above and below as part of a second pass.

This accesses the `pixelsSeen` bitmap much more nicely. It will simply scan left and right of the current pixel. After the stack gets popped back down to this pixel, only then will it scan above and below. By this time, those are likely to be filled, so it will just be a quick check and then done. The next command will likely be the command to scan above and below a horizontally adjacent pixel, making for nice linear accesses once again.

To actually implement this, we first need to define the commands, which I simply wrote as `enum`s:

```
    enum {
        EXAMINE,
        ENQUEUE_VERTICALS
    };
```

Next, `Coordinate` and `pixelsToExamine` need to change to incorporate a new field to hold the command:

```
    struct Command { int command; int x, y; };
    struct Command *pixelsToExamine = malloc(sizeof(*pixelsToExamine) * pixelsToExamineLength);
```

I'm now going to be enqueueing pixels in three places, and enqueueing two different commands. To cut back on duplicated code, I wrote a macro to handle enqueueing a command:

```
    #define ENQUEUE(...) do { \
            if(pixelsToExamineIndex >= pixelsToExamineLength) \
            { \
                pixelsToExamineLength *= 2; \
                pixelsToExamine = realloc(pixelsToExamine, sizeof(*pixelsToExamine) * pixelsToExamineLength); \
            } \
            pixelsToExamine[pixelsToExamineIndex++] = (__VA_ARGS__); \
        } while(0)
```

Note the use of `...`, which allows the macro to accept a C99 compound literal, like:

```
    ENQUEUE((struct Command){ command, x, y });
```

The C preprocessor isn't wise to the ways of compound literals, so it sees that as three separate parameters, separated by the commas.

The most common scenario will be enqueueing a pixel to examine, so I wrote a macro for that as well. This macro checks the pixel's coordinates to make sure they're within the image's bounds, and also checks the `pixelsSeen` bitmap, then uses `ENQUEUE` to add a new `EXAMINE` command if everything is good:

```
    #define ENQUEUE_PIXEL(x, y) do { \
            if((x) >= 0 && (y) >= 0 && (x) < width && (y) < height) \
                if(!CheckBitmap(x, y, pixelsSeen, width)) \
                    ENQUEUE((struct Command){ EXAMINE, (x), (y) }); \
        } while(0)
```

Now we have to change the rest of the function to use these commands.

The first change is when enqueueing the starting pixel. This now becomes:

```
    ENQUEUE((struct Command){ EXAMINE, startx, starty });
```

I'm not using `ENQUEUE_PIXEL` because I don't want all of the extra checking it does for this one, although it wouldn't really hurt.

The loop starts off pretty much the same, popping the command off the top of the stack:

```
    while(pixelsToExamineIndex > 0)
    {
        struct Command command = pixelsToExamine[--pixelsToExamineIndex];
        int x = command.x;
        int y = command.y;
```

At this point, it examines the actual command and branches. If it's `EXAMINE`, then the code is much like before. It adds the pixel to `pixelsSeen`, checks `PixelDiff` against `threshold`, and fills:

```
        if(command.command == EXAMINE)
        {
            AddToBitmap(x, y, pixelsSeen, width);

            int diff = PixelDiff(startPixel, PIXEL(x, y));
            if(diff <= threshold)
            {
                PIXEL(x, y) = fillValue;
```

At this point, the old code would enqueue the four adjacent pixels. Instead, we'll enqueue the two horizontally adjacent pixels, and one `ENQUEUE_VERTICALS` command for the current pixel. We do them backwards, since the stack is last-in, first-out:

```
                ENQUEUE((struct Command){ ENQUEUE_VERTICALS, x, y });
                ENQUEUE_PIXEL(x - 1, y);
                ENQUEUE_PIXEL(x + 1, y);
            }
        }
```

The code for an `ENQUEUE_VERTICALS` command is simple: just enqueue the pixels above and below:

```
        else if(command.command == ENQUEUE_VERTICALS)
        {
            ENQUEUE_PIXEL(x, y - 1);
            ENQUEUE_PIXEL(x, y + 1);
        }
    }
```

How does this optimization do? The previous version took 2.9 seconds, and this version takes only 1.9 seconds. Not too bad for the _second_ revision after what appeared to be an impasse.

At this point, we've started to hit diminishing returns. The final flood fill function is about 14 times faster than the original, plenty to brag about.

For those having trouble keeping track of all the changes made to the function throughout this article, here's a full listing of the final version of it:

```
    void FloodFill(struct Pixel *image, int width, int height, int startx, int starty, struct Pixel fillValue, int threshold)
    {
    #define PIXEL_TO_INDEX(x, y) ((x) + (y) * width)
    #define PIXEL(x, y) image[PIXEL_TO_INDEX(x, y)]

        enum {
            EXAMINE,
            ENQUEUE_VERTICALS
        };

        int length = width * height;
        int bytes = (length + CHAR_BIT - 1) / CHAR_BIT;
        uint8_t *pixelsSeen = calloc(1, bytes);

        int pixelsToExamineLength = 128;
        struct Command { int command; int x, y; };
        struct Command *pixelsToExamine = malloc(sizeof(*pixelsToExamine) * pixelsToExamineLength);
        int pixelsToExamineIndex = 0;
    #define ENQUEUE(...) do { \
            if(pixelsToExamineIndex >= pixelsToExamineLength) \
            { \
                pixelsToExamineLength *= 2; \
                pixelsToExamine = realloc(pixelsToExamine, sizeof(*pixelsToExamine) * pixelsToExamineLength); \
            } \
            pixelsToExamine[pixelsToExamineIndex++] = (__VA_ARGS__); \
        } while(0)

    #define ENQUEUE_PIXEL(x, y) do { \
            if((x) >= 0 && (y) >= 0 && (x) < width && (y) < height) \
                if(!CheckBitmap(x, y, pixelsSeen, width)) \
                    ENQUEUE((struct Command){ EXAMINE, (x), (y) }); \
        } while(0)

        ENQUEUE((struct Command){ EXAMINE, startx, starty });
        struct Pixel startPixel = PIXEL(startx, starty);

        while(pixelsToExamineIndex > 0)
        {
            struct Command command = pixelsToExamine[--pixelsToExamineIndex];
            int x = command.x;
            int y = command.y;

            if(command.command == EXAMINE)
            {
                AddToBitmap(x, y, pixelsSeen, width);

                int diff = PixelDiff(startPixel, PIXEL(x, y));
                if(diff <= threshold)
                {
                    PIXEL(x, y) = fillValue;

                    ENQUEUE((struct Command){ ENQUEUE_VERTICALS, x, y });
                    ENQUEUE_PIXEL(x - 1, y);
                    ENQUEUE_PIXEL(x + 1, y);
                }
            }
            else if(command.command == ENQUEUE_VERTICALS)
            {
                ENQUEUE_PIXEL(x, y - 1);
                ENQUEUE_PIXEL(x, y + 1);
            }
        }

        free(pixelsSeen);
        free(pixelsToExamine);
    #undef ENQUEUE
    #undef ENQUEUE_PIXEL
    }
```

**Conclusion**  
Effective optimization requires good measurements and careful thoughts. Appropriate data structures and algorithms are key, and should always be the first place you look when you need to optimize a routine. In this case, `NSIndexSet` ended up being a pretty slow choice for pixel membership tests and queueing, and more appropriate, specialized solutions were much faster. When operating on large amounts of data, pay close attention to your memory access patterns. Linear memory access will be far faster than scattered access.

Micro-optimizations should always be the choice of last resort. We could have spent ages trying to apply micro-optimizations to `ComponentDiff` and never made any sort of measurable difference, while simply rearranging the order in which pixels were visited sped up the function by over 60%.

Finally, be sure to only optimize when necessary, and what's necessary. Don't waste time optimizing code that doesn't take up a significant amount of time in the first place. Measure first, identify bottlenecks, and only then see if they might be worth improving.

This flood fill function can probably be optimized further, although the easiest speed improvements are long gone by now. Profiling reveals the various `ENQUEUE` operations to be the bottleneck in the latest version. It should be possible to improve the speed of the queue by packing values more efficiently, being smarter about the checks that are performed, etc. An algorithmic overhaul to work in terms of scanline segments rather than individual pixels is probably the best hope for gaining more speed. Most flood fill operations will have rows of many contiguous pixels, and representing the entire row as a `(startx, endx, y)` tuple could make for a major speed win. This is known as a [scanline flood fill](http://will.thimbleby.net/scanline-flood-fill/).

One thing that stood out at me when looking at this last version of the flood fill was that `AddToBitmap` is only called after a pixel is dequeued. This seems wasteful, as the same pixel could accumulate multiple entries in the command queue, which will then be wasted. This can be avoided by calling `AddToBitmap` when enqueueing a new pixel instead of when dequeueing. However, in practice, this resulted in no measurable change in performance. I didn't look to hard to figure out why, but this is a good lesson in why measurement is essential for this kind of work.

That's it for today. Come back next time for the next wacky adventure. Friday Q&A is driven by reader suggestions as always, so if you have any suggestions for topics you'd like to see, please [send them in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).

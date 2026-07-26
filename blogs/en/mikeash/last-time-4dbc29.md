---
title: Last time
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-09-14-implementing-a-flood-fill.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6f7f13b492711236'
translated: false
---

> 原文：[Last time](https://www.mikeash.com/pyblog/friday-qa-2012-09-14-implementing-a-flood-fill.html)　·　mikeash.com Friday Q&A

Posted at 2012-09-14 14:16 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-09-28: Optimizing Flood Fill](https://www.mikeash.com/pyblog/friday-qa-2012-09-28-optimizing-flood-fill.html)  
Previous article: [Friday Q&A 2012-08-31: Obtaining and Interpreting Image Data](https://www.mikeash.com/pyblog/friday-qa-2012-08-31-obtaining-and-interpreting-image-data.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa) [image](https://www.mikeash.com/pyblog/?tag=image)

Friday Q&A 2012-09-14: Implementing a Flood Fill

by [Mike Ash](https://www.mikeash.com/)

**Theory**  
A flood fill takes a starting point and a color. It then searches for contiguous points from that starting point which match the starting point's color. It sets all of those points to the fill color. In short, if you start a flood fill on a patch of color, it will change the color of the whole patch, but no other parts of the image, including parts that have the same color but aren't connected.

A refinement to this is to have a threshold instead of simply looking for an exact color match. Any color that's close enough to the starting point's color counts as being part of the fill region.

To implement this, we'll keep two lists of pixels. One list will be a list of candidate pixels to examine. This list will start off containing the starting point. The other list will be a list of pixels that have already been examined. We'll then enter a loop. Each time through the loop, we'll pull a pixel off the candidate list and check it out. If the candidate's color is close enough to the starting pixel's color, we'll fill the candidate by setting its color to the fill color. We'll then add the candidate to the list of pixels that have been examined, and add all four of its neighbors to the list of candidates, except for those neighbors which have already been examined.

One question is how to implement the lists of pixels. The most obvious way to do it in a Cocoa application is to use `NSMutableSet`s containing `NSValue` objects containing `NSPoint` values. This works, but it's really slow. Too slow to be usable. Running a flood fill over a reasonably sized section of a 640x480 image takes a minute or two, which is just awful. We need something faster.

A pixel coordinate is just two integers, an `x` and a `y`. However, as we saw earlier, for a given image, we can convert the coordinate into a single index by simply calculating `x + y * width`. So these lists really just need to be sets of indexes. As it happens, Cocoa has a class made just for storing sets of indexes: `NSIndexSet` and its mutable cousin `NSMutableIndexSet`.

I don't think that `NSIndexSet` was built with this application in mind, but it works perfectly for it, giving good performance with a straightforward API. With `NSMutableIndexSet` to store the pixel lists, and some simple calculations for the rest of the flood fill, we're on our way.

**Code**  
Here's the pixel structure from last time, which corresponds nicely to the RGBA image representation you get from a properly configured `NSBitmapImageRep`:

```
    struct Pixel { uint8_t r, g, b, a; };
```

To use the threshold, we need to compute the difference between two pixels. To do _that_, we need to compute the difference between two pixel components, which is just a simple subtraction:

```
    static inline int ComponentDiff(uint8_t a, uint8_t b)
    {
        return MAX(a, b) - MIN(a, b);
    }
```

To compute the difference of two pixels, we'll just add together the differences of the red, green, and blue components:

```
    static inline int PixelDiff(struct Pixel p1, struct Pixel p2)
    {
        return ComponentDiff(p1.r, p2.r)
             + ComponentDiff(p1.g, p2.g)
             + ComponentDiff(p1.b, p2.b);
    }
```

Now on to the flood fill function itself. It takes image data, its width and height, the starting pixel coordinate, the fill value, and the threshold:

```
    void FloodFill(struct Pixel *image, int width, int height, int startx, int starty, struct Pixel fillValue, int threshold)
    {
```

This function uses a few macros to convert pixel coordinates to indexes and back again:

```
    #define PIXEL_TO_INDEX(x, y) ((x) + (y) * width)
    #define INDEX_TO_X(index) ((index) % width)
    #define INDEX_TO_Y(index) ((index) / width)
```

There's also a macro to make it easier to access an individual pixel. Because this expands to a simple array access, it works for both reading and writing:

```
    #define PIXEL(x, y) image[PIXEL_TO_INDEX(x, y)]
```

We set up the two index sets that hold the lists of candidate pixels and pixels that already have been examined:

```
        NSMutableIndexSet *pixelsToExamine = [NSMutableIndexSet indexSet];
        NSMutableIndexSet *pixelsSeen = [NSMutableIndexSet indexSet];
```

Then add the starting pixel to the list of pixels to examine, and also store the starting pixel's color to use in the threshold computation:

```
        [pixelsToExamine addIndex: PIXEL_TO_INDEX(startx, starty)];
        struct Pixel startPixel = PIXEL(startx, starty);
```

Now it's time to enter the loop. We keep going as long as there are candidate pixels to examine:

```
        while([pixelsToExamine count] > 0)
        {
```

It grabs the first index in the list, removes it, and adds it to `pixelsSeen`:

```
            int index = [pixelsToExamine firstIndex];
            [pixelsToExamine removeIndex: index];
            [pixelsSeen addIndex: index];
```

Note that the choice of `firstIndex` is completely arbitrary. This could just as well be `lastIndex` or any other way of getting _some_ index in the set.

This index is converted to pixel coordinates:

```
            int x = INDEX_TO_X(index);
            int y = INDEX_TO_Y(index);
```

Next comes the threshold check. The difference between the pixel at `x, y` and the starting pixel is computed. If it's under the threshold, we proceed with the fill:

```
            int diff = PixelDiff(startPixel, PIXEL(x, y));
            if(diff <= threshold)
            {
```

The first thing is to actually perform the fill operation on this pixel by setting its value to the fill value:

```
                PIXEL(x, y) = fillValue;
```

The code then loops over the four neighbors of this pixel: above, below, left, and right. I used an array of x coordinates and another array of y coordinates, then just loop over those arrays:

```
                int nextXs[4] = { x + 1, x - 1, x, x };
                int nextYs[4] = { y, y, y + 1, y - 1 };
                for(int i = 0; i < 4; i++)
                {
                    int nextX = nextXs[i];
                    int nextY = nextYs[i];
```

The pixel we're looking at may lie at the edge of the image. If it does, the candidate pixels can lie off the edge. Such pixels must be detected and rejected to avoid accessing bad memory:

```
                    if(nextX >= 0 && nextY >= 0 && nextX < width && nextY < height)
                    {
```

If the candidate is within bounds, we convert the coordinate back to an index so it can be used with the pixel lists:

```
                        int next = PIXEL_TO_INDEX(nextX, nextY);
```

The `next` index is then added to `pixelsToExamine`, but only if it hasn't already been seen:

```
                        if(![pixelsSeen containsIndex: next])
                            [pixelsToExamine addIndex: next];
                    }
                }
            }
        }
    }
```

And that's it! The loop exits on its own once there are no more pixels to examine. Since the image is being mutated in place, there's nothing to return. Once the loop finishes, the flood fill has been completed. If you passed in an `NSBitmapImageRep`'s bitmap data, the `NSBitmapImageRep` will now contain the flood-filled image.

**Conclusion**  
This code plays nicely with the `ImageRepFromImage` function from [the last article](https://www.mikeash.com/pyblog/friday-qa-2012-08-31-obtaining-and-interpreting-image-data.html), allowing flood fills on any image that `NSImage` can load. The threshold computation is not particularly sophisticated, but it gets the job done here, and can easily be replaced with something more complex.

That's it for today! Come back next time for another wacky adventure. Friday Q&A is driven by reader submissions, so as always, if you have an idea that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-09-14-implementing-a-flood-fill.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).

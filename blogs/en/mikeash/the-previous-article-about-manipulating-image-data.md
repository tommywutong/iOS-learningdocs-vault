---
title: the previous article about manipulating image data
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-08-31-obtaining-and-interpreting-image-data.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a02108f1e8b09ad2'
translated: false
---

> 原文：[the previous article about manipulating image data](https://www.mikeash.com/pyblog/friday-qa-2012-08-31-obtaining-and-interpreting-image-data.html)　·　mikeash.com Friday Q&A

Posted at 2012-08-31 14:52 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-09-14: Implementing a Flood Fill](https://www.mikeash.com/pyblog/friday-qa-2012-09-14-implementing-a-flood-fill.html)  
Previous article: [Friday Q&A 2012-08-24: Things You Never Wanted To Know About C](https://www.mikeash.com/pyblog/friday-qa-2012-08-24-things-you-never-wanted-to-know-about-c.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa) [image](https://www.mikeash.com/pyblog/?tag=image)

Friday Q&A 2012-08-31: Obtaining and Interpreting Image Data

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Russian (translation by Science for Everyone)](https://i-love-png.com/obtaining-and-interpreting-image-data-rus.html), [Belarusian (translation by Science for Everyone)](https://i-love-png.com/obtaining-and-interpreting-image-data.html), [Lithuanian (translation by Erelis Steponavicius)](http://anynfo.com/penktadienis-qa-20120831/), [Ukrainian (translation by Sandi Wolfe)](http://www.opensourceinitiative.net/edu/pyblog/), [Czech (translation by Andrijana Savicević)](https://www.bildelerekspert.co.no/tips/?p=547), [Portuguese (translation by Artur Weber & Adelina Domingos)](https://www.homeyou.com/~edu/qa-de-sexta), and [Norwegian (translation by Rune Sk)](https://japsedeler.no/info/7.html).

**Theory**  
The simplest image representation is a plain bitmap. This is an array of bits, one per pixel, indicating whether it's black or white. The array contains rows of pixels one after another, so that the total number of bits is equal to the width of the image multiplied by the height. Here's an example bitmap of a smiley face:

```
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 1 0 0 1 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    0 1 0 0 0 0 1 0
    0 0 1 1 1 1 0 0
    0 0 0 0 0 0 0 0
```

Pure black and white is not a very expressive medium, of course, and accessing individual bits in an array is a bit of a hassle. Let's move a step up to using one byte per pixel, which allows grayscale (we can have zero be black, `255` be white, and numbers in between be different shades of gray) and makes it easier to access the elements as well.

Once again, we'll use an array of bytes with sequential rows. Here's some example code to allocate memory for the image:

```
    uint8_t *AllocateImage(int width, int height)
    {
        return malloc(width * height);
    }
```

To get to a particular pixel at `(x, y)`, we have to move down `y` rows, then across that row by `x` pixels. Since the rows are laid out sequentially, we move down `y` rows by moving through the array by `y * width` bytes. The index for a particular pixel is then `x + y * width`. Based on this, here are two functions for getting and setting a grayscale pixel at a particular coordinate:

```
    uint8_t ReadPixel(uint8_t *image, int width, int x, int y)
    {
        int index = x + y * width;
        return image[index];
    }

    void SetPixel(uint8_t *image, int width, int x, int y, uint8_t value)
    {
        int index = x + y * width;
        image[index] = value;
    }
```

Grayscale is still not all that interesting in many cases, and we want to be able to represent color. The typical way to represent colored pixels is with a combination of three values for red, green, and blue components. All zeroes results in black, with other values mixing the three colors together to form whatever color is needed. It's typical to use `8` bits per color, which results in `24` bits per pixel. Sometimes these are packed together, and sometimes they're padded with an extra `8` bits of emptiness to give `32` bits per pixel, which is nicer to work with since computers are usually good at manipulating `32`-bit values.

Transparency, or alpha, can also be handy to represent in an image. `8` bits of transparency fits nicely into the `8` bits of padding in a `32` bit pixel, and using `32` bit pixels holding red, green, blue, and alpha is probably the most common pixel format currently in use.

There are two ways to pack these pixels together. The common way is to just run them all together in sequence, so you'd have one byte of red, one byte of green, one byte of blue, and one byte of alpha all next to each other. Then you'd have red, green, blue, and alpha for the next pixel, and so forth. Each pixel occupies four bytes of contiguous memory.

It's also possible to store each color in a separate chunk of memory. Each chunk is called a plane, and this format is called "planar". In this case, you essentially have three or four (depending on whether alpha is present) regions of memory, each of which is laid out exactly like the pixels from the grayscale example from above. The pixel's color is a combination of the values from all of the planes. This can sometimes be more convenient to work with, but is often slower, due to bad locality of reference, and often _more_ complex to work with, so it's a much less common format.

The only other thing to figure out is how the colors are ordered. RGBA (red, green, blue, then alpha) ordering is the most common on the Mac, but orders like ARGB and BGRA show up occasionally as well. There's no particular reason to choose one over another, other than compatibility or speed. To avoid expensive format conversions, it's best to match the format used by whatever you'll be drawing to, saving to, or loading from, when possible.

**Obtaining Pixel Data**  
The Cocoa class which contains and provides pixel data is `NSBitmapImageRep`. This is a subclass of `NSImageRep`, which is an abstract class for a single "representation" of an image. `NSImage` is a container for one or more `NSImageRep` instances. In the case where there's more than one representation, they may represent different sizes, resolutions, color spaces, etc., and `NSImage` will choose the best one for the current context when drawing.

Given that, it _seems like_ it should be pretty easy to get the image data from an `NSImage`: find an `NSBitmapImageRep` in its representations, then ask that representation for its pixel data.

There are two problems with this. First, the image may not have an `NSBitmapImageRep` at all. There are representation types that aren't bitmaps. For example, an `NSImage` representing a PDF will contain vector data, not bitmap data, and use a different type of image representation. Second, even if the image does have an `NSBitmapImageRep`, there's no telling what the pixel format of that representation will be. It's not practical to write code to handle every possible pixel format, especially since it's going to be difficult to test most of the cases.

There's a lot of code out there that does this anyway. It gets away with it by making assumptions about the contents of the `NSImage` and the pixel format of the `NSBitmapImageRep`. This is not reliable, and should be avoided.

How _do_ you reliably get pixel data, then? You can _draw_ an `NSImage` reliably, and you can draw _into_ an `NSBitmapImageRep` using the `NSGraphicsContext` class, and you can get pixel data _from_ that `NSBitmapImageRep`. Chain it all together, and you can get pixel data.

Here's some code to handle this sequence. The first thing it does is figure out the pixel width and height of the bitmap representation. This is _not_ necessarily obvious, as `NSImage`'s `size` doesn't have to correspond to pixel dimensions. This code will use `size` anyway, but depending on your situation, you may want to use a different way to figure out the size:

```
    NSBitmapImageRep *ImageRepFromImage(NSImage *image)
    {
        int width = [image size].width;
        int height = [image size].height;

        if(width < 1 || height < 1)
            return nil;
```

Next, we create the `NSBitmapImageRep`. This involves the use of a _really_ long initializer method which looks kind of frightening, but I'll go through all of the parameters in detail:

```
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
                                 bitsPerPixel: 32]
```

Let's look at these parameters one by one. The first argument, `BitmapDataPlanes`, allows you to specify the memory where the pixel data will be stored. Passing `NULL` here, as this code does, tells `NSBitmapImageRep` to allocate its own memory internally, which is usually the most convenient way to handle this.

Next, the code specifies the number of pixels wide and high, which it computed previously. It just passes those values in for `pixelsWide` and `pixelsHigh`.

Now we start getting into the actual pixel format. I mentioned earlier that 32-bit RGBA (where red, green, blue, and alpha each take up one byte and are laid out contiguously in memory) is a common pixel format, and that's what we're going to use. Since each sample is one byte, the code passes `8` for `bitsPerSample:`. The `samplesPerPixel:` parameter refers to the number of different components used in the image. We have four components (R, G, B, and A) and so the code passes `4` here.

The RGBA format has alpha, so we pass `YES` for `hasAlpha`. We don't want a planar format, so we pass `NO` for isPlanar. We want an RGB color space, so we pass `NSCalibratedRGBColorSpace`.

Next, `NSBitmapImageRep` wants to know how many bytes make up each row of the image. This is used in case padding is desired. Sometimes an image row uses more than the strictly minimum number of bytes, usually for performance reasons, to keep things aligned nicely. We don't want to mess around with padding, so we pass the minimum number of bytes needed for one row of pixels, which is just `width * 4`.

Finally, it asks for the number of bits per pixel. At `8` bits per component and 4 components, this is just `32`.

We now have an `NSBitmapImageRep` with the format we want, but how do we draw into it? The first step is to make an `NSGraphicsContext` with it:

```
        NSGraphicsContext *ctx = [NSGraphicsContext graphicsContextWithBitmapImageRep: rep];
```

An important note when troubleshooting: not all parameters for an `NSBitmapImageRep` are acceptable when creating an `NSGraphicsContext`. If this line complains about an unsupported format, that means that one of the parameters used to create the `NSBitmapImageRep` wasn't to the system's liking, so go back and double-check those.

The next step is set this context as the current graphics context. In order to make sure that we don't mess with any other graphics activity that might be going on, we first save the current graphics state, so we can restore it later:

```
        [NSGraphicsContext saveGraphicsState];
        [NSGraphicsContext setCurrentContext: ctx];
```

At this point, any drawing we do will go into our newly-minted `NSBitmapImageRep`. The next step is to simply draw the image.

```
        [image drawAtPoint: NSZeroPoint fromRect: NSZeroRect operation: NSCompositeCopy fraction: 1.0];
```

`NSZeroRect` is simply a convenient shortcut which tells `NSImage` to draw the entire image.

Now that the image is drawn, we flush the graphics context to ensure none of this stuff is still queued up, restore the graphics state, and return the bitmap:

```
        [ctx flushGraphics];
        [NSGraphicsContext restoreGraphicsState];

        return rep;
    }
```

Using this technique, you can get _anything_ that Cocoa is able to draw into a convenient `32`-bit RGBA bitmap.

**Interpreting Pixel Data**  
Now that we have the pixel data, what do we _do_ with it? Precisely what to do with it is up to you, but let's look at how to actually get at the pixel data.

Let's start by defining a struct to represent an individual pixel:

```
    struct Pixel { uint8_t r, g, b, a; };
```

This will line up with the RGBA pixel data stored in the `NSBitmapImageRep`. We can grab a pointer out of it to use:

```
    struct Pixel *pixels = (struct Pixel *)[rep bitmapData];
```

Accessing a specific pixel at `(x, y)` works just like the previous example code for grayscale images:

```
    int index = x + y * width;
    NSLog(@"Pixel at %d, %d: R=%u G=%u B=%u A=%u",
          x, y
          pixels[index].r,
          pixels[index].g,
          pixels[index].b,
          pixels[index].a);
```

Make sure that `x` and `y` are located within the image bounds before doing this, or else hilarious results may ensue. If you're lucky, out-of-bounds coordinates will crash.

To iterate over all of the pixels in the image, a simple pair of for loops will do:

```
    for(int y = 0; y < height; y++)
        for(int x = 0; x < width; x++)
        {
            int index = x + y * width;
            // Use pixels[index] here
        }
```

Notice how the `y` loop is the outermost one, even though `x` first would be the natural order. This is because it's much faster to iterate over the pixels in the same order that they're stored in memory, so that adjacent pixels are accessed sequentially. Putting `x` on the inside does this, and the resulting code is much friendlier to the cache and memory controllers which are built to handle sequential access.

A modern compiler is likely to generate good code for the above, but in case you're paranoid and want to make sure the compiler won't generate a multiply and array index for every loop iteration, you can iterate using pointer arithmetic instead:

```
    struct Pixel *cursor = pixels;
    for(int y = 0; y < height; y++)
        for(int x = 0; x < width; x++)
        {
            // Use cursor->r, cursor->g, etc.
            cursor++;
        }
```

Finally, note that this data is _mutable_. If you should so desire, you can actually modify `r`, `g`, `b`, and `a`, and the `NSBitmapImageRep` will reflect the changes.

**Conclusion**  
Dealing with raw pixel data isn't something you usually have to do, but if you need it, Cocoa makes it relatively easy. The technique is a little roundabout, but by drawing into an `NSBitmapImageRep` with a chosen pixel format, you can obtain pixel data in the format of your choice. Once you have that pixel data, it's a simple matter of indexing into it to obtain the individual pixel values.

That's it for today! Friday Q&A is driven by reader ideas as always, so if you have any suggestions for topics you'd like to see covered in a future installment, please [send them in](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).

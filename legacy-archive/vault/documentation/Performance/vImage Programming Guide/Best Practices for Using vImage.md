---
title: vImage Programming Guide
apple_id: TP30001001
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Accelerate
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vImage/BestPractices/BestPractices.html
archived_at: '2026-07-27T06:57:05.617719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vImage Programming Guide](Introduction%20to%20vImage%20Programming%20Guide.md)


[Next](Glossary.md)[Previous](Performing%20Image%20Transformation%20Operations.md)

# Best Practices for Using vImage

This chapter gives guidelines for getting optimal performance from vImage. It covers the following best practices:

- Make sure the system your application runs on meets the basic requirements
- Use the Image I/O framework to load images into memory
- When possible, use planar image formats
- Take advantage of tiles
- Align data buffers
- Reuse buffers
- Use threads appropriately
- Separate 2D kernels into multiple 1D kernels

## Loading Image Data

The first step to integrating vImage into your own applications is getting raw image data loaded into memory. You can use the Image I/O framework to load images of any major image file format (.JPG, .PNG, .GIF) into C-style buffers (void \* arrays).

Below is an example of how to extract raw image data from a local file. If you would like to know more about the other methods and options available in Image I/O, see _[Image I/O Programming Guide](../../Graphics%20Imaging/Image%20I-O%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrs)_.

```
NSURL* url = [NSURL fileURLWithPath:filename];
//Create the image source with the options left null for now
//Keep in mind since we created it, we're responsible for getting rid of it
CGImageSourceRef image_source = CGImageSourceCreateWithURL( (CFURLRef)url, NULL);
if(image_source == NULL)
{
    //Something went wrong
    fprintf(stderr, "VImage error: Couldn't create image source from URL\n");
    return false;
}
//Now that we got the source, let's create an image from the first image in the CGImageSource
CGImageRef image = CGImageSourceCreateImageAtIndex(image_source, 0, NULL);

//We created our image, and that's all we needed the source for, so let's release it
CFRelease(image_source);

if(image == NULL)
{
    //something went wrong
    fprintf(stderr, "VImage error: Couldn't create image source from URL\n");
    return false;
}
```

After you’ve loaded the images into the buffers, they are ready to be passed to vImage functions. Pay close attention to the character sequence that follows the underscore in the function name—this is the format that it expects the pixel data to match. vImage functions can either work in-place (the output is in the same buffer that was passed as input) or they use a destination buffer that you can supply.

Since vImage handles only the image processing, you need to look to another technology to actually display the image. Depending on the goal of your application, or the application environment you used (Carbon or Cocoa), you may have to find a way of displaying the resultant pixel data (Quartz, for example), or saving the image data to disk (Image I/O).

### Use Planar Image Formats

Most vImage functions come with four image format variants, (one for each of the image formats understood by vImage). Planar images encode one single channel at a time (e.g. all the byte data for the red channel is stored consecutively, then all for the green channel, then the blue, then alpha, and so on), instead of mixing the bits of all channels throughout the in-memory representation of the image (interleaved).

Since most vImage functions have to separate by channel the bits of the images you pass to it anyway (thus putting it into a planar format), it frequently makes sense to do this ahead of time. Since vImage usually works only on one channel at a time anyway, having your image data grouped by channel saves you the time that would usually be spent deinterleaving and reinterleaving each pixel. So in general, use planar image formats as much as possible.

__Note:__ In some cases you may not even need all red, green, blue, and alpha channels. For example, you may know beforehand that the alpha channel is irrelevant in the images that you’re dealing with, or perhaps all of your images are grayscale and thus can use only one channel. Using planar formats makes it is possible to isolate only the channels you need.

### Take Advantage of Tiles

Tiling is a technique commonly used in graphics applications that takes a large image and breaks it into several, smaller images. This is called tiling because much like how floor tiles can be placed together to create a larger floor, small subunits of an image can be stitched together to form a larger image. The benefit behind this method is that CPUs tend to handle data a lot faster when it fits in their high-speed data caches.

In general, vImage functions have much better performance when the data they process (including input and output buffers) fit in processor data caches. Data stored in the CPU caches can be accessed a lot faster than data stored in main memory. While CPU cache memory is fast, it is also limited in space. Cache size varies from processor to processor, but in general it’s good to keep image tile sizes below 2 MB for Intel processors and below 512 KB for PowerPC processors.

- Here are some tips for tiling:

  - Some caches can only hold a small amount at a time (usually 512 KB or less)

    - Tile sizes of 128 KB - 256 KB give overall best throughput
  - Many vImage functions use tiling (along with multithreading)internally. If you want to control tiling yourself, set the `kvImageDoNotTile` flag in the flags parameter when you call a function, which prevents the function from using tiling or multithreading internally.
  - For square tiles, a tile size of 128 KB to 256 KB gives the best overall throughput.
  - Which functions tile or multithread internally is subject to change from one release to another. If you are doing your own tiling or multithreading, you can probably improve performance by using the `kvImageDoNotTile` flag with all functions. You may also need the `kvImageDoNotTile` flag if you are concerned about vImage blocking on a condition variable while worker threads do the work. This may be required to prevent a priority inversion in real time code.
  - The best tile size varies according to function. Functions with very little computation per byte (mostly conversion functions) are fastest with tiles smaller than 16 KB. Typical vImage functions do best with 256 KB tiles. Tile size is less important for computation-heavy functions (such as those that use multithreading).

### Align Data Buffers

When allocating floating-point data for images, it’s important to keep the data 4-byte aligned. This means that the amount of bytes that you allocate should be an integer multiple of 4.

Here are some tips about data alignment and buffer sizes:

- Though vImage tolerates lesser alignments, for best performance, everything should be 16-byte aligned and `rowbytes` should be a multiple of 16 bytes.
- Floating-point data must be at least 4-byte aligned or some functions will fail.
- The value you pass in the `rowBytes` parameter to a function should not be a power of 2.

### Reuse Buffers

Many vImage functions use temporary buffers to hold intermediate values when performing a task. Creating this buffer once initially, and supplying it to the various functions can save time depending on how frequently you call the functions.

If you do not provide a buffer, these functions allocate memory for themselves (and, of course, deallocate it when they are finished).

If you are going to call the function only a small number of times, and the possibility of blocking on a lock for a short period of time is not a concern, it is sensible to let the function allocate the buffer itself.

Each function that uses a temporary buffer has a `src` and a `dest` parameter (both of type `vImage_Buffer`). The function uses only the `height` and `width` fields of these parameters; the `data` and `rowBytes` fields are ignored.

If possible, applications should also try to reuse the regular image buffers that the `data` field of `vImage_Buffer` data type points to. This saves time otherwise spent reallocating and zero-filling the buffer.

In order to facilitate real-time usage, vImage avoids, as much as possible, usage of the heap and other operations that block on a lock, such as memory allocation

### Thread Appropriately

vImage is thread-safe and can be called reentrantly. If you tile your image, you can use separate threads for different tiles. If you use different processors to handle different tiles, you should choose tiles that are not horizontally adjacent to each other. Otherwise the tile edges may share cache lines, potentially resulting in time-consuming crosstalk between the two processors.

The state of a vImage output buffer is undefined while a vImage call is working on it. There may be times when the value of a pixel is neither the starting data or ending result, but the result of some intermediate calculation.

In OS X v10.4 and later, some vImage functions are transparently multithreaded internally. They do their own parameter checking and only multithread in cases where it is expected that a performance benefit will be obtained. vImage maintains its own lazily allocated pool of threads to do this work. Thus, your code should just automatically be multithreaded without you doing anything for those vImage functions that have been internally multithreaded. (In OS X v10.4.0, these are most functions in `Geometry.h`, and the gamma functionality.) The threads are not destroyed once created. They are reused. The calling thread may block while it is waiting for the secondary threads to finish their work. It is safe to call internally multithreaded functions reentrantly.

Thread-safe functions use locks to maintain data coherency. If you don’t want functions to use locks, you may prevent vImage from multithreading and tiling by passing the `kvImageDoNotTile` flag. If you use this flag, your application is responsible for tiling its own data and doing its own multithreading.

### Separate 2D Kernels into 1D Kernels

If you’re using convolution to apply filters to images, you can sometimes gain a performance boost by splitting the two-dimensional kernel into multiple one-dimensional kernels, and then applying the convolution twice (once per dimension).

You can, of course, pass the 2D kernel to one of the `vImageConvolve` functions. vImage uses the 2D kernel to perform nine multiply and eight add operations to compute each pixel result. To get better performance, call the `vImageConvolve` function twice, once for each of the 1D convolve filters. When separated, vImage performs three multiply and two add operations per pixel per convolve pass, for a total of six multiply and four add operations. You’ll notice that separating the convolution kernel into multiple passes, there is an algorithmic savings of one third of the multiply operations and half the add operations. For a M x N kernel, the processing cost is roughly reduced from M\*N to M+N when kernels are separated. For larger kernels, the savings becomes more dramatic. A 5 x 5 kernel might be 2.5 times faster when separated, and a 11x11 kernel might be over 5 times faster!

Keep in mind that this technique may be slower in routines where the cost of traversing the image is higher than the arithmetic involved. This typically happens when the images are very large, or they don’t fit into physical RAM.

There are cases involving very large filters where separating the filter may be the only way to perform the convolution operation. A very larger filter that sums to a value larger than 224, over its entirety or any part, runs the risk of overflowing the accumulators that vImage uses for 8-bit vImage convolution operations. In such cases, separating the kernel is likely to allow you to avoid the overflow. You can even use this to add more fixed-point precision into your filter, by scaling the filter values to be larger. The extent to which the loss of precision from the intermediate rounding offsets this advantage is unknown.

Separating the filters might be slower in routines where the cost of traversing the image is higher than the arithmetic involved. This typically happens with very large images, or images that don’t fit into physical RAM.

[Next](Glossary.md)[Previous](Performing%20Image%20Transformation%20Operations.md)

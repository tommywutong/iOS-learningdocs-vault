---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/CreatingandManagingImageObjects/Creating%20and%20Managing%20Image%20Objects.html
archived_at: '2026-07-18T01:48:59.383135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenCL Programming Guide for Mac](About%20OpenCL%20for%20OS%20X.md)


[Next](Creating%20and%20Managing%20Buffer%20Objects%20In%20OpenCL.md)[Previous](Memory%20Objects%20in%20OS%20X%20OpenCL.md)

# Creating and Managing Image Objects In OpenCL

OpenCL has built-in support for processing image data. Using image objects, you can take image data that resides in host memory and make it available for processing in a kernel executing on an OpenCL device. Image objects simplify the process of representing and accessing image data since they offer native support for a multitude of image formats. If you are writing kernel functions that need to efficiently perform calculations on image data, you will find OpenCL for OS X’s native support for images useful.

This chapter illustrates how to take image data residing in host memory and place it into image objects that a kernel can access. It also provides an overview of how to go about processing this image data. See [Parameters That Describe Images and Buffers in OS X OpenCL](Memory%20Objects%20in%20OS%20X%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjqgmwvgvzs) for conceptual descriptions of the kinds of parameters typically passed to these functions.

To create image objects, use `gcl_create_image`. This function can be used to create two-dimensional image and three-dimensional image objects. To specify a two-dimensional image, set the `image_depth` parameter to `0`. To create a three-dimensional image object, specify the `image_depth` in pixels. If you pass an `IOSurfaceRef` as the `io_surface` parameter, the image will be created using the IOSurface you pass. Otherwise, set the `io_surface` parameter to `NULL`.

```
cl_image gcl_create_image(
                            const cl_image_format *image_format,
                            size_t image_width,
                            size_t image_height,
                            size_t image_depth,
                            IOSurfaceRef io_surface
);
```

| Parameter | Description |
| --- | --- |
| `image_format` | An OpenCL image format descriptor. |
| `image_width` | The image width in pixels. |
| `image_height` | The image height in pixels. |
| `image_depth` | The image depth in pixels. |
| `io_surface` | If you pass an `IOSurfaceRef` as the `io_surface` parameter, the image will be created using the IOSurface you pass. Otherwise, set this parameter to `NULL`. |
|
|  |  |

After you’ve created the image object, you can enqueue reads, writes, and copies between it and host memory. From your host application, you can use the following functions:

- To copy data between two images or to copy data from one portion of an image to another portion (in the same image), call:

```
void gcl_copy_image(
               cl_image dst_image,
               cl_image src_image,
               const size_t dst_origin[3],
               const size_t src_origin[3],
               const size_t region[3]);
```

  The copy starts from `src_origin` (an x, y, z value) and starts writing at `dst_origin` (also x, y, z). It copies the two- or three-dimensional rectangular amount specified by `region`. Because we are copying between images, all parameters are specified in pixels.
- To copy data from an image to a buffer, call:

```
void gcl_copy_image_to_ptr(
                void *buffer_ptr,
                cl_image src_image,
                const size_t src_origin[3],
                const size_t region[3]);
```

  The `buffer_ptr` parameter points to the destination buffer to which pixels will be copied. The `src_image` is the image from which pixels are to be copied. The `src_origin` is the first pixel to be copied. The `region` is the region to which pixels are to be copied. Because we are copying from an image, the origin and region are specified in pixels.

  For example, say we have a 4 pixel x 4 pixel image. Each pixel requires 4 bytes, one byte for each red, green, blue, and alpha channel. In this example, we want to take a portion of this image data—say a region 3 pixels wide and 2 pixels high—starting at pixel 1,1 of the image and copy this portion of the image to a buffer. In [Figure 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjrguwvgvzt), we would want to copy all the light and dark green pixels, but not the gray pixels.

  __Figure 8-1__  Copying a portion of an image to a buffer

  !!

  Because our image requires four bytes per pixel and we want to copy out 3 x 2 = 6 pixels, we require a buffer of (at least) 6 x 4 = 24 bytes to accommodate the copy.

  The call would look like this:

```
const size_t origin[3] = { 1, 1, 0 };
const size_t region[3] = { 3, 2, 1};
gcl_copy_image_to_ptr(our_buffer, the_image, origin, region);
```
- To copy data from a buffer to an image, call:

```
void gcl_copy_ptr_to_image(
                cl_image dst_image,
                void *src_buffer_ptr,
                const size_t dst_origin[3],
                const size_t buffer_region[3]);
```

  The parameters you pass to the `gcl_copy_ptr_to_image` function are similar to those passed to the `gcl_copy_image_to_ptr` function, except that the destination is the image and the pixels are being copied from a buffer.

The `gcl_copy`\* functions enable you to move images to and from host memory. To actually process this image data on a device, you have to make this data available to the work items that execute on the device. The following sections show you how to pass your data to the kernels for further processing.

See [How the Kernel Interacts With Data in OS X OpenCL](How%20the%20Kernel%20Interacts%20With%20Data%20in%20OS%20X%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrrfvjvomi) for more information.

To map a region in an image into the host address space, call:

```
void *gcl_map_image(cl_image image,
                    cl_map_flags map_flags,
                    const size_t origin[3],
                    const size_t region[3]);
```

Returns a pointer to the region it has mapped.

| Parameter | Description |
| --- | --- |
| `image` | The image to be mapped. |
| `map_flags` | Bitfield specifying `CL_MAP_READ` and/or `CL_MAP_WRITE`, depending on how you intend to use the returned pointer. |
| `origin` | The (x, y, z) position in pixels in the image at which to start the mapping. |
| `region` | The region (in pixels) to read. |
|
|  |  |

This function provides functionality similar to that of the OpenCL standard `clEnqueueMapImage` function.

To unmap memory mapped by the `gcl_map_ptr` or `gcl_map_image` functions, call:

```
void gcl_unmap(void *ptr);
```

| Parameter | Description |
| --- | --- |
| `ptr` | Pointer to the device memory, or image, to unmap. |
|
|  |  |

To avoid memory leaks, image objects should be freed when they are no longer needed.

- `void gcl_retain_image(cl_image image)`
- `void gcl_release_image(cl_image image)`

In the following example, the host creates one image for input and one image for output, calls the kernel to swap the red and green pixels, then checks the results.

__Listing 8-1__  Sample host function creates images then calls kernel function

```c
#include <stdio.h>
#include <stdlib.h>
#include <OpenCL/opencl.h>

// Include the automatically-generated header which provides the kernel block
// declaration.
#include "kernels.cl.h"

#define COUNT 2048

static void display_device(cl_device_id device)
{
    char name_buf[128];
    char vendor_buf[128];

    clGetDeviceInfo(device, CL_DEVICE_NAME, sizeof(char)*128, name_buf, NULL);
    clGetDeviceInfo(device, CL_DEVICE_VENDOR, sizeof(char)*128, vendor_buf, NULL);

    fprintf(stdout, "Using OpenCL device: %s %s\n", vendor_buf, name_buf);
}

static void image_test(const dispatch_queue_t dq)
{
    // This example uses a dispatch semaphore to achieve synchronization
    // between the host application and the work done for us by the OpenCL device.
    dispatch_semaphore_t dsema = dispatch_semaphore_create(0);

    // This example creates a "fake" RGBA, 8-bit-per channel image, solid red.
    // In a real program, you would use some real raster data.
    // Most OpenCL devices support a wide variety of image formats.

    unsigned int i;
    size_t height = 2048, width = 2048;

    unsigned int *pixels =
               (unsigned int*)malloc( sizeof(unsigned int) * width * height );

    for (i = 0; i < width*height; i++)
        pixels[i] = 0xFF0000FF; // 0xAABBGGRR: 8bits per channel, all red.

    // This image data is on the host side.
    // You need to create two OpenCL images in order to perform some
    // manipulations: one for the input and one for the ouput.

    // This describes the format of the image data.
    cl_image_format format;
    format.image_channel_order = CL_RGBA;
    format.image_channel_data_type = CL_UNSIGNED_INT8;

    cl_mem input_image = gcl_create_image(&format, width, height, 1, NULL);
    cl_mem output_image = gcl_create_image(&format, width, height, 1, NULL);

    dispatch_async(dq, ^{

      // This kernel is written such that each work item processes one pixel.
      // Thus, it executes over a two-dimensional range, with the width and
      // height of the image determining the dimensions
      // of execution.

        cl_ndrange range = {
            2,                  // Using a two-dimensional execution.
            {0},                // Start at the beginning of the range.
            {width, height},    // Execute width * height work items.
            {0}                 // And let OpenCL decide how to divide
                                // the work items into work-groups.
        };

        // Copy the host-side, initial pixel data to the image memory object on
        // the OpenCL device.  Here, we copy the whole image, but you could use
        // the origin and region parameters to specify an offset and sub-region
        // of the image, if you'd like.
        const size_t origin[3] = { 0, 0, 0 };
        const size_t region[3] = { width, height, 1 };
        gcl_copy_ptr_to_image(input_image, pixels, origin, region);

        // Do it!
        red_to_green_kernel(&range, input_image, output_image);

        // Read back the results; then reuse the host-side buffer we
        // started with.
        gcl_copy_image_to_ptr(pixels, output_image, origin, region);

        // Let the host know we're done.
        dispatch_semaphore_signal(dsema);
    });

    // Do other work, if you'd like...

    // ... but eventually, you will want to wait for OpenCL to finish up.
    dispatch_semaphore_wait(dsema, DISPATCH_TIME_FOREVER);

    // We expect '0xFF00FF00' for each pixel.
    // Solid green, all the way.
    int results_ok = 1;
    for (i = 0; i < width*height; i++) {
        if (pixels[i] != 0xFF00FF00) {
            fprintf(stdout,
                "Oh dear. Pixel %d was not correct.
                 Expected 0xFF00FF00, saw %x\n",
                i, pixels[i]);
            results_ok = 0;
            break;
        }
    }

    if (results_ok)
        fprintf(stdout, "Image results OK!\n");

    // Clean up device-size allocations.
    // Note that we use the "standard" OpenCL API here.
    clReleaseMemObject(input_image);
    clReleaseMemObject(output_image);

    // Clean up host-side allocations.
    free(pixels);
}

int main (int argc, const char * argv[])
{
    // Grab a CPU-based dispatch queue.
    dispatch_queue_t dq = gcl_create_dispatch_queue(CL_DEVICE_TYPE_CPU, NULL);
    if (!dq)
    {
        fprintf(stdout, "Unable to create a CPU-based dispatch queue.\n");
        exit(1);
    }

    // Display the OpenCL device associated with this dispatch queue.
    display_device(gcl_get_device_id_with_dispatch_queue(dq));

    image_test(dq);

    fprintf(stdout, "\nDone.\n\n");

    dispatch_release(dq);
}
```


__Listing 8-2__  Sample kernel swaps the red and green channels

```
// A simple kernel that swaps the red and green channels.

const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_FILTER_NEAREST;

kernel void red_to_green(read_only image2d_t input, write_only image2d_t output)
{
    size_t x = get_global_id(0);
    size_t y = get_global_id(1);

    uint4 tap = read_imageui(input, sampler, (int2)(x,y));
    write_imageui(output, (int2)(x,y), tap.yxzw);
}
```

[Next](Creating%20and%20Managing%20Buffer%20Objects%20In%20OpenCL.md)[Previous](Memory%20Objects%20in%20OS%20X%20OpenCL.md)


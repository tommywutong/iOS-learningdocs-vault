---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/SynchronizingIOSurfacesAcrossProcessors/SynchronizingIOSurfacesAcrossProcessors.html
archived_at: '2026-07-18T01:49:04.139318Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenCL Programming Guide for Mac](About%20OpenCL%20for%20OS%20X.md)


[Next](Autovectorizer.md)[Previous](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md)

# Using IOSurfaces With OpenCL

An IOSurface is an abstraction for sharing image data. IOSurfaces are an efficient way to manage image memory because when you use an IOSurface, if no copy is necessary, no time is wasted on making a copy. An IOSurface transcends APIs, architectures, address spaces, and processes.

If you create an OpenCL image from an IOSurface, you can use the OpenCL C language to modify the image data, taking full advantage of the parallelism OpenCL gives you. You use the IOSurface’s ID to pass the IOSurface from process to process, so that completely separate applications can share the same object. This makes sharing an IOSurface between devices very easy.

If you create an OpenCL image memory object from an existing IOSurface, you can modify the data contained in the IOSurface either in your main program running on the CPU, or in an OpenCL kernel running on either the CPU or a GPU.

If you want to modify or read the IOSurface directly on the host, then you need to first call the `IOSurfaceLock` function. Call the `IOSurfaceUnlock` function when done. Otherwise, you can just use the image in OpenCL as if it were a normal, old non-IOSurface-backed image.

You can either create an IOSurface in code or you can request an IOSurface from another running process such as Photo Booth. The underlying texture transfer mechanism for an IOSurface combines `GL_UNPACK_CLIENT_STORAGE_APPLE` and `GL_STORAGE_HINT_CACHED_APPLE` together. The transfer is done as a straight DMA to and from system memory and video memory with no format conversions of any kind (other than some GPU-specific memory layout details). No matter how many different OpenGL contexts (in the same process or not) bind a texture to an IOSurface, they all share the same system memory and GPU memory copies of the data.

Once you’ve created or obtained an IOSurface, before you use it in OpenCL, you need to create an OpenCL image memory object using the IOSurface. When you create the memory object, you are not making a copy; the image memory object points at the same memory as the original IOSurface. This makes using the IOSurface very efficient.

If you are using GCD to interact with the IOSurface, create the IOSurface-backed CL image as shown in [Listing 12-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjxfvjvooa).

__Listing 12-1__  Creating an IOSurface-backed CL Image

```
// Create a 2D image (depth = 0 or 1) or a 3D image (depth > 1).
// Can also be used to create an image from an IOSurfaceRef.
cl_image gcl_create_image(
  const cl_image_format *image_format,
  size_t image_width,
  size_t image_height,
  size_t image_depth,
  IOSurfaceRef io_surface);
```

If you are using the standard OpenCL API and not using GCD to create an IOSurface-backed OpenCL object, use `clCreateImageFromIOSurface2D` as shown in [Listing 12-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjxfvjvooi).

__Listing 12-2__  Extracting an Image From an IOSurface

```
cl_image_format image_format;
image_format.image_channel_order = CL_RGBA;
image_format.image_channel_data_type = CL_UNORM_INT8;
cl_mem image = clCreateImageFromIOSurface2D(
  context, flags, image_format, width, height, surface, &err
);
```


Sharing an IOSurface in OpenCL is very simple. The key is to lock the IOSurface properly.

If your CPU (host) is going to modify the IOSurface and then share it with an OpenCL device, you should lock the IOSurface before reading or writing to it, then unlock it before passing it to a kernel:

- The host creates or obtains the IOSurface and creates its OpenCL image object.
- If the host will be writing to the IOSurface, the host write-locks the IOSurface by calling the `IOSurfaceLock(..., write type lock)` function. If the host will only be reading from the IOSurface, the host read-locks it.
- The host writes to and reads from the IOSurface as necessary.
- The host unlocks the IOSurface by calling the `IOSurfaceUnlock(...)` function. This tells the system that you changed the data. You can then use the IOSurface-backed image in OpenCL. The IOSurface object handles any necessary read-locking internally for you.
- The host enqueues the OpenCL kernel, passing it the IOSurface.

The locking and unlocking are simply the minimal calls needed to give OS X enough information to ensure that each device always gets the latest, correct data.

If you will be using OpenCL to modify the IOSurface, you don't have to lock it. Just access the image memory object directly.

[Next](Autovectorizer.md)[Previous](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md)


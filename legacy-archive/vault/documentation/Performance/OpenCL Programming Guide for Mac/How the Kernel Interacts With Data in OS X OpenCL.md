---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/InteractingWiththeKernelinOSXOpenCL/InteractingWiththeKernelinOSXOpenCL.html
archived_at: '2026-07-18T01:48:59.796639Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenCL Programming Guide for Mac](About%20OpenCL%20for%20OS%20X.md)


[Next](Using%20Grand%20Central%20Dispatch%20With%20OpenCL.md)[Previous](Identifying%20Parallelizable%20Routines.md)

# How the Kernel Interacts With Data in OS X OpenCL

There are two parts of every OpenCL program. The part that runs on the device is called the _kernel_; the part that creates memory objects, then configures and calls the kernel is called the _host_ and usually runs on the CPU. A kernel is essentially a function written in the OpenCL language that enables it to be compiled for execution on any device that supports OpenCL. The kernel is the only way the host can call a function that will run on a device. When the host invokes a kernel, many work items start running on the device. Each work item runs the code of the kernel, but works on a different part of the dataset. The kernel manages work items by accessing them using their IDs using functions such as `get_global_id(…)` and `get_local_id(…)`. Although kernels are enqueued for execution by host applications written in C, C++, or Objective-C, a kernel must be compiled separately to be customized for the device on which it is going to run.

Interacting with kernels is easier using tools provided by OS X than it is using standard OpenCL. As of OS X v10.7, you can include OpenCL kernels as resources in Xcode projects and compile them along with the rest of your application. Also as of OS X v10.7, the host can invoke kernels by passing them parameters just as if they were typical functions (see [Passing Data To a Kernel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrrfvjvomy)); it is no longer necessary to explicitly set kernel arguments using special OpenCL APIs.

In order for a device to actually process data, you have to make the data available to the work items that execute on the device.

To pass data from the host to a compute kernel:

- Prepare the input data.
- Specify how data is to be assigned to work items. See [Specifying How To Divide Up A Dataset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrrfvjvoni).
- Create buffer and image object(s) of the appropriate size. Move the input data from host memory using `gcl_malloc` or the various `gcl_ copy` functions (such as `gcl_memcpy`) to the device. See [Memory Objects in OS X OpenCL](Memory%20Objects%20in%20OS%20X%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjqgmwvgvzu) for more information.
- Invoke the kernel. Unlike in standard OpenCL, you don't have to explicitly set kernel arguments or enqueue the kernel to an OpenCL command queue; instead just queue the kernel as a block to a dispatch queue. See [Passing Data To a Kernel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrrfvjvomy).
- Retrieve results. See [Retrieving Results From a Kernel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrrfvjvona).

When you write a kernel in OpenCL, you are writing the code that each work item will execute-instructions on how to process one portion of your overall dataset. By launching many work items, each of which operates on just a small portion of the data, you end up processing the whole data set. The _ndrange structure_ is used to specify how data is assigned to work items.

The n-dimensional range (`cl_ndrange`) structure you pass to the kernel consists of the following fields:

- `size_t work_dim`:

  The number of dimensions to use for the kernel launch: 1, 2, or 3.

  Some problems are easiest to break up into kernel-sized chunks if you treat them as one-dimensional. An example of this type of problem is computing the md5 hash for a list of 50 million words. You could write a kernel that computes the md5 hash for one word and launch 50 million instances of the kernel. In this case, the ndrange is a 1-D range: a single range (0 - 50 million) that has only one coordinate. You can think of it as as index. In your kernel, you can call `get_global_id(0)`, and it will give you that coordinate—a value from 0 to 49,999,999 that represents the index into your data that this instance of the kernel should process.

  If your data represents a flat image that is _x_ pixels wide by _y_ pixels high, then you have a two-dimensional data set with each data point represented by its coordinates on the x and y axes. Many image processing algorithms are best represented using a two-dimensional ndrange. Let's say you want to do something different to each pixel of a 2048 x 1024 image. You could write an OpenCL kernel that does something to a single pixel, and then launch it using an two-dimensional ndrange with a global work size of 2048 x 1024. In this case, your kernel is (obviously) not one-dimensional. You can call `get_global_id(0)` and `get_global_id(1)` to get the x,y coordinates of _this_ instance in the entire ndrange. Because there is a 1-to-1 mapping between the ndrange and pixels, selecting the pixel to process is really easy; just call these two functions.

  If you are dealing with spatial data that involves the _(x, y, z)_ position of nodes in three-dimensional space, you can use a three-dimensional ndrange.

  Another way to look at the dimensionality of your data is in terms of nested loops in traditional, non-parallel applications. If you can loop through your entire data set with a single loop, then your data is one-dimensional. If you would use one loop nested in another, your data is two-dimensional, and if you would have loops nested three-deep to cycle through all your data, your data is three-dimensional.
- `global_work_size`:

  The `global_work_size` field specifies the size of each dimension. Effectively, this determines the number of total work items that will be launched. If you have a one-dimensional range and you want to process a million things, then the `global_work_size` field will be `{1000000, 0, 0}`. If you are processing a 2048 pixel by 1024 pixel image, you would set `work_dim = 2` and `global_work_size = { 2048, 1024, 0 }`.

  The only constraint on the `global_work_size` is that the work size of each dimension must be a multiple of the `local_work_size` of that dimension.
- `global_work_offset`:

  The `global_work_offset` field specifies a per-dimension offset to add to the values returned by `get_global_id(…)`. Say, for example, you have a list of one million words and you want to compute the md5 hash of words 50,000 - 60,000. Because the data is one-dimensional, the ndrange would have a `work_dim` of `1`. Because there are 10,000 items to be processed, set `global_work_size = {10000, 0, 0}`. To "skip" to word 50,000 from the get-go, set the `global_work_offset = {50000, 0, 0}`. That way, the very first call to `get_global_id(0)` returns the 50,000th pixel, the second returns the 50,001st pixel, and so on.
- `local_work_size`:

  A _workgroup_ is a collection of work items that execute on the same compute unit on the same OpenCL device. The way data is broken up into workgroups can affect the performance of an algorithm on certain hardware. When enqueuing a kernel to execute on a device, you can specify the size of the workgroup that you’d like OpenCL to use during execution. By providing OpenCL with a suggested workgroup size, you are telling it how you would like it to delegate the work items to the various computational units on the device. Work items within a workgroup have the unique ability to share local memory with one another, and synchronize with one another at programmer-specified barriers.

  The `local_work_size` gives you control over the workgroup size directly.

Xcode uses your kernel code to automatically generate the kernel function prototype in the kernel header file. To pass data to a kernel, pass the memory objects as parameters (just as you would pass parameters to any other function) when you call the kernel from your host code. OpenCL kernel arguments can be scoped with a local or global qualifier, designating the memory storage for these arguments. This means that, as of OS X v10.7, kernel parameters declared with the `local` or  `__local` address qualifier are declared as `size_t` in the block declaration of the kernel.

For example, if a kernel has an argument declared with the `local` address qualifier:

```
kernel void foo(
                global float *a,
                local float *shared);  // This kernel parameter is of type
                                       // local float; will be size_t in the
                                       // kernel block
```

The compiler generates the following extern declaration of this kernel block:

```
extern void (^foo_kernel)(
                  const cl_ndrange *ndrange,
                  float *a,
                  size_t shared       // In the generated declaration,
                                      // local float is declared as size_t
             );
```

By associating your buffer objects with specific kernel arguments, you make it possible to process your data using a kernel function. For example, in [Example: Allocating, Using, and Releasing Buffer Objects](Creating%20and%20Managing%20Buffer%20Objects%20In%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjrgywvgvzrge), notice how the code sample treats the input data pointer much as you would treat a pointer in C. In this example, the input data is an array of `float` values, and you can process each element of the `float` array by indexing into the pointer.

If the kernel will be returning results in a buffer, call a function such as `gcl_memcpy(…)` while inside a block on a given queue.

To make sure that the results are all accessible to the host before you continue, use `dispatch_sync` or wait using another synchronization method.

If the kernel will be returning results in a buffer, call the `dispatch_sync` function like this:

```
dispatch_sync(queue,
              ^{
                 gcl_memcpy(ptr_c,
                            device_c,
                            num_floats * sizeof(float));
               });
```

If the kernel will be returning results in an image, call the `dispatch_sync` function like this:

```
dispatch_sync(queue,^{
                         size_t origin = {0,0,0};
                         size_t region = {512, 512, 1};
                         gcl_copy_image_to_ptr(
                                             results_ptr,
                                             image,
                                             origin,
                                             region);
                       });
```

This will copy the bytes for 512 x 512 pixels from the image to the buffer specified by the `results_ptr` parameter.

[Next](Using%20Grand%20Central%20Dispatch%20With%20OpenCL.md)[Previous](Identifying%20Parallelizable%20Routines.md)


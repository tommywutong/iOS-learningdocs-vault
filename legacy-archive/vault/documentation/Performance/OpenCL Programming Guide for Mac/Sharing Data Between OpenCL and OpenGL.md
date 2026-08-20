---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/shareGroups/shareGroups.html
archived_at: '2026-07-18T01:49:31.782223Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenCL Programming Guide for Mac](About%20OpenCL%20for%20OS%20X.md)


[Next](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md)[Previous](Creating%20and%20Managing%20Buffer%20Objects%20In%20OpenCL.md)

# Sharing Data Between OpenCL and OpenGL

OpenGL (Open Graphics Library) is an API for writing applications that produce two- and three-dimensional computer graphics. OpenCL and OpenGL are designed to interoperate. In particular, OpenCL and OpenGL can share data, which reduces overhead. For example, OpenGL objects and OpenCL memory objects created from OpenGL objects can access the same memory. In addition, GLSL (OpenGL Shading Language) shaders and OpenCL kernels can access the shared data.

To make sure OpenCL and OpenGL work together smoothly:

- Set your program up to do all its computation and rendering on the GPU.

  This will improve performance because you’ll avoid having to transfer data between the host and the GPU.
- Allocate memory to ensure that data is shared efficiently.

This chapter shows how the OpenCL API can be used to create OpenCL memory objects from OpenGL vertex buffer objects (VBOs), texture objects, and renderbuffer objects. It also shows how to create OpenCL buffer objects from OpenGL buffer objects and how to create an OpenCL image object from an OpenGL texture or renderbuffer object.

To allow an OpenCL application to access an OpenGL object, use an OpenCL context that is created from an OpenGL _sharegroup_ (`CGLShareGroupObj`) object. Open_CL_ objects you create in this context will reference these Open_GL_ objects. When an OpenCL context is connected to an OpenGL sharegroup object in this way, both the OpenCL and OpenGL contexts can reference the same objects.

[Figure 10-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrqfvjvomy) illustrates a typical scenario in which Open_CL_ generates geometry on the GPU and Open_GL_ renders the shared geometry, also on the GPU. They may see what they are looking at as different objects - in this case, OpenGL sees the data as a VBO and OpenCL sees it as a `cl_mem`. The result is that both the OpenCL and OpenGL contexts end up referencing the same sharegroup (CGLShareGroupObj) object, see the same devices, and access this shared geometry.

__Figure 10-1__  OpenGL and OpenCL share data using sharegroups

!

To interoperate between OpenCL and OpenGL:

1. Set the sharegroup:

```
CGLContextObj cgl_context = CGLGetCurrentContext();
CGLShareGroupObj sharegroup = CGLGetShareGroup(cgl_context);
gcl_gl_set_sharegroup(sharegroup);
...
```
2. After the sharegroup has been set, you can create OpenCL memory objects from the existing OpenGL objects:

   - To create an OpenCL buffer object from an OpenGL buffer object, call:

```
void * gcl_gl_create_ptr_from_buffer(GLuint bufobj);
```
   - To create an OpenCL image object from an OpenGL texture object, call:

```
cl_image gcl_gl_create_image_from_texture(
            GLenum texture_target,
            GLint mip_level,
            GLuint texture);
```
   - To create an OpenCL two-dimensional image object from an OpenGL render buffer object, call:

```
cl_image gcl_gl_create_image_from_renderbuffer(GLuint render_buffer);
```


To ensure data integrity, the application must synchronize access to objects shared by OpenCL and OpenGL. Failure to provide such synchronization may result in race conditions or other undefined behavior including non-portability between implementations. For information about synchronizing OpenCL and OpenGL events and fences, see [Controlling OpenCL / OpenGL Interoperation With GCD](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjyfvjvomi).

This code example is excerpted from the [OpenCL Procedural Geometric Displacement Example with GCD Integration](https://developer.apple.com/library/mac/#samplecode/OpenCL_Procedural_Geometric_Displacement_Example/Introduction/Intro.html). It shows how OpenCL can bind to existing OpenGL buffers in order to avoid copying data back from a compute device when it needs to use the results of the computation for rendering. In this example, an OpenCL compute kernel displaces the vertices of an OpenGL-managed vertex buffer object (_VBO_). The compute kernel calculates several octaves of procedural noise to push the resulting vertex positions outwards and calculates new normal directions using finite differences. The vertices are then rendered by OpenGL.

To build this application:

1. Include the header file generated by Xcode. This header file contains the kernel block declaration.

   `#include "displacement_kernel.cl.h"`
2. Declare the dispatch queue and the dispatch semaphore used for synchronization between OpenCL and OpenGL. For more information about the dispatch semaphores, see [Synchronizing A Host With OpenCL Using A Dispatch Semaphore](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjyfvjvonq).

```
static dispatch_queue_t queue;
static dispatch_semaphore_t cl_gl_semaphore;
```
3. Declare the memory objects that will hold input and output data.

```
static void *InputVertexBuffer;
static void *OutputVertexBuffer;
static void *OutputNormalBuffer;
```
4. Set the sharegroup, create the dispatch queue and the dispatch semaphore, and get the compute device.

```
static int setup_compute_devices(int gpu)
{
    int err;
    size_t returned_size;
    ComputeDeviceType =
      gpu ? CL_DEVICE_TYPE_GPU : CL_DEVICE_TYPE_CPU;

    printf(SEPARATOR);
    printf("Using active OpenGL context...\n");

    // Set the sharegroup.
    CGLContextObj kCGLContext =
                  CGLGetCurrentContext();
    CGLShareGroupObj kCGLShareGroup =
                  CGLGetShareGroup(kCGLContext);

    gcl_gl_set_sharegroup(kCGLShareGroup);

    // Create a dispatch queue.
    queue = gcl_create_dispatch_queue(
                  ComputeDeviceType, NULL);
    if (!queue)
    {
        printf("Error: Failed to create a dispatch queue!\n");
        return EXIT_FAILURE;
    }

    // Create a dispatch semaphore.
    cl_gl_semaphore = dispatch_semaphore_create(0);
    if (!cl_gl_semaphore)
    {
        printf("Error:
           Failed to create a dispatch semaphore!\n");
        return EXIT_FAILURE;
    }

    // Get the device ID.
    ComputeDeviceId =
         gcl_get_device_id_with_dispatch_queue(queue);

    // Report the device vendor and device name.
    cl_char vendor_name[1024] = {0};
    cl_char device_name[1024] = {0};
    err = clGetDeviceInfo(
            ComputeDeviceId, CL_DEVICE_VENDOR,
            sizeof(vendor_name), vendor_name,
            &returned_size);
    err|= clGetDeviceInfo(
            ComputeDeviceId, CL_DEVICE_NAME,
            sizeof(device_name), device_name,
            &returned_size);
    if (err != CL_SUCCESS)
    {
        printf(
            "Error: Failed to retrieve device info!\n");
        return EXIT_FAILURE;
    }

    printf(SEPARATOR);
    printf(
            "Connecting to %s %s...\n",
             vendor_name, device_name);
    return CL_SUCCESS;
}
```
5. Create the memory objects that will hold input and output data and initialize the input memory object with the input data.

   This example creates a new memory object, `InputVertexBuffer`, using the `gcl_malloc` function. It then uses the `gcl_gl_create_ptr_from_buffer` function to create OpenCL objects (`OutputVertexBuffer` and `OutputNormalBuffer`) from existing OpenGL VBOs (`VertexBufferId` and `NormalBufferId`). The `InputVertexBuffer` memory object is initialized with input data stored in `VertexBuffer`, using the `gcl_memcpy` function.

```
static int setup_compute_memory()
{
    size_t bytes =
        sizeof(float) * VertexComponents * VertexElements;

    printf(SEPARATOR); 
    printf("Allocating buffers on compute device...\n");

    InputVertexBuffer = gcl_malloc(bytes, NULL, 0);
    if (!InputVertexBuffer)
    {
        printf("Failed to create InputVertexBuffer!\n");
        return EXIT_FAILURE;
    }
    OutputVertexBuffer =
        gcl_gl_create_ptr_from_buffer(VertexBufferId);
    if (!OutputVertexBuffer)
    {
        printf("Failed to create OutputVertexBuffer!\n");
        return EXIT_FAILURE;
    }

    OutputNormalBuffer =
        gcl_gl_create_ptr_from_buffer(NormalBufferId);
    if (!OutputNormalBuffer)
    {
        printf("Failed to create OutputNormalBuffer!\n");
        return EXIT_FAILURE;
    }

    dispatch_async(queue,
        ^{gcl_memcpy(
           InputVertexBuffer,
           VertexBuffer, VertexBytes);});

    return CL_SUCCESS;
}
```
6. Create the compute kernel from the kernel block generated by Xcode.

```
static int setup_compute_kernels(void)
{
    int err = 0;

    ComputeKernel =
       gcl_create_kernel_from_block(displace_kernel);

    // Get the maximum work group size for executing
    // the kernel on the device.
    size_t max = 1;
    err = clGetKernelWorkGroupInfo(
        ComputeKernel, ComputeDeviceId,
        CL_KERNEL_WORK_GROUP_SIZE, sizeof(size_t),
        &max, NULL);
    if (err != CL_SUCCESS)
    {
        printf("Error:
          Failed to retrieve kernel work group
          info! %d\n", err);
        return EXIT_FAILURE;
    }

    MaxWorkGroupSize = max;
    printf("Maximum Workgroup Size '%d'\n",
         MaxWorkGroupSize);

    return CL_SUCCESS;
}
```
7. Use the `cl_ndrange` structure to specify the data parallel range over which to execute the kernel. Dispatch the kernel block asynchronously using the `dispatch_async` function. After you dispatch the kernel, signal the dispatch semaphore to indicate that OpenGL can now access the shared resources.

```
static int recompute(void)
{
    size_t global[2];
    size_t local[2];
    cl_ndrange ndrange;

    uint uiSplitCount = ceilf(sqrtf(VertexElements));
    uint uiActive = (MaxWorkGroupSize / GroupSize);
    uiActive = uiActive < 1 ? 1 : uiActive;

    uint uiQueued = MaxWorkGroupSize / uiActive;

    local[0] = uiActive;
    local[1] = uiQueued;

    global[0] = divide_up(uiSplitCount, uiActive) * uiActive;
    global[1] = divide_up(uiSplitCount, uiQueued) * uiQueued;

    ndrange.work_dim = 2;
    ndrange.global_work_offset[0] = 0;
    ndrange.global_work_offset[1] = 0;
    ndrange.global_work_size[0] = global[0];
    ndrange.global_work_size[1] = global[1];
    ndrange.local_work_size[0] = local[0];
    ndrange.local_work_size[1] = local[1];

    dispatch_async(queue,
                   ^{
                     displace_kernel(&ndrange,
                     InputVertexBuffer,
                     OutputNormalBuffer,
                     OutputVertexBuffer,
                     ActualDimX, ActualDimY,
                     Frequency, Amplitude, Phase,
                     Lacunarity, Increment, Octaves,
                     Roughness, VertexElements);
                     dispatch_semaphore_signal(
                       cl_gl_semaphore);
                    });
    return 0;
}
```
8. Free the OpenCL memory objects, release the compute kernel, the dispatch queue, and the semaphore.

```
static void shutdown_opencl(void)
{
    gcl_free(InputVertexBuffer);
    gcl_free(OutputVertexBuffer);
    gcl_free(OutputNormalBuffer);

    clReleaseKernel(ComputeKernel);

    if(VertexBuffer)
        free(VertexBuffer);
    if(NormalBuffer)
        free(NormalBuffer);
    dispatch_release(cl_gl_semaphore);
    dispatch_release(queue);
}
```

[Next](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md)[Previous](Creating%20and%20Managing%20Buffer%20Objects%20In%20OpenCL.md)


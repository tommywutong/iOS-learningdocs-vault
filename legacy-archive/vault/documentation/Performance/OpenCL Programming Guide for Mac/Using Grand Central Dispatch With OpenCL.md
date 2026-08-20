---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/UsingGCDwOpenCL/UsingGCDwOpenCL.html
archived_at: '2026-07-18T01:49:26.611695Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenCL Programming Guide for Mac](About%20OpenCL%20for%20OS%20X.md)


[Next](Memory%20Objects%20in%20OS%20X%20OpenCL.md)[Previous](How%20the%20Kernel%20Interacts%20With%20Data%20in%20OS%20X%20OpenCL.md)

# Using Grand Central Dispatch With OpenCL

As of OS X v10.7, OpenCL developers can enqueue work coded as OpenCL kernels to Grand Central Dispatch (GCD) queues backed by OpenCL compute devices. You can use GCD with OpenCL to:

- Investigate the computational environment in which your OpenCL application is running. Specifically, you can learn which devices in the system would be best for performing particular OpenCL computations and operations:

  - You can find out about the computational power and technical characteristics of each OpenCL-capable device in the system. See [Discovering Available Compute Devices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvona).
  - GCD can suggest which OpenCL device(s) would be best for running a particular kernel.
  - You can obtain recommendations about how to configure kernels. For example, you can get the suggested optimal size of the workgroup for each kernel on any particular device. See [Notes](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/UsingGCDwOpenCL/UsingGCDwOpenCL.html#//apple_ref/doc/uid/TP40008312-CH13-SW5).
- Enqueue the kernel.
- Synchronize work between the host and OpenCL devices and synchronize work between devices.

  Your host can wait on completion of work in all queues (see [Using GCD To Synchronize A Host With OpenCL](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjyfvjvomq)) or one queue can wait on completion of another queue (see [Synchronizing Multiple Queues](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjyfvjvomy)).

OpenCL kernels assume a Single Instruction, Multiple Data (_SIMD_) parallel model of computation. In SIMD, you have a large amount of data divided into chunks, and you want the kernel to perform the same computation on each chunk.

Some SIMD algorithms perform better on CPUs; others perform better on GPUs; some work better on certain kinds of GPUs rather than on others. Tools in OS X v10.7 and later facilitate discovery of the types of devices that are available to process data.

In order to learn about the environment in which your OpenCL kernels will be running, you have to retrieve the default global _context_. The context gives you information about the set of devices, the memory accessible to those devices, and one or more queues used to schedule execution of one or more kernels.

From the context, your application can discover the types of devices in the system and can obtain recommendations as to the optimal configuration for running a kernel. Once it knows the context, your application can call on GCD to create a queue for a particular type of device or to create a queue for a specific device.

To find out about available compute devices, an application:

1. Calls the `gcl_get_context` function to get the "global" OpenCL context that OS X creates for you.
2. Calls the `clGetDeviceIds`( ... ) function (an API in the OpenCL standard API), specifying the context you just obtained as the context parameter. This call returns a list of the IDs of the attached OpenCL devices. See _The OpenCL Specification_ for details about this function.
3. You can choose to send different types of work to a device depending upon its characteristics and capabilities. Once you have the IDs of the devices in the context, call the `clGetDeviceInfo`() function for each of the devices to obtain information about the device. The sample code in [Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvomq) requests the vendor (the manufacturer) and the device name. You could also use the `clGetDeviceInfo`() function to request more technical information such as the number of compute cores, the cache line size and so on. See _The OpenCL Specification_ for information about the types of information you can obtain.

Your application must use an OpenCL-compatible dispatch queue for its OpenCL work. You can create a queue for a particular device in the system or you can create a queue for a particular type of device. You can enqueue as many kernels on each queue as you choose. You can create as many different queues as you would like:

- To create a dispatch queue to run on any device so long as it’s of a particular type, call the `gcl_create_dispatch_queue` function passing `CL_DEVICE_TYPE_CPU`, `CL_DEVICE_TYPE_GPU`, or `CL_DEVICE_TYPE_ACCELERATOR` as the first parameter.

  OS X OpenCL will create a dispatch queue that uses a GPU or CPU, depending upon the device type you specified. If more than one GPU is available, OS X OpenCL enqueues the kernel on the device of the type you specify that has the largest number of compute cores.
- If you know exactly which OpenCL device ID you want to use because you've obtained it with the `clGetDeviceIds` function and found out about it using the `clGetDeviceInfo` function, call the `cl_create_dispatch_queue` function with `CL_DEVICE_TYPE_USE_ID` and pass the ID of the device you want to use.

Both of these methods of enqueing a kernel on a dispatch queue are illustrated in [Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvomq).

Once you have created a queue, you can enqueue as many kernels onto that queue as necessary. Or, you can create additional queues with different characteristics.

For more information about GCD queues, see [Concurrency Programming Guide: Dispatch Queues](https://developer.apple.com/library/mac/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationQueues/OperationQueues.html#//apple_ref/doc/uid/TP40008091-CH102-SW28).

To obtain information specific to a kernel/device pair, such as how much private and local memory the kernel will consume on a device, or the optimal workgroup size for execution, call the `gcl_get_kernel_block_workgroup_info` function. This information is useful when you are tuning performance for a kernel running on a particular device or debugging performance issues.

You can use the suggested workgroup size returned by the `gcl_get_kernel_block_workgroup_info` function for a particular kernel on a particular device as the `cl_ndrange.local_work_size`.

[Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvomq) demonstrates how to get the global OpenCL context, and how to ask that context about the devices it contains. It also shows how to create a dispatch queue by asking for a device type (CPU or GPU), and by specifying the queue's OpenCL device directly.

[Listing 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvomy) shows how to obtain workgroup information -- useful for obtaining peak performance -- from the kernel block.

__Listing 6-1__  Creating a dispatch queue

```c

#include <stdio.h>

// Include OpenCL/opencl.h to include everything you need for OpenCL
// development on OS X v10.7 or later.
#include <OpenCL/opencl.h>

// In this example, mykernel.cl.h is the header file that contains
// the kernel block declaration.  The name of this header file would
// be different if the name of the file containing the kernel source
// were different.
// This header file is generated by Xcode.
#include "mykernel.cl.h"

static void print_device_info(cl_device_id device) {
    char name[128];
    char vendor[128];

    clGetDeviceInfo(device, CL_DEVICE_NAME, 128, name, NULL);
    clGetDeviceInfo(device, CL_DEVICE_VENDOR, 128, vendor, NULL);
    fprintf(stdout, "%s : %s\n", vendor, name);
}

// Demonstrates how to get the global OpenCL context, and how to ask that
// context about the devices it contains.  It also shows how
// to create a dispatch queue by asking for a device type (CPU or GPU) and
// by specifying the queue's OpenCL device directly.

static void hello_world_sample1 ()
{
    int i;

    // Ask for the global OpenCL context:
    // Note: If you will not be enqueing to a specific device, you do not need
    // to retrieve the context.

    cl_context context = gcl_get_context();

    // Query this context to see what kinds of devices are available.

    size_t length;
    cl_device_id devices[8];
    clGetContextInfo(
         context, CL_CONTEXT_DEVICES, sizeof(devices), devices, &length);

    // Walk over these devices, printing out some basic information.  You could
    // query any of the information available about the device here.

    fprintf(stdout, "The following devices are available for use:\n");
    int num_devices = (int)(length / sizeof(cl_device_id));
    for (i = 0; i < num_devices; i++) {
        print_device_info(devices[i]);
    }

    // To do any work, you need to create a dispatch queue associated
    // with some OpenCL device.  You can either let the system give you
    // a GPU—perhaps the only GPU—or the CPU device.  Or, you can
    // create a dispatch queue with a cl_device_id you specify.  This
    // device id comes from the OpenCL context, as above.  Below are three
    // examples.

    // 1. Ask for a GPU-based dispatch queue; notice that here we do not provide
    // a device id.  Instead, we let the system tell us the most capable GPU.

    dispatch_queue_t gpu_queue =
       gcl_create_dispatch_queue(CL_DEVICE_TYPE_GPU, NULL);

    // Get the device from the queue, so we can ask OpenCL questions about it.
    // Note that we check to make sure there WAS an OpenCL-capable GPU in the
    // system by checking against a NULL return value.

    if (gpu_queue != NULL) {

        cl_device_id gpu_device =
          gcl_get_device_id_with_dispatch_queue(gpu_queue);
        fprintf(stdout, "\nAsking for CL_DEVICE_TYPE_GPU gives us:\n");
        print_device_info(gpu_device);

    } else {
        fprintf(stdout, "\nYour system does not contain an OpenCL-compatible "
                "GPU\n.");
    }

    // 2. Try the same thing for CL_DEVICE_TYPE_CPU.  All Mac
    // systems have a CPU OpenCL device, so you don't have to
    // check for NULL, as you have to do in the case of a GPU.

    dispatch_queue_t cpu_queue =
        gcl_create_dispatch_queue(CL_DEVICE_TYPE_CPU, NULL);
    cl_device_id cpu_device = gcl_get_device_id_with_dispatch_queue(cpu_queue);
    fprintf(stdout, "\nAsking for CL_DEVICE_TYPE_CPU gives us:\n");
    print_device_info(cpu_device);

    // 3. Or perhaps you are in a situation where you want a specific device
    // from the list of devices you found on the context.
    // Notice the difference here:
    // Pass CL_DEVICE_TYPE_USE_ID and a device_id. This example just uses the
    // first device on the context from above, whatever that might be.

    dispatch_queue_t custom_queue =
        gcl_create_dispatch_queue(CL_DEVICE_TYPE_USE_ID, devices[0]);
    cl_device_id custom_device =
        gcl_get_device_id_with_dispatch_queue(custom_queue);
    fprintf(stdout,
       "\nAsking for CL_DEVICE_TYPE_USE_ID and our own device gives us:\n");
    print_device_info(custom_device);

    // Now you can use any of these 3 dispatch queues to run some kernels.
    …                                              // Run your kernels here.

    // Use the GCD API to free your queues.

    dispatch_release(custom_queue);
    dispatch_release(cpu_queue);

    if (gpu_queue != NULL) dispatch_release(gpu_queue);
}
```


__Listing 6-2__  Obtaining workgroup information

```
// This listing shows how to obtain workgroup info –
// useful for obtaining peak performance—from the kernel block.

static void hello_world_sample2() {

    // Get a queue backed by a GPU for running our squaring kernel.
    dispatch_queue_t queue =
       gcl_create_dispatch_queue(CL_DEVICE_TYPE_GPU, NULL);

    // Did we get a GPU?  If not, fall back to the CPU device.
    if (queue == NULL) {
        gcl_create_dispatch_queue(CL_DEVICE_TYPE_GPU, NULL);
    }

    // In any case, print out the device you're using:

    fprintf(stdout, "\nExamining workgroup info for square_kernel on device ");
    print_device_info(gcl_get_device_id_with_dispatch_queue(queue));

    // Now find out what OpenCL thinks is the best workgroup size for
    // executing this kernel on this particular device.  Notice that this
    // method is executed in a block, on a dispatch queue you've created
    // with OpenCL.

    dispatch_sync(queue,
                  ^{
                      size_t wgs, preferred_wgs_multiple;
                      cl_ulong local_memsize, private_memsize;

                      // The next two calls give you information about how much
                      // memory, local and private, is used by the kernel on this
                      // particular device.
                      gcl_get_kernel_block_workgroup_info(square_kernel,
                                CL_KERNEL_LOCAL_MEM_SIZE,
                                sizeof(local_memsize),
                                &local_memsize, NULL);
                      fprintf(stdout, "Local memory size: %lld\n", local_memsize);

                      gcl_get_kernel_block_workgroup_info(square_kernel,
                                CL_KERNEL_PRIVATE_MEM_SIZE,
                                sizeof(private_memsize),
                                &private_memsize, NULL);
                      fprintf(stdout,
                          "Private memory size: %lld\n", private_memsize);

                       // Ask OpenCL to suggest the optimal workgroup
                       // size for this kernel on this device.
                       gcl_get_kernel_block_workgroup_info(square_kernel,
                               CL_KERNEL_WORK_GROUP_SIZE,
                               sizeof(wgs), &wgs, NULL);
                       fprintf(stdout, "Workgroup size: %ld\n", wgs);

                       // Finally, you can ask OpenCL for a workgroup size multiple.
                       // This is a performance hint.
                       gcl_get_kernel_block_workgroup_info(square_kernel,
                               CL_KERNEL_PREFERRED_WORK_GROUP_SIZE_MULTIPLE,
                               sizeof(preferred_wgs_multiple),
                               &preferred_wgs_multiple, NULL);
                       fprintf(stdout, "Preferred workgroup size multiple: %ld\n",
                               preferred_wgs_multiple);

                      // You can now use these workgroup values to craft an
                      // appropriate cl_ndrange structure for use in launching
                      // your kernel.

                });

    dispatch_release(queue);
}


int main(int argc, const char* argv[]) {
    hello_world_sample1();
    hello_world_sample2();
}
```


In [Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvomq), the host calls the `gcl_get_kernel_block_workgroup_info` method in a block on a dispatch queue created with OpenCL to request the local memory size:

```
gcl_get_kernel_block_workgroup_info(
                             square_kernel,
                             CL_KERNEL_LOCAL_MEM_SIZE,
                             sizeof(local_memsize),
                             &local_memsize, NULL);
```

Then, in [Listing 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvomy), the `gcl_get_kernel_block_workgroup_info` function returns what it considers to be the optimal workgroup size for this kernel on this device:

```
gcl_get_kernel_block_workgroup_info(
                             square_kernel,
                             CL_KERNEL_WORK_GROUP_SIZE,
                             sizeof(workgroup_size), &workgroup_size, NULL);
                             fprintf(stdout, "Workgroup size: %ld\n",
                                     workgroup_size);
```

Finally, the host calls the `gcl_get_kernel_block_workgroup_info` function to suggest a workgroup size multiple based on the capabilities of the underlying device:

```
gcl_get_kernel_block_workgroup_info(
                             square_kernel,
                             CL_KERNEL_PREFERRED_WORK_GROUP_SIZE_MULTIPLE,
                             sizeof(preferred_workgroup_size_multiple),
                             &preferred_workgroup_size_multiple, NULL);
```

You can use the returned workgroup values to craft an appropriate `cl_ndrange structure` to use in launching your kernel.

```
cl_ndrange range = {
        1,                  // The number of dimensions to use.

        {0, 0, 0},          // The offset in each dimension.  Want to process
                                // ALL of the data, so all three offsets are 0.
                                // Always pass an offset for each of the
                                // three dimensions even though the workgroup
                                // may have fewer than three dimensions.

        {NUM_VALUES, 0, 0},  // The global range—this is how many items
                                // total in each dimension you want to
                                // process.
                                // Always pass the global range for each of the
                                // three dimensions even though the workgroup
                                // may have fewer than three dimensions.

        {workgroup_size, 0, 0 } // The local size of each workgroup.  This
                                // determines the number of work items per
                                // workgroup.  It indirectly affects the
                                // number of workgroups, since the global
                                // size / local size yields the number of
                                // workgroups.  So in this test case,
                                // have NUM_VALUE/workgroup_size workgroups.
                                // Always pass the workgroup size for each of the
                                // three dimensions even though the workgroup
                                // may have fewer than three dimensions.
};
```

[Next](Memory%20Objects%20in%20OS%20X%20OpenCL.md)[Previous](How%20the%20Kernel%20Interacts%20With%20Data%20in%20OS%20X%20OpenCL.md)


---
title: Selecting a GPU for OpenCL on the Mac Pro (Late 2013)
apple_id: DTS40014355
resource_type: Technical Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: OpenCL
published: '2014-04-18'
source_url: https://developer.apple.com/library/archive/technotes/tn2335/_index.html
archived_at: '2026-07-26T19:54:14.095560Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2335

# Selecting a GPU for OpenCL on the Mac Pro (Late 2013)

The Mac Pro (Late 2013) includes dual AMD FirePro workstation-class GPUs that are ideal for compute intensive tasks. This document describes how to query the GPUs and select one or both for use by OpenCL.

[What you should know when using OpenCL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimzvguwugsbrfvke4vcbi4yq)[Selecting a GPU when not using OpenGL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimzvguwugsbrfvke4vcbi4za)[Selecting a GPU when using CL/GL Sharing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimzvguwugsbrfvke4vcbi43a)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimzvguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## What you should know when using OpenCL

OS X has longstanding support for multiple GPUs and the following references have useful background information for setting up your application for multiple GPUs.

Technical Note TN2229: Supporting Multiple GPUs on OS X describes the use of multiple GPUs on the Mac platform.

Introduction to OpenGL Programming Guide for OS X describes many key concepts related to the graphics and display system.

WWDC 2013 Session 508: Working with OpenCL describes how to switch between two GPUs in a Mac portable using power considerations.

The Mac Pro (Late 2013) is different from other Macs as only the primary GPU provides output for the display. The secondary GPU provides additional processing capability and can perform OpenCL and off-screen OpenGL tasks without affecting the responsiveness of the user interface. Note: There may be additional latency when sharing data between the primary and secondary GPU. WWDC 2013 Session 508, mentioned above, also covers of the particulars of data sharing with OpenCL.

[Back to Top](#)

## Selecting a GPU when not using OpenGL

The following code shows how to look up an array containing cl_device_ids for all of the available GPUs in the machine. This array will contain two device on the Mac Pro (Late 2013). Both devices will have the same name and their clGetDeviceInfo queries will return the same values. An application that is not using CL/GL sharing to pass objects between OpenCL and OpenGL may create a cl_context from this device array and then perform compute tasks on either device.

__Listing 1__  Looking up the available GPUs

```
cl_uint num = 0;
clGetDeviceIDs(NULL,CL_DEVICE_TYPE_GPU,0,NULL,&num);

cl_device_id devices[num];
clGetDeviceIDs(NULL,CL_DEVICE_TYPE_GPU,num,devices,NULL);

cl_context ctx = clCreateContext(NULL,num,devices,NULL,NULL,NULL);
```

Programs that are not sharing resources between OpenCL and OpenGL may use the CGL API to distinguish the GPUs without creating a share group.

SDK Example: DeviceSelectCL shows how to identify the offline GPU that is not connected to a display, and then use the CL device corresponding to this GPU.

The following code shows how to select the non-connected GPU. Using the CGL API, iterate over all of the available renderers and query each for its kCGLRPOnline, kCGLRPAcceleratedCompute, and kCGLRPRendererID, then determine the renderer ID that is both offline and supports accelerated compute:

__Listing 2__  Selecting the non-connected GPU

```
CGLRendererInfoObj rend;
GLint nrend = 0;
GLint nonDisplayGPURendererID = 0x0;
CGLQueryRendererInfo(0xffffffff, &rend, &nrend);
for(GLint idx=0; idx<nrend; idx++) {
    GLint online = 1;
    CGLDescribeRenderer(rend, idx, kCGLRPOnline, &online);
    if(!online) {
        GLint accelerated = 0;
        CGLDescribeRenderer(rend, idx, kCGLRPAcceleratedCompute, &accelerated);
        if(accelerated) {
                CGLDescribeRenderer(rend, idx, kCGLRPRendererID,
                                                        &nonDisplayGPURendererID);
                break;
            }
        }
    }
CGLDestroyRendererInfo(rend);
```

For GPUs that support OpenCL in Mac OS X, the rendererID may be transformed into a cl_device_id by masking away the low byte:

__Listing 3__  Converting a renderer ID to a cl_device_id

```
cl_device_id nonDisplayCLDeviceId = (cl_device_id)(intptr_t)(nonDisplayGPURendererID&~0xff);
```

This variable may be used to create a CL context, or to create a command queue in an existing context that contains the device.

[Back to Top](#)

## Selecting a GPU when using CL/GL Sharing

Applications that share resources between OpenCL and OpenGL by creating a CL context from CGLSharegroup may use an OpenCL extension to determine which device is connected to the display. These applications may also use the CGL API mechanism described in the previous section.

SDK Example: DeviceSelectCLGL shows how to identify the offline GPU that is not connected to a display.

The application will create a CL context from a CGL sharegroup, using the following code:

__Listing 4__  Creating a CGL sharegroup and a CL context

```
CGLShareGroupObj sharegroup = CGLGetShareGroup(self.view.openGLContext.CGLContextObj);

cl_context_properties props[] = {
  CL_CONTEXT_PROPERTY_USE_CGL_SHAREGROUP_APPLE,
  (cl_context_properties)sharegroup,
  0
};

cl_int err;
ctx = clCreateContext(props, 0, NULL, NULL, NULL, &err);
```

The CGL sharegroup must include offline renderers. In an NSOpenGLView based application, this selection is performed within InterfaceBuilder. In other applications, call CGLChoosePixelFormat with an attribute list including the kCGLPFAAllowOfflineRenderers attribute.

The CL context will contain all of the GPU devices in the sharegroup that support OpenCL. If you want to include the OpenCL CPU device in the context, pass it to clCreateContext in an array with the third argument.

You can use the clGetGLContextInfoAPPLE function to query the cl_device_id corresponding to the current virtual screen and then compare this value to the other devices in the context to distinguish display connected GPU.

__Listing 5__  Querying for the connected GPU with the app's current virtual screen

```
cl_device_id displayDevice;
clGetGLContextInfoAPPLE(ctx,self.view.openGLContext.CGLContextObj,
    CL_CGL_DEVICE_FOR_CURRENT_VIRTUAL_SCREEN_APPLE, sizeof(displayDevice), &displayDevice, NULL);
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-04-18 | New document that describes how to select a GPU in CL-only or CL/GL apps on the Mac Pro (Late 2013) |


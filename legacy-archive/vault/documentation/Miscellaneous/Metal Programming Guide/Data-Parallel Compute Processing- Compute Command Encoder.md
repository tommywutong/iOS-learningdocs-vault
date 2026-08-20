---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Compute-Ctx/Compute-Ctx.html
archived_at: '2026-07-15T08:16:49.687973Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Buffer%20and%20Texture%20Operations-%20Blit%20Command%20Encoder.md)[Previous](Graphics%20Rendering-%20Render%20Command%20Encoder.md)

# Data-Parallel Compute Processing: Compute Command Encoder

This chapter explains how to create and use a [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) object to encode data-parallel compute processing state and commands and submit them for execution on a device.

To perform a data-parallel computation, follow these main steps:

1. Use a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) method to create a compute state ([MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate)) that contains compiled code from a [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object, as discussed in [Creating a Compute State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltg). The `MTLFunction` object represents a compute function written with the Metal shading language, as described in [Functions and Libraries](Functions%20and%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnjnknltc).
2. Specify the [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) object to be used by the compute command encoder, as discussed in [Specifying a Compute State and Resources for a Compute Command Encoder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltgma).
3. Specify resources and related objects ([MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer), [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture), and possibly [MTLSamplerState](https://developer.apple.com/documentation/metal/mtlsamplerstate)) that may contain the data to be processed and returned by the compute state, as discussed in [Specifying a Compute State and Resources for a Compute Command Encoder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltgma). Also set their argument table indices, so that Metal framework code can locate a corresponding resource in the shader code. At any given moment, the [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) can be associated to a number of resource objects.
4. Dispatch the compute function a specified number of times, as explained in [Executing a Compute Command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknlte).

A [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object represents data-parallel code that can be executed by a [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) object. The [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) object encodes commands that set arguments and execute the compute function. Because creating a compute pipeline state can require an expensive compilation of Metal shading language code, you can use either a blocking or an asynchronous method to schedule such work in a way that best fits the design of your app.

- To synchronously create the compute pipeline state object, call either the [newComputePipelineStateWithFunction:error:](https://developer.apple.com/documentation/metal/mtldevice/1433395-newcomputepipelinestatewithfunct) or [newComputePipelineStateWithFunction:options:reflection:error:](https://developer.apple.com/documentation/metal/mtldevice/1433419-makecomputepipelinestate) method of [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice). These methods block the current thread while Metal compiles shader code to create the pipeline state object.
- To asynchronously create the compute pipeline state object, call either the [newComputePipelineStateWithFunction:completionHandler:](https://developer.apple.com/documentation/metal/mtldevice/1433427-makecomputepipelinestate) or [newComputePipelineStateWithFunction:options:completionHandler:](https://developer.apple.com/documentation/metal/mtldevice/1433410-makecomputepipelinestate) method of [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice). These methods return immediately—Metal asynchronously compiles shader code to create the pipeline state object, then calls your completion handler to provide the new [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) object.

When you create a [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) object you can also choose to create reflection data that reveals details of the compute function and its arguments. The [newComputePipelineStateWithFunction:options:reflection:error:](https://developer.apple.com/documentation/metal/mtldevice/1433419-makecomputepipelinestate) and [newComputePipelineStateWithFunction:options:completionHandler:](https://developer.apple.com/documentation/metal/mtldevice/1433410-makecomputepipelinestate) methods provide this data. Avoid obtaining reflection data if it will not be used. For more information on how to analyze reflection data, see [Determining Function Details at Runtime](Functions%20and%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnjnknltm).

The [setComputePipelineState:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443140-setcomputepipelinestate) method of a [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) object specifies the state, including a compiled compute shader function, to use for a data-parallel compute pass. At any given moment, a compute command encoder can be associated to only one compute function.

The following [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) methods specify a resource (that is, a buffer, texture, sampler state, or threadgroup memory) that is used as an argument to the compute function represented by the [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) object.

- [setBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443126-setbuffer)
- [setBuffers:offsets:withRange:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443134-setbuffers)
- [setTexture:atIndex:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443130-settexture)
- [setTextures:withRange:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443148-settextures)
- [setSamplerState:atIndex:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443144-setsamplerstate)
- [setSamplerState:lodMinClamp:lodMaxClamp:atIndex:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443153-setsamplerstate)
- [setSamplerStates:withRange:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443155-setsamplerstates)
- [setSamplerStates:lodMinClamps:lodMaxClamps:withRange:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443128-setsamplerstates)
- [setThreadgroupMemoryLength:atIndex:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443142-setthreadgroupmemorylength)

Each method assigns one or more resources to the corresponding argument(s), as illustrated in Figure 6-1.

__Figure 6-1__  Argument Tables for the Compute Command Encoder

!

The limits for the maximum number of entries in a buffer, texture, or sampler state argument table are listed in the [Implementation Limits](https://developer.apple.com/metal/limits/) table.

The limits for the maximum total threadgroup memory allocation is also listed in the [Implementation Limits](https://developer.apple.com/metal/limits/) table.

To encode a command to execute a compute function, call the [dispatchThreadgroups:threadsPerThreadgroup:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443138-dispatchthreadgroups) method of [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) and specify the threadgroup dimensions and the number of threadgroups. You can query the [threadExecutionWidth](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/1414911-threadexecutionwidth) and [maxTotalThreadsPerThreadgroup](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/1414927-maxtotalthreadsperthreadgroup) properties of [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) to optimize the execution of the compute function on this device.

The total number of threads in a threadgroup is the product of the components of `threadsPerThreadgroup`: `threadsPerThreadgroup.width * threadsPerThreadgroup.height * threadsPerThreadgroup.depth`. The [maxTotalThreadsPerThreadgroup](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/1414927-maxtotalthreadsperthreadgroup) property specifies the maximum number of threads that can be in a single threadgroup to execute this compute function on the device.

Compute commands are executed in the order in which they are encoded into the command buffer. A compute command finishes execution when all threadgroups associated with the command finish execution and all results are written to memory. Because of this sequencing, the results of a compute command are available to any commands encoded after it in the command buffer.

To end encoding commands for a compute command encoder, call the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method of [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder). After ending the previous command encoder, you can create a new command encoder of any type to encode additional commands into the command buffer.

[Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltm) shows an example that creates and uses a [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) object to perform the parallel computations of an image transformation on specified data. (This example does not show how the device, library, command queue, and resource objects are created and initialized.) The example creates a command buffer and then uses it to create the [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) object. Next a [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object is created that represents the entry point `filter_main` loaded from the [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) object, shown in [Listing 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltk). Then the function object is used to create a [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) object called `filterState`.

The compute function performs an image transformation and filtering operation on the image `inputImage` with the results returned in `outputImage`. First the [setTexture:atIndex:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443130-settexture) and [setBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443126-setbuffer) methods assign texture and buffer objects to indices in the specified argument tables. `paramsBuffer` specifies values used to perform the image transformation, and `inputTableData` specifies filter weights. The compute function is executed as a 2D threadgroup of size 16 x 16 pixels in each dimension. The [dispatchThreadgroups:threadsPerThreadgroup:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443138-dispatchthreadgroups) method enqueues the command to dispatch the threads executing the compute function, and the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method terminates the [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder). Finally, the [commit](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443003-commit) method of [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) causes the commands to be executed as soon as possible.

__Listing 6-1__  Specifying and Running a Function in a Compute State

```
id <MTLDevice> device;
id <MTLLibrary> library;
id <MTLCommandQueue> commandQueue;

id <MTLTexture> inputImage;
id <MTLTexture> outputImage;
id <MTLTexture> inputTableData;
id <MTLBuffer> paramsBuffer;

// ... Create and initialize device, library, queue, resources

// Obtain a new command buffer
id <MTLCommandBuffer> commandBuffer = [commandQueue commandBuffer];

// Create a compute command encoder
id <MTLComputeCommandEncoder> computeCE = [commandBuffer computeCommandEncoder];

NSError *errors;
id <MTLFunction> func = [library newFunctionWithName:@"filter_main"];
id <MTLComputePipelineState> filterState
              = [device newComputePipelineStateWithFunction:func error:&errors];
[computeCE setComputePipelineState:filterState];
[computeCE setTexture:inputImage atIndex:0];
[computeCE setTexture:outputImage atIndex:1];
[computeCE setTexture:inputTableData atIndex:2];
[computeCE setBuffer:paramsBuffer offset:0 atIndex:0];

MTLSize threadsPerGroup = {16, 16, 1};
MTLSize numThreadgroups = {inputImage.width/threadsPerGroup.width,
                           inputImage.height/threadsPerGroup.height, 1};

[computeCE dispatchThreadgroups:numThreadgroups
                                threadsPerThreadgroup:threadsPerGroup];
[computeCE endEncoding];

// Commit the command buffer
[commandBuffer commit];
```

Listing 6-2 shows the corresponding shader code for the preceding example. (The functions `read_and_transform` and `filter_table` are placeholders for user-defined code).

__Listing 6-2__  Shading Language Compute Function Declaration

```swift
kernel void filter_main(   texture2d<float,access::read>   inputImage   [[ texture(0) ]],   texture2d<float,access::write>  outputImage  [[ texture(1) ]],   uint2 gid                                    [[ thread_position_in_grid ]],   texture2d<float,access::sample> table        [[ texture(2) ]],   constant Parameters* params                  [[ buffer(0) ]]   ) {   float2 p0          = static_cast<float2>(gid);   float3x3 transform = params->transform;   float4   dims      = params->dims;      float4 v0 = read_and_transform(inputImage, p0, transform);   float4 v1 = filter_table(v0,table, dims);      outputImage.write(v1,gid); }
```

[Next](Buffer%20and%20Texture%20Operations-%20Blit%20Command%20Encoder.md)[Previous](Graphics%20Rendering-%20Render%20Command%20Encoder.md)


---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Cmd-Submiss/Cmd-Submiss.html
archived_at: '2026-07-15T08:16:48.613767Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Resource%20Objects-%20Buffers%20and%20Textures.md)[Previous](Fundamental%20Metal%20Concepts.md)

# Command Organization and Execution Model

In the Metal architecture, the [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) protocol defines the interface that represents a single GPU. The `MTLDevice` protocol supports methods for interrogating device properties, for creating other device-specific objects such as buffers and textures, and for encoding and queueing render and compute commands to be submitted to the GPU for execution.

A _command queue_ consists of a queue of _command buffers_, and a command queue organizes the order of execution of those command buffers. A command buffer contains encoded commands that are intended for execution on a particular device. A _command encoder_ appends rendering, computing, and blitting commands onto a command buffer, and those command buffers are eventually committed for execution on the device.

The [MTLCommandQueue](https://developer.apple.com/documentation/metal/mtlcommandqueue) protocol defines an interface for command queues, primarily supporting methods for creating command buffer objects. The [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) protocol defines an interface for command buffers and provides methods for creating command encoders, enqueueing command buffers for execution, checking status, and other operations. The `MTLCommandBuffer` protocol supports the following command encoder types, which are interfaces for encoding different kinds of GPU workloads into a command buffer:

- The [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) protocol encodes graphics (3D) rendering commands for a single rendering pass.
- The [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) protocol encodes data-parallel computation workloads.
- The [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) protocol encodes simple copy operations between buffers and textures, as well as utility operations like mipmap generation.

At any point in time, only a single command encoder can be active and append commands into a command buffer. Each command encoder must be ended before another command encoder can be created for use with the same command buffer. The one exception to the “one active command encoder for each command buffer” rule is the [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder) protocol, discussed in [Encoding a Single Rendering Pass Using Multiple Threads](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltcnq).

Once all encoding is completed, you commit the `MTLCommandBuffer` object itself, which marks the command buffer as ready for execution by the GPU. The `MTLCommandQueue` protocol controls when the commands in the committed `MTLCommandBuffer` object are executed, relative to other `MTLCommandBuffer` objects that are already in the command queue.

Figure 2-1 shows how the command queue, command buffer, and command encoder objects are closely related. Each column of components at the top of the diagram (buffer, texture, sampler, depth and stencil state, pipeline state) represent resources and state that are specific to a particular command encoder.

__Figure 2-1__  Metal Object Relationships

!

A [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object represents a GPU that can execute commands. The `MTLDevice` protocol has methods to create new command queues, to allocate buffers from memory, to create textures, and to make queries about the device’s capabilities. To obtain the preferred system device on the system, call the [MTLCreateSystemDefaultDevice](https://developer.apple.com/documentation/metal/1433401-mtlcreatesystemdefaultdevice) function.

Some objects in Metal are designed to be transient and extremely lightweight, while others are more expensive and can last for a long time, perhaps for the lifetime of the app.

Command buffer and command encoder objects are transient and designed for a single use. They are very inexpensive to allocate and deallocate, so their creation methods return autoreleased objects.

The following objects are not transient. Reuse these objects in performance sensitive code, and avoid creating them repeatedly.

- Command queues
- Data buffers
- Textures
- Sampler states
- Libraries
- Compute states
- Render pipeline states
- Depth/stencil states

A command queue accepts an ordered list of command buffers that the GPU will execute. All command buffers sent to a single queue are guaranteed to execute in the order in which the command buffers were enqueued. In general, command queues are thread-safe and allow multiple active command buffers to be encoded simultaneously.

To create a command queue, call either the [newCommandQueue](https://developer.apple.com/documentation/metal/mtldevice/1433388-newcommandqueue) method or the [newCommandQueueWithMaxCommandBufferCount:](https://developer.apple.com/documentation/metal/mtldevice/1433433-makecommandqueue) method of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object. In general, command queues are expected to be long-lived, so they should not be repeatedly created and destroyed.

A command buffer stores encoded commands until the buffer is committed for execution by the GPU. A single command buffer can contain many different kinds of encoded commands, depending on the number and type of encoders that are used to build it. In a typical app, an entire frame of rendering is encoded into a single command buffer, even if rendering that frame involves multiple rendering passes, compute processing functions, or blit operations.

Command buffers are transient single-use objects and do not support reuse. Once a command buffer has been committed for execution, the only valid operations are to wait for the command buffer to be scheduled or completed—through synchronous calls or handler blocks discussed in [Registering Handler Blocks for Command Buffer Execution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmznknltema)—and to check the status of the command buffer execution.

Command buffers also represent the only independently trackable unit of work by the app, and they define the coherency boundaries established by the Metal memory model, as detailed in [Resource Objects: Buffers and Textures](Resource%20Objects-%20Buffers%20and%20Textures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltc).

To create a [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object, call the `commandBuffer` method of [MTLCommandQueue](https://developer.apple.com/documentation/metal/mtlcommandqueue). A `MTLCommandBuffer` object can only be committed into the `MTLCommandQueue` object that created it.

Command buffers created by the `commandBuffer` method retain data that is needed for execution. For certain scenarios, where you hold a retain to these objects elsewhere for the duration of the execution of a `MTLCommandBuffer` object, you can instead create a command buffer by calling the `commandBufferWithUnretainedReferences` method of `MTLCommandQueue`. Use the `commandBufferWithUnretainedReferences` method only for extremely performance-critical apps that can guarantee that crucial objects have references elsewhere in the app until command buffer execution is completed. Otherwise, an object that no longer has other references may be prematurely released, and the results of the command buffer execution are undefined.

The `MTLCommandBuffer` protocol uses the following methods to establish the execution order of command buffers in the command queue. A command buffer does not begin execution until it is committed. Once committed, command buffers are executed in the order in which they were enqueued.

- The [enqueue](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443019-enqueue) method reserves a place for the command buffer on the command queue, but does not commit the command buffer for execution. When this command buffer is eventually committed, it is executed after any previously enqueued command buffers within the associated command queue.
- The [commit](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443003-commit) method causes the command buffer to be executed as soon as possible, but after any previously enqueued command buffers in the same command queue are committed. If the command buffer has not previously been enqueued, `commit` makes an implied `enqueue` call.

For an example of using `enqueue` with multiple threads, see [Multiple Threads, Command Buffers, and Command Encoders](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmznknltm).

The [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) methods listed below monitor command execution. Scheduled and completed handlers are invoked in execution order on an undefined thread. Any code you execute in these handlers should complete quickly; if expensive or blocking work needs to be done, defer that work to another thread.

- The [addScheduledHandler:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442991-addscheduledhandler) method registers a block of code to be called when the command buffer is scheduled. A command buffer is considered _scheduled_ when any dependencies between work submitted by other `MTLCommandBuffer` objects or other APIs in the system is satisfied. You can register multiple scheduled handlers for a command buffer.
- The [waitUntilScheduled](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443036-waituntilscheduled) method synchronously waits and returns after the command buffer is scheduled and all handlers registered by the `addScheduledHandler:` method are completed.
- The [addCompletedHandler:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442997-addcompletedhandler) method registers a block of code to be called immediately after the device completes the execution of the command buffer. You can register multiple completed handlers for a command buffer.
- The [waitUntilCompleted](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443039-waituntilcompleted) method synchronously waits and returns after the device has completed the execution of the command buffer and all handlers registered by the [addCompletedHandler:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442997-addcompletedhandler) method have returned.

The [presentDrawable:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443029-present) method is a special case of completed handler. This convenience method presents the contents of a displayable resource (a [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable) object) when the command buffer is scheduled. For details about the `presentDrawable:` method, see [Integration with Core Animation: CAMetalLayer](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgnq).

The read-only [status](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443048-status) property contains a `MTLCommandBufferStatus` enum value listed in [Command Buffer Status Codes](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus) that reflects the current scheduling stage in the lifetime of this command buffer.

If execution finishes successfully, the value of the read-only [error](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443040-error) property is `nil`. If execution fails, then `status` is set to `MTLCommandBufferStatusError`, and the `error` property may contain a value listed in [Command Buffer Error Codes](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/code) that indicates the cause of the failure.

A command encoder is a transient object that you use once to write commands and state into a single command buffer in a format that the GPU can execute. Many command encoder object methods append commands onto the command buffer. While a command encoder is active, it has the exclusive right to append commands for its command buffer. Once you finish encoding commands, call the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method. To write further commands, create a new command encoder.

Because a command encoder appends commands into a specific command buffer, you create a command encoder by requesting one from the [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object you want to use it with. Use the following `MTLCommandBuffer` methods to create command encoders of each type:

- The [renderCommandEncoderWithDescriptor:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442999-rendercommandencoderwithdescript) method creates a [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) object for graphics rendering to an attachment in a [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor).
- The [computeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443044-computecommandencoder) method creates a [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) object for data-parallel computations.
- The [blitCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443001-blitcommandencoder) method creates a [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) object for memory operations.
- The [parallelRenderCommandEncoderWithDescriptor:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443009-parallelrendercommandencoderwith) method creates a [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder) object that enables several `MTLRenderCommandEncoder` objects to run on different threads while still rendering to an attachment that is specified in a shared [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor).

Graphics rendering can be described in terms of a _rendering pass_. A [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) object represents the rendering state and drawing commands associated with a single rendering pass. A `MTLRenderCommandEncoder` requires an associated [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) (described in [Creating a Render Pass Descriptor](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltk)) that includes the color, depth, and stencil attachments that serve as destinations for rendering commands. The `MTLRenderCommandEncoder` has methods to:

- Specify graphics resources, such as buffer and texture objects, that contain vertex, fragment, or texture image data
- Specify a [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object that contains compiled rendering state, including vertex and fragment shaders
- Specify fixed-function state, including viewport, triangle fill mode, scissor rectangle, depth and stencil tests, and other values
- Draw 3D primitives

For detailed information about the `MTLRenderCommandEncoder` protocol, see [Graphics Rendering: Render Command Encoder](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltc).

For data-parallel computing, the [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) protocol provides methods to encode commands in the command buffer that can specify the compute function and its arguments (for example, texture, buffer, and sampler state) and dispatch the compute function for execution. To create a compute command encoder object, use the [computeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443044-computecommandencoder) method of [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer). For detailed information about the `MTLComputeCommandEncoder` methods and properties, see [Data-Parallel Compute Processing: Compute Command Encoder](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltc).

The [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) protocol has methods that append commands for memory copy operations between buffers ([MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer)) and textures ([MTLTexture](https://developer.apple.com/documentation/metal/mtltexture)). The `MTLBlitCommandEncoder` protocol also provides methods to fill textures with a solid color and to generate mipmaps. To create a blit command encoder object, use the [blitCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443001-blitcommandencoder) method of `MTLCommandBuffer`. For detailed information about the `MTLBlitCommandEncoder` methods and properties, see [Buffer and Texture Operations: Blit Command Encoder](Buffer%20and%20Texture%20Operations-%20Blit%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqojnknltg).

Most apps use a single thread to encode the rendering commands for a single frame in a single command buffer. At the end of each frame, you commit the command buffer, which both schedules and begins command execution.

If you want to parallelize command buffer encoding, then you can create multiple command buffers at the same time, and encode to each one with a separate thread. If you know ahead of time in what order a command buffer should execute, then the [enqueue](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443019-enqueue) method of [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) can declare the execution order within the command queue without needing to wait for the commands to be encoded and committed. Otherwise, when a command buffer is committed, it is assigned a place in the command queue after any previously enqueued command buffers.

Only one CPU thread can access a command buffer at time. Multithreaded apps can use one thread per command buffer to create multiple command buffers in parallel.

Figure 2-2 shows an example with three threads. Each thread has its own command buffer. For each thread, one command encoder at a time has access to its associated command buffer. Figure 2-2 also shows each command buffer receiving commands from different command encoders. When you finish encoding, call the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method of the command encoder, and a new command encoder object can then begin encoding commands to the command buffer.

__Figure 2-2__  Metal Command Buffers with Multiple Threads

!

A [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder) object allows a single rendering pass to be broken up across multiple command encoders and assigned to separate threads. For more information about [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder), see [Encoding a Single Rendering Pass Using Multiple Threads](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltcnq).

[Next](Resource%20Objects-%20Buffers%20and%20Textures.md)[Previous](Fundamental%20Metal%20Concepts.md)


---
title: Metal Best Practices Guide
apple_id: TP40016642
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/BufferBindings.html
archived_at: '2026-07-15T03:48:43.193593Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Best Practices Guide](index.md)



## Buffer Bindings

__Best Practice:__ Use an appropriate method to bind your buffer data to a graphics or compute function.

Metal provides several API options for binding buffer data to a graphics or compute function so it can be processed by the GPU.

> [!NOTE]
> 

The [setVertexBytes:length:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515846-setvertexbytes) method is the best option for binding a very small amount (less than 4 KB) of dynamic buffer data to a vertex function, as shown in Listing 5-1. This method avoids the overhead of creating an intermediary [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) object. Instead, Metal manages a transient buffer for you.

__Listing 5-1__Binding a very small amount (less than 4 KB) of dynamic buffer data

1. `float _verySmallData = 1.0;`
2. `[renderEncoder setVertexBytes:&_verySmallData length:sizeof(float) atIndex:0];`

If your data size is larger than 4 KB, create a [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) object once and update its contents as needed. Call the [setVertexBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515829-setvertexbuffer) method to bind the buffer to a vertex function; if your buffer contains data used in multiple draw calls, call the [setVertexBufferOffset:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515433-setvertexbufferoffset) method afterward to update the buffer offset so it points to the location of the corresponding draw call data, as shown in Listing 5-2. You do not need to rebind the currently bound buffer if you are only updating its offset.

__Listing 5-2__Updating the offset of a bound buffer

1. `// Bind the vertex buffer once`
2. `[renderEncoder setVertexBuffer:_vertexBuffer[_frameIndex] offset:0 atIndex:0];`
3. `for(int i=0; i<_drawCalls; i++)`
4. `{`
5. `// Update the vertex buffer offset for each draw call`
6. `[renderEncoder setVertexBufferOffset:i*_sizeOfVertices atIndex:0];`
8. `// Draw the vertices`
9. `[renderEncoder drawPrimitives:MTLPrimitiveTypeTriangle vertexStart:0 vertexCount:_vertexCount];`
10. `}`

[Triple Buffering](TripleBuffering.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqnjnknltc)

[Drawables](Drawables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrnknltc)

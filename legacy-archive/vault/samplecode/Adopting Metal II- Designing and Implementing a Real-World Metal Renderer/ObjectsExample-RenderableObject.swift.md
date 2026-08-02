---
title: 'Adopting Metal II: Designing and Implementing a Real-World Metal Renderer'
apple_id: TP40017288
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdoptingMetalII/Listings/ObjectsExample_RenderableObject_swift.html
archived_at: '2026-07-18T03:00:48.342031Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Adopting Metal II: Designing and Implementing a Real-World Metal Renderer](Adopting%20Metal%20II-%20Designing%20and%20Implementing%20a%20Real-World%20Metal%20Renderer.md)


[Next](ObjectsExample-Shading.metal.md)[Previous](ObjectsExample-MetalView.swift.md)

# ObjectsExample/RenderableObject.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Definition of the `RenderableObject` class.
 */

import Foundation
import Metal

class RenderableObject
{
    let mesh : MTLBuffer?
    let indexBuffer : MTLBuffer?
    let texture : MTLTexture?

    var count : Int

    var scale : vector_float3 = float3(1.0)
    var position : vector_float4
    var rotation : vector_float3
    var rotationRate : vector_float3

    var objectData : ObjectData

    init()
    {
        self.mesh = nil
        self.indexBuffer = nil
        self.texture = nil
        self.count = 0
        self.objectData = ObjectData()
        self.objectData.LocalToWorld = matrix_identity_float4x4
        self.position = vector_float4(0.0, 0.0, 0.0, 1.0)
        self.rotation = float3(0.0, 0.0, 0.0)
        self.rotationRate = float3(0.0, 0.0, 0.0)
    }

    init(m : MTLBuffer, idx : MTLBuffer?, count : Int, tex : MTLTexture?)
    {
        self.mesh = m
        self.indexBuffer = idx
        self.texture = tex
        self.count = count
        self.objectData = ObjectData()
        self.objectData.LocalToWorld = matrix_identity_float4x4
        self.objectData.color = float4(0.0, 0.0, 0.0, 0.0)
        self.objectData.pad1 = matrix_identity_float4x4
        self.objectData.pad2 = matrix_identity_float4x4

        self.position = vector_float4(0.0, 0.0, 0.0, 1.0)
        self.rotation = float3(0.0, 0.0, 0.0)
        self.rotationRate = float3(0.0, 0.0, 0.0)
    }

    func SetRotationRate(_ rot : vector_float3)
    {
        rotationRate = rot
    }

    func UpdateData(_ dest : UnsafeMutablePointer<ObjectData>, deltaTime : Float) -> UnsafeMutablePointer<ObjectData>
    {
        rotation += rotationRate * deltaTime

        objectData.LocalToWorld = getScaleMatrix(scale.x, y: scale.y, z: scale.z)

        objectData.LocalToWorld = matrix_multiply(getRotationAroundX(rotation.x), objectData.LocalToWorld)
        objectData.LocalToWorld = matrix_multiply(getRotationAroundY(rotation.y), objectData.LocalToWorld)
        objectData.LocalToWorld = matrix_multiply(getRotationAroundZ(rotation.z), objectData.LocalToWorld)
        objectData.LocalToWorld = matrix_multiply(getTranslationMatrix(position), objectData.LocalToWorld)

        dest.pointee = objectData
        return dest.advanced(by: 1)
    }

    func DrawZPass(_ enc :MTLRenderCommandEncoder, offset : Int)
    {
        enc.setVertexBufferOffset(offset, at: 1)

        if(indexBuffer != nil)
        {
            enc.drawIndexedPrimitives(type: MTLPrimitiveType.triangle, indexCount: count, indexType: MTLIndexType.uint16, indexBuffer: indexBuffer!, indexBufferOffset: 0)
        }
        else
        {
            enc.drawPrimitives(type: MTLPrimitiveType.triangle, vertexStart: 0, vertexCount: count)
        }
    }

    func Draw(_ enc : MTLRenderCommandEncoder, offset : Int)
    {
        enc.setVertexBufferOffset(offset, at: 1)
        enc.setFragmentBufferOffset(offset, at: 1)

        if(indexBuffer != nil)
        {
            enc.drawIndexedPrimitives(type: MTLPrimitiveType.triangle, indexCount: count, indexType: MTLIndexType.uint16, indexBuffer: indexBuffer!, indexBufferOffset: 0)
        }
        else
        {
            enc.drawPrimitives(type: MTLPrimitiveType.triangle, vertexStart: 0, vertexCount: count)
        }

    }
}

class StaticRenderableObject : RenderableObject
{
    override func UpdateData(_ dest: UnsafeMutablePointer<ObjectData>, deltaTime: Float) -> UnsafeMutablePointer<ObjectData>
    {
        return dest
    }

    override func Draw(_ enc: MTLRenderCommandEncoder, offset: Int)
    {
        enc.setVertexBuffer(mesh, offset: 0, at: 0)
        enc.setVertexBytes(&objectData, length: MemoryLayout<ObjectData>.size, at: 1)
        enc.setFragmentBytes(&objectData, length: MemoryLayout<ObjectData>.size, at: 1)

        enc.drawPrimitives(type: .triangle, vertexStart: 0, vertexCount: count)
    }
}
```

[Next](ObjectsExample-Shading.metal.md)[Previous](ObjectsExample-MetalView.swift.md)


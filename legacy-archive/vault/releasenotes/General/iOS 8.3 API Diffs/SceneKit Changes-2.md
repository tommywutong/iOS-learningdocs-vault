---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/SceneKit.html
archived_at: '2026-07-18T02:56:27.495238Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# SceneKit Changes

## SceneKit

Removed SCNWrapMode.ClampToBorderRemoved SCNSceneSourceConvertToYUpKeyRemoved SCNSceneSourceConvertUnitsToMetersKeyAdded SCNMatrix4.init()Added SCNMatrix4.init(m11: Float, m12: Float, m13: Float, m14: Float, m21: Float, m22: Float, m23: Float, m24: Float, m31: Float, m32: Float, m33: Float, m34: Float, m41: Float, m42: Float, m43: Float, m44: Float)Added SCNVector3.init()Added SCNVector3.init(x: Float, y: Float, z: Float)Added SCNVector4.init()Added SCNVector4.init(x: Float, y: Float, z: Float, w: Float)Added SCNMatrix4FromGLKMatrix4(GLKMatrix4) -> SCNMatrix4Added SCNMatrix4ToGLKMatrix4(SCNMatrix4) -> GLKMatrix4Added SCNVector3FromGLKVector3(GLKVector3) -> SCNVector3Added SCNVector3ToGLKVector3(SCNVector3) -> GLKVector3Added SCNVector4FromGLKVector4(GLKVector4) -> SCNVector4Added SCNVector4ToGLKVector4(SCNVector4) -> GLKVector4Modified CAAnimation.animationEvents

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified CAAnimation.fadeInDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified CAAnimation.fadeOutDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified NSValue.init(SCNMatrix4: SCNMatrix4)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified NSValue.SCNMatrix4Value

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified SCNIKConstraint.inverseKinematicsConstraintWithChainRootNode(SCNNode) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func inverseKinematicsConstraintWithChainRootNode(_ chainRootNode: SCNNode) -> Self! ``` | iOS 8.0 |
| To | ``` class func inverseKinematicsConstraintWithChainRootNode(_ chainRootNode: SCNNode) -> Self ``` | iOS 8.3 |

Modified SCNMatrix4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNMatrix4 {     var m11: Float     var m12: Float     var m13: Float     var m14: Float     var m21: Float     var m22: Float     var m23: Float     var m24: Float     var m31: Float     var m32: Float     var m33: Float     var m34: Float     var m41: Float     var m42: Float     var m43: Float     var m44: Float } ``` |
| To | ``` struct SCNMatrix4 {     var m11: Float     var m12: Float     var m13: Float     var m14: Float     var m21: Float     var m22: Float     var m23: Float     var m24: Float     var m31: Float     var m32: Float     var m33: Float     var m34: Float     var m41: Float     var m42: Float     var m43: Float     var m44: Float     init()     init(m11 m11: Float, m12 m12: Float, m13 m13: Float, m14 m14: Float, m21 m21: Float, m22 m22: Float, m23 m23: Float, m24 m24: Float, m31 m31: Float, m32 m32: Float, m33 m33: Float, m34 m34: Float, m41 m41: Float, m42 m42: Float, m43 m43: Float, m44 m44: Float) } ``` |

Modified SCNPhysicsBody.dynamicBody() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func dynamicBody() -> Self! ``` | iOS 8.0 |
| To | ``` class func dynamicBody() -> Self ``` | iOS 8.3 |

Modified SCNPhysicsBody.kinematicBody() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func kinematicBody() -> Self! ``` | iOS 8.0 |
| To | ``` class func kinematicBody() -> Self ``` | iOS 8.3 |

Modified SCNPhysicsBody.staticBody() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func staticBody() -> Self! ``` | iOS 8.0 |
| To | ``` class func staticBody() -> Self ``` | iOS 8.3 |

Modified SCNSceneRenderer.overlaySKScene

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified SCNVector3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNVector3 {     var x: Float     var y: Float     var z: Float } ``` |
| To | ``` struct SCNVector3 {     var x: Float     var y: Float     var z: Float     init()     init(x x: Float, y y: Float, z z: Float) } ``` |

Modified SCNVector4 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNVector4 {     var x: Float     var y: Float     var z: Float     var w: Float } ``` |
| To | ``` struct SCNVector4 {     var x: Float     var y: Float     var z: Float     var w: Float     init()     init(x x: Float, y y: Float, z z: Float, w w: Float) } ``` |

Modified SCNConsistencyElementIDErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNConsistencyElementIDErrorKey: NSString! ``` |
| To | ``` let SCNConsistencyElementIDErrorKey: String ``` |

Modified SCNConsistencyElementTypeErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNConsistencyElementTypeErrorKey: NSString! ``` |
| To | ``` let SCNConsistencyElementTypeErrorKey: String ``` |

Modified SCNConsistencyLineNumberErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNConsistencyLineNumberErrorKey: NSString! ``` |
| To | ``` let SCNConsistencyLineNumberErrorKey: String ``` |

Modified SCNDetailedErrorsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNDetailedErrorsKey: NSString! ``` |
| To | ``` let SCNDetailedErrorsKey: String ``` |

Modified SCNErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let SCNErrorDomain: NSString! ``` |
| To | ``` let SCNErrorDomain: String ``` |

Modified SCNGeometrySourceSemanticBoneIndices

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticBoneIndices: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticBoneIndices: String ``` |

Modified SCNGeometrySourceSemanticBoneWeights

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticBoneWeights: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticBoneWeights: String ``` |

Modified SCNGeometrySourceSemanticColor

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticColor: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticColor: String ``` |

Modified SCNGeometrySourceSemanticEdgeCrease

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticEdgeCrease: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticEdgeCrease: String ``` |

Modified SCNGeometrySourceSemanticNormal

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticNormal: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticNormal: String ``` |

Modified SCNGeometrySourceSemanticTexcoord

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticTexcoord: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticTexcoord: String ``` |

Modified SCNGeometrySourceSemanticVertex

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticVertex: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticVertex: String ``` |

Modified SCNGeometrySourceSemanticVertexCrease

|  | Declaration |
| --- | --- |
| From | ``` let SCNGeometrySourceSemanticVertexCrease: NSString! ``` |
| To | ``` let SCNGeometrySourceSemanticVertexCrease: String ``` |

Modified SCNHitTestBackFaceCullingKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestBackFaceCullingKey: NSString! ``` |
| To | ``` let SCNHitTestBackFaceCullingKey: String ``` |

Modified SCNHitTestBoundingBoxOnlyKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestBoundingBoxOnlyKey: NSString! ``` |
| To | ``` let SCNHitTestBoundingBoxOnlyKey: String ``` |

Modified SCNHitTestClipToZRangeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestClipToZRangeKey: NSString! ``` |
| To | ``` let SCNHitTestClipToZRangeKey: String ``` |

Modified SCNHitTestFirstFoundOnlyKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestFirstFoundOnlyKey: NSString! ``` |
| To | ``` let SCNHitTestFirstFoundOnlyKey: String ``` |

Modified SCNHitTestIgnoreChildNodesKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestIgnoreChildNodesKey: NSString! ``` |
| To | ``` let SCNHitTestIgnoreChildNodesKey: String ``` |

Modified SCNHitTestIgnoreHiddenNodesKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestIgnoreHiddenNodesKey: NSString! ``` |
| To | ``` let SCNHitTestIgnoreHiddenNodesKey: String ``` |

Modified SCNHitTestRootNodeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestRootNodeKey: NSString! ``` |
| To | ``` let SCNHitTestRootNodeKey: String ``` |

Modified SCNHitTestSortResultsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNHitTestSortResultsKey: NSString! ``` |
| To | ``` let SCNHitTestSortResultsKey: String ``` |

Modified SCNLightTypeAmbient

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightTypeAmbient: NSString! ``` |
| To | ``` let SCNLightTypeAmbient: String ``` |

Modified SCNLightTypeDirectional

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightTypeDirectional: NSString! ``` |
| To | ``` let SCNLightTypeDirectional: String ``` |

Modified SCNLightTypeOmni

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightTypeOmni: NSString! ``` |
| To | ``` let SCNLightTypeOmni: String ``` |

Modified SCNLightTypeSpot

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightTypeSpot: NSString! ``` |
| To | ``` let SCNLightTypeSpot: String ``` |

Modified SCNLightingModelBlinn

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightingModelBlinn: NSString! ``` |
| To | ``` let SCNLightingModelBlinn: String ``` |

Modified SCNLightingModelConstant

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightingModelConstant: NSString! ``` |
| To | ``` let SCNLightingModelConstant: String ``` |

Modified SCNLightingModelLambert

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightingModelLambert: NSString! ``` |
| To | ``` let SCNLightingModelLambert: String ``` |

Modified SCNLightingModelPhong

|  | Declaration |
| --- | --- |
| From | ``` let SCNLightingModelPhong: NSString! ``` |
| To | ``` let SCNLightingModelPhong: String ``` |

Modified SCNModelTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNModelTransform: NSString! ``` |
| To | ``` let SCNModelTransform: String ``` |

Modified SCNModelViewProjectionTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNModelViewProjectionTransform: NSString! ``` |
| To | ``` let SCNModelViewProjectionTransform: String ``` |

Modified SCNModelViewTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNModelViewTransform: NSString! ``` |
| To | ``` let SCNModelViewTransform: String ``` |

Modified SCNNormalTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNNormalTransform: NSString! ``` |
| To | ``` let SCNNormalTransform: String ``` |

Modified SCNParticleEventBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNParticleEventBlock = (UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt32>, Int) -> Void ``` |
| To | ``` typealias SCNParticleEventBlock = (UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UInt32>, Int) -> Void ``` |

Modified SCNParticleModifierBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNParticleModifierBlock = (UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UInt>, Int, Int, Float) -> Void ``` |
| To | ``` typealias SCNParticleModifierBlock = (UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Int>, Int, Int, Float) -> Void ``` |

Modified SCNParticlePropertyAngle

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyAngle: NSString! ``` |
| To | ``` let SCNParticlePropertyAngle: String ``` |

Modified SCNParticlePropertyAngularVelocity

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyAngularVelocity: NSString! ``` |
| To | ``` let SCNParticlePropertyAngularVelocity: String ``` |

Modified SCNParticlePropertyBounce

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyBounce: NSString! ``` |
| To | ``` let SCNParticlePropertyBounce: String ``` |

Modified SCNParticlePropertyCharge

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyCharge: NSString! ``` |
| To | ``` let SCNParticlePropertyCharge: String ``` |

Modified SCNParticlePropertyColor

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyColor: NSString! ``` |
| To | ``` let SCNParticlePropertyColor: String ``` |

Modified SCNParticlePropertyContactNormal

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyContactNormal: NSString! ``` |
| To | ``` let SCNParticlePropertyContactNormal: String ``` |

Modified SCNParticlePropertyContactPoint

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyContactPoint: NSString! ``` |
| To | ``` let SCNParticlePropertyContactPoint: String ``` |

Modified SCNParticlePropertyFrame

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyFrame: NSString! ``` |
| To | ``` let SCNParticlePropertyFrame: String ``` |

Modified SCNParticlePropertyFrameRate

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyFrameRate: NSString! ``` |
| To | ``` let SCNParticlePropertyFrameRate: String ``` |

Modified SCNParticlePropertyFriction

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyFriction: NSString! ``` |
| To | ``` let SCNParticlePropertyFriction: String ``` |

Modified SCNParticlePropertyLife

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyLife: NSString! ``` |
| To | ``` let SCNParticlePropertyLife: String ``` |

Modified SCNParticlePropertyOpacity

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyOpacity: NSString! ``` |
| To | ``` let SCNParticlePropertyOpacity: String ``` |

Modified SCNParticlePropertyPosition

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyPosition: NSString! ``` |
| To | ``` let SCNParticlePropertyPosition: String ``` |

Modified SCNParticlePropertyRotationAxis

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyRotationAxis: NSString! ``` |
| To | ``` let SCNParticlePropertyRotationAxis: String ``` |

Modified SCNParticlePropertySize

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertySize: NSString! ``` |
| To | ``` let SCNParticlePropertySize: String ``` |

Modified SCNParticlePropertyVelocity

|  | Declaration |
| --- | --- |
| From | ``` let SCNParticlePropertyVelocity: NSString! ``` |
| To | ``` let SCNParticlePropertyVelocity: String ``` |

Modified SCNPhysicsShapeKeepAsCompoundKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeKeepAsCompoundKey: NSString! ``` |
| To | ``` let SCNPhysicsShapeKeepAsCompoundKey: String ``` |

Modified SCNPhysicsShapeScaleKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeScaleKey: NSString! ``` |
| To | ``` let SCNPhysicsShapeScaleKey: String ``` |

Modified SCNPhysicsShapeTypeBoundingBox

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeTypeBoundingBox: NSString! ``` |
| To | ``` let SCNPhysicsShapeTypeBoundingBox: String ``` |

Modified SCNPhysicsShapeTypeConcavePolyhedron

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeTypeConcavePolyhedron: NSString! ``` |
| To | ``` let SCNPhysicsShapeTypeConcavePolyhedron: String ``` |

Modified SCNPhysicsShapeTypeConvexHull

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeTypeConvexHull: NSString! ``` |
| To | ``` let SCNPhysicsShapeTypeConvexHull: String ``` |

Modified SCNPhysicsShapeTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsShapeTypeKey: NSString! ``` |
| To | ``` let SCNPhysicsShapeTypeKey: String ``` |

Modified SCNPhysicsTestBackfaceCullingKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestBackfaceCullingKey: NSString! ``` |
| To | ``` let SCNPhysicsTestBackfaceCullingKey: String ``` |

Modified SCNPhysicsTestCollisionBitMaskKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestCollisionBitMaskKey: NSString! ``` |
| To | ``` let SCNPhysicsTestCollisionBitMaskKey: String ``` |

Modified SCNPhysicsTestSearchModeAll

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestSearchModeAll: NSString! ``` |
| To | ``` let SCNPhysicsTestSearchModeAll: String ``` |

Modified SCNPhysicsTestSearchModeAny

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestSearchModeAny: NSString! ``` |
| To | ``` let SCNPhysicsTestSearchModeAny: String ``` |

Modified SCNPhysicsTestSearchModeClosest

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestSearchModeClosest: NSString! ``` |
| To | ``` let SCNPhysicsTestSearchModeClosest: String ``` |

Modified SCNPhysicsTestSearchModeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNPhysicsTestSearchModeKey: NSString! ``` |
| To | ``` let SCNPhysicsTestSearchModeKey: String ``` |

Modified SCNProgramMappingChannelKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNProgramMappingChannelKey: NSString! ``` |
| To | ``` let SCNProgramMappingChannelKey: String ``` |

Modified SCNProjectionTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNProjectionTransform: NSString! ``` |
| To | ``` let SCNProjectionTransform: String ``` |

Modified SCNSceneEndTimeAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneEndTimeAttributeKey: NSString! ``` |
| To | ``` let SCNSceneEndTimeAttributeKey: String ``` |

Modified SCNSceneExportDestinationURL

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneExportDestinationURL: NSString! ``` |
| To | ``` let SCNSceneExportDestinationURL: String ``` |

Modified SCNSceneFrameRateAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneFrameRateAttributeKey: NSString! ``` |
| To | ``` let SCNSceneFrameRateAttributeKey: String ``` |

Modified SCNSceneSourceAnimationImportPolicyDoNotPlay

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyDoNotPlay: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyDoNotPlay: String ``` |

Modified SCNSceneSourceAnimationImportPolicyKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyKey: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyKey: String ``` |

Modified SCNSceneSourceAnimationImportPolicyPlay

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyPlay: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyPlay: String ``` |

Modified SCNSceneSourceAnimationImportPolicyPlayRepeatedly

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyPlayRepeatedly: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyPlayRepeatedly: String ``` |

Modified SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase: NSString! ``` |
| To | ``` let SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase: String ``` |

Modified SCNSceneSourceAssetAuthorKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetAuthorKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetAuthorKey: String ``` |

Modified SCNSceneSourceAssetAuthoringToolKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetAuthoringToolKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetAuthoringToolKey: String ``` |

Modified SCNSceneSourceAssetContributorsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetContributorsKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetContributorsKey: String ``` |

Modified SCNSceneSourceAssetCreatedDateKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetCreatedDateKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetCreatedDateKey: String ``` |

Modified SCNSceneSourceAssetDirectoryURLsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetDirectoryURLsKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetDirectoryURLsKey: String ``` |

Modified SCNSceneSourceAssetModifiedDateKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetModifiedDateKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetModifiedDateKey: String ``` |

Modified SCNSceneSourceAssetUnitKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetUnitKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetUnitKey: String ``` |

Modified SCNSceneSourceAssetUnitMeterKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetUnitMeterKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetUnitMeterKey: String ``` |

Modified SCNSceneSourceAssetUnitNameKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetUnitNameKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetUnitNameKey: String ``` |

Modified SCNSceneSourceAssetUpAxisKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceAssetUpAxisKey: NSString! ``` |
| To | ``` let SCNSceneSourceAssetUpAxisKey: String ``` |

Modified SCNSceneSourceCheckConsistencyKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceCheckConsistencyKey: NSString! ``` |
| To | ``` let SCNSceneSourceCheckConsistencyKey: String ``` |

Modified SCNSceneSourceCreateNormalsIfAbsentKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceCreateNormalsIfAbsentKey: NSString! ``` |
| To | ``` let SCNSceneSourceCreateNormalsIfAbsentKey: String ``` |

Modified SCNSceneSourceFlattenSceneKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceFlattenSceneKey: NSString! ``` |
| To | ``` let SCNSceneSourceFlattenSceneKey: String ``` |

Modified SCNSceneSourceOverrideAssetURLsKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceOverrideAssetURLsKey: NSString! ``` |
| To | ``` let SCNSceneSourceOverrideAssetURLsKey: String ``` |

Modified SCNSceneSourceStrictConformanceKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceStrictConformanceKey: NSString! ``` |
| To | ``` let SCNSceneSourceStrictConformanceKey: String ``` |

Modified SCNSceneSourceUseSafeModeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneSourceUseSafeModeKey: NSString! ``` |
| To | ``` let SCNSceneSourceUseSafeModeKey: String ``` |

Modified SCNSceneStartTimeAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneStartTimeAttributeKey: NSString! ``` |
| To | ``` let SCNSceneStartTimeAttributeKey: String ``` |

Modified SCNSceneUpAxisAttributeKey

|  | Declaration |
| --- | --- |
| From | ``` let SCNSceneUpAxisAttributeKey: NSString! ``` |
| To | ``` let SCNSceneUpAxisAttributeKey: String ``` |

Modified SCNShaderModifierEntryPointFragment

|  | Declaration |
| --- | --- |
| From | ``` let SCNShaderModifierEntryPointFragment: NSString! ``` |
| To | ``` let SCNShaderModifierEntryPointFragment: String ``` |

Modified SCNShaderModifierEntryPointGeometry

|  | Declaration |
| --- | --- |
| From | ``` let SCNShaderModifierEntryPointGeometry: NSString! ``` |
| To | ``` let SCNShaderModifierEntryPointGeometry: String ``` |

Modified SCNShaderModifierEntryPointLightingModel

|  | Declaration |
| --- | --- |
| From | ``` let SCNShaderModifierEntryPointLightingModel: NSString! ``` |
| To | ``` let SCNShaderModifierEntryPointLightingModel: String ``` |

Modified SCNShaderModifierEntryPointSurface

|  | Declaration |
| --- | --- |
| From | ``` let SCNShaderModifierEntryPointSurface: NSString! ``` |
| To | ``` let SCNShaderModifierEntryPointSurface: String ``` |

Modified SCNViewTransform

|  | Declaration |
| --- | --- |
| From | ``` let SCNViewTransform: NSString! ``` |
| To | ``` let SCNViewTransform: String ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

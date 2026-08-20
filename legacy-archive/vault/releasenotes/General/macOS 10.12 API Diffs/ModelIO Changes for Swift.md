---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/ModelIO.html
archived_at: '2026-07-18T02:51:29.940148Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# ModelIO Changes for Swift

### ModelIO

Removed [MDLAsset.exportAssetToURL(_: NSURL) -> Bool](https://developer.apple.com/documentation/modelio/mdlasset/1391223-exportassettourl)Removed MDLGeometryType.kindLinesRemoved MDLGeometryType.kindPointsRemoved MDLGeometryType.kindQuadsRemoved MDLGeometryType.kindTrianglesRemoved MDLGeometryType.kindTriangleStripsAdded [MDLAsset.childObjects(of: Swift.AnyClass) -> [MDLObject]](https://developer.apple.com/documentation/modelio/mdlasset/1644589-childobjects)Added [MDLAsset.init(bufferAllocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlasset/1644590-initwithbufferallocator)Added [MDLAsset.masters](https://developer.apple.com/documentation/modelio/mdlasset/2097126-masters)Added [MDLAsset.placeLightProbes(withDensity: Float, heuristic: MDLProbePlacement, using: MDLLightProbeIrradianceDataSource) -> [MDLLightProbe] [class]](https://developer.apple.com/documentation/modelio/mdlasset/1644588-placelightprobeswithdensity)Added [MDLCamera.projection](https://developer.apple.com/documentation/modelio/mdlcamera/1645841-projection)Added [MDLCameraProjection [enum]](https://developer.apple.com/documentation/modelio/mdlcameraprojection)Added [MDLCameraProjection.orthographic](https://developer.apple.com/documentation/modelio/mdlcameraprojection/orthographic)Added [MDLCameraProjection.perspective](https://developer.apple.com/documentation/modelio/mdlcameraprojection/mdlcameraprojectionperspective)Added [MDLLight.colorSpace](https://developer.apple.com/documentation/modelio/mdllight/1823498-colorspace)Added [MDLLightProbeIrradianceDataSource](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource)Added [MDLLightProbeIrradianceDataSource.boundingBox](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource/1644585-boundingbox)Added [MDLLightProbeIrradianceDataSource.sphericalHarmonicsCoefficients(atPosition: vector_float3) -> Data](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource/1644584-sphericalharmonicscoefficients)Added [MDLLightProbeIrradianceDataSource.sphericalHarmonicsLevel](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource/1644586-sphericalharmonicslevel)Added [MDLMaterial.materialFace](https://developer.apple.com/documentation/modelio/mdlmaterial/1642036-materialface)Added [MDLMaterialFace [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialface)Added [MDLMaterialFace.back](https://developer.apple.com/documentation/modelio/mdlmaterialface/back)Added [MDLMaterialFace.doubleSided](https://developer.apple.com/documentation/modelio/mdlmaterialface/mdlmaterialfacedoublesided)Added [MDLMaterialFace.front](https://developer.apple.com/documentation/modelio/mdlmaterialface/front)Added [MDLMaterialProperty.luminance](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/1642051-luminance)Added [MDLMaterialPropertyConnection](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection)Added [MDLMaterialPropertyConnection.init(output: MDLMaterialProperty, input: MDLMaterialProperty)](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection/1642034-initwithoutput)Added [MDLMaterialPropertyConnection.input](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection/1642037-input)Added [MDLMaterialPropertyConnection.output](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection/1642041-output)Added [MDLMaterialPropertyGraph](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph)Added [MDLMaterialPropertyGraph.connections](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph/1642040-connections)Added [MDLMaterialPropertyGraph.evaluate()](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph/1642044-evaluate)Added [MDLMaterialPropertyGraph.init(nodes: [MDLMaterialPropertyNode], connections: [MDLMaterialPropertyConnection])](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph/1642048-init)Added [MDLMaterialPropertyGraph.nodes](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph/1642043-nodes)Added [MDLMaterialPropertyNode](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode)Added [MDLMaterialPropertyNode.evaluationFunction](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/1642039-evaluationfunction)Added [MDLMaterialPropertyNode.init(inputs: [MDLMaterialProperty], outputs: [MDLMaterialProperty], evaluationFunction: (MDLMaterialPropertyNode) -> Swift.Void)](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/1642053-init)Added [MDLMaterialPropertyNode.inputs](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/1642052-inputs)Added [MDLMaterialPropertyNode.outputs](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode/1642049-outputs)Added [MDLMesh.addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int)](https://developer.apple.com/documentation/modelio/mdlmesh/1823499-addattributewithname)Added [MDLMesh.addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int, time: TimeInterval)](https://developer.apple.com/documentation/modelio/mdlmesh/2097115-addattribute)Added [MDLMesh.addUnwrappedTextureCoordinates(forAttributeNamed: String)](https://developer.apple.com/documentation/modelio/mdlmesh/1644690-addunwrappedtexturecoordinates)Added [MDLMesh.allocator](https://developer.apple.com/documentation/modelio/mdlmesh/1778158-allocator)Added [MDLMesh.init(boxWithExtent: vector_float3, segments: vector_uint3, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644689-initboxwithextent)Added [MDLMesh.init(bufferAllocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1778157-initwithbufferallocator)Added [MDLMesh.init(capsuleWithExtent: vector_float3, cylinderSegments: vector_uint2, hemisphereSegments: Int32, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644680-initcapsulewithextent)Added [MDLMesh.init(coneWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, cap: Bool, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644688-init)Added [MDLMesh.init(cylinderWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, topCap: Bool, bottomCap: Bool, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644686-init)Added [MDLMesh.init(hemisphereWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, cap: Bool, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644685-init)Added [MDLMesh.init(icosahedronWithExtent: vector_float3, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644682-init)Added [MDLMesh.init(meshBySubdividingMesh: MDLMesh, submeshIndex: Int32, subdivisionLevels: UInt32, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644678-init)Added [MDLMesh.init(planeWithExtent: vector_float3, segments: vector_uint2, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644677-initplanewithextent)Added [MDLMesh.init(sphereWithExtent: vector_float3, segments: vector_uint2, inwardNormals: Bool, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlmesh/1644681-init)Added [MDLMesh.newBox(withDimensions: vector_float3, segments: vector_uint3, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: MDLMeshBufferAllocator?) -> Self [class]](https://developer.apple.com/documentation/modelio/mdlmesh/1562077-newbox)Added [MDLMesh.newPlane(withDimensions: vector_float2, segments: vector_uint2, geometryType: MDLGeometryType, allocator: MDLMeshBufferAllocator?) -> Self [class]](https://developer.apple.com/documentation/modelio/mdlmesh/1562078-newplanewithdimensions)Added [MDLMesh.removeAttributeNamed(_: String)](https://developer.apple.com/documentation/modelio/mdlmesh/1644684-removeattributenamed)Added [MDLMesh.replaceAttributeNamed(_: String, with: MDLVertexAttributeData)](https://developer.apple.com/documentation/modelio/mdlmesh/1644679-replaceattributenamed)Added [MDLMesh.updateAttributeNamed(_: String, with: MDLVertexAttributeData)](https://developer.apple.com/documentation/modelio/mdlmesh/1644683-updateattributenamed)Added [MDLMesh.vertexAttributeData(forAttributeNamed: String, as: MDLVertexFormat) -> MDLVertexAttributeData?](https://developer.apple.com/documentation/modelio/mdlmesh/1644687-vertexattributedata)Added [MDLObject.atPath(_: String) -> MDLObject](https://developer.apple.com/documentation/modelio/mdlobject/2097124-objectatpath)Added [MDLObject.hidden](https://developer.apple.com/documentation/modelio/mdlobject/2143069-hidden)Added [MDLObject.instance](https://developer.apple.com/documentation/modelio/mdlobject/2097123-instance)Added [MDLObject.path](https://developer.apple.com/documentation/modelio/mdlobject/1642272-path)Added [MDLProbePlacement [enum]](https://developer.apple.com/documentation/modelio/mdlprobeplacement)Added [MDLProbePlacement.irradianceDistribution](https://developer.apple.com/documentation/modelio/mdlprobeplacement/mdlprobeplacementirradiancedistribution)Added [MDLProbePlacement.uniformGrid](https://developer.apple.com/documentation/modelio/mdlprobeplacement/uniformgrid)Added [MDLSubmesh.indexBuffer(asIndexType: MDLIndexBitDepth) -> MDLMeshBuffer](https://developer.apple.com/documentation/modelio/mdlsubmesh/1644031-indexbufferasindextype)Added [MDLTexture.hasAlphaValues](https://developer.apple.com/documentation/modelio/mdltexture/1644783-hasalphavalues)Added [MDLTexture.init()](https://developer.apple.com/documentation/modelio/mdltexture/1644782-init)Added [MDLTransform.init(matrix: matrix_float4x4, resetsTransform: Bool)](https://developer.apple.com/documentation/modelio/mdltransform/1643554-initwithmatrix)Added [MDLTransform.init(transformComponent: MDLTransformComponent, resetsTransform: Bool)](https://developer.apple.com/documentation/modelio/mdltransform/1643552-initwithtransformcomponent)Added [MDLTransformComponent.keyTimes](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1823488-keytimes)Added [MDLTransformComponent.resetsTransform](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1643553-resetstransform)Added [MDLVertexAttribute.time](https://developer.apple.com/documentation/modelio/mdlvertexattribute/2097127-time)Added [MDLVertexBufferLayout.init(stride: Int)](https://developer.apple.com/documentation/modelio/mdlvertexbufferlayout/2097125-init)Added [MDLVertexDescriptor.removeAttributeNamed(_: String)](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor/1645007-removeattributenamed)Added [MDLVoxelArray.coarseMesh() -> MDLMesh?](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640656-coarsemesh)Added [MDLVoxelArray.coarseMesh(using: MDLMeshBufferAllocator?) -> MDLMesh?](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1823497-coarsemeshusingallocator)Added [MDLVoxelArray.convertToSignedShellField()](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640668-converttosignedshellfield)Added [MDLVoxelArray.init(asset: MDLAsset, divisions: Int32, patchRadius: Float)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640657-initwithasset)Added [MDLVoxelArray.isValidSignedShellField](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640661-isvalidsignedshellfield)Added [MDLVoxelArray.setVoxelsFor(_: MDLMesh, divisions: Int32, patchRadius: Float)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640666-setvoxelsformesh)Added [MDLVoxelArray.shellFieldExteriorThickness](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640670-shellfieldexteriorthickness)Added [MDLVoxelArray.shellFieldInteriorThickness](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1640664-shellfieldinteriorthickness)Added [kUTTypeUniversalSceneDescription](https://developer.apple.com/documentation/modelio/kuttypeuniversalscenedescription)Modified [MDLAsset](https://developer.apple.com/documentation/modelio/mdlasset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLAsset : NSObject, NSCopying, NSFastEnumeration {     init(URL URL: NSURL)     init(URL URL: NSURL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     init(URL URL: NSURL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?, preserveTopology preserveTopology: Bool, error error: NSErrorPointer)     func exportAssetToURL(_ URL: NSURL) -> Bool     func exportAssetToURL(_ URL: NSURL, error error: ()) throws     class func canImportFileExtension(_ extension: String) -> Bool     class func canExportFileExtension(_ extension: String) -> Bool     func boundingBoxAtTime(_ time: NSTimeInterval) -> MDLAxisAlignedBoundingBox     var boundingBox: MDLAxisAlignedBoundingBox { get }     var frameInterval: NSTimeInterval     var startTime: NSTimeInterval     var endTime: NSTimeInterval     var URL: NSURL? { get }     var bufferAllocator: MDLMeshBufferAllocator { get }     var vertexDescriptor: MDLVertexDescriptor? { get }     func addObject(_ object: MDLObject)     func removeObject(_ object: MDLObject)     var count: Int { get }     subscript (_ index: Int) -> MDLObject? { get }     func objectAtIndexedSubscript(_ index: Int) -> MDLObject?     func objectAtIndex(_ index: Int) -> MDLObject } extension MDLAsset {     convenience init(SCNScene scnScene: SCNScene)     class func assetWithSCNScene(_ scnScene: SCNScene) -> Self } ``` | NSCopying, NSFastEnumeration |
| To | ``` class MDLAsset : NSObject, NSCopying, NSFastEnumeration {     init(url URL: URL)     init(url URL: URL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     init(bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     init(url URL: URL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?, preserveTopology preserveTopology: Bool, error error: NSErrorPointer)     func export(to URL: URL) -> Bool     func export(to URL: URL) throws     class func canImportFileExtension(_ extension: String) -> Bool     class func canExportFileExtension(_ extension: String) -> Bool     func childObjects(of objectClass: Swift.AnyClass) -> [MDLObject]     func boundingBox(atTime time: TimeInterval) -> MDLAxisAlignedBoundingBox     var boundingBox: MDLAxisAlignedBoundingBox { get }     var frameInterval: TimeInterval     var startTime: TimeInterval     var endTime: TimeInterval     var url: URL? { get }     var bufferAllocator: MDLMeshBufferAllocator { get }     var vertexDescriptor: MDLVertexDescriptor? { get }     func add(_ object: MDLObject)     func remove(_ object: MDLObject)     var count: Int { get }     subscript(_ index: Int) -> MDLObject? { get }     func objectAtIndexedSubscript(_ index: Int) -> MDLObject?     func object(at index: Int) -> MDLObject     var masters: MDLObjectContainerComponent     class func placeLightProbes(withDensity value: Float, heuristic type: MDLProbePlacement, using dataSource: MDLLightProbeIrradianceDataSource) -> [MDLLightProbe]     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLAsset : CVarArg { } extension MDLAsset : Equatable, Hashable {     var hashValue: Int { get } } extension MDLAsset {     class func placeLightProbes(withDensity value: Float, heuristic type: MDLProbePlacement, using dataSource: MDLLightProbeIrradianceDataSource) -> [MDLLightProbe] } extension MDLAsset {     convenience init(scnScene scnScene: SCNScene)     class func withSCNScene(_ scnScene: SCNScene) -> Self     convenience init(scnScene scnScene: SCNScene, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     class func withSCNScene(_ scnScene: SCNScene, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?) -> Self } ``` | CVarArg, Equatable, Hashable, NSCopying, NSFastEnumeration |

Modified [MDLAsset.add(_: MDLObject)](https://developer.apple.com/documentation/modelio/mdlasset/1391634-add)

|  | Declaration |
| --- | --- |
| From | ``` func addObject(_ object: MDLObject) ``` |
| To | ``` func add(_ object: MDLObject) ``` |

Modified [MDLAsset.boundingBox(atTime: TimeInterval) -> MDLAxisAlignedBoundingBox](https://developer.apple.com/documentation/modelio/mdlasset/1391667-boundingbox)

|  | Declaration |
| --- | --- |
| From | ``` func boundingBoxAtTime(_ time: NSTimeInterval) -> MDLAxisAlignedBoundingBox ``` |
| To | ``` func boundingBox(atTime time: TimeInterval) -> MDLAxisAlignedBoundingBox ``` |

Modified [MDLAsset.endTime](https://developer.apple.com/documentation/modelio/mdlasset/1391393-endtime)

|  | Declaration |
| --- | --- |
| From | ``` var endTime: NSTimeInterval ``` |
| To | ``` var endTime: TimeInterval ``` |

Modified [MDLAsset.export(to: URL) throws](https://developer.apple.com/documentation/modelio/mdlasset/1391036-exportassettourl)

|  | Declaration |
| --- | --- |
| From | ``` func exportAssetToURL(_ URL: NSURL, error error: ()) throws ``` |
| To | ``` func export(to URL: URL) throws ``` |

Modified [MDLAsset.frameInterval](https://developer.apple.com/documentation/modelio/mdlasset/1391944-frameinterval)

|  | Declaration |
| --- | --- |
| From | ``` var frameInterval: NSTimeInterval ``` |
| To | ``` var frameInterval: TimeInterval ``` |

Modified [MDLAsset.init(url: URL)](https://developer.apple.com/documentation/modelio/mdlasset/1391513-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL) ``` |
| To | ``` init(url URL: URL) ``` |

Modified [MDLAsset.init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: MDLMeshBufferAllocator?)](https://developer.apple.com/documentation/modelio/mdlasset/1391511-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?) ``` |
| To | ``` init(url URL: URL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?) ``` |

Modified [MDLAsset.init(url: URL, vertexDescriptor: MDLVertexDescriptor?, bufferAllocator: MDLMeshBufferAllocator?, preserveTopology: Bool, error: NSErrorPointer)](https://developer.apple.com/documentation/modelio/mdlasset/1391912-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?, preserveTopology preserveTopology: Bool, error error: NSErrorPointer) ``` |
| To | ``` init(url URL: URL, vertexDescriptor vertexDescriptor: MDLVertexDescriptor?, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?, preserveTopology preserveTopology: Bool, error error: NSErrorPointer) ``` |

Modified [MDLAsset.object(at: Int) -> MDLObject](https://developer.apple.com/documentation/modelio/mdlasset/1391170-objectatindex)

|  | Declaration |
| --- | --- |
| From | ``` func objectAtIndex(_ index: Int) -> MDLObject ``` |
| To | ``` func object(at index: Int) -> MDLObject ``` |

Modified [MDLAsset.remove(_: MDLObject)](https://developer.apple.com/documentation/modelio/mdlasset/1391495-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ object: MDLObject) ``` |
| To | ``` func remove(_ object: MDLObject) ``` |

Modified [MDLAsset.startTime](https://developer.apple.com/documentation/modelio/mdlasset/1391675-starttime)

|  | Declaration |
| --- | --- |
| From | ``` var startTime: NSTimeInterval ``` |
| To | ``` var startTime: TimeInterval ``` |

Modified [MDLAsset.subscript(_: Int) -> MDLObject?](https://developer.apple.com/documentation/modelio/mdlasset/1391542-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> MDLObject? { get } ``` |
| To | ``` subscript(_ index: Int) -> MDLObject? { get } ``` |

Modified [MDLAsset.url](https://developer.apple.com/documentation/modelio/mdlasset/1391923-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL? { get } ``` |
| To | ``` var url: URL? { get } ``` |

Modified [MDLCamera](https://developer.apple.com/documentation/modelio/mdlcamera)

|  | Declaration |
| --- | --- |
| From | ``` class MDLCamera : MDLObject {     var projectionMatrix: matrix_float4x4 { get }     func frameBoundingBox(_ boundingBox: MDLAxisAlignedBoundingBox, setNearAndFar setNearAndFar: Bool)     func lookAt(_ focusPosition: vector_float3)     func lookAt(_ focusPosition: vector_float3, from cameraPosition: vector_float3)     func rayTo(_ pixel: vector_int2, forViewPort size: vector_int2) -> vector_float3     var nearVisibilityDistance: Float     var farVisibilityDistance: Float     var worldToMetersConversionScale: Float     var barrelDistortion: Float     var fisheyeDistortion: Float     var opticalVignetting: Float     var chromaticAberration: Float     var focalLength: Float     var focusDistance: Float     var fieldOfView: Float     var fStop: Float     var apertureBladeCount: Int     var maximumCircleOfConfusion: Float     func bokehKernelWithSize(_ size: vector_int2) -> MDLTexture     var shutterOpenInterval: NSTimeInterval     var sensorVerticalAperture: Float     var sensorAspect: Float     var sensorEnlargement: vector_float2     var sensorShift: vector_float2     var flash: vector_float3     var exposureCompression: vector_float2     var exposure: vector_float3 } extension MDLCamera {     convenience init(SCNCamera scnCamera: SCNCamera)     class func cameraWithSCNCamera(_ scnCamera: SCNCamera) -> Self } ``` |
| To | ``` class MDLCamera : MDLObject {     var projectionMatrix: matrix_float4x4 { get }     var projection: MDLCameraProjection     func frameBoundingBox(_ boundingBox: MDLAxisAlignedBoundingBox, setNearAndFar setNearAndFar: Bool)     func look(at focusPosition: vector_float3)     func look(at focusPosition: vector_float3, from cameraPosition: vector_float3)     func ray(to pixel: vector_int2, forViewPort size: vector_int2) -> vector_float3     var nearVisibilityDistance: Float     var farVisibilityDistance: Float     var worldToMetersConversionScale: Float     var barrelDistortion: Float     var fisheyeDistortion: Float     var opticalVignetting: Float     var chromaticAberration: Float     var focalLength: Float     var focusDistance: Float     var fieldOfView: Float     var fStop: Float     var apertureBladeCount: Int     var maximumCircleOfConfusion: Float     func bokehKernel(withSize size: vector_int2) -> MDLTexture     var shutterOpenInterval: TimeInterval     var sensorVerticalAperture: Float     var sensorAspect: Float     var sensorEnlargement: vector_float2     var sensorShift: vector_float2     var flash: vector_float3     var exposureCompression: vector_float2     var exposure: vector_float3 } extension MDLCamera {     convenience init(scnCamera scnCamera: SCNCamera)     class func withSCNCamera(_ scnCamera: SCNCamera) -> Self } ``` |

Modified [MDLCamera.bokehKernel(withSize: vector_int2) -> MDLTexture](https://developer.apple.com/documentation/modelio/mdlcamera/1391898-bokehkernel)

|  | Declaration |
| --- | --- |
| From | ``` func bokehKernelWithSize(_ size: vector_int2) -> MDLTexture ``` |
| To | ``` func bokehKernel(withSize size: vector_int2) -> MDLTexture ``` |

Modified [MDLCamera.look(at: vector_float3)](https://developer.apple.com/documentation/modelio/mdlcamera/1391395-lookat)

|  | Declaration |
| --- | --- |
| From | ``` func lookAt(_ focusPosition: vector_float3) ``` |
| To | ``` func look(at focusPosition: vector_float3) ``` |

Modified [MDLCamera.look(at: vector_float3, from: vector_float3)](https://developer.apple.com/documentation/modelio/mdlcamera/1391907-lookat)

|  | Declaration |
| --- | --- |
| From | ``` func lookAt(_ focusPosition: vector_float3, from cameraPosition: vector_float3) ``` |
| To | ``` func look(at focusPosition: vector_float3, from cameraPosition: vector_float3) ``` |

Modified [MDLCamera.ray(to: vector_int2, forViewPort: vector_int2) -> vector_float3](https://developer.apple.com/documentation/modelio/mdlcamera/1391047-rayto)

|  | Declaration |
| --- | --- |
| From | ``` func rayTo(_ pixel: vector_int2, forViewPort size: vector_int2) -> vector_float3 ``` |
| To | ``` func ray(to pixel: vector_int2, forViewPort size: vector_int2) -> vector_float3 ``` |

Modified [MDLCamera.shutterOpenInterval](https://developer.apple.com/documentation/modelio/mdlcamera/1392029-shutteropeninterval)

|  | Declaration |
| --- | --- |
| From | ``` var shutterOpenInterval: NSTimeInterval ``` |
| To | ``` var shutterOpenInterval: TimeInterval ``` |

Modified [MDLColorSwatchTexture](https://developer.apple.com/documentation/modelio/mdlcolorswatchtexture)

|  | Declaration |
| --- | --- |
| From | ``` class MDLColorSwatchTexture : MDLTexture {     init(colorTemperatureGradientFrom colorTemperature1: Float, toColorTemperature colorTemperature2: Float, name name: String?, textureDimensions textureDimensions: vector_int2)     init(colorGradientFrom color1: CGColor, toColor color2: CGColor, name name: String?, textureDimensions textureDimensions: vector_int2) } ``` |
| To | ``` class MDLColorSwatchTexture : MDLTexture {     init(colorTemperatureGradientFrom colorTemperature1: Float, toColorTemperature colorTemperature2: Float, name name: String?, textureDimensions textureDimensions: vector_int2)     init(colorGradientFrom color1: CGColor, to color2: CGColor, name name: String?, textureDimensions textureDimensions: vector_int2) } ``` |

Modified [MDLColorSwatchTexture.init(colorGradientFrom: CGColor, to: CGColor, name: String?, textureDimensions: vector_int2)](https://developer.apple.com/documentation/modelio/mdlcolorswatchtexture/1391260-initwithcolorgradientfrom)

|  | Declaration |
| --- | --- |
| From | ``` init(colorGradientFrom color1: CGColor, toColor color2: CGColor, name name: String?, textureDimensions textureDimensions: vector_int2) ``` |
| To | ``` init(colorGradientFrom color1: CGColor, to color2: CGColor, name name: String?, textureDimensions textureDimensions: vector_int2) ``` |

Modified [MDLGeometryType [enum]](https://developer.apple.com/documentation/modelio/mdlgeometrytype)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLGeometryType : Int {     case TypePoints     case TypeLines     case TypeTriangles     case TypeTriangleStrips     case TypeQuads     case TypeVariableTopology     static var KindPoints: MDLGeometryType { get }     static var KindLines: MDLGeometryType { get }     static var KindTriangles: MDLGeometryType { get }     static var KindTriangleStrips: MDLGeometryType { get }     static var KindQuads: MDLGeometryType { get } } ``` |
| To | ``` enum MDLGeometryType : Int {     case points     case lines     case triangles     case triangleStrips     case quads     case variableTopology } ``` |

Modified [MDLGeometryType.lines](https://developer.apple.com/documentation/modelio/mdlgeometrytype/lines)

|  | Declaration |
| --- | --- |
| From | ``` case TypeLines ``` |
| To | ``` case lines ``` |

Modified [MDLGeometryType.points](https://developer.apple.com/documentation/modelio/mdlgeometrytype/points)

|  | Declaration |
| --- | --- |
| From | ``` case TypePoints ``` |
| To | ``` case points ``` |

Modified [MDLGeometryType.quads](https://developer.apple.com/documentation/modelio/mdlgeometrytype/quads)

|  | Declaration |
| --- | --- |
| From | ``` case TypeQuads ``` |
| To | ``` case quads ``` |

Modified [MDLGeometryType.triangles](https://developer.apple.com/documentation/modelio/mdlgeometrytype/triangles)

|  | Declaration |
| --- | --- |
| From | ``` case TypeTriangles ``` |
| To | ``` case triangles ``` |

Modified [MDLGeometryType.triangleStrips](https://developer.apple.com/documentation/modelio/mdlgeometrytype/trianglestrips)

|  | Declaration |
| --- | --- |
| From | ``` case TypeTriangleStrips ``` |
| To | ``` case triangleStrips ``` |

Modified [MDLGeometryType.variableTopology](https://developer.apple.com/documentation/modelio/mdlgeometrytype/variabletopology)

|  | Declaration |
| --- | --- |
| From | ``` case TypeVariableTopology ``` |
| To | ``` case variableTopology ``` |

Modified [MDLIndexBitDepth [enum]](https://developer.apple.com/documentation/modelio/mdlindexbitdepth)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLIndexBitDepth : UInt {     case Invalid     case UInt8     static var Uint8: MDLIndexBitDepth { get }     case UInt16     static var Uint16: MDLIndexBitDepth { get }     case UInt32     static var Uint32: MDLIndexBitDepth { get } } ``` |
| To | ``` enum MDLIndexBitDepth : UInt {     case invalid     case uInt8     static var uint8: MDLIndexBitDepth { get }     case uInt16     static var uint16: MDLIndexBitDepth { get }     case uInt32     static var uint32: MDLIndexBitDepth { get } } ``` |

Modified [MDLIndexBitDepth.invalid](https://developer.apple.com/documentation/modelio/mdlindexbitdepth/mdlindexbitdepthinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [MDLIndexBitDepth.uint16](https://developer.apple.com/documentation/modelio/mdlindexbitdepth/mdlindexbitdepthuint16-emu)

|  | Declaration |
| --- | --- |
| From | ``` static var Uint16: MDLIndexBitDepth { get } ``` |
| To | ``` static var uint16: MDLIndexBitDepth { get } ``` |

Modified [MDLIndexBitDepth.uInt16](https://developer.apple.com/documentation/modelio/mdlindexbitdepth/mdlindexbitdepthuint16)

|  | Declaration |
| --- | --- |
| From | ``` case UInt16 ``` |
| To | ``` case uInt16 ``` |

Modified [MDLIndexBitDepth.uint32](https://developer.apple.com/documentation/modelio/mdlindexbitdepth/1391790-uint32)

|  | Declaration |
| --- | --- |
| From | ``` static var Uint32: MDLIndexBitDepth { get } ``` |
| To | ``` static var uint32: MDLIndexBitDepth { get } ``` |

Modified [MDLIndexBitDepth.uInt32](https://developer.apple.com/documentation/modelio/mdlindexbitdepth/uint32)

|  | Declaration |
| --- | --- |
| From | ``` case UInt32 ``` |
| To | ``` case uInt32 ``` |

Modified [MDLIndexBitDepth.uint8](https://developer.apple.com/documentation/modelio/mdlindexbitdepth/1391324-uint8)

|  | Declaration |
| --- | --- |
| From | ``` static var Uint8: MDLIndexBitDepth { get } ``` |
| To | ``` static var uint8: MDLIndexBitDepth { get } ``` |

Modified [MDLIndexBitDepth.uInt8](https://developer.apple.com/documentation/modelio/mdlindexbitdepth/uint8)

|  | Declaration |
| --- | --- |
| From | ``` case UInt8 ``` |
| To | ``` case uInt8 ``` |

Modified [MDLLight](https://developer.apple.com/documentation/modelio/mdllight)

|  | Declaration |
| --- | --- |
| From | ``` class MDLLight : MDLObject {     func irradianceAtPoint(_ point: vector_float3) -> Unmanaged<CGColor>     func irradianceAtPoint(_ point: vector_float3, colorSpace colorSpace: CGColorSpace) -> Unmanaged<CGColor>     var lightType: MDLLightType } extension MDLLight {     convenience init(SCNLight scnLight: SCNLight)     class func lightWithSCNLight(_ scnLight: SCNLight) -> Self } ``` |
| To | ``` class MDLLight : MDLObject {     func irradiance(atPoint point: vector_float3) -> Unmanaged<CGColor>     func irradiance(atPoint point: vector_float3, colorSpace colorSpace: CGColorSpace) -> Unmanaged<CGColor>     var lightType: MDLLightType     var colorSpace: String } extension MDLLight {     convenience init(scnLight scnLight: SCNLight)     class func withSCNLight(_ scnLight: SCNLight) -> Self } ``` |

Modified [MDLLight.irradiance(atPoint: vector_float3) -> Unmanaged<CGColor>](https://developer.apple.com/documentation/modelio/mdllight/1391254-irradianceatpoint)

|  | Declaration |
| --- | --- |
| From | ``` func irradianceAtPoint(_ point: vector_float3) -> Unmanaged<CGColor> ``` |
| To | ``` func irradiance(atPoint point: vector_float3) -> Unmanaged<CGColor> ``` |

Modified [MDLLight.irradiance(atPoint: vector_float3, colorSpace: CGColorSpace) -> Unmanaged<CGColor>](https://developer.apple.com/documentation/modelio/mdllight/1392005-irradiance)

|  | Declaration |
| --- | --- |
| From | ``` func irradianceAtPoint(_ point: vector_float3, colorSpace colorSpace: CGColorSpace) -> Unmanaged<CGColor> ``` |
| To | ``` func irradiance(atPoint point: vector_float3, colorSpace colorSpace: CGColorSpace) -> Unmanaged<CGColor> ``` |

Modified [MDLLightProbe](https://developer.apple.com/documentation/modelio/mdllightprobe)

|  | Declaration |
| --- | --- |
| From | ``` class MDLLightProbe : MDLLight {     init(reflectiveTexture reflectiveTexture: MDLTexture?, irradianceTexture irradianceTexture: MDLTexture?)     func generateSphericalHarmonicsFromIrradiance(_ sphericalHarmonicsLevel: Int)     var reflectiveTexture: MDLTexture? { get }     var irradianceTexture: MDLTexture? { get }     var sphericalHarmonicsLevel: Int { get }     @NSCopying var sphericalHarmonicsCoefficients: NSData? { get } } extension MDLLightProbe {      init?(textureSize textureSize: Int, forLocation transform: MDLTransform, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], reflectiveCubemap reflectiveCubemap: MDLTexture?, irradianceCubemap irradianceCubemap: MDLTexture?)     class func lightProbeWithTextureSize(_ textureSize: Int, forLocation transform: MDLTransform, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], reflectiveCubemap reflectiveCubemap: MDLTexture?, irradianceCubemap irradianceCubemap: MDLTexture?) -> MDLLightProbe? } ``` |
| To | ``` class MDLLightProbe : MDLLight {     init(reflectiveTexture reflectiveTexture: MDLTexture?, irradianceTexture irradianceTexture: MDLTexture?)     func generateSphericalHarmonics(fromIrradiance sphericalHarmonicsLevel: Int)     var reflectiveTexture: MDLTexture? { get }     var irradianceTexture: MDLTexture? { get }     var sphericalHarmonicsLevel: Int { get }     var sphericalHarmonicsCoefficients: Data? { get }      init?(textureSize textureSize: Int, forLocation transform: MDLTransform, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], reflectiveCubemap reflectiveCubemap: MDLTexture?, irradianceCubemap irradianceCubemap: MDLTexture?)     class func withTextureSize(_ textureSize: Int, forLocation transform: MDLTransform, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], reflectiveCubemap reflectiveCubemap: MDLTexture?, irradianceCubemap irradianceCubemap: MDLTexture?) -> MDLLightProbe? } extension MDLLightProbe {      init?(textureSize textureSize: Int, forLocation transform: MDLTransform, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], reflectiveCubemap reflectiveCubemap: MDLTexture?, irradianceCubemap irradianceCubemap: MDLTexture?)     class func withTextureSize(_ textureSize: Int, forLocation transform: MDLTransform, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], reflectiveCubemap reflectiveCubemap: MDLTexture?, irradianceCubemap irradianceCubemap: MDLTexture?) -> MDLLightProbe? } ``` |

Modified [MDLLightProbe.generateSphericalHarmonics(fromIrradiance: Int)](https://developer.apple.com/documentation/modelio/mdllightprobe/1391579-generatesphericalharmonicsfromir)

|  | Declaration |
| --- | --- |
| From | ``` func generateSphericalHarmonicsFromIrradiance(_ sphericalHarmonicsLevel: Int) ``` |
| To | ``` func generateSphericalHarmonics(fromIrradiance sphericalHarmonicsLevel: Int) ``` |

Modified [MDLLightProbe.sphericalHarmonicsCoefficients](https://developer.apple.com/documentation/modelio/mdllightprobe/1390927-sphericalharmonicscoefficients)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sphericalHarmonicsCoefficients: NSData? { get } ``` |
| To | ``` var sphericalHarmonicsCoefficients: Data? { get } ``` |

Modified [MDLLightType [enum]](https://developer.apple.com/documentation/modelio/mdllighttype)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLLightType : UInt {     case Unknown     case Ambient     case Directional     case Spot     case Point     case Linear     case DiscArea     case RectangularArea     case SuperElliptical     case Photometric     case Probe     case Environment } ``` |
| To | ``` enum MDLLightType : UInt {     case unknown     case ambient     case directional     case spot     case point     case linear     case discArea     case rectangularArea     case superElliptical     case photometric     case probe     case environment } ``` |

Modified [MDLLightType.ambient](https://developer.apple.com/documentation/modelio/mdllighttype/ambient)

|  | Declaration |
| --- | --- |
| From | ``` case Ambient ``` |
| To | ``` case ambient ``` |

Modified [MDLLightType.directional](https://developer.apple.com/documentation/modelio/mdllighttype/directional)

|  | Declaration |
| --- | --- |
| From | ``` case Directional ``` |
| To | ``` case directional ``` |

Modified [MDLLightType.discArea](https://developer.apple.com/documentation/modelio/mdllighttype/mdllighttypediscarea)

|  | Declaration |
| --- | --- |
| From | ``` case DiscArea ``` |
| To | ``` case discArea ``` |

Modified [MDLLightType.environment](https://developer.apple.com/documentation/modelio/mdllighttype/mdllighttypeenvironment)

|  | Declaration |
| --- | --- |
| From | ``` case Environment ``` |
| To | ``` case environment ``` |

Modified [MDLLightType.linear](https://developer.apple.com/documentation/modelio/mdllighttype/mdllighttypelinear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [MDLLightType.photometric](https://developer.apple.com/documentation/modelio/mdllighttype/mdllighttypephotometric)

|  | Declaration |
| --- | --- |
| From | ``` case Photometric ``` |
| To | ``` case photometric ``` |

Modified [MDLLightType.point](https://developer.apple.com/documentation/modelio/mdllighttype/point)

|  | Declaration |
| --- | --- |
| From | ``` case Point ``` |
| To | ``` case point ``` |

Modified [MDLLightType.probe](https://developer.apple.com/documentation/modelio/mdllighttype/mdllighttypeprobe)

|  | Declaration |
| --- | --- |
| From | ``` case Probe ``` |
| To | ``` case probe ``` |

Modified [MDLLightType.rectangularArea](https://developer.apple.com/documentation/modelio/mdllighttype/rectangulararea)

|  | Declaration |
| --- | --- |
| From | ``` case RectangularArea ``` |
| To | ``` case rectangularArea ``` |

Modified [MDLLightType.spot](https://developer.apple.com/documentation/modelio/mdllighttype/spot)

|  | Declaration |
| --- | --- |
| From | ``` case Spot ``` |
| To | ``` case spot ``` |

Modified [MDLLightType.superElliptical](https://developer.apple.com/documentation/modelio/mdllighttype/mdllighttypesuperelliptical)

|  | Declaration |
| --- | --- |
| From | ``` case SuperElliptical ``` |
| To | ``` case superElliptical ``` |

Modified [MDLLightType.unknown](https://developer.apple.com/documentation/modelio/mdllighttype/mdllighttypeunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [MDLMaterial](https://developer.apple.com/documentation/modelio/mdlmaterial)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLMaterial : NSObject, MDLNamed, NSFastEnumeration {     init(name name: String, scatteringFunction scatteringFunction: MDLScatteringFunction)     func setProperty(_ property: MDLMaterialProperty)     func removeProperty(_ property: MDLMaterialProperty)     func propertyNamed(_ name: String) -> MDLMaterialProperty?     func propertyWithSemantic(_ semantic: MDLMaterialSemantic) -> MDLMaterialProperty?     func removeAllProperties()     var scatteringFunction: MDLScatteringFunction { get }     var name: String     var baseMaterial: MDLMaterial?     subscript (_ idx: Int) -> MDLMaterialProperty? { get }     func objectAtIndexedSubscript(_ idx: Int) -> MDLMaterialProperty?     subscript (_ name: String) -> MDLMaterialProperty? { get }     func objectForKeyedSubscript(_ name: String) -> MDLMaterialProperty?     var count: Int { get } } extension MDLMaterial {     convenience init(SCNMaterial scnMaterial: SCNMaterial)     class func materialWithSCNMaterial(_ scnMaterial: SCNMaterial) -> Self } ``` | MDLNamed, NSFastEnumeration |
| To | ``` class MDLMaterial : NSObject, MDLNamed, NSFastEnumeration {     init(name name: String, scatteringFunction scatteringFunction: MDLScatteringFunction)     func setProperty(_ property: MDLMaterialProperty)     func remove(_ property: MDLMaterialProperty)     func propertyNamed(_ name: String) -> MDLMaterialProperty?     func property(with semantic: MDLMaterialSemantic) -> MDLMaterialProperty?     func removeAllProperties()     var scatteringFunction: MDLScatteringFunction { get }     var name: String     var base: MDLMaterial?     subscript(_ idx: Int) -> MDLMaterialProperty? { get }     func objectAtIndexedSubscript(_ idx: Int) -> MDLMaterialProperty?     subscript(_ name: String) -> MDLMaterialProperty? { get }     func objectForKeyedSubscript(_ name: String) -> MDLMaterialProperty?     var count: Int { get }     var materialFace: MDLMaterialFace     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLMaterial : CVarArg { } extension MDLMaterial : Equatable, Hashable {     var hashValue: Int { get } } extension MDLMaterial {     convenience init(scnMaterial scnMaterial: SCNMaterial)     class func withSCNMaterial(_ scnMaterial: SCNMaterial) -> Self } ``` | CVarArg, Equatable, Hashable, MDLNamed, NSFastEnumeration |

Modified [MDLMaterial.base](https://developer.apple.com/documentation/modelio/mdlmaterial/1391599-base)

|  | Declaration |
| --- | --- |
| From | ``` var baseMaterial: MDLMaterial? ``` |
| To | ``` var base: MDLMaterial? ``` |

Modified [MDLMaterial.property(with: MDLMaterialSemantic) -> MDLMaterialProperty?](https://developer.apple.com/documentation/modelio/mdlmaterial/1391900-propertywithsemantic)

|  | Declaration |
| --- | --- |
| From | ``` func propertyWithSemantic(_ semantic: MDLMaterialSemantic) -> MDLMaterialProperty? ``` |
| To | ``` func property(with semantic: MDLMaterialSemantic) -> MDLMaterialProperty? ``` |

Modified [MDLMaterial.remove(_: MDLMaterialProperty)](https://developer.apple.com/documentation/modelio/mdlmaterial/1391387-removeproperty)

|  | Declaration |
| --- | --- |
| From | ``` func removeProperty(_ property: MDLMaterialProperty) ``` |
| To | ``` func remove(_ property: MDLMaterialProperty) ``` |

Modified [MDLMaterial.subscript(_: String) -> MDLMaterialProperty?](https://developer.apple.com/documentation/modelio/mdlmaterial/1391012-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ name: String) -> MDLMaterialProperty? { get } ``` |
| To | ``` subscript(_ name: String) -> MDLMaterialProperty? { get } ``` |

Modified [MDLMaterial.subscript(_: Int) -> MDLMaterialProperty?](https://developer.apple.com/documentation/modelio/mdlmaterial/1391886-objectatindexedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ idx: Int) -> MDLMaterialProperty? { get } ``` |
| To | ``` subscript(_ idx: Int) -> MDLMaterialProperty? { get } ``` |

Modified [MDLMaterialMipMapFilterMode [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialmipmapfiltermode)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLMaterialMipMapFilterMode : UInt {     case Nearest     case Linear } ``` |
| To | ``` enum MDLMaterialMipMapFilterMode : UInt {     case nearest     case linear } ``` |

Modified [MDLMaterialMipMapFilterMode.linear](https://developer.apple.com/documentation/modelio/mdlmaterialmipmapfiltermode/linear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [MDLMaterialMipMapFilterMode.nearest](https://developer.apple.com/documentation/modelio/mdlmaterialmipmapfiltermode/nearest)

|  | Declaration |
| --- | --- |
| From | ``` case Nearest ``` |
| To | ``` case nearest ``` |

Modified [MDLMaterialProperty](https://developer.apple.com/documentation/modelio/mdlmaterialproperty)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLMaterialProperty : NSObject, MDLNamed {     convenience init()     init(name name: String, semantic semantic: MDLMaterialSemantic)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, float value: Float)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, float2 value: vector_float2)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, float3 value: vector_float3)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, float4 value: vector_float4)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, matrix4x4 value: matrix_float4x4)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, URL URL: NSURL?)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, string string: String?)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, textureSampler textureSampler: MDLTextureSampler?)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, color color: CGColor)     func setProperties(_ property: MDLMaterialProperty)     var semantic: MDLMaterialSemantic     var type: MDLMaterialPropertyType { get }     var name: String     var stringValue: String?     @NSCopying var URLValue: NSURL?     var textureSamplerValue: MDLTextureSampler?     var color: CGColor?     var floatValue: Float     var float2Value: vector_float2     var float3Value: vector_float3     var float4Value: vector_float4     var matrix4x4: matrix_float4x4 } ``` | MDLNamed |
| To | ``` class MDLMaterialProperty : NSObject, MDLNamed, NSCopying {     convenience init()     init(name name: String, semantic semantic: MDLMaterialSemantic)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, float value: Float)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, float2 value: vector_float2)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, float3 value: vector_float3)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, float4 value: vector_float4)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, matrix4x4 value: matrix_float4x4)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, url URL: URL?)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, string string: String?)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, textureSampler textureSampler: MDLTextureSampler?)     convenience init(name name: String, semantic semantic: MDLMaterialSemantic, color color: CGColor)     func setProperties(_ property: MDLMaterialProperty)     var semantic: MDLMaterialSemantic     var type: MDLMaterialPropertyType { get }     var name: String     var stringValue: String?     var urlValue: URL?     var textureSamplerValue: MDLTextureSampler?     var color: CGColor?     var floatValue: Float     var float2Value: vector_float2     var float3Value: vector_float3     var float4Value: vector_float4     var matrix4x4: matrix_float4x4     var luminance: Float     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLMaterialProperty : CVarArg { } extension MDLMaterialProperty : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLNamed, NSCopying |

Modified [MDLMaterialProperty.init(name: String, semantic: MDLMaterialSemantic, url: URL?)](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/1391247-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String, semantic semantic: MDLMaterialSemantic, URL URL: NSURL?) ``` |
| To | ``` convenience init(name name: String, semantic semantic: MDLMaterialSemantic, url URL: URL?) ``` |

Modified [MDLMaterialProperty.urlValue](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/1391644-urlvalue)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URLValue: NSURL? ``` |
| To | ``` var urlValue: URL? ``` |

Modified [MDLMaterialPropertyType [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLMaterialPropertyType : UInt {     case None     case String     case URL     case Texture     case Color     case Float     case Float2     case Float3     case Float4     case Matrix44 } ``` |
| To | ``` enum MDLMaterialPropertyType : UInt {     case none     case string     case URL     case texture     case color     case float     case float2     case float3     case float4     case matrix44 } ``` |

Modified [MDLMaterialPropertyType.color](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/mdlmaterialpropertytypecolor)

|  | Declaration |
| --- | --- |
| From | ``` case Color ``` |
| To | ``` case color ``` |

Modified [MDLMaterialPropertyType.float](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/float)

|  | Declaration |
| --- | --- |
| From | ``` case Float ``` |
| To | ``` case float ``` |

Modified [MDLMaterialPropertyType.float2](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/float2)

|  | Declaration |
| --- | --- |
| From | ``` case Float2 ``` |
| To | ``` case float2 ``` |

Modified [MDLMaterialPropertyType.float3](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/mdlmaterialpropertytypefloat3)

|  | Declaration |
| --- | --- |
| From | ``` case Float3 ``` |
| To | ``` case float3 ``` |

Modified [MDLMaterialPropertyType.float4](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/mdlmaterialpropertytypefloat4)

|  | Declaration |
| --- | --- |
| From | ``` case Float4 ``` |
| To | ``` case float4 ``` |

Modified [MDLMaterialPropertyType.matrix44](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/mdlmaterialpropertytypematrix44)

|  | Declaration |
| --- | --- |
| From | ``` case Matrix44 ``` |
| To | ``` case matrix44 ``` |

Modified [MDLMaterialPropertyType.none](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/mdlmaterialpropertytypenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MDLMaterialPropertyType.string](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/mdlmaterialpropertytypestring)

|  | Declaration |
| --- | --- |
| From | ``` case String ``` |
| To | ``` case string ``` |

Modified [MDLMaterialPropertyType.texture](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/mdlmaterialpropertytypetexture)

|  | Declaration |
| --- | --- |
| From | ``` case Texture ``` |
| To | ``` case texture ``` |

Modified [MDLMaterialSemantic [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLMaterialSemantic : UInt {     case BaseColor     case Subsurface     case Metallic     case Specular     case SpecularExponent     case SpecularTint     case Roughness     case Anisotropic     case AnisotropicRotation     case Sheen     case SheenTint     case Clearcoat     case ClearcoatGloss     case Emission     case Bump     case Opacity     case InterfaceIndexOfRefraction     case MaterialIndexOfRefraction     case ObjectSpaceNormal     case TangentSpaceNormal     case Displacement     case DisplacementScale     case AmbientOcclusion     case AmbientOcclusionScale     case None     case UserDefined } ``` |
| To | ``` enum MDLMaterialSemantic : UInt {     case baseColor     case subsurface     case metallic     case specular     case specularExponent     case specularTint     case roughness     case anisotropic     case anisotropicRotation     case sheen     case sheenTint     case clearcoat     case clearcoatGloss     case emission     case bump     case opacity     case interfaceIndexOfRefraction     case materialIndexOfRefraction     case objectSpaceNormal     case tangentSpaceNormal     case displacement     case displacementScale     case ambientOcclusion     case ambientOcclusionScale     case none     case userDefined } ``` |

Modified [MDLMaterialSemantic.ambientOcclusion](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticambientocclusion)

|  | Declaration |
| --- | --- |
| From | ``` case AmbientOcclusion ``` |
| To | ``` case ambientOcclusion ``` |

Modified [MDLMaterialSemantic.ambientOcclusionScale](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/ambientocclusionscale)

|  | Declaration |
| --- | --- |
| From | ``` case AmbientOcclusionScale ``` |
| To | ``` case ambientOcclusionScale ``` |

Modified [MDLMaterialSemantic.anisotropic](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/anisotropic)

|  | Declaration |
| --- | --- |
| From | ``` case Anisotropic ``` |
| To | ``` case anisotropic ``` |

Modified [MDLMaterialSemantic.anisotropicRotation](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticanisotropicrotation)

|  | Declaration |
| --- | --- |
| From | ``` case AnisotropicRotation ``` |
| To | ``` case anisotropicRotation ``` |

Modified [MDLMaterialSemantic.baseColor](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/basecolor)

|  | Declaration |
| --- | --- |
| From | ``` case BaseColor ``` |
| To | ``` case baseColor ``` |

Modified [MDLMaterialSemantic.bump](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/bump)

|  | Declaration |
| --- | --- |
| From | ``` case Bump ``` |
| To | ``` case bump ``` |

Modified [MDLMaterialSemantic.clearcoat](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticclearcoat)

|  | Declaration |
| --- | --- |
| From | ``` case Clearcoat ``` |
| To | ``` case clearcoat ``` |

Modified [MDLMaterialSemantic.clearcoatGloss](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/clearcoatgloss)

|  | Declaration |
| --- | --- |
| From | ``` case ClearcoatGloss ``` |
| To | ``` case clearcoatGloss ``` |

Modified [MDLMaterialSemantic.displacement](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/displacement)

|  | Declaration |
| --- | --- |
| From | ``` case Displacement ``` |
| To | ``` case displacement ``` |

Modified [MDLMaterialSemantic.displacementScale](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticdisplacementscale)

|  | Declaration |
| --- | --- |
| From | ``` case DisplacementScale ``` |
| To | ``` case displacementScale ``` |

Modified [MDLMaterialSemantic.emission](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticemission)

|  | Declaration |
| --- | --- |
| From | ``` case Emission ``` |
| To | ``` case emission ``` |

Modified [MDLMaterialSemantic.interfaceIndexOfRefraction](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticinterfaceindexofrefraction)

|  | Declaration |
| --- | --- |
| From | ``` case InterfaceIndexOfRefraction ``` |
| To | ``` case interfaceIndexOfRefraction ``` |

Modified [MDLMaterialSemantic.materialIndexOfRefraction](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/materialindexofrefraction)

|  | Declaration |
| --- | --- |
| From | ``` case MaterialIndexOfRefraction ``` |
| To | ``` case materialIndexOfRefraction ``` |

Modified [MDLMaterialSemantic.metallic](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/metallic)

|  | Declaration |
| --- | --- |
| From | ``` case Metallic ``` |
| To | ``` case metallic ``` |

Modified [MDLMaterialSemantic.none](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MDLMaterialSemantic.objectSpaceNormal](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/objectspacenormal)

|  | Declaration |
| --- | --- |
| From | ``` case ObjectSpaceNormal ``` |
| To | ``` case objectSpaceNormal ``` |

Modified [MDLMaterialSemantic.opacity](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticopacity)

|  | Declaration |
| --- | --- |
| From | ``` case Opacity ``` |
| To | ``` case opacity ``` |

Modified [MDLMaterialSemantic.roughness](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/roughness)

|  | Declaration |
| --- | --- |
| From | ``` case Roughness ``` |
| To | ``` case roughness ``` |

Modified [MDLMaterialSemantic.sheen](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticsheen)

|  | Declaration |
| --- | --- |
| From | ``` case Sheen ``` |
| To | ``` case sheen ``` |

Modified [MDLMaterialSemantic.sheenTint](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticsheentint)

|  | Declaration |
| --- | --- |
| From | ``` case SheenTint ``` |
| To | ``` case sheenTint ``` |

Modified [MDLMaterialSemantic.specular](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/specular)

|  | Declaration |
| --- | --- |
| From | ``` case Specular ``` |
| To | ``` case specular ``` |

Modified [MDLMaterialSemantic.specularExponent](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticspecularexponent)

|  | Declaration |
| --- | --- |
| From | ``` case SpecularExponent ``` |
| To | ``` case specularExponent ``` |

Modified [MDLMaterialSemantic.specularTint](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticspeculartint)

|  | Declaration |
| --- | --- |
| From | ``` case SpecularTint ``` |
| To | ``` case specularTint ``` |

Modified [MDLMaterialSemantic.subsurface](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/subsurface)

|  | Declaration |
| --- | --- |
| From | ``` case Subsurface ``` |
| To | ``` case subsurface ``` |

Modified [MDLMaterialSemantic.tangentSpaceNormal](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/tangentspacenormal)

|  | Declaration |
| --- | --- |
| From | ``` case TangentSpaceNormal ``` |
| To | ``` case tangentSpaceNormal ``` |

Modified [MDLMaterialSemantic.userDefined](https://developer.apple.com/documentation/modelio/mdlmaterialsemantic/mdlmaterialsemanticuserdefined)

|  | Declaration |
| --- | --- |
| From | ``` case UserDefined ``` |
| To | ``` case userDefined ``` |

Modified [MDLMaterialTextureFilterMode [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialtexturefiltermode)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLMaterialTextureFilterMode : UInt {     case Nearest     case Linear } ``` |
| To | ``` enum MDLMaterialTextureFilterMode : UInt {     case nearest     case linear } ``` |

Modified [MDLMaterialTextureFilterMode.linear](https://developer.apple.com/documentation/modelio/mdlmaterialtexturefiltermode/mdlmaterialtexturefiltermodelinear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [MDLMaterialTextureFilterMode.nearest](https://developer.apple.com/documentation/modelio/mdlmaterialtexturefiltermode/mdlmaterialtexturefiltermodenearest)

|  | Declaration |
| --- | --- |
| From | ``` case Nearest ``` |
| To | ``` case nearest ``` |

Modified [MDLMaterialTextureWrapMode [enum]](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLMaterialTextureWrapMode : UInt {     case Clamp     case Repeat     case Mirror } ``` |
| To | ``` enum MDLMaterialTextureWrapMode : UInt {     case clamp     case `repeat`     case mirror } ``` |

Modified [MDLMaterialTextureWrapMode.clamp](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode/mdlmaterialtexturewrapmodeclamp)

|  | Declaration |
| --- | --- |
| From | ``` case Clamp ``` |
| To | ``` case clamp ``` |

Modified [MDLMaterialTextureWrapMode.mirror](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode/mirror)

|  | Declaration |
| --- | --- |
| From | ``` case Mirror ``` |
| To | ``` case mirror ``` |

Modified [MDLMaterialTextureWrapMode.repeat](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode/repeat)

|  | Declaration |
| --- | --- |
| From | ``` case Repeat ``` |
| To | ``` case `repeat` ``` |

Modified [MDLMesh](https://developer.apple.com/documentation/modelio/mdlmesh)

|  | Declaration |
| --- | --- |
| From | ``` class MDLMesh : MDLObject {     init(vertexBuffer vertexBuffer: MDLMeshBuffer, vertexCount vertexCount: Int, descriptor descriptor: MDLVertexDescriptor, submeshes submeshes: [MDLSubmesh])     init(vertexBuffers vertexBuffers: [MDLMeshBuffer], vertexCount vertexCount: Int, descriptor descriptor: MDLVertexDescriptor, submeshes submeshes: [MDLSubmesh])     func vertexAttributeDataForAttributeNamed(_ name: String) -> MDLVertexAttributeData?     var boundingBox: MDLAxisAlignedBoundingBox { get }     @NSCopying var vertexDescriptor: MDLVertexDescriptor     var vertexCount: Int { get }     var vertexBuffers: [MDLMeshBuffer] { get }     var submeshes: NSMutableArray { get } } extension MDLMesh {     func addAttributeWithName(_ name: String, format format: MDLVertexFormat)     func addNormalsWithAttributeNamed(_ attributeName: String?, creaseThreshold creaseThreshold: Float)     func addTangentBasisForTextureCoordinateAttributeNamed(_ textureCoordinateAttributeName: String, tangentAttributeNamed tangentAttributeName: String, bitangentAttributeNamed bitangentAttributeName: String?)     func addTangentBasisForTextureCoordinateAttributeNamed(_ textureCoordinateAttributeName: String, normalAttributeNamed normalAttributeName: String, tangentAttributeNamed tangentAttributeName: String)     func makeVerticesUnique() } extension MDLMesh {     class func newEllipsoidWithRadii(_ radii: vector_float3, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, hemisphere hemisphere: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newCylinderWithHeight(_ height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newEllipticalConeWithHeight(_ height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newIcosahedronWithRadius(_ radius: Float, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newSubdividedMesh(_ mesh: MDLMesh, submeshIndex submeshIndex: Int, subdivisionLevels subdivisionLevels: Int) -> Self? } extension MDLMesh {     func generateAmbientOcclusionTextureWithSize(_ textureSize: vector_int2, raysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionTextureWithQuality(_ bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionVertexColorsWithRaysPerSample(_ raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateAmbientOcclusionVertexColorsWithQuality(_ bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateLightMapTextureWithTextureSize(_ textureSize: vector_int2, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapTextureWithQuality(_ bakeQuality: Float, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapVertexColorsWithLightsToConsider(_ lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool } extension MDLMesh {     convenience init(SCNGeometry scnGeometry: SCNGeometry)     class func meshWithSCNGeometry(_ scnGeometry: SCNGeometry) -> Self } ``` |
| To | ``` class MDLMesh : MDLObject {     init(bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     init(vertexBuffer vertexBuffer: MDLMeshBuffer, vertexCount vertexCount: Int, descriptor descriptor: MDLVertexDescriptor, submeshes submeshes: [MDLSubmesh])     init(vertexBuffers vertexBuffers: [MDLMeshBuffer], vertexCount vertexCount: Int, descriptor descriptor: MDLVertexDescriptor, submeshes submeshes: [MDLSubmesh])     func vertexAttributeData(forAttributeNamed name: String) -> MDLVertexAttributeData?     func vertexAttributeData(forAttributeNamed name: String, as format: MDLVertexFormat) -> MDLVertexAttributeData?     var boundingBox: MDLAxisAlignedBoundingBox { get }     @NSCopying var vertexDescriptor: MDLVertexDescriptor     var vertexCount: Int     var vertexBuffers: [MDLMeshBuffer] { get }     @NSCopying var submeshes: NSMutableArray?     var allocator: MDLMeshBufferAllocator { get }     func generateAmbientOcclusionTexture(withSize textureSize: vector_int2, raysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionTexture(withQuality bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionVertexColors(withRaysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateAmbientOcclusionVertexColors(withQuality bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateLightMapTexture(withTextureSize textureSize: vector_int2, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapTexture(withQuality bakeQuality: Float, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapVertexColorsWithLights(toConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     init(boxWithExtent extent: vector_float3, segments segments: vector_uint3, inwardNormals inwardNormals: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(sphereWithExtent extent: vector_float3, segments segments: vector_uint2, inwardNormals inwardNormals: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(hemisphereWithExtent extent: vector_float3, segments segments: vector_uint2, inwardNormals inwardNormals: Bool, cap cap: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(cylinderWithExtent extent: vector_float3, segments segments: vector_uint2, inwardNormals inwardNormals: Bool, topCap topCap: Bool, bottomCap bottomCap: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(capsuleWithExtent extent: vector_float3, cylinderSegments segments: vector_uint2, hemisphereSegments hemisphereSegments: Int32, inwardNormals inwardNormals: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(coneWithExtent extent: vector_float3, segments segments: vector_uint2, inwardNormals inwardNormals: Bool, cap cap: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(planeWithExtent extent: vector_float3, segments segments: vector_uint2, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(icosahedronWithExtent extent: vector_float3, inwardNormals inwardNormals: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(meshBySubdividingMesh mesh: MDLMesh, submeshIndex submeshIndex: Int32, subdivisionLevels subdivisionLevels: UInt32, allocator allocator: MDLMeshBufferAllocator?)     class func newBox(withDimensions dimensions: vector_float3, segments segments: vector_uint3, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newEllipsoid(withRadii radii: vector_float3, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, hemisphere hemisphere: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newCylinder(withHeight height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newEllipticalCone(withHeight height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newPlane(withDimensions dimensions: vector_float2, segments segments: vector_uint2, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newIcosahedron(withRadius radius: Float, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newSubdividedMesh(_ mesh: MDLMesh, submeshIndex submeshIndex: Int, subdivisionLevels subdivisionLevels: Int) -> Self?     func addAttribute(withName name: String, format format: MDLVertexFormat)     func addAttribute(withName name: String, format format: MDLVertexFormat, type type: String, data data: Data, stride stride: Int)     func addAttribute(withName name: String, format format: MDLVertexFormat, type type: String, data data: Data, stride stride: Int, time time: TimeInterval)     func addNormals(withAttributeNamed attributeName: String?, creaseThreshold creaseThreshold: Float)     func addTangentBasis(forTextureCoordinateAttributeNamed textureCoordinateAttributeName: String, tangentAttributeNamed tangentAttributeNamed: String, bitangentAttributeNamed bitangentAttributeName: String?)     func addTangentBasis(forTextureCoordinateAttributeNamed textureCoordinateAttributeName: String, normalAttributeNamed normalAttributeNamed: String, tangentAttributeNamed tangentAttributeNamed: String)     func addUnwrappedTextureCoordinates(forAttributeNamed textureCoordinateAttributeName: String)     func makeVerticesUnique()     func replaceAttributeNamed(_ name: String, with newData: MDLVertexAttributeData)     func updateAttributeNamed(_ name: String, with newData: MDLVertexAttributeData)     func removeAttributeNamed(_ name: String) } extension MDLMesh {     func addAttribute(withName name: String, format format: MDLVertexFormat)     func addAttribute(withName name: String, format format: MDLVertexFormat, type type: String, data data: Data, stride stride: Int)     func addAttribute(withName name: String, format format: MDLVertexFormat, type type: String, data data: Data, stride stride: Int, time time: TimeInterval)     func addNormals(withAttributeNamed attributeName: String?, creaseThreshold creaseThreshold: Float)     func addTangentBasis(forTextureCoordinateAttributeNamed textureCoordinateAttributeName: String, tangentAttributeNamed tangentAttributeNamed: String, bitangentAttributeNamed bitangentAttributeName: String?)     func addTangentBasis(forTextureCoordinateAttributeNamed textureCoordinateAttributeName: String, normalAttributeNamed normalAttributeNamed: String, tangentAttributeNamed tangentAttributeNamed: String)     func addUnwrappedTextureCoordinates(forAttributeNamed textureCoordinateAttributeName: String)     func makeVerticesUnique()     func replaceAttributeNamed(_ name: String, with newData: MDLVertexAttributeData)     func updateAttributeNamed(_ name: String, with newData: MDLVertexAttributeData)     func removeAttributeNamed(_ name: String) } extension MDLMesh {     init(boxWithExtent extent: vector_float3, segments segments: vector_uint3, inwardNormals inwardNormals: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(sphereWithExtent extent: vector_float3, segments segments: vector_uint2, inwardNormals inwardNormals: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(hemisphereWithExtent extent: vector_float3, segments segments: vector_uint2, inwardNormals inwardNormals: Bool, cap cap: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(cylinderWithExtent extent: vector_float3, segments segments: vector_uint2, inwardNormals inwardNormals: Bool, topCap topCap: Bool, bottomCap bottomCap: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(capsuleWithExtent extent: vector_float3, cylinderSegments segments: vector_uint2, hemisphereSegments hemisphereSegments: Int32, inwardNormals inwardNormals: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(coneWithExtent extent: vector_float3, segments segments: vector_uint2, inwardNormals inwardNormals: Bool, cap cap: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(planeWithExtent extent: vector_float3, segments segments: vector_uint2, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(icosahedronWithExtent extent: vector_float3, inwardNormals inwardNormals: Bool, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?)     init(meshBySubdividingMesh mesh: MDLMesh, submeshIndex submeshIndex: Int32, subdivisionLevels subdivisionLevels: UInt32, allocator allocator: MDLMeshBufferAllocator?)     class func newBox(withDimensions dimensions: vector_float3, segments segments: vector_uint3, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newEllipsoid(withRadii radii: vector_float3, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, hemisphere hemisphere: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newCylinder(withHeight height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newEllipticalCone(withHeight height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newPlane(withDimensions dimensions: vector_float2, segments segments: vector_uint2, geometryType geometryType: MDLGeometryType, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newIcosahedron(withRadius radius: Float, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self     class func newSubdividedMesh(_ mesh: MDLMesh, submeshIndex submeshIndex: Int, subdivisionLevels subdivisionLevels: Int) -> Self? } extension MDLMesh {     func generateAmbientOcclusionTexture(withSize textureSize: vector_int2, raysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionTexture(withQuality bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateAmbientOcclusionVertexColors(withRaysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateAmbientOcclusionVertexColors(withQuality bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool     func generateLightMapTexture(withTextureSize textureSize: vector_int2, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapTexture(withQuality bakeQuality: Float, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool     func generateLightMapVertexColorsWithLights(toConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool } extension MDLMesh {     convenience init(scnGeometry scnGeometry: SCNGeometry)     class func withSCNGeometry(_ scnGeometry: SCNGeometry) -> Self     convenience init(scnGeometry scnGeometry: SCNGeometry, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     class func withSCNGeometry(_ scnGeometry: SCNGeometry, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?) -> Self } ``` |

Modified [MDLMesh.addAttribute(withName: String, format: MDLVertexFormat)](https://developer.apple.com/documentation/modelio/mdlmesh/1391701-addattributewithname)

|  | Declaration |
| --- | --- |
| From | ``` func addAttributeWithName(_ name: String, format format: MDLVertexFormat) ``` |
| To | ``` func addAttribute(withName name: String, format format: MDLVertexFormat) ``` |

Modified [MDLMesh.addNormals(withAttributeNamed: String?, creaseThreshold: Float)](https://developer.apple.com/documentation/modelio/mdlmesh/1391284-addnormalswithattributenamed)

|  | Declaration |
| --- | --- |
| From | ``` func addNormalsWithAttributeNamed(_ attributeName: String?, creaseThreshold creaseThreshold: Float) ``` |
| To | ``` func addNormals(withAttributeNamed attributeName: String?, creaseThreshold creaseThreshold: Float) ``` |

Modified [MDLMesh.addTangentBasis(forTextureCoordinateAttributeNamed: String, normalAttributeNamed: String, tangentAttributeNamed: String)](https://developer.apple.com/documentation/modelio/mdlmesh/1391237-addtangentbasisfortexturecoordin)

|  | Declaration |
| --- | --- |
| From | ``` func addTangentBasisForTextureCoordinateAttributeNamed(_ textureCoordinateAttributeName: String, normalAttributeNamed normalAttributeName: String, tangentAttributeNamed tangentAttributeName: String) ``` |
| To | ``` func addTangentBasis(forTextureCoordinateAttributeNamed textureCoordinateAttributeName: String, normalAttributeNamed normalAttributeNamed: String, tangentAttributeNamed tangentAttributeNamed: String) ``` |

Modified [MDLMesh.addTangentBasis(forTextureCoordinateAttributeNamed: String, tangentAttributeNamed: String, bitangentAttributeNamed: String?)](https://developer.apple.com/documentation/modelio/mdlmesh/1391942-addtangentbasis)

|  | Declaration |
| --- | --- |
| From | ``` func addTangentBasisForTextureCoordinateAttributeNamed(_ textureCoordinateAttributeName: String, tangentAttributeNamed tangentAttributeName: String, bitangentAttributeNamed bitangentAttributeName: String?) ``` |
| To | ``` func addTangentBasis(forTextureCoordinateAttributeNamed textureCoordinateAttributeName: String, tangentAttributeNamed tangentAttributeNamed: String, bitangentAttributeNamed bitangentAttributeName: String?) ``` |

Modified [MDLMesh.generateAmbientOcclusionTexture(withQuality: Float, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](https://developer.apple.com/documentation/modelio/mdlmesh/1391828-generateambientocclusiontexturew)

|  | Declaration |
| --- | --- |
| From | ``` func generateAmbientOcclusionTextureWithQuality(_ bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool ``` |
| To | ``` func generateAmbientOcclusionTexture(withQuality bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool ``` |

Modified [MDLMesh.generateAmbientOcclusionTexture(withSize: vector_int2, raysPerSample: Int, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](https://developer.apple.com/documentation/modelio/mdlmesh/1391857-generateambientocclusiontexture)

|  | Declaration |
| --- | --- |
| From | ``` func generateAmbientOcclusionTextureWithSize(_ textureSize: vector_int2, raysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool ``` |
| To | ``` func generateAmbientOcclusionTexture(withSize textureSize: vector_int2, raysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool ``` |

Modified [MDLMesh.generateAmbientOcclusionVertexColors(withQuality: Float, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](https://developer.apple.com/documentation/modelio/mdlmesh/1391004-generateambientocclusionvertexco)

|  | Declaration |
| --- | --- |
| From | ``` func generateAmbientOcclusionVertexColorsWithQuality(_ bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool ``` |
| To | ``` func generateAmbientOcclusionVertexColors(withQuality bakeQuality: Float, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool ``` |

Modified [MDLMesh.generateAmbientOcclusionVertexColors(withRaysPerSample: Int, attenuationFactor: Float, objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](https://developer.apple.com/documentation/modelio/mdlmesh/1390975-generateambientocclusionvertexco)

|  | Declaration |
| --- | --- |
| From | ``` func generateAmbientOcclusionVertexColorsWithRaysPerSample(_ raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool ``` |
| To | ``` func generateAmbientOcclusionVertexColors(withRaysPerSample raysPerSample: Int, attenuationFactor attenuationFactor: Float, objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool ``` |

Modified [MDLMesh.generateLightMapTexture(withQuality: Float, lightsToConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](https://developer.apple.com/documentation/modelio/mdlmesh/1391235-generatelightmaptexturewithquali)

|  | Declaration |
| --- | --- |
| From | ``` func generateLightMapTextureWithQuality(_ bakeQuality: Float, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool ``` |
| To | ``` func generateLightMapTexture(withQuality bakeQuality: Float, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool ``` |

Modified [MDLMesh.generateLightMapTexture(withTextureSize: vector_int2, lightsToConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String, materialPropertyNamed: String) -> Bool](https://developer.apple.com/documentation/modelio/mdlmesh/1392011-generatelightmaptexture)

|  | Declaration |
| --- | --- |
| From | ``` func generateLightMapTextureWithTextureSize(_ textureSize: vector_int2, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool ``` |
| To | ``` func generateLightMapTexture(withTextureSize textureSize: vector_int2, lightsToConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String, materialPropertyNamed materialPropertyName: String) -> Bool ``` |

Modified [MDLMesh.generateLightMapVertexColorsWithLights(toConsider: [MDLLight], objectsToConsider: [MDLObject], vertexAttributeNamed: String) -> Bool](https://developer.apple.com/documentation/modelio/mdlmesh/1391059-generatelightmapvertexcolorswith)

|  | Declaration |
| --- | --- |
| From | ``` func generateLightMapVertexColorsWithLightsToConsider(_ lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool ``` |
| To | ``` func generateLightMapVertexColorsWithLights(toConsider lightsToConsider: [MDLLight], objectsToConsider objectsToConsider: [MDLObject], vertexAttributeNamed vertexAttributeName: String) -> Bool ``` |

Modified [MDLMesh.newCylinder(withHeight: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: MDLMeshBufferAllocator?) -> Self [class]](https://developer.apple.com/documentation/modelio/mdlmesh/1391807-newcylinderwithheight)

|  | Declaration |
| --- | --- |
| From | ``` class func newCylinderWithHeight(_ height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self ``` |
| To | ``` class func newCylinder(withHeight height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self ``` |

Modified [MDLMesh.newEllipsoid(withRadii: vector_float3, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, hemisphere: Bool, allocator: MDLMeshBufferAllocator?) -> Self [class]](https://developer.apple.com/documentation/modelio/mdlmesh/1391499-newellipsoidwithradii)

|  | Declaration |
| --- | --- |
| From | ``` class func newEllipsoidWithRadii(_ radii: vector_float3, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, hemisphere hemisphere: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self ``` |
| To | ``` class func newEllipsoid(withRadii radii: vector_float3, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, hemisphere hemisphere: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self ``` |

Modified [MDLMesh.newEllipticalCone(withHeight: Float, radii: vector_float2, radialSegments: Int, verticalSegments: Int, geometryType: MDLGeometryType, inwardNormals: Bool, allocator: MDLMeshBufferAllocator?) -> Self [class]](https://developer.apple.com/documentation/modelio/mdlmesh/1390925-newellipticalconewithheight)

|  | Declaration |
| --- | --- |
| From | ``` class func newEllipticalConeWithHeight(_ height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self ``` |
| To | ``` class func newEllipticalCone(withHeight height: Float, radii radii: vector_float2, radialSegments radialSegments: Int, verticalSegments verticalSegments: Int, geometryType geometryType: MDLGeometryType, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self ``` |

Modified [MDLMesh.newIcosahedron(withRadius: Float, inwardNormals: Bool, allocator: MDLMeshBufferAllocator?) -> Self [class]](https://developer.apple.com/documentation/modelio/mdlmesh/1391685-newicosahedronwithradius)

|  | Declaration |
| --- | --- |
| From | ``` class func newIcosahedronWithRadius(_ radius: Float, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self ``` |
| To | ``` class func newIcosahedron(withRadius radius: Float, inwardNormals inwardNormals: Bool, allocator allocator: MDLMeshBufferAllocator?) -> Self ``` |

Modified [MDLMesh.submeshes](https://developer.apple.com/documentation/modelio/mdlmesh/1390937-submeshes)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` var submeshes: NSMutableArray { get } ``` | yes |
| To | ``` @NSCopying var submeshes: NSMutableArray? ``` | -- |

Modified [MDLMesh.vertexAttributeData(forAttributeNamed: String) -> MDLVertexAttributeData?](https://developer.apple.com/documentation/modelio/mdlmesh/1391002-vertexattributedataforattributen)

|  | Declaration |
| --- | --- |
| From | ``` func vertexAttributeDataForAttributeNamed(_ name: String) -> MDLVertexAttributeData? ``` |
| To | ``` func vertexAttributeData(forAttributeNamed name: String) -> MDLVertexAttributeData? ``` |

Modified [MDLMesh.vertexCount](https://developer.apple.com/documentation/modelio/mdlmesh/1391411-vertexcount)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` var vertexCount: Int { get } ``` | yes |
| To | ``` var vertexCount: Int ``` | -- |

Modified [MDLMeshBuffer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer)

|  | Declaration |
| --- | --- |
| From | ``` protocol MDLMeshBuffer : NSObjectProtocol, NSCopying {     func fillData(_ data: NSData, offset offset: Int)     func map() -> MDLMeshBufferMap     var length: Int { get }     var allocator: MDLMeshBufferAllocator { get }     var type: MDLMeshBufferType { get } } ``` |
| To | ``` protocol MDLMeshBuffer : NSObjectProtocol, NSCopying {     func fill(_ data: Data, offset offset: Int)     func map() -> MDLMeshBufferMap     var length: Int { get }     var allocator: MDLMeshBufferAllocator { get }     var type: MDLMeshBufferType { get } } ``` |

Modified [MDLMeshBuffer.fill(_: Data, offset: Int)](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/1391979-filldata)

|  | Declaration |
| --- | --- |
| From | ``` func fillData(_ data: NSData, offset offset: Int) ``` |
| To | ``` func fill(_ data: Data, offset offset: Int) ``` |

Modified [MDLMeshBufferAllocator](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator)

|  | Declaration |
| --- | --- |
| From | ``` protocol MDLMeshBufferAllocator : NSObjectProtocol {     func newZone(_ capacity: Int) -> MDLMeshBufferZone     func newZoneForBuffersWithSize(_ sizes: [NSNumber], andType types: [NSNumber]) -> MDLMeshBufferZone     func newBuffer(_ length: Int, type type: MDLMeshBufferType) -> MDLMeshBuffer     func newBufferWithData(_ data: NSData, type type: MDLMeshBufferType) -> MDLMeshBuffer     func newBufferFromZone(_ zone: MDLMeshBufferZone?, length length: Int, type type: MDLMeshBufferType) -> MDLMeshBuffer?     func newBufferFromZone(_ zone: MDLMeshBufferZone?, data data: NSData, type type: MDLMeshBufferType) -> MDLMeshBuffer? } ``` |
| To | ``` protocol MDLMeshBufferAllocator : NSObjectProtocol {     func newZone(_ capacity: Int) -> MDLMeshBufferZone     func newZoneForBuffers(withSize sizes: [NSNumber], andType types: [NSNumber]) -> MDLMeshBufferZone     func newBuffer(_ length: Int, type type: MDLMeshBufferType) -> MDLMeshBuffer     func newBuffer(with data: Data, type type: MDLMeshBufferType) -> MDLMeshBuffer     func newBuffer(from zone: MDLMeshBufferZone?, length length: Int, type type: MDLMeshBufferType) -> MDLMeshBuffer?     func newBuffer(from zone: MDLMeshBufferZone?, data data: Data, type type: MDLMeshBufferType) -> MDLMeshBuffer? } ``` |

Modified [MDLMeshBufferAllocator.newBuffer(from: MDLMeshBufferZone?, data: Data, type: MDLMeshBufferType) -> MDLMeshBuffer?](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator/1391332-newbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferFromZone(_ zone: MDLMeshBufferZone?, data data: NSData, type type: MDLMeshBufferType) -> MDLMeshBuffer? ``` |
| To | ``` func newBuffer(from zone: MDLMeshBufferZone?, data data: Data, type type: MDLMeshBufferType) -> MDLMeshBuffer? ``` |

Modified [MDLMeshBufferAllocator.newBuffer(from: MDLMeshBufferZone?, length: Int, type: MDLMeshBufferType) -> MDLMeshBuffer?](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator/1391792-newbufferfromzone)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferFromZone(_ zone: MDLMeshBufferZone?, length length: Int, type type: MDLMeshBufferType) -> MDLMeshBuffer? ``` |
| To | ``` func newBuffer(from zone: MDLMeshBufferZone?, length length: Int, type type: MDLMeshBufferType) -> MDLMeshBuffer? ``` |

Modified [MDLMeshBufferAllocator.newBuffer(with: Data, type: MDLMeshBufferType) -> MDLMeshBuffer](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator/1392007-newbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferWithData(_ data: NSData, type type: MDLMeshBufferType) -> MDLMeshBuffer ``` |
| To | ``` func newBuffer(with data: Data, type type: MDLMeshBufferType) -> MDLMeshBuffer ``` |

Modified [MDLMeshBufferAllocator.newZoneForBuffers(withSize: [NSNumber], andType: [NSNumber]) -> MDLMeshBufferZone](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator/1391742-newzoneforbufferswithsize)

|  | Declaration |
| --- | --- |
| From | ``` func newZoneForBuffersWithSize(_ sizes: [NSNumber], andType types: [NSNumber]) -> MDLMeshBufferZone ``` |
| To | ``` func newZoneForBuffers(withSize sizes: [NSNumber], andType types: [NSNumber]) -> MDLMeshBufferZone ``` |

Modified [MDLMeshBufferData](https://developer.apple.com/documentation/modelio/mdlmeshbufferdata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLMeshBufferData : NSObject, MDLMeshBuffer {     init(type type: MDLMeshBufferType, length length: Int)     init(type type: MDLMeshBufferType, data data: NSData?)     var data: NSData { get } } ``` | MDLMeshBuffer |
| To | ``` class MDLMeshBufferData : NSObject, MDLMeshBuffer {     init(type type: MDLMeshBufferType, length length: Int)     init(type type: MDLMeshBufferType, data data: Data?)     var data: Data { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLMeshBufferData : CVarArg { } extension MDLMeshBufferData : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLMeshBuffer |

Modified [MDLMeshBufferData.data](https://developer.apple.com/documentation/modelio/mdlmeshbufferdata/1391880-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData { get } ``` |
| To | ``` var data: Data { get } ``` |

Modified [MDLMeshBufferData.init(type: MDLMeshBufferType, data: Data?)](https://developer.apple.com/documentation/modelio/mdlmeshbufferdata/1391127-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: MDLMeshBufferType, data data: NSData?) ``` |
| To | ``` init(type type: MDLMeshBufferType, data data: Data?) ``` |

Modified [MDLMeshBufferDataAllocator](https://developer.apple.com/documentation/modelio/mdlmeshbufferdataallocator)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLMeshBufferDataAllocator : NSObject, MDLMeshBufferAllocator { } ``` | MDLMeshBufferAllocator |
| To | ``` class MDLMeshBufferDataAllocator : NSObject, MDLMeshBufferAllocator {     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLMeshBufferDataAllocator : CVarArg { } extension MDLMeshBufferDataAllocator : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLMeshBufferAllocator |

Modified [MDLMeshBufferMap](https://developer.apple.com/documentation/modelio/mdlmeshbuffermap)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLMeshBufferMap : NSObject {     init(bytes bytes: UnsafeMutablePointer<Void>, deallocator deallocator: (() -> Void)?)     var bytes: UnsafeMutablePointer<Void> { get } } ``` | -- |
| To | ``` class MDLMeshBufferMap : NSObject {     init(bytes bytes: UnsafeMutableRawPointer, deallocator deallocator: (@escaping () -> Swift.Void)? = nil)     var bytes: UnsafeMutableRawPointer { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLMeshBufferMap : CVarArg { } extension MDLMeshBufferMap : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MDLMeshBufferMap.bytes](https://developer.apple.com/documentation/modelio/mdlmeshbuffermap/1391215-bytes)

|  | Declaration |
| --- | --- |
| From | ``` var bytes: UnsafeMutablePointer<Void> { get } ``` |
| To | ``` var bytes: UnsafeMutableRawPointer { get } ``` |

Modified [MDLMeshBufferMap.init(bytes: UnsafeMutableRawPointer, deallocator: ( () -> Swift.Void)?)](https://developer.apple.com/documentation/modelio/mdlmeshbuffermap/1391650-initwithbytes)

|  | Declaration |
| --- | --- |
| From | ``` init(bytes bytes: UnsafeMutablePointer<Void>, deallocator deallocator: (() -> Void)?) ``` |
| To | ``` init(bytes bytes: UnsafeMutableRawPointer, deallocator deallocator: (@escaping () -> Swift.Void)? = nil) ``` |

Modified [MDLMeshBufferType [enum]](https://developer.apple.com/documentation/modelio/mdlmeshbuffertype)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLMeshBufferType : UInt {     case Vertex     case Index } ``` |
| To | ``` enum MDLMeshBufferType : UInt {     case vertex     case index } ``` |

Modified [MDLMeshBufferType.index](https://developer.apple.com/documentation/modelio/mdlmeshbuffertype/index)

|  | Declaration |
| --- | --- |
| From | ``` case Index ``` |
| To | ``` case index ``` |

Modified [MDLMeshBufferType.vertex](https://developer.apple.com/documentation/modelio/mdlmeshbuffertype/vertex)

|  | Declaration |
| --- | --- |
| From | ``` case Vertex ``` |
| To | ``` case vertex ``` |

Modified [MDLMeshBufferZoneDefault](https://developer.apple.com/documentation/modelio/mdlmeshbufferzonedefault)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLMeshBufferZoneDefault : NSObject, MDLMeshBufferZone {     var capacity: Int { get }     var allocator: MDLMeshBufferAllocator { get } } ``` | MDLMeshBufferZone |
| To | ``` class MDLMeshBufferZoneDefault : NSObject, MDLMeshBufferZone {     var capacity: Int { get }     var allocator: MDLMeshBufferAllocator { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLMeshBufferZoneDefault : CVarArg { } extension MDLMeshBufferZoneDefault : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLMeshBufferZone |

Modified [MDLNormalMapTexture](https://developer.apple.com/documentation/modelio/mdlnormalmaptexture)

|  | Declaration |
| --- | --- |
| From | ``` class MDLNormalMapTexture : MDLTexture {     init(byGeneratingNormalMapWithTexture sourceTexture: MDLTexture, name name: String?, smoothness smoothness: Float, contrast contrast: Float) } ``` |
| To | ``` class MDLNormalMapTexture : MDLTexture {     init(byGeneratingNormalMapWith sourceTexture: MDLTexture, name name: String?, smoothness smoothness: Float, contrast contrast: Float) } ``` |

Modified [MDLNormalMapTexture.init(byGeneratingNormalMapWith: MDLTexture, name: String?, smoothness: Float, contrast: Float)](https://developer.apple.com/documentation/modelio/mdlnormalmaptexture/1391884-init)

|  | Declaration |
| --- | --- |
| From | ``` init(byGeneratingNormalMapWithTexture sourceTexture: MDLTexture, name name: String?, smoothness smoothness: Float, contrast contrast: Float) ``` |
| To | ``` init(byGeneratingNormalMapWith sourceTexture: MDLTexture, name name: String?, smoothness smoothness: Float, contrast contrast: Float) ``` |

Modified [MDLObject](https://developer.apple.com/documentation/modelio/mdlobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLObject : NSObject, MDLNamed {     func setComponent(_ component: MDLComponent, forProtocol protocol: Protocol)     func componentConformingToProtocol(_ protocol: Protocol) -> MDLComponent?     weak var parent: MDLObject?     var transform: MDLTransformComponent?     var children: MDLObjectContainerComponent     func addChild(_ child: MDLObject)     func boundingBoxAtTime(_ time: NSTimeInterval) -> MDLAxisAlignedBoundingBox } extension MDLObject {     convenience init(SCNNode scnNode: SCNNode)     class func objectWithSCNNode(_ scnNode: SCNNode) -> Self } ``` | MDLNamed |
| To | ``` class MDLObject : NSObject, MDLNamed {     func setComponent(_ component: MDLComponent, for protocol: Protocol)     func componentConforming(to protocol: Protocol) -> MDLComponent?     weak var parent: MDLObject?     var instance: MDLObject?     var path: String { get }     func atPath(_ path: String) -> MDLObject     var transform: MDLTransformComponent?     var children: MDLObjectContainerComponent     var hidden: Bool     func addChild(_ child: MDLObject)     func boundingBox(atTime time: TimeInterval) -> MDLAxisAlignedBoundingBox     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLObject : CVarArg { } extension MDLObject : Equatable, Hashable {     var hashValue: Int { get } } extension MDLObject {     convenience init(scnNode scnNode: SCNNode)     class func withSCNNode(_ scnNode: SCNNode) -> Self     convenience init(scnNode scnNode: SCNNode, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     class func withSCNNode(_ scnNode: SCNNode, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?) -> Self } ``` | CVarArg, Equatable, Hashable, MDLNamed |

Modified [MDLObject.boundingBox(atTime: TimeInterval) -> MDLAxisAlignedBoundingBox](https://developer.apple.com/documentation/modelio/mdlobject/1391020-boundingboxattime)

|  | Declaration |
| --- | --- |
| From | ``` func boundingBoxAtTime(_ time: NSTimeInterval) -> MDLAxisAlignedBoundingBox ``` |
| To | ``` func boundingBox(atTime time: TimeInterval) -> MDLAxisAlignedBoundingBox ``` |

Modified [MDLObject.componentConforming(to: Protocol) -> MDLComponent?](https://developer.apple.com/documentation/modelio/mdlobject/1391664-componentconforming)

|  | Declaration |
| --- | --- |
| From | ``` func componentConformingToProtocol(_ protocol: Protocol) -> MDLComponent? ``` |
| To | ``` func componentConforming(to protocol: Protocol) -> MDLComponent? ``` |

Modified [MDLObject.setComponent(_: MDLComponent, for: Protocol)](https://developer.apple.com/documentation/modelio/mdlobject/1391974-setcomponent)

|  | Declaration |
| --- | --- |
| From | ``` func setComponent(_ component: MDLComponent, forProtocol protocol: Protocol) ``` |
| To | ``` func setComponent(_ component: MDLComponent, for protocol: Protocol) ``` |

Modified [MDLObjectContainer](https://developer.apple.com/documentation/modelio/mdlobjectcontainer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLObjectContainer : NSObject, MDLObjectContainerComponent { } ``` | MDLObjectContainerComponent |
| To | ``` class MDLObjectContainer : NSObject, MDLObjectContainerComponent {     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLObjectContainer : CVarArg { } extension MDLObjectContainer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLObjectContainerComponent |

Modified [MDLObjectContainerComponent](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent)

|  | Declaration |
| --- | --- |
| From | ``` protocol MDLObjectContainerComponent : MDLComponent, NSFastEnumeration {     func addObject(_ object: MDLObject)     func removeObject(_ object: MDLObject)     var objects: [MDLObject] { get } } ``` |
| To | ``` protocol MDLObjectContainerComponent : MDLComponent, NSFastEnumeration {     func add(_ object: MDLObject)     func remove(_ object: MDLObject)     var objects: [MDLObject] { get } } ``` |

Modified [MDLObjectContainerComponent.add(_: MDLObject)](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent/1391683-add)

|  | Declaration |
| --- | --- |
| From | ``` func addObject(_ object: MDLObject) ``` |
| To | ``` func add(_ object: MDLObject) ``` |

Modified [MDLObjectContainerComponent.remove(_: MDLObject)](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent/1391437-removeobject)

|  | Declaration |
| --- | --- |
| From | ``` func removeObject(_ object: MDLObject) ``` |
| To | ``` func remove(_ object: MDLObject) ``` |

Modified [MDLPhotometricLight](https://developer.apple.com/documentation/modelio/mdlphotometriclight)

|  | Declaration |
| --- | --- |
| From | ``` class MDLPhotometricLight : MDLPhysicallyPlausibleLight {     init?(IESProfile URL: NSURL)     func generateSphericalHarmonicsFromLight(_ sphericalHarmonicsLevel: Int)     func generateCubemapFromLight(_ textureSize: Int)     var lightCubeMap: MDLTexture? { get }     var sphericalHarmonicsLevel: Int { get }     @NSCopying var sphericalHarmonicsCoefficients: NSData? { get } } ``` |
| To | ``` class MDLPhotometricLight : MDLPhysicallyPlausibleLight {     init?(iesProfile URL: URL)     func generateSphericalHarmonics(fromLight sphericalHarmonicsLevel: Int)     func generateCubemap(fromLight textureSize: Int)     var lightCubeMap: MDLTexture? { get }     var sphericalHarmonicsLevel: Int { get }     var sphericalHarmonicsCoefficients: Data? { get } } ``` |

Modified [MDLPhotometricLight.generateCubemap(fromLight: Int)](https://developer.apple.com/documentation/modelio/mdlphotometriclight/1391832-generatecubemapfromlight)

|  | Declaration |
| --- | --- |
| From | ``` func generateCubemapFromLight(_ textureSize: Int) ``` |
| To | ``` func generateCubemap(fromLight textureSize: Int) ``` |

Modified [MDLPhotometricLight.generateSphericalHarmonics(fromLight: Int)](https://developer.apple.com/documentation/modelio/mdlphotometriclight/1391583-generatesphericalharmonicsfromli)

|  | Declaration |
| --- | --- |
| From | ``` func generateSphericalHarmonicsFromLight(_ sphericalHarmonicsLevel: Int) ``` |
| To | ``` func generateSphericalHarmonics(fromLight sphericalHarmonicsLevel: Int) ``` |

Modified [MDLPhotometricLight.init(iesProfile: URL)](https://developer.apple.com/documentation/modelio/mdlphotometriclight/1391803-initwithiesprofile)

|  | Declaration |
| --- | --- |
| From | ``` init?(IESProfile URL: NSURL) ``` |
| To | ``` init?(iesProfile URL: URL) ``` |

Modified [MDLPhotometricLight.sphericalHarmonicsCoefficients](https://developer.apple.com/documentation/modelio/mdlphotometriclight/1390994-sphericalharmonicscoefficients)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sphericalHarmonicsCoefficients: NSData? { get } ``` |
| To | ``` var sphericalHarmonicsCoefficients: Data? { get } ``` |

Modified [MDLScatteringFunction](https://developer.apple.com/documentation/modelio/mdlscatteringfunction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLScatteringFunction : NSObject, MDLNamed {     var name: String     var baseColor: MDLMaterialProperty { get }     var emission: MDLMaterialProperty { get }     var specular: MDLMaterialProperty { get }     var materialIndexOfRefraction: MDLMaterialProperty { get }     var interfaceIndexOfRefraction: MDLMaterialProperty { get }     var normal: MDLMaterialProperty { get }     var ambientOcclusion: MDLMaterialProperty { get }     var ambientOcclusionScale: MDLMaterialProperty { get } } ``` | MDLNamed |
| To | ``` class MDLScatteringFunction : NSObject, MDLNamed {     var name: String     var baseColor: MDLMaterialProperty { get }     var emission: MDLMaterialProperty { get }     var specular: MDLMaterialProperty { get }     var materialIndexOfRefraction: MDLMaterialProperty { get }     var interfaceIndexOfRefraction: MDLMaterialProperty { get }     var normal: MDLMaterialProperty { get }     var ambientOcclusion: MDLMaterialProperty { get }     var ambientOcclusionScale: MDLMaterialProperty { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLScatteringFunction : CVarArg { } extension MDLScatteringFunction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLNamed |

Modified [MDLSkyCubeTexture](https://developer.apple.com/documentation/modelio/mdlskycubetexture)

|  | Declaration |
| --- | --- |
| From | ``` class MDLSkyCubeTexture : MDLTexture {     init(name name: String?, channelEncoding channelEncoding: MDLTextureChannelEncoding, textureDimensions textureDimensions: vector_int2, turbidity turbidity: Float, sunElevation sunElevation: Float, upperAtmosphereScattering upperAtmosphereScattering: Float, groundAlbedo groundAlbedo: Float)     func updateTexture()     var turbidity: Float     var sunElevation: Float     var upperAtmosphereScattering: Float     var groundAlbedo: Float     var horizonElevation: Float     var groundColor: CGColor?     var gamma: Float     var exposure: Float     var brightness: Float     var contrast: Float     var saturation: Float     var highDynamicRangeCompression: vector_float2 } ``` |
| To | ``` class MDLSkyCubeTexture : MDLTexture {     init(name name: String?, channelEncoding channelEncoding: MDLTextureChannelEncoding, textureDimensions textureDimensions: vector_int2, turbidity turbidity: Float, sunElevation sunElevation: Float, upperAtmosphereScattering upperAtmosphereScattering: Float, groundAlbedo groundAlbedo: Float)     func update()     var turbidity: Float     var sunElevation: Float     var upperAtmosphereScattering: Float     var groundAlbedo: Float     var horizonElevation: Float     var groundColor: CGColor?     var gamma: Float     var exposure: Float     var brightness: Float     var contrast: Float     var saturation: Float     var highDynamicRangeCompression: vector_float2 } ``` |

Modified [MDLSkyCubeTexture.update()](https://developer.apple.com/documentation/modelio/mdlskycubetexture/1391548-update)

|  | Declaration |
| --- | --- |
| From | ``` func updateTexture() ``` |
| To | ``` func update() ``` |

Modified [MDLSubmesh](https://developer.apple.com/documentation/modelio/mdlsubmesh)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLSubmesh : NSObject, MDLNamed {     init(name name: String, indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?)     init(indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?)     init(name name: String, indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?, topology topology: MDLSubmeshTopology?)     init?(MDLSubmesh submesh: MDLSubmesh, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType)     var indexBuffer: MDLMeshBuffer { get }     var indexCount: Int { get }     var indexType: MDLIndexBitDepth { get }     var geometryType: MDLGeometryType { get }     var material: MDLMaterial?     var topology: MDLSubmeshTopology? { get }     var name: String } extension MDLSubmesh {     convenience init(SCNGeometryElement scnGeometryElement: SCNGeometryElement)     class func submeshWithSCNGeometryElement(_ scnGeometryElement: SCNGeometryElement) -> Self } ``` | MDLNamed |
| To | ``` class MDLSubmesh : NSObject, MDLNamed {     init(name name: String, indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?)     init(indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?)     init(name name: String, indexBuffer indexBuffer: MDLMeshBuffer, indexCount indexCount: Int, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType, material material: MDLMaterial?, topology topology: MDLSubmeshTopology?)     init?(mdlSubmesh submesh: MDLSubmesh, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType)     var indexBuffer: MDLMeshBuffer { get }     func indexBuffer(asIndexType indexType: MDLIndexBitDepth) -> MDLMeshBuffer     var indexCount: Int { get }     var indexType: MDLIndexBitDepth { get }     var geometryType: MDLGeometryType { get }     var material: MDLMaterial?     var topology: MDLSubmeshTopology? { get }     var name: String     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLSubmesh : CVarArg { } extension MDLSubmesh : Equatable, Hashable {     var hashValue: Int { get } } extension MDLSubmesh {     convenience init(scnGeometryElement scnGeometryElement: SCNGeometryElement)     class func withSCNGeometryElement(_ scnGeometryElement: SCNGeometryElement) -> Self     convenience init(scnGeometryElement scnGeometryElement: SCNGeometryElement, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?)     class func withSCNGeometryElement(_ scnGeometryElement: SCNGeometryElement, bufferAllocator bufferAllocator: MDLMeshBufferAllocator?) -> Self } ``` | CVarArg, Equatable, Hashable, MDLNamed |

Modified [MDLSubmesh.init(mdlSubmesh: MDLSubmesh, indexType: MDLIndexBitDepth, geometryType: MDLGeometryType)](https://developer.apple.com/documentation/modelio/mdlsubmesh/1391889-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(MDLSubmesh submesh: MDLSubmesh, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType) ``` |
| To | ``` init?(mdlSubmesh submesh: MDLSubmesh, indexType indexType: MDLIndexBitDepth, geometryType geometryType: MDLGeometryType) ``` |

Modified [MDLSubmeshTopology](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLSubmeshTopology : NSObject {     var faceTopology: MDLMeshBuffer?     var faceCount: Int     var vertexCreaseIndices: MDLMeshBuffer?     var vertexCreases: MDLMeshBuffer?     var vertexCreaseCount: Int     var edgeCreaseIndices: MDLMeshBuffer?     var edgeCreases: MDLMeshBuffer?     var edgeCreaseCount: Int     var holes: MDLMeshBuffer?     var holeCount: Int } ``` | -- |
| To | ``` class MDLSubmeshTopology : NSObject {     var faceTopology: MDLMeshBuffer?     var faceCount: Int     var vertexCreaseIndices: MDLMeshBuffer?     var vertexCreases: MDLMeshBuffer?     var vertexCreaseCount: Int     var edgeCreaseIndices: MDLMeshBuffer?     var edgeCreases: MDLMeshBuffer?     var edgeCreaseCount: Int     var holes: MDLMeshBuffer?     var holeCount: Int     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLSubmeshTopology : CVarArg { } extension MDLSubmeshTopology : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MDLTexture](https://developer.apple.com/documentation/modelio/mdltexture)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLTexture : NSObject, MDLNamed {     convenience init?(named name: String)     class func textureNamed(_ name: String) -> Self?     convenience init?(named name: String, bundle bundleOrNil: NSBundle?)     class func textureNamed(_ name: String, bundle bundleOrNil: NSBundle?) -> Self?     convenience init?(cubeWithImagesNamed names: [String])     class func textureCubeWithImagesNamed(_ names: [String]) -> Self?     convenience init?(cubeWithImagesNamed names: [String], bundle bundleOrNil: NSBundle?)     class func textureCubeWithImagesNamed(_ names: [String], bundle bundleOrNil: NSBundle?) -> Self?     class func irradianceTextureCubeWithTexture(_ texture: MDLTexture, name name: String?, dimensions dimensions: vector_int2) -> Self     class func irradianceTextureCubeWithTexture(_ texture: MDLTexture, name name: String?, dimensions dimensions: vector_int2, roughness roughness: Float) -> Self     init(data pixelData: NSData?, topLeftOrigin topLeftOrigin: Bool, name name: String?, dimensions dimensions: vector_int2, rowStride rowStride: Int, channelCount channelCount: Int, channelEncoding channelEncoding: MDLTextureChannelEncoding, isCube isCube: Bool)     func writeToURL(_ URL: NSURL) -> Bool     func writeToURL(_ nsurl: NSURL, type type: CFString) -> Bool     func imageFromTexture() -> Unmanaged<CGImage>?     func texelDataWithTopLeftOrigin() -> NSData?     func texelDataWithBottomLeftOrigin() -> NSData?     func texelDataWithTopLeftOriginAtMipLevel(_ level: Int, create create: Bool) -> NSData?     func texelDataWithBottomLeftOriginAtMipLevel(_ level: Int, create create: Bool) -> NSData?     var dimensions: vector_int2 { get }     var rowStride: Int { get }     var channelCount: Int { get }     var mipLevelCount: Int { get }     var channelEncoding: MDLTextureChannelEncoding { get }     var isCube: Bool } ``` | MDLNamed |
| To | ``` class MDLTexture : NSObject, MDLNamed {     init()     convenience init?(named name: String)     class func textureNamed(_ name: String) -> Self?     convenience init?(named name: String, bundle bundleOrNil: Bundle?)     class func textureNamed(_ name: String, bundle bundleOrNil: Bundle?) -> Self?     convenience init?(cubeWithImagesNamed names: [String])     class func textureCube(withImagesNamed names: [String]) -> Self?     convenience init?(cubeWithImagesNamed names: [String], bundle bundleOrNil: Bundle?)     class func textureCube(withImagesNamed names: [String], bundle bundleOrNil: Bundle?) -> Self?     class func irradianceTextureCube(with texture: MDLTexture, name name: String?, dimensions dimensions: vector_int2) -> Self     class func irradianceTextureCube(with texture: MDLTexture, name name: String?, dimensions dimensions: vector_int2, roughness roughness: Float) -> Self     init(data pixelData: Data?, topLeftOrigin topLeftOrigin: Bool, name name: String?, dimensions dimensions: vector_int2, rowStride rowStride: Int, channelCount channelCount: Int, channelEncoding channelEncoding: MDLTextureChannelEncoding, isCube isCube: Bool)     func write(to URL: URL) -> Bool     func write(to nsurl: URL, type type: CFString) -> Bool     func imageFromTexture() -> Unmanaged<CGImage>?     func texelDataWithTopLeftOrigin() -> Data?     func texelDataWithBottomLeftOrigin() -> Data?     func texelDataWithTopLeftOrigin(atMipLevel level: Int, create create: Bool) -> Data?     func texelDataWithBottomLeftOrigin(atMipLevel level: Int, create create: Bool) -> Data?     var dimensions: vector_int2 { get }     var rowStride: Int { get }     var channelCount: Int { get }     var mipLevelCount: Int { get }     var channelEncoding: MDLTextureChannelEncoding { get }     var isCube: Bool     var hasAlphaValues: Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLTexture : CVarArg { } extension MDLTexture : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLNamed |

Modified [MDLTexture.init(cubeWithImagesNamed: [String], bundle: Bundle?)](https://developer.apple.com/documentation/modelio/mdltexture/1391418-texturecubewithimagesnamed)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(cubeWithImagesNamed names: [String], bundle bundleOrNil: NSBundle?) ``` |
| To | ``` convenience init?(cubeWithImagesNamed names: [String], bundle bundleOrNil: Bundle?) ``` |

Modified [MDLTexture.init(data: Data?, topLeftOrigin: Bool, name: String?, dimensions: vector_int2, rowStride: Int, channelCount: Int, channelEncoding: MDLTextureChannelEncoding, isCube: Bool)](https://developer.apple.com/documentation/modelio/mdltexture/1391913-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data pixelData: NSData?, topLeftOrigin topLeftOrigin: Bool, name name: String?, dimensions dimensions: vector_int2, rowStride rowStride: Int, channelCount channelCount: Int, channelEncoding channelEncoding: MDLTextureChannelEncoding, isCube isCube: Bool) ``` |
| To | ``` init(data pixelData: Data?, topLeftOrigin topLeftOrigin: Bool, name name: String?, dimensions dimensions: vector_int2, rowStride rowStride: Int, channelCount channelCount: Int, channelEncoding channelEncoding: MDLTextureChannelEncoding, isCube isCube: Bool) ``` |

Modified [MDLTexture.init(named: String, bundle: Bundle?)](https://developer.apple.com/documentation/modelio/mdltexture/1391166-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(named name: String, bundle bundleOrNil: NSBundle?) ``` |
| To | ``` convenience init?(named name: String, bundle bundleOrNil: Bundle?) ``` |

Modified [MDLTexture.irradianceTextureCube(with: MDLTexture, name: String?, dimensions: vector_int2) -> Self [class]](https://developer.apple.com/documentation/modelio/mdltexture/1391190-irradiancetexturecubewithtexture)

|  | Declaration |
| --- | --- |
| From | ``` class func irradianceTextureCubeWithTexture(_ texture: MDLTexture, name name: String?, dimensions dimensions: vector_int2) -> Self ``` |
| To | ``` class func irradianceTextureCube(with texture: MDLTexture, name name: String?, dimensions dimensions: vector_int2) -> Self ``` |

Modified [MDLTexture.irradianceTextureCube(with: MDLTexture, name: String?, dimensions: vector_int2, roughness: Float) -> Self [class]](https://developer.apple.com/documentation/modelio/mdltexture/1391909-irradiancetexturecube)

|  | Declaration |
| --- | --- |
| From | ``` class func irradianceTextureCubeWithTexture(_ texture: MDLTexture, name name: String?, dimensions dimensions: vector_int2, roughness roughness: Float) -> Self ``` |
| To | ``` class func irradianceTextureCube(with texture: MDLTexture, name name: String?, dimensions dimensions: vector_int2, roughness roughness: Float) -> Self ``` |

Modified [MDLTexture.texelDataWithBottomLeftOrigin() -> Data?](https://developer.apple.com/documentation/modelio/mdltexture/1391872-texeldatawithbottomleftorigin)

|  | Declaration |
| --- | --- |
| From | ``` func texelDataWithBottomLeftOrigin() -> NSData? ``` |
| To | ``` func texelDataWithBottomLeftOrigin() -> Data? ``` |

Modified [MDLTexture.texelDataWithBottomLeftOrigin(atMipLevel: Int, create: Bool) -> Data?](https://developer.apple.com/documentation/modelio/mdltexture/1391656-texeldatawithbottomleftoriginatm)

|  | Declaration |
| --- | --- |
| From | ``` func texelDataWithBottomLeftOriginAtMipLevel(_ level: Int, create create: Bool) -> NSData? ``` |
| To | ``` func texelDataWithBottomLeftOrigin(atMipLevel level: Int, create create: Bool) -> Data? ``` |

Modified [MDLTexture.texelDataWithTopLeftOrigin() -> Data?](https://developer.apple.com/documentation/modelio/mdltexture/1391666-texeldatawithtopleftorigin)

|  | Declaration |
| --- | --- |
| From | ``` func texelDataWithTopLeftOrigin() -> NSData? ``` |
| To | ``` func texelDataWithTopLeftOrigin() -> Data? ``` |

Modified [MDLTexture.texelDataWithTopLeftOrigin(atMipLevel: Int, create: Bool) -> Data?](https://developer.apple.com/documentation/modelio/mdltexture/1391845-texeldatawithtopleftoriginatmipl)

|  | Declaration |
| --- | --- |
| From | ``` func texelDataWithTopLeftOriginAtMipLevel(_ level: Int, create create: Bool) -> NSData? ``` |
| To | ``` func texelDataWithTopLeftOrigin(atMipLevel level: Int, create create: Bool) -> Data? ``` |

Modified [MDLTexture.write(to: URL) -> Bool](https://developer.apple.com/documentation/modelio/mdltexture/1391755-writetourl)

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ URL: NSURL) -> Bool ``` |
| To | ``` func write(to URL: URL) -> Bool ``` |

Modified [MDLTexture.write(to: URL, type: CFString) -> Bool](https://developer.apple.com/documentation/modelio/mdltexture/1391911-writetourl)

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ nsurl: NSURL, type type: CFString) -> Bool ``` |
| To | ``` func write(to nsurl: URL, type type: CFString) -> Bool ``` |

Modified [MDLTextureChannelEncoding [enum]](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLTextureChannelEncoding : Int {     case UInt8     static var Uint8: MDLTextureChannelEncoding { get }     case UInt16     static var Uint16: MDLTextureChannelEncoding { get }     case UInt24     static var Uint24: MDLTextureChannelEncoding { get }     case UInt32     static var Uint32: MDLTextureChannelEncoding { get }     case Float16     case Float32 } ``` |
| To | ``` enum MDLTextureChannelEncoding : Int {     case uInt8     static var uint8: MDLTextureChannelEncoding { get }     case uInt16     static var uint16: MDLTextureChannelEncoding { get }     case uInt24     static var uint24: MDLTextureChannelEncoding { get }     case uInt32     static var uint32: MDLTextureChannelEncoding { get }     case float16     case float32 } ``` |

Modified [MDLTextureChannelEncoding.float16](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/mdltexturechannelencodingfloat16)

|  | Declaration |
| --- | --- |
| From | ``` case Float16 ``` |
| To | ``` case float16 ``` |

Modified [MDLTextureChannelEncoding.float32](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/mdltexturechannelencodingfloat32)

|  | Declaration |
| --- | --- |
| From | ``` case Float32 ``` |
| To | ``` case float32 ``` |

Modified [MDLTextureChannelEncoding.uint16](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/mdltexturechannelencodinguint16)

|  | Declaration |
| --- | --- |
| From | ``` static var Uint16: MDLTextureChannelEncoding { get } ``` |
| To | ``` static var uint16: MDLTextureChannelEncoding { get } ``` |

Modified [MDLTextureChannelEncoding.uInt16](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/uint16)

|  | Declaration |
| --- | --- |
| From | ``` case UInt16 ``` |
| To | ``` case uInt16 ``` |

Modified [MDLTextureChannelEncoding.uint24](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/1391893-uint24)

|  | Declaration |
| --- | --- |
| From | ``` static var Uint24: MDLTextureChannelEncoding { get } ``` |
| To | ``` static var uint24: MDLTextureChannelEncoding { get } ``` |

Modified [MDLTextureChannelEncoding.uInt24](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/mdltexturechannelencodinguint24)

|  | Declaration |
| --- | --- |
| From | ``` case UInt24 ``` |
| To | ``` case uInt24 ``` |

Modified [MDLTextureChannelEncoding.uint32](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/mdltexturechannelencodinguint32-f6s)

|  | Declaration |
| --- | --- |
| From | ``` static var Uint32: MDLTextureChannelEncoding { get } ``` |
| To | ``` static var uint32: MDLTextureChannelEncoding { get } ``` |

Modified [MDLTextureChannelEncoding.uInt32](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/mdltexturechannelencodinguint32)

|  | Declaration |
| --- | --- |
| From | ``` case UInt32 ``` |
| To | ``` case uInt32 ``` |

Modified [MDLTextureChannelEncoding.uint8](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/1391045-uint8)

|  | Declaration |
| --- | --- |
| From | ``` static var Uint8: MDLTextureChannelEncoding { get } ``` |
| To | ``` static var uint8: MDLTextureChannelEncoding { get } ``` |

Modified [MDLTextureChannelEncoding.uInt8](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding/mdltexturechannelencodinguint8-eug)

|  | Declaration |
| --- | --- |
| From | ``` case UInt8 ``` |
| To | ``` case uInt8 ``` |

Modified [MDLTextureFilter](https://developer.apple.com/documentation/modelio/mdltexturefilter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLTextureFilter : NSObject {     var sWrapMode: MDLMaterialTextureWrapMode     var tWrapMode: MDLMaterialTextureWrapMode     var rWrapMode: MDLMaterialTextureWrapMode     var minFilter: MDLMaterialTextureFilterMode     var magFilter: MDLMaterialTextureFilterMode     var mipFilter: MDLMaterialMipMapFilterMode } ``` | -- |
| To | ``` class MDLTextureFilter : NSObject {     var sWrapMode: MDLMaterialTextureWrapMode     var tWrapMode: MDLMaterialTextureWrapMode     var rWrapMode: MDLMaterialTextureWrapMode     var minFilter: MDLMaterialTextureFilterMode     var magFilter: MDLMaterialTextureFilterMode     var mipFilter: MDLMaterialMipMapFilterMode     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLTextureFilter : CVarArg { } extension MDLTextureFilter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MDLTextureSampler](https://developer.apple.com/documentation/modelio/mdltexturesampler)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLTextureSampler : NSObject {     var texture: MDLTexture?     var hardwareFilter: MDLTextureFilter?     var transform: MDLTransform? } ``` | -- |
| To | ``` class MDLTextureSampler : NSObject {     var texture: MDLTexture?     var hardwareFilter: MDLTextureFilter?     var transform: MDLTransform?     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLTextureSampler : CVarArg { } extension MDLTextureSampler : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MDLTransform](https://developer.apple.com/documentation/modelio/mdltransform)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLTransform : NSObject, MDLTransformComponent {     init(identity identity: ())     convenience init(transformComponent component: MDLTransformComponent)     convenience init(matrix matrix: matrix_float4x4)     func setIdentity()     func translationAtTime(_ time: NSTimeInterval) -> vector_float3     func rotationAtTime(_ time: NSTimeInterval) -> vector_float3     func shearAtTime(_ time: NSTimeInterval) -> vector_float3     func scaleAtTime(_ time: NSTimeInterval) -> vector_float3     func setTranslation(_ translation: vector_float3, forTime time: NSTimeInterval)     func setRotation(_ rotation: vector_float3, forTime time: NSTimeInterval)     func setShear(_ shear: vector_float3, forTime time: NSTimeInterval)     func setScale(_ scale: vector_float3, forTime time: NSTimeInterval)     func rotationMatrixAtTime(_ time: NSTimeInterval) -> matrix_float4x4     var translation: vector_float3     var rotation: vector_float3     var shear: vector_float3     var scale: vector_float3 } ``` | MDLTransformComponent |
| To | ``` class MDLTransform : NSObject, NSCopying, MDLTransformComponent {     init(identity identity: ())     convenience init(transformComponent component: MDLTransformComponent)     convenience init(transformComponent component: MDLTransformComponent, resetsTransform resetsTransform: Bool)     convenience init(matrix matrix: matrix_float4x4)     convenience init(matrix matrix: matrix_float4x4, resetsTransform resetsTransform: Bool)     func setIdentity()     func translation(atTime time: TimeInterval) -> vector_float3     func rotation(atTime time: TimeInterval) -> vector_float3     func shear(atTime time: TimeInterval) -> vector_float3     func scale(atTime time: TimeInterval) -> vector_float3     func setTranslation(_ translation: vector_float3, forTime time: TimeInterval)     func setRotation(_ rotation: vector_float3, forTime time: TimeInterval)     func setShear(_ shear: vector_float3, forTime time: TimeInterval)     func setScale(_ scale: vector_float3, forTime time: TimeInterval)     func rotationMatrix(atTime time: TimeInterval) -> matrix_float4x4     var translation: vector_float3     var rotation: vector_float3     var shear: vector_float3     var scale: vector_float3     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLTransform : CVarArg { } extension MDLTransform : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLTransformComponent, NSCopying |

Modified [MDLTransform.rotation(atTime: TimeInterval) -> vector_float3](https://developer.apple.com/documentation/modelio/mdltransform/1391460-rotation)

|  | Declaration |
| --- | --- |
| From | ``` func rotationAtTime(_ time: NSTimeInterval) -> vector_float3 ``` |
| To | ``` func rotation(atTime time: TimeInterval) -> vector_float3 ``` |

Modified [MDLTransform.rotationMatrix(atTime: TimeInterval) -> matrix_float4x4](https://developer.apple.com/documentation/modelio/mdltransform/1391445-rotationmatrix)

|  | Declaration |
| --- | --- |
| From | ``` func rotationMatrixAtTime(_ time: NSTimeInterval) -> matrix_float4x4 ``` |
| To | ``` func rotationMatrix(atTime time: TimeInterval) -> matrix_float4x4 ``` |

Modified [MDLTransform.scale(atTime: TimeInterval) -> vector_float3](https://developer.apple.com/documentation/modelio/mdltransform/1391616-scale)

|  | Declaration |
| --- | --- |
| From | ``` func scaleAtTime(_ time: NSTimeInterval) -> vector_float3 ``` |
| To | ``` func scale(atTime time: TimeInterval) -> vector_float3 ``` |

Modified [MDLTransform.setRotation(_: vector_float3, forTime: TimeInterval)](https://developer.apple.com/documentation/modelio/mdltransform/1391525-setrotation)

|  | Declaration |
| --- | --- |
| From | ``` func setRotation(_ rotation: vector_float3, forTime time: NSTimeInterval) ``` |
| To | ``` func setRotation(_ rotation: vector_float3, forTime time: TimeInterval) ``` |

Modified [MDLTransform.setScale(_: vector_float3, forTime: TimeInterval)](https://developer.apple.com/documentation/modelio/mdltransform/1391221-setscale)

|  | Declaration |
| --- | --- |
| From | ``` func setScale(_ scale: vector_float3, forTime time: NSTimeInterval) ``` |
| To | ``` func setScale(_ scale: vector_float3, forTime time: TimeInterval) ``` |

Modified [MDLTransform.setShear(_: vector_float3, forTime: TimeInterval)](https://developer.apple.com/documentation/modelio/mdltransform/1391206-setshear)

|  | Declaration |
| --- | --- |
| From | ``` func setShear(_ shear: vector_float3, forTime time: NSTimeInterval) ``` |
| To | ``` func setShear(_ shear: vector_float3, forTime time: TimeInterval) ``` |

Modified [MDLTransform.setTranslation(_: vector_float3, forTime: TimeInterval)](https://developer.apple.com/documentation/modelio/mdltransform/1391732-settranslation)

|  | Declaration |
| --- | --- |
| From | ``` func setTranslation(_ translation: vector_float3, forTime time: NSTimeInterval) ``` |
| To | ``` func setTranslation(_ translation: vector_float3, forTime time: TimeInterval) ``` |

Modified [MDLTransform.shear(atTime: TimeInterval) -> vector_float3](https://developer.apple.com/documentation/modelio/mdltransform/1391078-shear)

|  | Declaration |
| --- | --- |
| From | ``` func shearAtTime(_ time: NSTimeInterval) -> vector_float3 ``` |
| To | ``` func shear(atTime time: TimeInterval) -> vector_float3 ``` |

Modified [MDLTransform.translation(atTime: TimeInterval) -> vector_float3](https://developer.apple.com/documentation/modelio/mdltransform/1390919-translation)

|  | Declaration |
| --- | --- |
| From | ``` func translationAtTime(_ time: NSTimeInterval) -> vector_float3 ``` |
| To | ``` func translation(atTime time: TimeInterval) -> vector_float3 ``` |

Modified [MDLTransformComponent](https://developer.apple.com/documentation/modelio/mdltransformcomponent)

|  | Declaration |
| --- | --- |
| From | ``` protocol MDLTransformComponent : MDLComponent {     var matrix: matrix_float4x4 { get set }     var minimumTime: NSTimeInterval { get }     var maximumTime: NSTimeInterval { get }     optional func setLocalTransform(_ transform: matrix_float4x4, forTime time: NSTimeInterval)     optional func setLocalTransform(_ transform: matrix_float4x4)     optional func localTransformAtTime(_ time: NSTimeInterval) -> matrix_float4x4     optional static func globalTransformWithObject(_ object: MDLObject, atTime time: NSTimeInterval) -> matrix_float4x4 } ``` |
| To | ``` protocol MDLTransformComponent : MDLComponent {     var matrix: matrix_float4x4 { get set }     var resetsTransform: Bool { get set }     var minimumTime: TimeInterval { get }     var maximumTime: TimeInterval { get }     var keyTimes: [NSNumber] { get }     optional func setLocalTransform(_ transform: matrix_float4x4, forTime time: TimeInterval)     optional func setLocalTransform(_ transform: matrix_float4x4)     optional func localTransform(atTime time: TimeInterval) -> matrix_float4x4     optional static func globalTransform(with object: MDLObject, atTime time: TimeInterval) -> matrix_float4x4 } ``` |

Modified [MDLTransformComponent.globalTransform(with: MDLObject, atTime: TimeInterval) -> matrix_float4x4 [class]](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1391239-globaltransformwithobject)

|  | Declaration |
| --- | --- |
| From | ``` optional static func globalTransformWithObject(_ object: MDLObject, atTime time: NSTimeInterval) -> matrix_float4x4 ``` |
| To | ``` optional static func globalTransform(with object: MDLObject, atTime time: TimeInterval) -> matrix_float4x4 ``` |

Modified [MDLTransformComponent.localTransform(atTime: TimeInterval) -> matrix_float4x4](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1391570-localtransformattime)

|  | Declaration |
| --- | --- |
| From | ``` optional func localTransformAtTime(_ time: NSTimeInterval) -> matrix_float4x4 ``` |
| To | ``` optional func localTransform(atTime time: TimeInterval) -> matrix_float4x4 ``` |

Modified [MDLTransformComponent.maximumTime](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1391474-maximumtime)

|  | Declaration |
| --- | --- |
| From | ``` var maximumTime: NSTimeInterval { get } ``` |
| To | ``` var maximumTime: TimeInterval { get } ``` |

Modified [MDLTransformComponent.minimumTime](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1391558-minimumtime)

|  | Declaration |
| --- | --- |
| From | ``` var minimumTime: NSTimeInterval { get } ``` |
| To | ``` var minimumTime: TimeInterval { get } ``` |

Modified [MDLTransformComponent.setLocalTransform(_: matrix_float4x4, forTime: TimeInterval)](https://developer.apple.com/documentation/modelio/mdltransformcomponent/1391349-setlocaltransform)

|  | Declaration |
| --- | --- |
| From | ``` optional func setLocalTransform(_ transform: matrix_float4x4, forTime time: NSTimeInterval) ``` |
| To | ``` optional func setLocalTransform(_ transform: matrix_float4x4, forTime time: TimeInterval) ``` |

Modified [MDLURLTexture](https://developer.apple.com/documentation/modelio/mdlurltexture)

|  | Declaration |
| --- | --- |
| From | ``` class MDLURLTexture : MDLTexture {     init(URL URL: NSURL, name name: String?)     @NSCopying var URL: NSURL } ``` |
| To | ``` class MDLURLTexture : MDLTexture {     init(url URL: URL, name name: String?)     var url: URL } ``` |

Modified [MDLURLTexture.init(url: URL, name: String?)](https://developer.apple.com/documentation/modelio/mdlurltexture/1391585-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL, name name: String?) ``` |
| To | ``` init(url URL: URL, name name: String?) ``` |

Modified [MDLURLTexture.url](https://developer.apple.com/documentation/modelio/mdlurltexture/1391186-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL ``` |
| To | ``` var url: URL ``` |

Modified [MDLVertexAttribute](https://developer.apple.com/documentation/modelio/mdlvertexattribute)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLVertexAttribute : NSObject, NSCopying {     init(name name: String, format format: MDLVertexFormat, offset offset: Int, bufferIndex bufferIndex: Int)     var name: String     var format: MDLVertexFormat     var offset: Int     var bufferIndex: Int     var initializationValue: vector_float4 } ``` | NSCopying |
| To | ``` class MDLVertexAttribute : NSObject, NSCopying {     init(name name: String, format format: MDLVertexFormat, offset offset: Int, bufferIndex bufferIndex: Int)     var name: String     var format: MDLVertexFormat     var offset: Int     var bufferIndex: Int     var time: TimeInterval     var initializationValue: vector_float4     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLVertexAttribute : CVarArg { } extension MDLVertexAttribute : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MDLVertexAttributeData](https://developer.apple.com/documentation/modelio/mdlvertexattributedata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLVertexAttributeData : NSObject {     var map: MDLMeshBufferMap     var dataStart: UnsafeMutablePointer<Void>     var stride: Int     var format: MDLVertexFormat } ``` | -- |
| To | ``` class MDLVertexAttributeData : NSObject {     var map: MDLMeshBufferMap     var dataStart: UnsafeMutableRawPointer     var stride: Int     var format: MDLVertexFormat     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLVertexAttributeData : CVarArg { } extension MDLVertexAttributeData : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MDLVertexAttributeData.dataStart](https://developer.apple.com/documentation/modelio/mdlvertexattributedata/1391593-datastart)

|  | Declaration |
| --- | --- |
| From | ``` var dataStart: UnsafeMutablePointer<Void> ``` |
| To | ``` var dataStart: UnsafeMutableRawPointer ``` |

Modified [MDLVertexBufferLayout](https://developer.apple.com/documentation/modelio/mdlvertexbufferlayout)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLVertexBufferLayout : NSObject, NSCopying {     var stride: Int } ``` | NSCopying |
| To | ``` class MDLVertexBufferLayout : NSObject, NSCopying {     init(stride stride: Int)     var stride: Int     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLVertexBufferLayout : CVarArg { } extension MDLVertexBufferLayout : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MDLVertexDescriptor](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MDLVertexDescriptor : NSObject, NSCopying {     init(vertexDescriptor vertexDescriptor: MDLVertexDescriptor)     func attributeNamed(_ name: String) -> MDLVertexAttribute?     func addOrReplaceAttribute(_ attribute: MDLVertexAttribute)     var attributes: NSMutableArray     var layouts: NSMutableArray     func reset()     func setPackedStrides()     func setPackedOffsets() } ``` | NSCopying |
| To | ``` class MDLVertexDescriptor : NSObject, NSCopying {     init(vertexDescriptor vertexDescriptor: MDLVertexDescriptor)     func attributeNamed(_ name: String) -> MDLVertexAttribute?     func addOrReplaceAttribute(_ attribute: MDLVertexAttribute)     func removeAttributeNamed(_ name: String)     var attributes: NSMutableArray     var layouts: NSMutableArray     func reset()     func setPackedStrides()     func setPackedOffsets()     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MDLVertexDescriptor : CVarArg { } extension MDLVertexDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MDLVertexFormat [enum]](https://developer.apple.com/documentation/modelio/mdlvertexformat)

|  | Declaration |
| --- | --- |
| From | ``` enum MDLVertexFormat : UInt {     case Invalid     case PackedBit     case UCharBits     case CharBits     case UCharNormalizedBits     case CharNormalizedBits     case UShortBits     case ShortBits     case UShortNormalizedBits     case ShortNormalizedBits     case UIntBits     case IntBits     case HalfBits     case FloatBits     case UChar     case UChar2     case UChar3     case UChar4     case Char     case Char2     case Char3     case Char4     case UCharNormalized     case UChar2Normalized     case UChar3Normalized     case UChar4Normalized     case CharNormalized     case Char2Normalized     case Char3Normalized     case Char4Normalized     case UShort     case UShort2     case UShort3     case UShort4     case Short     case Short2     case Short3     case Short4     case UShortNormalized     case UShort2Normalized     case UShort3Normalized     case UShort4Normalized     case ShortNormalized     case Short2Normalized     case Short3Normalized     case Short4Normalized     case UInt     case UInt2     case UInt3     case UInt4     case Int     case Int2     case Int3     case Int4     case Half     case Half2     case Half3     case Half4     case Float     case Float2     case Float3     case Float4     case Int1010102Normalized     case UInt1010102Normalized } ``` |
| To | ``` enum MDLVertexFormat : UInt {     case invalid     case packedBit     case uCharBits     case charBits     case uCharNormalizedBits     case charNormalizedBits     case uShortBits     case shortBits     case uShortNormalizedBits     case shortNormalizedBits     case uIntBits     case intBits     case halfBits     case floatBits     case uChar     case uChar2     case uChar3     case uChar4     case char     case char2     case char3     case char4     case uCharNormalized     case uChar2Normalized     case uChar3Normalized     case uChar4Normalized     case charNormalized     case char2Normalized     case char3Normalized     case char4Normalized     case uShort     case uShort2     case uShort3     case uShort4     case short     case short2     case short3     case short4     case uShortNormalized     case uShort2Normalized     case uShort3Normalized     case uShort4Normalized     case shortNormalized     case short2Normalized     case short3Normalized     case short4Normalized     case uInt     case uInt2     case uInt3     case uInt4     case int     case int2     case int3     case int4     case half     case half2     case half3     case half4     case float     case float2     case float3     case float4     case int1010102Normalized     case uInt1010102Normalized } ``` |

Modified [MDLVertexFormat.char](https://developer.apple.com/documentation/modelio/mdlvertexformat/char)

|  | Declaration |
| --- | --- |
| From | ``` case Char ``` |
| To | ``` case char ``` |

Modified [MDLVertexFormat.char2](https://developer.apple.com/documentation/modelio/mdlvertexformat/char2)

|  | Declaration |
| --- | --- |
| From | ``` case Char2 ``` |
| To | ``` case char2 ``` |

Modified [MDLVertexFormat.char2Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/char2normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Char2Normalized ``` |
| To | ``` case char2Normalized ``` |

Modified [MDLVertexFormat.char3](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatchar3)

|  | Declaration |
| --- | --- |
| From | ``` case Char3 ``` |
| To | ``` case char3 ``` |

Modified [MDLVertexFormat.char3Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/char3normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Char3Normalized ``` |
| To | ``` case char3Normalized ``` |

Modified [MDLVertexFormat.char4](https://developer.apple.com/documentation/modelio/mdlvertexformat/char4)

|  | Declaration |
| --- | --- |
| From | ``` case Char4 ``` |
| To | ``` case char4 ``` |

Modified [MDLVertexFormat.char4Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatchar4normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Char4Normalized ``` |
| To | ``` case char4Normalized ``` |

Modified [MDLVertexFormat.charBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatcharbits)

|  | Declaration |
| --- | --- |
| From | ``` case CharBits ``` |
| To | ``` case charBits ``` |

Modified [MDLVertexFormat.charNormalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/charnormalized)

|  | Declaration |
| --- | --- |
| From | ``` case CharNormalized ``` |
| To | ``` case charNormalized ``` |

Modified [MDLVertexFormat.charNormalizedBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatcharnormalizedbits)

|  | Declaration |
| --- | --- |
| From | ``` case CharNormalizedBits ``` |
| To | ``` case charNormalizedBits ``` |

Modified [MDLVertexFormat.float](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatfloat)

|  | Declaration |
| --- | --- |
| From | ``` case Float ``` |
| To | ``` case float ``` |

Modified [MDLVertexFormat.float2](https://developer.apple.com/documentation/modelio/mdlvertexformat/float2)

|  | Declaration |
| --- | --- |
| From | ``` case Float2 ``` |
| To | ``` case float2 ``` |

Modified [MDLVertexFormat.float3](https://developer.apple.com/documentation/modelio/mdlvertexformat/float3)

|  | Declaration |
| --- | --- |
| From | ``` case Float3 ``` |
| To | ``` case float3 ``` |

Modified [MDLVertexFormat.float4](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatfloat4)

|  | Declaration |
| --- | --- |
| From | ``` case Float4 ``` |
| To | ``` case float4 ``` |

Modified [MDLVertexFormat.floatBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatfloatbits)

|  | Declaration |
| --- | --- |
| From | ``` case FloatBits ``` |
| To | ``` case floatBits ``` |

Modified [MDLVertexFormat.half](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformathalf)

|  | Declaration |
| --- | --- |
| From | ``` case Half ``` |
| To | ``` case half ``` |

Modified [MDLVertexFormat.half2](https://developer.apple.com/documentation/modelio/mdlvertexformat/half2)

|  | Declaration |
| --- | --- |
| From | ``` case Half2 ``` |
| To | ``` case half2 ``` |

Modified [MDLVertexFormat.half3](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformathalf3)

|  | Declaration |
| --- | --- |
| From | ``` case Half3 ``` |
| To | ``` case half3 ``` |

Modified [MDLVertexFormat.half4](https://developer.apple.com/documentation/modelio/mdlvertexformat/half4)

|  | Declaration |
| --- | --- |
| From | ``` case Half4 ``` |
| To | ``` case half4 ``` |

Modified [MDLVertexFormat.halfBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformathalfbits)

|  | Declaration |
| --- | --- |
| From | ``` case HalfBits ``` |
| To | ``` case halfBits ``` |

Modified [MDLVertexFormat.int](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatint)

|  | Declaration |
| --- | --- |
| From | ``` case Int ``` |
| To | ``` case int ``` |

Modified [MDLVertexFormat.int1010102Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/int1010102normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Int1010102Normalized ``` |
| To | ``` case int1010102Normalized ``` |

Modified [MDLVertexFormat.int2](https://developer.apple.com/documentation/modelio/mdlvertexformat/int2)

|  | Declaration |
| --- | --- |
| From | ``` case Int2 ``` |
| To | ``` case int2 ``` |

Modified [MDLVertexFormat.int3](https://developer.apple.com/documentation/modelio/mdlvertexformat/int3)

|  | Declaration |
| --- | --- |
| From | ``` case Int3 ``` |
| To | ``` case int3 ``` |

Modified [MDLVertexFormat.int4](https://developer.apple.com/documentation/modelio/mdlvertexformat/int4)

|  | Declaration |
| --- | --- |
| From | ``` case Int4 ``` |
| To | ``` case int4 ``` |

Modified [MDLVertexFormat.intBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatintbits)

|  | Declaration |
| --- | --- |
| From | ``` case IntBits ``` |
| To | ``` case intBits ``` |

Modified [MDLVertexFormat.invalid](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [MDLVertexFormat.packedBit](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatpackedbit)

|  | Declaration |
| --- | --- |
| From | ``` case PackedBit ``` |
| To | ``` case packedBit ``` |

Modified [MDLVertexFormat.short](https://developer.apple.com/documentation/modelio/mdlvertexformat/short)

|  | Declaration |
| --- | --- |
| From | ``` case Short ``` |
| To | ``` case short ``` |

Modified [MDLVertexFormat.short2](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatshort2)

|  | Declaration |
| --- | --- |
| From | ``` case Short2 ``` |
| To | ``` case short2 ``` |

Modified [MDLVertexFormat.short2Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatshort2normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Short2Normalized ``` |
| To | ``` case short2Normalized ``` |

Modified [MDLVertexFormat.short3](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatshort3)

|  | Declaration |
| --- | --- |
| From | ``` case Short3 ``` |
| To | ``` case short3 ``` |

Modified [MDLVertexFormat.short3Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatshort3normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Short3Normalized ``` |
| To | ``` case short3Normalized ``` |

Modified [MDLVertexFormat.short4](https://developer.apple.com/documentation/modelio/mdlvertexformat/short4)

|  | Declaration |
| --- | --- |
| From | ``` case Short4 ``` |
| To | ``` case short4 ``` |

Modified [MDLVertexFormat.short4Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/short4normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Short4Normalized ``` |
| To | ``` case short4Normalized ``` |

Modified [MDLVertexFormat.shortBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/shortbits)

|  | Declaration |
| --- | --- |
| From | ``` case ShortBits ``` |
| To | ``` case shortBits ``` |

Modified [MDLVertexFormat.shortNormalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatshortnormalized)

|  | Declaration |
| --- | --- |
| From | ``` case ShortNormalized ``` |
| To | ``` case shortNormalized ``` |

Modified [MDLVertexFormat.shortNormalizedBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/shortnormalizedbits)

|  | Declaration |
| --- | --- |
| From | ``` case ShortNormalizedBits ``` |
| To | ``` case shortNormalizedBits ``` |

Modified [MDLVertexFormat.uChar](https://developer.apple.com/documentation/modelio/mdlvertexformat/uchar)

|  | Declaration |
| --- | --- |
| From | ``` case UChar ``` |
| To | ``` case uChar ``` |

Modified [MDLVertexFormat.uChar2](https://developer.apple.com/documentation/modelio/mdlvertexformat/uchar2)

|  | Declaration |
| --- | --- |
| From | ``` case UChar2 ``` |
| To | ``` case uChar2 ``` |

Modified [MDLVertexFormat.uChar2Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/uchar2normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UChar2Normalized ``` |
| To | ``` case uChar2Normalized ``` |

Modified [MDLVertexFormat.uChar3](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatuchar3)

|  | Declaration |
| --- | --- |
| From | ``` case UChar3 ``` |
| To | ``` case uChar3 ``` |

Modified [MDLVertexFormat.uChar3Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/uchar3normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UChar3Normalized ``` |
| To | ``` case uChar3Normalized ``` |

Modified [MDLVertexFormat.uChar4](https://developer.apple.com/documentation/modelio/mdlvertexformat/uchar4)

|  | Declaration |
| --- | --- |
| From | ``` case UChar4 ``` |
| To | ``` case uChar4 ``` |

Modified [MDLVertexFormat.uChar4Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/uchar4normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UChar4Normalized ``` |
| To | ``` case uChar4Normalized ``` |

Modified [MDLVertexFormat.uCharBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/ucharbits)

|  | Declaration |
| --- | --- |
| From | ``` case UCharBits ``` |
| To | ``` case uCharBits ``` |

Modified [MDLVertexFormat.uCharNormalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatucharnormalized)

|  | Declaration |
| --- | --- |
| From | ``` case UCharNormalized ``` |
| To | ``` case uCharNormalized ``` |

Modified [MDLVertexFormat.uCharNormalizedBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatucharnormalizedbits)

|  | Declaration |
| --- | --- |
| From | ``` case UCharNormalizedBits ``` |
| To | ``` case uCharNormalizedBits ``` |

Modified [MDLVertexFormat.uInt](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatuint)

|  | Declaration |
| --- | --- |
| From | ``` case UInt ``` |
| To | ``` case uInt ``` |

Modified [MDLVertexFormat.uInt1010102Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/uint1010102normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UInt1010102Normalized ``` |
| To | ``` case uInt1010102Normalized ``` |

Modified [MDLVertexFormat.uInt2](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatuint2)

|  | Declaration |
| --- | --- |
| From | ``` case UInt2 ``` |
| To | ``` case uInt2 ``` |

Modified [MDLVertexFormat.uInt3](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatuint3)

|  | Declaration |
| --- | --- |
| From | ``` case UInt3 ``` |
| To | ``` case uInt3 ``` |

Modified [MDLVertexFormat.uInt4](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatuint4)

|  | Declaration |
| --- | --- |
| From | ``` case UInt4 ``` |
| To | ``` case uInt4 ``` |

Modified [MDLVertexFormat.uIntBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/uintbits)

|  | Declaration |
| --- | --- |
| From | ``` case UIntBits ``` |
| To | ``` case uIntBits ``` |

Modified [MDLVertexFormat.uShort](https://developer.apple.com/documentation/modelio/mdlvertexformat/ushort)

|  | Declaration |
| --- | --- |
| From | ``` case UShort ``` |
| To | ``` case uShort ``` |

Modified [MDLVertexFormat.uShort2](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatushort2)

|  | Declaration |
| --- | --- |
| From | ``` case UShort2 ``` |
| To | ``` case uShort2 ``` |

Modified [MDLVertexFormat.uShort2Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatushort2normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UShort2Normalized ``` |
| To | ``` case uShort2Normalized ``` |

Modified [MDLVertexFormat.uShort3](https://developer.apple.com/documentation/modelio/mdlvertexformat/ushort3)

|  | Declaration |
| --- | --- |
| From | ``` case UShort3 ``` |
| To | ``` case uShort3 ``` |

Modified [MDLVertexFormat.uShort3Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatushort3normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UShort3Normalized ``` |
| To | ``` case uShort3Normalized ``` |

Modified [MDLVertexFormat.uShort4](https://developer.apple.com/documentation/modelio/mdlvertexformat/ushort4)

|  | Declaration |
| --- | --- |
| From | ``` case UShort4 ``` |
| To | ``` case uShort4 ``` |

Modified [MDLVertexFormat.uShort4Normalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatushort4normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UShort4Normalized ``` |
| To | ``` case uShort4Normalized ``` |

Modified [MDLVertexFormat.uShortBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatushortbits)

|  | Declaration |
| --- | --- |
| From | ``` case UShortBits ``` |
| To | ``` case uShortBits ``` |

Modified [MDLVertexFormat.uShortNormalized](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatushortnormalized)

|  | Declaration |
| --- | --- |
| From | ``` case UShortNormalized ``` |
| To | ``` case uShortNormalized ``` |

Modified [MDLVertexFormat.uShortNormalizedBits](https://developer.apple.com/documentation/modelio/mdlvertexformat/mdlvertexformatushortnormalizedbits)

|  | Declaration |
| --- | --- |
| From | ``` case UShortNormalizedBits ``` |
| To | ``` case uShortNormalizedBits ``` |

Modified [MDLVoxelArray](https://developer.apple.com/documentation/modelio/mdlvoxelarray)

|  | Declaration | Superclasses |
| --- | --- | --- |
| From | ``` class MDLVoxelArray : NSObject {     init(asset asset: MDLAsset, divisions divisions: Int32, interiorShells interiorShells: Int32, exteriorShells exteriorShells: Int32, patchRadius patchRadius: Float)     init(asset asset: MDLAsset, divisions divisions: Int32, interiorNBWidth interiorNBWidth: Float, exteriorNBWidth exteriorNBWidth: Float, patchRadius patchRadius: Float)     init(data voxelData: NSData, boundingBox boundingBox: MDLAxisAlignedBoundingBox, voxelExtent voxelExtent: Float)     func meshUsingAllocator(_ allocator: MDLMeshBufferAllocator?) -> MDLMesh?     func voxelExistsAtIndex(_ index: MDLVoxelIndex, allowAnyX allowAnyX: Bool, allowAnyY allowAnyY: Bool, allowAnyZ allowAnyZ: Bool, allowAnyShell allowAnyShell: Bool) -> Bool     func setVoxelAtIndex(_ index: MDLVoxelIndex)     func setVoxelsForMesh(_ mesh: MDLMesh, divisions divisions: Int32, interiorShells interiorShells: Int32, exteriorShells exteriorShells: Int32, patchRadius patchRadius: Float)     func setVoxelsForMesh(_ mesh: MDLMesh, divisions divisions: Int32, interiorNBWidth interiorNBWidth: Float, exteriorNBWidth exteriorNBWidth: Float, patchRadius patchRadius: Float)     func voxelsWithinExtent(_ extent: MDLVoxelIndexExtent) -> NSData?     func voxelIndices() -> NSData?     func unionWithVoxels(_ voxels: MDLVoxelArray)     func differenceWithVoxels(_ voxels: MDLVoxelArray)     func intersectWithVoxels(_ voxels: MDLVoxelArray)     func indexOfSpatialLocation(_ location: vector_float3) -> MDLVoxelIndex     func spatialLocationOfIndex(_ index: MDLVoxelIndex) -> vector_float3     func voxelBoundingBoxAtIndex(_ index: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox     var count: Int { get }     var voxelIndexExtent: MDLVoxelIndexExtent { get }     var boundingBox: MDLAxisAlignedBoundingBox { get } } ``` | NSObject |
| To | ``` class MDLVoxelArray : MDLObject {     init(asset asset: MDLAsset, divisions divisions: Int32, patchRadius patchRadius: Float)     init(data voxelData: Data, boundingBox boundingBox: MDLAxisAlignedBoundingBox, voxelExtent voxelExtent: Float)     init(asset asset: MDLAsset, divisions divisions: Int32, interiorShells interiorShells: Int32, exteriorShells exteriorShells: Int32, patchRadius patchRadius: Float)     init(asset asset: MDLAsset, divisions divisions: Int32, interiorNBWidth interiorNBWidth: Float, exteriorNBWidth exteriorNBWidth: Float, patchRadius patchRadius: Float)     var count: Int { get }     var voxelIndexExtent: MDLVoxelIndexExtent { get }     func voxelExists(atIndex index: MDLVoxelIndex, allowAnyX allowAnyX: Bool, allowAnyY allowAnyY: Bool, allowAnyZ allowAnyZ: Bool, allowAnyShell allowAnyShell: Bool) -> Bool     func voxels(within extent: MDLVoxelIndexExtent) -> Data?     func voxelIndices() -> Data?     func setVoxelAtIndex(_ index: MDLVoxelIndex)     func setVoxelsFor(_ mesh: MDLMesh, divisions divisions: Int32, patchRadius patchRadius: Float)     func setVoxelsFor(_ mesh: MDLMesh, divisions divisions: Int32, interiorShells interiorShells: Int32, exteriorShells exteriorShells: Int32, patchRadius patchRadius: Float)     func setVoxelsFor(_ mesh: MDLMesh, divisions divisions: Int32, interiorNBWidth interiorNBWidth: Float, exteriorNBWidth exteriorNBWidth: Float, patchRadius patchRadius: Float)     func union(with voxels: MDLVoxelArray)     func intersect(with voxels: MDLVoxelArray)     func difference(with voxels: MDLVoxelArray)     var boundingBox: MDLAxisAlignedBoundingBox { get }     func index(ofSpatialLocation location: vector_float3) -> MDLVoxelIndex     func spatialLocation(ofIndex index: MDLVoxelIndex) -> vector_float3     func voxelBoundingBox(atIndex index: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox     func convertToSignedShellField()     var isValidSignedShellField: Bool { get }     var shellFieldInteriorThickness: Float     var shellFieldExteriorThickness: Float     func coarseMesh() -> MDLMesh?     func coarseMesh(using allocator: MDLMeshBufferAllocator?) -> MDLMesh?     func mesh(using allocator: MDLMeshBufferAllocator?) -> MDLMesh? } ``` | MDLObject |

Modified [MDLVoxelArray.difference(with: MDLVoxelArray)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391915-differencewithvoxels)

|  | Declaration |
| --- | --- |
| From | ``` func differenceWithVoxels(_ voxels: MDLVoxelArray) ``` |
| To | ``` func difference(with voxels: MDLVoxelArray) ``` |

Modified [MDLVoxelArray.index(ofSpatialLocation: vector_float3) -> MDLVoxelIndex](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391753-index)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfSpatialLocation(_ location: vector_float3) -> MDLVoxelIndex ``` |
| To | ``` func index(ofSpatialLocation location: vector_float3) -> MDLVoxelIndex ``` |

Modified [MDLVoxelArray.init(asset: MDLAsset, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391981-initwithasset)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [MDLVoxelArray.init(asset: MDLAsset, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391256-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [MDLVoxelArray.init(data: Data, boundingBox: MDLAxisAlignedBoundingBox, voxelExtent: Float)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391564-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data voxelData: NSData, boundingBox boundingBox: MDLAxisAlignedBoundingBox, voxelExtent voxelExtent: Float) ``` |
| To | ``` init(data voxelData: Data, boundingBox boundingBox: MDLAxisAlignedBoundingBox, voxelExtent voxelExtent: Float) ``` |

Modified [MDLVoxelArray.intersect(with: MDLVoxelArray)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391369-intersect)

|  | Declaration |
| --- | --- |
| From | ``` func intersectWithVoxels(_ voxels: MDLVoxelArray) ``` |
| To | ``` func intersect(with voxels: MDLVoxelArray) ``` |

Modified [MDLVoxelArray.mesh(using: MDLMeshBufferAllocator?) -> MDLMesh?](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391883-mesh)

|  | Declaration |
| --- | --- |
| From | ``` func meshUsingAllocator(_ allocator: MDLMeshBufferAllocator?) -> MDLMesh? ``` |
| To | ``` func mesh(using allocator: MDLMeshBufferAllocator?) -> MDLMesh? ``` |

Modified [MDLVoxelArray.setVoxelsFor(_: MDLMesh, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391241-setvoxelsformesh)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func setVoxelsForMesh(_ mesh: MDLMesh, divisions divisions: Int32, interiorNBWidth interiorNBWidth: Float, exteriorNBWidth exteriorNBWidth: Float, patchRadius patchRadius: Float) ``` | -- |
| To | ``` func setVoxelsFor(_ mesh: MDLMesh, divisions divisions: Int32, interiorNBWidth interiorNBWidth: Float, exteriorNBWidth exteriorNBWidth: Float, patchRadius patchRadius: Float) ``` | OS X 10.12 |

Modified [MDLVoxelArray.setVoxelsFor(_: MDLMesh, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1392017-setvoxelsfor)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func setVoxelsForMesh(_ mesh: MDLMesh, divisions divisions: Int32, interiorShells interiorShells: Int32, exteriorShells exteriorShells: Int32, patchRadius patchRadius: Float) ``` | -- |
| To | ``` func setVoxelsFor(_ mesh: MDLMesh, divisions divisions: Int32, interiorShells interiorShells: Int32, exteriorShells exteriorShells: Int32, patchRadius patchRadius: Float) ``` | OS X 10.12 |

Modified [MDLVoxelArray.spatialLocation(ofIndex: MDLVoxelIndex) -> vector_float3](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391204-spatiallocation)

|  | Declaration |
| --- | --- |
| From | ``` func spatialLocationOfIndex(_ index: MDLVoxelIndex) -> vector_float3 ``` |
| To | ``` func spatialLocation(ofIndex index: MDLVoxelIndex) -> vector_float3 ``` |

Modified [MDLVoxelArray.union(with: MDLVoxelArray)](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391026-union)

|  | Declaration |
| --- | --- |
| From | ``` func unionWithVoxels(_ voxels: MDLVoxelArray) ``` |
| To | ``` func union(with voxels: MDLVoxelArray) ``` |

Modified [MDLVoxelArray.voxelBoundingBox(atIndex: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391435-voxelboundingbox)

|  | Declaration |
| --- | --- |
| From | ``` func voxelBoundingBoxAtIndex(_ index: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox ``` |
| To | ``` func voxelBoundingBox(atIndex index: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox ``` |

Modified [MDLVoxelArray.voxelExists(atIndex: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391686-voxelexists)

|  | Declaration |
| --- | --- |
| From | ``` func voxelExistsAtIndex(_ index: MDLVoxelIndex, allowAnyX allowAnyX: Bool, allowAnyY allowAnyY: Bool, allowAnyZ allowAnyZ: Bool, allowAnyShell allowAnyShell: Bool) -> Bool ``` |
| To | ``` func voxelExists(atIndex index: MDLVoxelIndex, allowAnyX allowAnyX: Bool, allowAnyY allowAnyY: Bool, allowAnyZ allowAnyZ: Bool, allowAnyShell allowAnyShell: Bool) -> Bool ``` |

Modified [MDLVoxelArray.voxelIndices() -> Data?](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1391866-voxelindices)

|  | Declaration |
| --- | --- |
| From | ``` func voxelIndices() -> NSData? ``` |
| To | ``` func voxelIndices() -> Data? ``` |

Modified [MDLVoxelArray.voxels(within: MDLVoxelIndexExtent) -> Data?](https://developer.apple.com/documentation/modelio/mdlvoxelarray/1390977-voxels)

|  | Declaration |
| --- | --- |
| From | ``` func voxelsWithinExtent(_ extent: MDLVoxelIndexExtent) -> NSData? ``` |
| To | ``` func voxels(within extent: MDLVoxelIndexExtent) -> Data? ``` |

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

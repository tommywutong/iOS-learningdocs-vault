---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/GLKit.html
archived_at: '2026-07-18T02:55:26.672820Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# GLKit Changes for Swift

### GLKit

Added [GLKTextureInfo.arrayLength](https://developer.apple.com/documentation/glkit/glktextureinfo/1639613-arraylength)Added [GLKTextureInfo.depth](https://developer.apple.com/documentation/glkit/glktextureinfo/1639589-depth)Added [GLKTextureInfo.mimapLevelCount](https://developer.apple.com/documentation/glkit/glktextureinfo/1639598-mimaplevelcount)Added [GLKTextureLoader.texture(withName: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1639590-texture)Added [GLKTextureLoader.texture(withName: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]?, queue: DispatchQueue?, completionHandler: GLKit.GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1639591-texturewithname)Added [GLKTextureLoaderError [struct]](https://developer.apple.com/documentation/glkit/glktextureloadererror)Added [GLKTextureLoaderError.alphaPremultiplicationFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330513-alphapremultiplicationfailure)Added [GLKTextureLoaderError.compressedTextureUpload](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330514-compressedtextureupload)Added [GLKTextureLoaderError.cubeMapInvalidNumFiles](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330518-cubemapinvalidnumfiles)Added [GLKTextureLoaderError.dataPreprocessingFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330519-datapreprocessingfailure)Added [GLKTextureLoaderError.fileOrURLNotFound](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330515-fileorurlnotfound)Added [GLKTextureLoaderError.incompatibleFormatSRGB](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330528-incompatibleformatsrgb)Added GLKTextureLoaderError.init(_nsError: NSError)Added [GLKTextureLoaderError.invalidCGImage](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330523-invalidcgimage)Added [GLKTextureLoaderError.invalidEAGLContext](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330520-invalideaglcontext)Added [GLKTextureLoaderError.invalidNSData](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330524-invalidnsdata)Added [GLKTextureLoaderError.mipmapUnsupported](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330532-mipmapunsupported)Added [GLKTextureLoaderError.pvrAtlasUnsupported](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330526-pvratlasunsupported)Added [GLKTextureLoaderError.reorientationFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330530-reorientationfailure)Added [GLKTextureLoaderError.uncompressedTextureUpload](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330525-uncompressedtextureupload)Added [GLKTextureLoaderError.unknownFileType](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330522-unknownfiletype)Added [GLKTextureLoaderError.unknownPathType](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330529-unknownpathtype)Added [GLKTextureLoaderError.unsupportedBitDepth](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330527-unsupportedbitdepth)Added [GLKTextureLoaderError.unsupportedCubeMapDimensions](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330531-unsupportedcubemapdimensions)Added [GLKTextureLoaderError.unsupportedOrientation](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330521-unsupportedorientation)Added [GLKTextureLoaderError.unsupportedPVRFormat](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330516-unsupportedpvrformat)Added [GLKTextureLoaderError.unsupportedTextureTarget](https://developer.apple.com/documentation/glkit/glktextureloadererror/2330517-unsupportedtexturetarget)Added [GLKTextureLoaderError.Code.unsupportedTextureTarget](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/unsupportedtexturetarget)Modified [GLKBaseEffect](https://developer.apple.com/documentation/glkit/glkbaseeffect)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKBaseEffect : NSObject, GLKNamedEffect {     func prepareToDraw()     var colorMaterialEnabled: GLboolean     var lightModelTwoSided: GLboolean     var useConstantColor: GLboolean     var transform: GLKEffectPropertyTransform { get }     var light0: GLKEffectPropertyLight { get }     var light1: GLKEffectPropertyLight { get }     var light2: GLKEffectPropertyLight { get }     var lightingType: GLKLightingType     var lightModelAmbientColor: GLKVector4     var material: GLKEffectPropertyMaterial { get }     var texture2d0: GLKEffectPropertyTexture { get }     var texture2d1: GLKEffectPropertyTexture { get }     var textureOrder: [GLKEffectPropertyTexture]?     var constantColor: GLKVector4     var fog: GLKEffectPropertyFog { get }     var label: String? } ``` | GLKNamedEffect |
| To | ``` class GLKBaseEffect : NSObject, GLKNamedEffect {     func prepareToDraw()     var colorMaterialEnabled: GLboolean     var lightModelTwoSided: GLboolean     var useConstantColor: GLboolean     var transform: GLKEffectPropertyTransform { get }     var light0: GLKEffectPropertyLight { get }     var light1: GLKEffectPropertyLight { get }     var light2: GLKEffectPropertyLight { get }     var lightingType: GLKLightingType     var lightModelAmbientColor: GLKVector4     var material: GLKEffectPropertyMaterial { get }     var texture2d0: GLKEffectPropertyTexture { get }     var texture2d1: GLKEffectPropertyTexture { get }     var textureOrder: [GLKEffectPropertyTexture]?     var constantColor: GLKVector4     var fog: GLKEffectPropertyFog { get }     var label: String?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKBaseEffect : CVarArg { } extension GLKBaseEffect : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, GLKNamedEffect, Hashable |

Modified [GLKEffectProperty](https://developer.apple.com/documentation/glkit/glkeffectproperty)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKEffectProperty : NSObject { } ``` | -- |
| To | ``` class GLKEffectProperty : NSObject {     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKEffectProperty : CVarArg { } extension GLKEffectProperty : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GLKFogMode [enum]](https://developer.apple.com/documentation/glkit/glkfogmode)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKFogMode : GLint {     case Exp     case Exp2     case Linear } ``` |
| To | ``` enum GLKFogMode : GLint {     case exp     case exp2     case linear } ``` |

Modified [GLKFogMode.exp](https://developer.apple.com/documentation/glkit/glkfogmode/glkfogmodeexp)

|  | Declaration |
| --- | --- |
| From | ``` case Exp ``` |
| To | ``` case exp ``` |

Modified [GLKFogMode.exp2](https://developer.apple.com/documentation/glkit/glkfogmode/glkfogmodeexp2)

|  | Declaration |
| --- | --- |
| From | ``` case Exp2 ``` |
| To | ``` case exp2 ``` |

Modified [GLKFogMode.linear](https://developer.apple.com/documentation/glkit/glkfogmode/glkfogmodelinear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [GLKLightingType [enum]](https://developer.apple.com/documentation/glkit/glklightingtype)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKLightingType : GLint {     case PerVertex     case PerPixel } ``` |
| To | ``` enum GLKLightingType : GLint {     case perVertex     case perPixel } ``` |

Modified [GLKLightingType.perPixel](https://developer.apple.com/documentation/glkit/glklightingtype/perpixel)

|  | Declaration |
| --- | --- |
| From | ``` case PerPixel ``` |
| To | ``` case perPixel ``` |

Modified [GLKLightingType.perVertex](https://developer.apple.com/documentation/glkit/glklightingtype/pervertex)

|  | Declaration |
| --- | --- |
| From | ``` case PerVertex ``` |
| To | ``` case perVertex ``` |

Modified GLKMatrix2.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ i: Int) -> Float { get } ``` |
| To | ``` subscript(_ i: Int) -> Float { get } ``` |

Modified GLKMatrix3.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ i: Int) -> Float { get } ``` |
| To | ``` subscript(_ i: Int) -> Float { get } ``` |

Modified GLKMatrix4.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ i: Int) -> Float { get } ``` |
| To | ``` subscript(_ i: Int) -> Float { get } ``` |

Modified [GLKMesh](https://developer.apple.com/documentation/glkit/glkmesh)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKMesh : NSObject {     init?()     init(mesh mesh: MDLMesh) throws     class func newMeshesFromAsset(_ asset: MDLAsset, sourceMeshes sourceMeshes: AutoreleasingUnsafeMutablePointer<NSArray?>) throws -> [GLKMesh]     var vertexCount: Int { get }     var vertexBuffers: [GLKMeshBuffer] { get }     var vertexDescriptor: MDLVertexDescriptor { get }     var submeshes: [GLKSubmesh] { get }     var name: String { get } } ``` | -- |
| To | ``` class GLKMesh : NSObject {     init?()     init(mesh mesh: MDLMesh) throws     class func newMeshes(from asset: MDLAsset, sourceMeshes sourceMeshes: AutoreleasingUnsafeMutablePointer<NSArray?>?) throws -> [GLKMesh]     var vertexCount: Int { get }     var vertexBuffers: [GLKMeshBuffer] { get }     var vertexDescriptor: MDLVertexDescriptor { get }     var submeshes: [GLKSubmesh] { get }     var name: String { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKMesh : CVarArg { } extension GLKMesh : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GLKMesh.newMeshes(from: MDLAsset, sourceMeshes: AutoreleasingUnsafeMutablePointer<NSArray?>?) throws -> [GLKMesh] [class]](https://developer.apple.com/documentation/glkit/glkmesh/1488791-newmeshesfromasset)

|  | Declaration |
| --- | --- |
| From | ``` class func newMeshesFromAsset(_ asset: MDLAsset, sourceMeshes sourceMeshes: AutoreleasingUnsafeMutablePointer<NSArray?>) throws -> [GLKMesh] ``` |
| To | ``` class func newMeshes(from asset: MDLAsset, sourceMeshes sourceMeshes: AutoreleasingUnsafeMutablePointer<NSArray?>?) throws -> [GLKMesh] ``` |

Modified [GLKMeshBuffer](https://developer.apple.com/documentation/glkit/glkmeshbuffer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKMeshBuffer : NSObject, MDLMeshBuffer {     var length: Int { get }     var allocator: GLKMeshBufferAllocator { get }     var glBufferName: GLuint { get }     var offset: Int { get }     var type: MDLMeshBufferType { get }     func zone() -> MDLMeshBufferZone? } ``` | MDLMeshBuffer |
| To | ``` class GLKMeshBuffer : NSObject, MDLMeshBuffer {     var length: Int { get }     var allocator: GLKMeshBufferAllocator { get }     var glBufferName: GLuint { get }     var offset: Int { get }     var type: MDLMeshBufferType { get }     func zone() -> MDLMeshBufferZone?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKMeshBuffer : CVarArg { } extension GLKMeshBuffer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLMeshBuffer |

Modified [GLKMeshBufferAllocator](https://developer.apple.com/documentation/glkit/glkmeshbufferallocator)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKMeshBufferAllocator : NSObject, MDLMeshBufferAllocator { } ``` | MDLMeshBufferAllocator |
| To | ``` class GLKMeshBufferAllocator : NSObject, MDLMeshBufferAllocator {     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKMeshBufferAllocator : CVarArg { } extension GLKMeshBufferAllocator : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, MDLMeshBufferAllocator |

Modified GLKQuaternion.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ i: Int) -> Float { get } ``` |
| To | ``` subscript(_ i: Int) -> Float { get } ``` |

Modified [GLKSkyboxEffect](https://developer.apple.com/documentation/glkit/glkskyboxeffect)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKSkyboxEffect : NSObject, GLKNamedEffect {     func prepareToDraw()     func draw()     var center: GLKVector3     var xSize: GLfloat     var ySize: GLfloat     var zSize: GLfloat     var textureCubeMap: GLKEffectPropertyTexture { get }     var transform: GLKEffectPropertyTransform { get }     var label: String? } ``` | GLKNamedEffect |
| To | ``` class GLKSkyboxEffect : NSObject, GLKNamedEffect {     func prepareToDraw()     func draw()     var center: GLKVector3     var xSize: GLfloat     var ySize: GLfloat     var zSize: GLfloat     var textureCubeMap: GLKEffectPropertyTexture { get }     var transform: GLKEffectPropertyTransform { get }     var label: String?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKSkyboxEffect : CVarArg { } extension GLKSkyboxEffect : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, GLKNamedEffect, Hashable |

Modified [GLKSubmesh](https://developer.apple.com/documentation/glkit/glksubmesh)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKSubmesh : NSObject {     init?()     var type: GLenum { get }     var mode: GLenum { get }     var elementCount: GLsizei { get }     var elementBuffer: GLKMeshBuffer { get }     weak var mesh: GLKMesh? { get }     var name: String { get } } ``` | -- |
| To | ``` class GLKSubmesh : NSObject {     init?()     var type: GLenum { get }     var mode: GLenum { get }     var elementCount: GLsizei { get }     var elementBuffer: GLKMeshBuffer { get }     weak var mesh: GLKMesh? { get }     var name: String { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKSubmesh : CVarArg { } extension GLKSubmesh : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GLKTextureEnvMode [enum]](https://developer.apple.com/documentation/glkit/glktextureenvmode)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKTextureEnvMode : GLint {     case Replace     case Modulate     case Decal } ``` |
| To | ``` enum GLKTextureEnvMode : GLint {     case replace     case modulate     case decal } ``` |

Modified [GLKTextureEnvMode.decal](https://developer.apple.com/documentation/glkit/glktextureenvmode/decal)

|  | Declaration |
| --- | --- |
| From | ``` case Decal ``` |
| To | ``` case decal ``` |

Modified [GLKTextureEnvMode.modulate](https://developer.apple.com/documentation/glkit/glktextureenvmode/glktextureenvmodemodulate)

|  | Declaration |
| --- | --- |
| From | ``` case Modulate ``` |
| To | ``` case modulate ``` |

Modified [GLKTextureEnvMode.replace](https://developer.apple.com/documentation/glkit/glktextureenvmode/glktextureenvmodereplace)

|  | Declaration |
| --- | --- |
| From | ``` case Replace ``` |
| To | ``` case replace ``` |

Modified [GLKTextureInfo](https://developer.apple.com/documentation/glkit/glktextureinfo)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKTextureInfo : NSObject, NSCopying {     var name: GLuint { get }     var target: GLenum { get }     var width: GLuint { get }     var height: GLuint { get }     var alphaState: GLKTextureInfoAlphaState { get }     var textureOrigin: GLKTextureInfoOrigin { get }     var containsMipmaps: Bool { get } } ``` | NSCopying |
| To | ``` class GLKTextureInfo : NSObject, NSCopying {     var name: GLuint { get }     var target: GLenum { get }     var width: GLuint { get }     var height: GLuint { get }     var depth: GLuint { get }     var alphaState: GLKTextureInfoAlphaState { get }     var textureOrigin: GLKTextureInfoOrigin { get }     var containsMipmaps: Bool { get }     var mimapLevelCount: GLuint { get }     var arrayLength: GLuint { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKTextureInfo : CVarArg { } extension GLKTextureInfo : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [GLKTextureInfoAlphaState [enum]](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKTextureInfoAlphaState : GLint {     case None     case NonPremultiplied     case Premultiplied } ``` |
| To | ``` enum GLKTextureInfoAlphaState : GLint {     case none     case nonPremultiplied     case premultiplied } ``` |

Modified [GLKTextureInfoAlphaState.none](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate/glktextureinfoalphastatenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [GLKTextureInfoAlphaState.nonPremultiplied](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate/nonpremultiplied)

|  | Declaration |
| --- | --- |
| From | ``` case NonPremultiplied ``` |
| To | ``` case nonPremultiplied ``` |

Modified [GLKTextureInfoAlphaState.premultiplied](https://developer.apple.com/documentation/glkit/glktextureinfoalphastate/premultiplied)

|  | Declaration |
| --- | --- |
| From | ``` case Premultiplied ``` |
| To | ``` case premultiplied ``` |

Modified [GLKTextureInfoOrigin [enum]](https://developer.apple.com/documentation/glkit/glktextureinfoorigin)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKTextureInfoOrigin : GLint {     case Unknown     case TopLeft     case BottomLeft } ``` |
| To | ``` enum GLKTextureInfoOrigin : GLint {     case unknown     case topLeft     case bottomLeft } ``` |

Modified [GLKTextureInfoOrigin.bottomLeft](https://developer.apple.com/documentation/glkit/glktextureinfoorigin/glktextureinfooriginbottomleft)

|  | Declaration |
| --- | --- |
| From | ``` case BottomLeft ``` |
| To | ``` case bottomLeft ``` |

Modified [GLKTextureInfoOrigin.topLeft](https://developer.apple.com/documentation/glkit/glktextureinfoorigin/glktextureinfoorigintopleft)

|  | Declaration |
| --- | --- |
| From | ``` case TopLeft ``` |
| To | ``` case topLeft ``` |

Modified [GLKTextureInfoOrigin.unknown](https://developer.apple.com/documentation/glkit/glktextureinfoorigin/glktextureinfooriginunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [GLKTextureLoader](https://developer.apple.com/documentation/glkit/glktextureloader)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKTextureLoader : NSObject {     class func textureWithContentsOfFile(_ path: String, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func textureWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func textureWithContentsOfData(_ data: NSData, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func textureWithCGImage(_ cgImage: CGImage, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func cubeMapWithContentsOfFiles(_ paths: [AnyObject], options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func cubeMapWithContentsOfFile(_ path: String, options options: [String : NSNumber]?) throws -> GLKTextureInfo     class func cubeMapWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?) throws -> GLKTextureInfo     init(sharegroup sharegroup: EAGLSharegroup)     func textureWithContentsOfFile(_ path: String, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func textureWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func textureWithContentsOfData(_ data: NSData, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func textureWithCGImage(_ cgImage: CGImage, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func cubeMapWithContentsOfFiles(_ paths: [AnyObject], options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func cubeMapWithContentsOfFile(_ path: String, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback)     func cubeMapWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) } ``` | -- |
| To | ``` class GLKTextureLoader : NSObject {     class func texture(withContentsOfFile path: String, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo     class func texture(withContentsOf url: URL, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo     class func texture(withName name: String, scaleFactor scaleFactor: CGFloat, bundle bundle: Bundle?, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo     class func texture(withContentsOf data: Data, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo     class func texture(with cgImage: CGImage, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo     class func cubeMap(withContentsOfFiles paths: [Any], options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo     class func cubeMap(withContentsOfFile path: String, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo     class func cubeMap(withContentsOf url: URL, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo     init(sharegroup sharegroup: EAGLSharegroup)     func texture(withContentsOfFile path: String, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback)     func texture(withContentsOf url: URL, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback)     func texture(withName name: String, scaleFactor scaleFactor: CGFloat, bundle bundle: Bundle?, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback)     func texture(withContentsOf data: Data, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback)     func texture(with cgImage: CGImage, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback)     func cubeMap(withContentsOfFiles paths: [Any], options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback)     func cubeMap(withContentsOfFile path: String, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback)     func cubeMap(withContentsOf url: URL, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKTextureLoader : CVarArg { } extension GLKTextureLoader : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GLKTextureLoader.cubeMap(withContentsOf: URL, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488743-cubemapwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` class func cubeMapWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |
| To | ``` class func cubeMap(withContentsOf url: URL, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.cubeMap(withContentsOf: URL, options: [String : NSNumber]?, queue: DispatchQueue?, completionHandler: GLKit.GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488926-cubemapwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` func cubeMapWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |
| To | ``` func cubeMap(withContentsOf url: URL, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.cubeMap(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488848-cubemapwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` class func cubeMapWithContentsOfFile(_ path: String, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |
| To | ``` class func cubeMap(withContentsOfFile path: String, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.cubeMap(withContentsOfFile: String, options: [String : NSNumber]?, queue: DispatchQueue?, completionHandler: GLKit.GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488617-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` func cubeMapWithContentsOfFile(_ path: String, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |
| To | ``` func cubeMap(withContentsOfFile path: String, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488810-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` class func cubeMapWithContentsOfFiles(_ paths: [AnyObject], options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |
| To | ``` class func cubeMap(withContentsOfFiles paths: [Any], options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?, queue: DispatchQueue?, completionHandler: GLKit.GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488854-cubemap)

|  | Declaration |
| --- | --- |
| From | ``` func cubeMapWithContentsOfFiles(_ paths: [AnyObject], options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |
| To | ``` func cubeMap(withContentsOfFiles paths: [Any], options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.texture(with: CGImage, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488673-texture)

|  | Declaration |
| --- | --- |
| From | ``` class func textureWithCGImage(_ cgImage: CGImage, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |
| To | ``` class func texture(with cgImage: CGImage, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.texture(with: CGImage, options: [String : NSNumber]?, queue: DispatchQueue?, completionHandler: GLKit.GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488861-texturewithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` func textureWithCGImage(_ cgImage: CGImage, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |
| To | ``` func texture(with cgImage: CGImage, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.texture(withContentsOf: Data, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1489081-texturewithcontentsofdata)

|  | Declaration |
| --- | --- |
| From | ``` class func textureWithContentsOfData(_ data: NSData, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |
| To | ``` class func texture(withContentsOf data: Data, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.texture(withContentsOf: URL, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1489025-texturewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` class func textureWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |
| To | ``` class func texture(withContentsOf url: URL, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.texture(withContentsOf: URL, options: [String : NSNumber]?, queue: DispatchQueue?, completionHandler: GLKit.GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488621-texturewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` func textureWithContentsOfURL(_ url: NSURL, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |
| To | ``` func texture(withContentsOf url: URL, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.texture(withContentsOf: Data, options: [String : NSNumber]?, queue: DispatchQueue?, completionHandler: GLKit.GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1488905-texturewithcontentsofdata)

|  | Declaration |
| --- | --- |
| From | ``` func textureWithContentsOfData(_ data: NSData, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |
| To | ``` func texture(withContentsOf data: Data, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoader.texture(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo [class]](https://developer.apple.com/documentation/glkit/glktextureloader/1488932-texture)

|  | Declaration |
| --- | --- |
| From | ``` class func textureWithContentsOfFile(_ path: String, options options: [String : NSNumber]?) throws -> GLKTextureInfo ``` |
| To | ``` class func texture(withContentsOfFile path: String, options options: [String : NSNumber]? = nil) throws -> GLKTextureInfo ``` |

Modified [GLKTextureLoader.texture(withContentsOfFile: String, options: [String : NSNumber]?, queue: DispatchQueue?, completionHandler: GLKit.GLKTextureLoaderCallback)](https://developer.apple.com/documentation/glkit/glktextureloader/1489064-texture)

|  | Declaration |
| --- | --- |
| From | ``` func textureWithContentsOfFile(_ path: String, options options: [String : NSNumber]?, queue queue: dispatch_queue_t?, completionHandler block: GLKTextureLoaderCallback) ``` |
| To | ``` func texture(withContentsOfFile path: String, options options: [String : NSNumber]? = nil, queue queue: DispatchQueue?, completionHandler block: GLKit.GLKTextureLoaderCallback) ``` |

Modified [GLKTextureLoaderError.Code [enum]](https://developer.apple.com/documentation/glkit/glktextureloadererror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKTextureLoaderError : GLuint {     case FileOrURLNotFound     case InvalidNSData     case InvalidCGImage     case UnknownPathType     case UnknownFileType     case PVRAtlasUnsupported     case CubeMapInvalidNumFiles     case CompressedTextureUpload     case UncompressedTextureUpload     case UnsupportedCubeMapDimensions     case UnsupportedBitDepth     case UnsupportedPVRFormat     case DataPreprocessingFailure     case MipmapUnsupported     case UnsupportedOrientation     case ReorientationFailure     case AlphaPremultiplicationFailure     case InvalidEAGLContext     case IncompatibleFormatSRGB } ``` |
| To | ``` enum Code : GLuint {         typealias _ErrorType = GLKTextureLoaderError         case fileOrURLNotFound         case invalidNSData         case invalidCGImage         case unknownPathType         case unknownFileType         case pvrAtlasUnsupported         case cubeMapInvalidNumFiles         case compressedTextureUpload         case uncompressedTextureUpload         case unsupportedCubeMapDimensions         case unsupportedBitDepth         case unsupportedPVRFormat         case dataPreprocessingFailure         case mipmapUnsupported         case unsupportedOrientation         case reorientationFailure         case alphaPremultiplicationFailure         case invalidEAGLContext         case incompatibleFormatSRGB         case unsupportedTextureTarget     } ``` |

Modified [GLKTextureLoaderError.Code.alphaPremultiplicationFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererroralphapremultiplicationfailure)

|  | Declaration |
| --- | --- |
| From | ``` case AlphaPremultiplicationFailure ``` |
| To | ``` case alphaPremultiplicationFailure ``` |

Modified [GLKTextureLoaderError.Code.compressedTextureUpload](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorcompressedtextureupload)

|  | Declaration |
| --- | --- |
| From | ``` case CompressedTextureUpload ``` |
| To | ``` case compressedTextureUpload ``` |

Modified [GLKTextureLoaderError.Code.cubeMapInvalidNumFiles](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorcubemapinvalidnumfiles)

|  | Declaration |
| --- | --- |
| From | ``` case CubeMapInvalidNumFiles ``` |
| To | ``` case cubeMapInvalidNumFiles ``` |

Modified [GLKTextureLoaderError.Code.dataPreprocessingFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/datapreprocessingfailure)

|  | Declaration |
| --- | --- |
| From | ``` case DataPreprocessingFailure ``` |
| To | ``` case dataPreprocessingFailure ``` |

Modified [GLKTextureLoaderError.Code.fileOrURLNotFound](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorfileorurlnotfound)

|  | Declaration |
| --- | --- |
| From | ``` case FileOrURLNotFound ``` |
| To | ``` case fileOrURLNotFound ``` |

Modified [GLKTextureLoaderError.Code.incompatibleFormatSRGB](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorincompatibleformatsrgb)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case IncompatibleFormatSRGB ``` | iOS 8.0 |
| To | ``` case incompatibleFormatSRGB ``` | iOS 10.0 |

Modified [GLKTextureLoaderError.Code.invalidCGImage](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorinvalidcgimage)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidCGImage ``` |
| To | ``` case invalidCGImage ``` |

Modified [GLKTextureLoaderError.Code.invalidEAGLContext](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/invalideaglcontext)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidEAGLContext ``` |
| To | ``` case invalidEAGLContext ``` |

Modified [GLKTextureLoaderError.Code.invalidNSData](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/invalidnsdata)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidNSData ``` |
| To | ``` case invalidNSData ``` |

Modified [GLKTextureLoaderError.Code.mipmapUnsupported](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/mipmapunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case MipmapUnsupported ``` |
| To | ``` case mipmapUnsupported ``` |

Modified [GLKTextureLoaderError.Code.pvrAtlasUnsupported](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorpvratlasunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case PVRAtlasUnsupported ``` |
| To | ``` case pvrAtlasUnsupported ``` |

Modified [GLKTextureLoaderError.Code.reorientationFailure](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorreorientationfailure)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ReorientationFailure ``` | iOS 8.0 |
| To | ``` case reorientationFailure ``` | iOS 10.0 |

Modified [GLKTextureLoaderError.Code.uncompressedTextureUpload](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererroruncompressedtextureupload)

|  | Declaration |
| --- | --- |
| From | ``` case UncompressedTextureUpload ``` |
| To | ``` case uncompressedTextureUpload ``` |

Modified [GLKTextureLoaderError.Code.unknownFileType](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorunknownfiletype)

|  | Declaration |
| --- | --- |
| From | ``` case UnknownFileType ``` |
| To | ``` case unknownFileType ``` |

Modified [GLKTextureLoaderError.Code.unknownPathType](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorunknownpathtype)

|  | Declaration |
| --- | --- |
| From | ``` case UnknownPathType ``` |
| To | ``` case unknownPathType ``` |

Modified [GLKTextureLoaderError.Code.unsupportedBitDepth](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorunsupportedbitdepth)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedBitDepth ``` |
| To | ``` case unsupportedBitDepth ``` |

Modified [GLKTextureLoaderError.Code.unsupportedCubeMapDimensions](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/unsupportedcubemapdimensions)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedCubeMapDimensions ``` |
| To | ``` case unsupportedCubeMapDimensions ``` |

Modified [GLKTextureLoaderError.Code.unsupportedOrientation](https://developer.apple.com/documentation/glkit/glktextureloadererror/code/unsupportedorientation)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedOrientation ``` |
| To | ``` case unsupportedOrientation ``` |

Modified [GLKTextureLoaderError.Code.unsupportedPVRFormat](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorunsupportedpvrformat)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedPVRFormat ``` |
| To | ``` case unsupportedPVRFormat ``` |

Modified [GLKTextureTarget [enum]](https://developer.apple.com/documentation/glkit/glktexturetarget)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKTextureTarget : GLenum {     case Target2D     case TargetCubeMap     case TargetCt } ``` |
| To | ``` enum GLKTextureTarget : GLenum {     case target2D     case targetCubeMap     case targetCt } ``` |

Modified [GLKTextureTarget.target2D](https://developer.apple.com/documentation/glkit/glktexturetarget/glktexturetarget2d)

|  | Declaration |
| --- | --- |
| From | ``` case Target2D ``` |
| To | ``` case target2D ``` |

Modified [GLKTextureTarget.targetCt](https://developer.apple.com/documentation/glkit/glktexturetarget/targetct)

|  | Declaration |
| --- | --- |
| From | ``` case TargetCt ``` |
| To | ``` case targetCt ``` |

Modified [GLKTextureTarget.targetCubeMap](https://developer.apple.com/documentation/glkit/glktexturetarget/glktexturetargetcubemap)

|  | Declaration |
| --- | --- |
| From | ``` case TargetCubeMap ``` |
| To | ``` case targetCubeMap ``` |

Modified GLKVector2.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ i: Int) -> Float { get } ``` |
| To | ``` subscript(_ i: Int) -> Float { get } ``` |

Modified GLKVector3.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ i: Int) -> Float { get } ``` |
| To | ``` subscript(_ i: Int) -> Float { get } ``` |

Modified GLKVector4.subscript(_: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ i: Int) -> Float { get } ``` |
| To | ``` subscript(_ i: Int) -> Float { get } ``` |

Modified [GLKVertexAttrib [enum]](https://developer.apple.com/documentation/glkit/glkvertexattrib)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKVertexAttrib : GLint {     case Position     case Normal     case Color     case TexCoord0     case TexCoord1 } ``` |
| To | ``` enum GLKVertexAttrib : GLint {     case position     case normal     case color     case texCoord0     case texCoord1 } ``` |

Modified [GLKVertexAttrib.color](https://developer.apple.com/documentation/glkit/glkvertexattrib/glkvertexattribcolor)

|  | Declaration |
| --- | --- |
| From | ``` case Color ``` |
| To | ``` case color ``` |

Modified [GLKVertexAttrib.normal](https://developer.apple.com/documentation/glkit/glkvertexattrib/normal)

|  | Declaration |
| --- | --- |
| From | ``` case Normal ``` |
| To | ``` case normal ``` |

Modified [GLKVertexAttrib.position](https://developer.apple.com/documentation/glkit/glkvertexattrib/glkvertexattribposition)

|  | Declaration |
| --- | --- |
| From | ``` case Position ``` |
| To | ``` case position ``` |

Modified [GLKVertexAttrib.texCoord0](https://developer.apple.com/documentation/glkit/glkvertexattrib/glkvertexattribtexcoord0)

|  | Declaration |
| --- | --- |
| From | ``` case TexCoord0 ``` |
| To | ``` case texCoord0 ``` |

Modified [GLKVertexAttrib.texCoord1](https://developer.apple.com/documentation/glkit/glkvertexattrib/glkvertexattribtexcoord1)

|  | Declaration |
| --- | --- |
| From | ``` case TexCoord1 ``` |
| To | ``` case texCoord1 ``` |

Modified [GLKView](https://developer.apple.com/documentation/glkit/glkview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKView : UIView, NSCoding {     init(frame frame: CGRect, context context: EAGLContext)     @IBOutlet unowned(unsafe) var delegate: GLKViewDelegate?     var context: EAGLContext     var drawableWidth: Int { get }     var drawableHeight: Int { get }     var drawableColorFormat: GLKViewDrawableColorFormat     var drawableDepthFormat: GLKViewDrawableDepthFormat     var drawableStencilFormat: GLKViewDrawableStencilFormat     var drawableMultisample: GLKViewDrawableMultisample     func bindDrawable()     func deleteDrawable()     var snapshot: UIImage { get }     var enableSetNeedsDisplay: Bool     func display() } ``` | NSCoding |
| To | ``` class GLKView : UIView, NSCoding {     init(frame frame: CGRect, context context: EAGLContext)     @IBOutlet unowned(unsafe) var delegate: GLKViewDelegate?     var context: EAGLContext     var drawableWidth: Int { get }     var drawableHeight: Int { get }     var drawableColorFormat: GLKViewDrawableColorFormat     var drawableDepthFormat: GLKViewDrawableDepthFormat     var drawableStencilFormat: GLKViewDrawableStencilFormat     var drawableMultisample: GLKViewDrawableMultisample     func bindDrawable()     func deleteDrawable()     var snapshot: UIImage { get }     var enableSetNeedsDisplay: Bool     func display()     func viewPrintFormatter() -> UIViewPrintFormatter     func draw(_ rect: CGRect, for formatter: UIViewPrintFormatter)     func endEditing(_ force: Bool) -> Bool     func snapshotView(afterScreenUpdates afterUpdates: Bool) -> UIView?     func resizableSnapshotView(from rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView?     func drawHierarchy(in rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool     var restorationIdentifier: String?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func constraintsAffectingLayout(for axis: UILayoutConstraintAxis) -> [NSLayoutConstraint]     var hasAmbiguousLayout: Bool { get }     func exerciseAmbiguityInLayout()     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get }     var layoutGuides: [UILayoutGuide] { get }     func addLayoutGuide(_ layoutGuide: UILayoutGuide)     func removeLayoutGuide(_ layoutGuide: UILayoutGuide)     func systemLayoutSizeFitting(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFitting(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize     func alignmentRect(forFrame frame: CGRect) -> CGRect     func frame(forAlignmentRect alignmentRect: CGRect) -> CGRect     var alignmentRectInsets: UIEdgeInsets { get }     func forBaselineLayout() -> UIView     var forFirstBaselineLayout: UIView { get }     var forLastBaselineLayout: UIView { get }     var intrinsicContentSize: CGSize { get }     func invalidateIntrinsicContentSize()     func contentHuggingPriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     func contentCompressionResistancePriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     var translatesAutoresizingMaskIntoConstraints: Bool     class var requiresConstraintBasedLayout: Bool { get }     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints()     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint])     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [UIMotionEffect]     var gestureRecognizers: [UIGestureRecognizer]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool     class func animateKeyframes(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewKeyframeAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func addKeyframe(withRelativeStartTime frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(with view: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(from fromView: UIView, to toView: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], completion completion: (@escaping (Bool) -> Void)? = nil)     class func perform(_ animation: UISystemAnimation, on views: [UIView], options options: UIViewAnimationOptions = [], animations parallelAnimations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func beginAnimations(_ animationID: String?, context context: UnsafeMutableRawPointer?)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: Any?)     class func setAnimationWillStart(_ selector: Selector?)     class func setAnimationDidStop(_ selector: Selector?)     class func setAnimationDuration(_ duration: TimeInterval)     class func setAnimationDelay(_ delay: TimeInterval)     class func setAnimationStart(_ startDate: Date)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, for view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class var areAnimationsEnabled: Bool { get }     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void)     class var inheritedAnimationDuration: TimeInterval { get }     func draw(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplay(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var isOpaque: Bool     var clearsContextBeforeDrawing: Bool     var isHidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var mask: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange()     var superview: UIView? { get }     var subviews: [UIView] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, at index: Int)     func exchangeSubview(at index1: Int, withSubviewAt index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubview(toFront view: UIView)     func sendSubview(toBack view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMove(toSuperview newSuperview: UIView?)     func didMoveToSuperview()     func willMove(toWindow newWindow: UIWindow?)     func didMoveToWindow()     func isDescendant(of view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange()     var layoutMarginsGuide: UILayoutGuide { get }     var readableContentGuide: UILayoutGuide { get }     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var isMultipleTouchEnabled: Bool     var isExclusiveTouch: Bool     func hitTest(_ point: CGPoint, with event: UIEvent?) -> UIView?     func point(inside point: CGPoint, with event: UIEvent?) -> Bool     func convert(_ point: CGPoint, to view: UIView?) -> CGPoint     func convert(_ point: CGPoint, from view: UIView?) -> CGPoint     func convert(_ rect: CGRect, to view: UIView?) -> CGRect     func convert(_ rect: CGRect, from view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit()     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKView : UIAccessibilityIdentification { } extension GLKView : CVarArg { } extension GLKView : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, UIAccessibilityIdentification |

Modified [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GLKViewController : UIViewController, NSCoding, GLKViewDelegate {     @IBOutlet unowned(unsafe) var delegate: GLKViewControllerDelegate?     var preferredFramesPerSecond: Int     var framesPerSecond: Int { get }     var paused: Bool     var framesDisplayed: Int { get }     var timeSinceFirstResume: NSTimeInterval { get }     var timeSinceLastResume: NSTimeInterval { get }     var timeSinceLastUpdate: NSTimeInterval { get }     var timeSinceLastDraw: NSTimeInterval { get }     var pauseOnWillResignActive: Bool     var resumeOnDidBecomeActive: Bool } ``` | GLKViewDelegate, NSCoding |
| To | ``` class GLKViewController : UIViewController, NSCoding, GLKViewDelegate {     @IBOutlet unowned(unsafe) var delegate: GLKViewControllerDelegate?     var preferredFramesPerSecond: Int     var framesPerSecond: Int { get }     var isPaused: Bool     var framesDisplayed: Int { get }     var timeSinceFirstResume: TimeInterval { get }     var timeSinceLastResume: TimeInterval { get }     var timeSinceLastUpdate: TimeInterval { get }     var timeSinceLastDraw: TimeInterval { get }     var pauseOnWillResignActive: Bool     var resumeOnDidBecomeActive: Bool     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GLKViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension GLKViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension GLKViewController : CVarArg { } extension GLKViewController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, GLKViewDelegate, Hashable, NSCoding, NSExtensionRequestHandling, UIStateRestoring |

Modified [GLKViewController.isPaused](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620712-ispaused)

|  | Declaration |
| --- | --- |
| From | ``` var paused: Bool ``` |
| To | ``` var isPaused: Bool ``` |

Modified [GLKViewController.timeSinceFirstResume](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620709-timesincefirstresume)

|  | Declaration |
| --- | --- |
| From | ``` var timeSinceFirstResume: NSTimeInterval { get } ``` |
| To | ``` var timeSinceFirstResume: TimeInterval { get } ``` |

Modified [GLKViewController.timeSinceLastDraw](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620725-timesincelastdraw)

|  | Declaration |
| --- | --- |
| From | ``` var timeSinceLastDraw: NSTimeInterval { get } ``` |
| To | ``` var timeSinceLastDraw: TimeInterval { get } ``` |

Modified [GLKViewController.timeSinceLastResume](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620706-timesincelastresume)

|  | Declaration |
| --- | --- |
| From | ``` var timeSinceLastResume: NSTimeInterval { get } ``` |
| To | ``` var timeSinceLastResume: TimeInterval { get } ``` |

Modified [GLKViewController.timeSinceLastUpdate](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620726-timesincelastupdate)

|  | Declaration |
| --- | --- |
| From | ``` var timeSinceLastUpdate: NSTimeInterval { get } ``` |
| To | ``` var timeSinceLastUpdate: TimeInterval { get } ``` |

Modified [GLKViewDelegate](https://developer.apple.com/documentation/glkit/glkviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GLKViewDelegate : NSObjectProtocol {     func glkView(_ view: GLKView, drawInRect rect: CGRect) } ``` |
| To | ``` protocol GLKViewDelegate : NSObjectProtocol {     func glkView(_ view: GLKView, drawIn rect: CGRect) } ``` |

Modified [GLKViewDelegate.glkView(_: GLKView, drawIn: CGRect)](https://developer.apple.com/documentation/glkit/glkviewdelegate/1615595-glkview)

|  | Declaration |
| --- | --- |
| From | ``` func glkView(_ view: GLKView, drawInRect rect: CGRect) ``` |
| To | ``` func glkView(_ view: GLKView, drawIn rect: CGRect) ``` |

Modified [GLKViewDrawableDepthFormat [enum]](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKViewDrawableDepthFormat : GLint {     case FormatNone     case Format16     case Format24 } ``` |
| To | ``` enum GLKViewDrawableDepthFormat : GLint {     case formatNone     case format16     case format24 } ``` |

Modified [GLKViewDrawableDepthFormat.format16](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat/format16)

|  | Declaration |
| --- | --- |
| From | ``` case Format16 ``` |
| To | ``` case format16 ``` |

Modified [GLKViewDrawableDepthFormat.format24](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat/format24)

|  | Declaration |
| --- | --- |
| From | ``` case Format24 ``` |
| To | ``` case format24 ``` |

Modified [GLKViewDrawableDepthFormat.formatNone](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat/formatnone)

|  | Declaration |
| --- | --- |
| From | ``` case FormatNone ``` |
| To | ``` case formatNone ``` |

Modified [GLKViewDrawableMultisample [enum]](https://developer.apple.com/documentation/glkit/glkviewdrawablemultisample)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKViewDrawableMultisample : GLint {     case MultisampleNone     case Multisample4X } ``` |
| To | ``` enum GLKViewDrawableMultisample : GLint {     case multisampleNone     case multisample4X } ``` |

Modified [GLKViewDrawableMultisample.multisample4X](https://developer.apple.com/documentation/glkit/glkviewdrawablemultisample/glkviewdrawablemultisample4x)

|  | Declaration |
| --- | --- |
| From | ``` case Multisample4X ``` |
| To | ``` case multisample4X ``` |

Modified [GLKViewDrawableMultisample.multisampleNone](https://developer.apple.com/documentation/glkit/glkviewdrawablemultisample/glkviewdrawablemultisamplenone)

|  | Declaration |
| --- | --- |
| From | ``` case MultisampleNone ``` |
| To | ``` case multisampleNone ``` |

Modified [GLKViewDrawableStencilFormat [enum]](https://developer.apple.com/documentation/glkit/glkviewdrawablestencilformat)

|  | Declaration |
| --- | --- |
| From | ``` enum GLKViewDrawableStencilFormat : GLint {     case FormatNone     case Format8 } ``` |
| To | ``` enum GLKViewDrawableStencilFormat : GLint {     case formatNone     case format8 } ``` |

Modified [GLKViewDrawableStencilFormat.format8](https://developer.apple.com/documentation/glkit/glkviewdrawablestencilformat/glkviewdrawablestencilformat8)

|  | Declaration |
| --- | --- |
| From | ``` case Format8 ``` |
| To | ``` case format8 ``` |

Modified [GLKViewDrawableStencilFormat.formatNone](https://developer.apple.com/documentation/glkit/glkviewdrawablestencilformat/glkviewdrawablestencilformatnone)

|  | Declaration |
| --- | --- |
| From | ``` case FormatNone ``` |
| To | ``` case formatNone ``` |

Modified GLKEffectPropertyPrvPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias GLKEffectPropertyPrvPtr = COpaquePointer ``` |
| To | ``` typealias GLKEffectPropertyPrvPtr = OpaquePointer ``` |

Modified [GLKMathUnproject(_: GLKVector3, _: GLKMatrix4, _: GLKMatrix4, _: UnsafeMutablePointer<Int32>, _: UnsafeMutablePointer<Bool>?) -> GLKVector3](https://developer.apple.com/documentation/glkit/1488720-glkmathunproject)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMathUnproject(_ window: GLKVector3, _ model: GLKMatrix4, _ projection: GLKMatrix4, _ viewport: UnsafeMutablePointer<Int32>, _ success: UnsafeMutablePointer<Bool>) -> GLKVector3 ``` |
| To | ``` func GLKMathUnproject(_ window: GLKVector3, _ model: GLKMatrix4, _ projection: GLKMatrix4, _ viewport: UnsafeMutablePointer<Int32>, _ success: UnsafeMutablePointer<Bool>?) -> GLKVector3 ``` |

Modified [GLKMatrix3Invert(_: GLKMatrix3, _: UnsafeMutablePointer<Bool>!) -> GLKMatrix3](https://developer.apple.com/documentation/glkit/1488816-glkmatrix3invert)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrix3Invert(_ matrix: GLKMatrix3, _ isInvertible: UnsafeMutablePointer<Bool>) -> GLKMatrix3 ``` |
| To | ``` func GLKMatrix3Invert(_ matrix: GLKMatrix3, _ isInvertible: UnsafeMutablePointer<Bool>!) -> GLKMatrix3 ``` |

Modified [GLKMatrix3InvertAndTranspose(_: GLKMatrix3, _: UnsafeMutablePointer<Bool>!) -> GLKMatrix3](https://developer.apple.com/documentation/glkit/1488692-glkmatrix3invertandtranspose)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrix3InvertAndTranspose(_ matrix: GLKMatrix3, _ isInvertible: UnsafeMutablePointer<Bool>) -> GLKMatrix3 ``` |
| To | ``` func GLKMatrix3InvertAndTranspose(_ matrix: GLKMatrix3, _ isInvertible: UnsafeMutablePointer<Bool>!) -> GLKMatrix3 ``` |

Modified [GLKMatrix3MakeWithArray(_: UnsafeMutablePointer<Float>!) -> GLKMatrix3](https://developer.apple.com/documentation/glkit/1488889-glkmatrix3makewitharray)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrix3MakeWithArray(_ values: UnsafeMutablePointer<Float>) -> GLKMatrix3 ``` |
| To | ``` func GLKMatrix3MakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKMatrix3 ``` |

Modified [GLKMatrix3MakeWithArrayAndTranspose(_: UnsafeMutablePointer<Float>!) -> GLKMatrix3](https://developer.apple.com/documentation/glkit/1488737-glkmatrix3makewitharrayandtransp)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrix3MakeWithArrayAndTranspose(_ values: UnsafeMutablePointer<Float>) -> GLKMatrix3 ``` |
| To | ``` func GLKMatrix3MakeWithArrayAndTranspose(_ values: UnsafeMutablePointer<Float>!) -> GLKMatrix3 ``` |

Modified [GLKMatrix4Invert(_: GLKMatrix4, _: UnsafeMutablePointer<Bool>?) -> GLKMatrix4](https://developer.apple.com/documentation/glkit/1488859-glkmatrix4invert)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrix4Invert(_ matrix: GLKMatrix4, _ isInvertible: UnsafeMutablePointer<Bool>) -> GLKMatrix4 ``` |
| To | ``` func GLKMatrix4Invert(_ matrix: GLKMatrix4, _ isInvertible: UnsafeMutablePointer<Bool>?) -> GLKMatrix4 ``` |

Modified [GLKMatrix4InvertAndTranspose(_: GLKMatrix4, _: UnsafeMutablePointer<Bool>?) -> GLKMatrix4](https://developer.apple.com/documentation/glkit/1489040-glkmatrix4invertandtranspose)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrix4InvertAndTranspose(_ matrix: GLKMatrix4, _ isInvertible: UnsafeMutablePointer<Bool>) -> GLKMatrix4 ``` |
| To | ``` func GLKMatrix4InvertAndTranspose(_ matrix: GLKMatrix4, _ isInvertible: UnsafeMutablePointer<Bool>?) -> GLKMatrix4 ``` |

Modified [GLKMatrix4MakeWithArray(_: UnsafeMutablePointer<Float>!) -> GLKMatrix4](https://developer.apple.com/documentation/glkit/1488687-glkmatrix4makewitharray)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrix4MakeWithArray(_ values: UnsafeMutablePointer<Float>) -> GLKMatrix4 ``` |
| To | ``` func GLKMatrix4MakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKMatrix4 ``` |

Modified [GLKMatrix4MakeWithArrayAndTranspose(_: UnsafeMutablePointer<Float>!) -> GLKMatrix4](https://developer.apple.com/documentation/glkit/1489079-glkmatrix4makewitharrayandtransp)

|  | Declaration |
| --- | --- |
| From | ``` func GLKMatrix4MakeWithArrayAndTranspose(_ values: UnsafeMutablePointer<Float>) -> GLKMatrix4 ``` |
| To | ``` func GLKMatrix4MakeWithArrayAndTranspose(_ values: UnsafeMutablePointer<Float>!) -> GLKMatrix4 ``` |

Modified [GLKQuaternionMakeWithArray(_: UnsafeMutablePointer<Float>!) -> GLKQuaternion](https://developer.apple.com/documentation/glkit/1476889-glkquaternionmakewitharray)

|  | Declaration |
| --- | --- |
| From | ``` func GLKQuaternionMakeWithArray(_ values: UnsafeMutablePointer<Float>) -> GLKQuaternion ``` |
| To | ``` func GLKQuaternionMakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKQuaternion ``` |

Modified [GLKTextureLoaderCallback](https://developer.apple.com/documentation/glkit/glktextureloadercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias GLKTextureLoaderCallback = (GLKTextureInfo?, NSError?) -> Void ``` |
| To | ``` typealias GLKTextureLoaderCallback = (GLKTextureInfo?, Error?) -> Swift.Void ``` |

Modified [GLKVector2MakeWithArray(_: UnsafeMutablePointer<Float>!) -> GLKVector2](https://developer.apple.com/documentation/glkit/1391980-glkvector2makewitharray)

|  | Declaration |
| --- | --- |
| From | ``` func GLKVector2MakeWithArray(_ values: UnsafeMutablePointer<Float>) -> GLKVector2 ``` |
| To | ``` func GLKVector2MakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKVector2 ``` |

Modified [GLKVector3MakeWithArray(_: UnsafeMutablePointer<Float>!) -> GLKVector3](https://developer.apple.com/documentation/glkit/1393760-glkvector3makewitharray)

|  | Declaration |
| --- | --- |
| From | ``` func GLKVector3MakeWithArray(_ values: UnsafeMutablePointer<Float>) -> GLKVector3 ``` |
| To | ``` func GLKVector3MakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKVector3 ``` |

Modified [GLKVector4MakeWithArray(_: UnsafeMutablePointer<Float>!) -> GLKVector4](https://developer.apple.com/documentation/glkit/1403358-glkvector4makewitharray)

|  | Declaration |
| --- | --- |
| From | ``` func GLKVector4MakeWithArray(_ values: UnsafeMutablePointer<Float>) -> GLKVector4 ``` |
| To | ``` func GLKVector4MakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKVector4 ``` |

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

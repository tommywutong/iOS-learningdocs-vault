---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/OpenGLES.html
archived_at: '2026-07-18T02:55:35.368514Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# OpenGLES Changes for Swift

### OpenGLES

Added [EAGLContext.presentRenderbuffer(_: Int, atTime: CFTimeInterval) -> Bool](https://developer.apple.com/documentation/opengles/eaglcontext/1648214-presentrenderbuffer)Modified [EAGLContext](https://developer.apple.com/documentation/opengles/eaglcontext)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EAGLContext : NSObject {     convenience init!()     convenience init!(API api: EAGLRenderingAPI)     init!(API api: EAGLRenderingAPI, sharegroup sharegroup: EAGLSharegroup!)     class func setCurrentContext(_ context: EAGLContext!) -> Bool     class func currentContext() -> EAGLContext!     var API: EAGLRenderingAPI { get }     var sharegroup: EAGLSharegroup! { get }     var debugLabel: String!     var multiThreaded: Bool } extension EAGLContext {     func renderbufferStorage(_ target: Int, fromDrawable drawable: EAGLDrawable!) -> Bool     func presentRenderbuffer(_ target: Int) -> Bool } ``` | -- |
| To | ``` class EAGLContext : NSObject {     convenience init!()     convenience init!(api api: EAGLRenderingAPI)     init!(api api: EAGLRenderingAPI, sharegroup sharegroup: EAGLSharegroup!)     class func setCurrent(_ context: EAGLContext!) -> Bool     class func current() -> EAGLContext!     var api: EAGLRenderingAPI { get }     var sharegroup: EAGLSharegroup! { get }     var debugLabel: String!     var isMultiThreaded: Bool     func renderbufferStorage(_ target: Int, from drawable: EAGLDrawable!) -> Bool     func presentRenderbuffer(_ target: Int) -> Bool     func presentRenderbuffer(_ target: Int, atTime presentationTime: CFTimeInterval) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension EAGLContext : CVarArg { } extension EAGLContext : Equatable, Hashable {     var hashValue: Int { get } } extension EAGLContext {     func renderbufferStorage(_ target: Int, from drawable: EAGLDrawable!) -> Bool     func presentRenderbuffer(_ target: Int) -> Bool     func presentRenderbuffer(_ target: Int, atTime presentationTime: CFTimeInterval) -> Bool } ``` | CVarArg, Equatable, Hashable |

Modified [EAGLContext.api](https://developer.apple.com/documentation/opengles/eaglcontext/1624885-api)

|  | Declaration |
| --- | --- |
| From | ``` var API: EAGLRenderingAPI { get } ``` |
| To | ``` var api: EAGLRenderingAPI { get } ``` |

Modified [EAGLContext.current() -> EAGLContext! [class]](https://developer.apple.com/documentation/opengles/eaglcontext/1624880-current)

|  | Declaration |
| --- | --- |
| From | ``` class func currentContext() -> EAGLContext! ``` |
| To | ``` class func current() -> EAGLContext! ``` |

Modified [EAGLContext.init(api: EAGLRenderingAPI)](https://developer.apple.com/documentation/opengles/eaglcontext/1624895-initwithapi)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(API api: EAGLRenderingAPI) ``` |
| To | ``` convenience init!(api api: EAGLRenderingAPI) ``` |

Modified [EAGLContext.init(api: EAGLRenderingAPI, sharegroup: EAGLSharegroup!)](https://developer.apple.com/documentation/opengles/eaglcontext/1624877-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(API api: EAGLRenderingAPI, sharegroup sharegroup: EAGLSharegroup!) ``` |
| To | ``` init!(api api: EAGLRenderingAPI, sharegroup sharegroup: EAGLSharegroup!) ``` |

Modified [EAGLContext.isMultiThreaded](https://developer.apple.com/documentation/opengles/eaglcontext/1624881-multithreaded)

|  | Declaration |
| --- | --- |
| From | ``` var multiThreaded: Bool ``` |
| To | ``` var isMultiThreaded: Bool ``` |

Modified [EAGLContext.renderbufferStorage(_: Int, from: EAGLDrawable!) -> Bool](https://developer.apple.com/documentation/opengles/eaglcontext/1622262-renderbufferstorage)

|  | Declaration |
| --- | --- |
| From | ``` func renderbufferStorage(_ target: Int, fromDrawable drawable: EAGLDrawable!) -> Bool ``` |
| To | ``` func renderbufferStorage(_ target: Int, from drawable: EAGLDrawable!) -> Bool ``` |

Modified [EAGLContext.setCurrent(_: EAGLContext!) -> Bool [class]](https://developer.apple.com/documentation/opengles/eaglcontext/1624882-setcurrent)

|  | Declaration |
| --- | --- |
| From | ``` class func setCurrentContext(_ context: EAGLContext!) -> Bool ``` |
| To | ``` class func setCurrent(_ context: EAGLContext!) -> Bool ``` |

Modified [EAGLDrawable](https://developer.apple.com/documentation/opengles/eagldrawable)

|  | Declaration |
| --- | --- |
| From | ``` protocol EAGLDrawable {     var drawableProperties: [NSObject : AnyObject]! { get set } } ``` |
| To | ``` protocol EAGLDrawable {     var drawableProperties: [AnyHashable : Any]! { get set } } ``` |

Modified [EAGLDrawable.drawableProperties](https://developer.apple.com/documentation/opengles/eagldrawable/1622263-drawableproperties)

|  | Declaration |
| --- | --- |
| From | ``` var drawableProperties: [NSObject : AnyObject]! { get set } ``` |
| To | ``` var drawableProperties: [AnyHashable : Any]! { get set } ``` |

Modified [EAGLRenderingAPI [enum]](https://developer.apple.com/documentation/opengles/eaglrenderingapi)

|  | Declaration |
| --- | --- |
| From | ``` enum EAGLRenderingAPI : UInt {     case OpenGLES1     case OpenGLES2     case OpenGLES3 } ``` |
| To | ``` enum EAGLRenderingAPI : UInt {     case openGLES1     case openGLES2     case openGLES3 } ``` |

Modified [EAGLRenderingAPI.openGLES1](https://developer.apple.com/documentation/opengles/eaglrenderingapi/opengles1)

|  | Declaration |
| --- | --- |
| From | ``` case OpenGLES1 ``` |
| To | ``` case openGLES1 ``` |

Modified [EAGLRenderingAPI.openGLES2](https://developer.apple.com/documentation/opengles/eaglrenderingapi/keaglrenderingapiopengles2)

|  | Declaration |
| --- | --- |
| From | ``` case OpenGLES2 ``` |
| To | ``` case openGLES2 ``` |

Modified [EAGLRenderingAPI.openGLES3](https://developer.apple.com/documentation/opengles/eaglrenderingapi/keaglrenderingapiopengles3)

|  | Declaration |
| --- | --- |
| From | ``` case OpenGLES3 ``` |
| To | ``` case openGLES3 ``` |

Modified [EAGLSharegroup](https://developer.apple.com/documentation/opengles/eaglsharegroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EAGLSharegroup : NSObject {     var debugLabel: String! } ``` | -- |
| To | ``` class EAGLSharegroup : NSObject {     var debugLabel: String!     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension EAGLSharegroup : CVarArg { } extension EAGLSharegroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [EAGLGetVersion(_: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!)](https://developer.apple.com/documentation/opengles/1624889-eaglgetversion)

|  | Declaration |
| --- | --- |
| From | ``` func EAGLGetVersion(_ major: UnsafeMutablePointer<UInt32>, _ minor: UnsafeMutablePointer<UInt32>) ``` |
| To | ``` func EAGLGetVersion(_ major: UnsafeMutablePointer<UInt32>!, _ minor: UnsafeMutablePointer<UInt32>!) ``` |

Modified [glBindAttribLocation(_: GLuint, _: GLuint, _: UnsafePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1617262-glbindattriblocation)

|  | Declaration |
| --- | --- |
| From | ``` func glBindAttribLocation(_ program: GLuint, _ index: GLuint, _ name: UnsafePointer<GLchar>) ``` |
| To | ``` func glBindAttribLocation(_ program: GLuint, _ index: GLuint, _ name: UnsafePointer<GLchar>!) ``` |

Modified [glBufferData(_: GLenum, _: GLsizeiptr, _: UnsafeRawPointer!, _: GLenum)](https://developer.apple.com/documentation/opengles/1617693-glbufferdata)

|  | Declaration |
| --- | --- |
| From | ``` func glBufferData(_ target: GLenum, _ size: GLsizeiptr, _ data: UnsafePointer<Void>, _ usage: GLenum) ``` |
| To | ``` func glBufferData(_ target: GLenum, _ size: GLsizeiptr, _ data: UnsafeRawPointer!, _ usage: GLenum) ``` |

Modified [glBufferSubData(_: GLenum, _: GLintptr, _: GLsizeiptr, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1617644-glbuffersubdata)

|  | Declaration |
| --- | --- |
| From | ``` func glBufferSubData(_ target: GLenum, _ offset: GLintptr, _ size: GLsizeiptr, _ data: UnsafePointer<Void>) ``` |
| To | ``` func glBufferSubData(_ target: GLenum, _ offset: GLintptr, _ size: GLsizeiptr, _ data: UnsafeRawPointer!) ``` |

Modified glClearBufferfv(_: GLenum, _: GLint, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glClearBufferfv(_ buffer: GLenum, _ drawbuffer: GLint, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glClearBufferfv(_ buffer: GLenum, _ drawbuffer: GLint, _ value: UnsafePointer<GLfloat>!) ``` |

Modified glClearBufferiv(_: GLenum, _: GLint, _: UnsafePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glClearBufferiv(_ buffer: GLenum, _ drawbuffer: GLint, _ value: UnsafePointer<GLint>) ``` |
| To | ``` func glClearBufferiv(_ buffer: GLenum, _ drawbuffer: GLint, _ value: UnsafePointer<GLint>!) ``` |

Modified glClearBufferuiv(_: GLenum, _: GLint, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glClearBufferuiv(_ buffer: GLenum, _ drawbuffer: GLint, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glClearBufferuiv(_ buffer: GLenum, _ drawbuffer: GLint, _ value: UnsafePointer<GLuint>!) ``` |

Modified glClientWaitSync(_: GLsync!, _: GLbitfield, _: GLuint64) -> GLenum

|  | Declaration |
| --- | --- |
| From | ``` func glClientWaitSync(_ sync: GLsync, _ flags: GLbitfield, _ timeout: GLuint64) -> GLenum ``` |
| To | ``` func glClientWaitSync(_ sync: GLsync!, _ flags: GLbitfield, _ timeout: GLuint64) -> GLenum ``` |

Modified [glClientWaitSyncAPPLE(_: GLsync!, _: GLbitfield, _: GLuint64) -> GLenum](https://developer.apple.com/documentation/opengles/1624707-glclientwaitsyncapple)

|  | Declaration |
| --- | --- |
| From | ``` func glClientWaitSyncAPPLE(_ sync: GLsync, _ flags: GLbitfield, _ timeout: GLuint64) -> GLenum ``` |
| To | ``` func glClientWaitSyncAPPLE(_ sync: GLsync!, _ flags: GLbitfield, _ timeout: GLuint64) -> GLenum ``` |

Modified [glClipPlanef(_: GLenum, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1622809-glclipplanef)

|  | Declaration |
| --- | --- |
| From | ``` func glClipPlanef(_ plane: GLenum, _ equation: UnsafePointer<GLfloat>) ``` |
| To | ``` func glClipPlanef(_ plane: GLenum, _ equation: UnsafePointer<GLfloat>!) ``` |

Modified [glClipPlanex(_: GLenum, _: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622728-glclipplanex)

|  | Declaration |
| --- | --- |
| From | ``` func glClipPlanex(_ plane: GLenum, _ equation: UnsafePointer<GLfixed>) ``` |
| To | ``` func glClipPlanex(_ plane: GLenum, _ equation: UnsafePointer<GLfixed>!) ``` |

Modified glColorPointer(_: GLint, _: GLenum, _: GLsizei, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glColorPointer(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafePointer<Void>) ``` |
| To | ``` func glColorPointer(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafeRawPointer!) ``` |

Modified [glCompressedTexImage2D(_: GLenum, _: GLint, _: GLenum, _: GLsizei, _: GLsizei, _: GLint, _: GLsizei, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1617532-glcompressedteximage2d)

|  | Declaration |
| --- | --- |
| From | ``` func glCompressedTexImage2D(_ target: GLenum, _ level: GLint, _ internalformat: GLenum, _ width: GLsizei, _ height: GLsizei, _ border: GLint, _ imageSize: GLsizei, _ data: UnsafePointer<Void>) ``` |
| To | ``` func glCompressedTexImage2D(_ target: GLenum, _ level: GLint, _ internalformat: GLenum, _ width: GLsizei, _ height: GLsizei, _ border: GLint, _ imageSize: GLsizei, _ data: UnsafeRawPointer!) ``` |

Modified glCompressedTexImage3D(_: GLenum, _: GLint, _: GLenum, _: GLsizei, _: GLsizei, _: GLsizei, _: GLint, _: GLsizei, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glCompressedTexImage3D(_ target: GLenum, _ level: GLint, _ internalformat: GLenum, _ width: GLsizei, _ height: GLsizei, _ depth: GLsizei, _ border: GLint, _ imageSize: GLsizei, _ data: UnsafePointer<Void>) ``` |
| To | ``` func glCompressedTexImage3D(_ target: GLenum, _ level: GLint, _ internalformat: GLenum, _ width: GLsizei, _ height: GLsizei, _ depth: GLsizei, _ border: GLint, _ imageSize: GLsizei, _ data: UnsafeRawPointer!) ``` |

Modified [glCompressedTexSubImage2D(_: GLenum, _: GLint, _: GLint, _: GLint, _: GLsizei, _: GLsizei, _: GLenum, _: GLsizei, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1617488-glcompressedtexsubimage2d)

|  | Declaration |
| --- | --- |
| From | ``` func glCompressedTexSubImage2D(_ target: GLenum, _ level: GLint, _ xoffset: GLint, _ yoffset: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ imageSize: GLsizei, _ data: UnsafePointer<Void>) ``` |
| To | ``` func glCompressedTexSubImage2D(_ target: GLenum, _ level: GLint, _ xoffset: GLint, _ yoffset: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ imageSize: GLsizei, _ data: UnsafeRawPointer!) ``` |

Modified glCompressedTexSubImage3D(_: GLenum, _: GLint, _: GLint, _: GLint, _: GLint, _: GLsizei, _: GLsizei, _: GLsizei, _: GLenum, _: GLsizei, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glCompressedTexSubImage3D(_ target: GLenum, _ level: GLint, _ xoffset: GLint, _ yoffset: GLint, _ zoffset: GLint, _ width: GLsizei, _ height: GLsizei, _ depth: GLsizei, _ format: GLenum, _ imageSize: GLsizei, _ data: UnsafePointer<Void>) ``` |
| To | ``` func glCompressedTexSubImage3D(_ target: GLenum, _ level: GLint, _ xoffset: GLint, _ yoffset: GLint, _ zoffset: GLint, _ width: GLsizei, _ height: GLsizei, _ depth: GLsizei, _ format: GLenum, _ imageSize: GLsizei, _ data: UnsafeRawPointer!) ``` |

Modified [glCreateShaderProgramvEXT(_: GLenum, _: GLsizei, _: UnsafePointer<UnsafePointer<GLchar>?>!) -> GLuint](https://developer.apple.com/documentation/opengles/1623803-glcreateshaderprogramvext)

|  | Declaration |
| --- | --- |
| From | ``` func glCreateShaderProgramvEXT(_ type: GLenum, _ count: GLsizei, _ strings: UnsafePointer<UnsafePointer<GLchar>>) -> GLuint ``` |
| To | ``` func glCreateShaderProgramvEXT(_ type: GLenum, _ count: GLsizei, _ strings: UnsafePointer<UnsafePointer<GLchar>?>!) -> GLuint ``` |

Modified [glDeleteBuffers(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617677-gldeletebuffers)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteBuffers(_ n: GLsizei, _ buffers: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteBuffers(_ n: GLsizei, _ buffers: UnsafePointer<GLuint>!) ``` |

Modified [glDeleteFramebuffers(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617575-gldeleteframebuffers)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteFramebuffers(_ n: GLsizei, _ framebuffers: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteFramebuffers(_ n: GLsizei, _ framebuffers: UnsafePointer<GLuint>!) ``` |

Modified [glDeleteFramebuffersOES(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1614354-gldeleteframebuffersoes)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteFramebuffersOES(_ n: GLsizei, _ framebuffers: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteFramebuffersOES(_ n: GLsizei, _ framebuffers: UnsafePointer<GLuint>!) ``` |

Modified [glDeleteProgramPipelinesEXT(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1623799-gldeleteprogrampipelinesext)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteProgramPipelinesEXT(_ n: GLsizei, _ pipelines: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteProgramPipelinesEXT(_ n: GLsizei, _ pipelines: UnsafePointer<GLuint>!) ``` |

Modified glDeleteQueries(_: GLsizei, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteQueries(_ n: GLsizei, _ ids: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteQueries(_ n: GLsizei, _ ids: UnsafePointer<GLuint>!) ``` |

Modified [glDeleteQueriesEXT(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1624734-gldeletequeriesext)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteQueriesEXT(_ n: GLsizei, _ ids: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteQueriesEXT(_ n: GLsizei, _ ids: UnsafePointer<GLuint>!) ``` |

Modified [glDeleteRenderbuffers(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617550-gldeleterenderbuffers)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteRenderbuffers(_ n: GLsizei, _ renderbuffers: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteRenderbuffers(_ n: GLsizei, _ renderbuffers: UnsafePointer<GLuint>!) ``` |

Modified [glDeleteRenderbuffersOES(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1614222-gldeleterenderbuffersoes)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteRenderbuffersOES(_ n: GLsizei, _ renderbuffers: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteRenderbuffersOES(_ n: GLsizei, _ renderbuffers: UnsafePointer<GLuint>!) ``` |

Modified glDeleteSamplers(_: GLsizei, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteSamplers(_ count: GLsizei, _ samplers: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteSamplers(_ count: GLsizei, _ samplers: UnsafePointer<GLuint>!) ``` |

Modified glDeleteSync(_: GLsync!)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteSync(_ sync: GLsync) ``` |
| To | ``` func glDeleteSync(_ sync: GLsync!) ``` |

Modified [glDeleteSyncAPPLE(_: GLsync!)](https://developer.apple.com/documentation/opengles/1624696-gldeletesyncapple)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteSyncAPPLE(_ sync: GLsync) ``` |
| To | ``` func glDeleteSyncAPPLE(_ sync: GLsync!) ``` |

Modified [glDeleteTextures(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617330-gldeletetextures)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteTextures(_ n: GLsizei, _ textures: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteTextures(_ n: GLsizei, _ textures: UnsafePointer<GLuint>!) ``` |

Modified glDeleteTransformFeedbacks(_: GLsizei, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteTransformFeedbacks(_ n: GLsizei, _ ids: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteTransformFeedbacks(_ n: GLsizei, _ ids: UnsafePointer<GLuint>!) ``` |

Modified glDeleteVertexArrays(_: GLsizei, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteVertexArrays(_ n: GLsizei, _ arrays: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteVertexArrays(_ n: GLsizei, _ arrays: UnsafePointer<GLuint>!) ``` |

Modified [glDeleteVertexArraysOES(_: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1614230-gldeletevertexarraysoes)

|  | Declaration |
| --- | --- |
| From | ``` func glDeleteVertexArraysOES(_ n: GLsizei, _ arrays: UnsafePointer<GLuint>) ``` |
| To | ``` func glDeleteVertexArraysOES(_ n: GLsizei, _ arrays: UnsafePointer<GLuint>!) ``` |

Modified [glDiscardFramebufferEXT(_: GLenum, _: GLsizei, _: UnsafePointer<GLenum>!)](https://developer.apple.com/documentation/opengles/1614266-gldiscardframebufferext)

|  | Declaration |
| --- | --- |
| From | ``` func glDiscardFramebufferEXT(_ target: GLenum, _ numAttachments: GLsizei, _ attachments: UnsafePointer<GLenum>) ``` |
| To | ``` func glDiscardFramebufferEXT(_ target: GLenum, _ numAttachments: GLsizei, _ attachments: UnsafePointer<GLenum>!) ``` |

Modified glDrawBuffers(_: GLsizei, _: UnsafePointer<GLenum>!)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawBuffers(_ n: GLsizei, _ bufs: UnsafePointer<GLenum>) ``` |
| To | ``` func glDrawBuffers(_ n: GLsizei, _ bufs: UnsafePointer<GLenum>!) ``` |

Modified [glDrawElements(_: GLenum, _: GLsizei, _: GLenum, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1617598-gldrawelements)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawElements(_ mode: GLenum, _ count: GLsizei, _ type: GLenum, _ indices: UnsafePointer<Void>) ``` |
| To | ``` func glDrawElements(_ mode: GLenum, _ count: GLsizei, _ type: GLenum, _ indices: UnsafeRawPointer!) ``` |

Modified glDrawElementsInstanced(_: GLenum, _: GLsizei, _: GLenum, _: UnsafeRawPointer!, _: GLsizei)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawElementsInstanced(_ mode: GLenum, _ count: GLsizei, _ type: GLenum, _ indices: UnsafePointer<Void>, _ instancecount: GLsizei) ``` |
| To | ``` func glDrawElementsInstanced(_ mode: GLenum, _ count: GLsizei, _ type: GLenum, _ indices: UnsafeRawPointer!, _ instancecount: GLsizei) ``` |

Modified [glDrawElementsInstancedEXT(_: GLenum, _: GLsizei, _: GLenum, _: UnsafeRawPointer!, _: GLsizei)](https://developer.apple.com/documentation/opengles/1624690-gldrawelementsinstancedext)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawElementsInstancedEXT(_ mode: GLenum, _ count: GLsizei, _ type: GLenum, _ indices: UnsafePointer<Void>, _ instanceCount: GLsizei) ``` |
| To | ``` func glDrawElementsInstancedEXT(_ mode: GLenum, _ count: GLsizei, _ type: GLenum, _ indices: UnsafeRawPointer!, _ instanceCount: GLsizei) ``` |

Modified glDrawRangeElements(_: GLenum, _: GLuint, _: GLuint, _: GLsizei, _: GLenum, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawRangeElements(_ mode: GLenum, _ start: GLuint, _ end: GLuint, _ count: GLsizei, _ type: GLenum, _ indices: UnsafePointer<Void>) ``` |
| To | ``` func glDrawRangeElements(_ mode: GLenum, _ start: GLuint, _ end: GLuint, _ count: GLsizei, _ type: GLenum, _ indices: UnsafeRawPointer!) ``` |

Modified [glDrawTexfvOES(_: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1622768-gldrawtexfvoes)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawTexfvOES(_ coords: UnsafePointer<GLfloat>) ``` |
| To | ``` func glDrawTexfvOES(_ coords: UnsafePointer<GLfloat>!) ``` |

Modified [glDrawTexivOES(_: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1622754-gldrawtexivoes)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawTexivOES(_ coords: UnsafePointer<GLint>) ``` |
| To | ``` func glDrawTexivOES(_ coords: UnsafePointer<GLint>!) ``` |

Modified [glDrawTexsvOES(_: UnsafePointer<GLshort>!)](https://developer.apple.com/documentation/opengles/1622793-gldrawtexsvoes)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawTexsvOES(_ coords: UnsafePointer<GLshort>) ``` |
| To | ``` func glDrawTexsvOES(_ coords: UnsafePointer<GLshort>!) ``` |

Modified [glDrawTexxvOES(_: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622759-gldrawtexxvoes)

|  | Declaration |
| --- | --- |
| From | ``` func glDrawTexxvOES(_ coords: UnsafePointer<GLfixed>) ``` |
| To | ``` func glDrawTexxvOES(_ coords: UnsafePointer<GLfixed>!) ``` |

Modified glFenceSync(_: GLenum, _: GLbitfield) -> GLsync!

|  | Declaration |
| --- | --- |
| From | ``` func glFenceSync(_ condition: GLenum, _ flags: GLbitfield) -> GLsync ``` |
| To | ``` func glFenceSync(_ condition: GLenum, _ flags: GLbitfield) -> GLsync! ``` |

Modified [glFenceSyncAPPLE(_: GLenum, _: GLbitfield) -> GLsync!](https://developer.apple.com/documentation/opengles/1624705-glfencesyncapple)

|  | Declaration |
| --- | --- |
| From | ``` func glFenceSyncAPPLE(_ condition: GLenum, _ flags: GLbitfield) -> GLsync ``` |
| To | ``` func glFenceSyncAPPLE(_ condition: GLenum, _ flags: GLbitfield) -> GLsync! ``` |

Modified glFogfv(_: GLenum, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glFogfv(_ pname: GLenum, _ params: UnsafePointer<GLfloat>) ``` |
| To | ``` func glFogfv(_ pname: GLenum, _ params: UnsafePointer<GLfloat>!) ``` |

Modified [glFogxv(_: GLenum, _: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622695-glfogxv)

|  | Declaration |
| --- | --- |
| From | ``` func glFogxv(_ pname: GLenum, _ params: UnsafePointer<GLfixed>) ``` |
| To | ``` func glFogxv(_ pname: GLenum, _ params: UnsafePointer<GLfixed>!) ``` |

Modified [glGenBuffers(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617417-glgenbuffers)

|  | Declaration |
| --- | --- |
| From | ``` func glGenBuffers(_ n: GLsizei, _ buffers: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenBuffers(_ n: GLsizei, _ buffers: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGenFramebuffers(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617341-glgenframebuffers)

|  | Declaration |
| --- | --- |
| From | ``` func glGenFramebuffers(_ n: GLsizei, _ framebuffers: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenFramebuffers(_ n: GLsizei, _ framebuffers: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGenFramebuffersOES(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1614285-glgenframebuffersoes)

|  | Declaration |
| --- | --- |
| From | ``` func glGenFramebuffersOES(_ n: GLsizei, _ framebuffers: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenFramebuffersOES(_ n: GLsizei, _ framebuffers: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGenProgramPipelinesEXT(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1623828-glgenprogrampipelinesext)

|  | Declaration |
| --- | --- |
| From | ``` func glGenProgramPipelinesEXT(_ n: GLsizei, _ pipelines: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenProgramPipelinesEXT(_ n: GLsizei, _ pipelines: UnsafeMutablePointer<GLuint>!) ``` |

Modified glGenQueries(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGenQueries(_ n: GLsizei, _ ids: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenQueries(_ n: GLsizei, _ ids: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGenQueriesEXT(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1624720-glgenqueriesext)

|  | Declaration |
| --- | --- |
| From | ``` func glGenQueriesEXT(_ n: GLsizei, _ ids: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenQueriesEXT(_ n: GLsizei, _ ids: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGenRenderbuffers(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617681-glgenrenderbuffers)

|  | Declaration |
| --- | --- |
| From | ``` func glGenRenderbuffers(_ n: GLsizei, _ renderbuffers: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenRenderbuffers(_ n: GLsizei, _ renderbuffers: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGenRenderbuffersOES(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1614335-glgenrenderbuffersoes)

|  | Declaration |
| --- | --- |
| From | ``` func glGenRenderbuffersOES(_ n: GLsizei, _ renderbuffers: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenRenderbuffersOES(_ n: GLsizei, _ renderbuffers: UnsafeMutablePointer<GLuint>!) ``` |

Modified glGenSamplers(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGenSamplers(_ count: GLsizei, _ samplers: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenSamplers(_ count: GLsizei, _ samplers: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGenTextures(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617621-glgentextures)

|  | Declaration |
| --- | --- |
| From | ``` func glGenTextures(_ n: GLsizei, _ textures: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenTextures(_ n: GLsizei, _ textures: UnsafeMutablePointer<GLuint>!) ``` |

Modified glGenTransformFeedbacks(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGenTransformFeedbacks(_ n: GLsizei, _ ids: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenTransformFeedbacks(_ n: GLsizei, _ ids: UnsafeMutablePointer<GLuint>!) ``` |

Modified glGenVertexArrays(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGenVertexArrays(_ n: GLsizei, _ arrays: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenVertexArrays(_ n: GLsizei, _ arrays: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGenVertexArraysOES(_: GLsizei, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1614235-glgenvertexarraysoes)

|  | Declaration |
| --- | --- |
| From | ``` func glGenVertexArraysOES(_ n: GLsizei, _ arrays: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGenVertexArraysOES(_ n: GLsizei, _ arrays: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGetActiveAttrib(_: GLuint, _: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLint>!, _: UnsafeMutablePointer<GLenum>!, _: UnsafeMutablePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1617596-glgetactiveattrib)

|  | Declaration |
| --- | --- |
| From | ``` func glGetActiveAttrib(_ program: GLuint, _ index: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ size: UnsafeMutablePointer<GLint>, _ type: UnsafeMutablePointer<GLenum>, _ name: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetActiveAttrib(_ program: GLuint, _ index: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ size: UnsafeMutablePointer<GLint>!, _ type: UnsafeMutablePointer<GLenum>!, _ name: UnsafeMutablePointer<GLchar>!) ``` |

Modified [glGetActiveUniform(_: GLuint, _: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLint>!, _: UnsafeMutablePointer<GLenum>!, _: UnsafeMutablePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1617325-glgetactiveuniform)

|  | Declaration |
| --- | --- |
| From | ``` func glGetActiveUniform(_ program: GLuint, _ index: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ size: UnsafeMutablePointer<GLint>, _ type: UnsafeMutablePointer<GLenum>, _ name: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetActiveUniform(_ program: GLuint, _ index: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ size: UnsafeMutablePointer<GLint>!, _ type: UnsafeMutablePointer<GLenum>!, _ name: UnsafeMutablePointer<GLchar>!) ``` |

Modified glGetActiveUniformBlockiv(_: GLuint, _: GLuint, _: GLenum, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetActiveUniformBlockiv(_ program: GLuint, _ uniformBlockIndex: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetActiveUniformBlockiv(_ program: GLuint, _ uniformBlockIndex: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetActiveUniformBlockName(_: GLuint, _: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLchar>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetActiveUniformBlockName(_ program: GLuint, _ uniformBlockIndex: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ uniformBlockName: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetActiveUniformBlockName(_ program: GLuint, _ uniformBlockIndex: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ uniformBlockName: UnsafeMutablePointer<GLchar>!) ``` |

Modified glGetActiveUniformsiv(_: GLuint, _: GLsizei, _: UnsafePointer<GLuint>!, _: GLenum, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetActiveUniformsiv(_ program: GLuint, _ uniformCount: GLsizei, _ uniformIndices: UnsafePointer<GLuint>, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetActiveUniformsiv(_ program: GLuint, _ uniformCount: GLsizei, _ uniformIndices: UnsafePointer<GLuint>!, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetAttachedShaders(_: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1617610-glgetattachedshaders)

|  | Declaration |
| --- | --- |
| From | ``` func glGetAttachedShaders(_ program: GLuint, _ maxcount: GLsizei, _ count: UnsafeMutablePointer<GLsizei>, _ shaders: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGetAttachedShaders(_ program: GLuint, _ maxcount: GLsizei, _ count: UnsafeMutablePointer<GLsizei>!, _ shaders: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGetAttribLocation(_: GLuint, _: UnsafePointer<GLchar>!) -> Int32](https://developer.apple.com/documentation/opengles/1617398-glgetattriblocation)

|  | Declaration |
| --- | --- |
| From | ``` func glGetAttribLocation(_ program: GLuint, _ name: UnsafePointer<GLchar>) -> Int32 ``` |
| To | ``` func glGetAttribLocation(_ program: GLuint, _ name: UnsafePointer<GLchar>!) -> Int32 ``` |

Modified [glGetBooleanv(_: GLenum, _: UnsafeMutablePointer<GLboolean>!)](https://developer.apple.com/documentation/opengles/1617391-glgetbooleanv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetBooleanv(_ pname: GLenum, _ params: UnsafeMutablePointer<GLboolean>) ``` |
| To | ``` func glGetBooleanv(_ pname: GLenum, _ params: UnsafeMutablePointer<GLboolean>!) ``` |

Modified glGetBufferParameteri64v(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint64>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetBufferParameteri64v(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint64>) ``` |
| To | ``` func glGetBufferParameteri64v(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint64>!) ``` |

Modified [glGetBufferParameteriv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617520-glgetbufferparameteriv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetBufferParameteriv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetBufferParameteriv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetBufferPointerv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetBufferPointerv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |
| To | ``` func glGetBufferPointerv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) ``` |

Modified [glGetBufferPointervOES(_: GLenum, _: GLenum, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](https://developer.apple.com/documentation/opengles/1614309-glgetbufferpointervoes)

|  | Declaration |
| --- | --- |
| From | ``` func glGetBufferPointervOES(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |
| To | ``` func glGetBufferPointervOES(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) ``` |

Modified [glGetClipPlanef(_: GLenum, _: UnsafeMutablePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1622716-glgetclipplanef)

|  | Declaration |
| --- | --- |
| From | ``` func glGetClipPlanef(_ pname: GLenum, _ equation: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetClipPlanef(_ pname: GLenum, _ equation: UnsafeMutablePointer<GLfloat>!) ``` |

Modified [glGetClipPlanex(_: GLenum, _: UnsafeMutablePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622772-glgetclipplanex)

|  | Declaration |
| --- | --- |
| From | ``` func glGetClipPlanex(_ pname: GLenum, _ eqn: UnsafeMutablePointer<GLfixed>) ``` |
| To | ``` func glGetClipPlanex(_ pname: GLenum, _ eqn: UnsafeMutablePointer<GLfixed>!) ``` |

Modified [glGetFixedv(_: GLenum, _: UnsafeMutablePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622805-glgetfixedv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetFixedv(_ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>) ``` |
| To | ``` func glGetFixedv(_ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>!) ``` |

Modified [glGetFloatv(_: GLenum, _: UnsafeMutablePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617275-glgetfloatv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetFloatv(_ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetFloatv(_ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>!) ``` |

Modified glGetFragDataLocation(_: GLuint, _: UnsafePointer<GLchar>!) -> GLint

|  | Declaration |
| --- | --- |
| From | ``` func glGetFragDataLocation(_ program: GLuint, _ name: UnsafePointer<GLchar>) -> GLint ``` |
| To | ``` func glGetFragDataLocation(_ program: GLuint, _ name: UnsafePointer<GLchar>!) -> GLint ``` |

Modified [glGetFramebufferAttachmentParameteriv(_: GLenum, _: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617682-glgetframebufferattachmentparame)

|  | Declaration |
| --- | --- |
| From | ``` func glGetFramebufferAttachmentParameteriv(_ target: GLenum, _ attachment: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetFramebufferAttachmentParameteriv(_ target: GLenum, _ attachment: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetFramebufferAttachmentParameterivOES(_: GLenum, _: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1614343-glgetframebufferattachmentparame)

|  | Declaration |
| --- | --- |
| From | ``` func glGetFramebufferAttachmentParameterivOES(_ target: GLenum, _ attachment: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetFramebufferAttachmentParameterivOES(_ target: GLenum, _ attachment: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetInteger64i_v(_: GLenum, _: GLuint, _: UnsafeMutablePointer<GLint64>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetInteger64i_v(_ target: GLenum, _ index: GLuint, _ data: UnsafeMutablePointer<GLint64>) ``` |
| To | ``` func glGetInteger64i_v(_ target: GLenum, _ index: GLuint, _ data: UnsafeMutablePointer<GLint64>!) ``` |

Modified glGetInteger64v(_: GLenum, _: UnsafeMutablePointer<GLint64>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetInteger64v(_ pname: GLenum, _ params: UnsafeMutablePointer<GLint64>) ``` |
| To | ``` func glGetInteger64v(_ pname: GLenum, _ params: UnsafeMutablePointer<GLint64>!) ``` |

Modified [glGetInteger64vAPPLE(_: GLenum, _: UnsafeMutablePointer<GLint64>!)](https://developer.apple.com/documentation/opengles/1624695-glgetinteger64vapple)

|  | Declaration |
| --- | --- |
| From | ``` func glGetInteger64vAPPLE(_ pname: GLenum, _ params: UnsafeMutablePointer<GLint64>) ``` |
| To | ``` func glGetInteger64vAPPLE(_ pname: GLenum, _ params: UnsafeMutablePointer<GLint64>!) ``` |

Modified glGetIntegeri_v(_: GLenum, _: GLuint, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetIntegeri_v(_ target: GLenum, _ index: GLuint, _ data: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetIntegeri_v(_ target: GLenum, _ index: GLuint, _ data: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetIntegerv(_: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617284-glgetintegerv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetIntegerv(_ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetIntegerv(_ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetInternalformativ(_: GLenum, _: GLenum, _: GLenum, _: GLsizei, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetInternalformativ(_ target: GLenum, _ internalformat: GLenum, _ pname: GLenum, _ bufSize: GLsizei, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetInternalformativ(_ target: GLenum, _ internalformat: GLenum, _ pname: GLenum, _ bufSize: GLsizei, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetLightfv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetLightfv(_ light: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetLightfv(_ light: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>!) ``` |

Modified [glGetLightxv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622747-glgetlightxv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetLightxv(_ light: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>) ``` |
| To | ``` func glGetLightxv(_ light: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>!) ``` |

Modified glGetMaterialfv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetMaterialfv(_ face: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetMaterialfv(_ face: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>!) ``` |

Modified [glGetMaterialxv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622765-glgetmaterialxv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetMaterialxv(_ face: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>) ``` |
| To | ``` func glGetMaterialxv(_ face: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>!) ``` |

Modified [glGetObjectLabelEXT(_: GLenum, _: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1614334-glgetobjectlabelext)

|  | Declaration |
| --- | --- |
| From | ``` func glGetObjectLabelEXT(_ type: GLenum, _ object: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ label: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetObjectLabelEXT(_ type: GLenum, _ object: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ label: UnsafeMutablePointer<GLchar>!) ``` |

Modified glGetPointerv(_: GLenum, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetPointerv(_ pname: GLenum, _ params: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |
| To | ``` func glGetPointerv(_ pname: GLenum, _ params: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) ``` |

Modified glGetProgramBinary(_: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLenum>!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetProgramBinary(_ program: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ binaryFormat: UnsafeMutablePointer<GLenum>, _ binary: UnsafeMutablePointer<Void>) ``` |
| To | ``` func glGetProgramBinary(_ program: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ binaryFormat: UnsafeMutablePointer<GLenum>!, _ binary: UnsafeMutableRawPointer!) ``` |

Modified [glGetProgramInfoLog(_: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1617233-glgetprograminfolog)

|  | Declaration |
| --- | --- |
| From | ``` func glGetProgramInfoLog(_ program: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ infolog: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetProgramInfoLog(_ program: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ infolog: UnsafeMutablePointer<GLchar>!) ``` |

Modified [glGetProgramiv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617643-glgetprogramiv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetProgramiv(_ program: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetProgramiv(_ program: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetProgramPipelineInfoLogEXT(_: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1623790-glgetprogrampipelineinfologext)

|  | Declaration |
| --- | --- |
| From | ``` func glGetProgramPipelineInfoLogEXT(_ pipeline: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ infoLog: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetProgramPipelineInfoLogEXT(_ pipeline: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ infoLog: UnsafeMutablePointer<GLchar>!) ``` |

Modified [glGetProgramPipelineivEXT(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1623867-glgetprogrampipelineivext)

|  | Declaration |
| --- | --- |
| From | ``` func glGetProgramPipelineivEXT(_ pipeline: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetProgramPipelineivEXT(_ pipeline: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetQueryiv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetQueryiv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetQueryiv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetQueryivEXT(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1624752-glgetqueryivext)

|  | Declaration |
| --- | --- |
| From | ``` func glGetQueryivEXT(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetQueryivEXT(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetQueryObjectuiv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetQueryObjectuiv(_ id: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGetQueryObjectuiv(_ id: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGetQueryObjectuivEXT(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1624686-glgetqueryobjectuivext)

|  | Declaration |
| --- | --- |
| From | ``` func glGetQueryObjectuivEXT(_ id: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGetQueryObjectuivEXT(_ id: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGetRenderbufferParameteriv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617615-glgetrenderbufferparameteriv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetRenderbufferParameteriv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetRenderbufferParameteriv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetRenderbufferParameterivOES(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1614237-glgetrenderbufferparameterivoes)

|  | Declaration |
| --- | --- |
| From | ``` func glGetRenderbufferParameterivOES(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetRenderbufferParameterivOES(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetSamplerParameterfv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetSamplerParameterfv(_ sampler: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetSamplerParameterfv(_ sampler: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>!) ``` |

Modified glGetSamplerParameteriv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetSamplerParameteriv(_ sampler: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetSamplerParameteriv(_ sampler: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetShaderInfoLog(_: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1617419-glgetshaderinfolog)

|  | Declaration |
| --- | --- |
| From | ``` func glGetShaderInfoLog(_ shader: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ infolog: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetShaderInfoLog(_ shader: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ infolog: UnsafeMutablePointer<GLchar>!) ``` |

Modified [glGetShaderiv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617370-glgetshaderiv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetShaderiv(_ shader: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetShaderiv(_ shader: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetShaderPrecisionFormat(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617276-glgetshaderprecisionformat)

|  | Declaration |
| --- | --- |
| From | ``` func glGetShaderPrecisionFormat(_ shadertype: GLenum, _ precisiontype: GLenum, _ range: UnsafeMutablePointer<GLint>, _ precision: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetShaderPrecisionFormat(_ shadertype: GLenum, _ precisiontype: GLenum, _ range: UnsafeMutablePointer<GLint>!, _ precision: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetShaderSource(_: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1617452-glgetshadersource)

|  | Declaration |
| --- | --- |
| From | ``` func glGetShaderSource(_ shader: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ source: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetShaderSource(_ shader: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ source: UnsafeMutablePointer<GLchar>!) ``` |

Modified [glGetString(_: GLenum) -> UnsafePointer<GLubyte>!](https://developer.apple.com/documentation/opengles/1617676-glgetstring)

|  | Declaration |
| --- | --- |
| From | ``` func glGetString(_ name: GLenum) -> UnsafePointer<GLubyte> ``` |
| To | ``` func glGetString(_ name: GLenum) -> UnsafePointer<GLubyte>! ``` |

Modified glGetStringi(_: GLenum, _: GLuint) -> UnsafePointer<GLubyte>!

|  | Declaration |
| --- | --- |
| From | ``` func glGetStringi(_ name: GLenum, _ index: GLuint) -> UnsafePointer<GLubyte> ``` |
| To | ``` func glGetStringi(_ name: GLenum, _ index: GLuint) -> UnsafePointer<GLubyte>! ``` |

Modified glGetSynciv(_: GLsync!, _: GLenum, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetSynciv(_ sync: GLsync, _ pname: GLenum, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ values: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetSynciv(_ sync: GLsync!, _ pname: GLenum, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ values: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetSyncivAPPLE(_: GLsync!, _: GLenum, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1624746-glgetsyncivapple)

|  | Declaration |
| --- | --- |
| From | ``` func glGetSyncivAPPLE(_ sync: GLsync, _ pname: GLenum, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ values: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetSyncivAPPLE(_ sync: GLsync!, _ pname: GLenum, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ values: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetTexEnvfv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetTexEnvfv(_ env: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetTexEnvfv(_ env: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>!) ``` |

Modified glGetTexEnviv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetTexEnviv(_ env: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetTexEnviv(_ env: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetTexEnvxv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622691-glgettexenvxv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetTexEnvxv(_ env: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>) ``` |
| To | ``` func glGetTexEnvxv(_ env: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>!) ``` |

Modified [glGetTexParameterfv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617309-glgettexparameterfv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetTexParameterfv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetTexParameterfv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>!) ``` |

Modified [glGetTexParameteriv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617366-glgettexparameteriv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetTexParameteriv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetTexParameteriv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetTexParameterxv(_: GLenum, _: GLenum, _: UnsafeMutablePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622758-glgettexparameterxv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetTexParameterxv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>) ``` |
| To | ``` func glGetTexParameterxv(_ target: GLenum, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfixed>!) ``` |

Modified glGetTransformFeedbackVarying(_: GLuint, _: GLuint, _: GLsizei, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLsizei>!, _: UnsafeMutablePointer<GLenum>!, _: UnsafeMutablePointer<GLchar>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetTransformFeedbackVarying(_ program: GLuint, _ index: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>, _ size: UnsafeMutablePointer<GLsizei>, _ type: UnsafeMutablePointer<GLenum>, _ name: UnsafeMutablePointer<GLchar>) ``` |
| To | ``` func glGetTransformFeedbackVarying(_ program: GLuint, _ index: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ size: UnsafeMutablePointer<GLsizei>!, _ type: UnsafeMutablePointer<GLenum>!, _ name: UnsafeMutablePointer<GLchar>!) ``` |

Modified glGetUniformBlockIndex(_: GLuint, _: UnsafePointer<GLchar>!) -> GLuint

|  | Declaration |
| --- | --- |
| From | ``` func glGetUniformBlockIndex(_ program: GLuint, _ uniformBlockName: UnsafePointer<GLchar>) -> GLuint ``` |
| To | ``` func glGetUniformBlockIndex(_ program: GLuint, _ uniformBlockName: UnsafePointer<GLchar>!) -> GLuint ``` |

Modified [glGetUniformfv(_: GLuint, _: GLint, _: UnsafeMutablePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617597-glgetuniformfv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetUniformfv(_ program: GLuint, _ location: GLint, _ params: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetUniformfv(_ program: GLuint, _ location: GLint, _ params: UnsafeMutablePointer<GLfloat>!) ``` |

Modified glGetUniformIndices(_: GLuint, _: GLsizei, _: UnsafePointer<UnsafePointer<GLchar>?>!, _: UnsafeMutablePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetUniformIndices(_ program: GLuint, _ uniformCount: GLsizei, _ uniformNames: UnsafePointer<UnsafePointer<GLchar>>, _ uniformIndices: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGetUniformIndices(_ program: GLuint, _ uniformCount: GLsizei, _ uniformNames: UnsafePointer<UnsafePointer<GLchar>?>!, _ uniformIndices: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGetUniformiv(_: GLuint, _: GLint, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617629-glgetuniformiv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetUniformiv(_ program: GLuint, _ location: GLint, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetUniformiv(_ program: GLuint, _ location: GLint, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetUniformLocation(_: GLuint, _: UnsafePointer<GLchar>!) -> Int32](https://developer.apple.com/documentation/opengles/1617403-glgetuniformlocation)

|  | Declaration |
| --- | --- |
| From | ``` func glGetUniformLocation(_ program: GLuint, _ name: UnsafePointer<GLchar>) -> Int32 ``` |
| To | ``` func glGetUniformLocation(_ program: GLuint, _ name: UnsafePointer<GLchar>!) -> Int32 ``` |

Modified glGetUniformuiv(_: GLuint, _: GLint, _: UnsafeMutablePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetUniformuiv(_ program: GLuint, _ location: GLint, _ params: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGetUniformuiv(_ program: GLuint, _ location: GLint, _ params: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGetVertexAttribfv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617512-glgetvertexattribfv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetVertexAttribfv(_ index: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func glGetVertexAttribfv(_ index: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLfloat>!) ``` |

Modified glGetVertexAttribIiv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetVertexAttribIiv(_ index: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetVertexAttribIiv(_ index: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified glGetVertexAttribIuiv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glGetVertexAttribIuiv(_ index: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLuint>) ``` |
| To | ``` func glGetVertexAttribIuiv(_ index: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLuint>!) ``` |

Modified [glGetVertexAttribiv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617255-glgetvertexattribiv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetVertexAttribiv(_ index: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func glGetVertexAttribiv(_ index: GLuint, _ pname: GLenum, _ params: UnsafeMutablePointer<GLint>!) ``` |

Modified [glGetVertexAttribPointerv(_: GLuint, _: GLenum, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](https://developer.apple.com/documentation/opengles/1617511-glgetvertexattribpointerv)

|  | Declaration |
| --- | --- |
| From | ``` func glGetVertexAttribPointerv(_ index: GLuint, _ pname: GLenum, _ pointer: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |
| To | ``` func glGetVertexAttribPointerv(_ index: GLuint, _ pname: GLenum, _ pointer: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) ``` |

Modified [glInsertEventMarkerEXT(_: GLsizei, _: UnsafePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1614284-glinserteventmarkerext)

|  | Declaration |
| --- | --- |
| From | ``` func glInsertEventMarkerEXT(_ length: GLsizei, _ marker: UnsafePointer<GLchar>) ``` |
| To | ``` func glInsertEventMarkerEXT(_ length: GLsizei, _ marker: UnsafePointer<GLchar>!) ``` |

Modified [glInvalidateFramebuffer(_: GLenum, _: GLsizei, _: UnsafePointer<GLenum>!)](https://developer.apple.com/documentation/opengles/1617652-glinvalidateframebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func glInvalidateFramebuffer(_ target: GLenum, _ numAttachments: GLsizei, _ attachments: UnsafePointer<GLenum>) ``` |
| To | ``` func glInvalidateFramebuffer(_ target: GLenum, _ numAttachments: GLsizei, _ attachments: UnsafePointer<GLenum>!) ``` |

Modified [glInvalidateSubFramebuffer(_: GLenum, _: GLsizei, _: UnsafePointer<GLenum>!, _: GLint, _: GLint, _: GLsizei, _: GLsizei)](https://developer.apple.com/documentation/opengles/1617516-glinvalidatesubframebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func glInvalidateSubFramebuffer(_ target: GLenum, _ numAttachments: GLsizei, _ attachments: UnsafePointer<GLenum>, _ x: GLint, _ y: GLint, _ width: GLsizei, _ height: GLsizei) ``` |
| To | ``` func glInvalidateSubFramebuffer(_ target: GLenum, _ numAttachments: GLsizei, _ attachments: UnsafePointer<GLenum>!, _ x: GLint, _ y: GLint, _ width: GLsizei, _ height: GLsizei) ``` |

Modified glIsSync(_: GLsync!) -> GLboolean

|  | Declaration |
| --- | --- |
| From | ``` func glIsSync(_ sync: GLsync) -> GLboolean ``` |
| To | ``` func glIsSync(_ sync: GLsync!) -> GLboolean ``` |

Modified [glIsSyncAPPLE(_: GLsync!) -> GLboolean](https://developer.apple.com/documentation/opengles/1624727-glissyncapple)

|  | Declaration |
| --- | --- |
| From | ``` func glIsSyncAPPLE(_ sync: GLsync) -> GLboolean ``` |
| To | ``` func glIsSyncAPPLE(_ sync: GLsync!) -> GLboolean ``` |

Modified [glLabelObjectEXT(_: GLenum, _: GLuint, _: GLsizei, _: UnsafePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1614324-gllabelobjectext)

|  | Declaration |
| --- | --- |
| From | ``` func glLabelObjectEXT(_ type: GLenum, _ object: GLuint, _ length: GLsizei, _ label: UnsafePointer<GLchar>) ``` |
| To | ``` func glLabelObjectEXT(_ type: GLenum, _ object: GLuint, _ length: GLsizei, _ label: UnsafePointer<GLchar>!) ``` |

Modified glLightfv(_: GLenum, _: GLenum, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glLightfv(_ light: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfloat>) ``` |
| To | ``` func glLightfv(_ light: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfloat>!) ``` |

Modified glLightModelfv(_: GLenum, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glLightModelfv(_ pname: GLenum, _ params: UnsafePointer<GLfloat>) ``` |
| To | ``` func glLightModelfv(_ pname: GLenum, _ params: UnsafePointer<GLfloat>!) ``` |

Modified [glLightModelxv(_: GLenum, _: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622806-gllightmodelxv)

|  | Declaration |
| --- | --- |
| From | ``` func glLightModelxv(_ pname: GLenum, _ params: UnsafePointer<GLfixed>) ``` |
| To | ``` func glLightModelxv(_ pname: GLenum, _ params: UnsafePointer<GLfixed>!) ``` |

Modified [glLightxv(_: GLenum, _: GLenum, _: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622696-gllightxv)

|  | Declaration |
| --- | --- |
| From | ``` func glLightxv(_ light: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfixed>) ``` |
| To | ``` func glLightxv(_ light: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfixed>!) ``` |

Modified glLoadMatrixf(_: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glLoadMatrixf(_ m: UnsafePointer<GLfloat>) ``` |
| To | ``` func glLoadMatrixf(_ m: UnsafePointer<GLfloat>!) ``` |

Modified [glLoadMatrixx(_: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622791-glloadmatrixx)

|  | Declaration |
| --- | --- |
| From | ``` func glLoadMatrixx(_ m: UnsafePointer<GLfixed>) ``` |
| To | ``` func glLoadMatrixx(_ m: UnsafePointer<GLfixed>!) ``` |

Modified [glMapBufferOES(_: GLenum, _: GLenum) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/opengles/1614241-glmapbufferoes)

|  | Declaration |
| --- | --- |
| From | ``` func glMapBufferOES(_ target: GLenum, _ access: GLenum) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func glMapBufferOES(_ target: GLenum, _ access: GLenum) -> UnsafeMutableRawPointer! ``` |

Modified glMapBufferRange(_: GLenum, _: GLintptr, _: GLsizeiptr, _: GLbitfield) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func glMapBufferRange(_ target: GLenum, _ offset: GLintptr, _ length: GLsizeiptr, _ access: GLbitfield) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func glMapBufferRange(_ target: GLenum, _ offset: GLintptr, _ length: GLsizeiptr, _ access: GLbitfield) -> UnsafeMutableRawPointer! ``` |

Modified [glMapBufferRangeEXT(_: GLenum, _: GLintptr, _: GLsizeiptr, _: GLbitfield) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/opengles/1614197-glmapbufferrangeext)

|  | Declaration |
| --- | --- |
| From | ``` func glMapBufferRangeEXT(_ target: GLenum, _ offset: GLintptr, _ length: GLsizeiptr, _ access: GLbitfield) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func glMapBufferRangeEXT(_ target: GLenum, _ offset: GLintptr, _ length: GLsizeiptr, _ access: GLbitfield) -> UnsafeMutableRawPointer! ``` |

Modified glMaterialfv(_: GLenum, _: GLenum, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glMaterialfv(_ face: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfloat>) ``` |
| To | ``` func glMaterialfv(_ face: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfloat>!) ``` |

Modified [glMaterialxv(_: GLenum, _: GLenum, _: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622783-glmaterialxv)

|  | Declaration |
| --- | --- |
| From | ``` func glMaterialxv(_ face: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfixed>) ``` |
| To | ``` func glMaterialxv(_ face: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfixed>!) ``` |

Modified [glMatrixIndexPointerOES(_: GLint, _: GLenum, _: GLsizei, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1622721-glmatrixindexpointeroes)

|  | Declaration |
| --- | --- |
| From | ``` func glMatrixIndexPointerOES(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafePointer<Void>) ``` |
| To | ``` func glMatrixIndexPointerOES(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafeRawPointer!) ``` |

Modified glMultMatrixf(_: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glMultMatrixf(_ m: UnsafePointer<GLfloat>) ``` |
| To | ``` func glMultMatrixf(_ m: UnsafePointer<GLfloat>!) ``` |

Modified [glMultMatrixx(_: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622692-glmultmatrixx)

|  | Declaration |
| --- | --- |
| From | ``` func glMultMatrixx(_ m: UnsafePointer<GLfixed>) ``` |
| To | ``` func glMultMatrixx(_ m: UnsafePointer<GLfixed>!) ``` |

Modified glNormalPointer(_: GLenum, _: GLsizei, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glNormalPointer(_ type: GLenum, _ stride: GLsizei, _ pointer: UnsafePointer<Void>) ``` |
| To | ``` func glNormalPointer(_ type: GLenum, _ stride: GLsizei, _ pointer: UnsafeRawPointer!) ``` |

Modified glPointParameterfv(_: GLenum, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glPointParameterfv(_ pname: GLenum, _ params: UnsafePointer<GLfloat>) ``` |
| To | ``` func glPointParameterfv(_ pname: GLenum, _ params: UnsafePointer<GLfloat>!) ``` |

Modified [glPointParameterxv(_: GLenum, _: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622785-glpointparameterxv)

|  | Declaration |
| --- | --- |
| From | ``` func glPointParameterxv(_ pname: GLenum, _ params: UnsafePointer<GLfixed>) ``` |
| To | ``` func glPointParameterxv(_ pname: GLenum, _ params: UnsafePointer<GLfixed>!) ``` |

Modified [glPointSizePointerOES(_: GLenum, _: GLsizei, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1622717-glpointsizepointeroes)

|  | Declaration |
| --- | --- |
| From | ``` func glPointSizePointerOES(_ type: GLenum, _ stride: GLsizei, _ pointer: UnsafePointer<Void>) ``` |
| To | ``` func glPointSizePointerOES(_ type: GLenum, _ stride: GLsizei, _ pointer: UnsafeRawPointer!) ``` |

Modified glProgramBinary(_: GLuint, _: GLenum, _: UnsafeRawPointer!, _: GLsizei)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramBinary(_ program: GLuint, _ binaryFormat: GLenum, _ binary: UnsafePointer<Void>, _ length: GLsizei) ``` |
| To | ``` func glProgramBinary(_ program: GLuint, _ binaryFormat: GLenum, _ binary: UnsafeRawPointer!, _ length: GLsizei) ``` |

Modified [glProgramUniform1fvEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623778-glprogramuniform1fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform1fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniform1fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniform1ivEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1623805-glprogramuniform1ivext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform1ivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLint>) ``` |
| To | ``` func glProgramUniform1ivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLint>!) ``` |

Modified [glProgramUniform1uivEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1623788-glprogramuniform1uivext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform1uivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glProgramUniform1uivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>!) ``` |

Modified [glProgramUniform2fvEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623769-glprogramuniform2fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform2fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniform2fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniform2ivEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1623880-glprogramuniform2ivext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform2ivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLint>) ``` |
| To | ``` func glProgramUniform2ivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLint>!) ``` |

Modified [glProgramUniform2uivEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1623831-glprogramuniform2uivext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform2uivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glProgramUniform2uivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>!) ``` |

Modified [glProgramUniform3fvEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623770-glprogramuniform3fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform3fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniform3fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniform3ivEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1623784-glprogramuniform3ivext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform3ivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLint>) ``` |
| To | ``` func glProgramUniform3ivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLint>!) ``` |

Modified [glProgramUniform3uivEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1623837-glprogramuniform3uivext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform3uivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glProgramUniform3uivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>!) ``` |

Modified [glProgramUniform4fvEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623804-glprogramuniform4fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform4fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniform4fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniform4ivEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1623791-glprogramuniform4ivext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform4ivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLint>) ``` |
| To | ``` func glProgramUniform4ivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLint>!) ``` |

Modified [glProgramUniform4uivEXT(_: GLuint, _: GLint, _: GLsizei, _: UnsafePointer<GLuint>!)](https://developer.apple.com/documentation/opengles/1623818-glprogramuniform4uivext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniform4uivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glProgramUniform4uivEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>!) ``` |

Modified [glProgramUniformMatrix2fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623814-glprogramuniformmatrix2fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix2fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix2fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniformMatrix2x3fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623845-glprogramuniformmatrix2x3fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix2x3fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix2x3fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniformMatrix2x4fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623794-glprogramuniformmatrix2x4fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix2x4fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix2x4fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniformMatrix3fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623873-glprogramuniformmatrix3fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix3fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix3fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniformMatrix3x2fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623806-glprogramuniformmatrix3x2fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix3x2fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix3x2fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniformMatrix3x4fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623812-glprogramuniformmatrix3x4fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix3x4fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix3x4fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniformMatrix4fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623777-glprogramuniformmatrix4fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix4fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix4fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniformMatrix4x2fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623786-glprogramuniformmatrix4x2fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix4x2fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix4x2fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glProgramUniformMatrix4x3fvEXT(_: GLuint, _: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1623887-glprogramuniformmatrix4x3fvext)

|  | Declaration |
| --- | --- |
| From | ``` func glProgramUniformMatrix4x3fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glProgramUniformMatrix4x3fvEXT(_ program: GLuint, _ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glPushGroupMarkerEXT(_: GLsizei, _: UnsafePointer<GLchar>!)](https://developer.apple.com/documentation/opengles/1614275-glpushgroupmarkerext)

|  | Declaration |
| --- | --- |
| From | ``` func glPushGroupMarkerEXT(_ length: GLsizei, _ marker: UnsafePointer<GLchar>) ``` |
| To | ``` func glPushGroupMarkerEXT(_ length: GLsizei, _ marker: UnsafePointer<GLchar>!) ``` |

Modified [glReadPixels(_: GLint, _: GLint, _: GLsizei, _: GLsizei, _: GLenum, _: GLenum, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/opengles/1617321-glreadpixels)

|  | Declaration |
| --- | --- |
| From | ``` func glReadPixels(_ x: GLint, _ y: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ pixels: UnsafeMutablePointer<Void>) ``` |
| To | ``` func glReadPixels(_ x: GLint, _ y: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ pixels: UnsafeMutableRawPointer!) ``` |

Modified glSamplerParameterfv(_: GLuint, _: GLenum, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glSamplerParameterfv(_ sampler: GLuint, _ pname: GLenum, _ param: UnsafePointer<GLfloat>) ``` |
| To | ``` func glSamplerParameterfv(_ sampler: GLuint, _ pname: GLenum, _ param: UnsafePointer<GLfloat>!) ``` |

Modified glSamplerParameteriv(_: GLuint, _: GLenum, _: UnsafePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glSamplerParameteriv(_ sampler: GLuint, _ pname: GLenum, _ param: UnsafePointer<GLint>) ``` |
| To | ``` func glSamplerParameteriv(_ sampler: GLuint, _ pname: GLenum, _ param: UnsafePointer<GLint>!) ``` |

Modified [glShaderBinary(_: GLsizei, _: UnsafePointer<GLuint>!, _: GLenum, _: UnsafeRawPointer!, _: GLsizei)](https://developer.apple.com/documentation/opengles/1617514-glshaderbinary)

|  | Declaration |
| --- | --- |
| From | ``` func glShaderBinary(_ n: GLsizei, _ shaders: UnsafePointer<GLuint>, _ binaryformat: GLenum, _ binary: UnsafePointer<Void>, _ length: GLsizei) ``` |
| To | ``` func glShaderBinary(_ n: GLsizei, _ shaders: UnsafePointer<GLuint>!, _ binaryformat: GLenum, _ binary: UnsafeRawPointer!, _ length: GLsizei) ``` |

Modified [glShaderSource(_: GLuint, _: GLsizei, _: UnsafePointer<UnsafePointer<GLchar>?>!, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617674-glshadersource)

|  | Declaration |
| --- | --- |
| From | ``` func glShaderSource(_ shader: GLuint, _ count: GLsizei, _ string: UnsafePointer<UnsafePointer<GLchar>>, _ length: UnsafePointer<GLint>) ``` |
| To | ``` func glShaderSource(_ shader: GLuint, _ count: GLsizei, _ string: UnsafePointer<UnsafePointer<GLchar>?>!, _ length: UnsafePointer<GLint>!) ``` |

Modified GLsync

|  | Declaration |
| --- | --- |
| From | ``` typealias GLsync = COpaquePointer ``` |
| To | ``` typealias GLsync = OpaquePointer ``` |

Modified glTexCoordPointer(_: GLint, _: GLenum, _: GLsizei, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glTexCoordPointer(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafePointer<Void>) ``` |
| To | ``` func glTexCoordPointer(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafeRawPointer!) ``` |

Modified glTexEnvfv(_: GLenum, _: GLenum, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glTexEnvfv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfloat>) ``` |
| To | ``` func glTexEnvfv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfloat>!) ``` |

Modified glTexEnviv(_: GLenum, _: GLenum, _: UnsafePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glTexEnviv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLint>) ``` |
| To | ``` func glTexEnviv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLint>!) ``` |

Modified [glTexEnvxv(_: GLenum, _: GLenum, _: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622766-gltexenvxv)

|  | Declaration |
| --- | --- |
| From | ``` func glTexEnvxv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfixed>) ``` |
| To | ``` func glTexEnvxv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfixed>!) ``` |

Modified [glTexImage2D(_: GLenum, _: GLint, _: GLint, _: GLsizei, _: GLsizei, _: GLint, _: GLenum, _: GLenum, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1617448-glteximage2d)

|  | Declaration |
| --- | --- |
| From | ``` func glTexImage2D(_ target: GLenum, _ level: GLint, _ internalformat: GLint, _ width: GLsizei, _ height: GLsizei, _ border: GLint, _ format: GLenum, _ type: GLenum, _ pixels: UnsafePointer<Void>) ``` |
| To | ``` func glTexImage2D(_ target: GLenum, _ level: GLint, _ internalformat: GLint, _ width: GLsizei, _ height: GLsizei, _ border: GLint, _ format: GLenum, _ type: GLenum, _ pixels: UnsafeRawPointer!) ``` |

Modified glTexImage3D(_: GLenum, _: GLint, _: GLint, _: GLsizei, _: GLsizei, _: GLsizei, _: GLint, _: GLenum, _: GLenum, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glTexImage3D(_ target: GLenum, _ level: GLint, _ internalformat: GLint, _ width: GLsizei, _ height: GLsizei, _ depth: GLsizei, _ border: GLint, _ format: GLenum, _ type: GLenum, _ pixels: UnsafePointer<Void>) ``` |
| To | ``` func glTexImage3D(_ target: GLenum, _ level: GLint, _ internalformat: GLint, _ width: GLsizei, _ height: GLsizei, _ depth: GLsizei, _ border: GLint, _ format: GLenum, _ type: GLenum, _ pixels: UnsafeRawPointer!) ``` |

Modified [glTexParameterfv(_: GLenum, _: GLenum, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617517-gltexparameterfv)

|  | Declaration |
| --- | --- |
| From | ``` func glTexParameterfv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfloat>) ``` |
| To | ``` func glTexParameterfv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfloat>!) ``` |

Modified [glTexParameteriv(_: GLenum, _: GLenum, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617318-gltexparameteriv)

|  | Declaration |
| --- | --- |
| From | ``` func glTexParameteriv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLint>) ``` |
| To | ``` func glTexParameteriv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLint>!) ``` |

Modified [glTexParameterxv(_: GLenum, _: GLenum, _: UnsafePointer<GLfixed>!)](https://developer.apple.com/documentation/opengles/1622737-gltexparameterxv)

|  | Declaration |
| --- | --- |
| From | ``` func glTexParameterxv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfixed>) ``` |
| To | ``` func glTexParameterxv(_ target: GLenum, _ pname: GLenum, _ params: UnsafePointer<GLfixed>!) ``` |

Modified [glTexSubImage2D(_: GLenum, _: GLint, _: GLint, _: GLint, _: GLsizei, _: GLsizei, _: GLenum, _: GLenum, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1617588-gltexsubimage2d)

|  | Declaration |
| --- | --- |
| From | ``` func glTexSubImage2D(_ target: GLenum, _ level: GLint, _ xoffset: GLint, _ yoffset: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ pixels: UnsafePointer<Void>) ``` |
| To | ``` func glTexSubImage2D(_ target: GLenum, _ level: GLint, _ xoffset: GLint, _ yoffset: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ pixels: UnsafeRawPointer!) ``` |

Modified glTexSubImage3D(_: GLenum, _: GLint, _: GLint, _: GLint, _: GLint, _: GLsizei, _: GLsizei, _: GLsizei, _: GLenum, _: GLenum, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glTexSubImage3D(_ target: GLenum, _ level: GLint, _ xoffset: GLint, _ yoffset: GLint, _ zoffset: GLint, _ width: GLsizei, _ height: GLsizei, _ depth: GLsizei, _ format: GLenum, _ type: GLenum, _ pixels: UnsafePointer<Void>) ``` |
| To | ``` func glTexSubImage3D(_ target: GLenum, _ level: GLint, _ xoffset: GLint, _ yoffset: GLint, _ zoffset: GLint, _ width: GLsizei, _ height: GLsizei, _ depth: GLsizei, _ format: GLenum, _ type: GLenum, _ pixels: UnsafeRawPointer!) ``` |

Modified glTransformFeedbackVaryings(_: GLuint, _: GLsizei, _: UnsafePointer<UnsafePointer<GLchar>?>!, _: GLenum)

|  | Declaration |
| --- | --- |
| From | ``` func glTransformFeedbackVaryings(_ program: GLuint, _ count: GLsizei, _ varyings: UnsafePointer<UnsafePointer<GLchar>>, _ bufferMode: GLenum) ``` |
| To | ``` func glTransformFeedbackVaryings(_ program: GLuint, _ count: GLsizei, _ varyings: UnsafePointer<UnsafePointer<GLchar>?>!, _ bufferMode: GLenum) ``` |

Modified [glUniform1fv(_: GLint, _: GLsizei, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617478-gluniform1fv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform1fv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniform1fv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLfloat>!) ``` |

Modified [glUniform1iv(_: GLint, _: GLsizei, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617393-gluniform1iv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform1iv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLint>) ``` |
| To | ``` func glUniform1iv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLint>!) ``` |

Modified glUniform1uiv(_: GLint, _: GLsizei, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform1uiv(_ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glUniform1uiv(_ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>!) ``` |

Modified [glUniform2fv(_: GLint, _: GLsizei, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617460-gluniform2fv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform2fv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniform2fv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLfloat>!) ``` |

Modified [glUniform2iv(_: GLint, _: GLsizei, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617688-gluniform2iv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform2iv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLint>) ``` |
| To | ``` func glUniform2iv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLint>!) ``` |

Modified glUniform2uiv(_: GLint, _: GLsizei, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform2uiv(_ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glUniform2uiv(_ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>!) ``` |

Modified [glUniform3fv(_: GLint, _: GLsizei, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617425-gluniform3fv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform3fv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniform3fv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLfloat>!) ``` |

Modified [glUniform3iv(_: GLint, _: GLsizei, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617225-gluniform3iv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform3iv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLint>) ``` |
| To | ``` func glUniform3iv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLint>!) ``` |

Modified glUniform3uiv(_: GLint, _: GLsizei, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform3uiv(_ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glUniform3uiv(_ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>!) ``` |

Modified [glUniform4fv(_: GLint, _: GLsizei, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617566-gluniform4fv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform4fv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniform4fv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLfloat>!) ``` |

Modified [glUniform4iv(_: GLint, _: GLsizei, _: UnsafePointer<GLint>!)](https://developer.apple.com/documentation/opengles/1617314-gluniform4iv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform4iv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLint>) ``` |
| To | ``` func glUniform4iv(_ location: GLint, _ count: GLsizei, _ v: UnsafePointer<GLint>!) ``` |

Modified glUniform4uiv(_: GLint, _: GLsizei, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniform4uiv(_ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>) ``` |
| To | ``` func glUniform4uiv(_ location: GLint, _ count: GLsizei, _ value: UnsafePointer<GLuint>!) ``` |

Modified [glUniformMatrix2fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617513-gluniformmatrix2fv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix2fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix2fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified glUniformMatrix2x3fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix2x3fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix2x3fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified glUniformMatrix2x4fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix2x4fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix2x4fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glUniformMatrix3fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617396-gluniformmatrix3fv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix3fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix3fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified glUniformMatrix3x2fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix3x2fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix3x2fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified glUniformMatrix3x4fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix3x4fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix3x4fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glUniformMatrix4fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617249-gluniformmatrix4fv)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix4fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix4fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified glUniformMatrix4x2fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix4x2fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix4x2fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified glUniformMatrix4x3fv(_: GLint, _: GLsizei, _: GLboolean, _: UnsafePointer<GLfloat>!)

|  | Declaration |
| --- | --- |
| From | ``` func glUniformMatrix4x3fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>) ``` |
| To | ``` func glUniformMatrix4x3fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!) ``` |

Modified [glVertexAttrib1fv(_: GLuint, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617573-glvertexattrib1fv)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexAttrib1fv(_ indx: GLuint, _ values: UnsafePointer<GLfloat>) ``` |
| To | ``` func glVertexAttrib1fv(_ indx: GLuint, _ values: UnsafePointer<GLfloat>!) ``` |

Modified [glVertexAttrib2fv(_: GLuint, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617479-glvertexattrib2fv)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexAttrib2fv(_ indx: GLuint, _ values: UnsafePointer<GLfloat>) ``` |
| To | ``` func glVertexAttrib2fv(_ indx: GLuint, _ values: UnsafePointer<GLfloat>!) ``` |

Modified [glVertexAttrib3fv(_: GLuint, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617226-glvertexattrib3fv)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexAttrib3fv(_ indx: GLuint, _ values: UnsafePointer<GLfloat>) ``` |
| To | ``` func glVertexAttrib3fv(_ indx: GLuint, _ values: UnsafePointer<GLfloat>!) ``` |

Modified [glVertexAttrib4fv(_: GLuint, _: UnsafePointer<GLfloat>!)](https://developer.apple.com/documentation/opengles/1617484-glvertexattrib4fv)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexAttrib4fv(_ indx: GLuint, _ values: UnsafePointer<GLfloat>) ``` |
| To | ``` func glVertexAttrib4fv(_ indx: GLuint, _ values: UnsafePointer<GLfloat>!) ``` |

Modified glVertexAttribI4iv(_: GLuint, _: UnsafePointer<GLint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexAttribI4iv(_ index: GLuint, _ v: UnsafePointer<GLint>) ``` |
| To | ``` func glVertexAttribI4iv(_ index: GLuint, _ v: UnsafePointer<GLint>!) ``` |

Modified glVertexAttribI4uiv(_: GLuint, _: UnsafePointer<GLuint>!)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexAttribI4uiv(_ index: GLuint, _ v: UnsafePointer<GLuint>) ``` |
| To | ``` func glVertexAttribI4uiv(_ index: GLuint, _ v: UnsafePointer<GLuint>!) ``` |

Modified glVertexAttribIPointer(_: GLuint, _: GLint, _: GLenum, _: GLsizei, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexAttribIPointer(_ index: GLuint, _ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafePointer<Void>) ``` |
| To | ``` func glVertexAttribIPointer(_ index: GLuint, _ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafeRawPointer!) ``` |

Modified [glVertexAttribPointer(_: GLuint, _: GLint, _: GLenum, _: GLboolean, _: GLsizei, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1617630-glvertexattribpointer)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexAttribPointer(_ indx: GLuint, _ size: GLint, _ type: GLenum, _ normalized: GLboolean, _ stride: GLsizei, _ ptr: UnsafePointer<Void>) ``` |
| To | ``` func glVertexAttribPointer(_ indx: GLuint, _ size: GLint, _ type: GLenum, _ normalized: GLboolean, _ stride: GLsizei, _ ptr: UnsafeRawPointer!) ``` |

Modified glVertexPointer(_: GLint, _: GLenum, _: GLsizei, _: UnsafeRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func glVertexPointer(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafePointer<Void>) ``` |
| To | ``` func glVertexPointer(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafeRawPointer!) ``` |

Modified glWaitSync(_: GLsync!, _: GLbitfield, _: GLuint64)

|  | Declaration |
| --- | --- |
| From | ``` func glWaitSync(_ sync: GLsync, _ flags: GLbitfield, _ timeout: GLuint64) ``` |
| To | ``` func glWaitSync(_ sync: GLsync!, _ flags: GLbitfield, _ timeout: GLuint64) ``` |

Modified [glWaitSyncAPPLE(_: GLsync!, _: GLbitfield, _: GLuint64)](https://developer.apple.com/documentation/opengles/1624698-glwaitsyncapple)

|  | Declaration |
| --- | --- |
| From | ``` func glWaitSyncAPPLE(_ sync: GLsync, _ flags: GLbitfield, _ timeout: GLuint64) ``` |
| To | ``` func glWaitSyncAPPLE(_ sync: GLsync!, _ flags: GLbitfield, _ timeout: GLuint64) ``` |

Modified [glWeightPointerOES(_: GLint, _: GLenum, _: GLsizei, _: UnsafeRawPointer!)](https://developer.apple.com/documentation/opengles/1622734-glweightpointeroes)

|  | Declaration |
| --- | --- |
| From | ``` func glWeightPointerOES(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafePointer<Void>) ``` |
| To | ``` func glWeightPointerOES(_ size: GLint, _ type: GLenum, _ stride: GLsizei, _ pointer: UnsafeRawPointer!) ``` |

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

---
title: 创建增强安全辅助扩展
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-enhanced-security-helper-extensions
source_url: 'https://developer.apple.com/documentation/xcode/creating-enhanced-security-helper-extensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-enhanced-security-helper-extensions.json'
content_hash: 'sha256:f66ff5b499f05a9c'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 创建增强安全辅助扩展

<sub>文章</sub>

减少攻击者通过你的 App 的扩展攻击它的机会。

## 概述

把敏感计算（例如处理来自不受信任来源的数据）分离到扩展中——由系统作为与你的 App 分开的进程来运行——能减少攻击者瞄准敏感计算、进而访问你的 App 或系统其他部分的机会。在 iOS、iPadOS 和 macOS 上创建增强安全（Enhanced Security）辅助扩展，以实施更严格的沙盒限制，并启用编译器与运行时安全防护。

### 在你的 App 中定义扩展点

向 App target 的构建设置中添加用户自定义构建设置 `EX_ENABLE_EXTENSION_POINT_GENERATION`，值为 `YES`。在你的 App 源码中，创建一个到 [AppExtensionPoint](../extensionfoundation/appextensionpoint.md) 的扩展，用它定义你的 App 的扩展点。给扩展点起一个你自定的 [AppExtensionPoint.Name](../extensionfoundation/appextensionpoint/name.md)，并加上 [AppExtensionPoint.EnhancedSecurity](../extensionfoundation/appextensionpoint/enhancedsecurity.md) 属性，告诉系统在增强安全运行时中运行你的扩展：

```swift
import ExtensionFoundation

extension AppExtensionPoint {
  @Definition
  static var exampleExtension: AppExtensionPoint {
    Name("exampleExtension")
    EnhancedSecurity()
  }
}
```

### 创建扩展

按以下步骤创建扩展：

1. 在 Xcode 中，选取 File \> New \> Target，选择 Generic Extension 模板。
2. 选择 Enhanced Security Extension 扩展类型，然后点按 Finish。
3. 在 Xcode 的项目导航器中，删除扩展 target 的 `Info.plist` 文件。
4. 在 target 构建设置编辑器中，删除扩展 target 的 `INFOPLIST_FILE` 构建设置。

编辑扩展的主源文件，让它所绑定的扩展点的 [AppExtensionPoint.Identifier](../extensionfoundation/appextensionpoint/identifier.md) 以你的 App 的 bundle ID 作为宿主标识符，并使用你在上一节中给扩展点起的名字：

```swift
import ExtensionFoundation

@main
struct MyAppHelper: ExampleExtension {
  @AppExtensionPoint.Bind
  var boundExtensionPoint: AppExtensionPoint {
    AppExtensionPoint.Identifier(host: "com.example.my-app", name: "exampleExtension")
  }
}
```

编写实现扩展行为的代码。系统在一个沙盒中运行你的扩展，该沙盒限制了对大多数系统服务和框架的访问。特别地，你的扩展无法呈现 UI；它必须与宿主 App 通信，请 App 代替它呈现 UI 并与其他系统服务交互。

### 发现并启动扩展

在你的 App 中，创建一个 [AppExtensionPoint.Monitor](../extensionfoundation/appextensionpoint/monitor.md) 来发现增强安全扩展：

```swift
let monitor = try await AppExtensionPoint.Monitor(appExtensionPoint: AppExtensionPoint.exampleExtension)
guard let identity = monitor.identities.first else {     
   fatalError("Extension not found")
} 
```

`identity` 代表你在上一节创建的增强安全扩展的 bundle。用这个 bundle 创建一个 [AppExtensionProcess](../extensionfoundation/appextensionprocess.md) 来启动扩展：

```swift
do {
  self.process = try await AppExtensionProcess(configuration: .init(appExtensionIdentity: identity, onInterruption: {
    // 系统会在扩展退出时调用这个闭包。
  }))
  // 与扩展通信。
}
catch let error {
  // 系统无法启动扩展。
}
```

### 在 App 与扩展之间通信

使用 [XPCSession](../xpc/xpcsession.md) 处理 App 与其增强安全扩展之间的通信。更多信息参见[创建 XPC 服务](../xpc/creating-xpc-services.md)。

在 App 与扩展共享的代码中定义遵循 [Codable](../swift/codable.md) 的结构体，并创建这些结构体的实例，通过你创建的会话经 XPC 发送：

```swift
struct Message: Identifiable, Codable {
  var id: String
  // 添加表示你的 App 发送给扩展的数据的属性。

  struct Response: Codable {
    // 定义扩展在回复中发回 App 的另一个结构体。
  }
}
```

在 App 中调用 [makeXPCSession()](<../extensionfoundation/appextensionprocess/makexpcsession().md>) 创建一个用于向扩展发送消息的 `XPCSession`：

```swift
do {
  self.xpcSession = try process.makeXPCSession()
  try xpcSession.activate()
  // 向扩展发送消息。
}
catch let error {
  // 系统无法创建 XPC 会话。
}
```

用你创建的会话向扩展发送消息并接收响应：

```swift
let response = try await withCheckedThrowingContinuation { continuation in
  do {
    // 构造 App 发送给扩展的消息。
    let message = Message()
    try xpcSession.send(Message()) { result in
      switch result {
      case .success(let reply):
        let response = (try? reply.decode(as: Message.Response.self)) ?? /* 创建一个默认响应。 */
        continuation.resume(returning: response)
      case .failure(let error):
        continuation.resume(throwing: error)
      }
    }
  }
  catch {
    continuation.resume(throwing: error)
  }
}
// 解读来自扩展的响应。
```

在扩展中，创建一个 [ConnectionHandler](../extensionfoundation/connectionhandler.md) 来接受来自 App 的连入连接。调用 [init(onSessionRequest:)](<../extensionfoundation/connectionhandler/init(onsessionrequest_).md>) 初始化方法，并在闭包中接受 XPC 连接、创建会话。

```swift
extension ExampleExtension {
    var configuration: some AppExtensionConfiguration {
        // 应请求返回你的扩展的配置。
        return ConnectionHandler(onSessionRequest: { request in
            let handler = MessageHandler(appExtension: self)
            return request.accept { session in
                return handler
            }
        })
    }
}
 
fileprivate struct MessageHandler<E: ExampleExtension>: XPCPeerHandler, Sendable {
    let appExtension: E
     
    func handleIncomingRequest(_ message: Message) -> (any Encodable)? {
        // 处理收到的消息。
        return Message.Response()
    }
}

```

### 采用其他安全加固特性

增强安全扩展与采用增强安全能力（Enhanced Security capability）的 App 使用相同的编译器和运行时安全特性。更多信息参见[为你的 App 启用增强安全性](enabling-enhanced-security-for-your-app.md)。

## 另请参阅

### 安全与隐私

- [验证 XCFramework 的来源](verifying-the-origin-of-your-xcframeworks.md) — 发现框架的签名者，并在其发生变化时采取行动。
- [为你的 App 启用增强安全性](enabling-enhanced-security-for-your-app.md) — 检测越界内存访问、已释放内存的使用及其他潜在漏洞。
- [采用类型感知内存分配](adopting-type-aware-memory-allocation.md) — 减少把代码中的指针当作数据来处理的机会。
- [遵循 Mach IPC 安全限制](conforming-to-mach-ipc-security-restrictions.md) — 避免与 Mach 消息相关的崩溃和潜在不安全情形。

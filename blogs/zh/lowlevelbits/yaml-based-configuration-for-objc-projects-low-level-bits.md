---
title: 基于 YAML 的 ObjC 项目配置方法 - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/yaml-based-configuration-for-objc-projects/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2ad8fce4a5743154'
translated: true
---

> 原文：[YAML-based Configuration for ObjC Projects - Low Level Bits 🇺🇦](https://lowlevelbits.org/yaml-based-configuration-for-objc-projects/)　·　Low Level Bits (Alex Denisov)

# 基于 YAML 的 ObjC 项目配置方法

_发表于 2015 年 2 月 6 日_

几乎每个 iOS 或 OS X App 都要处理配置，比如服务器地址、分析服务的 API 密钥等等。这些配置在开发环境和生产环境中通常是不同的，例如：`[https://staging.example.com](https://staging.example.com)` 和 `[https://example.com](https://example.com)`。我们的工具链并没有为这个问题提供很好的解决方案，所以需要自己来实现。

我在使用 Ruby On Rails 时，非常喜欢它的数据库配置方式：

```yaml
development:
  user: dev
  password: dev123
# ...
production:
  user: root
  password: supersecurepassword
# ...
```

我希望能在日常的 iOS 开发中也能用同样的方式。

幸运的是，我可以！

**TL;DR;**

请查看项目 [xcconf](https://github.com/AlexDenisov/xcconf) 和 `Sample/Sample.xcodeproj`。

### 常用的机制

至少有两种常用的方法来分离配置：预处理器定义（preprocessor definition）和 plist 文件。两者都有严重的缺点。

#### 预处理器定义

你可能见过甚至用过这种方法。它相当简单易用：

```objectivec
#ifdef DEBUG
NSString *const kServerAddress = @"https://staging.example.com";
#else
NSString *const kServerAddress = @"https://example.com";
#endif
```

但是假设你要增加一个环境，例如为 Beta 测试者增加“Beta”环境。这意味着你必须添加新的预处理器定义并更新所有常量声明。而且，这种方法容易出错：很容易打错字或“意外”删除一个定义。你的代码仍然可以编译，但会使用错误的环境。不过，这种方法至少有一个优点：你的代码只包含你需要的内容，所有私有数据（地址、密钥）都不会暴露。

#### Plist 文件

这是另一种常用的机制。这种方法在[此处](http://code.tutsplus.com/tutorials/ios-quick-tip-managing-configurations-with-ease--mobile-18324)有描述。它也有一些缺点：如果你想添加新的配置变量，必须把它加到每个小节中，还需要向类中添加一个属性并编写（复制粘贴？）初始化代码。此外，你所有的密钥和端点都会分发给最终用户，或者你必须在部署到 App Store 之前清理这个文件。尽管如此，对于这样一个简单的任务，你需要执行的操作还是太多了。

谢天谢地，有一种更简单、更健壮的方法。

### XCCONF 和 YAML

[xcconf](https://github.com/AlexDenisov/xcconf) 整合了前面所述方法的所有优点：

- 所有设置存放在一个地方
- 不暴露私有数据
- 所有工作在编译时完成

##### 它看起来是这样的：

配置文件：

```yaml
principalClass: Configuration

Debug:
  serverAddress: https://staging.example.com
  APIKey: qwe123!!qwe

Release:
  serverAddress: https://example.com
  APIKey: qwe123qwe
```

ObjC 代码：

```objectivec
@Interface Configuration : NSObject
- (NSString *)serverAddress;
- (NSString *)APIKey;
@end

// ...

Config *config = [Config new];
NSLog(@"%@", config.serverAddress);
```

无需预处理器，没有样板代码！

#### 安装和使用

要安装 `xcconf`，你需要克隆仓库并运行一条命令，它会构建可执行文件并安装到 `/usr/local/bin` 中：

```bash
git clone [email protected]:AlexDenisov/xcconf.git && cd xcconf
make install
```

集成到项目中看起来有点奇怪，但别担心，这是正常的 :)

首先，创建一个 YAML 文件，例如：`config.yaml`

![新建文件](https://lowlevelbits.org/img/yaml-based-configuration/new_file.png)

将初始配置放入其中：

```yaml
principalClass: Config

Debug:
  color: Green

Release:
  color: Blue
```

准备配置的类接口。**但不要创建实现**。它的名称应该与 `principalClass` 相同，并且可以包含所有可用参数的 getter 方法，在这个例子中就是 `color`：

```objectivec
@interface Config : NSObject
- (NSString *)color;
@end
```

现在编译我们的配置，前往 `Build Phases` -> `Compile Sources` -> `+`，然后添加 `config.yaml`：

![编译 YAML](https://lowlevelbits.org/img/yaml-based-configuration/compile_yaml.png)

显然 Xcode 没有 YAML 编译器，但我们可以提供自己的。打开 `Build Rules`，添加一条新规则，匹配模式为 `*.yaml` 的文件，并运行 shell 命令 `/usr/local/bin/xcconf`。同时，我们需要指定输出文件，否则它将无法工作：`$(DERIVED_FILE_DIR)/xcconf.m`。请确保输出文件的扩展名是 `.m`，这样 Xcode 就可以编译它，并为 `principalClass` 提供实现。

![xcconf](https://lowlevelbits.org/img/yaml-based-configuration/xcconf.png)

现在我们可以使用它了：

```objectivec
#import "Config.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        Config *config = [Config new];
        NSLog(@"%@", config.color);
    }
    return 0;
}
```

构建并运行：

![输出](https://lowlevelbits.org/img/yaml-based-configuration/output.png)

### 总结

这个项目还很年轻，我一天前才开始，所以它可能会有（它肯定有）一些问题，还可以改进。

非常感谢任何反馈。

P.S. 欢迎提交 Pull Request！:)

</SOURCE>

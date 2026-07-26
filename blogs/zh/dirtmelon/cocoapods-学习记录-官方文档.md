---
title: CocoaPods 学习记录 - 官方文档
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/cocoapods-first/'
original_language: zh
published: 2021-03-13
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ae61e62a57cf959d'
translated: n/a
---

> 原文：[CocoaPods 学习记录 - 官方文档](https://dirtmelon.github.io/posts/cocoapods-first/)　·　dirtmelon

CocoaPods 的官方文档写得比较详细，建议都过一遍，以免用错方法和漏掉一些可以提高效率的小技巧。

## pod install vs pod update

[CocoaPods Guides - pod install vs. pod update](https://guides.cocoapods.org/using/pod-install-vs-update.html)

很多人都认为只有在第一次配置 CocoaPods 时才使用 `pod install` ，后面都是使用 `pod update` ，然而事实并非如此。

TL;DR:

- 来下载新的 pods ，即使你已经有

  且之前已经执行过

  。就算只是给已使用 CocoaPods 的项目添加或者移除 pods ，也是执行

  ；
- 。

`pod install` ：

- 来下载和安装新的 pods 时，它都会把新的 pods 对应的版本和名字写进

  中，以此来锁定 pods 的版本；
- 时，它只会解析没有

  中没有出现过的 pods 依赖：

    - 中有出现，它就会下载

      中对应的版本，不去检查是否有更新的版本；
    - 中没有出现，它就会去搜索

      中所匹配的版本，例如

      。

通过 `pod outdated` 可以检查是否有更新的版本。

当执行 `pod update PodNAME` 时， CocoaPods 会尝试在匹配 `Podfile` 中版本条件的前提下更新至最新版本，而不是直接使用 `Podfile.lock` 的版本。如果说执行 `pod update` 时没有输入 `PODNAME` ，那么 CocoaPods 会更新 `Podfile` 中所有 pod 版本。只有在想要更新某个 pod 的版本时才使用 `pod update PODNAME` ，否则使用 `pod install` ， `pod install` 不会更新已经安装的 pod 。

当添加一个 pod 到 `Podfile` 时，应该执行 `pod install` 而不是 `pod update` ，以免同时更新其它的库。把 `Podfile.lock` 提交到代码仓库中，以此来锁定 pod 库的版本。

咋一看只使用 `Podfile` 应该足够获取 pod 库的精确版本了，其实不然。像是在 `Podfile` 中指定版本 `pod ‘A’, ’1.0.0’` ，不管是 `pod install` 或者 `pod update` 都会更新其它 pod 的版本，因为它们已经在 `Podfile` 中指定版本了。 假设有 pod `A` 依赖了 pod `A2` ，声明在 `A.podspec` 中： `dependency ‘A2’, ‘~> 3.0’` 。在这个例子中，通过 `pod ‘A’, ‘1.0.0’` 可以指定所有成员都使用 pod `A` 的 `1.0.0` 版本，但是：

- 是 3.4 版本，因为这是

  的最新版本；
- 时，他下载的 pod

  库版本是 3.5 ，因为

  后面可能会放了一个新的版本处理。

所以需要通过 `Podfile.lock` 来指定所有依赖库的版本，这样就可以确保所有人的依赖库版本都是一致的。 团队成员之间合理使用 `pod install` 和 `pod update` 可以大大提高开发效率。

## Using CocoaPods

[CocoaPods Guides - Using CocoaPods](https://guides.cocoapods.org/using/using-cocoapods.html)

是否需要把 `Pods` 目录添加到版本管理记录中。 Cocoapods 官方推荐说不要把 `Pods` 目录添加到 `.gitignore` 中，但是就一般大型项目来说都会把 `Pods` 目录添加到 `.gitignore` 中，否则整个 Git 仓库会非常大。

把 `Pods` 目录添加到记录中的好处：

- 和连接网络；
- 即使 Pod 的源（例如 Github ）挂掉了，项目中的 Pod 库也还可以使用；
- Pod 库中的代码可以保证一致。

忽略掉 `Pods` 目录的好处：

- 仓库会占用更小的空间；
- 只要 Pods 的源可用， CocoaPods 就可以执行相同的安装过程；
- 库不会有冲突。

## Using a Gemfile

[CocoaPods Guides - Using a Gemfile](https://guides.cocoapods.org/using/a-gemfile.html)

CocoaPods 借鉴了很多版本管理工具的思想，比如说 [RubyGems](https://rubygems.org/) ， [Bundler](http://bundler.io/) ， [npm](https://www.npmjs.com/) 和 [Gradle](http://gradle.org/) 。通过 `RubyGems` 加 `Bundler` 可以给应用设置特定的环境，指定库的版本。其用法和 `CocoaPods` 类似，通过 `Gemfile` 来进行配置，然后执行 `bundle install` 来获取对应的库。一个 `Gemfile` 的写法也和 `Podfile` 类似：

```ruby
source 'https://rubygems.org'

gem 'cocoapods'
gem 'cocoapods-keys'

gem 'fui', '~> 0.3.0'
gem 'xcpretty'
gem 'second_curtain', '~> 0.2.3'
gem 'fastlane'
```

执行完 `bundle install` 之后， `Gemfile` 相关的命令都需要加上 `bundle exec` ，比如说 `pod XX YY` 需要改为 `bundle exec pod XX YY` 。

[为什么我们要使用 RVM / Bundler ？](https://juejin.cn/post/6844903745822670861)

可以通过安装 [rubygems-bundler](https://github.com/rvm/rubygems-Bundler) 来避免每次都要输入 `bundle exec` ， 1.11.0 以上的 RVM 版本在安装 Ruby 时会默认安装 `rubygems-Bundler` ，可以通过 `gem list rubygems-Bundler` 来检查是否安装了这个 Gem 。

[Bundler Version Autoswitch](https://bundler.io/v2.2/guides/bundler_2_upgrade.html#version-autoswitch)

如果你安装了 Bundler 2 ，那么 Bundler 会根据 `Gemfile.lock` 中的版本自动进行切换。如果你的 lockfile 是使用 Bundler 1 进行创建，那么就会使用 Bundler 1 运行，如果是使用 Bundler 2 创建，那么就会使用 Bundler 2 运行。例如下面的 `Gemfile.lock` 是使用 Bundler 1.17.1 创建：

```ruby
GEM
  remote: https://rubygems.org/
  specs:
    rack (2.0.6)

PLATFORMS
  ruby

DEPENDENCIES
  rack

BUNDLED WITH
   1.17.1
```

Bundler 会读取 `BUNDLED WITH` 的区域来决定使用哪个版本，运行以下命令可以查看所使用的 Bundler 版本：

```ruby
$ grep -A 1 "BUNDLED WITH" Gemfile.lock
BUNDLED WITH
   1.17.1

$ bundle version
Bundler version 1.17.1
```

如果 Gemfile 是使用 Bundler 2 创建或者经由开发者手动从 Bundler 1 升级到 Bundler 2 ，那么就会使用 Bundler 2 版本运行：

```ruby
$ grep -A 1 "BUNDLED WITH" Gemfile.lock
BUNDLED WITH
   2.0.0

$ bundle version
Bundler version 2.0.0
```

而在应用环境外运行时，则会使用已安装的最新版本：

```ruby
$ ls -a
.	..

$ bundle version
Bundler version 2.0.0
```

## How to use CocoaPods plugins

[CocoaPods Guides - How to use CocoaPods plugins](https://guides.cocoapods.org/plugins/setting-up-plugins.html)

CocoaPods 不仅提供了依赖库版本管理的功能，还提供了插件功能，社区也提供了不少插件，以此来提高开发效率。

CocoaPods 插件能做什么：

- 过程，包括

  前和

  后；
- 子命令；
- Ruby 是门动态语言，受益于此，插件可以做任何你想做的事情。

通过 `Gemfile` 可以安装插件，安装 [cocoapods-repo-update](https://github.com/wordpress-mobile/cocoapods-repo-update)：

```ruby
source 'https://rubygems.org'

gem 'cocoapods'
gem 'cocoapods-repo-update'
gem 'fastlane'
```

然后修改 `Podfile` 添加对应的插件：

```ruby
platform :ios, '9.0'
plugin 'cocoapods-repo-update'

use_frameworks!

# OWS Pods
pod 'SignalCoreKit', git: 'https://github.com/signalapp/SignalCoreKit.git', testspecs: ["Tests"]
```

然后运行 `bundle exec pod install` 来运行插件。

通过 [Check](https://github.com/square/cocoapods-check) 插件可以优化 CI 的时间，三方库比较多时 `pod install` 可以需要耗费较多的时间，为了减少这部分的时间损耗，可以通过 `pod check` 来判断是否需要执行 `pod install` ，完整命令如下：

```ruby
bundle exec pod check || bundle exec pod install
```

通过 [leavez/cocoapods-binary](https://github.com/leavez/cocoapods-binary) 预编译库来减少编译时间。在执行 `pod install` 之后，即使 `Pods` 没有任何改变， Xcode 仍然会重新编译所有的库。 `cocoapods-binary` 通过在 `pod install` 时期就执行预编译，生成二进制资源比如说 `.framework` ，然后 Xcode 直接使用二进制资源而不是源码。这个流程如下：

1. 拉取需要预编译的 pods ；
2. 编译这些 pods ；
3. 文件，从指向源码改为指向编译好的 frameworks 。

可以通过一下方式来指定需要使用预编译的 pods ：

```ruby
 plugin 'cocoapods-binary'
  use_frameworks!

  target "HP" do
-      pod "ExpectoPatronum"
+      pod "ExpectoPatronum", :binary => true
  end
```

## Podfile 和 Podspec 语法

Podfile 用于描述一个或者多个 Xcode 项目中的 targets 依赖和一些配置，Podfile 文件可以非常简单：

```ruby
target 'MyApp'
pod 'AFNetworking', '~> 1.0'
```

也可以很复杂，一般大工程都会在 Podfile 干各种事情和 hook 操作。[CocoaPods Guides - Podfile Syntax Reference](https://guides.cocoapods.org/syntax/podfile.html#podfile) 详细说明了 Podfile 的相关语法。熟悉 Podfile 语法后，可以借助 Podfile 来干不少事情，比如说添加自定义的脚本：

```ruby
script_phase :name => 'HelloWorldScript', :script => 'echo "Hello World"'
script_phase :name => 'HelloWorldScript', :script => 'puts "Hello World"', :shell_path => '/usr/bin/ruby'
```

使用插件：

```ruby
plugin 'cocoapods-keys', :keyring => 'Eidolon'
plugin 'slather'
```

`hook pre_install` ，执行时机为 pods 完成下载但是还没安装：

```ruby
# installer 为 Pod::Installer
pre_install do |installer|
  # Do something fancy!
end
```

`hook post_install` 用于配置生成 Xcode 项目的相关配置，或者执行其它一些任务：

```ruby
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['GCC_ENABLE_OBJC_GC'] = 'supported'
    end
  end
end
```

Podspec 文件则用于描述 pod 库的配置， `source` ， `files` ， `build settings` 等等，都可以进行配置。[CocoaPods Guides - Podspec Syntax Reference](https://guides.cocoapods.org/syntax/podspec.html) 这里有列出 Podspec 文件支持的配置。 Podspec 可以很简单，也可以很复杂。由于 CocoaPods 在生成 pod 库对应的 Target 时是根据 Podspec 文件来生成的，所以 Xcode 的 编译属性也有支持。Podspec 在指定配置相关的文件时也支持进行格式匹配：[group_file_patterns](https://guides.cocoapods.org/syntax/podspec.html#group_file_patterns) 。

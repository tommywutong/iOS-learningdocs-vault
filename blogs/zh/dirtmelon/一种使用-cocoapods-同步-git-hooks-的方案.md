---
title: 一种使用 CocoaPods 同步 Git hooks 的方案
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/cocoapods-sync-githooks/'
original_language: zh
published: 2021-05-23
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:90849e8fdf4ad8b1'
translated: n/a
---

> 原文：[一种使用 CocoaPods 同步 Git hooks 的方案](https://dirtmelon.github.io/posts/cocoapods-sync-githooks/)　·　dirtmelon

## Git hooks 是什么

Git hooks 是一段脚本，可以在 Git 执行某些操作之前或者之后执行，比如说 commit ， push 或者 receive 。随便打开某个 Git 项目的目录，可以在 `.git/hooks` 这个目录下看到 Git hooks 的示例代码，不过都是以 `.sample` 后缀结尾，需要把 `.sample` 去掉后才会生效。

Git hooks 可以使用多种语言编写，包括 Shell ， Ruby ， Perl 和 Python 等。如果想要跳过 Git hooks 的检查，可以在执行 Git 命令时添加 `—no-verify` 参数，那么就算 Git hooks 失败，命令也会继续执行。但是必须要清楚明白跳过 Git hooks 的后果。

### Git hooks 作用

Git-SCM [Git - Git Hooks](http://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) 详细说明了各种 hooks 的类型，同时也提供了中文版本 [Pro Git - Git hooks](https://www.progit.cn/#_git_hooks) 。 常用的 hooks ：

- `pre-commit` ：执行 `git commit` 时触发，可以用于代码规范等，就 iOS 来说，如果团队间禁止使用 `xib` 或者 `storyboard` ，那么在 `commit` 时可以检测是否有 `xib` 或者 `storyboard` 文件。也可以用于资源大小的检测，可以设置图片资源大小不能超过某个尺寸；
- `prepare-commit-msg` ： 在执行 `git commit` 时会调用，可用于提供 `commit` 信息的模版；
- `commit-msg` ：在完成 `commit message` 编写和提交后出发，可用于校验 `commit` 的说明是否符合规范，结合 `prepare-commit-msg` 可以在团队间设置 `commit` 信息的规范；
- `post-commit` ：在完成 `commit` 之后执行，不接受任何参数，但是可以通过 `git log -1 HEAD` 来获取最后一次的提交信息，可以用于发送邮件提醒之类。

## 同步问题

Git hooks 所在目录 `.git/hooks` 不会被 Git 记录，所以只能通过其它工具来辅助同步。比较粗糙的方法是把 Git hooks 脚本放到另外一个 Git 仓库下，然后通知团队的其他成员进行同步。每次有改动时再手动进行同步。这种方法一听起来就比较粗糙，于是各种包管理工具和语言就开发出自己的 Git hooks 管理工具，比如说 [husky](https://github.com/typicode/husky) 。

CocoaPods 也有一个插件用于管理 Git hooks 脚本：[cocoapods-githooks](https://github.com/VladKorzun/cocoapods-githooks) ，但是这个插件有以下几个问题：

1. Git hooks 脚本和仓库绑定在一起，无法在各个项目间共享；
2. 所有 Git hooks 脚本都放在同一个文件中，无法根据不同的功能进行组装。

## 新的插件

其实 CocoaPods 已经为我们提供了包管理功能，所以我们可以通过 Podfile 来使用和管理不同的 Git hooks 脚本。 首先通过 CocoaPods 的 `plugin` 命令来创建插件：

```shell
pod plugins create cocoapods-sync-githooks
```

## 原理解析

CocoaPods 为插件提供了 `post_install` 和 `post_update` 的 hook 入口，所以插件可以通过注册对应 `hook_name` 来在 `pod install` 和 `pod update` 时进行一些操作，这部分代码添加在 `cocoapods_plugin.rb` 中：

```ruby
require 'cocoapods-sync-githooks/command'
require 'cocoapods-sync-githooks/sync_githooks'

module CocoapodsGitHooks
  Pod::HooksManager.register('cocoapods-sync-githooks', :post_install) do |context|
    CocoapodsGitHooks::GitHooksManager.sync
  end
  Pod::HooksManager.register('cocoapods-sync-githooks', :post_update) do |context|
    CocoapodsGitHooks::GitHooksManager.sync
  end
end
```

`cocoapods_plugin.rb` 对应实现：

```ruby
def sync
    Pod::UI.message 'Start syncing Git Hook' do
		# 1. 校验是否有 .git 目录
      return unless validate_git_directory?
		# 2. 如果没有 .git/hooks 目录，就主动创建
      FileUtils.mkdir '.git/hooks' unless File.directory?('.git/hooks')

		# 3. 找到对应的 Githooks 库
      abstract_target = abstract_target_of_githooks
      return if abstract_target.nil?
      dependencies = dependencies_in_target(abstract_target)
      if dependencies.nil? || dependencies.empty?
        Pod::UI.warn 'The dependencies of SyncGithooks is nil or empty.'
        return
      end
      dependencies.each { |dependency|
        Pod::UI.message "- #{dependency.name}"
      }
		#4. 开始同步
      sync_githooks_in_dependencies(dependencies)
    end
    Pod::UI.message 'Githooks are synced'
  end
end
```

为了区分普通的 Pod 库和 Git hooks 专用 Pod 库， Podfile 中需要新增一个 `Githooks` 的 `abstract_target` ，所有 Git hooks 相关库都放到这个 target 下。

```ruby
# @return [TargetDefinition]
def abstract_target_of_githooks
  abstract_target = nil
	# 通过 Podfile 来获取所有 target
  podfile = Pod::Config.instance.podfile
  podfile.target_definition_list.each do |target|
    if target.name == 'Githooks'
      abstract_target = target
      break
    end
  end unless podfile.target_definition_list.nil?

  if abstract_target.nil?
    Pod::UI.puts 'The abstract_target of SyncGithooks is not defined.'
    return nil
  end
	# 找到 Githooks 的 target
  abstract_target
end
```

找到 `GitHooks` 对应的库后，开始同步 Git hooks 脚本到 `.git/hooks` 目录下。 `sync_githooks_in_dependencies` 写得有点长，会分成两部分来说明：

```ruby
# @return [Array<String>]
def hook_types
  %w(applypatch-msg commit-msg fsmonitor-watchman post-update pre-applypatch pre-commit pre-merge-commit pre-push pre-rebase prepare-commit-msg push-to-checkout)
end

def sync_githooks_in_dependencies(dependencies)
  pods_directory = "#{Dir.pwd}/Pods"
  hook_dependencies = Hash.new([])
  dependencies.each do |dependency|
	  # 1. 由于 `dependency` 为 `local pod` 时对应的目录为 Pod 库自己所在的目录，
	  #    所以 `dependency_directory` 需要判断一下是否为 `local` ，如果是 `local` 就使用 `external_source[:path]` ，
	  #    否则使用 `pods_directory` 和 `dependency.name` 来拼成对应的目录
    dependency_directory = if dependency.local?
                             File.expand_path(dependency.external_source[:path])
                           else
                             "#{pods_directory}/#{dependency.name}"
                           end
    hook_types.each { |hook_type|
      # 2. 如果 `dependency` 对应的目录下 （ `githooks` ）中有对应类型的脚本，就把 `dependency` 添加到 `hook_dependencies[hook_type]` 中
      file_path = "#{dependency_directory}/githooks/#{hook_type}"
      if File.exist?(file_path)
        hook_dependencies[hook_type] += [dependency]
      end
    }
  end
	# ...
end
```

收集好对应的 Git hooks 脚本后就可以开始同步：

```ruby
git_hook_directory = '.git/hooks'
hook_dependencies.each_pair { |key, dependencies|
  file_path = "#{git_hook_directory}/#{key}"

	# 1. 先删除原有的 Git hook 对应类型的脚本
  File.delete(file_path) if File.exist?(file_path)

  File.new(file_path, 'w')
  File.open(file_path, File::RDWR) do |file|
    # 2. 设置语言环境，以便可以直接执行语言
    file.write("#!/bin/sh\n")
    file.write("#!/usr/bin/env ruby\n")
    file.write("#!/usr/bin/env python\n")

    dependencies.each do |dependency|
      dependency_directory = if dependency.local?
                               File.expand_path(dependency.external_source[:path])
                             else
                               "#{pods_directory}/#{dependency.name}"
                             end
		# 3. 获取对应类型的 Git hook 脚本目录
      hook_file_path = "#{dependency_directory}/githooks/#{key}"

      file.write("# #{dependency.name} githook\n")
		# 4. 生成对应的脚本方法，同步 Git hook 库的脚本到方法中
      file.write("if [ -f \"#{hook_file_path}\" ]; then\n")
      file.write("  function #{dependency.name}(){\n")
      file.write("    local script_directory=#{dependency_directory}/scripts\n")
      File.readlines(hook_file_path).each { |line|
        file.write("    #{line}")
      }
      file.write("\n  }\n")
		# 5. 执行对应的方法
      file.write("  #{dependency.name}\n")
      file.write("fi\n")
    end

    FileUtils.chmod('+x', file_path)
  end
}
```

为了保证 Git hook 源脚本的简洁，插件提供了执行 `scripts` 中脚本的方法， Git hook 库的可以直接调用 `scripts` 中的脚本，[githooksA/pre-commit](https://github.com/dirtmelon/githooksA/blob/master/githooks/pre-commit)：

```shell
export LC_ALL=en_US.UTF-8
set -eu
ruby ${script_directory}/Test.rb
```

上面提到 `local pod` 时对应的 Pod 库目录会不同，所以提供了 `${script_directory}` 变量，通过 `${script_directory}` 不管是否为 `local pod` 都可以访问到对应的 Git hooks 的 `script` 目录。

## 相关

插件地址：

[GitHub - dirtmelon/cocoapods-sync-githooks](https://github.com/dirtmelon/cocoapods-sync-githooks)

Demo 地址：

[GitHub - dirtmelon/githooksA](https://github.com/dirtmelon/githooksA)

[GitHub - dirtmelon/githooksB](https://github.com/dirtmelon/githooksB)

[GitHub - dirtmelon/SyncGithooksDemo](https://github.com/dirtmelon/SyncGithooksDemo)

延伸阅读：

[Git Hooks

Learn how to use pre-commit hooks, post-commit hooks, post-receive hooks, and more.](https://githooks.com/)

[Pro Git](https://www.progit.cn/#_pro_git)
